axiom = 'F'
sentence = axiom
length_line = 250
rules = []
rules.append({ 'a': 'F', 'b': 'FF+[+F-F-F]-[-F+F+F]'})

def generate():
    global sentence
    global rules
    global length_line
    nextsentence = ''
    length_line *= 0.56
    for i in range(len(sentence)):
        current = sentence[i]
        found = False
        print(len(rules))
        for j in range(len(rules)):
            if current == rules[j]['a']:
                found = True
                nextsentence += rules[j]['b']
                break
        if found != True:
            nextsentence += current
    sentence = nextsentence 
    turtle() 

def turtle():#turtle graphics instruct a turtle to move around the screen
    background(255, 255, 0)
    resetMatrix()
    stroke(0, 0, 255, 90)
    translate(width/2, height)
    for char in sentence:
        if char == 'F':
            line(0, 0, 0, -length_line)
            translate(0, -length_line)
        elif char == '+':
            rotate(25 * PI/180)
        elif char == '-':
            rotate(-25 * PI/180)
        elif char == '[':
            pushMatrix()
        elif char == ']':
            popMatrix()

def setup():
    size(3000, 2000)
    background(0)
    turtle()

def draw():
    pass

def mousePressed():
    generate()
