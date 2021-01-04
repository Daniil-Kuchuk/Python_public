import math
import unittest

class InvalidSidesOfTriangle(Exception): pass
class SidesLessOrEqualToZero(Exception): pass
class AnglesNotEqualTo180(Exception): pass
class AnglesLessOrEqualToZero(Exception): pass

class TriangelOnThePlane:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__A = math.acos( (pow(self.__b, 2) + pow(self.__c, 2) - pow(self.__a, 2)) / (2 * self.__b * self.__c) ) * 180 / math.pi
        self.__B = math.acos( (pow(self.__a, 2) + pow(self.__c, 2) - pow(self.__b, 2)) / (2 * self.__a * self.__c) ) * 180 / math.pi
        self.__C = math.acos( (pow(self.__a, 2) + pow(self.__b, 2) - pow(self.__c, 2)) / (2 * self.__a * self.__b) ) * 180 / math.pi
        try:
            self.__true_triangle()
        except InvalidSidesOfTriangle:
            print('стороны треугольника не соответсвуют правилу!')
            exit()
        except SidesLessOrEqualToZero:
            print('стороны не могут быть < 0!')
            exit()
        except AnglesNotEqualTo180:
            print('углы треугольника не равны 180!')
            exit()
        except AnglesLessOrEqualToZero:
            print('углы не могут быть <= 0! ')
            exit()

    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c
    @property
    def A(self):
        return self.__A
    @property
    def B(self):
        return self.__B
    @property
    def C(self):
        return self.__C
    
    def __true_triangle(self):
        if self.__a + self.__b <= self.__c or self.__a + self.__c <= self.__b or self.__c + self.__b <= self.__a:
            raise InvalidSidesOfTriangle#стороны треугольника не соответсвуют правилу!
        if self.__a < 0 or self.__b < 0 or self.__c < 0:
            raise SidesLessOrEqualToZero#стороны не могут быть <= 0!
        if round(self.__A, 2) + round(self.__B, 2) + round(self.__C, 2) != 180:
            raise AnglesNotEqualTo180#углы треугольника не равны 180!
        if self.__A <= 0 or self.__B <= 0 or self.__C <= 0:
            raise AnglesLessOrEqualToZero#углы не могут быть <= 0!

    @property
    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    @property
    def perimetr(self):
        return self.__a + self.__b + self.__c
    
    def similar(self, other):
        k_a = self.__a / other.__a
        k_b = self.__b / other.__b
        k_c = self.__c / other.__c
        if k_a == k_b and k_b == k_c:
            return True
        return False

    def height_of_triangle(self, side):
        if side != self.__a and side != self.__b and side != self.__c:
            return 0
        return 2 * self.area / side

    def __eq__(self, other):
        if self.__a == other.__a and self.__b == other.__b and self.__c == other.__c:
            return True
        return False

    def __lt__(self, other):
        if self.__a < other.__a and self.__b < other.__b and self.__c < other.__c:
            return True
        return False
    
    def __le__(self, other):
        if self.__a <= other.__a and self.__b <= other.__b and self.__c <= other.__c:
            return True
        return False
    
    def __str__(self):
        return '''сторона a:, self.__a, 
сторона b:, self.__b, 
сторона c:, self.__c, 
угол А:, self.__A, 
угол B:, self.__B, 
угол C:, self.__C, 
периметр:, self.perimetr, 
площадь:, self.area, 
высота:, self.height_of_triangle(11)'''

class Test(unittest.TestCase): 
    def setUp(self):
        self.test_triangle = TriangelOnThePlane(11, 5, 8)

    def test_area(self):
        self.assertEqual(round(self.test_triangle.area), 18)

    def test_perimetr(self):
        self.assertEqual(self.test_triangle.perimetr, 24)

    def test_height(self):
        self.assertEqual(round(self.test_triangle.height_of_triangle(11)), 3)    

if __name__ == "__main__":
    unittest.main()