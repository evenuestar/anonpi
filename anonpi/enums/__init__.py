"""
This module contains the models for the main application.

Do not edit the classes manually or import them directly.
"""
from anonpi.enums.languages import AnonLang
from json import dumps


class Language(AnonLang):
    """ Language class having all supported languages of sounds and tts used in call.speak() and call.gather_using_speak() methods.

        ```python
        en = Language.ENGLISH
        hin = Language.HINDI
        ...

    """

    @classmethod
    def iterr(cls):
        return dict(zip([x for x in dir(cls) if not x.startswith("__") and not x.startswith("_") and not x in ['iterr', 'valid']], [getattr(cls, x) for x in dir(cls) if not x.startswith("__") and not x.startswith("_")]))

    @classmethod
    def valid(cls, lang: str):
        if isinstance(lang, str):
            if (lang.lower() in [x.lower() for x in list(cls.iterr().values())]):
                return lang
            if (lang.upper() in [x.upper() for x in list(cls.iterr().keys())]):
                return getattr(cls, lang.upper())
            else:
                raise ValueError(
                    "Invalid Language || List of Languages: \n" + dumps(cls.iterr(), indent=4))
            

__slots__ = ['Language']
