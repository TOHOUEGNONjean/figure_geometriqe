#coding: utf-8

'''
	nous allons esseyer importer notre bibliothèque turtul
'''
from turtle import *
from math import * 
 #creons notre écrant

figure = Screen ()
#j'ai nommé mon ecrant figure..

figure.screensize( 1500 ,1000)# pour obtenir les barres de defilement
#ma fenêtre sera nommé 'figure géométrique'. 
#en utilisant la méthode title() on aura

colormode(255) #pour utiliser lesvaleurs de 0 à 255

pensize(5) #donne une taille a notre crayon

figure.bgcolor(10,200,60) #on attibut une couleur verte à l'ecran
figure.title(' Figure géométrique ')

'''
Notre ecrant est enfin crér, 

servons-nous du crayon pour commencer notre dessin

Premièrement dessinons un carré
-----------------------------------------------------
Un carré à 4 côtés et 4 angles droits
------------------------------------------------------
NB: NOUS TRAVAILLONS DANS UN REPERE ORTHONOMME
-------------------------------------------------

le crayon au depart est placé au centre du repère

pour le moment, on ne modifie pas sa position d'origine

debut
	le deplacé d'une distance donné vers la droite

	------forward(120)

	je ne déplace d'une distance de 120px

A chaque itération:
	tourné de 90° vers la doite et deplacer d'une distance donné vers la droite
	----left(90)

apres trois itératons :
	ON ARRETE
'''
up ()

goto ((-200,0)) 

down ()

#initialisons notre entier i à 0


i = 0
while i < 4 :
	forward ( 120 )

	left ( 90 )

	i += 1
# et là ça marche bien 
#------------------------------------------------------------
# remarquons que le crayon est revenu a l'origine du repère

#commen dans la pratique, on le deplace pour consruit un autre figure

up () #il permet de soulever le crayon

goto ( 0, 0 ) # ramener à l'origine du repère

down () #et le positionne

#le parallellogramme

'''
	on se deplade de 200px vers la droite 
	-------forward ( 200 )

	cette fois ci on tourne de 30° vers la droite
	------right ( 30°)
	on se deplade de 90px vers la droite 
	-------forward ( 100 )
	on tourne vers la gauche de 150° (la notion des angles alternes internes est utilisée)
	--------- right ( 30 )
	 on avance de 120px

le crayon s'incline  d'un angle en fonction de sa direction précédente
'''
forward ( 200 )

left ( 30 )

forward ( 100 )

left ( 150 )

forward ( 200 )

left ( 30 )

forward ( 100 )
left(150) #Enfin on le repositionne parallèlement à l'axe des abscisses 

# nous venons donc de crér notre parallelogramme

# penssons à créer le triangle (le triangle de préférence)


up()
goto((300,0)) # se positionner au point de coordonné (-400;0)

down()
'''
	le tiangle rectange a un angle droit

'''
forward (120)# la base du rectangle
up()

goto(300,0) # la hauteur
down()
left(90)
forward(200) #l'hypothénus

goto(420,0)

#pour maintenir l'écran, utilisons la methode mainloop()
figure.mainloop()


#c'est la fin
