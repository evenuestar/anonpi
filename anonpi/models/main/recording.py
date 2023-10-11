import typing as t
import pathlib as pl
from anonpi.models.manager import RequestCooker


class RecordedCall(object):
    """RecordedCall having recorded call properties.

    Properties:
        audio_url (str): the url of the audio
        audio_data (bytes): the audio data in bytes
    """
    def __init__(self, src):
        self.__src = src
        __requester = RequestCooker.cook_request(rname=True, url=src)
        hv = __requester.prepare_request(__requester)
        if hv[1] != 200:
            raise ValueError("Invalid url")
        self.__audio_data = hv[0]

    @property
    def audio_url(self):
        return self.__src

    def __repr__(self) -> str:
        return "<{} {}>".format(self.__class__.__name__, "audio_url={} audio_data_length={}".format(self.audio_url, len(self.audio_data)))

    def __str__(self) -> str:
        return "<{} {}>".format(self.__class__.__name__, "audio_url={} audio_data_length={}".format(self.audio_url, len(self.audio_data)))

    def save_file(self, path: t.Union[str, pl.Path]) -> None:
        """ Save audio data to file 

        Valid file extentions are .mp3, .wav, .ogg, .flac

        Args:
            path (t.Union[str,Path]): Path to save audio data

        Raises:
            >>> TypeError: If path is not instance of str or Path
            >>> PermissionError: If permission is denied
            >>> FileNotFoundError: If file is not found
        """
        valid_extentions = [".mp3", ".wav", ".ogg", ".flac"]
        if isinstance(path, str):
            path = pl.Path(path)
        if path.suffix not in valid_extentions:
            raise ValueError(f"Invalid file extention {path.suffix}")
        with path.open("wb") as f:
            f.write(self.audio_data)

    @property
    def audio_data(self):
        return self.__audio_data

    def __getitem__(self, __name: str) -> bytes | str:
        vl = getattr(self, __name)
        if vl is None:
            raise AttributeError(f"Recording object has no attribute {__name}")
        return vl
