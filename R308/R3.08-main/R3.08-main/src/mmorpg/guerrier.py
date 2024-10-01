from personnage import Personnage

class Guerrier(Personnage):
    """
    Classe Guerrier
    """
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.nbr_pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6

    def degats(self):
        """
        Methode renvoyant les dégats du peronnage
        :return: degats
        """
        degats = self.niveau * 2
        return degats
