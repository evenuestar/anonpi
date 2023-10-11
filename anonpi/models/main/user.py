from anonpi.models.sub import UserCallRecords, UserTopupRecords, CallHistory, TopupHistory
from anonpi.models.sub import UserBaseConn
from anonpi.error import *
import typing as t


class User(UserBaseConn):
    """User class having call properties of a user
        Example:
        ```python
         balance = User.balance()
    """
    obj_name = "user"

    @classmethod
    def balance(cls) -> t.Union[int, float]:
        """#### Get the balance of the user

        Returns:
            Union[int, float]: Balance of the user
        """
        return User.get_balance()

    @classmethod
    def get_topup_history(cls) -> UserTopupRecords:
        """#### Get the topup history of the user

        Returns:
            UserTopupRecords: Topup history of the user consist of >>> List[TopupHistory]
        """
        return UserTopupRecords(User.get_history_topup(), _D=True)

    @classmethod
    def get_call_history(cls) -> UserCallRecords:
        """#### Get the call history of the user

        Returns:
            UserCallRecords: Call history of the user consist of >>> List[CallHistory]
        """
        return UserCallRecords(User.get_history_calls(), _D=True)
