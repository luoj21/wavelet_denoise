import numpy as np
import pywt

class Wavelet_Filter:
    """A wavelet-based denoising algorithm based off of:

     - Iain M. Johnstone, Bernard W. Silverman, Wavelet Threshold Estimators for Data with Correlated Noise, 
    Journal of the Royal Statistical Society: Series B (Methodological), Volume 59, Issue 2, July 1997, 
    Pages 319–351, https://doi.org/10.1111/1467-9868.00071
    
    - Abd El-Fattah, M.A., Dessouky, M.I., Abbas, A.M. et al. 
    Speech enhancement with an adaptive Wiener filter. Int J Speech Technol 17, 53–64 (2014). 
    https://doi.org/10.1007/s10772-013-9205-5
    
    - https://stackoverflow.com/questions/56789030/why-is-wavelet-denoising-producing-identical-results-regardless-of-threshold-lev"""
    
    
    def __init__(self, threshold_type: str, wavelet: str, level: int, mode: str, x: np.ndarray):
        if wavelet not in set(pywt.wavelist(family=None, kind='all')):
            raise ValueError("Improper Wavelet name")
        
        if threshold_type.lower() not in ["hard", "soft"]:
            raise ValueError("Improper threshold (must be hard or soft)")
        

        self.threshold_type = threshold_type
        self.wavelet = wavelet
        self.level = level
        self.mode = mode
        self.x = x

    @staticmethod   
    def median_abs_dev(w: np.ndarray):
        """ Computes median absolute deviation of the wavlet coefficients w1...wn """
        return np.median(np.abs(w - np.median(w)))
    
    @staticmethod
    def mean_abs_dev(w: np.ndarray):
        """ Computes mean absolute deviation of the wavlet coefficients w1...wn """
        return np.mean(np.abs(w - np.mean(w)))


    def _filter(self, scaling_factor: float, universal: bool, operation: str):
        """Performs filtering based off of universal or per-scale thresholds. The
        former is based off the AWGN (Additive White Gaussian Noise) assumption. The latter
        is better suited when dealing with correlated noise"""
        coeffs = pywt.wavedec(self.x, wavelet = self.wavelet, mode= self.mode)
        cA = coeffs[0] # cA_n
        cDs = coeffs[1:] # cD_n, cD_n-1, …, cD2, cD1
        cDs_new = []

        if operation.lower() == "median":
            mad = self.median_abs_dev
        elif operation.lower() == "mean":
            mad = self.mean_abs_dev
        else:
            raise ValueError("Operation must be mean (for mean absolute deviation) or median for (median absolute deviation)")

        if universal:
            _lambda = np.sqrt(2 * np.log(len(self.x)))
            sigma = mad(coeffs[-self.level]) / 0.6745
            threshold = _lambda * sigma * scaling_factor
            cDs_new.extend(pywt.threshold(i, value=threshold, mode=self.threshold_type) for i in cDs)

        else:
            for cD in cDs:
                N = len(cD) 
                _lambda = np.sqrt(2 * np.log(N))
                sigma = mad(cD) / 0.6745 
                threshold = _lambda * sigma * scaling_factor
                cDs_new.append(pywt.threshold(cD, value=threshold, mode=self.threshold_type))
        
        assert len(cDs_new) == len(cDs)
        reconstr = pywt.waverec([cA] + cDs_new, wavelet = self.wavelet, mode = self.mode)
        reconstr = reconstr[0:len(self.x)] if len(self.x) != len(reconstr) else reconstr
        return reconstr