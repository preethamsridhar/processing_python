
class drop(object):
    
    def __init__(self, y=0, x=0, yspeed=0):    
        self.x = random(width)
        self.y = random(-200, height)
        self.z = random(0, 20)
        self.drop_length = map(self.z, 0, 20, 20, 40) 
        self.yspeed = map(self.z, 0, 20, 4, 10)
        
    def fall(self):
        self.y += self.yspeed
        self.gravity = map(self.z, 0, 20, 0, 0.20)
        self.yspeed += self.gravity
        
        if self.y > height:
            self.y = random(-200, -100)
            self.yspeed = map(self.z, 0, 20, 4, 10)
            
        
    def show(self):
        self.thick = map(self.z, 0, 20, 2, 5)
        strokeWeight(self.thick)
        stroke(138, 43, 226)
        line(self.x, self.y, self.x, self.y + self.drop_length)
      
