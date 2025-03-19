import scipy.io
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load source data
data = scipy.io.loadmat('exp_IRs_data.mat')
motions = data['motions']

# Define variable
X = []
Y = []
Z = []
actual_lengths_X = []  
actual_lengths_Y = [] 



for i in range(16):
    motion_name = f'motion_{i}'
    motion_data = motions[0, 0][motion_name][0, 0]

    
    for j in range(100):
        path_name = f'path_{j}'
        path_data = motion_data[path_name][0, 0]

        #load data
        test_power = path_data['measured_apparent_power']
        test_time = path_data['measured_time']
        test_timestamps = path_data['measured_timestamps']

        test_position = path_data['measured_IRs_position']
        test_velocity = path_data['measured_IRs_velocity']
        test_acceleration = path_data['measured_IRs_acceleration']
        time_start_timestamp = path_data['time_start_timestamp']
        time_end_timestamp = path_data['time_end_timestamp']

        # Processing format
        test_time_series = pd.Series(test_timestamps.flatten())
        
        
        # Gets a valid partial index
        start_time_scalar = time_start_timestamp.item()
        end_time_scalar = time_end_timestamp.item()
        start_index = test_time_series[test_time_series == start_time_scalar].index[0]
        end_index = test_time_series[test_time_series == end_time_scalar].index[0]

        # Intercept the valid part
        selected_power = test_power[start_index:end_index + 1, :]
        selected_time = test_time[start_index:end_index + 1, :]
        selected_time = selected_time - selected_time[0, 0]
        selected_test_position = test_position[start_index:end_index + 1, :]
        selected_test_velocity = test_velocity[start_index:end_index + 1, :]
        selected_test_acceleration = test_acceleration[start_index:end_index + 1, :]


        # Calculate total energy consumption
        selected_time = selected_time.flatten()
        time_differences = np.diff(selected_time)
        average_power = (selected_power[:-1] + selected_power[1:]) / 2
        average_power = average_power.flatten()
        total_energy_consumption = np.sum(average_power * time_differences)


        # Save effective length
        actual_lengths_X.append(len(selected_time))
        actual_lengths_Y.append(len(selected_power))

        
        features = np.concatenate([selected_test_position,selected_test_velocity,
                                   selected_test_acceleration], axis=1)

        # Add to data set
        X.append(features)
        Y.append(selected_power)
        Z.append(total_energy_consumption)


# Find the maximum length of the trajectory
maxlen_X = max(actual_lengths_X) 
maxlen_y = max(actual_lengths_Y) 

# Padding, 9999.0 does not appear in the trajectory
X_padded = pad_sequences(X, padding='post', dtype='float32', maxlen=maxlen_X,value = 9999.0)
Y_padded = pad_sequences(Y, padding='post', dtype='float32', maxlen=maxlen_y,value = 9999.0)

#Transformation format
X_padded = np.array(X_padded)
Y_padded = np.array(Y_padded)
Z = np.array(Z)
actual_lengths_X = np.array(actual_lengths_X)
actual_lengths_Y = np.array(actual_lengths_Y)


#print the shape of the data
print("X_padded shape:", X_padded.shape)
print("Y_padded shape:", Y_padded.shape)
print("Z shape:", Z.shape)
print("actual_lengths_X shape:", actual_lengths_X.shape)
print("actual_lengths_Y shape:", actual_lengths_Y.shape)


#save the data
np.savez('processed_IRs_data.npz', X=X_padded, Y=Y_padded, Z=Z, actual_lengths_X=actual_lengths_X, actual_lengths_Y=actual_lengths_Y)
