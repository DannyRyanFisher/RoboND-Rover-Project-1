#    decision.py contains the class structure and state behaviour of the mars 
#    rover in the Unity simulator. 

import numpy as np
from rover_commands_2 import Driving, Steering
from rover_commands_3 import Navigate 
from navigable_pixels import NavPixels, NavPixelLimits, NavPixelsInSegment

class Decision():

    def decision_step(Rover):

        a = Navigate(Rover)
        Rover = a.drive_and_steer_responsively()

        b = Steering(Rover)
        b.steer_mean_biased_left()


#        c = NavPixelsInSegment(Rover)
#        print("FRONT PIXELS", c.front)
#        print("LEFT PIXELS", c.left)
#        print("RIGHT PIXELS", c.right)

        return Rover

