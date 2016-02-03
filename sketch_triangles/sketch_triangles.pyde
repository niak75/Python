pointsX = []
pointsY = []

def setup():
    size(700,700)
    noStroke()
    background(0)
    frameRate(3)
    
def draw():
    background(0)
    
    pointsX = []
    pointsY = []
    for x in range(0,3):
        pointsX.append(random(700))
        pointsY.append(random(700))
    
    fill(255)
    # Triangle de base :
    triangle(pointsX[0],pointsY[0],pointsX[1],pointsY[1],pointsX[2],pointsY[2])
    
    fill(0)
    # Deuxième triangle :
    for x in range(0,3):
        pointsX.append((pointsX[x]+pointsX[(x+1)%3])/2)
        pointsY.append((pointsY[x]+pointsY[(x+1)%3])/2)
    triangle(pointsX[3],pointsY[3],pointsX[4],pointsY[4],pointsX[5],pointsY[5])
    
    # Troisièmes triangles
    for x in range(0,3):
        pointsX.append((pointsX[x]+pointsX[x+3])/2)
        pointsY.append((pointsY[x]+pointsY[x+3])/2)
        
        pointsX.append((pointsX[x]+pointsX[(x+2)%3+3])/2)
        pointsY.append((pointsY[x]+pointsY[(x+2)%3+3])/2)
        
        pointsX.append((pointsX[x+3]+pointsX[(x+2)%3+3])/2)
        pointsY.append((pointsY[x+3]+pointsY[(x+2)%3+3])/2)
        
    for x in range(0,3):
        triangle(pointsX[3*x+6],pointsY[3*x+6],pointsX[3*x+7],pointsY[3*x+7],pointsX[3*x+8],pointsY[3*x+8])
    
    
        
    