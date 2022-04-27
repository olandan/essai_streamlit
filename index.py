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
      q = quest_alg(i*100+j*10+k,L.nbs)
      if  q.LaTeX() != "None":
        st.write("""
    # Question n°""",str(compt),""" :""")
        st.latex(q.quest)
        compt += 1
