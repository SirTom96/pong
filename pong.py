#Ping pong

import turtle

#Descrizione della finestra
wn = turtle.Screen()
wn.title("Classic Pong by @Tom")
wn.bgcolor("black")
#Il centro è (0,0)
wn.setup(width=800, height=600)
#tracer migliora l'esperienza di gioco rendendola più veloce.
wn.tracer(0)

#punteggio
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Giocatore A: 0  Giocatore B: 0", align="center", font=("Courier", 20, "normal"))

#Aggiornamento punteggio
score_a = 0
score_b = 0

#Pad_a
paddle_a=turtle.Turtle()
#velocità delle animazioni(max)
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
#stretch_wid=5 moltiplica *5 la larghezza originale(20px *5)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#penup non fa disegnare nessuna riga quando turtle si muove
paddle_a.penup()
paddle_a.goto(-350, 0)

#Pad_b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#movimento palla (dx =delta x)
ball.dx = 0.15
ball.dy = 0.15

#Far muovere la palla - funzioni
def paddle_a_up():
    #prendo la coordinata y del pad
    y = paddle_a.ycor()
    #lo traslo di 20px verso l'alto
    y += 20
    #aggiorno y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard input
#rende la finestra sensibile agli input
wn.listen()
#all'input w chiama paddle_a_up
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Loop di gioco
while True:
    #Ogni volta che il loop itera lo schermo si aggiorna
    wn.update()
    #Movimento palla (inizia in 0,0 al primo loop, poi aggiunge 2)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Funzioni ai bordi
    #se la palla tocca il bordo alto
    if ball.ycor() > 290:
        #reimposto la coordinata y a 290
        ball.sety(290)
        #inverto la velocità (dy = deltay, invertito con *-1)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        #Se la palla va oltre il bordo riportala al centro e inverti la direzione
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Giocatore A: {}  Giocatore B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Giocatore A: {}  Giocatore B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    #rimbalzo
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
