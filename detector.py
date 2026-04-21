import typing


class SilenceOrSpeech(typing.TypedDict):
    energy: int
    zcr: float
    type: str | None


def is_silence_or_speech(energy: int, zcr: float) -> SilenceOrSpeech:
    if energy > 250 and zcr < 0.3:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="speech")
    elif energy < 100:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="silence")
    elif energy >= 101 and energy <= 249 and zcr > 0.6:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="speech")
    else:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="silence")


def detect_speech(result):
    result = []
    for frame in result:
        energy, zcr = frame
        result.append(is_silence_or_speech(energy, zcr))
    return smoothing(result)


def smoothing(result):
    for i in range(2, len(result) - 2):
        window = result[i - 2 : i + 3]
        speech_count = len([f for f in window if f["type"] == "speech"])
        if speech_count >= 3:
            result[i]["type"] = "speech"
        else:
            result[i]["type"] = "silence"
    return result


if __name__ == "__main__":
    from features import get_test_result

    result = get_test_result()
    for frame in result:
        energy, zcr = frame
        print(is_silence_or_speech(energy, zcr))
