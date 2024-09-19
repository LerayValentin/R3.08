class Tasse:
    matière: str = 'céramique'

    def __init__(self, couleur: str, contenance: float, marque: str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        return (f'la tasse de matière {self.matière}, '
                f'de couleur {self.couleur} et de marque {self.marque}'
                f' a une contenance de {self.contenance} ml')

    def add_contenu(self, contenu: str):
        self.contenu = contenu

    def del_contenu(self):
        del self.contenu


petitetasse = Tasse('rouge', 30, 'marquedelatasse')
print(petitetasse)
petitetasse.add_contenu("lait")
print(petitetasse.contenu)
petitetasse.del_contenu()
print(petitetasse.contenu)