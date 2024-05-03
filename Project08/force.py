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
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    """
    def __init__(self, magnitude=0, angle=0):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        self.magnitude = magnitude
        self.angle = angle
        

    def get_magnitude(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        return self.magnitude

    def get_angle(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        return self.angle

    def get_components(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        x = self.magnitude * math.cos(math.radians(self.angle))
        y = self.magnitude * math.sin(math.radians(self.angle))
        return x, y



    def __str__(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        return "Magnitude: {:.2f}\nAngle: {:.2f}".format(
            self.magnitude, self.angle
        )

        
    def __eq__(self, other):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO  
        """
        if not isinstance(other, Force):
            raise RuntimeError("Operand is not a Force instance")
        return (
            self.magnitude == other.magnitude 
            and self.angle == other.angle
        )
            
    
    
    def __add__(self, other):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
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
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    I LOVE POKEMON GO
    """

    def __init__(self, forces=None):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        self.forces = {} if forces is None else forces

    def get_forces(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        return self.forces
        

    def add_force(self, name, magnitude, angle):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        if name in self.forces:
            raise RuntimeError(f"\nForce object {name} already exists!")
        else:
            self.forces[name] = Force(magnitude, angle)
        
    
    def remove_force(self, name):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        del self.forces[name]

    def __getitem__(self, name):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        try:
            return self.forces[name]
        except KeyError:
            raise RuntimeError(f"\nForce object {name} does not exist!")

    def compute_net_force(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        if len(self.forces) == 0:
            return Force()
        total_net_force = Force()
        for forces in self.forces.values():
            total_net_force += forces
        return total_net_force


    def __str__(self):
        """
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        I LOVE POKEMON GO
        """
        force_str = ""
        for index, name in enumerate(self.forces):
            force_str += "\nForce #0{}: {}".format(index+1, name)
            force_str += "\n{}".format(self.forces[name])
        return force_str


