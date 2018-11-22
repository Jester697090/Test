import math

class Prostokat:

    type = "czworokąt"  # prawdziwe dla wszystkich prostokątów

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.P = self.a * self.b
        self.p = math.sqrt(self.a ** 2 + self.b ** 2)

    def pole(self):
        return 1.0 * self.P

    def przekatna(self):
        return self.p

r1 = Prostokat(3, 4)
print("Pole prostokata = ", r1.pole())
print("Przekątna prostokąta = ", r1.przekatna())