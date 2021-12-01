import streamlit as st

def f(x):
    return(2*x+3)

def rev_f(y):
    return((y-3)*0.5)

st.write("""
# Calculer une image
Déterminer les images de nombres par la fonction définie par f(x)=2x+3
""")

x = st.slider('Choisir un nombre entier entre -10 et 10', -10, 1, 10)

st.write("L'image de ",x," par f(x)=2x+3 est f(",x,")=",str(f(x)))

st.write("""
# Calculer un antécédent
Déterminer l'antécédent de nombres pour la fonction définie par f(x)=2x+3
""")

y = st.slider('Choisir un nombre entier entre -10 et 10', -10, 1, 10)

st.write("L'antécédent de ",y," pour f(x)=2x+3 est f(",str(rev_f(y)),")=",y)
