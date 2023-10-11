import json


class AnonPiError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__("Code: {} | Message: {}".format(code, message))

    def __str__(self):
        return "Code: {} | Message: {}".format(self.code, self.message)

    def __repr__(self):
        return "Code: {} | Message: {}".format(self.code, self.message)

    pass


class InvalidParameter(AnonPiError):
    # Another Error
    pass


class CountryNotAvailable(AnonPiError):
    def __init__(self, code, message, available_countries: list = None):
        super().__init__(code, "%s Available Countries: %s" %
                         (message, available_countries))
    pass


class InvalidAPIKey(AnonPiError):
    def __init__(self, code, message):
        super().__init__(code, "Invalid API Key\n"
                         "Please visit https://docs.anonpi.co to read docs\n"
                         "or visit https://anonpi.co to get API Key\n")
    pass


class GatherAlreadyExists(AnonPiError):
    # Another Error
    pass


class CalluuidNotFound(AnonPiError):
    # Another Error
    pass


class CallNotExists(AnonPiError):
    # Another Error
    pass


class NotEnoughBalance(AnonPiError):
    def __init__(self):
        super().__init__(403, "Not Enough Balance To Make Call "
                         "Please visit https://docs.anonpi.co to add funds")
    pass


class MissingParameter(AnonPiError):
    def __init__(self, code, message, missing: list = None):
        super().__init__(code, "%s Missing Parameters: %s" % (message, missing))
    pass


class ExtraParameter(AnonPiError):
    def __init__(self, code, message, extra_params: list = None):
        super().__init__(code, "%s Extra Parameters: %s" % (message, extra_params))
    pass


class InvalidCallbackURL(AnonPiError):
    def __init__(self, code, message):
        super().__init__(code, "Invalid Callback URL")
    pass


class RecordingNotFound(AnonPiError):
    def __init__(self, code, message):
        super().__init__(code, "Recording Not Found")
    pass


class InvalidNumber(AnonPiError):
    # Another Error
    pass


DATAOBJECTS = {
    "calluuid not found": CalluuidNotFound,
    "country not available": CountryNotAvailable,
    "invalid authorization": InvalidAPIKey,
    "missing parameters": MissingParameter,
    "extra parameters provided": ExtraParameter,
    "invalid callback_url": InvalidCallbackURL,
    "datatype expected": InvalidParameter,
}


class AnonException:
    def __init__(self, *resp, **k_):
        try:
            resp, code = json.loads(resp[0]), int(resp[1])
        except IndexError:
            raise TypeError("response must be instance of tuple with length 2\t"
                            "Use module level object to get values\t"
                            "If issuse presists please report it to anonpi.co/support"
                            )
        except ValueError:
            raise TypeError("response must be instance of tuple with length 2\t"
                            "Use module level object to get values\t"
                            "If issuse presists please report it to anonpi.co/support"
                            )
        _err_cls = self.filter_error(resp.get("message").lower())
        if _err_cls in (MissingParameter, ExtraParameter):
            raise _err_cls(code, resp.get("message"), resp.get("params"))
        if _err_cls == CountryNotAvailable:
            raise _err_cls(code, resp.get("message"),
                           resp.get("available_countries"))
        if k_.get("clsname") == "call":
            if _err_cls == CalluuidNotFound:
                raise CallNotExists(
                    code, "Call not exists or not active anymore")
        if "not found" in resp.get("message").lower() and k_.get("clsname") == "recording":
            raise RecordingNotFound(code, resp.get("message"))
        raise _err_cls(code, resp.get("message"))

    def filter_error(self, message):
        for key, value in DATAOBJECTS.items():
            if key in message:
                return value
        return AnonPiError
