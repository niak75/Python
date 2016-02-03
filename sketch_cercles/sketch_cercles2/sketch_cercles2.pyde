rayon=10
ancienRayon=30
x=350
y=350
direction=0

def setup():
    size(700,700)
    noStroke()
    background(0)
    frameRate(30)
    
def draw():
    global rayon
    global ancienRayon
    global x
    global y
    global direction

    direction+=random(-80,80)
    rayon=ancienRayon+random(-3-((rayon-10)/3),3-((rayon-10)/3))
     
    x+=sin(radians(direction))*(ancienRayon+rayon)
    y+=cos(radians(direction))*(ancienRayon+rayon)
    ancienRayon=rayon
    
    ellipse(x,y,rayon*2,rayon*2)
    print(direction)
    
    if x>width or x<0 or y>height or y<0 :
        direction-=90
    
    
    
    
    
    