## This file contains all the maneuovering commands that are send to the rover in order to navigate the terrain. It does not include rock grapsing or any decision making.

import numpy as np
import time

class Rover_commands_basic():

        def drive_forwards_at_throttle_set(Rover):

                Rover.throttle = Rover.throttle_set

                return

        def drive_forwards_at_custom_throttle(Rover, throttle):

                Rover.throttle = throttle

                return


        def drive_backwards_at_throttle_set(Rover):

                Rover.throttle = -Rover.throttle_set

                return

        def release_throttle(Rover):

                Rover.throttle = 0

                return

        def apply_brakes_at_brake_set(Rover):

                Rover.brake = Rover.brake_set

                return

        def release_brakes(Rover):

                Rover.brake = 0

                return

        def steer_right(Rover):

                Rover.steer = -5

                return

        def steer_left(Rover):

                Rover.steer = 5

                return

        def turn_right(Rover):

                Rover.steer = -15

                return

        def turn_left(Rover):

                Rover.steer = 15


        def release_steering(Rover):

                Rover.steer = 0

                return


        def drive_forwards_whilst_steering_left(Rover):

                Rover_commands_basic.drive_forwards_at_throttle_set(Rover)
                Rover_commands_basic.steer_left(Rover)

                return

        def drive_forwards_whilst_steering_right(Rover):

                Rover_commands_basic.drive_forwards_at_throttle_set(Rover)
                Rover_commands_basic.steer_right(Rover)

                return

        def coast(Rover):

                Rover_commands_basic.release_brakes(Rover)
                Rover_commands_basic.release_throttle(Rover)
                Rover_commands_basic.release_steering(Rover)

                return

## The aim for the steering class is to provide a steering behaviour which 
## steers with a magnitude proportional to the nav_angles value which the Rover
## receives.

class Driving(Rover_commands_basic):

	def __init__(self, Rover):
		self.Rover = Rover

	def drive_to_specified_speed(self, specified_speed):

		if self.Rover.vel < specified_speed:
			Driving.drive_forwards_at_custom_throttle(self.Rover, 0.6)
		else: 
			Driving.apply_brakes_at_brake_set(self.Rover)

		return self.Rover

class Steering():

	def __init__(self, Rover):
		self.Rover = Rover
		self.steer_angle = np.mean(Rover.nav_angles)
		self.max_steer_value = 15


## NOTE: for steering, steering based on distance may also be needed.
## NOTE: a wall can be defined using minimum of nav angles and nav dists.

	def steer_proportionally_to_mean_nav_angle(self):

		max_nav_angle = 0.8
		# Normalised steering will give a value between -1 and 1.
		normalised_steering = self.steer_angle/max_nav_angle

		steering_output = normalised_steering * self.max_steer_value
		self.Rover.steer = steering_output

		return self.Rover

## Proximity is responsible for the Rover.nav_dist. It identifies 3 levels of proximity; Close, Medium and Far. These proximity outputs are then used in the Measured_Thottle class to integrate the driving beahviour with throttle control.

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

class ThrottledDrive(Proximity, Driving):

	def __init__(self, Rover):
		self.Rover = Rover
		Proximity.__init__(self, Rover)
		Driving.__init__(self, Rover)
		self.determine_proximity()

	def run(self):

		if self.proximity_array[0] == True:
			self.brake_and_turn()
		elif self.proximity_array[1] == False:
			self.drive_slow_speed()
		else:
			self.drive_full_speed()

		self.coast()

		return	

	def drive_full_speed(self):

		self.drive_to_specified_speed(3)

		return

	def drive_slow_speed(self):

		self.drive_to_specified_speed(0.5)

		return

	def brake_and_turn(self):

		self.apply_brakes_at_brake_set(self.Rover)
		time.delay(1)
		self.turn_right(self.Rover)

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


