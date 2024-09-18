from point import Point

class Rectangle:
    """
    Classe rectangle
    """
    def __init__(self, point_bas_gauche: Point = Point(),
                 long: float = 1, haut: float = 1, point_haut_droit: Point = None):
        if point_haut_droit is None:
            self.__point_bas_gauche = point_bas_gauche
            self.__long = long
            self.__haut = haut
        else:
            if ((isinstance(point_haut_droit.x, float) or isinstance(point_haut_droit.x, int)) and (isinstance(point_haut_droit.y, float) or isinstance(point_haut_droit.y, int)) and
                    (isinstance(point_bas_gauche.x, float) or isinstance(point_bas_gauche.x, int)) and (isinstance(point_bas_gauche.y, float) or isinstance(point_bas_gauche.y, int))):
                self.__point_bas_gauche = point_bas_gauche
                self.__long = point_haut_droit.x - point_bas_gauche.x
                self.__haut = point_haut_droit.y - point_bas_gauche.y
            else:
                raise ValueError("n'est pas un réel ou un entier")



    def __str__(self):
        return f"- Point Bas Gauche : x={self.__point_bas_gauche.x}, y={self.__point_bas_gauche.y}\n- Longueur : {self.__long}\n- Hauteur : {self.__haut}\n"

    def surface(self) -> float:
        return self.__long * self.__haut

    def perimetre(self) -> float:
        try:
            return (self.__long + self.__haut) * 2
        except TypeError:
            print("Une des valeurs fournies n'est pas un entier ou un réel")

    def point_bas_gauche(self):
        return self.__point_bas_gauche

    def point_bas_droit(self):
        try:
            return Point((self.__point_bas_gauche.x + self.__long), self.__point_bas_gauche.y)
        except TypeError:
            print("Une des valeurs fournies n'est pas un entier ou un réel")

    def point_haut_gauche(self):
        try:
            return Point(self.__point_bas_gauche.x, (self.__point_bas_gauche.y + self.__haut))
        except TypeError:
            print("Une des valeurs fournies n'est pas un entier ou un réel")

    def point_haut_droit(self):
        try:
            return Point((self.__point_bas_gauche.x + self.__long), (self.__point_bas_gauche.y + self.__haut))
        except TypeError:
            print("Une des valeurs fournies n'est pas un entier ou un réel")

    def dans_rectangle(self):



def main():
    rectangle1 = Rectangle(point_bas_gauche=Point(5, 5), point_haut_droit=Point(8, 8))
    print(rectangle1)
    rectangle2 = Rectangle(Point(1, 1), 5, 10)
    print(rectangle2)
    print(rectangle2.surface(),"unités d'aire")
    print(rectangle2.perimetre(),"unités")
    print(rectangle2.point_bas_gauche())
    print(rectangle2.point_bas_droit())
    print(rectangle2.point_haut_gauche())
    print(rectangle2.point_haut_droit())

if __name__ == "__main__":
    main()