# Bibliothèque de tirages au sort de nombres
# ==========================================

# Import des bibliothèques Python
# -------------------------------

from sympy import Rational
from random import randint

class liste_nombres:

    def __init__(self,combien=5,ensemble=["N","N","N","N","N"]):

        # Méthode créant une instance
        self.taille_liste = combien # Taille de la liste de nombres
        self.nb_type = ensemble # Liste des ensembles de nombres
        self.nbs = self.Nbs() # Tirage des nombres
        
    
    def Nbs(self):

        # Méthode tirant au hasard des nombres
        nbs = []
        for i in range(self.taille_liste):
            # Si on veut un entier naturel
            if self.nb_type[i] == "N" :
                nbs.append(randint(1,12))
            # Si on veut un nombre décimal non entier
            elif self.nb_type[i] == "D" :
                nbs.append(round(randint(1,12)+0.1*randint(0,9)+0.01*randint(1,9),2))
            # Si on veut un nombre rationnel
            elif self.nb_type[i] == "Q" :
                nbs.append(Rational(randint(1,12),randint(2,6)))
                while nbs[-1]%1 == 0:
                    nbs[-1] = Rational(randint(1,12),randint(2,6))

        return(nbs)
