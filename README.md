# Audio-Restoration using median filter and cubic_splines

## Introduction

Audio restoration is critical to signal processing, addressing challenges such as noise reduction and reconstruction of distorted samples. 
The assigned Task 2 is about dealing with clicks using median filtering and cubic spline interpolation, in the context of audio signal enhancement.
Through their distinct approaches, these methods aim to refine audio quality by mitigating noise and interpolating missing or distorted components.

## Background

After performing AR interpolation in Matlab gave a clear idea regarding the positions of 
the clicks and estimated and replaced the value in the place of clicks. The position of the 
clicks is downloaded from Matlab, which is further used in median filtering and cubic spline.

## Audio Restoration using Median Filter

Median filtering is a nonlinear filtering technique commonly used in image and signal processing. It replaces each sample in a signal with the median value of neighboring samples within a specified window. Median filtering proves effective in reducing impulse noise and outliers. By identifying and replacing extreme values with the median, the algorithm mitigates the impact of sudden spikes or drops in the audio signal.

- ### Steps:


  - #### **Filtering Process:**
     - Utilizes zero padding for handling edge effects during median filtering.
     - `apply_median_filter` function is employed for filtering around detected click positions, leading to signal restoration.

  - #### **Visualizations:**
      - Generates visualizations of the original degraded signal and the restored signal using Matplotlib.

- ### Metrics:

   - Calculates mean squared error (MSE) between the restored and clean audio as a quantitative measure of restoration quality.

- ### Output:

   - Saves restored and degraded audio signals as WAV files.

- ### Feedback:

   - Auditory evaluation facilitated by the `playsound` library.
   - Unit tests using the `unittest` library ensure the correctness of the filtering process.

- ### Approach:

  - Offers a comprehensive approach to audio restoration with a median filter.
  - Combines visualizations, quantitative assessments (MSE calculation), and auditory feedback for enhanced quality.


## Audio Restoration using Cubic Splines

Cubic spline interpolation is a mathematical method used to construct a smooth curve that passes through a set of given points. It is particularly useful for interpolating missing samples in a signal. Cubic spline interpolation can be applied to reconstruct missing or distorted audio samples. By fitting a cubic spline curve to the existing data points, the algorithm estimates the values of missing samples, contributing to a more continuous and coherent audio signal. 


- ### **Steps:**
  - Load degraded and clean audio.
  - Visualize degraded signal.
  - Detect error positions based on precomputed clicks.
  - Apply cubic spline for smoothing and restoration.

- ### **Metrics:**
  - Measure filter duration.
  - Calculate MSE for restoration quality.

- ### **Output:**
  - Save as "restored_audio_cubic.wav."

- ### **Feedback:**
  - Play both degraded and restored audio.

- ### **Approach:**
  - Comprehensive: combines visualization, MSE analysis, and auditory feedback.
