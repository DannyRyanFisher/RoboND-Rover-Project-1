#   This file contains the class which uses the navigable pixels to determine which state the rover should adopt.


# determine navigable state should determine whether to:

#   - Crawl wall
#   - Stop
#   - Turn around in a dead-end scenario
#   - Partially turn in an almost dead-end scenario
#   - Reverse if stuck

# this file does not include rock identification or related states

from navigable_pixels import NavPixelsInSegement
import numpy as np


# Combinations of low nav pixs requiring different rover nav state
# front                 (CONVEX WALL, STEER LEFT)
# right & front         (DEAD END EXIT LEFT)
# left & front          (DEAD END EXIT RIGHT)
# left & front & right  (DEAD END)

class RoverNavStateConditionObject():

    def __init__(self, Rover):
        self.navpixsegment = NavPixelsInSegment(Rover)
        self.condition_value_array = np.empty(4, dtype = np.int8)

        self.create_condition_array()
    def create_condition_array(self):

        self.condition_array[0] = self.navpixsegment.front
        self.condition_array[1] = self.navpixsegment.front + \
                self.navpixsegment.right
        self.condition_array[2] = self.navpixsegment.front + \
                self.navpixsegment.left
        self.condition_array[3] = self.navpixsegment.front + \
                self.navpixsegment.left + self.navpixsegment.right

        return

    def run(self):

        dictionary = {
                0: "action1"
                1: "action2"
                2: "action2"
                3: "action4" }

        for i in self.condition_array_value[i]:
            if self.condition_array_value[i] > 80:
                if dictionary.get(i) == "action1":
                    self.action1()
                elif dictionary.get(i) == "action2":
                    self.action2()
                elif dictionary.get(i) == "action3":
                    self.action3()
                elif dictionary.get(i) == "action4":
                    self.action4()
                else:
                    print("Action failed")

        return

    def action1(self):
        print("Do action 1")
        return

    def action2(self):
        print("Do action 2")
        return

    def action3(self):
        print("Do action 3")
        return

    def action4(self):
        print("Do action 4")
        return


class ConditionObject():

    def __init__(self, Rover):
        self.conditions = RoverNavStateConditions(Rover)


class RoverNavState():

    def __init__(self, Rover):
        self.conditions = RoverNavStateConditions(Rover)


    def determine_action(self):

        for i in self.conditions.condition_array[i]:
            if self.conditions.condition_array[i] > 80:

