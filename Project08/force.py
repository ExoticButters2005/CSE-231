import copy
import math

"Magnitude: {}"
"\nAngle: {}"
"\nBoth objects must be of the Force class"
"\nForce object {} already exists!"
"\nForce object {} does not exist!"
"\nForce #{}: {}"
"\n{}"

class Force(object):
    """
    """
    def __init__(self, magnitude=0, angle=0):
        """
        """
        self.magnitude = magnitude
        self.angle = angle
        

    def get_magnitude(self):
        """
        """
        return self.magnitude

    def get_angle(self):
        """
        """
        return self.angle

    def get_components(self):
        """
        """
        x = self.magnitude * math.cos(math.radians(self.angle))
        y = self.magnitude * math.sin(math.radians(self.angle))
        return x, y



    def __str__(self):
        """
        """
        return "Magnitude: {:.2f}\nAngle: {:.2f}".format(
            self.magnitude, self.angle
        )

        
    def __eq__(self, other):
        """
        """
        if not isinstance(other, Force):
            raise RuntimeError("Operand is not a Force instance")
        return (
            self.magnitude == other.magnitude 
            and self.angle == other.angle
        )
            
    
    
    def __add__(self, other):
        """
        """
        if not isinstance(other, Force):
            raise RuntimeError("Operand is not a Force instance")
        x_one, y_one = self.get_components()
        x_two, y_two = other.get_components()
        resultant_x = x_one + x_two
        resultant_y = y_one + y_two
        magnitude = math.sqrt(resultant_x**2 + resultant_y**2)
        if resultant_x > 0:
            angle = math.degrees(
                math.atan2(resultant_y, resultant_x))
        elif resultant_x < 0 and resultant_y >= 0:
            angle = math.degrees(
                math.atan2(resultant_y, resultant_x) + math.pi)
        elif resultant_x < 0 and resultant_y < 0:
            angle = math.degrees(
                math.atan2(resultant_y, resultant_x) - math.pi)
        elif resultant_x == 0 and resultant_y > 0:
            angle = 90
        elif resultant_x == 0 and resultant_y < 0:
            angle = -90
        else:
            angle = 0
            
        return Force(magnitude, angle%360)
        


class ForceCalculator(object):

    """
    """

    def __init__(self, forces=None):
        """
        """
        self.forces = {} if forces is None else forces

    def get_forces(self):
        """
        """
        return self.forces
        

    def add_force(self, name, magnitude, angle):
        """
        """
        if name in self.forces:
            raise RuntimeError(f"\nForce object {name} already exists!")
        else:
            self.forces[name] = Force(magnitude, angle)
        
    
    def remove_force(self, name):
        """
        """
        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        del self.forces[name]

    def __getitem__(self, name):
        """
        """
        try:
            return self.forces[name]
        except KeyError:
            raise RuntimeError(f"\nForce object {name} does not exist!")

    def compute_net_force(self):
        """
        """
        if len(self.forces) == 0:
            return Force()
        total_net_force = Force()
        for forces in self.forces.values():
            total_net_force += forces
        return total_net_force


    def __str__(self):
        """
        """
        force_str = ""
        for index, name in enumerate(self.forces):
            force_str += "\nForce #0{}: {}".format(index+1, name)
            force_str += "\n{}".format(self.forces[name])
        return force_str


