# Import des bibliothèques thématiques
from themes.nombres import *
from themes.algebre.algebre_2nde import *

# Import des bibliothèques Python
from sympy import *

# Zone de test
# ============

# Tirage d'une liste d'entiers
# ----------------------------
L = liste_nombres(6,["Q" for i in range(6)])

# Test de la classe créant une question d'algèbre
# -----------------------------------------------
for i in range(2):
    for j in range(4):
        for k in range(4):
            q1 = quest_alg((i+1)*100+(j+1)*10+(k+1),L.nbs)
            print(q1.quest)

r=quest_alg(233,[3,5,7,9,11,13])
print(r.quest)
