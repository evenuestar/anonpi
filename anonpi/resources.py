"""
#### This module contains the models for the `main application`.

#### Do not edit the classes manually or import them directly.
"""

from anonpi.models import Call, RecordedCall, Language, TopupHistory, CallHistory, UserTopupRecords, UserCallRecords , User


# Path: models/main/call.py
dev = True

__slots__ = ['CallManager', 'Call', 'Recording', 'Language',
             'TopupHistory', 'CallHistory', 'UserTopupRecords', 'UserCallRecords']
