# Search and Sample return project

## Description

This project is derived from the NASA Human Exploration Rover Challenge which provides the participants with a simulated Martian environment within which the Curiosity Rover must collect rock samples for testing, whilst also mapping the previously unknown environment. 

There are two main files that this repository contains: drive_rover.py and Rover_Project_test_Notebook.ipynb. The Python Notebook contains all of the developmental code. Once the individual functions worked, they were then integrated into the drive_rover.py file (and its sub-files). 

## Before you run the code

### Setup the conda environment

- Ensure Anaconda is installed. To install Anaconda (https://docs.anaconda.com/anaconda/install/) follow the appropriate links for your operating system.

- With Anaconda installed, you will need to set up the environment which will run the code. To do this follow the following steps below in a temporary directory. 


	git clone https://github.com/ryan-keenan/RoboND-Python-Starterkit

	conda env create --file environment.yml -n myEnvironmentName   

	conda activate myEnvironmentName


- You now have an environment which is capable of runnning the repository code successfully and is isolated from your current computer environment.

### Install the Simulator
To download the simulator build that's appropriate for your operating system.  Here are the links for [Linux](https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Linux_Roversim.zip), [Mac](	https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Mac_Roversim.zip), or [Windows](https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Windows_Roversim.zip).  
You must allow Roversim to be executable first, before running the file in the next section. Please search how to do this for your own operating system. 

- With the environment active, you should now be able to run the code as below.

## How to run the code

- Navigate to the code folder and run:

      python drive_rover.py
      
- Next you must run the Roversim executable file, and select 'Autonomous mode' for drive_rover.py to be able to control the rover.

- Lastly, sit back and watch the rover collect the rock samples and map the environment. On screen telemetry provides the data informing on how the rover is performing.


## Recording Data
To record your own data you should first create a new folder to store the image data in.  Then launch the simulator and choose "Training Mode" then hit "r".  Navigate to the directory you want to store data in, select it, and then drive around collecting data.  Hit "r" again to stop data collection.

## Specification

### Summary

A robot which is able to navigate the simulated environment, be able to complete mapping to a 90% level with a fidelity of 90% within 5 minutes. The rover should also be able to collect 5 out of 6 rock samples within this time. 

### Structure specification (incomplete)

#### Navigation
1.1 Rover should drive on the ground only and manoeuvre around obstacles
	1.1.1 Rover should be capable of driving around obstacles without making contact with them
	1.1.2 Rover should be capable of driving within the walls without making contact with them
	1.1.3 Rover should not get stuck for more than 10 seconds
	1.1.4 Rover should be able to manoeuvre out of dead-end scenarios

1.2 Rover should use a follow wall technique to optimise the mapping efficiency


#### Mapping

* Items of interest are rocks, obstacles, walls, ground.

2.1 Rover should log all items of *interest* 
	2.1.1 The items of interest should be displayed on the ground truth map 
		2.1.1.1 Obstacles and walls should be coloured in red
		2.1.1.2 The ground (navigable terrain) should be coloured in blue
		2.1.1.3 Rocks should be coloured in white

#### Collecting rock samples

3.1 Rover must identify when it has located a rock
	3.1.1 Rover must display a figure on the telemetry output onscreen denoting it has located a rock
		3.1.1.1 Must display this on the map
		3.1.1.2 This must be displayed in the on-screen telemetry read-out

3.2 Rover must be able to navigate to the rock
	3.2.1 Rover must navigate to within xx metres (close enough to allow the robotic arm to successfully grasp the sample)
	3.2.2 Rover must approach the rock with the rock in front of the rover and the rover driving forwards

3.3 Rover must be able to collect the rock sample
	3.3.1 Rover must collect the rock sample with a success rate of 90%
	3.3.2 Rover must collect the sample with the rock in full view of the onboard, forwadly mounted camera.

### Notes

- What do I need to determine? How to navigate throughout the environment.

- NavPixelsInSegment and the .front, .left, .right values only register the number of points in the segment and do not take into account the magnitude of nav_dists

### Problems to fix
- Rover does not stop at a dead end. A proximity indicator is needed. Potentially integrate this with the navigation around obstacles


- Steering.steer_median_left_biased() is not able to determine a correct path with large rock in middle of the map. Photo in ./photos
    - It also struggles to drive down a narrow path to the right as it is driving too quickly.
    - It struggles with convexed wall when it approaches and drives straight into the wall 

- A combined nav_dists and nav_angles navigation would provide a method for determining the direction ahead which has the greatest potential for furhter exploration.

### Problems FIXED
- Slow steering response. Not very responsive to the wall

- Median steering angles causing a steering angle value of 0 intermittently on the outfeed. This had eventually caused the rover to crash into walls and obstacles as it was far less responsive. Median steering approximations to steering angle have been changed to mean and the values for steering left biased has been added to photo 4 in the appropriate project folder.

- Rover drives into obstacles too easily. If an obstacle is in the middle of the rover's route, the average/ median angle to navigate by is still in the middle causing the rover to drive into the obstacle ahead. 

- Driving.drive_to_specified_speed()
	Throttle 0.6 and brake 0.1 are constantly on, providing a reasonable speed however always increasing. This also results in no increase in speed once the rover is stopped in manual mode.
