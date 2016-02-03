# Moyenne pour un nombre au hasard entre le min et le max : 7,2612895
# Moyenne pour un nombre au hasard entre le min et le max : 5,799738
# Dichotomie

from random import *
from math import *

somme=0
i=0

while i<100000:

    onCherche = True
    minimumNbCache = 1
    maximumNbCache = 100000000
    nbEtapes=0

    nbCache = ceil(random()*maximumNbCache)
    # print(nbCache)
    # print()

    while onCherche :
        n=ceil((maximumNbCache-minimumNbCache)/2)+minimumNbCache
    
        if n<minimumNbCache or n>maximumNbCache :
            print(n,"  ",maximumNbCache,"  ",maximumNbCache)

        if n==nbCache :
            onCherche=False
            #print("Nombre trouve !")

        if n > nbCache :
            maximumNbCache=n-1
            #print("n superieur : ",n,"  ",maximumNbCache,"  ",minimumNbCache)

        if n < nbCache :
            minimumNbCache=n+1
            #print("n inferieur : ",n,"  ",maximumNbCache,"  ",minimumNbCache)

        nbEtapes+=1

    i+=1
    somme+=nbEtapes
    #print("Ca a mis "+str(nbEtapes)+" etapes")

print (somme/100000)


    