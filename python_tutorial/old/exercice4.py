# EXERCICES 4
#Elements de Procedure
import random

# 4.1.1 PATRON D'ETOILES
# ecrire une fonction patron d'etoile qui recoit un argument n et retourne un triangle inverse d'etoile

# 4.1.1 REPONSE
def afficher_patron(n):
    for i in range(n):
        print((n-i)*'*')

afficher_patron(5)

# 4.1.2 PATRON DE CHIFFRES
# definir une fonction qui recoit en argument un entier n et retourne le patron suivant
# 0
# 01
# 012

# 4.1.2 REPONSE
def afficher_patron(n):
    ligne = ''
    for i in range(n):
        ligne += str(i%8)
        print(ligne)

afficher_patron(10)

# 4.1.3 MINIMUM D'UNE LISTE DE NOMBRES
#Écrivez une fonction nommée minimum qui accepte en argument une liste de nombres et retourne sa valeur minimum. Dans le cas d'une liste vide, retournez la valeur None.

# 4.1.3 REPONSE
def minimum(x):
    if not x:
        return None
    min = x[0]
    for i in x[1:]:
        if i < min:
            min = i
    return min

# 4.1.4 COMPTE DES NOMBRES POSITIFS D'UNE LISTE
# definir une fonction qui compte le nombre de valeur positif dans une liste

# 4.1.4 REPONSE
def compte_positif(liste):
    compteur = 0;
    for i in liste:
        if i > 0:
            compteur += 1
    return compteur

# 4.2.1 COUT D'UN PANIER D'EPICERIE
# Définissez une fonction nommée calculer_coût qui accepte en entrée ces deux dictionnaires :
# le dictionnaire du contenu d'un panier ;
# le dictionnaire des prix ;
# et qui retourne le coût total de ce panier.
contenu = {'pomme':3, 'orange':2, 'patate':10}
prix = {'pomme':1.5, 'orange':3.0, 'patate':1, 'banane':0.75}

# 4.2.1 REPONSE
def calculer_cout(contenu, prix):
    cout = 0
    for i in contenu.keys():
        cout += contenu[i] * prix[i]
    return cout

print(calculer_cout(contenu, prix))

#4.2.1 REPONSE 2
def calcuer_cout2(contenu, prix):
    return sum(prix[item] * quantite for item, quantite in contenu.items())

print(calcuer_cout2(contenu, prix))

# 4.2.2 COMPTER LES OCCURENCES DANS UNE LISTE
# Définissez une fonction nommée compter_éléments qui accepte en entrée une liste de valeurs et
# retourne en sortie un dictionnaire des nombres d'occurences de chaque élément distinct dans la liste
liste = ['chat', 'chat', 'chien', 3, 2, 2, 3]

# 4.2.2 REPONSE
def compter_element(liste):
    dico = {}
    for valeur in liste:
        dico[valeur] = dico.get(valeur, 0) + 1
    return dico

print(compter_element(liste))

# 4.3.1 CONSTRUCTION D'UN ENSEMBLE
# construire un ensemble a partir des elements de la liste
liste = [random.randint(1, 5) for i in range(random.randint(5, 15))]

# 4.3.1 REPONSE
X = set(liste)
print(X)

# 4.3.2 PLANIFIER UNE REUNION
# Définissez une fonction nommée planifier_réunion qui accepte en entrée une liste des ensembles de disponibilités
# des personnes devant participer à une réunion, et retourne l'ensemble des plages horaires où tous les participants sont disponibles.
dispos = [{1, 2, 3, 4}, {2, 3, 4}, {1, 2, 3}, {4, 5, 3, 2}]

# 4.3.2 REPONSE
def planifier_reunion(liste):
    if liste:
        resultat = liste[0]
        for valeur in liste[1:]:
            resultat &= valeur
        return resultat
    else:
        return set()

print(planifier_reunion(dispos))

# QUIZ 1. SOIREE CINEMA
# Définissez une fonction nommée calculer_coût qui accepte les arguments suivants :
# adulte : le nombre de billets au prix adulte ;
# enfant : le nombre de billets au prix enfant ;
# popcorn : le nombre de popcorns ;
# boisson : le nombre de boissons gazeuzes.
# Votre fonction doit retourner le coût total. Utilisez les noms d'argument ci-dessus et ne faites aucun affichage dans votre fonction.

# QUIZZ 1. REPONSE
def calcuer_cout(adulte, enfant, popcorn, boisson):
    return adulte*11.0 + enfant*5.0 + max(popcorn - adulte//2, 0)*10.0 + max(boisson - enfant//2)*5.0

# QUIZ 2. VALEUR D'UN INVESTISSEMENT
# On vous demande de définir une fonction nommée valeur_investissement permettant de calculer des intérêts composés
# sur un capital initial. Votre fonction doit accepter les trois arguments suivants :
# capital, le montant du capital initial sur lequel on veut calculer des intérêts ;
# taux, le taux d'intérêt annuel (en %) ;
# duree, la durée de l'investissement (en années).
# Votre fonction doit retourner la valeur totale de l'investissement à la fin de la période spécifiée.

# QUIZ 2. REPONSE
def valeur_investissement(capital, taux, duree):
    return capital*(1 + taux/100)**duree