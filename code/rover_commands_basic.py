#   This file contains the basic rover commands which control the simulated 
#   rover in the Rover() class


class RoverCommandsBasic():

    def __init__(self, Rover):
        self.Rover = Rover


    def drive_forwards_at_throttle_set(self):

        self.Rover.throttle = self.Rover.throttle_set

        return

    def drive_forwards_at_custom_throttle(self, throttle):

        self.Rover.throttle = throttle

        return

    def drive_backwards_at_throttle_set(self):

        self.Rover.throttle = -self.Rover.throttle_set

        return

    def release_throttle(self):

        self.Rover.throttle = 0

        return

    def apply_brakes_at_brake_set(self):

        self.Rover.brake = self.Rover.break_set

        return

    def apply_brakes_lightly(self):

        self.Rover.brake = 0.1

        return


    def release_brakes(self):

        self.Rover.brake = 0

        return

    def steer_right(self):

        self.Rover.steer = -5

        return

    def steer_left(self):

        self.Rover.steer = 5

        return

    def turn_right(self):

        self.Rover.steer = -15

        return

    def turn_left(self):

        self.Rover.steer = 15

        return

    def release_steering(self):

        self.Rover.steer = 0

        return


    def drive_forwards_whilst_steering_left(self):

        self.Rover.commands_basic.drive_forwards_at_throttle_set()
        self.Rover.commands_basic.steer_left()

        return

    def drive_forwards_whilst_steering_right(self):

        self.Rover.commands_basic.drive_forwards_at_throttle_set()
        self.Rover.commands_basic.steer_right()

        return

    def coast(self):

        self.release_brakes()
        self.release_throttle()
        self.release_steering()

        return
