def setup():
    size(700,700)

def draw():
    contraste=20
    rouge=[]
    vert=[]
    bleu=[]
    for y in range(0,height):
        for x in range(0,width):
            if x==0 or y==0 :
                stroke(125)
                point(x,y)
                rouge.append(125)
                vert.append(125)
                bleu.append(125)
            else :
                r=(rouge[y*width+x-1]+rouge[(y-1)*width+x])/2+random(-contraste,contraste)
                g=(vert[y*width+x-1]+vert[(y-1)*width+x])/2+random(-contraste,contraste)
                b=(bleu[y*width+x-1]+bleu[(y-1)*width+x])/2+random(-contraste,contraste)
                stroke(r,g,b)
                point(x,y)
                rouge.append(r)
                vert.append(g)
                bleu.append(b)
                
         
         
        
        
        
        
    