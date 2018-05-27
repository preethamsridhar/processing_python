from drop import drop
   
no_drops = 2000                 
def setup():
    size(4000, 3000)
    global d
    d = []
    for i in range(no_drops):
        d.append(drop())
    
def draw():
    background(230, 230, 250)
    stroke(4)
    line(1000, 1000, 1000, 1010)
    for i in range(no_drops):
        d[i].fall()
        d[i].show()
    
