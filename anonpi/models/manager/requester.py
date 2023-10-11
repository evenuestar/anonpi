import json
import http.client
import typing as t
import socket
from urllib.parse import urlparse as up


class RequestCooker:
    class ReqMapper(json.JSONEncoder):
        def __init__(self, data: dict):
            super().__init__()
            try:
                self.encode(data)
            except:
                raise TypeError("data must be instance of dict")
            self.data = data

        def __str__(self):
            return json.JSONEncoder().encode(self.data)

        @property
        def to_dict(self):
            return self.data

    @classmethod
    def cook_request(cls, ob=None, path=None, body=None, rname=None, **kwargs):
        if rname:
            if kwargs.get("url") is None:
                raise ValueError("url must be provided")
            h, p, e, c = RequestCooker.cls_url(kwargs.get("url"))
            _new_in = type("RequestWrapper", (http.client.HTTPConnection if
                                              c == 'http' else http.client.HTTPSConnection,), {})
            _rwar = _new_in(h, p, timeout=5)
            setattr(_rwar, "prepare_request", cls.prepare_request)
            _rwar._hd, _rwar._bd, _rwar._mt, _rwar._url = cls.ReqMapper(
                {}), cls.__cook_body({}), "GET", e
            return _rwar

        from anonpi import api_key as key, api_base as base
        if key is None:
            raise ValueError("""anonpi.api_key must be set
            >>> import anonpi
            >>> anopi.api_key = <ANONPI_API_KEY>
            Please visit https://docs.anonpi.co to read docs""")
        _url, __mt = "", ""
        _url, __mt = getattr(ob, path)()
        _rwar = ""
        try:
            _rwar = getattr(cls, "cooked_request")
        except AttributeError:
            _rwar, e = cls.__cook_request(base)
        _rwar, e = getattr(cls, "cooked_request")
        setattr(_rwar, "prepare_request", cls.prepare_request)
        _rwar._hd, _rwar._bd, _rwar._mt, _rwar._url = cls.__cook_headers(
            key), cls.__cook_body(body), __mt.upper(), cls.__cook_url(e, _url)
        return _rwar

    @staticmethod
    def __cook_url(url, endpoint=None):
        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        url = url if url.startswith("/") else f"/{url}"
        url = url.removesuffix("/") if url.endswith("/") else url
        return f"{url}{endpoint}"

    @staticmethod
    def __cook_headers(key=None) -> ReqMapper:
        headers = {}
        headers["Authorization"] = f"{key}" if key is not None else ""
        headers['User-Agent'] = 'AnonPiRequest/2.0'
        headers["Content-Type"] = "application/json"
        return RequestCooker.ReqMapper(headers)

    @staticmethod
    def cls_url(url) -> t.Tuple[str, str, str, str]:
        if not isinstance(url, str):
            raise TypeError("url must be instance of str")
        if not "https://" in url and not "http://" in url:
            raise ValueError("url must be http or https")
        parsed = up(url)
        host, port, endpoint, scheme = parsed.hostname, parsed.port, parsed.path, parsed.scheme
        return host, port, endpoint if endpoint else "/", scheme

    @staticmethod
    def __cook_body(body: dict | str = None) -> str:
        if body is not None:
            if not isinstance(body, (dict, str)):
                raise TypeError("body must be instance of dict or str")
            body = body.strip() if isinstance(body, str) else body
            return json.dumps(body)
        return json.dumps({})

    @classmethod
    def __cook_request(cls, base):
        if base is None:
            raise ValueError("""anonpi.api_base must not be None
            >>> import anonpicomplex
            >>> anonpicomplex.api_base = "https://api.anonpi.co/api/v1/"
            Please visit https://docs.anonpi.co to read docs
            """)
        h, p, e, c = RequestCooker.cls_url(base)
        _new_in = type("RequestWrapper", (http.client.HTTPConnection if
                                          c == 'http' else http.client.HTTPSConnection,), {})
        _rwar = _new_in(h, p, timeout=5)
        setattr(_rwar, "prepare_request", cls.prepare_request)
        setattr(cls, "cooked_request", (_rwar, e))
        return _rwar, e

    def prepare_request(self) -> str:
        if (not isinstance(self._hd, RequestCooker.ReqMapper) or not isinstance(self._bd, str)):
            raise TypeError(
                "struct must be instance of tuple(HttpConnection, headers, body, method)")
        if not isinstance(self._mt, str) and not self._mt in ["GET", "POST", "PUT", "DELETE"]:
            raise ValueError("method must be GET, POST, PUT or DELETE")
        try:
            self.request(method=self._mt, url=self._url,
                         headers=self._hd.to_dict, body=self._bd if (self._mt != "GET" or self._bd != {}) else None)

        except http.client.CannotSendRequest:
            raise ConnectionError(
                "Connection Error: Please check your internet connection")

        except socket.gaierror:
            raise ConnectionError(
                "Please check your internet connection "
                "or Please ensure your anonpi.api_base is correct or leave it default "
                "If issue persists please report us at anonpi.co/support")

        except socket.timeout:
            raise ConnectionError(
                "Please check your internet connection "
                "or Please ensure your anonpi.api_base is correct or leave it default "
                "If issue persists please report us at anonpi.co/support")
        except ConnectionRefusedError:
            raise ConnectionError(
                "AnonPi API is down please try again later or report us at anonpi.co/support or please check anonpi.api_base is correct or leave it default")

        resp = self.getresponse()
        rr = resp.read()
        return rr if type(rr) == bytes else rr.decode("utf-8"), resp.status
