# Import des bibliothèques Python
import streamlit as st

# Import des bibliothèques thématiques
from themes.nombres import *
from themes.algebre.algebre_2nde import *

# Zone de test
# ============

# Tirage d'une liste d'entiers
# ----------------------------
L = liste_nombres(6,["Q" for i in range(6)])

# Test de la classe créant une question d'algèbre
# -----------------------------------------------
for i in range(4):
  for j in range(4):
    for k in range(4):
      compt = 1
      if quest_alg(111,L.nbs) != "none":
        st.write("""
    # Question n°"""+str(compt)+""" :""")
        st.latex(q1.quest)
