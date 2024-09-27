from personnage import Personnage

class Mage(Personnage):
    """
    Classe Mage
    """

    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.nbr_pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.__mana = niveau * 5

    def degats(self):
        """
        Methode renvoyant les dégats du peronnage
        :return: degats
        """
        if self.__mana > 0:
            self.__mana -= 4
            degats = self.niveau + 3
            return degats
        else:
            degats = self.niveau
            return degats

