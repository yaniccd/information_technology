# EXERCICE 15
# EXERCICES DE REVISION

import numpy as np
from matplotlib import pyplot as plt
import math

# QUIZ 1 AFFICHAGE D'UN LOSANGE

# Définissez une fonction nommée losange qui accepte en argument un nombre entier  𝑛  et qui affiche à la console un losange
# sur  2𝑛+1  lignes et  2𝑛+1  colonnes. Par exemple pour  𝑛=5 , vous devez afficher :


def losange(n):
    if n < 0:
        raise ValueError("Entrez une valeur positive")
    if n == 0:
        return
    print(' '*n + '.')
    for i in range(1, n+1):
            print(' '*(n-i) + '.' + ' '*(2*i-1) + '.')
    for i in range(n-1, 0, -1):
            print(' '*(n-i) + '.' + ' '*(2*i-1) + '.')
    print(' ' * n + '.')

losange(5)
losange(1)

# QUIZ 2 STATISTIQUE DE BASE

# Définissez une fonction nommée statistiques qui accepte en argument une
# liste de nombres et qui retourne un tuple de deux valeurs: la moyenne et l'écart type des nombres.


def statistique(n):
    moy = sum(n)/len(n)
    sd = 0
    if len(n) > 0:
        sd = (sum((x-moy)**2 for x in n)/(len(n)-1))**.5
    else:
        sd = 0
    return moy, sd

liste = [1, 2, 3, 4, 5]
print(statistique(liste))

# QUIZ 4 QUESTION A CHOIX MULTIPLE

# En procédant par héritage, définissez une nouvelle classe nommée ChoixMultiple qui encapsule une question à choix multiple,
# c'est-à-dire une question dont les instances possèdent une séquence de choix de réponse en plus de l'énoncé et de la réponse.
# Dans ce cas, la réponse à la question prend la forme de l'indice du bon choix dans la séquence de choix. Réutilisez autant que
# possible les méthodes de la classe de base. Ajoutez cependant une méthode nommée ajouter_choix qui permet d'ajouter un choix
# de réponse à la question. Également, réimplantez la méthode afficher afin d'afficher l'énoncé de la question ainsi que les
# différents choix de réponse, chacun d'entre eux sur une ligne distincte.


class Question:
    def __init__(self):
        self._enonce = ''
        self._reponse = ''

    def definir_enonce(self, x):
        self._enonce = x

    def definir_reponse(self, x):
        self._reponse = x

    def verifier_reponse(self, x):
        return self._reponse == x

    def afficher(self):
        print(self._enonce)


class ChoixMultiple(Question):
    def __init__(self):
        super().__init__()
        self.choix = []

    def ajouter_choix(self, x):
        self.choix.append(x)

    def afficher(self):
        super().afficher()
        for i, x in enumerate(self.choix):
            print('{}- {}'.format(i+1, x))

# QUIZ 5 CLASSE CADENAS
# Définissez une classe nommée Cadenas qui simule le fonctionnement d'un cadenas à combinaison :
# L'interface de votre classe doit supporter les fonctionnalités suivantes :
# Un constructeur qui accepte les trois numéros de la combinaison ;
# Une méthode ouvrir qui retourne un booléen indiquant si oui ou non la bonne combinaison a été entrée correctement depuis la dernière réinitialisation ;
# Une méthode réinitialiser qui permet d'oublier les actions précédentes de l'utilisateur et de placer la roulette sur le zéro ;
# Une méthode tourner qui accepte en argument un nombre  𝑛  et qui tourne la roulette de  𝑛  unités dans le sens
# horaire si  𝑛  est positif, et dans le sens anti-horaire si  𝑛  est négatif.

class Cadenas:
    def __init__(self, x, y, z):
        if x < 0 or x > 40 or y < 0 or y > 40 or z < 0 or z > 40:
            raise ValueError("Combinaison impossible")
        self.cle = [x, -y, z]
        self.combine = [0]

    def ouvrir(self):
        rep = True

        if len(self.combine) != len(self.cle):
            rep = False

        if self.combine[0] < 80: #2 tours obligatoires pour le premier nombre
            rep = False
        else: #valeur du premier nombre
            self.combine[0] = 40 - (self.combine[0]%40)
            if self.combine[0] != self.cle[0]:
                rep = False

        if self.combine[1] > -40 or self.combine[1] <= -80: #exactement un tour obligatoire pour le 2e tour
            rep = False
        else:
            self.combine[1] = -((self.combine[0] - self.combine[1]) % 40)
            if self.combine[1] != self.cle[1]:
                rep = False

        if self.combine[2] > 40: #moins d'un tour a la fin
            rep = False
        else:
            self.combine[2] = 40 - ((self.combine[2] + self.combine[1]) % 40)
            if self.combine[2] != self.cle[2]:
                rep = False

        self.afficher()
        self.reinitialiser()
        return rep

    def reinitialiser(self):
        self.combine = [0]

    def tourner(self, n):
        if n*self.combine[-1] >= 0: #on tourne dans le meme sens
            self.combine[-1] += n
        else:
            self.combine.append(n)

    def afficher(self):
        print(self.combine)


cad = Cadenas(10, 20, 35)
cad.afficher()
cad.tourner(80)
cad.afficher()
cad.tourner(30)
cad.afficher()
cad.tourner(-40)
cad.afficher()
cad.tourner(-10)
cad.afficher()
cad.tourner(25)
cad.afficher()
print(cad.ouvrir())

# QUIZ 6 REPONSE D'UN CIRCUIT
# Soit un circuit RC
# constitué d'une source de tension continue  𝐵 , d'une résistance  𝑅  et d'un condensateur  𝐶 . Au temps  𝑡=0 ,
# l'interrupteur est actionné afin de fermer le circuit. La réponse  𝑣(𝑡)  du circuit est alors définie par l'équation suivante :
# 𝑣(𝑡)=𝐵(1−𝑒−𝑡/(𝑅𝐶))
# Définissez une fonction nommée réponse qui calcule la réponse du circuit en fonction de ses paramètres.
# Les arguments de la fonction doivent être dans l'ordre :
# le temps  𝑡  ;
# la tension  𝐵  ;
# la résistance  𝑅  ;
# le condensateur  𝐶 .
# Construisez un tableau numpy contenant cent valeurs de temps échantillonnées uniformément dans l'intervalle  [0,1]  secondes.
# Appelez ce tableau temps. Utilisez la fonction réponse afin de calculer les 100 réponses correspondantes du circuit RC, avec  𝐵=12  volts,
# 𝑅=5000  ohms et  𝐶=100  microfarads ( 10−6  farads). Stockez vos résultats dans un tableau numpy nommé tension.
# Finalement, utilisez matplotlib pour tracer le graphique de la réponse du circuit dans l'intervalle choisi.

def reponse(t, b, r, c):
    return b*(1-math.exp(-t/r/c))

temps = np.linspace(0, 1, 100)
tension = np.array(list(reponse(t, b=12, r=5000, c=0.0001) for t in temps))
plt.plot(temps, tension)
plt.title("Reponse d'un circuit RC avec R=5000 et C=0.0001")
plt.xlabel('temps (secondes)')
plt.ylabel('tension (volts)')
plt.show()
