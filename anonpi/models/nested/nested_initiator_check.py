def initiator_check(cls):
    def initiate_class(self, **k):
        _D = k.get('_D')
        if not _D:
            raise NotImplementedError(
                "Please use module level object to get values, "
                "Creating a call manually is not supported. "
                "Please use Call.create() to create a call and you will get Call object with calluuid "
                "Visit https://docs.anonpi.com/ for docs"
            )
        return None
    setattr(cls, '__init__', initiate_class)
    return cls
