from anonpi.models.sub import CallBaseAnon
from anonpi.enums import Language
from anonpi.models.main.recording import RecordedCall
from anonpi.error import *
import typing as t


class Call(CallBaseAnon):
    obj_name = "call"
    """Call class having call properties of a active call and methods to interact with the call.
        Example:
        ```python
         call:Call = Call.get_call("calluuid")
         status = call.status()
         call.hangup()
    """
    
    def hangup(self) -> None:
        """ ### Hangup the call 
        Raises:
            >>> AnonException: If any error occurs
            >>> CallNotFound: If call is not found
            ...For more errors see AnonException
        Returns:
            None
        """
        return Call.create_hangup(calluuid=self.calluuid)

    def status(self) -> None:
        """ ### Get status of the call
        Raises:
            >>> AnonException: If any error occurs
            >>> CallNotFound: If call is not found
            ...For more errors see AnonException
        Returns:
            None """
        return Call.get_status(calluuid=self.calluuid)

    def gather_using_audio(self, audio_url: str, dtmf_count: str = None, terminating_digit: str = None):
        """ ### Gather DTMF using audio

        Args:
            audio_url (str): Audio url to play must be a valid url follow "http" or "https" protocol
            dtmf_count (str, optional): Digits to be gathered. Defaults to None if terminating_digit is provided.
            terminating_digit (str, optional): Digits to terminate gathering. Defaults to None if dtmf_count is provided.

        Raises:
            >>> InvalidAudioUrl: If audio_url is not valid
            >>> InvalidDtmfDigits: If dtmf_count is not valid
            >>> InvalidTerminatingDigits: If terminating_digit is not valid
            >>> AnonException: If any other error occurs
        Returns:
            None
        """

        kg = {}
        if all([dtmf_count, terminating_digit]):
            raise ValueError(
                "dtmf_count and terminating_digit cannot be provided at the same time")
        if not any([dtmf_count, terminating_digit]):
            raise ValueError(
                "dtmf_count or terminating_digit must be provided")
        if terminating_digit:
            if len(terminating_digit) > 1:
                raise ValueError("terminating_digit must be a single digit")
            if not terminating_digit in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "*", "#"):
                raise ValueError("terminating_digit must be a valid digit")
            kg["terminating_digit"] = terminating_digit
        if dtmf_count:
            if not str(dtmf_count).isdigit():
                raise ValueError("dtmf_count must be a valid digit")
            if str(dtmf_count) == "0":
                raise ValueError("dtmf_count cannot be 0")
            kg["dtmf_count"] = dtmf_count
        return Call.create_gather_audio(calluuid=self.calluuid, audio_url=audio_url, **kg)

    def gather_using_speak(self, prompt: str, language: t.Union[str, Language] = "en", dtmf_count: str = None, terminating_digit: str = None):
        """ ### Gather DTMF using speak

        Args:
            prompt (str): Prompt to speak
            language (str): Language of the prompt | "en" | Language.english
            dtmf_count (str): Digits to be gathered
            terminating_digit (str): Digits to terminate gathering

        Raises:
            >>> InvalidPrompt: If prompt is not valid
            >>> InvalidLanguage: If language is not valid
            >>> InvalidDtmfDigits: If dtmf_count is not valid
            >>> InvalidTerminatingDigits: If terminating_digit is not valid
            >>> AnonException: If any other error occurs
        Returns:
            None
        """
        kg = {}
        if all([dtmf_count, terminating_digit]):
            raise ValueError(
                "dtmf_count and terminating_digit cannot be provided at the same time")
        if not any([dtmf_count, terminating_digit]):
            raise ValueError(
                "dtmf_count or terminating_digit must be provided")
        if terminating_digit:
            if len(terminating_digit) > 1:
                raise ValueError("terminating_digit must be a single digit")
            if not terminating_digit in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "*", "#"):
                raise ValueError("terminating_digit must be a valid digit")
            kg["terminating_digit"] = terminating_digit
        if dtmf_count:
            if not str(dtmf_count).isdigit():
                raise ValueError("dtmf_count must be a valid digit")
            if str(dtmf_count) == "0":
                raise ValueError("dtmf_count cannot be 0")
            kg["dtmf_count"] = dtmf_count
        return Call.create_gather_text(calluuid=self.calluuid, text=prompt, lang=Language.valid(language), **kg)

    def gather_stop(self) -> None:
        """ ### Stop gathering DTMF """
        return Call.create_gather_stop(calluuid=self.calluuid)

    def playback_start(self, audio_url: str) -> None:
        """ ### Play audio """
        if not audio_url.startswith("http"):
            raise ValueError("Audio url must start with http or https")
        return Call.create_playback_start_audio(calluuid=self.calluuid, audio_url=audio_url)

    def speak(self, prompt: str, language: t.Union[str, Language] = "en") -> None:
        """ ### Speak a prompt """
        return Call.create_playback_start_text(calluuid=self.calluuid, text=prompt, lang=Language.valid(language))

    def playback_stop(self) -> None:
        """ ### Stop playing audio """
        return Call.create_playback_stop(calluuid=self.calluuid)

    def record_pause(self) -> None:
        """ ### Pause recording """
        return Call.create_record_pause(calluuid=self.calluuid)

    def record_resume(self) -> None:
        """ ### Resume recording """
        return Call.create_record_unpause(calluuid=self.calluuid)

    def record_get(self) -> RecordedCall:
        """ ### Get recording

        Returns:
            Recording: Recording object having bytes data and url

        Raises:
            >>> AnonException: If any error occurs
            >>> RecordingNotFound: If recording is not found
            ...For more errors see AnonException
        """
        return Call.get_record_get(calluuid=self.calluuid)

    def record_start(self):
        """ ### Start recording """
        return Call.create_record_start(calluuid=self.calluuid)

    def record_stop(self):
        """ ### Stop recording """
        return Call.create_record_stop(calluuid=self.calluuid)

