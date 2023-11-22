#CHAPITRE 2
#Type de Donnees de Base

#le package math est un package installer de base avec python
#il contient plusieurs fonctions mathematiques utilent
import math
#2.1 Les Nombres
#Python distingue trois categories de nombres; les entiers (int), les virgules flotantes (float) et les complexes (complex).
print(3+4) #retourne un int
print(3+4.0) #retourne un float

#la fonction int() retourne un entier. Les floats sont tronque et non arrondis
x=int(3/2)
print(x)

#La fonction float() transforme un entier en float.
x=float(x)
print(x)

#les nombres complexes avec la fonction complex(). j pour la partie imaginaire
x=complex(2,5)
y=complex(-2,3)
print(x, y, x+y, x*y)

#on peut ajouter des parantheses a volonte.En l'absence de paranthese, les priorites
#d'operation standard s'appliquent
a=3
b=2
print((a+b)+(a*b))

#2.2 Les chaines de caracteres
#on peut utiliser ' ou "
x="Bonjour l'monde!"
print(x)

#Quelque caracteres speciaux
print('\'') #le caractere '
print('\\') #le caractere \
print('\a') #un son
print('allo\b') #le caractere d'effacement
print('\n') #un saut de ligne
print('\tallo') #tabulation

#operateur de base sur les strings
a='Petit poisson'
b='devient grand.'
print(a+' '+b)

#la fonction len() donne le nombre de caracteres
c='allo'
d=len(c)
print(d)

#pyton supporte le += (mais pas le ++)
phrase = "Je m'appele "
phrase += "Yanic."

#passe une chaine de caracteres en int
c="8866"
c=int(c)
print(c+1)

#on peut multiplier un string
print('allo '*5)

#par default, le print termine avec un saut de ligne. Ce saut de ligne est la valeur par default de l'argument end
print("Bonjour ", end=" ")
print("Yanic")
#index et decoupage
#utiliser [] pour acceder a un element d'une chaine de caracteres comme dans un vecteur
#l'indicage en python commence a 0 et termine un caractere avant la fin specifie!
#trois formes possible a, a:b, a:b:c
a='UneTranche'
print(a[3], a[-3])
print(a[1:3]) #caracteres 1 et 2 seulement
print(a[1:7:2])
print(a, a[:7], a[3:7], a[3:], a[-3:], a[-7:-3], a[3:-3])
x = '0123456789'
print(x, x[::2], x[::-1], x[::-2], x[7:3:-1])
#la chaine de caractere est immuable.
#l'operation a[1]='S' ne fonctionne pas.

#Formatage des chaines
#format permet de constuire des chaines de caracteres
nom=input('Entrez votre nom: ')
print('Bonjour {}!'.format(nom))
#on peut utiliser plusieur variables
famille=input('Entrez votre nom de famille: ')
print('Bonjour {0} {1}!'.format(nom, famille))
print('nom de famille : {1}\nprenom : {0}'.format(nom,famille))
#on peut ommettre les indices si l'ordre est exacte
print('Bonjour {} {}!'.format(nom, famille))
#on peut egalement formater les chaines de caracteres
x='123'
print('---{0}---{0:6}---{0:<6}---'.format(x)) #le 6 specifie qu'on veut 6 colonnes pour l'insertion
#< pour alignement a gauche, > pour alignement a droite, ^ pour centrer
#autre types de formatage
y = 3.141592
print('---{0:8.2f}---{0:^8.4f}---{0:8.2e}---'.format(y))

#autres fonctionnalites
devise = 'Le monde appartient À CELUI qui se lève tôt!'
print(devise.count('a')) #compte le nombre d'occurences
print(devise.find('à')) #trouve la position d'une occurence
print(devise.isdigit()) #determine si la chaine est un chiffre
print(devise.lower()) #renvoie la chaine en minuscule
print(devise.replace('CELUI', 'moi')) #remplace
print(devise.split()) #renvoie une liste de mots
print(devise.upper()) #renvoie la chaine en majuscule

#2.3 Les Listes
#permets de stocker des objets heterogenes (on peut  melanger les types)
#les [] permettent de creer une liste
a=[]
b=[1,2,3,4]
print(a,b)
#comme pour les chaines de caracteres, on accede aux element d'une liste avec les crochets
print(b[2])
#construction d'une liste de listes
c = [a, ['def', 'abc'], b]
print('c = ', c)
print('c[1] = ', c[1])
#on peut utiliser le double crochet pour acceder a une liste d'une liste
print(c[1][0])
#len fonctionne avec les chaines de caracteres
print(len(c))
#on peut transformer une chaine de caracteres en liste grace a la fonction list
d=list('spam')
print(d)
#la liste supporte +, -, *
print(a+b+d)
print(b*4)
#on ajoute un element a la fin grace a append
d.append('!')
print(d)
#la methode index retourne la position de la premiere valeur qui satisfait la recherche
print(d.index('m'))
#on peut inserer a un indice quelconque avec la methode insert
d.insert(d.index('a'), 'r') #insert devant l'element specifie
print(d)
#on retire un element grace a la methode remove. On retire une valeur et non un indice. ON RETIRE SEULEMENT LA 1ERE APPERANCE DE S
d.remove('s')
print(d)
#on peut egalement retirer en specifiant un element grace a del
del d[0]
print(d)
#autres fonctionnalites
liste=[1,2,3,4,5]
liste.reverse() #inverse la liste
print(liste)
liste.extend([11, 12, 13]) #fusion d'une autre liste a la fin de la liste
print(liste)
liste.pop() #retire le dernier element
print(liste)
liste.sort() #tri la liste
print(liste)
#le decoupage d'une liste ce fait de la meme facon que pour les chaines de caracteres