## Wavelet Denoising 

---

A custom implementation of Wavelet based thresholding for removing AWGN (Additive White Gaussian Noise) and correlated noise. This is based off the [1997 Paper by Johnstone and Silverman](https://academic.oup.com/jrsssb/article-abstract/59/2/319/7083031), in which the algorithm either performs soft or hard thresholding of the Wavelet coefficients of the input signal, where the treshold for each level $$j$$ is

$$\sigma_{j} \lambda_{j}$$

Here $$\sigma_{j}  = MAD(w_{jk}) / 0.6745$$ for the Wavelet coefficients $$w_{jk}$$ and $$\lambda_{j} = \sqrt{2 \log n}$$

This implementation was also based off details inspired by:
- [Speech enhancement using an adaptive Wiener Filter](https://dl.acm.org/doi/abs/10.1007/s10772-013-9205-5)
- [This Stack Overflow post](https://stackoverflow.com/questions/56789030/why-is-wavelet-denoising-producing-identical-results-regardless-of-threshold-lev)
- [WDenoise in MATLAB](https://www.mathworks.com/help/wavelet/denoising.html?s_tid=CRUX_topnav)

-----

### To get started:

- Do ```git clone https://github.com/luoj21/wavelet_denoise.git```
- Create a virtual environment: ```python3 -m venv .venv```
- Activate the environment```source .venv/bin/activate```
- Install packages: ```pip install -r requirements.txt```
- Run the notebooks in ```notebooks```

-----

### Other:

The audio used as data were pulled from the following YouTube links:
- [Man Born in 1853 Talks About Childhood in the 1860s- Enhanced Video & Audio [60 fps]](https://www.youtube.com/watch?v=_oqbLSisnME&list=LL&index=2)
- [Pablo Casals ('cello) - Apres un reve (Faure) (1926)](https://www.youtube.com/watch?v=rJsgL1_uw4M&list=RDrJsgL1_uw4M&start_radio=1)
