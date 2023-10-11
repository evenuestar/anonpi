from anonpi.models.sub import AnonObject
from anonpi.models.manager import CallAnonType
from anonpi.models.nested import nested_call_resouce


@nested_call_resouce("_status", "get")  # type: ignore
@nested_call_resouce("hangup", "create")  # type: ignore
@nested_call_resouce("hold", "create")  # type: ignore
@nested_call_resouce("unhold", "create")  # type: ignore
@nested_call_resouce("gather/stop", "create")  # type: ignore
@nested_call_resouce("gather/audio", "create")  # type: ignore
@nested_call_resouce("gather/text", "create")  # type: ignore
@nested_call_resouce("record/start", "create")  # type: ignore
@nested_call_resouce("record/pause", "create")  # type: ignore
@nested_call_resouce("record/unpause", "create")  # type: ignore
@nested_call_resouce("record/stop", "create")  # type: ignore
@nested_call_resouce("record/get", "get")  # type: ignore
@nested_call_resouce("playback/start/audio", "create")  # type: ignore
@nested_call_resouce("playback/start/text", "create")  # type: ignore
@nested_call_resouce("playback/stop", "create")  # type: ignore
#
# Base class for Call with meta manager
#
class CallBaseAnon(AnonObject, metaclass=CallAnonType):
    def __getattr__(self, _name: str) -> None:
        if _name == 'calluuid':
            raise ValueError(
                "calluuid is not defined please use Call.create() to create a call and you will get Call object with calluuid")

    pass
