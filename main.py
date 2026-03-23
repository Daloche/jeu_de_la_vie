import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


def generer_grille(colones, lignes):
    matrice = []
    for i in range(lignes):
        ligne = []
        for j in range(colones):
            ligne.append(random.randint(0, 1))
        matrice.append(ligne)
    return matrice


def compter_voisins(grille, ligne, colonne):
    nb_vivant = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((ligne + i < len(grille) and colonne + j < len(grille[0])) and (ligne + i >= 0 and colonne + j >= 0)) and (grille[ligne+i][colonne + j] == 1) and not (i == 0 and j == 0):
                nb_vivant += 1
    return nb_vivant


def generation_suivante(grille):
    new_grille = []
    for i in range(len(grille)):
        ligne = []
        for j in range(len(grille[i])):
            ligne.append(0)
        new_grille.append(ligne)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = compter_voisins(grille, i, j)
            if cellule == 3:
                new_grille[i][j] = 1
            if cellule == 2 and grille[i][j] == 1:
                new_grille[i][j] = 1
    return new_grille


def main():
    grille = generer_grille(100, 100 )
    fig, ax = plt.subplots()
    img = ax.imshow(grille, cmap='binary')

    def mettre_a_jour(frame):
        nonlocal grille
        grille = generation_suivante(grille)
        img.set_data(grille)
        return img

    ani = FuncAnimation(fig, mettre_a_jour, frames=100, interval=100)
    plt.show()


if __name__ == "__main__":
    main()
