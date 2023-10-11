"""
This module contains the models for the main application.

Do not edit the classes manually or import them directly.
"""


from anonpi.models.main import Call ,RecordedCall , User
from anonpi.enums import Language
from anonpi.models.sub import TopupHistory , CallHistory , UserTopupRecords , UserCallRecords


# Path: models/main/call.py

dev = True

__slots__ = [
    'Call',
    'RecordedCall',
    'Language',
    'TopupRecord',
    'CallRecord',
    'UserTopupRecords',
    'UserCallRecords'
]
__all__ = [
    'Call',
    'RecordedCall',
    'Language',
    'TopupRecord',
    'CallRecord',
    'UserTopupRecords',
    'UserCallRecords'
]