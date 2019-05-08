## Absolute_arrays() and Determine_array_is_in_range() have not been tested
## All code in this file has been pasted and therefore does not run as per.


class Detect_navigable_terrain():

    def __init__(self, Rover):
        self.Rover = Rover
        self.navigable_array = np.empty(3, dtype = bool)
        self.right_pixels = None
        self.left_pixels = None
        self.front_pixels = None


    def return_pixels_front(self):
        a = self.Rover.nav_angles
        a = np.absolute(a)
        b = np.full((len(self.Rover.nav_angles)), 0.2)
        c = sum(a < b)
        self.front_pixels = c
        print("Number of pixels in front (within +/- 0.2 rads", c)

        return self.Rover



    def return_pixels_left(self):
        a = self.Rover.nav_angles
        b = np.full((len(self.Rover.nav_angles)), 0.2)
        c = np.full((len(self.Rover.nav_angles)), 0.6)
        e = a > b 
        f = a < c
        d = e & f
        d = sum(d)
        self.left_pixels = d 
        print("Pixels within 0.2 to 0.6", d)

        return self.Rover


    def return_pixels_right(self):
        a = self.Rover.nav_angles
        b = np.full((len(self.Rover.nav_angles)), -0.2)
        c = np.full((len(self.Rover.nav_angles)), -0.6)
        e = a < b 
        f = a > c
        d = e & f
        d = sum(d)
        self.right_pixels = d
        print("Pixels within -0.2 to -0.6", d)

        return self.Rover


    def determine_navigable_direction(self):
        self.navigable_array = ([self.left_pixels, self.front_pixels, self.right_pixels])
        max_value = np.argmax(self.navigable_array)

        print("LEFT, INFRONT, RIGHT", self.navigable_array)
    #	if max_value == 0:
    #		print(" STEER LEFT ")
    #	elif max_value == 1:
    #		print("CONTINUE STRAIGHT")
    #	else: 
    #		print(" STEER RIGHT ")
    	return 


    def run_navigable_sequence(self):

        self.return_pixels_left()
        self.return_pixels_right()
        self.return_pixels_front()

        self.determine_navigable_direction()

        time.sleep(1)

        return self.Rover

class Nav_array():

    def __init__(self,Rover):

        self.distances = Rover.nav_dist
        self.angles = Rover.nav_angles
        self.array = np.vstack((self.distances, self.angles))

class Combining_two_general_arrays():

    def __init__(self, array1, array2)
        self.array1 = array1
        self.array2 = array2
        self.2d_array = np.vstack((self.array1, self.array2))
                            
class Absolute_arrays():

    def __init__(self):
        self.absolute_array_lower = None
        self.absolute_array_upper = None
        self.absolute_array = None


class Determine_array_is_in_range(Absolute_arrays):

    def __init__(self, array,  range_lower, range_upper):
        self.array = array
        self.range_lower = range_lower
        self.range_upper = range_upper

        Absolute_arrays.__init__()

            

    def define_absolute_arrays(self):

        filled_array_lower = np.full((len(self.array)),self.range_lower)
        filled_array_upper = np.full((len(self.array)),self.range_upper)

        self.absolute_array = abs(self.array)
        self.absolute_array_lower = abs(filled_array_lower)
        self.absolute_array_upper = abs(filled_array_upper)
        
        return

    def determine_number_of_array_values_in_range(self):

        values_greater_than_lower_limit = self.absolute_array_lower < self.array
        values_less_than_upper_limit = self.absolute_array_upper > self.array

        array_values_in_range = values_greater_than_lower_limit & values_less_than_upper_limit
        
        return sum(array_values_in_range)
