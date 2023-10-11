import typing as t
from anonpi.models.nested.nested_initiator_check import initiator_check


@initiator_check
class AnonBaseObject:

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {' '.join([f'{k}={v}' for k, v in self.__dict__.items()])}>"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, self.__class__):
            return False
        return self.__dict__ == o.__dict__

    def __getitem__(self, key):
        attr = getattr(self, key)
        if attr:
            return attr
        raise KeyError(f"Attribute {key} not found in {self.__class__.__name__}\t"
                       f"Please use module level object to get values\t"
                       )
    
