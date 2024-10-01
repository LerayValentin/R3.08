def plus_grand(a: float, b: float) -> float:
    """
        fonction qui retourne le plus grand de 2 nombres réels.
    """
    if a < b:
        return b
    else:
        return a


print(plus_grand(12.5, 5))


def seuil(valeur: float, seuil=10):
    """
        fonction qui indique si la valeur passée est supérieure à un seuil.
        Ce seuil est fixé à 10, mais peux être modifié dans un
        second argument
    """
    if valeur > seuil:
        return "Valeur supérieure au seuil"
    else:
        return "Valeur inférieure au seuil"


print(seuil(12, 30))


def liste(*nombres : float):
    """
        la fonction qui retourne la plus grande valeur d’une
        liste de valeur fournie
    """
    x = 0
    for i in range(len(nombres)):
        if nombres[i] > x:
            x = nombres[i]
    return x


print(liste(12, 52, 23, 45))


def liste_inferieur(*nombres : float, seuil : int =3) -> int:
    """
        la fonction qui retourne le nombre de valeurs d’une liste
        inférieure à un seuil qui est défini par défaut à 3 mais qui peux
        être modifié lors de l’appel de la fonction
    """
    compteur=0
    for i in range(len(nombres)):
        if nombres[i] < seuil:
            compteur+=1
    return compteur


print(liste_inferieur(1, 2, 3, 4, 5, 1.2, 3.2, 2.7, 0, seuil=2))


def dico(chaine : str, **dico) -> str :
    """
        Une fonction qui affiche l’ensemble des données d’un dictionnaire
        passé en argument. Cette fontion prendra aussi comme argument une
        chaine de caractère qui précédera chaque affichage
    """
    return f"{chaine} {dico}"


print(dico("Chaine de caractères :", test=1, Test=2))
