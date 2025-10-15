from math import sqrt 
from math import pi 
from math import sin 
from math import tan
from math import radians
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Oktagon:

    def __init__(self, side_oktagon):
        self.side_oktagon = side_oktagon
        self.corner_oktagone = radians(135)
        self.K = 1 + sqrt(2)

    def radius_square_circumscribed(self):
        return int(self.side_oktagon) / (2 * sin(pi/8)), pi * ((int(self.side_oktagon) / (2 * sin(pi/8)))**2)
    
    def  radius_square_inscribed(self):
        return (int(self.side_oktagon)) / (2 * tan(pi/8)), pi * ((int(self.side_oktagon)) / (2 * tan(pi/8)))**2
    
    def perimeter(self):
        return 8 * self.side_oktagon

    def square_oktagon(self):
        return 2 * self.K * (self.side_oktagon**2)
    
    def risuem_huetu(self):
        center = (0.0, 0.0)
        radius1,s2 = oktagon1.radius_square_circumscribed() 
        radius2,s2 = oktagon1.radius_square_inscribed() 

        fig, ax = plt.subplots()

        circle = patches.Circle(center, radius1, edgecolor='blue', facecolor='white')
        circle2 = patches.Circle(center, radius2, edgecolor='green', facecolor='white')

        ax.add_patch(circle)
        ax.add_patch(circle2)

        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_aspect('equal', adjustable='box')

        num_sides = 8
        angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
        x = radius1 * np.cos(angles)
        y = radius1 * np.sin(angles)

        x = np.append(x, x[0])
        y = np.append(y, y[0])

        ax.plot(x, y, 'red')

        plt.title("Октагон с вписанной и описанной окружностями")
        plt.grid(True)
        plt.show()
    
    def __del__(self):
        print("Объект удалён")



oktagon1 = Oktagon(12)
print(oktagon1.radius_square_circumscribed()," hgdjsdfk ", oktagon1.radius_square_inscribed(), " hjvsdk ", oktagon1.square_oktagon())
oktagon1.risuem_huetu()

