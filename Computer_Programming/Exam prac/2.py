import turtle
print("Welcome to turtle world")
while True:
    x = input("turtle |>")
    if x == "fd" or x == "back" or x == "lt" or x == "rt":
        lenght = int(input("Please input its argrument: "))
        if x == "fd":
            turtle.forward(lenght)
        elif x =="back":
            turtle.backward(lenght)
        elif x == "lt":
            turtle.left(lenght)
        else:
            turtle.right(lenght)
    elif x == "pu":
        turtle.penup()
    elif x == "pd":
        turtle.pendown()
    elif x == "reset":
        turtle.reset()
    elif x == "quit":
        break
    else:
        print("Wrong command: ")