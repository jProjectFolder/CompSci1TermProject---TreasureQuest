#**********************  10/22/2019.py  *********************
#
# Name: Jason Haldiman
#
# Course: CSCI 1470
#
# Assignment: Homework #7
#
# Algorithm:
#   Draw a square with a turtle that represents the set boundaries for searching
#   Display text descibing game and how to play.
#   Pop up turtle input box and ask if user wants to play
#   If user types yes, begin the game. If no, close the window.
#   If the game begins, randomly place the invisible treasure and randomly place the player's turtle
#   Allow the player to move with arrowkeys that correspond to functions.
#   As the player moves forward,
#       If the player is is not within range of treasure or border, take next key input.
#       If the turtle is within 30 pixels of the x or y plane from the treasure, display victory image, end game.
#       If the player crosses the boundary, stop the player and turn them around and move them back in the borders and take next key input
#       
#   ...
#**********************************************************





import turtle
import random
import math


moveMent = 3
def up():
    
    """Moves jill forward 20 pixels until jill's position is within 30 pixels ofthe treasure. Than it displays
        the victory image"""

    global moveMent #You have to just name the variable by itself as a global variable 

    #Victory Pop Up
    jill.forward(20)
    d = math.sqrt(math.pow(jill.xcor() - treasure.xcor(),2) + math.pow(jill.ycor() - treasure.ycor(),2))
    if d < 30:
        treasure.hideturtle()
        wn.clear()
        wn.bgcolor('black')
        wn.bgpic("52213-1-1395172721treasureCoins.png")
        
        wn.update()
    #Adding Border bounds 
    if not -x_size/2 < jill.xcor() < x_size/2  or not -y_size/2 < jill.ycor() < y_size/2 :
        jill.undo()
        jill.left(180)
        jill.forward(25)

    #Adding Movement limit
    moveMent = moveMent - 1
    if moveMent == 0:
        print("your movement is zero")
        moveMent = moveMent + 3
        

def left():
   jill.left(45)

def right():
   jill.right(45)

def Quit():
    wn.bye()
    
#Windor Screen Size
x_size = 500
y_size = 500
wn = turtle.Screen()
turtle.setup(x_size+50,y_size+50)
wn.bgcolor('black')
wn.title("Treasure Quest 500")

#border turtle
border = turtle.Turtle('turtle')
border.color('white')
border.speed(10)
border.penup()
border.setpos((- x_size)/2,(- y_size)/2)
border.pendown()
for i in range (4):
    border.forward(x_size)
    border.left(90)
border.hideturtle()

# Writing Turtle
write = turtle.Turtle()
write.color('lightblue')
style = ('Courier',12,'bold')
write.write("Hello. This is a treasure searching game.",font = style,align = 'center')
write.pu()
write.hideturtle()
write.goto(0,-20)
write.write("Your mission, should you choose to accept it,",font = style, align = 'center')
write.goto(0,-40)
write.write("is to find the treasure by using the arrow keys.",font = style, align = 'center')
write.goto(0,-60)
write.write("""""",font =("Courier",8,'bold'),align = 'center')

#Choose to play or not
play_or_not = wn.textinput("CHOOSE", "Do you accept the mission? y \ n")
if play_or_not == 'y':
    write.clear()
elif play_or_not == 'n':
    write.clear()
    write.write("You have declined the mission.",font = style, align = 'center')
    wn.bye()
    
#Hunting Turtle jill
jill = turtle.Turtle("arrow")
jill.color('white')
jill.pencolor('grey')
jill.pensize(30)
jill.speed(10)
jill.turtlesize(2)
jill.pu()
jill.setpos(random.randint(-250,250),random.randint(-250,250))
jill.pd()

#Treasure Turtle treasure
treasure = turtle.Turtle('square')
treasure.color('gold')
treasure.turtlesize(1)
treasure.speed(10)
treasure.hideturtle()
treasure.pu()
treasure.setpos(random.randint(-250,250),random.randint(-250,250))
treasure.pd()


#key commands that access functions for movement of jill
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(Quit, "q")

wn.listen()
wn.mainloop()
