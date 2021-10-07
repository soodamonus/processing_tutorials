TOTAL_DEGREES = 360
radius = 0 
grow = True

def setup():
    global width, height, radius
    # fullScreen()
    size(600, 600)
    background(0)
    noFill()
    stroke(255, 20)
    radius = 0
    
def draw():
    # translate(frameCount, 0)
    center_x = width / 2
    center_y = height / 2
    
    global TOTAL_DEGREES, radius, grow
    
    beginShape()
    # in this loop, we are making 
    for i in range(TOTAL_DEGREES):
        # use perlin noise algorithm
        noiseFactor = noise(i * 0.01, float(frameCount)/100)
        # multiply noiseFactor into x and y because output is always between 0 and 1
        x = center_x + radius * cos(radians(i)) * noiseFactor
        y = center_y + radius * sin(radians(i)) * noiseFactor
        # connect vertices in a circle
        curveVertex(x, y)
    #this function specifies final end shape
    endShape(CLOSE)
    
    # use bool to make
    if grow:
        radius += 1
    else:
        radius -= 1

    if radius == height / 1.5:
        grow = False
        
    if radius == 0:
        grow = True
        background(0)
