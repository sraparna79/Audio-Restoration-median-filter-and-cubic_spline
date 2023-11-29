# Audio-Restoration using median filter and cubic_splines

<span style="text-decoration:underline;"><span style="font-size:larger;">Introduction</span></span>

Audio restoration is critical to signal processing, addressing challenges such as noise reduction and reconstruction of distorted samples. The assigned Task 2 is about dealing with clicks using median filtering and cubic spline interpolation, in the context of audio signal enhancement. Through their distinct approaches, these methods aim to refine audio quality by mitigating noise and interpolating missing or distorted components.

<span style="font-size:larger;">Background</span>

After performing AR interpolation in Matlab gave a clear idea regarding the positions of the clicks and estimated and replaced the value in the place of clicks. The position of the clicks is downloaded from Matlab, which is further used in median filtering and cubic spline.

<span style="font-size:larger;">Median Filter</span>

<span style="text-decoration:underline;">**Overview**</span>

Median filtering is a nonlinear filtering technique commonly used in image and signal processing. It replaces each sample in a signal with the median value of neighboring samples within a specified window. Median filtering proves effective in reducing impulse noise and outliers. By identifying and replacing extreme values with the median, the algorithm mitigates the impact of sudden spikes or drops in the audio signal.

<span style="font-size:larger;">Cubic Spline</span>

<span style="text-decoration:underline;">**Overview**</span>

Cubic spline interpolation is a mathematical method used to construct a smooth curve that passes through a set of given points. It is particularly useful for interpolating missing samples in a signal. Cubic spline interpolation can be applied to reconstruct missing or distorted audio samples. By fitting a cubic spline curve to the existing data points, the algorithm estimates the values of missing samples, contributing to a more continuous and coherent audio signal.
