import numpy as np


def rms_energy(frame):
    return np.sqrt(np.mean(np.square(frame)))


def zero_crossing_rate(frame):
    return np.mean(np.abs(np.diff(np.sign(frame))))


def features(frames: list[np.ndarray]):
    result = []
    for i, frame in enumerate(frames):
        result.append([rms_energy(frame), zero_crossing_rate(frame)])
    return result


if __name__ == "__main__":
    from reading import get_test_result

    frames = get_test_result()
    print(features(frames))
