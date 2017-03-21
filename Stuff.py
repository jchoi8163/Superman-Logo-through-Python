def polygonR(t,sides,distance):
    angle = 360/sides
    for times in range(sides):
        t.forward(distance)
        t.right(angle)


def polygonL(t,sides,distance):
    angle = 360/sides
    for times in range(sides):
        t.forward(distance)
        t.left(angle)

        
def cool(t,C,d):
    t.color(C)
    polygon(t,4,d)
    t.color('red')
    polygon(t,3,d)
    t.right(90)


def CS (t,d):
    for times in range(4):
        cool(t,C,d)
        t.right(90)

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()



def star(t,d):

    for times in range(8):
        t.forward(d)
        t.left(135)

    


def stars(t,d,c):
    for n in range(8):
        star(t,n*9,c)
        t.left(40)
        t.penup()
        t.forward(50)
        t.pendown()

def funky(t):
    t.color('red')
    polygon(t,3,100)
    t.color('blue')
    polygon(t,3,50)


def box(t,d,c,ds):
    t.begin_fill()
    for times in range(2):
        t.color(c)
        t.forward(d)
        t.right(90)
        t.forward(ds)
        t.right(90)
    t.end_fill()
