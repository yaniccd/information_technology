# CHAPITRE 9
# Apercu des librairie standard

# MODULE datatime
# date et heure du jour
# addition et soustraction de dates
# support des fuseaux horaires, des années bissextiles, etc.
# classes:
# date: date (an, mois, jour) ;
# time: heure du jour (heure, minute, seconde, microseconde) ;
# datetime: date et heure ;
# timedelta: durée entre deux heures ou dates.
from datetime import date
a = date.today()
print(a)
b = a - date(2009, 10, 21)
print(b)
print(b+a)

from datetime import datetime
print(datetime.today())

print(dir(date))
print(dir(datetime))

# MODULE random
# nombres pseudoaleatoire
# bit, entier ou reel
# distrubtion uniforme ou gaussienne

# Fonctions principales:
# random() : réel aléatoire dans l'intervalle  [0,1]  ;
# uniform(a, b) : réel aléatoire dans l'intervalle  [𝑎,𝑏]  ;
# randrange([start,] stop [,step]) : élément aléatoire d'un range défini par start, stop et step ;
# randint(a, b) : entier aléatoire dans l'intervalle  [𝑎,𝑏]  ;
# choice(seq) : choix aléatoire d'un élément dans une séquence seq ;
# shuffle(seq) : permute aléatoirement les éléments d'une séquence seq ;
# gauss(mu, sigma) : variable gaussienne de moyenne mu et d'écart type sigma.
import random
#reel random
x = random.random()
print(x)

#liste entiers randoms
y = [random.randrange(-10, 10, 2) for i in range(9)]
print(y)

#shuffle d'une liste
a = [i for i in range(2,10)]
print(a)
random.shuffle(a)
print(a)

#loi normal
b = [random.gauss(0,1) for i in range(9)]
print(b)
print(sum(b)/len(b))

c = [random.gauss(0,1) for i in range(1000)]
print(sum(c)/len(c))

print(dir(random))

# MODULE math
# Toute une panoplie de fonctions mathématiques :
# puissances et logarithmes ;
# fonctions trigonométriques ;
# conversion d'angles ;
# fonction hyperboliques ;
# constantes e** et **pi.
# Il y a aussi le module cmath pour les fonctions équivalentes sur les nombres complexes.

import math
print(dir(math))

#MODULE re (regular expression)
# Une expression régulière permet de représenter un ensemble de chaînes de caractères :
# utilise des codes spéciaux de substitution, de groupement et de quantification ;
# le | permet de séparer deux expressions alternatives ;
# les () permettent de former une sous-expression pour lui appliquer des opérateurs de quantification ;
# le ? spécifie que l'expression précédente peut être présente ou absente ;
# le * spécifie que l'expression précédente peut être présente un nombre indéterminé de fois (y compris être absente) ;
# le + spécifie que l'expression précédente doit être présente au moins une fois.

# Les caractères suivants ont aussi une signification spéciale :
# . correspond à n'importe quel caractère sauf la fin de ligne ;
# ^ correspond au début de la chaîne ;
# $ correspond à la fin de la chaîne, ou au dernier caractère devant une fin de ligne ;
# {m} spécifie que l'expression précédente doit être présente exactement m fois ;
# {m,n} spécifie que l'expression précédente doit être présente entre m et n fois ;
# [] permet de spécifier un ensemble de caractères.

# Les fonctions principales sont :
# compile(exp) : pour créer un objet expression ;
# match(str) : pour déterminer si la chaîne est un cas particulier de l'expression ;
# search(str) : pour trouver une occurrence de l'expression dans la chaîne ;
# findall(str) : pour trouver toutes les occurrences de l'expression dans la chaîne.
import re
exp = re.compile('a+')
print(exp.findall('abcdefgaabcdefgaaabcdefg'))
print(re.findall('a+', 'abcdefgaabcdefgaaabcdefg'))
print(re.findall('[0-9]*', 'a0123bc456def789'))
print(re.findall('[0-9]+', 'a0123bc456def789'))
ch = 'abc, de ,fghij,k,l,mnopq'
print(re.split(',', ch))

# MODULE pickle
# Permet de sérialiser/désérialiser les objets Python pour :
# les écrire sur disque ;
# les écrire dans une base de données ;
# les transmettre sur le réseau.
# On peut à peu près tout sérialiser :

# None, True et False ;
# les entiers, les nombres à virgule flottante, les nombres complexes ;
# les chaînes de caractères ;
# les tuples, les listes, les ensembles et les dictionnaires ;
# les fonctions et les classes.
# Les principales méthodes sont :
#
# dump(obj, fich) : écrit dans le fichier fich, la séquence d'octets correspondant à l'objet obj après sérialisation ;
# dumps(obj) : retourne la séquence d'octets correspondant à l'objet obj après sérialisation ;
# load(fich) : retourne (désérialise) l'objet correspondant à la séquence d'octets contenue dans le fichier fich ;
# loads(bytes) : retourne (désérialise) l'objet contenu dans la séquence d'octets bytes.
# Le module définit aussi deux classes :
#
# Pickler(fich) : pour sérialiser des objets dans le fichier fich ;
# Unpickler(fich) : pour extraire les objets contenus dans le fichier fich.
import pickle
# f = open('toto.pkl', 'wb')
# p = pickle.Pickler(f)
# p.dump('allo')
# p.dump(['allo', 1234, {1:'bonjour', 5:19}])
# f.close()
#
# f = open('toto.pkl', 'rb')
# u = pickle.Unpickler(f)
# print(u.load())
# Attention: les fichiers doivent être ouverts en mode « binaire »

# MODULE glob
# Permet de facilement spécifier des chemins à la « Unix » pour nos manipulations de fichiers :
#
# glob(chemin) : retourne une liste de fichiers qui correspondent à chemin ;
# iglob(chemin) : idem glob, mais retourne un itérateur au lieu d'une liste.

# Par exemple, pour connaître tous les fichiers du répertoire courant qui contiennent au moins un chiffre :
import glob
print(glob.glob('./*[0-9]*'))

# Ou tous les fichiers qui se terminent par l'extension .py :
print(glob.glob('*chap'))