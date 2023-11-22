# EXERCICE 11
# RETOUR SUR LA PROGRAMMATION FONCTIONNEL

# 11.1.1 FONCTION MAP A UN SEUL ITERABLE
# Définissez une fonction génératrice nommée map qui reproduit le comportement du map de la librairie standard,
# mais dans le cas particulier où celui-ci n'accepte qu'un seul objet itérable. Notez bien que dans ce cas, la fonction
# sur laquelle on applique le map doit aussi est restreinte à un seul argument positionnel.

# 11.1.1 REPONSE
def map(func, iter):
    assert callable(func)
    assert hasattr(iter, '__iter__')
    for i in iter:
        yield func(i)

for i in map(lambda x: x**2, range(5)):
    print(i)

# 11.1.2 FONCTION MAP A N ITERABLES
# Définissez une fonction génératrice nommée map qui reproduit le comportement du map de la librairie standard,
# y compris dans le cas général où celui-ci accepte en argument un nombre arbitraire d'objets itérables. Notez bien que
# la fonction sur laquelle on applique le map doit accepter un nombre d'arguments positionnels égal au nombre d'objets
# itérables reçus par le map.

# 11.1.2 REPONSE
def map2(func, *iter):
    assert callable(func)
    for i in iter:
        assert hasattr(i, '__iter__')
    for i in zip(*iter):
        yield func(*i)

# 11.2.1 DECORATEUR OBSELETE
# Définissez un décorateur nommé obsolète qui affiche à la console le message suivant avant d'appeler la fonction décorée :
#
# Cette fonction est obsolète, vous ne devriez plus l'appeler!
# Faites en sorte que votre décorateur puisse fonctionner avec n'importe quelle fonction.

# 11.2.1 REPONSE
def obselete(func):
    def nouvelle_fct(*args, **kargs):
        print('Cette fonction est obselete')
        return func(*args, **kargs)
    return nouvelle_fct

# 11.3.1 SUITE DE FIBONACCI RECURSIVE
# Implantez la suite de Fibonacci définie par la formule de récurrence.
# Exprimez votre solution sous la forme d'une fonction récursive nommée fibo.

# 11.3.1 REPONSE
def fibo(n):
    assert n >= 0, "l'argument doit etre positif ou nul"
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(10))

# 11.3.2 FIBONNACI NON RECURSIVE
# Exprimez votre solution sous la forme d'une fonction NON récursive nommée fibo.

# 11.3.2 REPONSE
def fibo(n):
    assert n >= 0, "L'argument doit etre positif"
    if n==0 or n==1:
        return n
    tmp1, tmp2 = 1, 0
    for _ in range(2, n+1):
        tmp1, tmp2 = tmp1+tmp2, tmp1    # les deux assignations sont faites en simultane
    return tmp1

print(fibo(10))

# 11.3.3 FIBONNACI GENERATRICE
# Exprimez votre solution sous la forme d'une fonction génératrice nommée fibo qui retourne la séquence des  𝐹(𝑖) ,  ∀𝑖≤𝑛 .

# 11.3.3 REPONSE
def fibo(n):
    assert n >= 0, "L'argument doit etre positif"
    tmp1, tmp2 = 1, 0
    for i in range(n+1):
        if i == 0 or i == 1:
            yield i
        else:
            tmp1, tmp2 = tmp1+tmp2, tmp1
            yield tmp1

for i in fibo(10):
    print(i)

# 11.3.4 TOUR DE HANOI
# Définissez une fonction nommée hanoi capable de résoudre le problème de la tour de Hanoï, problème qui consiste à déplacer
# les disques d'une pile de disques (la tour) d'un piquet à un autre, par exemple du piquet 1 au piquet 3
# en respectant les régles suivantes :
#
# on ne peut déplacer qu'un seul disque à la fois ;
# à aucun moment un disque de diamètre supérieur ne doit reposer sur un disque de diamètre inférieur.
# L'algorithme récursif suivant permet de résoudre ce problème pour une tour de  𝑛  disques :
#
# Si  𝑛=0 , ne rien faire;
# Sinon:
# déplacer récursivement une tour de  𝑛−1  disques, du piquet de départ vers le piquet intermédiaire ;
# transférer un disque du piquet de départ vers le piquet de destination ;
# déplacer récursivement une tour de  𝑛−1  disques, du piquet intermédiaire vers le piquet de destination.
# Votre fonction doit accepter les quatre arguments suivants :
#
# la hauteur de la tour en nombre de disques ;
# l'indice du piquet de départ ;
# l'indice du piquet de destination ;
# l'indice du piquet intermédiaire.
#
# et retourner la liste des couples  (𝑖,𝑗)  représentant la séquence des déplacements de disques, depuis
# le piquet  𝑖  vers le piquet  𝑗 , qui permet de résoudre le problème. Dans le cas d'un nombre de disque négatif,
# votre fonction doit soulever une exception de type ValueError.

def hanoi(n, i, j, k):
    if n < 0:
        raise ValueError()
    if n == 0:
        return []
    return hanoi(n-1, i, k, j) + [(i, j)] + hanoi(n-1, k, j, i)

for i in hanoi(5, 1, 2, 3):
    print(i)