# Moyenne pour un nombre au hasard entre le min et le max : 7,2612895
# Moyenne pour un nombre au hasard entre le min et le max : 5,799738
# Dichotomie

def setup():
    size(700, 700)
    background(0)
    noStroke()
    


def draw():

    somme=0
    i=0

    while i<10000:

        onCherche = True
        minimumNbCache = 1
        maximumNbCache = frameCount%width
        nbEtapes=0

        nbCache = ceil(random(1)*maximumNbCache)
        # print(nbCache)
        # print()

        while onCherche :
            
            if frameCount%1400 <= 700 :
                 n=ceil((maximumNbCache-minimumNbCache)/2)+minimumNbCache
            
            if frameCount%1400 > 700 :
                n = ceil(random(minimumNbCache-1,maximumNbCache))
    
            if n<minimumNbCache or n>maximumNbCache :
                print(n,"  ",maximumNbCache,"  ",minimumNbCache)

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

    ellipse(frameCount%width,700-somme/200.0,5,5)


 

    
    
    
 


    