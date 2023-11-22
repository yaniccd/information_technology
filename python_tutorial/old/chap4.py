#CHAPITRE 4
#Elements de Procedure

#4.1 L'enonce Repetitif
#Permet de faire des boucles tant et aussi longtemps qu'une certaine condition est respectee

#Afficher les elements d'une liste a l'aide d'un for
maListe = [1,2,3,4]
for i in maListe:
    print(i)
else: #le else est facultatif. Executer une seule fois a la fin si on ne croise pas de break avant.
    print('Fin')
#on aurait aussi pu utiliser, dans le for, les enonces break et continue
#break permet de mettre fin prematurement au for selon une condition
#continue permet de mettre fin a l'iteration actuelle et passer tout de suite a la prochaine iteration

#exemple pour trouver la somme d'une liste. Il est important d'initialiser a 0
liste=[1,2,3,4,5,6,7]
somme=0
for i in liste:
    somme+=i
print(somme)

#exemple produit
produit=1
for i in liste:
    produit*=i
print(produit)

#utilisation du if in
items = ['aaa', 111, (4,5), 2.01]
cles = [(4,5), 3.14]

for cle in cles:
    if cle in items:
        print("cle = ", cle, " trouvee.")
    else:
        print("cle = ", cle, "non trouvee.")

#utilisate de break and nonprint
#on saute toutes le noprint
#on met fin a liste des qu'on croise stop
items = ['un', 'pomme', 'noprint', 34, 3.1416, [], 'stop', 54321, -12]

for item in items:
    if item=='stop':
        break
    elif item=='noprint':
        continue
    else:
        print(item)

#range permet de produire une sequence d'entiers
#range(start, stop, step), start et step sont facultatif. 0 et 1 par default
print(list(range(5)))
print(list(range(0,5,2)))
for i in range(-3,3):
    print(i)

#operateur for
#[exp for objet in iterable]
a = [i+10 for i in range(5)]
print(a)

#boucle while
#continue tant qu'une condition est respectee
#le programmeur doit gerer lui meme la variable de controle
#break et continue peuvent etre utilises avec le while
#en python, on n'utilise jamais le while. Toujours le for.
#attention aux boucles infinieeeeeeeee
n=0 #initialisation de la variable de controle
while n<20:
    print("Je te dois {}$".format(n))
    n+=1

#for: une meilleure solution
for i in range(20):
    print("Tu me dois {}$".format(i))

#4.2 Les Dictionnaires
#permet de stocker des associations cles valeurs.
#c'est donc un contenant associatif
#on accede a une valeur des le dictionnaire a l'aide d'une cle
#la cle est immuable.
#les cles et valeurs peuvent etre heterogenes
a={} #dictionnaire vide
print(a)
#ici, spam et eggs sont les cles. 25 et 37, les valeurs
a={'spam':25, 'eggs':37}
print(a)
#l'acces ce fait comme dans une liste, avec []. Toutefois, au lieu d'un indice, on utilise une cle
print(a['spam'])
#on peut ajouter une nouvelle valeur a un dictionnaire
a['pain'] = 44
print(a)
#on peut, de la meme facon, changer une valeur qui existe deja
a['pain'] = 99
print(a)
#la valeur peut meme etre un autre dictionnaire
a['fruit'] = {'fraises':56, 'mangues':43}
print(a)
print(a['fruit']['mangues'])
#methodes des dictionnaires
print(a.copy()) #permet de faire une copie d'une dictionnaire
print(a.keys()) #renvoie les cles du dictionnaire
print(a.values()) #renvoie les valeurs du dictionnaire
print(a.items()) #renvoie les items du dictionnaire (cle, valeur)
print(len(a)) #renvoie le longueur du dictionnaire
del a['fruit'] #supprime un item du dictionnaire en fonction d'une cle
print(a)
#on peut aussi utiliser la methode get plutot que les []
if a.get('spam')==None:
    print('Les dictionnaires ne contient pas spam')
else:
    print('la valeur de spam est {}.'.format(a.get('spam')))
#get permet aussi un deuxieme argument qui sera retourne si la cle n'est pas trouve
x=a.get('jambon','invalide')
print(x)
#les dictionnaires sont des iterables
#les dictonnaires ne sont pas ordonnes. Faire une boucle sur un dictionnaire peut renvoyer les elements dans un drole d'ordre
#on boucle implicitement sur les cles
dico = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for cle in dico:
    print('cle : {}, valeur : {}'.format(cle,dico[cle]))
#on peut aussi boucler explicitement sur les cles
for cle in dico.keys():
    print('cle : {}, valeur : {}'.format(cle, dico[cle]))
#ou encore, boucler sur les valeurs. Dans ce cas, on ne peut recuperer les cles!
for valeur in dico.values():
    print('{}: {}'.format('?', valeur))
#on peut finalement boucler sur les items
for item in dico.items():
    print("item : {}".format(item))
#ou encore, en separant les cles et valeurs de l'item
for cle, valeur in dico.items():
    print('cle : {}, valeur : {}'.format(cle, valeur))

#4.3 Les Ensembles
#Les ensembles, comme les dictionnaires, sont non ordonnes
#L'ensemble est une collection de cles uniques
#C'est un dictionnaire sans valeur
#Chaque element est unique et immuable
#Les ensembles permetent la reunion, l'intersection, la soustraction et la difference symetrique
#on construit un ensemble grace a set()
x=set('spam')
print(x)
#on peut aussi creer un ensemble grace aux accolades {}
y = {'h', 'a', 'm'}
print(y)
#la reunion
print(x|y)
#l'intersection
print(x&y)
#la difference (ce qui est dans x moins ce qui est egalament dans y
print(x-y)
#difference symetrique (ce que x et y n'ont pas de commun)
print(x^y)
#autres fonctions utiles
x.add(3.1415) #permet d'ajouter un element
print(x)
x.remove('s') #permet de retirer une element
print(x)
x.update(y) #ajoute a x tous les elemens de y
print(x)
