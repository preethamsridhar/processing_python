angle = 15 *PI / 180
level = 0

def setup():
    size(1500, 2000)

def draw():
    background(0)
    stroke(255, 255, 0)
    translate(width/2, height)
    branch(500)
    level = 0
    
def branch(line_len):
    strokeWeight(random(1,3))
    stroke(random(0, 250), random(0,250), 255)
    line(0, 0, 0, -line_len)
    translate(0, -line_len)
    # global level
    # level += 1
    # print(level)
    
    if line_len > 1:
        pushMatrix()
        rotate(angle)
        branch(line_len * 0.67)
        popMatrix()
        pushMatrix()
        rotate(-angle)
        branch(line_len * 0.67)
        popMatrix()
