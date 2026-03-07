import time
from collections import deque
from naze import extraire_resultats, afficher_etape, rafraichir_labyrinthe
from naze import GOAL, START


def resoudre_bfs(grille, anime=False):
    """
    Algorithme Breadth-First Search (Recherche en largeur).
    Utilise une file (FIFO) pour garantir le chemin le plus court.

    le paramètre 'anime' permet de déterminer s'il faut afficher chaque étape de l'exploration
    """
    debut_t = time.perf_counter()
    file = deque([START])
    parents = {START: None}
    explores = []

    print("\n" * 16)

    while file:
        curr = file.popleft() # Premier entré, premier sorti
        if curr not in explores: 
            explores.append(curr)
            
        if curr == GOAL: break
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nxt = (curr[0]+dx, curr[1]+dy)
            if grille[nxt[0]][nxt[1]] != '#' and nxt not in parents:
                parents[nxt] = curr
                file.append(nxt)

        if anime:              
            #afficher_etape(grille, explores, "BFS : Exploration en cours ---- ---- ")
            # print("\n" * 16)
            rafraichir_labyrinthe(grille, explores, "Exploration BFS en cours...", premiere_fois=False)
                
    fin_t = time.perf_counter()
    return extraire_resultats(parents, explores, fin_t - debut_t)
