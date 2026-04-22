import os

import pandas as pd
import soundfile as sf

from __types__ import SilenceOrSpeech


def grouping(result: list[SilenceOrSpeech]) -> list[list[SilenceOrSpeech]]:
    groups = []
    start_index = None
    for i, item in enumerate(result):
        if item["type"] == "speech":
            if start_index is None:
                start_index = i
        if item["type"] == "silence":
            if start_index is not None:
                groups.append((start_index, i))
                start_index = None
    if start_index is not None:
        groups.append((start_index, len(result)))
    return groups


def load_audio(file_path: str):
    # Bu sana (data, sample_rate) döner
    # data: Senin o en başta işlediğin sayılar dizisi
    # samplerate: 44100 veya 16000 gibi hız değeri
    return sf.read(file_path)


def segmenter(result, audio_data, actual_frame_size):
    segments = []
    for start, end in grouping(result):
        start_sample = start * actual_frame_size
        end_sample = end * actual_frame_size
        segments.append(audio_data[start_sample:end_sample])
    return segments


def export_segments(segments, sample_rate, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, segment in enumerate(segments):
        file_path = os.path.join(output_dir, f"{i}.wav")
        sf.write(file_path, segment, sample_rate)
    return True


def final_export(segments, sample_rate, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, segment in enumerate(segments):
        file_path = os.path.join(output_dir, f"{i}.wav")
        sf.write(file_path, segment, sample_rate)

    return True
