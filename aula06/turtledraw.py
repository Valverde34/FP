import turtle

t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
with open("drawing.txt") as f:
    for line in f:
        if line == "UP\n":
            t.up()
        elif line == "DOWN\n":
            t.down()
        else:
            x, y = line.split()
            t.goto(int(x), int(y))

    # wait
turtle.Screen().exitonclick()