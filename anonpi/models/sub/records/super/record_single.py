



class RecordRepresentation:
    def __str__(self):
        return f"<{self.__class__.__name__} {' '.join([f'{x}={getattr(self,x)}' for x in dir(self) if not x.startswith('__') and not x.startswith('_')])}>"

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, _item):
        item = getattr(self, _item, 'not_found')
        if item != 'not_found':
            return item
        else:
            raise KeyError(
                f"{_item} is not defined in {self.__class__.__name__} available keys are {([x for x in dir(self) if not x.startswith('__') and not x.startswith('_') and not callable(x) and not str(x) == 'str_repr'])}")