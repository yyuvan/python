import turtle

turtle.Screen().bgcolor("Orange")

sc=turtle.Screen()
sc.setup(400,300)
board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.right(90)