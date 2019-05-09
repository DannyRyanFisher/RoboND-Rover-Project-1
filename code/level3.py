#   This file contains the 3rd layer of functionality for the Rover class

from rover_commands import Proxmity, Driving

class ThrottledDrive(Proximity, Driving):

    def __init__(self, Rover):
        self.Rover = Rover
        Proximity.__init__(self, Rover)
        Driving.__init__(self, Rover)
        self.determine_proximity()

    def run(self):

        if self.Rover.brake >0:
                Rover_commands_basic.coast(self.Rover)

        if self.proximity_array[0] == True:
                self.drive_slow_speed()
        elif self.proximity_array[1] == True:
                self.drive_slow_speed()
        else:
                self.drive_full_speed()

        return	

    def drive_full_speed(self):

        self.drive_to_specified_speed(3)

        return

    def drive_slow_speed(self):

        self.drive_to_specified_speed(2)

        return

    def brake_and_turn(self):

        self.apply_brakes_at_brake_set()
        time.delay(1)
        self.turn_right()

        return

class Navigate():

    def __init__(self, Rover):
        self.Rover = Rover
        self.steering_instance = Steering(Rover)
        self.driving_instance = Driving(Rover)

    def drive_and_steer(self):

        self.Rover = self.steering_instance.steer_proportionally_to_mean_nav_angle()
        self.Rover = self.driving_instance.drive_to_specified_speed(2)

        return self.Rover

    def drive_and_steer_responsively(self):

        self.Rover = self.steering_instance.steer_to_median_nav_angle()
        self.Rover = self.driving_instance.drive_to_specified_speed(2)

        return self.Rover
