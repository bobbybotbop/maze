import turtle

window = turtle.Screen()

borders = turtle.Turtle()
borders.hideturtle()
borders.penup()
borders.speed(0)

bob = turtle.Turtle()
bob.shape("turtle")
bob.penup()
bob.goto(-240,-240)
bob.setheading(90)
bob.color("navy")

bob2 = turtle.Turtle()
bob2.shape("turtle")
bob2.penup()
bob2.goto(200,230)
bob2.setheading(90)
bob2.color("red")

obstacle1 = turtle.Turtle()
obstacle1.shape("circle")
obstacle1.penup()
obstacle1.goto(-140,-40)
obstacle1.setheading(270)
obstacle1.color("red")

anotherone = turtle.Turtle()
anotherone.shape("square")
anotherone.penup()
anotherone.goto(0,-200)
anotherone.setheading(270)
anotherone.color("red")

anotherone2 = turtle.Turtle()
anotherone2.shape("square")
anotherone2.penup()
anotherone2.goto(0,-0)
anotherone2.setheading(270)
anotherone2.color("red")

move_speed = 10
turn_speed = 10

def forward():
  bob.forward(move_speed)
def backward():
  bob.backward(move_speed)
def right():
  bob.right(turn_speed)
def left():
  bob.left(turn_speed)


def up():
  bob2.forward(move_speed)
def down():
  bob2.backward(move_speed)
def rt():
  bob2.right(turn_speed)
def lt():
  bob2.left(turn_speed)


def rectangle(x,y,length,width,color):
  borders.goto(x,y)
  borders.color(color)
  borders.pendown()
  borders.begin_fill()
  for x in range(2):
    borders.forward(length)
    borders.right(90)
    borders.forward(width)
    borders.right(90)
  borders.end_fill()
  borders.penup()

# Outside Wall
rectangle(-300,250,20,500,"black")
rectangle(-300,250,450,20,"black")
rectangle(250,250,20,500,"black")
rectangle(-200,-230,450,20,"black")

#Inside Wall
rectangle(-300,-160,50,20,"black")
rectangle(-200,-100,20,130,"black")
rectangle(-300,0,200,20,"black")
rectangle(-100,0,20,140,"black")
rectangle(-80,-120,200,20,"black")
rectangle(100,-20,150,20,"black")
rectangle(100,60,20,80,"black")
rectangle(-100,60,200,20,"black")


#Moves the Turtle
window.onkey(forward,"Up")
window.onkey(backward,"Down")
window.onkey(left,"Left")
window.onkey(right,"Right")

window.onkey(up,"w")
window.onkey(down,"s")
window.onkey(lt,"a")
window.onkey(rt,"d")

window.listen()

#Controls Animations and Boundaries
while(True):
  obstacle1.forward(5)


  if obstacle1.ycor() == -210:
    obstacle1.setheading(90)
  elif obstacle1.ycor() == -40:
    obstacle1.setheading(270)

  if anotherone.xcor() ==  0:
      anotherone.setheading(180)
      anotherone.forward(50)
  elif anotherone.xcor() == -50:
      anotherone.setheading(360)
      anotherone.forward(50)

  if anotherone2.xcor() ==  0:
      anotherone2.setheading(180)
      anotherone2.forward(50)
  elif anotherone2.xcor() == -50:
      anotherone2.setheading(360)
      anotherone2.forward(50)

  if bob.distance(obstacle1) < 20:
    bob.goto(-240,-240) 
    bob.setheading(90)

  
  if bob2.distance(obstacle1) < 20:
    bob2.goto(200,230) 
    bob2.setheading(0)

    
  if bob.distance(anotherone) < 20:
    bob.goto(-240,-240) 
    bob.setheading(90)

    
  if bob2.distance(anotherone) < 20:
    bob2.goto(200,230) 
    bob2.setheading(0)

  if bob.distance(anotherone2) < 20:
    bob.goto(-240,-240) 
    bob.setheading(90)

    
  if bob2.distance(anotherone2) < 20:
    bob2.goto(200,230) 
    bob2.setheading(0)
