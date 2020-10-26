# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 01:45:46 2020

@author: BICHA
"""

import turtle as t
import random as rd



t.bgcolor('green')

snake = t.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()


fruit=t.Turtle()
fshape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
snake = t.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()


t.register_shape('fruit',fshape)
fruit.shape('fruit')
fruit.color('red')
fruit.penup()
fruit.hideturtle()
fruit.speed()



gamestarted=False
text=t.Turtle()
text.write('Press SPACE to start',align='center',font=('Arial',16,'bold'))
text.hideturtle()

score=t.Turtle()
score.hideturtle()
score.speed(0)

def outwind():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y)=snake.pos()
    outside=x < left_wall or x > right_wall or y > top_wall or y<bottom_wall
    return outside
    
def placefruit():
    fruit.hideturtle()
    fruit.setx(rd.randint(-200,200))
    fruit.sety(rd.randint(-200, 200))
    fruit.showturtle()
    
def gameover():
    snake.color('green')
    fruit.color('green')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))
                         

def displayscore(currscore):
    score.clear()
    score.penup()
    x= (t.window_width()/2)-50
    y= (t.window_height()/2) - 50
    score.setpos(x,y)
    score.write(str(currscore) , align = 'right',font=('Arial',40,'bold'))
    
    
def startgame():
    global gamestarted
    if gamestarted:
        return
    gamestarted = True
    sc=0
    text.clear()
    snakespeed=2
    snakelen = 3
    snake.shapesize(1,snakelen,1)
    snake.showturtle()
    displayscore(sc)
    placefruit()
    
    while True:
        snake.forward(snakespeed)
        if snake.distance(fruit)<20:
            placefruit()
            snakelen=snakelen + 1
            snake.shapesize(1,snakelen,1)
            snakespeed=snakespeed + 1
            sc= sc + 10
            displayscore(sc)
        if outwind():
            gameover()
            break
        
def moveup():
    if snake.heading()==0 or snake.heading()==180:
        snake.setheading(90)
        
def movedown():
    if snake.heading()==0 or snake.heading()==180:
        snake.setheading(270)
        
def moveleft():
    if snake.heading()==90 or snake.heading()==270:
        snake.setheading(180)
        
def moveright():
    if snake.heading()==90 or snake.heading()==270:
        snake.setheading(0)
        
    
t.onkey(startgame,'space')
t.onkey(moveup,'Up')
t.onkey(movedown,'Down')
t.onkey(moveleft,'Left')
t.onkey(moveright,'Right')

t.listen()
t.mainloop()

