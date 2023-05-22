import turtle

pluma = turtle.Turtle()
turtle.Screen().bgcolor("#001F3F")

# Dibujo del corazón grande (rojo)
pluma.begin_fill()
pluma.fillcolor("red")
pluma.left(45)
pluma.forward(150)
pluma.circle(75, 180)
pluma.right(90)
pluma.circle(75, 180)
pluma.forward(150)
pluma.end_fill()
pluma.speed(15)

# Calcula las coordenadas para centrar el corazón negro
x = pluma.xcor()
y = pluma.ycor() - 75

# Espacio entre corazones
pluma.penup()
pluma.goto(x + 75, y)  # Ajusta la posición del segundo corazón
pluma.pendown()

# Dibujo del corazón pequeño (negro, mitad del tamaño)
pluma.begin_fill()
pluma.fillcolor("black")
pluma.left(45)
pluma.forward(75)  # Ajusta el tamaño del corazón pequeño
pluma.circle(37.5, 180)
pluma.right(90)
pluma.circle(37.5, 180)
pluma.forward(75)  # Ajusta el tamaño del corazón pequeño
pluma.end_fill()


# Dibujo de la estrella
pluma.penup()
pluma.goto(-250, -200)  # Ajusta la posición de la estrella
pluma.pendown()

for i in range(0, 52):
    pluma.forward(-195)
    pluma.left(205.90)
    pluma.speed(18)

pluma.end_fill()
pluma.hideturtle()

#SEGUNDA ESTRELLA
pluma.penup()
pluma.goto(-210, -130)  # Ajusta la posición de la estrella
pluma.pendown()
pluma.pencolor("green")


for i in range(0, 52):
    pluma.forward(-195)
    pluma.left(205.90)
    pluma.speed(22)

pluma.end_fill()
pluma.hideturtle()

#TERCERA ESTRELLA

pluma = turtle.Turtle()
pluma.penup()
pluma.goto(-195, 50)  # Ajusta la posición de la estrella a la mitad
pluma.pendown()
pluma.pencolor("white")


pluma.end_fill()
pluma.hideturtle()

for i in range(0, 40):
    pluma.forward(-97.5)  # Longitud reducida a la mitad
    pluma.left(205.90)
    pluma.speed(22)

#CUARTA ESTRELLA

pluma = turtle.Turtle()
pluma.penup()
pluma.goto(-165, 190)  # Ajusta la posición de la estrella a la mitad
pluma.pendown()

for i in range(0, 40):
    pluma.forward(-97.5)  # Longitud reducida a la mitad
    pluma.left(205.90)
    pluma.speed(18)

#QUINTA ESTRELLA

pluma = turtle.Turtle()
pluma.penup()
pluma.goto(245, 120)  # Ajusta la posición de la estrella a la mitad
pluma.pendown()

for i in range(0, 40):
    pluma.forward(-97.5)  # Longitud reducida a la mitad
    pluma.left(205.90)
    pluma.speed(18)

#ESTRELLA SEIS
pluma = turtle.Turtle()
pluma.penup()
pluma.goto(265, 255)  # Ajusta las coordenadas (x, y) para la posición deseada de la estrella

pluma.fillcolor("yellow")
pluma.begin_fill()
pluma.hideturtle()

for _ in range(5):
    pluma.forward(50)  # Ajusta la longitud de los lados de la estrella
    pluma.right(144)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()

#ESTRELLA SIETE
pluma = turtle.Turtle()
pluma.penup()
pluma.goto(205, 220)  # Ajusta las coordenadas (x, y) para la posición deseada de la estrella

pluma.fillcolor("yellow")
pluma.begin_fill()

for _ in range(5):
    pluma.forward(50)  # Ajusta la longitud de los lados de la estrella
    pluma.right(144)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()

#ESTRELLA OCHO
pluma = turtle.Turtle()
pluma.penup()
pluma.goto(175, 265)  # Ajusta las coordenadas (x, y) para la posición deseada de la estrella

pluma.fillcolor("yellow")
pluma.begin_fill()

for _ in range(5):
    pluma.forward(50)  # Ajusta la longitud de los lados de la estrella
    pluma.right(144)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()


#ESTRELLA NUEVE
pluma = turtle.Turtle()
pluma.penup()
pluma.goto(-105, 26)  # Ajusta las coordenadas (x, y) para la posición deseada de la estrella

pluma.fillcolor("yellow")
pluma.begin_fill()

for _ in range(5):
    pluma.forward(50)  # Ajusta la longitud de los lados de la estrella
    pluma.right(144)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()


#ESTRELLA DIEZ
pluma = turtle.Turtle()
pluma.penup()
pluma.goto(-80, 56)  # Ajusta las coordenadas (x, y) para la posición deseada de la estrella

pluma.fillcolor("purple") 
pluma.begin_fill()

for _ in range(5):
    pluma.forward(50)  # Ajusta la longitud de los lados de la estrella
    pluma.right(144)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()


import turtle

# Primera figura
pluma = turtle.Turtle()
pluma.speed(19)
pluma.penup()
pluma.goto(180, -135)
pluma.pencolor("cyan")
pluma.begin_fill()

for _ in range(50):
    pluma.pendown()
    pluma.forward(120)
    pluma.right(170)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()

# Segunda figura (mitad del tamaño)
pluma.penup()
pluma.goto(290, -240)  # Ajusta la posición de la segunda figura
pluma.pendown()
pluma.begin_fill()

for _ in range(50):
    pluma.pendown()
    pluma.forward(80)  # Ajusta el tamaño de la segunda figura
    pluma.right(170)
    pluma.speed(15)

pluma.end_fill()
pluma.hideturtle()

turtle.done()


# Centrar la pantalla
turtle.Screen().tracer(0)
pluma.penup()
pluma.goto(0, 0)
pluma.pendown()
turtle.Screen().update()

turtle.done()
