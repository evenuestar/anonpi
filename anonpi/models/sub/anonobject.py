import typing as t
from anonpi.models.manager import RequestCooker
from anonpi.models.manager import AnonConverter as conv
from anonpi.models.nested import AnonBaseObject


class AnonObject(AnonBaseObject):
    @classmethod
    def create(cls, from_number: str, to_number: str, callback_url: str, amd: bool = False) -> t.Self:
        """Create a Call And Return Call Instance

        Args:
            from_number (str): The number to call from
            to_number (str): The number to call to
            callback_url (str): The url to callback send call callbacks with data
            amd (bool, optional): If Amd is set to true and false. Defaults to False.

        Returns:
            t.Self: AnonPi Call Instance for further operations
        Raises:
            >>> ValueError: If from_number, to_number or callback_url is not provided
            >>> InvalidNumber: If from_number or to_number is not valid
            >>> InvalidCallbackUrl: If callback_url is not valid
            >>> InvalidAmd: If amd is not valid
            >>> InvalidParameter: If params is not valid
            >>> CountryNotAvailable: If country is not available
            >>> MissingParameter: If any required parameter is missing
            >>> ExtraParameter: If any extra parameter is provided
            >>> AnonException: If any other error occurs
            ... Futher Exceptions
        """
        res = RequestCooker.cook_request(cls, "_make_create", {
            "from_number": from_number, "to_number": to_number, "callback_url": callback_url, "amd": amd})
        return conv.convert_to_anonpi(cls, res.prepare_request(res), clsname="call")

    @classmethod
    def get(cls, calluuid: str) -> t.Self:
        """Get Call Instance by calluuid

        Args:
            calluuid (str): calluuid of the call

        Returns:
            Call: AnonPi Call Instance for further operations

        Raises:
            ValueError: If calluuid is not provided
            CallNotFound: If calluuid is not found
            ... Futher Exceptions
        """
        res = RequestCooker.cook_request(
            cls, "make_status", {"calluuid": calluuid})
        return conv.convert_to_anonpi(cls, res.prepare_request(res), clsname=cls.obj_name)

    def _make_create(*args, **kwargs) -> t.Literal['For Developer Use Only']:
        """For Developer Use Only"""
        return "call/create", "POST"
