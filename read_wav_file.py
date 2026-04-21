# Source - https://stackoverflow.com/a/54174291
# Posted by DavidPM, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-21, License - CC BY-SA 4.0

from scipy.io import wavfile


def read_wav_file(file_path="./sound.wav"):
    return wavfile.read(file_path)


if __name__ == "__main__":
    print(read_wav_file("./sound.wav"))
