# CHAPITRE 12.2
# INTRODUCTION AU CALCUL SCIENTIFIQUE - matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Reference
#   http://matplotlib.sourceforge.net/index.html
#   http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
#   http://videolectures.net/mloss08_hunter_mat/

# Dans jyputer notebook, pour afficher des graphiques matplotlib
#   %matplotlib inline

# Le module matplotlib est en fait un « package » qui contient plusieurs modules. Pour faire des graphiques, il faut importer le sous-module pyplot.
# La fonction plot de ce sous-module est la fonction principale qui trace les graphiques :
plt.plot([1,2,3,4])
plt.xlabel('toto')
plt.ylabel('tata')
plt.title('mon titre')
# Apres un graphique, pour l'afficher dans une ide comme pycharm
plt.show()
# Dans cet exemple simple, on lui fournit un seul itérable (ici une liste) et la fonction plot se débrouille afin de tracer
# quelque chose d'intelligent. Cet itérable est interprété comme une séquence d'ordonnées. Un nombre équivalent d'abcisses sont générés
# automatiquement (0, 1, 2, 3) et associés aux ordonnées afin de tracer une courbe.

# Autre exemple
# 'ro' specifie la couleur
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--')     # red dotted lines
plt.plot(t, t**2, 'bs')   # blue squares
plt.plot(t, t**3, 'g^')   # green up triangles
plt.plot(t, t**3, 'b:')   # green up triangles
plt.show()

# Voici un autre exemple qui trace trois sous-graphes distincts :
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.figure('nom de image') # nom du graphique
plt.subplot(211) #sous graphique dans la meme image
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()



# On peut aussi ajouter des annotations
ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
    arrowprops = dict(facecolor='black', shrink=0.05),)
plt.ylim(-2,2)
plt.show()

# courbe en coordonnees polaires
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0, 1, 0.001)
theta = 2*2*np.pi*r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
           xy=(thistheta, thisr),   # theta radius
           xytext=(0.05, 0.05),     # fraction, fraction
           textcoords='figure fraction',
           arrowprops=dict(facecolor='black', shrink=0.05),
           horizontalalignment='left',
           verticalalignment='bottom',
           )
plt.show()