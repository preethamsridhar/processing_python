class Branch(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.finished = False
        
    def show(self):
        stroke(255)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        
    def jitter(self):
        self.end.x += random(-2, 2)
        self.end.y += random(-2, 2)
    
    def branch_right(self):
        dir = PVector.sub(self.end, self.start)
        dir.rotate(15 * PI / 180)
        dir.mult(0.80)
        newEnd = PVector.add(self.end, dir)
        right = Branch(self.end, newEnd)
        return(right)
    
    def branch_left(self):
        dir = PVector.sub(self.end, self.start)
        dir.rotate(-15 * PI / 180)
        dir.mult(0.80)
        newEnd = PVector.add(self.end, dir)
        left = Branch(self.end, newEnd)
        return(left)
    
                
