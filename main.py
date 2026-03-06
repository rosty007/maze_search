from naze import generer_labyrinthe, afficher_visu, formater_chemin_str
from dfs import resoudre_dfs
from bfs import resoudre_bfs
from astar import resoudre_astar

def afficher_comparaison_statistiques(resultats):
    """
    Affiche un tableau comparatif des statistiques des algorithmes.
    'resultats' doit être une liste de tuples : (Nom, Noeuds, Longueur, Temps)
    """
    header = f"{'Algorithme':<20} {'Noeuds':<10} {'Longueur':<10} {'Temps (ms)':<10}"
    print("\n" + "="*55)
    print("RECAPITULATIF DES PERFORMANCES")
    print("="*55)
    print(header)
    print("-" * 55)
    
    for nom, n_explores, longueur, temps in resultats:
        # Conversion du temps en millisecondes pour correspondre à votre image
        temps_ms = temps * 1000
        print(f"{nom:<20} {n_explores:<10} {longueur:<10} {temps_ms:<10.3f}")
    print("="*55)

# --- MISE À JOUR DE LA BOUCLE PRINCIPALE ---



def main():
    print("Début exécution du programme principal de DevoirI")
    # --- PROGRAMME PRINCIPAL ---

    laby = generer_labyrinthe(seed=123)
    algos = [
        ("DFS (Recherche en Profondeur - Pile)", resoudre_dfs), 
        ("BFS (Recherche en Largeur - File)", resoudre_bfs), 
        ("A* (Recherche Informée - Priorité)", resoudre_astar)
    ]

    stats_collectees = []
    for nom, fonction in algos:
        print(f"\n{'-'*30}\n{nom}\n{'-'*30}")
        exp, sol, t = fonction(laby)
        
        # On stocke les résultats pour le tableau final
        stats_collectees.append((nom.split(" (")[0], len(exp), len(sol), t))
        print("\nVISUALISATION DE L'EXPLORATION (p):")
        afficher_visu(laby, exp, 'p')
        
        print("\nVISUALISATION DE LA SOLUTION (*):")
        afficher_visu(laby, sol, '*')
        
        print(f"\nChemin: {formater_chemin_str(sol)}")
        
        print(f"\nSTATISTIQUES:")
        print(f" - Nœuds explorés : {len(exp)}")
        print(f" - Longueur du chemin : {len(sol)}")
        print(f" - Temps d'exécution : {t:.6f} secondes")

    # Affichage final du tableau comparatif
    afficher_comparaison_statistiques(stats_collectees)
    
if __name__ == "__main__":
    main()
