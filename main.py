import argparse

from vad.detector import detect_speech as ds
from vad.exporter import final_export, segmenter
from vad.features import features
from vad.reading import read_audio as ra
from vad.reading import read_wav_file
from vad.visualization import visualize_result

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", type=str, help="Input audio file")
parser.add_argument("--output", type=str, help="Output audio file")
parser.add_argument("--threshold", type=float, help="Speech detection threshold")
args = parser.parse_args()

print(args)


class VAD:
    """
    Voice Activity Detection (VAD) class that processes audio files to detect speech segments.
    """

    def __init__(self, input_audio, output_audio, threshold):
        self.input_audio = input_audio
        self.output_audio = output_audio
        self.threshold = threshold

        self.frame_size = 20
        self.sample_rate, self.data = read_wav_file(self.input_audio)
        self.actual_frame_size = int(self.frame_size * 1000)

    def read_audio(self):
        audio = ra(self.input_audio)
        return audio

    def detect_speech(self, audio):
        speech = ds(audio, self.threshold)
        return speech

    def features(self, audio):
        return features(audio)

    def export(self):
        segments = segmenter(
            self.detect_speech(self.features(self.read_audio())),
            self.data,
            self.actual_frame_size,
        )
        return final_export(segments, self.sample_rate, self.output_audio)

    def visualize(self):
        try:
            visualize_result(self.data, self.sample_rate)
            return True, None
        except Exception as e:
            return False, e


if __name__ == "__main__":
    vad = VAD(args.input, args.output, args.threshold)
    vad.export()
    vad.visualize()

# Usage
# python main.py --input <input_audio> --output <output_audio> --threshold <threshold>
