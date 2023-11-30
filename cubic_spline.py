# -------------------------------Computational Methods(5c22)-----------------------------------------------
#-------------------------------------ASSIGNMENT-2---------------------------------------------------------
#--------------------------------STUDENT NUMBER: 23349040--------------------------------------------------
from sklearn.metrics import mean_squared_error
from scipy.io import wavfile
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import scipy.io
from scipy.io.wavfile import write
from datetime import datetime
from time import sleep
from tqdm import tqdm
from playsound import playsound

def plot_signal(signal_data, signal_sample_rate):

    '''Cubic spline interpolation is a mathematical method used to construct 
    a smooth curve that passes through a set of given points. It is particularly useful 
    for interpolating missing samples in a signal. Cubic spline interpolation can be applied 
    to reconstruct missing or distorted audio samples.'''

    signal_length = signal_data.shape[0] / signal_sample_rate
    signal_time = np.linspace(0., signal_length, signal_data.shape[0])
    plt.figure(figsize=(15, 5))
    plt.plot(signal_time, signal_data, label="Degraded Signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    return plt.show()

clean_sample_rate, clean_data = wavfile.read("clean.wav")
degraded_sample_rate, degraded_data = wavfile.read("degraded.wav")

# Plotting the input waveform
input_waveform = plot_signal(degraded_data, degraded_sample_rate)

# Assigning the detection file to the variables
click_points_data = scipy.io.loadmat('detection.mat')
click_signal_key = click_points_data['click_detection']

click_positions = np.where(click_signal_key == 1)
actual_clicks = click_positions[0]
num_clicks = len(actual_clicks)

degraded_index = np.arange(len(degraded_data))
filtered_data = np.delete(degraded_data, actual_clicks)
filtered_index = np.delete(degraded_index, actual_clicks)

start_time_value = datetime.now()

cubic_splined_data = degraded_data

#Progress bar for visual feedback
for s in tqdm(range(100)):
    cs = CubicSpline(filtered_index, filtered_data, bc_type='natural')

for i in range(num_clicks):
    cubic_splined_data[actual_clicks[i]] = cs(actual_clicks[i])

#The time take using cubi spline
end_time_value = datetime.now()
duration_time_value = end_time_value - start_time_value
print('Done')
print("The time taken is " , str(duration_time_value))

cs_data = plot_signal(cubic_splined_data, clean_sample_rate)

write("restored_audio_cubic.wav", degraded_sample_rate, cubic_splined_data.astype(np.int16))

#Formatting the waveform to get mean square error in simpler values
detected_clicks=134
clean_data= clean_data/2**16
cubic_splined_data= cubic_splined_data/2**16

#Calculating Mean Square Error
mse= np.sum(((clean_data-cubic_splined_data)**2)/detected_clicks)

# mse = (np.square(np.subtract(cubic_splined_data, clean_data)).mean())
print("The Mean Squar Error for cubic spline is : ",  mse)

#Paying both the audio to see the difference
print("Playing degraded audio")
playsound(r"C:\Users\sujathaa\Desktop\5c22\python lab\degraded.wav")

print("Restored audio using Cubic Spline")
playsound(r"C:\Users\sujathaa\Desktop\5c22\python lab\restored_audio_cubic.wav")

