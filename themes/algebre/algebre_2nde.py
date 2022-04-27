# Bibliothèque de questions d'algèbre
# ===============================================
#
# SOMMAIRE
# --------
#
#   I. Développer une expression........(1xx)
#
#       0. Simple distributivité..........(10x)
#           a. Type a(bx+c).................(101)
#           b. Type a(bx-c).................(102)
#       1. Double distributivité..........(11x)
#           a. Type (ax+b)(cx+d)............(111)
#           b. Type (ax-b)(cx+d)............(112)
#           c. Type (ax+b)(cx-d)............(113)
#           d. Type (ax-b)(cx-d)............(114)
#       2. Identités remarquables.........(12x)
#           a. Type (a+b)^2.................(121)
#           b. Type (a-b)^2.................(122)
#           c. Type (a+b)(a-b)..............(123)
#
#   II. Factoriser une expression.......(2xx)
#
#       1. Cas simples....................(21x)
#       2. Identités remarquables.........(22x)
#           a. Type ax^2+2ab+b^2............(221)
#           b. Type ax^2-2ab+b^2............(222)
#           c. Type a^2-b^2.................(223)
#       3. Ecritures quotients............(23x)
#           a. Type a/(cx+d)+e..............(231)
#           b. Type a/(cx+d)-e..............(232)
#           c. Type a/(cx+d)+e/(fx+g).......(233)
#           d. Type a/(cx+d)-e/(fx+g).......(234)
#
#================================================

# Import de la bibliothèque de génération de nombres
# --------------------------------------------------
from themes.nombres import *

# Import des bibliothèques
# ------------------------
from sympy import Rational, latex, symbols
from random import randint

# Définition de la classe
# -----------------------
class quest_alg:

    def __init__(self,niveau, liste=liste_nombres().nbs, variable="x"):

        # Méthode créant une instance
        self.niveau = niveau # code de la question voulue
        self.var = symbols(variable) # variable de la question
        self.liste = liste # liste de nombres
        self.aff_nbs = self.Aff_Nbs() # code LaTeX des nombres
        self.quest = self.LaTeX() # création du code de la question

    def Aff_Nbs(self):

        # Méthode créant le code LaTeX des nombres
        aff_nbs = []
        for i in range(len(self.liste)):
            if type(self.liste[i]) == int:
                aff_nbs.append(str(self.liste[i]))
            elif type(self.liste[i]) == float:
                aff_nbs.append(str(int((self.liste[i]*100)//100))+","+str(int((self.liste[i]*100)%100)))
            else:
                aff_nbs.append("\\dfrac{"+str(self.liste[i].p)+"}{"+str(self.liste[i].q)+"}")
        return(aff_nbs)

    def LaTeX(self):

        # Méthode créant le code LaTeX de la question voulue (code lié au sommaire)

        # Suppression des '1' devant les variables
        

        # I. Développements
        # 0. Simple distributivité
        if self.niveau // 10 == 10:
            # a. Type a(bx+c)
            if self.niveau % 10 == 1:
                return(latex(self.aff_nbs[0]+str(self.var)+"\\left("+self.aff_nbs[1]+str(self.var)+"+"+self.aff_nbs[2])+"\\right)")
            # b. Type a(bx-c)
            elif self.niveau % 10 == 2:
                return(latex(self.aff_nbs[0]+str(self.var)+"\\left("+self.aff_nbs[1]+str(self.var)+"-"+self.aff_nbs[2])+"\\right)")
            else:
                return("None")
        # 1. Double distributivité
        elif self.niveau // 10 == 11:
            # a. Type (ax+b)(cx+d)
            if self.niveau % 10 == 1:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"+"+self.aff_nbs[1]+"\\right) \\left("+self.aff_nbs[2]+str(self.var)+"+"+self.aff_nbs[3])+"\\right)")
            # b. Type (ax-b)(cx+d)
            elif self.niveau % 10 == 2:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"-"+self.aff_nbs[1]+"\\right) \\left("+self.aff_nbs[2]+str(self.var)+"+"+self.aff_nbs[3])+"\\right)")
            # c. Type (ax+b)(cx-d)
            elif self.niveau % 10 == 3:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"+"+self.aff_nbs[1]+"\\right) \\left("+self.aff_nbs[2]+str(self.var)+"-"+self.aff_nbs[3])+"\\right)")
            # d. Type (ax-b)(cx-d)
            elif self.niveau % 10 == 4:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"-"+self.aff_nbs[1]+"\\right) \\left("+self.aff_nbs[2]+str(self.var)+"-"+self.aff_nbs[3])+"\\right)")
            else:
                return("None")
        # 2. Identités remarquables
        elif self.niveau // 10 == 12:
            # a. Cas (a+b)^2
            if self.niveau % 10 == 1:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"+"+self.aff_nbs[1]+"\\right)^2"))
            # b. Cas (a-b)^2
            elif self.niveau % 10 == 2:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"-"+self.aff_nbs[1]+"\\right)^2"))
            # c. Cas (a+b)(a-b)
            elif self.niveau % 10 == 3:
                return(latex("\\left( "+self.aff_nbs[0]+str(self.var)+"+"+self.aff_nbs[1]+"\\right) \\left( "+self.aff_nbs[0]+str(self.var)+"+"+self.aff_nbs[1]+"\\right)"))
            else:
                return("None")

        # Factorisations
        # 1. Avec facteur commun
        elif self.niveau // 10 == 21 :
            return(latex(self.aff_nbs[0]+str(self.var)+"^2 +"+self.aff_nbs[1]+str(self.var)))
        # 2. Identités remarquables
        elif self.niveau // 10 == 22:

            # Définition des codes latex des coefficients
            coef = [self.liste[0]**2 , 2*self.liste[0]*self.liste[1], self.liste[1]**2]
            aff_coef = []
            for i in range(len(coef)):
                if type(coef[i]) == int:
                    aff_coef.append(str(coef[i]))
                elif type(coef[i]) == float:
                    aff_coef.append(str(int((coef[i]*100)//100))+","+str(int((coef[i]*100)%100)))
                else:
                    if coef[i].q == 1:
                        aff_coef.append(str(coef[i].p))
                    else:
                        aff_coef.append("\\dfrac{"+str(coef[i].p)+"}{"+str(coef[i].q)+"}")
            # a. Cas ax^2+2abx+b^2        
            if self.niveau % 10 == 1:
                return(latex(aff_coef[0]+str(self.var)+"^2 +"+aff_coef[1]+str(self.var)+"+"+aff_coef[2]))
            # b. Cas ax^2-2abx+b^2
            elif self.niveau % 10 == 2:
                return(latex(aff_coef[0]+str(self.var)+"^2 -"+aff_coef[1]+str(self.var)+"+"+aff_coef[2]))
            # c. Cas a^2-b^2
            elif self.niveau % 10 == 3:
                return(latex(aff_coef[0]+str(self.var)+"^2 -"+aff_coef[1]+"^2"))
            else:
                return("None")
        # 3. Écritures quotients
        elif self.niveau // 10 == 23:
            # a. Type a/(cx+d)+e
            if self.niveau % 10 == 1:
                return(latex("\\dfrac{"+self.aff_nbs[0]+"}{"+self.aff_nbs[1]+str(self.var)+"+"+self.aff_nbs[2]+"}+"+self.aff_nbs[3]))
            # b. Type a/(cx+d)-e
            elif self.niveau % 10 == 2:
                return(latex("\\dfrac{"+self.aff_nbs[0]+"}{"+self.aff_nbs[1]+str(self.var)+"+"+self.aff_nbs[2]+"}-"+self.aff_nbs[3]))
            # c. Type a/(cx+d)+e/(fx+g)
            elif self.niveau % 10 == 3:
                return(latex("\\dfrac{"+self.aff_nbs[0]+"}{"+self.aff_nbs[1]+str(self.var)+"+"+self.aff_nbs[2]+"}+\\dfrac{"+self.aff_nbs[3]+"}{"+self.aff_nbs[4]+str(self.var)+"+"+self.aff_nbs[5]+"}"))
            # d. Type a/(cx+d)-e/(fx+g)
            elif self.niveau % 10 == 4:
                return(latex("\\dfrac{"+self.aff_nbs[0]+"}{"+self.aff_nbs[1]+str(self.var)+"+"+self.aff_nbs[2]+"}-\\dfrac{"+self.aff_nbs[3]+"}{"+self.aff_nbs[4]+str(self.var)+"+"+self.aff_nbs[5]+"}"))
            else:
                return("None")

        else:
                return("None")
