# EXERCICES 2
#Type de Donnees de Base
import random
import math
from hypothesis import strategies

#2.1.1 CALCUL D'UNE PUISSANCE
#Affecter la valeur de 3 a la puissance 7 a la variable big

#2.1.1 REPONSE
big = 3**7
print(big)

#2.1.2 RESTE DE LA DIVISION
#Affecter a la variable reste le reste de la division de 1525 par 7

#2.1.2 REPONSE
reste = 1525 % 7
print(reste)

#2.1.3 CONVERSION EN ENTIER
#Affecter a la variable entier (un entier) la valeur de la variable flottante (un nombre a virgule flottante)
flottante = random.uniform(1,100)
print(flottante)

#2.1.3 REPONSE
entier = int(flottante)
print(entier)

#2.1.4 CALCUL D'UNE NORME
#Calculer la norme du vecteur v = (x, y)
x = random.randint(1,100)
y = random.randint(1, 100)

#2.1.4 REPONSE
v = math.sqrt(x**2 + y**2)

#2.2.1 AFFECTATION D'UNE CHAINE
#Affecter la chaine "Hello world" a la variable chaine

#REPONSE 2.2.1
chaine = "Hello world"
print(chaine)

#2.2.2 CONCATENATION DE DEUX CHAINES
#Concatener les chaines chaine1 et chaine2
chaine1 = strategies.text(alphabet = 'abcdef', min_size=5, max_size=10).example()
chaine2 = strategies.text(alphabet = 'abcdef', min_size=5, max_size=10).example()

#2.2.2 REPONSE
phrase = chaine1+', '+chaine2
print(phrase)

#2.2.3 MINUSCULE ET MAJUSCULE
#Affecter a minus, la chaine de caractere toute en minuscule
#Affecter a majus, la chaine de caractere toute en majuscule
chaine = strategies.text(alphabet= 'ABCDEF', min_size=5, max_size=15).example()
print("chaine =", chaine)

#2.2.3 REPONSE
minus = chaine.lower()
majus = minus.upper()
print('minu =', minus)
print('majus =', majus)

#2.2.4 FONCTION REPLACE
#Remplacez, dans phrase, toutes les occurences de la chn1 par la valeur de la chn2
phrase = 'Bonjour le monde!'
chn1 = 'on'
chn2 = 'xx'

#2.2.4 REPONSE
phrase2 = phrase.replace(chn1, chn2)
print(phrase2)

#2.2.5 FONCTION STRIP
#Retirez de la chaine phrase, tous les blancs qui precedent sont premier mot
phrase = '\n\t      Bonjour le monde!'
print(phrase)

#2.2.5 REPONSE
phrase2 = phrase.lstrip()
print(phrase2)

#2.2.6 FONCTION SPLIT
#Affecter a la variable mot la liste des mots de la variable phrase
phrase = 'Bonjour le monde!'

#2.2.6 REPONSE
mot = phrase.split()
print(mot)

#2.3.1 LISTE VIDE
#Affecter a liste une liste vide

#2.3.1 REPONSE
liste = []

#2.3.2 CREATION D'UNE LISTE
#Creer une liste a partir des 2, 3.1416, 'Bonjour le monde!"

#2.3.2 REPONSE
liste = [2, 3.1416, 'Bonjour le monde!']
print(liste)

#2.3.3 LISTE A PARTIR D'UNE CHAINE
#Creer une liste a partir des elements de bonjour le monde

#2.3.3 REPONSE
liste = list('Bonjour le monde!')
print(liste)

#2.3.4 CONCATENATION DE DEUX CHAINES
#Concatener lst1 et lst2
lst1 = strategies.lists(strategies.integers(), min_size=5).example()
lst2 = strategies.lists(strategies.integers(), min_size=5).example()
print(lst1)
print(lst2)

#2.3.4 REPONSE
liste = lst1 + lst2
print(liste)

#2.3.5 AJOUTER UN ELEMENT A UNE LISTE
#Ajouter la chaine "Bonjour le monde!" a la fin de liste1
liste = strategies.lists(strategies.text(alphabet='abcdefABCDEF', max_size=5), min_size=3).example()

#2.3.5 REPONSE
liste.append('Bonjour le monde!')
print(liste)

#2.3.6 INSERER UN ELEMENT DANS UNE LISTE
#Inserer 'hasta la vista' a la position n de la liste
liste = list('Make my day!')
n = 3

#2.3.6 REPONSE
liste.insert(n, 'hasta la vista, baby!')
print(liste)

#2.3.7 TRI D'UNE LISTE
#Trier les elements de la liste
liste = [1, 3, 10, 4, 9]

#2.3.7 REPONSE
liste.sort()
print(liste)

#2.3.8 DECOUPAGE D'UNE LISTE
#Decoupe la liste 'liste' a partir de l'indice i et l'afficher. La sous liste coutiendra n elements
liste = [1, 43, 'fruit', 44, 3.2, 2, 88]
i=2
n=4

#2.3.8 REPONSE
print(liste[i:i+n])

#2.3.9 DECOUPAGE D'UNE SOUS LISTE 2
#À l'intérieur de liste, découpez une sous-liste qui échantillone un caractère sur deux en commençant par la fin et en remontant vers le début 
# affectez le résultat à la variable result.
liste = [1, 43, 'fruit', 44, 3.2, 2, 88]

#2.3.9 REPONSE
resultat = liste[::-2]
print(resultat)

#2.3.10 CONCATENATION DE DEUX SOUS-LISTES
#En utilisant un seul énoncé Python, assemblez une nouvelle liste en combinant les 3 premiers et les 4 derniers éléments de liste, et affectez le résultat à la variable result.
liste = strategies.lists(strategies.integers(min_value=-100, max_value=100), min_size=8, max_size=15).example()
print(liste)

#2.3.10 REPONSE
resultat = liste[:3] + liste[-4:]
print(resultat)

#QUIZ 1. ASSEMBLAGE D'UNE PHRASE
#On vous demande de construire une phrase en joignant bout-à-bout les mots de cette liste, en les séparant par un espace, et en terminant la phrase par un point.
mot = ['Je', 'suis', 'un', 'bon', 'developpeur']

#QUIZ 1. REPONSE
phrase = ' '.join(mot) + '.'
print(phrase)
