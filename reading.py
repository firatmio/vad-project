# Source - https://stackoverflow.com/a/54174291
# Posted by DavidPM, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-21, License - CC BY-SA 4.0

import numpy as np
from scipy.io import wavfile


def read_wav_file(file_path="./sound.wav"):
    sample_rate, data = wavfile.read(file_path)
    return sample_rate, data


def stereo_to_mono(stereo_signal):
    data = stereo_signal
    return np.mean(data, axis=1)


def slice_signal(data, frame_size):
    num_frames = int(len(data) // int(frame_size))
    return [data[i * frame_size : (i + 1) * frame_size] for i in range(num_frames + 1)]


def get_test_result():
    sample_rate, stereo_signal = read_wav_file("./sound.wav")
    data = stereo_to_mono(stereo_signal)
    frame_size = 20
    actual_frame_size = int(sample_rate * (frame_size / 1000))

    return slice_signal(data, actual_frame_size)


if __name__ == "__main__":
    sample_rate, stereo_signal = read_wav_file("./sound.wav")
    data = stereo_to_mono(stereo_signal)
    frame_size = 20
    actual_frame_size = int(sample_rate * (frame_size / 1000))

    sliced_data = slice_signal(data, actual_frame_size)
    for i, frame in enumerate(sliced_data):
        start_time = i * (frame_size / 1000)
        end_time = (i + 1) * (frame_size / 1000)
        print(f"Frame {i} [{start_time:.2f}s - {end_time:.2f}s]: {frame}")

    # Çıktı tipi: List[np.ndarray]
