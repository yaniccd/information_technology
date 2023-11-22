#CHAPITRE 5
#Retour sur les Fonctions et Complexite Algorithmique

#5.1 Les Tuples
#Type sequentiel ordonne immuable
#similaire a la liste, mais on ne peut modifier son contenu apres sa creation
#iterable, elements heterogene
a=() #creation d'un tuple vide
print(a)
#Cest en fait la virgule qui va faire le tuple lorsqu'il n'y a qu'un element
a=(3)
print(a) #a est une expression entiere
a=(3,)
print(a) #a est un tuple.
#il n'y a plus d'ambiguite lorsque le nombre d'elements dans le tuple est superieur a 1
a=(3,7)
print(a)
#tuple complexe
a=(0, 'abc', (1,2,3))
print(a)
#le tuple a les memes operateurs que la liste
a=(1,2)+(3,4)
print(a)
a=(1,2)*4
print(a)
#le decoupage se fait avec les []
t=(1,2,3,4)
t=(t[0:2],t[2:4]) #tuple de tuples
print(t)
#on peut convertir un tuple en liste grace a list
t=('a','b','c','d')
l=list(t)
print('tuple : ',t)
print('liste : ',l)
#le tuple ne supporte pas le tri sort() car le tuple est immuable!

#par rapport a la liste, le tuple est utile pour:
#   la certitude que son contenu ne changera pas au cours du temps
#   le mecanisme d'appel de fonctions que nous verons plus tard
#   pour des raisons d'efficacite puisque son nombre d'element est constant

#5.2 Retour sur les Fonctions
#pre-conditions : conditions que les entrees de la fonction doivent respecter
#post-conditions : conditions sont les garanties sur ce qui est retourne par la fonction

#argument nomme
def fonc1(a,b,c):
    return a+b+c

print(fonc1(a=1,b=3,c=1))

#argument par default
def fonc2(a,b,c=3):
    return a+b+c

print(fonc2(1,2))

#argument etoile
#affectation multiple. La variable etoile ramasse tous les arguments positionnels sans correspondance
#nombre arbitraire d'arguments
#un seul argument etoile possible
#tous les arguments a droite de l'argument etoile doivent obligatoirement etre nomme
def fonc3(a,b,*c):
    print(a,b,c)

fonc3(1,2,3,4,5)

def fonc4(a,b,*c,d):
    print(a,b,c,d)

fonc4(1,2,3,4,5,d=99)

#on peut place une etoile sans arguments pour dire que tous les arguments a la droite de l'etoile doivent etre nommes
def fonc5(a,b,*,c=0):
    return a+b+c

print(fonc5(1,2))
print(fonc5(1,2,c=3))

#implentation d'un fonction min
def min1(*args):
    minimum = args[0]
    for arg in args[1:]:
        if arg < minimum:
            minimum = arg
    return minimum

#implementation 2, en laissant python faire la premiere affectation
def min2(premier, *args):
    for arg in args:
        if arg < premier:
            premier = arg
    return premier

#implementation 3 (moins performante) tri d'abord
def min3(*args):
    return sorted(args)[0]

print(min1(1,17,-3,-17,47))
print(min2(1,17,-3,-17,47))
print(min3(1,17,-3,-17,47))

#argument doublement etoile
#Python affecte a cet argument un dictionnaire avec l'ensemble des arguments nommes par l'utilisateur mais non definis par la fcontion
def fonc6(**kargs):
    print(kargs)

fonc6(age=17, nom='Hubert', tel='819 772 7645')

#les arguments d'une fonction sans valeur par default sont obligatoires.

#Syntaxe
#fonc(valeur, ...) valeurs normales affectees par position
#fonc(nom=valeur, ...) valeur nommees affectees par nom
#fonc(*iterable) passage des elements de l'objet iterable en tant que valeurs normales
#fonc(**dictionnaire) passage des elements de l'objet dictionnaire en tant que valeurs nommees

#exemple ou une fonction doit traiter un nombre variable d'arguments
def fonc7(a): pass
def fonc8(a,b,c): pass

test=True

if test:
    action, args = fonc7, (1,)
else:
    action, args = fonc8, (1,2,3)

action(*args)
#mecanisme puissant permettant d'appeler des fonctions a priori inconnue possedant des arguments egalement inconnus.

#Fonction anonyme (fonction lambda)
#Avantage:permet de definir une fonction a l'interieur d'une expression
#les deux fonctions suivantes sont equivalentes
def fonc9(x,y,z):
    return x+y+z

fonc10 = (lambda x,y,z : x+y+z)

print(fonc9(1,2,3)==fonc10(1,2,3))

#autre exemple de fonction anonuyme
fonctions = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for f in fonctions:
    print(f(2), end=' ')
print()

#Fonction generatrice et enonce yield
#permet de creer des types iterables
#utilise yield plutot que return
#yield suspend temporairement l'execution pour renvoyer une valeur intermediaire

def carre(n):
    for i in range(n):
        yield (i+1)**2

x=carre(10)
for i in carre(10):
    print(i, end=' ')
print()
print(list(carre(10)))
#on accede a un element a la fois grace a next
print(next(x))
print(next(x))
print(next(x))

#la fonction send injecte dans la fonction generatrice, une nouvelle valeur a chaque iteration
def gen():
    for i in range(10):
        x = yield i
        print(x)

g=gen()
print(next(g))
g.send(77)
g.send(88)
print(next(g)) #88 a remplace le 2

#expression generatrice
#<expression> for <cible> in <iterable> if <test>
#produit un iterable plutot qu'une liste
x=(c*4 for c in 'spam')
print(x)
print(next(x))
print(next(x))

#La fonction range que nous avons vu n'est rien d'autre qu'une fonction generatrice
def rangeSimplifie(deb, fin):
    while deb<fin:
        yield deb
        deb+=1

for i in rangeSimplifie(-3,10):
    print(i, end=' ')
print()

#La fonction enumerate s'applique a un iterable d'elements et retourne un iterable de tuple
#1. contient l'indice de l'element courant.
#2. la valeur de l'element courant.
#utile dans un for pour pouvoir avoir la valeur de la liste en plus d'une valeur d'increment
liste=['a', 1, 5, 'z', 3.1416]
for i, val in enumerate(liste):
    print(i, val)

#5.3 Les affectations multiples
#Exemple
a,b,c = 0, 2+4, 'spam'
print(a,b,c)
#une affectation multiple est en fait que l'affectation d'un tuple de valeurs a un tuple de variables
#ce qui defini le tuple, c'est la presence de virgules et non la presence de parantheses

#Utilisation d'une variable etoilee
#les variables orphelines sont regroupees dans une liste
a, *b, c = 0, 'allo', 3+4, 8
print(a,b,c)

#on peut meme placer un iterable a droite du signe d'egalite
((a,b),c) = ('sp','am')
print(a,b,c)
a,b,c,d = 'spam'
print(a,b,c,d)

#on peut egalement faire:
a=b=c=0

#les affectations multiples sont utilent pour echanger deux valeurs
a=1
b=2
a,b=b,a
print(a,b)

#5.4 Introduction a la complexite algorithmique

#Soit MSS, l'algorithme de maximum sub sum
#On cherche la sous-sequence adjacente dont la somme est maximal

#MSS1 en O(n^3)
#on test tous les combinaisons de debut et fin de liste en n^2
#puis on fait la somme de chacune de ces sous liste en n
def mss1(sequence):
    n=len(sequence)
    maxsum=0
    for i in range(n):
        for j in range(i,n):
            thissum=0
            for k in range(i,j):
                thissum+=sequence[k]
            if thissum > maxsum:
                maxsum = thissum
    return maxsum

#On test l'algo avec une sequence aleatoire
import random

def genData(n):
    return [random.randint(-10,10) for _ in range(n)]

data =genData(1000)

import time
debut = time.perf_counter()
x=mss1(data[:])
print('la sous-sequence maximum {} a ete trouvee en {} secondes'.format(x, time.perf_counter()-debut))

#MSS2 en O(n^2)
#on memorise ici la somme precedente
def mss2(sequence):
    n=len(sequence)
    maxsum=0
    for i in range(n):
        thissum=0
        for j in range(i,n):
            thissum+=sequence[j]
            if thissum > maxsum:
                maxsum = thissum
    return maxsum

debut = time.perf_counter()
x=mss2(data[:])
print('la sous-sequence maximum {} a ete trouvee en {} secondes'.format(x, time.perf_counter()-debut))

#MSS3 en O(n)
#une sous-sequence negative ne peut precede la MSS
def mss3(sequence):
    n=len(sequence)
    thissum=maxsum=0
    j=0
    while j < n:
        thissum += sequence[j]
        if thissum > maxsum:
            maxsum = thissum
        elif thissum < 0:
            thissum =0 #on recommence la somme a partir d'ici
        j+=1
    return maxsum

debut = time.perf_counter()
x=mss3(data[:])
print('la sous-sequence maximum {} a ete trouvee en {} secondes'.format(x, time.perf_counter()-debut))
