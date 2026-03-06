import random
from collections import deque


# --- CONFIGURATION GLOBALE ---
TAILLE = 16
START = (1, 1)
GOAL = (TAILLE - 2, TAILLE - 2)

def generer_labyrinthe(seed=42):
    """
    Génère une matrice 2D de 16x16 avec des murs extérieurs et des obstacles aléatoires.
    Garantit qu'un chemin existe entre S et G.
    """
    random.seed(seed)
    while True:
        # Initialisation de la grille avec des passages (.)
        grille = [['.' for _ in range(TAILLE)] for _ in range(TAILLE)]
        
        for i in range(TAILLE):
            for j in range(TAILLE):
                # Placement des murs extérieurs (bordures)
                if i == 0 or i == TAILLE-1 or j == 0 or j == TAILLE-1:
                    grille[i][j] = '#'
                # Placement aléatoire des murs intérieurs (densité ~60%)
                elif (i, j) != START and (i, j) != GOAL and random.random() < 0.4:
                    grille[i][j] = '#'
        
        # Placement des points de départ et d'arrivée
        grille[START[0]][START[1]] = 'S'
        grille[GOAL[0]][GOAL[1]] = 'G'
        
        # On ne valide le labyrinthe que s'il est techniquement possible de le finir
        if verifier_chemin_basique(grille): 
            return grille

def verifier_chemin_basique(grille):
    """ Utilise un BFS simple pour confirmer l'existence d'un chemin. """
    file = deque([START])
    visite = {START}
    while file:
        x, y = file.popleft()
        if (x, y) == GOAL: return True
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+dx, y+dy
            if grille[nx][ny] != '#' and (nx, ny) not in visite:
                visite.add((nx, ny))
                file.append((nx, ny))
    return False


# --- OUTILS DE FORMATAGE ---

def extraire_resultats(parents, explores, duree):
    """ Reconstruit le chemin inverse depuis Goal jusqu'à Start. """
    chemin = []
    curr = GOAL
    # On remonte la chaîne des dictionnaires 'parents'
    while curr:
        chemin.append(curr)
        curr = parents.get(curr)
    chemin.reverse()
    return explores, chemin, duree

def afficher_visu(grille, points, symbole):
    """ Affiche la grille en remplaçant temporairement les cases par le symbole donné. """
    copie = [ligne[:] for ligne in grille]
    for (x, y) in points:
        if copie[x][y] not in ('S', 'G'):
            copie[x][y] = symbole
    for ligne in copie:
        print(" ".join(ligne))

def formater_chemin_str(chemin):
    """ Transforme la liste de tuples en une chaîne lisible : S(1,1) -> (1,2) ... -> G(14,14). """
    etapes = [f"({x},{y})" for (x,y) in chemin]
    etapes[0] = f"S{etapes[0]}"
    etapes[-1] = f"G{etapes[-1]}"
    return " -> ".join(etapes)
