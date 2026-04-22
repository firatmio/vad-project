from __types__ import SilenceOrSpeech


def is_silence_or_speech(
    energy: int, zcr: float, threshold: int | float
) -> SilenceOrSpeech:
    if energy > threshold and zcr < 0.3:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="speech")

    elif energy >= 80 and energy <= 200 and zcr < 0.2:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="speech")

    elif zcr > 0.5:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="silence")

    else:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="silence")


def detect_speech(result, threshold):
    result_ = []
    for frame in result:
        energy, zcr = frame
        result_.append(is_silence_or_speech(energy, zcr, threshold))
    return smoothing(result_)


def smoothing(result):
    for i in range(1, len(result) - 1):
        window = result[i - 1 : i + 2]
        speech_count = len([f for f in window if f["type"] == "speech"])
        if speech_count >= 2:
            result[i]["type"] = "speech"
        else:
            result[i]["type"] = "silence"
    return result


def get_test_detect(threshold):
    from features import get_test_result

    result = get_test_result()
    return detect_speech(result, threshold)
