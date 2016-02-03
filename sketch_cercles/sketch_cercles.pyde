nbCercles=20

def setup():
    size(700,700)
    noStroke()
    
def draw():
    nbCercles=frameCount//60
    background(0)
    for y in range(0,nbCercles) :
        for x in range(0,nbCercles) :
            diametre=width/nbCercles*2
            diametre1=diametre*mouseX/width
            diametre2=diametre-diametre1
            
            if (y+x%2)%2!=0 :
                ellipse((2*x+1)*(width/(nbCercles*2)),(2*y+1)*(height/(nbCercles*2)),diametre1,diametre1)
            else :
                ellipse((2*x+1)*(width/(nbCercles*2)),(2*y+1)*(height/(nbCercles*2)),diametre2,diametre2)
         

    

