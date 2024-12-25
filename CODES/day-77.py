'''#operator overloadind#'''

from typing import Any


class vector:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'{self.x}i, {self.y}j,{self.z}k'

    def __add__(self,c):
        return f"{self.x+c.x}i, {self.y+c.y}j, {self.z+c.z}k"

v1=vector(2,3,4);
print(v1);
v2=vector(3,5,7);
print(v2);
print(v1+v1);
# print(v.__str__());