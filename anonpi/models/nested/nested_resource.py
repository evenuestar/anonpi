from anonpi.models.manager import RequestCooker, AnonConverter as conv


def nested_call_resouce(path: str, action: str):
    def inner(cls):
        def nested_url(cls):
            if path == "_status":
                return f"{cls.obj_name}/status", "GET"
            if action == "create":
                return f"{cls.obj_name}/{path}", "POST"
            elif action == "modify":
                return f"{cls.obj_name}/{path}", "PUT"
            elif action == "delete":
                return f"{cls.obj_name}/{path}", "DELETE"
            elif action == "get":
                return f"{cls.obj_name}/{path}", "GET"

        def make_path(path):
            path = path.replace("/", "_")
            if path == "_status":
                return "make_status"
            return f"make_{path}"

        def pluspath(path):
            if "/" in path:
                return path.replace("/", "_")
            return path

        setattr(cls, make_path(path), classmethod(nested_url))

        def check_nested_params(func):
            def inner(*args, **kwargs):
                given_annotations = func.__annotations__
                for param_name, param_type in given_annotations.items():
                    if param_name in kwargs:
                        if not isinstance(kwargs[param_name], param_type):
                            raise TypeError(
                                f'Parameter {param_name} should be of type {param_type.__name__}')
                    else:
                        arg_value = args[func.__code__.co_varnames.index(
                            param_name)]
                        if not isinstance(arg_value, param_type):
                            raise TypeError(
                                f'Parameter {param_name} should be of type {param_type.__name__}')
                return func(*args, **kwargs)
            return inner

        def nested_create_resouce(cls, *args, **kwargs):
            if args:
                raise TypeError("nested resource can not have positional arguments "
                                "use module level function instead "
                                f"Please visit https://docs.anonpi.co to read docs "
                                )
            res = RequestCooker.cook_request(cls, make_path(path), kwargs)
            return conv.convert_to_anonpi(cls, res.prepare_request(res), 
                                          clsname="recording" \
                                            if "record" in path else "call" if not "history" in path else "history")
        npath = path.removeprefix("_") if path.startswith("_") else path    
        plpath = pluspath(npath)
        setattr(cls, f"{action}_{plpath}", classmethod(
            check_nested_params(nested_create_resouce)))
        return cls
    return inner
