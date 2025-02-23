
# **The files in this folder are related to the paper:"Energy Consumption Modeling for Industrial Robots: A Dual-Stage Coupled Framework with Error Compensation Mechanism".**

Look at the paper for more details.

If you found any problem, please communicate it at:
q.x.zhou.work@gmail.com

The Authors:
Qiangxiao Zhou, Yiheng Wang, Hai Xiong and Long Cheng


## File description:  The folder contains three files

exp_IRs_data_split    : It includes all the data collected by industrial robots. 

load_and_preprocess_data.py     : Help you load and process data. (Processing the data into a dataset that the neural network can use)

Note: Due to the github platform's maximum file size, we split the data file into several parts, and you need to run the meger.py code to combine the data before using it. When you merge, you will get exp_IRs_data.mat, which contains the complete data. The instructions for using the data are explained below.

## exp_IRs_data.mat


The document contains 1600 tracks with energy consumption measurements. 
The 1,600 pieces of data are divided into 16 groups, and the difference between the groups is mainly the speed and acceleration Settings.
Speed and acceleration are set to four grades, which are [100,75,50,25] % of the maximum speed and acceleration of the robot arm.

Each groups of data consists of 100 paths,  including 50 pairs of back and forth paths.



| DATA     |  SIZE    |   MEASUREMENT UNIT |
 |---- | ---- | ---- | 
| motions.simulation_start_config	|	[1,1]  | 	[°] |
| motions.simulation_goal_config	|	[1,1]  | 	[°] |
| motions.simulation_vel_parameters	|	[1,1]	|	[%] |
| motions.simulation_acc_parameters	 | [1,1]	|	[%] |
| motions.simulation_joint_position	 |	[100,6]	| [°] |
| motions.simulation_joint_velocity	|	[100,6]	| [°/s] |
| motions.simulation_joint_acceleration	| [100,6] |	[°/s^2] |
| motions.simulation_joint_time		|	[100,1] |	[s] |
| motions.measured_active_power	|	[n,1] |		[W] |
| motions.measured_reactive_power	|	[n,1]	|	[Var] |
| motions.measured_apparent_power |	[n,1]	|	[VA] |
| motions.measured_voltage	|		[n,1]	|	[V] | 
| motions.measured_current |			[n,1] |		[A] |
| motions.measured_timestamps	|	[n,1]	|	[ns] |
| motions.measured_time	|			[n,1]	|	[s] |
| motions.measured_IRs_position	|		[n,6] |		[°] |
| motions.measured_IRs_velocity	|		[n,6] |		[°/s] |
| motions.measured_IRs_acceleration |	[n,6]	|	[°/s^2] |
| motions.time_start_timestamp	|		[1,1] |		[ns] |
| motionstime_end_timestamp		|	[1,1]	 |	[ns] |








