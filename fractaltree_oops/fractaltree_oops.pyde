from branch import Branch

angle = 15 *PI / 180
leaves = []
tree = []
count = 0

def setup():
    size(1500, 2000)
    a = PVector(1500/2 , 2000)
    b = PVector(1500/2 , 2000 - 200)
    root = Branch(a, b)
    tree.append(root)
    
def draw():
    background(0)
    for i in range(len(tree)):
        tree[i].show()
        tree[i].jitter()
        
    for i in range(len(leaves)):
        fill(255, 0, 100)
        noStroke()
        ellipse(leaves[i].x, leaves[i].y, 10, 4)
        leaves[i].y += random(0, 1)
    
def mousePressed():
    for i in range(len(tree), 0, -1): 
        if tree[i - 1].finished != True:
            tree.append(tree[i - 1].branch_right())
            tree.append(tree[i - 1].branch_left())
        tree[i - 1].finished = True
    global count
    count += 1
    
    if count == 6:
        for i in range(len(tree)):
            if tree[i].finished != True:
                leaf = tree[i].end.copy()
                leaves.append(leaf)
                
                
                
                
                
                
