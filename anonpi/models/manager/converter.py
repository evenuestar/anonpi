import json
from anonpi.error import AnonException

from anonpi.models.main.recording import RecordedCall


class AnonConverter:
    def __init__(self, cls, *args) -> None:
        self.args = args

    @staticmethod
    def convert_to_anonpi(cls, response: tuple, **k):
        if not isinstance(response, tuple):
            raise TypeError("response must be instance of dict")
        response_d = response[0]
        try:
            response_d = json.loads(response_d)
        except:
            raise TypeError("response must be instance of dict")
        if len(response) != 2:
            raise ValueError(
                "response must be instance of tuple with length 2")
        if not isinstance(response[1], int):
            raise TypeError("response code must be instance of int")
        if not response_d.get("status") == "ok":
            AnonException(*response, clsname=k.get("clsname"))
        if "balance" in response_d:
            return response_d.get("balance")
        if any(item in response_d.get("message").lower() for item in ["created", "fetched"]) and k.get("clsname") == "call":
            return AnonConverter.__set_cls_attrs(cls, {
                "calluuid": response_d.get("calluuid"),
                **response_d.get("meta")
            })
        if k.get("clsname") == 'history':
            return response_d.get('result')

        if k.get("clsname") == "recording":
            _tried_url = response_d.get("url")
            if not _tried_url:
                return None
            _r = RecordedCall(response_d.get("url"))
            return _r
        else:
            return None

    @staticmethod
    def __set_cls_attrs(cls, attrs):
        _ = cls(_D=True)
        for key, value in attrs.items():
            setattr(_, key, value)
        return _
