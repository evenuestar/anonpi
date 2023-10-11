from typing import Any, Union
import inspect


class CallAnonType(type):
    def __new__(cls, name, bases, attrs):
        # pending
        # for attr_name, attr_value in attrs.items():
        #     if callable(attr_value):
        #         attrs[attr_name] = cls.__baricate(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def __baricate(func):
        def inner(*args, **kwargs):
            p_d = {param.name:
                   [param.annotation,
                    param.default if param.default != inspect.Parameter.empty else inspect.Parameter.empty]
                   for param in list(inspect.signature(func).parameters.values())}
            if inspect.ismethod(func):
                args = args[1:]
            p_g = {
                **{func.__code__.co_varnames[index]: arg for index, arg in enumerate(args)}, **kwargs}
            for p_n, param_info in p_d.items():
                if p_n in p_g:
                    nont = type(None)
                    if param_info[0] != bool:
                        if type(p_g[p_n]) == bool:
                            raise TypeError(
                                f"{p_n} should be of type {' | '.join([x.__name__ for x in param_info[0].__args__]) if hasattr(param_info[0], '__origin__') and param_info[0].__origin__ == Union else param_info[0].__name__}")

                    if type(p_g[p_n]) == nont:
                        raise TypeError(
                            f"{p_n} should not be of type {nont.__name__}")
                    if not isinstance(p_g[p_n], param_info[0]):
                        if param_info[0] != inspect.Parameter.empty:
                            raise TypeError(
                                f"{p_n} should be of type {' | '.join([x.__name__ for x in param_info[0].__args__]) if hasattr(param_info[0], '__origin__') and param_info[0].__origin__ == Union else param_info[0].__name__}")

                if param_info[1] == inspect.Parameter.empty and p_n not in p_g and (not p_n in ('args', 'kwargs') and not param_info[0] == inspect.Parameter.empty):
                    raise TypeError(f"{p_n} is required")
                
            return func(*args, **kwargs)
        return inner
