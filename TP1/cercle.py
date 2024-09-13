from point import Point
from math import pi
class Cercle:

    def __init__(self, r: float = 1, centre: Point = Point()):
        self.__r = r
        self.__centre = centre

    def diam(self) -> float:
        try:
            diametre = self.__r * 2
            return diametre
        except TypeError:
            print("Le rayon du cercle n'est pas un réel ou un entier")

    def peri(self) -> float:
        try:
            perimetre = 2 * pi * self.__r
            return perimetre
        except TypeError:
            print("Le rayon du cercle n'est pas un réel ou un entier")

    def surf(self) -> float:
        try:
            surface = self.__r ** 2 * pi
            return surface
        except TypeError:
            print("Le rayon du cercle ou une des coordonées n'est pas un réel ou un entier")

    def inter(self, c2 : 'Cercle') -> str:
        try:
            distancecentres = self.__centre.distancePoint(c2.__centre)
            if distancecentres <= self.__r - c2.__r:
                return "le cercle passé en argument est à l’intérieur du cercle."
            elif distancecentres <= c2.__r - self.__r:
                return "le cercle est à l’intérieur du cercle passé en argument"
            elif distancecentres < self.__r + c2.__r:
                return "les cercles se coupent en deux points."
            elif distancecentres == self.__r + c2.__r:
                return "Les cercles sont en contact l'un avec l'autre."
            else:
                return "les cercles ne se chevauchent pas"
        except TypeError:
            print("Une des valeurs fournies n'est pas un entier ou un réel")

    def dedans(self, point: Point) -> str:
        try:
            d = self.__centre.distancePoint(point)
            if d < self.__r:
                return "Le point est dans le cercle"
            if d == self.__r:
                return "Le point est sur le cercle"
            if d > self.__r:
                return "Le point est en dehors le cercle"
        except TypeError:
            print("Une des valeurs fournies n'est pas un entier ou un réel")

c1 = Cercle(8)
c2= Cercle (8)
p1 = Point(8, 0)
c3 = Cercle(3, p1)
print(c1.peri())
print(c1.surf())
print(c1.diam())
print(c1.inter(c2))
print(c3.inter(c1))
print(c1.dedans(p1))
