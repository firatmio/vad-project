import numpy as np


def stereo_to_mono(stereo_signal):
    data = stereo_signal[1]
    return np.mean(data, axis=1)


if __name__ == "__main__":
    from read_wav_file import read_wav_file

    stereo_signal = read_wav_file()
    mono_signal = stereo_to_mono(stereo_signal)
    print(mono_signal)
