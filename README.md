# Projet de recherche de chemin dans un labyrinthe
Le projet consiste à générer de façon aléatoire des labyrinthes de 16 lignes et 16 colonnes, puis d'implémenter trois algorithmes de recherche pour trouver le chemin partant du noeud de départ (S) au noeud d'arrivée (G). La génération du labyrinthe doit garantir qu'un chemin existe pour partir de la source à la cible. Les trois algorithmes implémentés sont:
* Depth-First Search (DFS)
* BFS (Breadth-First Search)
* A* (A-star)

# Principales fonctions implémentées
* La génération aléatoire du labyrinthe avec le module **naze** (**naze.py**). Ce module inclut également les fonctions d'affichage du labyrinthe, des noeuds explorés et chemin solution résultant de l'exécution de chaque algorithme.
* l'implémentation de l'algorithme DFS via le module **dfs** (**dfs.py**).
* l'implémentation de l'algorithme BFS via le module **bfs** (**bfs.py**).
* l'implémentation de l'algorithme A* via le module **astar** (**astar.py**).

# Arborescence du projet

```text
.
├── README.md                
├── astar.py                 # script d'implémentation de l'algorithme A*
├── bfs.py                   # script d'implémentation de l'algorithme BFS
├── dfs.py                   # script d'implémentation de l'algorithme DFS
├── main.py                  # script principal
├── naze.py                  # génération et manipulation du labyrinthe
├── pyproject.toml           # Configuration du projet et dépendances
├── requirements.txt         # dépendances du projet converties sous un autre format 
└── uv.lock
```
le projet est géré via l'outil uv et les dépendances sont dans le fichier **pyproject.toml**.
le fichier **requirements.txt** a été obtenu en faisant une conversion du fichier **pyproject.toml**.

# Utilisation
## En utilisant *uv*
### Clone
**uv** doit être installé ou il faut l'installer via https://docs.astral.sh/uv/getting-started/installation/.
```
git clone https://github.com/rosty007/maze_search.git
cd maze_search
uv venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
uv sync
```

### Exécution
```
uv run main.py
```

Pour afficher étape par étape l'exploration de chaque algorithme, il faut définir le paramètre **print_steps** comme ci-dessous:
```
uv run main.py --print_steps Y
```

## En utilisant *pip*
### Clone
```
git clone https://github.com/rosty007/maze_search.git
cd maze_search
python -m venv .venv
source .venv/bin/activate (sous Windows : .venv\Scripts\activate)
pip install -r requirements.txt
```

### Exécution
```
python main.py
```

Pour afficher étape par étape l'exploration de chaque algorithme, il faut définir le paramètre **print_steps** comme ci-dessous:
```
python main.py --print_steps Y
```
