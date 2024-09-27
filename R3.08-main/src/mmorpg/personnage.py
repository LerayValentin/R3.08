
class Personnage :
    """
    Classe personnage
    """
    def __init__(self, pseudo: str, niveau: int = 1):
        """
        Methode d'initialisation des attributs
        :param pseudo: Nom du personage
        :param niveau: niveau du personnage
        """
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__nbr_pv = niveau
        self.__initiative = niveau

    def __str__(self) -> str:
        """
        Methode d'affichage d'un objet Personnage
        :return: Affichage du personnage
        """
        return (f"Le personnage {self.__pseudo} est de niveau {self.__niveau}, a {self.__nbr_pv}"
                f" PVs et une initiative de {self.__initiative}")

    @property
    def pseudo(self) -> str:
        """
        methode d'affichage de l'attribut pseudo
        :return: pseudo
        """
        return self.__pseudo
    @property
    def niveau(self) -> int:
        """
        methode d'affichage de l'attribut niveau
        :return: niveau
        """
        return self.__niveau
    @niveau.setter
    def niveau(self, niveau):
        """
        methode de modification de l'attribut niveau
        :param niveau: nouvelle valeur du niveau
        :return: Message d'erreur en cas d'erreur
        """
        if isinstance(niveau, int):
            self.__niveau = niveau
            self.__nbr_pv = niveau
            self.__initiative = niveau
        else:
            raise ValueError("n'est pas un entier")
    @property
    def nbr_pv(self):
        """
        methode d'affichage de l'attribut nbr_pv
        :return: nbr_pv
        """
        return self.__nbr_pv
    @nbr_pv.setter
    def nbr_pv(self, nbr_pv):
        """
        methode de modification de l'attribut nbr_pv
        :param nbr_pv: nouvelle valeur du nbr_pv
        :return: Message d'erreur en cas d'erreur
        """
        if isinstance(nbr_pv, int):
            self.__nbr_pv = nbr_pv
        else:
            raise ValueError("n'est pas un entier")
    @property
    def initiative(self):
        """
        methode d'affichage de l'attribut initiative
        :return: initiative
        """
        return self.__initiative
    @initiative.setter
    def initiative(self, initiative):
        """
        methode de modification de l'attribut initiative
        :param initiative: nouvelle valeur du initiative
        :return: Message d'erreur en cas d'erreur
        """
        if isinstance(initiative, int):
            self.__initiative = initiative
        else:
            raise ValueError("n'est pas un entier")
    def attaque(self, adversaire: 'Personnage'):
        """
        Methode d'echange de coups entre deux personnages
        :param adversaire: Personnage à affronter
        """
        if self.initiative > adversaire.initiative:
            adversaire.nbr_pv -= self.degats()
            if adversaire.nbr_pv > 0:
                self.nbr_pv -= adversaire.degats()
        if self.initiative < adversaire.initiative:
            self.nbr_pv -= adversaire.degats()
            if self.nbr_pv > 0:
                adversaire.nbr_pv -= self.degats()
        else:
            self.nbr_pv -= adversaire.degats()
            adversaire.nbr_pv -= self.degats()

    def combat(self, adversaire: 'Personnage'):
        """
        Methode de combat entre deux personnage jusqu'à la mort de l'un d'eux
        :param adversaire: Personnage à affronter
        :return: Nom du personnage mort
        """
        while adversaire.nbr_pv > 0 and self.nbr_pv > 0:
            self.attaque(adversaire)
        if self.nbr_pv <= 0 and adversaire.nbr_pv <= 0:
            return f"{self.pseudo} et {adversaire.pseudo} sont mort"
        elif self.nbr_pv <= 0:
            return f"{self.pseudo} est mort"
        elif adversaire.nbr_pv <= 0:
            return f"{adversaire.pseudo} est mort"

    def soigner(self) -> None:
        """
        Methode pour soigner un personnage à hauteur de son niveau
        """
        self.nbr_pv = self.niveau

    def degats(self):
        """
        Methode renvoyant les dégats du peronnage
        :return: degats
        """
        degats = self.niveau
        return degats

def main():
    marius = Personnage("marius", 10)
    valentin = Personnage("valentin", 9)
    print(marius.combat(valentin))
    print(marius)
    marius.soigner()
    print(marius)
if __name__ == "__main__":
    main()