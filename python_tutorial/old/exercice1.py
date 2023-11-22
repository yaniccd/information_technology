# EXERCICES 1
#Introduction et Syntaxe de Base
import random

#1.1.1 USAGE DU PRINT
#afficher la valeur de 1+2+3+4 a l'aide du print

#1.1.1 REPONSE
print("1+2+3+4 =", 1+2+3+4)

#1.1.2 AUTRE USAGE DU PRINT
#Afficher un message a l'aide de print

#1.1.2 REPONSE
print("Ceci est un message")

#1.2.1 AFFECTATION SIMPLE
#Affecter 257 a la variable a

#1.2.1 REPONSE
a = 257

#1.2.2 ADDITION ET AFFECTATION
#Additioner 12 a la variable b et affecter le tout a la variable b
a = random.randint(1,100)

#1.2.2 REPONSE
b = a + 12

#1.2.3 CALCUL D'UN EXPRESSION
#Affecter a b la valeur de 3a/(a+12)
a = random.randint(1,100)

#1.2.3 REPONSE
b = 3*a/(a+12)

#1.2.4 FONCTION INPUT
#Utilisez input() pour lire la valeur entrer au clavier et affecter cette valeur a la variable valeur.

#1.2.4 REPONSE
valeur = input("Entrez la valeur :")
print("la valeur de valeur est de", valeur)


#QUIZ 1. VOLUME D'UN PRISME RECTANGULAIRE
#Calculer le volume du prisme de les dimension sont donnees ci-dessous
largeur = random.randint(1, 100)
longeur = random.randint(1, 100)
hauteur = random.randint(1, 100)

#QUIZ 1. REPONSE
volume = largeur*longeur*hauteur
print("le volume est de", volume)