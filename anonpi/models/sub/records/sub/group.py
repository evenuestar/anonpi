import typing as t
from anonpi.models.sub import TopupHistory, CallHistory, RecordsBase


class UserCallRecords(RecordsBase):
    """ Call Records class consists of a list of CallHistory objects
    >>> length = len(user_call_records)
    >>> for record in user_call_records:
    >>>     print(record.cost)

    """
    obj_name = 'call_record', CallHistory

    def __getitem__(self, index: int) -> CallHistory:
        return super().__getitem__(index)


class UserTopupRecords(RecordsBase):
    """ Topup Records class consists of a list of TopupHistory objects
    >>> length = len(user_topup_records)
    >>> for record in user_topup_records:
    >>>     print(record.amount)
    """
    obj_name = 'topup_record', TopupHistory

    def __getitem__(self, index: int) -> TopupHistory:
        return super().__getitem__(index)
