# -------------------------------Computational Methods(5c22)-----------------------------------------------
#-------------------------------------ASSIGNMENT-2---------------------------------------------------------
#--------------------------------STUDENT NUMBER: 23349040-------------------------------------------------
import sys
import numpy as np
import scipy
from scipy.io import wavfile
import scipy.signal
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from sklearn.metrics import mean_squared_error
from datetime import datetime
from time import sleep
from tqdm import tqdm
from playsound import playsound
import unittest


# Function for calculating median filter 
def calculate_median(sorted_values):
    
    middle_index = int(len(sorted_values) / 2)
    median_value = sorted_values[middle_index]
    return median_value

# Function for applying median filter on the degraded audio
def apply_median_filter(signal, click_positions, num_clicks, window_size):
    """
    Perform median filtering to restore degraded audio to its clean audio version.

    This function takes the degraded audio signal and the positions of detected clicks,

    typically obtained during AR interpolation in Assignment 1. It applies median filtering

    around the detected click positions to remove artifacts and enhance the audio quality. """

    filtered_signal = signal
    for click_index in range(num_clicks):        
        signal_segment = signal[click_positions[click_index] - half_window: click_positions[click_index] + (half_window + 1)]        
        padded_signal = zero_padding(window_size, half_window, signal_segment)        
        sorted_signal = np.sort(padded_signal)        
        median_value = calculate_median(sorted_signal)        
        filtered_signal[click_positions[click_index] - half_window: click_positions[click_index] + (half_window + 1)] = median_value
    return filtered_signal


# Function for padding
def zero_padding(window_size, half_window, signal_segment):
    '''Applies zero padding to a signal segment to facilitate median filtering.

    Median filtering involves taking the median value within a moving window or kernel.
    When the window extends beyond the signal boundaries, zero padding is crucial to
    handle edge effects and ensure consistent filtering behavior.  

    Why Zero Padding is Important for Median Filtering:
    1. Avoiding Edge Effects: Zero padding prevents edge effects by extending the signal with zeros.
    2. Preserving Signal Length: Ensures the length of the filtered signal matches the original signal.
    3. Consistent Behavior: Provides consistent handling of edge values during the filtering process.'''

    if window_size % 2 != 0:
        
        return np.pad(signal_segment, (half_window, half_window), 'constant', constant_values=(0, 0))
    else:
        print("SEE TO YOUR WINDOW SIZE")
        sys.exit()


# Function to plot the Audio graphs
def plot_signal(signal, sample_rate):
    
    signal_length = signal.shape[0] / sample_rate
    time_values = np.linspace(0., signal_length, signal.shape[0])
    plt.figure(figsize=(10, 5))  
    plt.plot(time_values, signal, label="Degraded Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    return plt.show()

# Creating a copy of the original audio signal for preservation.
sample_rate, audio_signal = wavfile.read("degraded.wav")
audio_signal_copy = audio_signal

filtered_signal = audio_signal

# Displaying the input waveform.
input_waveform = plot_signal(audio_signal, sample_rate)

#Detection file is taken from Assignment-1
click_points_data = scipy.io.loadmat('detection_clicks.mat')

# Extracting the click signal key from the loaded data.
click_signal_key = click_points_data['click_detection']

click_positions = np.where(click_signal_key == 1)

actual_clicks = click_positions[0]

num_clicks = len(actual_clicks)

# Setting the window size
window_size = 7
half_window = int((window_size - 1) / 2)
start_time_value = datetime.now()

#The progress bar for visual feedback
for s in tqdm(range(100)):
    sleep(0.05)

filtered_signal = apply_median_filter(audio_signal, actual_clicks, num_clicks, window_size)

print("Done")
end_time_value = datetime.now()
duration_time_value = end_time_value - start_time_value
print("The time taken is " , str(duration_time_value))

# Plotting the restored value
output_waveform = plot_signal(filtered_signal, sample_rate)

# Creating and playing the restored audio
write("restored_audio.wav", sample_rate, filtered_signal.astype(np.int16))

# Reading the original file
new_sample_rate, clean_audio = wavfile.read("clean.wav")

#Converting the format to calculate mse to get in simpler value
detect_clicks=134
clean_audio= clean_audio/2**16
filtered_signal= filtered_signal/2**16
audio_signal_copy= audio_signal_copy/2**16
mean_error= np.sum(((clean_audio- filtered_signal)**2)/detect_clicks)

#Calculating mean squared error
# mse = (np.square(np.subtract(filtered_signal, clean_audio).mean()))
print("The MEAN SQUARE ERRROR IS:  ", mean_error)

# Playing degraded signal
print("Degraded audio")
playsound(r"C:\Users\sujathaa\Desktop\5c22\python lab\degraded.wav")

# Playing restored signal
print("Restored audio using median filter")
playsound(r"C:\Users\sujathaa\Desktop\5c22\python lab\restored_audio.wav")



#Unittest checking
class TestFilter(unittest.TestCase):
    

    def test_length(self):   
        length_filtered_signal = len(filtered_signal)
        length_audio_signal_copy = len(audio_signal_copy)
        self.assertEqual(length_filtered_signal, length_audio_signal_copy)

    def test_value_of_data(self):
        
        half_window_value = int((window_size - 1) / 2)

        for y in range(num_clicks):
            signal_segment = audio_signal_copy[actual_clicks[y] -
                                              half_window_value: actual_clicks[y] + (half_window_value + 1)]

            test_segment = scipy.signal.medfilt(signal_segment, kernel_size=window_size)

            filtered_signal[actual_clicks[y] -
                            half_window_value: actual_clicks[y] + (half_window_value + 1)] = test_segment

        check = np.array_equal(filtered_signal, audio_signal_copy)
        

# Executes the test case
if __name__ == '__main__':
    unittest.main()


