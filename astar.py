import time
import heapq
from naze import extraire_resultats, afficher_etape, rafraichir_labyrinthe
from naze import GOAL, START


def resoudre_astar(grille, anime=False):
    """
    Algorithme A* (A-Star).
    Utilise une file de priorité et une heuristique (Manhattan).
    f(n) = g(n) + h(n)

    le paramètre 'anime' permet de déterminer s'il faut afficher chaque étape de l'exploration
    """
    debut_t = time.perf_counter()
    
    # Distance de Manhattan : distance absolue entre n et la cible
    def h(n): 
        return abs(n[0]-GOAL[0]) + abs(n[1]-GOAL[1])
    
    # Stockage : (f_score, coordonnees)
    pq = [(h(START), START)]
    g_score = {START: 0} # Coût réel depuis le départ
    parents = {START: None}
    explores = []

    # Les 16 lignes laissées vides ci-dessous vont permettre d'afficher étape par étape le 
    # processus d'exploration
    print("\n" * 16)

    while pq:
        _, curr = heapq.heappop(pq) # On récupère le nœud ayant le plus petit f_score
        if curr not in explores: 
            explores.append(curr)
            
        if curr == GOAL: break
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nxt = (curr[0]+dx, curr[1]+dy)
            if grille[nxt[0]][nxt[1]] != '#':
                # Chaque déplacement coûte 1
                tentative_g = g_score[curr] + 1
                
                # Si ce nouveau chemin vers le voisin est meilleur
                if nxt not in g_score or tentative_g < g_score[nxt]:
                    g_score[nxt] = tentative_g
                    f = tentative_g + h(nxt)
                    parents[nxt] = curr
                    heapq.heappush(pq, (f, nxt))

        if anime:              
            # afficher chaque étape de l'exploration si le paramètre 'anime' est vrai            
            rafraichir_labyrinthe(grille, explores, "Exploration A* en cours...", premiere_fois=False)

    fin_t = time.perf_counter()
    return extraire_resultats(parents, explores, fin_t - debut_t)