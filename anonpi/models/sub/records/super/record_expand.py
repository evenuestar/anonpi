from anonpi.models.nested import nested_record_collector



@nested_record_collector
class RecordsBase:
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.__class__.__name__} Records={self.__all__}>"

    def __getitem__(self, index: int):
        return self.__all__[index]

    def __iter__(self):
        return iter(self.__all__)

    def __len__(self):
        return len(self.__all__)

    def __setitem__(self, index: int, value: dict):
        raise NotImplementedError("Cannot set item in a list")

    def __delitem__(self, index: int):
        raise NotImplementedError("Cannot delete item in a list")
