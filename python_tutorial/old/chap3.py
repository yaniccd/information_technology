#CHAPITRE 3
#Notion de Fonctions

#3.1 Introduction aux fonctions
#comme une fonction mathematique, recoit des arguments, retourne un resultat
#maximise la reutilisation. Minimise la redondance
#Qualite d'une fonction; coherence, independance, concision.
#coherente : Une seule tache.
#independante: Le resultat dependant uniquement des entrees (et non pas de variables globales)
#concision : limiter la longueur de nos fonctions (un encran de code).
#en python, l'indentation est necessaire!

def fonc():
    print('Ma premiere fonction.')

fonc()

def fonc2(x, y):
    return x*y  #l'enonce return est optionnel dans une fonction. Sans return, la fonction retourne None

print(fonc2(2,3))

#une fonction est un objet.
#on peut affecter une fonction a un objet
a= fonc2
print(a('a',4)) #cette fonction est polymorphe

#porte d'une variable globale vs locale
#x et fonc3 sont des variables globales. z et y sont locales
x = 99
def fonc3(x,y):
    z=x+y
    return z

w=fonc3(x+4,1)
print(w)

#usine a fonction (fonction qui retourne une fonction)
def usine(n):
    def puissance(x):
        return x**n
    return puissance

carre = usine(2)
cube = usine(3)
print(carre(3))
print(cube(3))

#par default, les arguments sont affectes en fonction de leur position..
#on peut aussi les nommer explicitement
def fonc4(a,b,c):
    print(a,b,c)

fonc4(1,2,3)
fonc4(b=1,a=2,c=3)

#valeur par defaut dans une fonction
def fonc5(a,b,c=4):
    print(a,b,c)

fonc5(1,2)

#3.2 Le Type Booleen
#True et False sont reseve en python
#utile pour la comparaison et la prise de decision
print(3<4)
print(3>4)
print(3==4)
print(3!=4)
print([4,3,1]<[3,4]) #on compare chaque element un a un. Il s'arrete au premier faux
#on peut combiner grace a and, or et not.
print(3<4 and 3>5)
print(3<4 or 3>5)

#les booleens sont tres utile pour les enoncees conditionnel
score = input('Entrez votre score.')
score = int(score)
if score <60 :
    print("Vous auriez pu faire mieux.")
else:
    print("Felicitation!")

#3.3 L'Enonce Conditionnel
#le if (le elif et le else sont optionnel)
age = input("Entrez votre age : ")
age=int(age)
if age<18:
    print("Vous etes jeune!")
elif age<30:
    print("Vous etes un jeune adulte!")
elif age<60:
    print("Vous etes un adulte!")
else:
    print("Vous etes vieux!")

#enonce indente
x=True
y=True
if x:
    if y:
        print('x et y sont vrais')

#nous avons vu le if sous forme d'enonce.
#on le retrouve aussi sous forme d'operateur
x=True
y=33; z=44
a = y if x else z
print(a)