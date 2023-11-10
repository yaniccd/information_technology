#CHAPITRE 1
#Introduction et Syntaxe de Base

#Une affectation comporte trois elements; un nom de variable, un operateur et une expression
pi = 3.1415
rayon = 5
perimetre = 2*pi*rayon
aire = pi*rayon**2
print(perimetre)
print(aire)

#Un erreur apparait a la console si on essait de faire afficher une variable non definie.
#Les commentaires, debut par #, ne sont pas execute. Ils sont present pour facilite la lecture du code
#Un nom de variable ne peut debuter par un chiffre
#Le seul caractere special qu'on puisse utiliser dans un nom de variable est _
#Certain nom de variable, tel True, False et None sont reserv a python

#operateur arithmetique
23+2 #addition
23-2 #soustraction
23*2 #multiplication
23/2 #divison
23//2 #division entiere
23%2 #modulo
23**2 #exponentiation

#La fonction print affiche a la console la valeur d'une ou plusieurs expressions
print(2, pi, rayon)
print()
print("perimetre = ", 2*pi*rayon)

#Autre fonction utile; input. Permet la lecteur d'une entree au clavier
nom = input("Entrez votre nom : ")
print("Bonjour, ", nom, "!")

