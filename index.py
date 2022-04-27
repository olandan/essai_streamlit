# Import des bibliothèques thématiques
from themes.nombres import *
from themes.algebre.algebre_2nde import *

# Import des bibliothèques Python
from random import randint
import streamlit as st

# Zone de test
# ============

# Tirage d'une liste d'entiers
# ----------------------------
L = liste_nombres(6,["N" for i in range(6)])

# Test de la classe créant une question d'algèbre
# -----------------------------------------------
q1 = quest_alg((i+1)*100+(j+1)*10+(k+1),L.nbs)

# Affichage dans streamlit.io
st.write("""
# Développer avec une double distributivité
Développer l'expression ci-dessous :
""")

st.write(q1.quest)
