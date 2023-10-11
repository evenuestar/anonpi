import typing as t


class AnonLang:
    AFRIKANST: t.Literal["af"] = "af"
    ARABIC: t.Literal["ar"] = "ar"
    BULGARIAN: t.Literal["bg"] = "bg"
    BENGALI: t.Literal["bn"] = "bn"
    BOSNIAN: t.Literal["bs"] = "bs"
    CATALAN: t.Literal["ca"] = "ca"
    CZECH: t.Literal["cs"] = "cs"
    DANISH: t.Literal["da"] = "da"
    GERMAN: t.Literal["de"] = "de"
    GREEK: t.Literal["el"] = "el"
    ENGLISH: t.Literal["en"] = "en"
    SPANISH: t.Literal["es"] = "es"
    ESTONIAN: t.Literal["et"] = "et"
    FINNISH: t.Literal["fi"] = "fi"
    FRENCH: t.Literal["fr"] = "fr"
    GUJARATI: t.Literal["gu"] = "gu"
    HINDI: t.Literal["hi"] = "hi"
    CROATIAN: t.Literal["hr"] = "hr"
    HUNGARIAN: t.Literal["hu"] = "hu"
    INDONESIAN: t.Literal["id"] = "id"
    ICELANDIC: t.Literal["is"] = "is"
    ITALIAN: t.Literal["it"] = "it"
    HEBREW: t.Literal["iw"] = "iw"
    JAPANESE: t.Literal["ja"] = "ja"
    JAVANESE: t.Literal["jw"] = "jw"
    KHMER: t.Literal["km"] = "km"
    KANNADA: t.Literal["kn"] = "kn"
    KOREAN: t.Literal["ko"] = "ko"
    LATIN: t.Literal["la"] = "la"
    LATVIAN: t.Literal["lv"] = "lv"
    MALAYALAM: t.Literal["ml"] = "ml"
    MARATHI: t.Literal["mr"] = "mr"
    MALAY: t.Literal["ms"] = "ms"
    MYANMAR: t.Literal["my"] = "my"
    NEPALI: t.Literal["ne"] = "ne"
    DUTCH: t.Literal["nl"] = "nl"
    NORWEGIAN: t.Literal["no"] = "no"
    POLISH: t.Literal["pl"] = "pl"
    PORTUGUESE: t.Literal["pt"] = "pt"
    ROMANIAN: t.Literal["ro"] = "ro"
    RUSSIAN: t.Literal["ru"] = "ru"
    SINHALA: t.Literal["si"] = "si"
    SLOVAK: t.Literal["sk"] = "sk"
    ALBANIAN: t.Literal["sq"] = "sq"
    SERBIAN: t.Literal["sr"] = "sr"
    SUNDANESE: t.Literal["su"] = "su"
    SWEDISH: t.Literal["sv"] = "sv"
    SWAHILI: t.Literal["sw"] = "sw"
    TAMIL: t.Literal["ta"] = "ta"
    TELUGU: t.Literal["te"] = "te"
    THAI: t.Literal["th"] = "th"
    FILIPINO: t.Literal["tl"] = "tl"
    TURKISH: t.Literal["tr"] = "tr"
    UKRAINIAN: t.Literal["uk"] = "uk"
    URDU: t.Literal["ur"] = "ur"
    VIETNAMESE: t.Literal["vi"] = "vi"
    CHINESE_SIMPLIFIED: t.Literal["zh-CN"] = "zh-CN"
    CHINESE_MANDARIN_TAIWAN: t.Literal["zh-TW"] = "zh-TW"
    CHINESE_MANDARIN: t.Literal["zh"] = "zh"



    def __iter__(self):
        return iter([getattr(self, x) for x in dir(self) if not x.startswith("__") and not x.startswith("_")])

    def __contains__(self, item):
        return item in self.__iter__()

    def __len__(self):
        return len(self.__iter__())

    def __repr__(self):
        return f"<Language {self.__iter__()}>"

    def __str__(self):
        return f"<Language {self.__iter__()}>"

    def __new__(cls, *args, **kwargs):
        raise TypeError("Language cannot be instantiated")
    

