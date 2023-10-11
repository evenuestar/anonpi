import typing as t


def nested_record_collector(cls):
    record = {
        "call_record": {'cost': 'cost', 'duration': 'duration', 'from': 'from_number', 'to': 'to_number'},
        "topup_record": {'cost': 'cost', 'date': 'date', 'credit': 'credit'}
    }

    def attr_():
        if hasattr(cls, '__setattr_failed'):
            k, v = getattr(cls, '__setattr_failed')
            raise AttributeError(f"Invalid attribute {k} for {cls.__name__}")

    def initialize_modal(self, s_model: t.Dict[str, t.Union[int, str]], initiator: object):
        init = initiator()
        if not all([x in s_model for x in record[self.obj_name[0]]]):
            raise AttributeError(
                f"Invalid attributes for {self.__class__.__name__} avl: {list(record[self.obj_name[0]])} got: {s_model.keys()}"
            )

        [setattr(init, "_"+record[self.obj_name[0]][k], v) if k in record[self.obj_name[0]]
         else setattr(self, '__setattr_failed', (k, v)) for k, v in s_model.items()]
        return init

    def models_setter(self, models: t.List[dict] = None, **k):
        if not k.get('_D'):
            raise NotImplementedError(
                "Please use module level object to get values "
                "Creating a class manually is not supported "
                "Please use User.get_topup_records() or User.get_call_records() to create a class and you will get Records Object with the lists of records "
                "Visit https://docs.anonpi.com/ for docs"
            )
        if not isinstance(models, list):
            raise TypeError(
                f"models must be instance of list got {type(models)}")
        if models == None:
            raise NotImplementedError(
                "Please use module level object to get values "
                "Creating a class manually is not supported "
                "Please use User.get_topup_records() or User.get_call_records() to create a class and you will get Records Object with the lists of records "
                "Visit https://docs.anonpi.com/ for docs"
            )
        self.__all__ = []
        [self.__all__.append(initialize_modal(
            self, x, initiator=self.obj_name[1])) for x in models]
        attr_()

    setattr(cls, '__init__', models_setter)
    return cls
