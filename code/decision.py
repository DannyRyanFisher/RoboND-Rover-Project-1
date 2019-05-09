
#    decision.py contains the class structure and state behaviour of the mars 
#    rover in the Unity simulator. 

import numpy as np
from rover_commands_2 import Driving, Steering
from rover_commands_3 import Navigate, ThrottledDrive
class Decision():

    def decision_step(Rover):

        a = Navigate(Rover)
        Rover = a.drive_and_steer_responsively()

        b = Steering(Rover)
        b.steer_median_biased_left()

        #b = ThrottledDrive(Rover)
        #b.run()

        return Rover

