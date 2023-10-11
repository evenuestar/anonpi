import typing as t
from anonpi.models.sub.records.super.record_single import RecordRepresentation


class TopupHistory(RecordRepresentation):
    """ Topup History class
    Properties:
        >>> amount: Cost of the topup
        >>> date: Date of the topup
        >>> credit: Credited amount of the topup
    """

    @property
    def cost(self):
        """Cost of the topup"""
        return self._cost

    @property
    def date(self):
        """Date of the topup"""
        return self._date

    @property
    def credit(self):
        """ID of the topup"""
        return self._credit


class CallHistory(RecordRepresentation):
    """ Call History class

    Properties:
        >>> cost: Cost of the call  
        >>> duration: Duration of the call
        >>> from_number: From number of the call
        >>> to_number: To number of the call 

    """
    @property
    def cost(self):
        """Cost of call"""
        return self._cost

    @property
    def duration(self):
        """Duration of call"""
        return self._duration

    @property
    def from_number(self):
        """From number of call"""
        return self._from_number

    @property
    def to_number(self):
        """To number of call"""
        return self._to_number
