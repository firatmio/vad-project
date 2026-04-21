import typing


class SilenceOrSpeech(typing.TypedDict):
    energy: int
    zcr: float
    type: str | None
