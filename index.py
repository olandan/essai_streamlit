# Import des bibliothèques thématiques
from themes.nombres import *
from themes.algebre.algebre_2nde import *

# Import des bibliothèques Python
import streamlit as st

# Zone de test
# ============

# Tirage d'une liste d'entiers
# ----------------------------
L = liste_nombres(6,["D" for i in range(6)])

# Test de la classe créant une question d'algèbre
# -----------------------------------------------
q1 = quest_alg(111,L.nbs)
st.write("""
# Développer avec une double distributivité
Développer l'expression ci-dessous :
""")

st.latex(q1.quest)
