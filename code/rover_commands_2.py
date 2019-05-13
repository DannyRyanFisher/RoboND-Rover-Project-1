## This file contains all the maneuovering commands that are send to the rover 
## in order to navigate the terrain. It does not include rock grapsing or any 
## decision making.

import numpy as np
import time
from rover_commands_basic import RoverCommandsBasic

## The aim for the steering class is to provide a steering behaviour which 
## steers with a magnitude proportional to the nav_angles value which the Rover
## receives.

class Driving():

    def __init__(self, Rover):
        self.Rover = Rover
        self.commands = RoverCommandsBasic(self.Rover)


    def drive_to_specified_speed(self, specified_speed):

        if self.Rover.vel < specified_speed:
                self.commands.release_brakes()
                self.commands.drive_forwards_at_custom_throttle(0.6)
        else: 
                self.commands.coast()
                #Driving.apply_brakes_lightly()


        return self.Rover



class Steering():

    def __init__(self, Rover):
        self.Rover = Rover
        self.steer_angle = np.mean(Rover.nav_angles)
        self.steer_angle_median = np.median(Rover.nav_angles)
        self.max_steer_value = 15


    def steer_proportionally_to_mean_nav_angle(self):

        max_nav_angle = 0.8
        # Normalised steering will give a value between -1 and 1.
        normalised_steering = self.steer_angle/max_nav_angle

        steering_output = normalised_steering * self.max_steer_value
        self.Rover.steer = steering_output

        return self.Rover

    def steer_to_mean_nav_angle(self):

        # The max nav angle is 0.8 in magnitude and therfore to achieve
        # the aximum steering angle value, it is necessary to divide the
        # Rover.steer value by 0.8.

        self.Rover.steer = self.steer_angle * self.max_steer_value/0.8 

        return self.Rover

    def steer_mean_biased_left(self):

        a = np.clip(self.Rover.nav_angles, -0.3, 0.8)

        self.Rover.steer = (np.mean(a)*15*1.9)/0.8 

        return 



## Proximity is responsible for the Rover.nav_dist. It identifies 3 levels of 
## proximity; Close, Medium and Far. These proximity outputs are then used in 
## the Measured_Thottle class to integrate the driving beahviour with throttle 
## control.

class Proximity():

    def __init__(self, Rover):

        ## Initialise class variables
        self.nav_dist = Rover.nav_dist
        self.max_nav_dist = 0
        self.mean_nav_dist = 0

        ## Values which discriminate the proximity of pixels
        self.close_proximity_value = 20 
        self.medium_proximity_value = 50

        ## 1D array for each close, medium and far proximity values
        self.proximity_array = \
        np.array([False, False, False], dtype=bool)

        if self.mean_nav_dist is not None:
                if np.mean(self.nav_dist) > 5:
                        self.update_variables()


    def update_variables(self):

        self.max_nav_dist = np.max(self.nav_dist)
        self.mean_nav_dist = np.mean(self.nav_dist)

        return


    def determine_proximity(self):


        if self.mean_nav_dist < self.close_proximity_value:
                self.proximity_array[0] = True
        elif self.mean_nav_dist < self.medium_proximity_value:
                self.proximity_array[1] = True
        elif self.mean_nav_dist > self.medium_proximity_value:
                self.proximity_array[2] = True
        else: 
                print("No Proximity Determined")

        print("Array", self.proximity_array)

        return 


