# Search and Sample return project

## Description

This project is derived from the NASA Human Exploration Rover Challenge which provides the participants with a simulated Martian environment within which the Curiosity Rover must collect rock samples for testing, whilst also mapping the previously unknown environment. 

drive_rover.py, decision.py and perception.py are the main 3 modules used to run a simulation in Unity environment called Roversim. More information on the project including the set-up and how to run the code are included below.

## How to run the code

- Firstly yRover_Project_Test_Notebook.ipynb is and select it. Run the cells in the notebook from top to bottom to see the various data analysis steps.

The last two cells in the notebook are for running the analysis on a folder of test images to create a map of the simulator environment and write the output to a video. These cells should run as-is and save a video called test_mapping.mp4 to the output folder. This should give you an idea of how to go about modifying the process_image() function to perform mapping on your data.ou must download the Unity Roversim simulator (instructions below)
- Secondly navigate to the code folder and run:

      python drive_rover.py
      
- Next you must run the Roversim executable file, and select 'Autonomous mode' for drive_rover.py to be able to control the rover.
- Lastly, sit back and watch the rover collect the rock samples and map the environment. On screen telemetry provides the data informing on how the rover is performing.

## The Simulator
The first step is to download the simulator build that's appropriate for your operating system.  Here are the links for [Linux](https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Linux_Roversim.zip), [Mac](	https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Mac_Roversim.zip), or [Windows](https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Windows_Roversim.zip).  

You can test out the simulator by opening it up and choosing "Training Mode".  Use the mouse or keyboard to navigate around the environment and see how it looks.

## Dependencies
You'll need Python 3 and Jupyter Notebooks installed to do this project.  The best way to get setup with these if you are not already is to use Anaconda following along with the [RoboND-Python-Starterkit](https://github.com/ryan-keenan/RoboND-Python-Starterkit). 


Here is a great link for learning more about [Anaconda and Jupyter Notebooks](https://classroom.udacity.com/courses/ud1111)

## Recording Data
I've saved some test data for you in the folder called `test_dataset`.  In that folder you'll find a csv file with the output data for steering, throttle position etc. and the pathnames to the images recorded in each run.  I've also saved a few images in the folder called `calibration_images` to do some of the initial calibration steps with.  

The first step of this project is to record data on your own.  To do this, you should first create a new folder to store the image data in.  Then launch the simulator and choose "Training Mode" then hit "r".  Navigate to the directory you want to store data in, select it, and then drive around collecting data.  Hit "r" again to stop data collection.

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

- Steering.steer_proportionally_to_mean_nav_angle() is currently the best steering and driving function


### Problems to fix
- Rover does not stop at a dead end. A proximity indicator is needed. Potentially integrate this with the navigation around obstacles

- Rover drives into obstacles too easily. If an obstacle is in the middle of the rover's route, the average/ median angle to navigate by is still in the middle causing the rover to drive into the obstacle ahead. 

- Steering.steer_median_left_biased() is not able to determine a corect path with large rock in middle of the map. Photo in ./photos
    - It also struggles to drive down a narrow path to the right as it is driving too quickly.
    - It struggles with convexed wall when it approaches and drives straight into the wall 

### Problems FIXED
- Slow steering response. Not very responsive to the wall

- Driving.drive_to_specified_speed()
	Throttle 0.6 and brake 0.1 are constantly on, providing a reasonable speed however always increasing. This also results in no increase in speed once the rover is stopped in manual mode.
