"""
@property
def x():
    return self.__x
@x.setter
dex x(val):
    if isInstance(x, float):
        self.__x = x
    else:
        raise ValueError("n'est pas un réel")
"""
from math import sqrt

class Point:
    """
        Classe Point qui prend en arguments deux coordonées x et y.
        Methodes pour calculer la distance entre deux points; soit avec des coordonnées fournies, soit directemment
        un autre objet de la classe Point.
    """
    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y

    def distancecoord(self, x2: float, y2: float) -> float:
        try:
            distance = sqrt((x2 - self.__x)**2 + (y2 - self.__y)**2)
            return distance
        except TypeError:
            print("Pas le bon type de coordonnées pour un des points")

    def distancePoint(self, camarade: 'Point') -> float:
        try:
            distance = sqrt((camarade.__x - self.__x)**2 + (camarade.__y - self.__y)**2)
            return distance
        except TypeError:
            print("Pas le bon type de coordonnées pour un des points")

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if isinstance(x, float) or isinstance(x, int):
            self.__x = x
        else:
            raise ValueError("n'est pas un réel ou un entier")
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if isinstance(y, float) or isinstance(y, int):
            self.__y = y
        else:
            raise ValueError("n'est pas un réel ou un entier")




def main():
    punto1 = Point(5, 6.2)
    punto2 = Point(12.3, 7)
    print(punto1.distancecoord(9, 3))
    print(punto2.distancePoint(punto1))
    print(punto2.x)
    punto2.x = 5
    print(punto2.x)
    print(punto2.y)
    punto2.y = 15
    print(punto2.y)


if __name__ == "__main__":
    main()
