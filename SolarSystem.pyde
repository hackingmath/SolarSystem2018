'''Planet Exploration
December 7, 2018
'''

G = 30000 #force of gravity

class Planet:
    def __init__(self,loc,vel,sz,img):
        self.loc = PVector(loc[0],loc[1],loc[2])
        self.vel = PVector(vel[0],vel[1],vel[2])
        self.sz = sz
        self.img = img
        self.globe = createShape(SPHERE,self.sz)
        self.globe.setTexture(self.img)
        self.locList = []
        
    def update(self):
        pushMatrix() #saves orientation
        translate(self.loc.x,
                  self.loc.y,
                  self.loc.z)
        
        shape(self.globe)
        popMatrix() #resets to saved orientation
        
        
    def orbit(self):
        
        #calculate earth - moon distance (earth is at origin)
        
        r = sqrt(self.loc.x**2 + self.loc.y**2 + self.loc.z**2)
        radialVector = PVector(self.loc.x,self.loc.y,self.loc.z)
        unitRadialVector = radialVector.div(r)
        F = -G/r**2
        gVector = unitRadialVector.mult(F)
        self.vel.add(gVector)
        self.loc.add(self.vel)
        self.locList.append(PVector(self.loc[0],
                            self.loc[1],
                            self.loc[2]))
        if len(self.locList)>120:
            self.locList = self.locList[:120]
        stroke(255)
        for i,s in enumerate(self.locList):
            if i > 0:
                line(s.x,s.y,s.z,self.locList[i-1].x,
                    self.locList[i-1].y,
                    self.locList[i-1].z)
        noStroke()

def setup():
    global earth, mercury, sun
    size(800,800,P3D)
    earthimg = loadImage("earth.jpg")
    mercuryimg = loadImage("mercury.jpeg")
    sunimg = loadImage("sun.jpg")
    noStroke() #no lines
    earth = Planet((300,0,0), #location
                     (0,0,10), #velocity
                     30,
                     earthimg)
    
    mercury = Planet((100,0,0),
                       (0,0,10),
                       10,
                       mercuryimg)
    sun = Planet((0,0,0),
                       (0,0,0),
                       50,
                       sunimg)
    
    
def draw():
    global earth, mercury, sun
    background(0) #black space
    rot = map(mouseX,0,width,0,TWO_PI)
    tilt = map(mouseY,0,height,0,-TWO_PI)
    translate(width/2,height/2,0)
    rotateY(rot)
    rotateX(tilt)
    mercury.orbit()
    earth.orbit()
    earth.update()
    mercury.update()
    sun.update()
