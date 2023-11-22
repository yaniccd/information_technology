# CHAPITRE 13
# NOTION DE PROGRAMMATION EVENEMENTIELLE

# Plan
# Notion d'événement.
#
# Boucle événementielle :
#
# traitement des événements.
# Module tkinter :
#
# Tcl/Tk ;
# widgets ;
# placement des widgets ;
# traitement des événements ;
# etc.

# Les exemples de code que vous trouverez dans cette leçon ne peuvent malheureusement pas être exécutés dans le
# contexte de ce notebook à partir du serveur web de cours, car celui-ci n'a pas la possibilité/permission de créer
# une fenêtre graphique sur votre ordinateur, à l'extérieur de votre fureteur web. Pour que ces exemples puissent
# fonctionner, il vous faudra télécharger cette leçon sur votre ordinateur, sous la forme d'un fichier avec l'extension .ipynb,
# et la visualiser en faisant appel au logiciel Jupyter exécuté directement sur votre ordinateur. Ce logiciel est
# un programme python qui s'installe facilement avec la commande pip. Il suffit d'exécuter en ligne de commande
# pip3 install jupyter et jupyter sera automatiquement installé sur votre machine. Pour de plus amples détails,
# parcourir la documentation de Jupyter.

# MODULE BY DEFAULT IN PYTHON

# Voir document word
import tkinter as tk
root = tk.Tk()
root.mainloop()

# La création d'un objet Tk provoque la création d'une fenêtre (« top-level frame »). La fenêtre est vide et ne fait rien.
# Pour lui ajouter un widget
root = tk.Tk()
etiq = tk.Label(root, text='Bonjour le monde!')
etiq.grid()
root.mainloop()
# La méthode grid permet de positionner le widget dans le contexte de son parent.
# Ici, le parent de l'étiquette est la fenêtre. Un widget est invisible tant que sa méthode grid n'a pas été appelée.
# C'est suite à l'exécution de grid qu'il devient visible.
# Par défaut, grid centre le widget à l'intérieur du cadre de son parent et ajuste la dimension de
# ce dernier sur la dimension de son contenu. On peut aisément ajouter de l'espace autour du widget en utilisant les arguments padx et pady
# On peut aussi changer la couleur et son libele
root = tk.Tk()
etiq = tk.Label(root, text='Bonjour le monde')
etiq.grid(padx = 200, pady = 200)
etiq['text'] = 'Au revoir' #Habituellement appeler plus tard pour modifier le text du label deja existant
etiq['foreground'] = 'blue'
root.mainloop()

# Chaque widget possède un ensemble d'attributs qui déterminent l'apparence du widget :
#
# les attributs sont stockés dans un dictionnaire ;
# ils possèdent des valeurs par défaut ;
# on peut définir les valeurs de ces attributs au moment de la création du widget à l'aide d'arguments nommés ;
# ou par la suite en utilisant l'opérateur [] du dictionnaire sous-jacent.

# Pour ajouter un bouton au widget
def pressButton():
    print('Le buton a ete presse')

root = tk.Tk()
etiq = tk.Label(root, text = 'Bonjour')
etiq['text'] = 'Bonjour le monde'
etiq['foreground'] = 'Blue'
etiq.grid(padx=20, pady=20)
quitter = tk.Button(root, text='Quitter', command=pressButton)
quitter.grid(pady=10)
root.mainloop()

# Autre exemple de boutton
root = tk.Tk()
root.title('grid()')
cadre = tk.Frame(root)
cadre.grid(padx=20, pady=20)
for i in range(3):
    for j in range(3):
        bt = tk.Button(cadre, text='({},{})'.format(i,j))
        bt.grid(row=i, column=j)
root.mainloop()

# Autre exemple ou on creer deux frames independant contenant chacun une serie de trois etiquettes
root = tk.Tk()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame1.grid(column=0)
frame2.grid(row=0, column=1)
frame1.grid(padx=10, pady=10)
frame2.grid(padx=15, pady=15)
tk.Label(frame1, text='mon').grid(row=0, column=1)
tk.Label(frame1, text='allo').grid(row=0, column=0)
tk.Label(frame1, text='coco').grid(row=0, column=2)
tk.Label(frame2, text='Bonjour').grid(row=0, column=0)
tk.Label(frame2, text='le').grid(row=1, column=0)
tk.Label(frame2, text='monde').grid(row=2, column=0)
frame1['relief']=tk.RIDGE
frame1['borderwidth']=5
frame2['relief']=tk.RAISED
frame2['borderwidth']=5
root.mainloop()

# Widget RadioButton
# Un seul bouton radio actionne a la fois
# ous les boutons d'un même groupe sont associés à un même objet soit de type IntVar, soit de type StringVar.
root = tk.Tk()
x = tk.IntVar()
b1 = tk.Radiobutton(root, text='bouton1', variable=x, value=1, command=lambda: print(x.get()))
b2 = tk.Radiobutton(root, text='bouton2', variable=x, value=2, command=lambda: print(x.get()))
b3 = tk.Radiobutton(root, text='bouton3', variable=x, value=3, command=lambda: print(x.get()))
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
x.set(2)
root.mainloop()