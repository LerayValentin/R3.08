def affiche(texte: str):
    print(f"texte à afficher : {texte} ")

class Velo:

    def __init__(self, marque: str, taille_pneu: float, couleur: str,
                 nombre_vitesse: int):
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nombre_vitesse = nombre_vitesse
        self.vitesse_courante = 1

    def gear_up(self):
        if self.vitesse_courante == self.nombre_vitesse:
            print("La vitesse est déja maximale")
        else:
            self.vitesse_courante += 1
            print(f"La vitesse courante est de {self.vitesse_courante}")

    def gear_down(self):
        if self.vitesse_courante == 1:
            print("La vitesse est déja minimale")
        else:
            self.vitesse_courante -= 1
            print(f"La vitesse courante est de {self.vitesse_courante}")

def fonction_principale():
    chaine = "str1"
    affiche(chaine)
    v1 = Velo("Nakamura", 19, "noir", 4)
    v1.gear_up()
    v1.gear_up()
    v1.gear_up()
    v1.gear_up()
    v1.gear_down()
    v1.gear_down()
    v1.gear_down()
    v1.gear_down()

if __name__ == "__main__" :
    fonction_principale()