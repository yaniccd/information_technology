#CHAPITRE 4.4
#Les fichiers
#un fichier est un objet qui possede un nom et un chemin
#un fichier contient soit des lignes de textes, soit des sequences d'octets

#
#ouverture d'un fichier. Renvoie une erreur si le fichier n'existe pas.
chemin = 'chap4.4/chap44.txt'
fich = open(chemin, 'w')
#la fonction open() a un argument mode pour le type d'ouverture
#'w' pour write. Le fichier est efface s'il existe deja. Dangereux!
#'r' pour lecture
#'x' pour ecriture, mais le fichier ne doit pas preexister. il sera cree
#'a' pour ecriture. Le fichier est cree, si necessaire, mais jamais efface. L'ecriture se fait a la fin du fichier (append).

#pour ecrire dans un fichier. write retourne aussi le nombre de caracteres qui ont ete ecrit dans le fichier
fich.write('Bonjour le monde!\n')
#pour fermer le fichier. On ne peut etre certain que l'ecriture a bien ete fait avant de fermer le fichier!
fich.close()
#utilisation de la methode with. Le fichier est automatiquement fermee a la fin du with
with open(chemin, 'a') as fich:
    fich.write('Il etait une fois,\nUn petit bonhomme')
#read permet la lecture du ficher (en entier par defaut)
with open(chemin, 'r') as fich:
    x=fich.read()
print(x,'\n')
#pour lire une ligne a la fois. strip retire le saut de ligne a la fin de la ligne
with open(chemin, 'r') as fich:
    print(fich.readline().strip())
    print(fich.readline().strip())
    print(fich.readline().strip())
#readlines retourne un liste de lignes
with open(chemin,'r') as fich:
    print(fich.readlines())
#on peut aussi lire toutes les lignes grace a une boucle
with open(chemin, 'r') as fich:
    for ligne in fich.readlines():
        print(ligne.strip())
#encore plus simple, on peut iterer sur le fichier directement
with open(chemin, 'r') as fich:
    for ligne in fich:
        print(ligne.strip())

#Ecriture dans un fichier a l'aide d'un print
#il suffit de specifier au print d'ecrire dans le fichier et non a la console
chemin2 = 'chap4.4/chap44_2.txt'
with open(chemin2, 'w') as fich:
    for i in range(4):
        print('numero de ligne : {}'.format(i+1), file=fich)
with open(chemin2, 'r') as fich:
    for ligne in fich:
        print(ligne.strip())

#Mode Binaire
#Par defaut, on prend en consideration que nos fichiers contiennent que des lignes de textes.
#Ce n'est pas toujours le cas.
#'...b' permet de specifier le mode binaire. On perd alors la notion de ligne
chemin3 = 'chap4.4/chap44_3.txt'
with open(chemin3, 'wb') as fich:
    fich.write('Ce texte est binaire'.encode('utf-8'))
with open(chemin3, 'rb') as fich:
    print(fich.read().decode('utf-8'))

#Module Pickle
#ce module permet la conversion d'objets python en sequence d'octets
import pickle
chemin4 = 'chap4.4/chap44_4.txt'
liste = [123, {'a': 100, 23: 'b'}]
with open(chemin3, 'wb') as fich:
    fich.write(pickle.dumps(liste)) #dumps encode

with open(chemin3, 'rb') as fich:
    seq_bin = fich.read()
    print(seq_bin, type(seq_bin))
    liste = pickle.loads(seq_bin) #loads decode
    print(liste, type(liste))

#Module json
#fonctionne de la meme facon qui pickle, mais utilise une representation textuelle de l'objet
#on est donc pas obliger d'ouvrir le fichier en mode binaire
import json
chemin5 = 'chap4.4/chap44_5.txt'
liste = [123, {'a': 100, 23: 'b'}]

with open(chemin5, 'w') as fich:
    fich.write(json.dumps(liste))

with open(chemin5, 'r') as fich:
    chaine=fich.read()
    print(chaine, type(chaine))
    liste=json.loads(chaine)
    print(liste, type(liste))