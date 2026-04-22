from __types__ import SilenceOrSpeech


def is_silence_or_speech(energy: int, zcr: float) -> SilenceOrSpeech:
    # 1. Senaryo: Güçlü konuşma (Barajı 150-200'e çekmek daha garanti olabilir)
    if energy > 200 and zcr < 0.3:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="speech")

    # 2. Senaryo: Kısık sesle konuşma (Enerji düşük ama ses pürüzsüz/ZCR düşük)
    elif energy >= 80 and energy <= 200 and zcr < 0.2:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="speech")

    # 3. Senaryo: Gürültü Filtresi (ZCR çok yüksekse enerjiye bakma, gürültüdür)
    elif zcr > 0.5:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="silence")

    # Geri kalan her şey (Çok düşük enerji veya belirsiz durumlar)
    else:
        return SilenceOrSpeech(energy=energy, zcr=zcr, type="silence")


def detect_speech(result):
    result_ = []
    for frame in result:
        energy, zcr = frame
        result_.append(is_silence_or_speech(energy, zcr))
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


def get_test_detect():
    from features import get_test_result

    result = get_test_result()
    return detect_speech(result)


if __name__ == "__main__":
    from features import get_test_result

    result = get_test_result()
    for frame in result:
        energy, zcr = frame
        print(is_silence_or_speech(energy, zcr))
