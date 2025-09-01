import numpy as np
import matplotlib.pyplot as plt
import librosa



def calc_snr(x: np.ndarray, x_hat: np.ndarray):
    """Calculates signal to noise ratio of a given signal based off:
    
    - J. L. Roux, S. Wisdom, H. Erdogan and J. R. Hershey, "SDR – Half-baked or Well Done?," ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 
    Brighton, UK, 2019, pp. 626-630, doi: 10.1109/ICASSP.2019.8683855. keywords: {speech enhancement;source separation;signal-to-noise-ratio;objective measure},"""

    eps = np.finfo(float).eps
    N = len(x)
    signal_power = (np.linalg.norm(x) ** 2) 
    noise_power = (np.linalg.norm(x - x_hat) ** 2)

    return 10 * np.log10(signal_power / (noise_power + eps))
    


def plot_spectrogram(audio_signal: np.ndarray, sr: int, title: str, out_path: str):
    """Computes log-power-spectrogram of a given signal"""

    D = librosa.amplitude_to_db(np.abs(librosa.stft(audio_signal)), ref=np.max)

    plt.figure(figsize=(10, 3))
    librosa.display.specshow(D, x_axis='time', y_axis='log', sr=sr, cmap='inferno')
    plt.title(title)
    plt.colorbar(format='%+2.0f dB')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.tight_layout()
    plt.savefig(f'{out_path}/{title}.png', dpi = 200)
    plt.show()


def plot_original_vs_filtered(x: np.ndarray, x_hat: np.ndarray, start: int, end: int, sr: int):
    """Plots side by side the filtered signal and the original signal"""
    fig, axs = plt.subplots(1, 2, figsize = (10, 3))
    t = np.arange(len(x)) / sr

    axs[0].plot(t[start:end], x[start:end])
    axs[0].set_title('Original Signal')

    axs[1].plot(t[start:end], x_hat[start:end])
    axs[1].set_title('Filtered Signal')

    plt.tight_layout()