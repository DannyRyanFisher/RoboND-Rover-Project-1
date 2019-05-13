#   The highest order class here is NavPixelsInSegment; When initialised it 
#   contains information (self.left, self.right, self.front) which indicates
#   how many navigable pixels are in the corresponding segments


import numpy as np

class NavPixels():

    def __init__(self):
        self.right = None
        self.left = None
        self.front = None

class NavPixelLimits():

    def __init__(self, Rover):
        self.Rover = Rover 
        self.front = np.full((len(self.Rover.nav_angles)), 0.2)
        self.left_lower = np.full((len(self.Rover.nav_angles)), 0.2)
        self.left_upper = np.full((len(self.Rover.nav_angles)), 0.6)
        self.right_lower = np.full((len(self.Rover.nav_angles)),-0.6)
        self.right_upper = np.full((len(self.Rover.nav_angles)), -0.2)
              

class NavPixelsInSegment(NavPixels):

    def __init__(self, Rover):
        self.Rover = Rover
        self.limits = NavPixelLimits(self.Rover)
        self.left_upper =  None
        self.right_upper = None
        self.right_lower = None
        self.magnitude_of_nav_pixels = np.absolute(Rover.nav_angles)
        NavPixels.__init__(self)

        self.update_all_values()


    def determine_rover_pixels_less_than_limit(self, limit):
        return self.Rover.nav_angles < limit

    def determine_rover_pixels_greater_than_limit(self, limit):
        return self.Rover.nav_angles > limit

    def update_all_values(self):
        self.left_upper = \
            self.determine_rover_pixels_less_than_limit(self.limits.left_upper)
        self.left_lower = self.determine_rover_pixels_greater_than_limit(\
                self.limits.left_lower)
        self.right_upper = self.determine_rover_pixels_less_than_limit(\
                self.limits.right_upper)
        self.right_lower = self.determine_rover_pixels_greater_than_limit(\
                self.limits.right_lower)
        self.front = sum(self.magnitude_of_nav_pixels < self.limits.front)
        self.left = sum(self.left_upper & self.left_lower)
        self.right = sum(self.right_upper & self.right_lower)
        return 

