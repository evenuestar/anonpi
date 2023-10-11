from anonpi.models.nested import nested_call_resouce


def err():
    raise NotImplementedError(
        """ Please use module level object to get values,"Creating a User is not supported. 
            Please use 
            >>> User.get_call_record()  -> to get records type[UserCallRecords]
            >>> User.get_topup_record() -> to get records type[UserTopupRecords]
            >>> User.balance() -> to get balance type[int, float]

            to create get values and you will get Records Object with the lists of records"
            "Visit https://docs.anonpi.com/ for docs"""
    )


@nested_call_resouce("history/topup", "get")  # type: ignore
@nested_call_resouce("history/calls", "get")  # type: ignore
@nested_call_resouce("balance", "get")  # type: ignore
#
# Base class for Call with meta manager
#
class UserBaseConn:
    ...

setattr(UserBaseConn, '__init__', lambda self, *args, **kwargs: err())
