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
