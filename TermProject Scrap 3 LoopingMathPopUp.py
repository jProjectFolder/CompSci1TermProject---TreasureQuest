#**********************  10/22/2019.py  *********************
#
# Name: Jason Haldiman
#
# Course: CSCI 1470
#
# Assignment: Term Project: Turtles Math Game
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
import time




##MATH FUNCITONS##
moveMent = 0
A1 = 0
# ADD



        





def addition_(many_questions):
    """
    Creates two random number and adds them together. Asks user what those
    random numbers added together equal and counts how many times user is correct.
    """
    global A1
    global moveMent
    correct1 = 0
    wrong1 = 0
    for i in range(many_questions):
        randomNum1 = random.randint(1,20) 
        randomNum2 = random.randint(1,20)
        #print (num1, "+", num2,"=")
        A1 = randomNum1+randomNum2
        print(A1)
        guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'+', randomNum2), None , 0 , 100 )
        print("Your guess is", guess1)
        ##Having two if statement allows the program to add axtra points if the geuss is correct the first time, which is cool
        #First if statement gives extra movement if first guess is correct.
        if guess1 == A1:
            moveMent = moveMent + 3 
        if guess1 == A1:
                correct1 += 1
                moveMent = moveMent + 3 
        else :
            while guess1 != A1:
                wrong1 += 1
                guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'+', randomNum2), None , 0 , 100 )
                print("the answer is",A1)
                if guess1 == A1:
                        moveMent = moveMent + 3 



## SUB

def subtraction_(many_questions):
    """
    Creates two random number and subtracts the first from second. Asks user what those
    random numbers equal and counts how many times user is correct.
    """
    global A1
    global moveMent
    correct1 = 0
    wrong1 = 0
    for i in range(many_questions):
        randomNum1 =random.randint(1,20)
        randomNum2 =random.randint(1,20)
        A1 = randomNum1-randomNum2
        print(A1)
        guess1 = iguess1 = wn.numinput("Math Question",  ("What is",randomNum1,'-', randomNum2), None , -100 , 100 )
        print("Your guess is", guess1)
        if guess1 == A1:
            moveMent = moveMent + 3 
        if guess1 == A1:
                correct1 += 1
                moveMent = moveMent + 3 
        else :
            while guess1 != A1:
                wrong1 += 1
                guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'-', randomNum2), None , -100 , 100 )
                print("the answer is",A1)
                if guess1 == A1:
                        moveMent = moveMent + 3 


    
    
### MULTI

def multiplication_(many_questions):
    """
    Creates two random number and multiplies them together. Asks user what those
    random numbers multiplied together equal and counts how many times user is correct.
    """
    global A1
    global moveMent
    correct1 = 0
    wrong1 = 0
    for i in range(many_questions):                                                    
        randomNum1 =random.randint(1,20)         
        randomNum2 =random.randint(1,20)        
        guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'*', randomNum2), None , 0 , 400 )
        A1 = randomNum1*randomNum2
        print(A1)
        print("Your guess is", guess1)
        if guess1 == A1:
            moveMent = moveMent + 3 
        if guess1 == A1:
                correct1 += 1
                moveMent = moveMent + 3 
        else :
            while guess1 != A1:
                wrong1 += 1
                guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'*', randomNum2), None , 0 , 400 )
                print("the answer is",A1)
                if guess1 == A1:
                        moveMent = moveMent + 3



        
#### DIVISION

def division_(many_questions):
    """
    Creates two random number and divides the first by second. The answer is rounded
    down to the nearest whole number. Asks user what those random numbers divided
    are equal to and counts how many times user is correct.
    """
    global A1
    global moveMent
    correct1 = 0
    wrong1 = 0
    for i in range(many_questions):
        randomNum1 =random.randint(1,20) 
        randomNum2 =random.randint(1,20)        
        print ("Floor division of",randomNum1, "//", randomNum2,"=")
        A1 = round( randomNum1/randomNum2, 2)
        print(A1)
        guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'/', randomNum2, "rounded to two decimal places?"), None , 0 , 100 )
        if guess1 == A1:
            moveMent = moveMent + 3 
        if guess1 == A1:
                correct1 += 1
                moveMent = moveMent + 3 
        else :
            while guess1 != A1:
                wrong1 += 1
                guess1 = wn.numinput("Math Question",  ("What is",randomNum1,'/', randomNum2, "rounded to two decimal places?"), None , 0 , 100 )
                print("the answer is",A1)
                if guess1 == A1:
                        moveMent = moveMent + 3









#############################TURTLE PROGRAM#############################3


moveMent = 3
def up():
    
    """Moves jill forward 20 pixels until jill's position is within 30 pixels ofthe treasure. Than it displays
        the victory image"""

    global moveMent #You have to just name the variable by itself as a global variable 
    print(moveMent)

    #Jill Move Forward
    jill.forward(20)

    #Victory Pop Up    
    d = math.sqrt(math.pow(jill.xcor() - treasure.xcor(),2) + math.pow(jill.ycor() - treasure.ycor(),2))
    if d < 30:
        treasure.hideturtle()
        wn.clear()
        wn.bgcolor('black')
        wn.bgpic("TreasureCoinsPicture.png")
        wn.update()
        
    #Adding Border bounds 
    if not -x_size/2 < jill.xcor() < x_size/2  or not -y_size/2 < jill.ycor() < y_size/2 :
        jill.undo()
        jill.left(180)
        jill.forward(25)
        
#Adding Movement limit with pop up question  from functions
    moveMent = moveMent - 1
    guess1 = mathProblem = 0
    if moveMent == 0:
        mathProblem = random.randint(4,4) # 4,4 call ony division problem, but i discovered its not working in SCRAP 5
                                #SO i wil fix here where its less complicated.

                                #COMING BACK. i just forgot to change the "if statement" variable to "mathProblem" instead of "random"
                                                                                        #BECUASE the mathProblem is the random :P
        print("Is chosen math problem type",mathProblem)
        if mathProblem == 1:
            addition_(1)
        elif mathProblem == 2:
           subtraction_(1)
        elif mathProblem == 3:
            multiplication_(1)
        elif mathProblem == 4:
            division_(1)
        print(A1)
                    
    # MonteCristo counter
    MonteCristo.clear()
    MonteCristo.write(moveMent, font = ('Courier',15,'bold'))
    wn.listen()
    


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
turtle.setup(x_size+200,y_size+200)
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

# Intro Title Writing Turtle
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
#play_or_not = wn.textinput("CHOOSE", "Do you accept the mission? y \ n")
#if play_or_not == 'y':
 #   write.clear()
#elif play_or_not == 'n':
 #   write.clear()
 #   #I needed the import tme module to get the delay stuff.
 #   write.write("You have declined the mission.",font = style, align = 'center')
 #   wn.bye()
    
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
#treasure.hideturtle()
treasure.pu()
treasure.setpos(random.randint(-250,250),random.randint(-250,250))
treasure.pd()


#Counting Turtle MonteCristo
MonteCristo = turtle.Turtle()
MonteCristo.color('blue')
MonteCristo.pu()
MonteCristo.setpos((x_size+150)/2,(y_size+150)/2)
MonteCristo.pd()
MonteCristo.write(moveMent, font = ('Courier',15,'bold'))
MonteCristo.hideturtle()

#key commands that access functions for movement of jill
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(Quit, "q")


wn.listen()
wn.mainloop()
