from math import sqrt 
from math import pi 
from math import sin 
from math import tan
from math import radians
import matplotlib.pyplot as plt

class Oktagon:

    def __init__(self, side_oktagon):
        self.side_oktagon = side_oktagon
        self.corner_oktagone = radians(135)
        self.k = 1 + sqrt(2)

    def radius_square_circumscribed(self):
        return int(self.side_oktagon) / (2 * sin(pi/8)), pi * ((int(self.side_oktagon) / (2 * sin(pi/8)))**2)
    
    def  radius_square_inscribed(self):
        return (int(self.side_oktagon)) / (2 * tan(pi/8)), pi * ((int(self.side_oktagon)) / (2 * tan(pi/8)))**2
    
    def perimeter(self):
        return 8 * self.side_oktagon

    def square_oktagon(self):
        return 2 * self.k * (self.side_oktagon**2)
    
    def __del__(self):
        print("Объект удалён")

    



oktagon1 = Oktagon(12)
print(oktagon1.radius_square_circumscribed()," hgdjsdfk ", oktagon1.radius_square_inscribed(), " hjvsdk ", oktagon1.square_oktagon())


import numpy as np

# Параметры окружности
radius = 5
theta = np.linspace(0, 2 * np.pi, 100)  # Углы от 0 до 2π
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Построение
plt.figure(figsize=(6,6))
plt.plot(x, y, label=f'Окружность радиуса {radius}')
plt.gca().set_aspect('equal')  # Чтобы круг не был эллипсом
plt.grid(True)
plt.title('Окружность')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()