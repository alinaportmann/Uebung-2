import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if type(other) == Vector3:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        if type(self) == int or type(self) == float:
            return Vector3(self * other.x, self * other.y, self * other.z)
        
    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)
    
    def dot(self,other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    
    def normalize(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)
    
# Beispiel
a = Vector3(3, 4, 2)
b = Vector3(2, 1, 0)

c = a * b 
print("Komponentenweise Multiplikation:", c)

d = a.dot(b)
print("Skalarprodukt:", d)

e = a.cross(b)
print("Kreuzprodukt:", e)

f = a.normalize()
print("Normalisierter Vektor a:", f)
