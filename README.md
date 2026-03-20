# 🧬 Jeu de la Vie — Conway's Game of Life

Bienvenue sur mon premier projet personnel ! 🎉

Ce projet est une implémentation du célèbre **Jeu de la Vie** de John Horton Conway, développée entièrement en Python.

---

## 📖 Description

Le **Jeu de la Vie** est un automate cellulaire imaginé par le mathématicien John Conway en 1970. Il se déroule sur une grille bidimensionnelle composée de cellules pouvant être **vivantes** (1) ou **mortes** (0). À chaque génération, l'état de chaque cellule évolue selon quatre règles simples :

1. Une cellule vivante avec **moins de 2 voisins vivants** meurt (sous-population).
2. Une cellule vivante avec **2 ou 3 voisins vivants** survit.
3. Une cellule vivante avec **plus de 3 voisins vivants** meurt (surpopulation).
4. Une cellule morte avec **exactement 3 voisins vivants** devient vivante (reproduction).

---

## 🛠️ Outils utilisés

| Outil | Rôle |
|---|---|
| **Python 3** | Langage de programmation principal |
| **matplotlib** | Bibliothèque utilisée pour l'affichage de la grille et l'animation |
| **matplotlib.animation.FuncAnimation** | Permet d'animer la grille génération par génération |
| **random** | Module Python standard pour générer la grille initiale aléatoirement |

---

## 🚀 Lancer le projet

### Prérequis

- Python 3 installé
- La bibliothèque `matplotlib` installée :

```bash
pip install matplotlib
```

### Exécution

```bash
python main.py
```

Une fenêtre s'ouvre et affiche l'évolution du Jeu de la Vie sur une grille de 10×10 cellules, avec une animation de 100 générations.

---

## 📁 Structure du projet

```
jeu_de_la_vie/
├── main.py       # Code source principal
└── README.md     # Ce fichier
```

---

## 💡 Ce que j'ai appris

Ce premier projet personnel m'a permis de :

- Pratiquer la logique algorithmique (parcours de grille, comptage de voisins)
- Découvrir la bibliothèque `matplotlib` pour la visualisation de données
- Utiliser `FuncAnimation` pour créer des animations interactives
- Structurer un programme Python avec plusieurs fonctions

---

## 👤 Auteur

Projet réalisé par **Daloche** — premier projet personnel Python. 🐍
