# Import des bibliothèques Python
import streamlit as st
import pandas as pd
import numpy as np
import math
from sympy import latex

# Import des bibliothèques thématiques

# Zone de test
# ============

# Tirage d'une liste d'entiers
# ----------------------------
L = [randint(2,6) for i in range(6)]

# Test de la classe créant une question d'algèbre
# -----------------------------------------------
q1 = latex("\\left( "+str(L[0])+"x+"+str(L[1])+"\\right) \\left( "+str(L[2])+"x+"+str(L[3])+"\\right)") 

# Affichage dans streamlit.io
st.write("""
# Développer avec une double distributivité
Développer l'expression ci-dessous :
""")

st.write(q1)
