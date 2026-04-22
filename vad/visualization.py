import matplotlib.pyplot as plt


def visualize_result(result, sample_rate, frame_size_ms=20):
    frame_duration = frame_size_ms / 1000 / 1000
    times = [i * frame_duration for i in range(len(result))]

    plt.figure(figsize=(10, 4))
    plt.plot(times, result, color="red")
    plt.xlabel("Time (s)")
    plt.ylabel("Speech Probability")
    plt.title("Speech Detection Result")
    plt.show()
