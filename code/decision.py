
#    decision.py contains the class structure and state behaviour of the mars 
#    rover in the Unity simulator. 

import numpy as np
from rover_commands import Rover_commands_basic, Navigate, Proximity, Driving, ThrottledDrive 

class Rover_Behaviours(Rover_commands_basic):

	def drive_using_mean_nav_angles(Rover):

		print("This is the nav_angles value", np.mean(Rover.nav_angles))

		if np.mean(Rover.nav_angles) < 0:
			print("1st if statement")
			Rover_Behaviours.drive_forwards_whilst_steering_right(Rover)
			
		else: 
			print("2nd if statement")
			Rover_Behaviours.drive_forwards_whilst_steering_left(Rover)

		return

	def adjustable_steering_magnitude(Rover):

		a = np.mean(Rover.nav_angles) < 0


		return

class Decision(Rover_Behaviours, Rover_commands_basic):

	def decision_step(Rover):

		a = Navigate(Rover)
		Rover = a.drive_and_steer()

		b = ThrottledDrive(Rover)
		b.run()

		return Rover

	## I have chosen to use staticmethod below in case I want the nstance to use the unbound, static method.
	
	@staticmethod  
	def print_nav_obs_rock_dists_and_angles(Rover):

		print("The full list of dist and angles" )
		print("Nav dist" , Rover.nav_dist)
		print("Nav angles" , Rover.nav_angles)
		print("obs dist" , Rover.obs_dist)
		print("obs angles" , Rover.obs_angles)
		print("rock dist" , Rover.rock_dist)
		print("rock angles" , Rover.rock_angles)

		return
