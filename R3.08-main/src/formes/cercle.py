from point import Point
from math import pi
class Cercle:
    """
    Classe Cercle qui prend en arguments un rayon r et un point qui correspond au centre du cercle
    """

    def __init__(self, r: float = 1, centre: Point = Point()):
        if isinstance(r, float) or isinstance(r, int):
            self.__r = r
            self.__centre = centre
        else:
            raise TypeError("les valeurs doivent etre de type réel")

    def diam(self) -> float:
        """
        Méthode qui renvoie le diametre d'un cercle
        :return: diametre du cercle
        """
        try:
            diametre = self.__r * 2
            return diametre
        except TypeError:
            print("Le rayon du cercle n'est pas un réel ou un entier")

    def peri(self) -> float:
        """
        Méthode qui renvoie le perimetre d'un cercle
        :return: perimetre du cercle
        """
        try:
            perimetre = 2 * pi * self.__r
            return perimetre
        except TypeError:
            print("Le rayon du cercle n'est pas un réel ou un entier")

    def surf(self) -> float:
        """
        Méthode qui renvoie la surface d'un cercle
        :return: surface du cercle
        """
        try:
            surface = self.__r ** 2 * pi
            return surface
        except TypeError:
            print("Le rayon du cercle ou une des coordonées n'est pas un réel ou un entier")

    def inter(self, c2 : 'Cercle') -> str:
        """
        Méthode qui indique comment est positionné un cercle par rapport à un autre
        :param c2: Deuxieme cercle
        :return: str de réponse
        """
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
        """
        Méthode qui indique si un point est à l'interieur d'un cercle
        :param point: point à étudier
        :return: str de réponse
        """
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


def main():
    """
    Méthode de Tests
    """
    c1 = Cercle(8)
    c2= Cercle (8)
    p1 = Point(8, 0)
    c3 = Cercle(3, p1)
    c3.r = 6
    print(c3.r)
    print(c1.peri())
    print(c1.surf())
    print(c1.diam())
    print(c1.inter(c2))
    print(c3.inter(c1))
    print(c1.dedans(p1))


if __name__ == "__main__":
    main()