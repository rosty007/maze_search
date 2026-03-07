import time
from naze import extraire_resultats, afficher_etape, rafraichir_labyrinthe
from naze import GOAL, START

# --- FONCTIONS DE RÉSOLUTION ---

def resoudre_dfs(grille, anime=False):
    """
    Algorithme Depth-First Search (Recherche en profondeur).
    Utilise une pile (LIFO) pour explorer chaque branche jusqu'au bout.
    Priorité : Droite, Bas, Gauche, Haut.
    """
    debut_t = time.perf_counter()
    pile = [START]
    parents = {START: None} # Pour reconstruire le chemin
    explores = []           # Historique de l'exploration pour affichage 'p'
    # Ordre cible : Droite (0,1), Bas (1,0), Gauche (0,-1), Haut (-1,0)
    priorites = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    print("\n" * 16)
    while pile:
        curr = pile.pop()
        if curr not in explores: 
            explores.append(curr)
            
        
        if curr == GOAL: break
        
        # On inverse les priorités car une pile sort le dernier élément ajouté en premier
        for dx, dy in reversed(priorites):
            nxt = (curr[0]+dx, curr[1]+dy)
            # Si le voisin est un passage et n'a pas été planifié ou visité
            if grille[nxt[0]][nxt[1]] != '#' and nxt not in parents:
                parents[nxt] = curr
                pile.append(nxt)
                
        if anime:              
            #afficher_etape(grille, explores, "DFS : Exploration en cours ---- ---- ")            
            rafraichir_labyrinthe(grille, explores, "Exploration DFS en cours...", premiere_fois=False)
    fin_t = time.perf_counter()
    return extraire_resultats(parents, explores, fin_t - debut_t)
