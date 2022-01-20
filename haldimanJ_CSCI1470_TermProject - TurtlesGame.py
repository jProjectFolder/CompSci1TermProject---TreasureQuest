#**********************  10/24/2019.py  *********************
#
# Name: Jason Haldiman
#
# Course: CSCI 1470
#
# Assignment: Term Project: Turtles Math Game
#
# Algorithm:
#   Call up turtle screen set to a certain size and 
#   Display text descibing game and how to play.
#       if yes 'y' continue to game
#       if no 'n' close the turtle screen
#   Call up a pop-up box that asks player to input level amount
#   Once level amount input received,
#        Draw boundary square (with boundary coding serperate), display hunting turtle in random location, hide treasure randomly,
        #allow the hunting turtle to be movable by key commands, show how many moves remain in corner with drawing turtle.
#   As the player moves forward,
#       If the player is is not within range of treasure or border, take next key input.
#       If the turtle is within 30 pixels of the x or y plane from the treasure, display victory image, clear screen, randomly drop turtles again
        #and begin next level unti all levels from 'level amount' are completed.
#       If the player crosses the boundary, stop the player and turn them around and move them back in the borders and take next key input
#       If the player answeres correctly, the question box disppears and more movement is added
#       Else, the player gets a new randomly generated math question and loses one of his\her three lives       
#   Once all the treasures are found (no more levels), some the scores are DISPLAYED until player exits with a click command.
#       A score of total movements 
#       A score of correct answers 
#       A score for wrong answers
#   ...
#**********************************************************



import turtle
import random
import math
import time
#######################MATH FUNCITONS#####################

#Some Extra assigned global variables
moveMent = 0
A1 = 0
wrong1 = 0
correct1 = 0
moveScore = 0
numLevels = 0




# ADD
def addition_(many_questions):
    """
    Creates randomly generated number and adds them together. Pops up int textbox and asks
    user to input correct answer. if user guesses correct first time, they get movement, otherwise
    it repeats the question until the answer is correct. Counts how many correct and wrong answers
    """
    global A1
    global moveMent
    global correct1
    global wrong1
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
    Creates randomly generated number and subtracts the first from second. Pops up int textbox and asks
    user to input correct answer. if user guesses correct first time, they get movement, otherwise
    it repeats the question until the answer is correct. Counts how many correct and wrong answers
    """
    global A1
    global moveMent
    global correct1
    global wrong1
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
    Creates randomly generated number and multiplies them together. Pops up int textbox and asks
    user to input correct answer. if user guesses correct first time, they get movement, otherwise
    it repeats the question until the answer is correct. Counts how many correct and wrong answers.
    """
    global A1
    global moveMent
    global correct1
    global wrong1
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
    down to the 2nd decimal place. Asks user what those random numbers divided
    are equal to and counts how many times user is correct or wrong. If correct the first time
    the user gets more movement.
    """
    global A1
    global moveMent
    global correct1
    global wrong1
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



###MOVEMENT FUCNTION###
def up():
    
    """This is where the majority of the program occurs based on the forward movement of jill.
    1. moves jill forward 20 pixels onkey(up) command.
    2.decreseases moement by 1 and checks if the movement is zero and if it is zero, calls a random
        math question
    3. Creates border boundary to turn turtle around
    4. Checks if turtle within distance of treasure turtle and displays victory image than resets new level
    5. Print score when number of levels is zero
    """
    global jill
    global treasure
    global MonteCristo
    global wn
    global x_size
    global y_size
    global numLevels
    global moveScore
    global moveMent #You have to just name the variable by itself as a global variable 
    
    #Jill Move Forward
    jill.forward(20)
    moveScore +=1
    print(numLevels)

    #Adding Movement limit with pop up question  from functions and taking away level counter
    moveMent = moveMent - 1
    guess1 = mathProblem = 0
    #Calling Math Equations
    if moveMent == 0:
        mathProblem = random.randint(1,4) ####NEXT STET IS FIXING THE DIVISION> IT DOES INFINTY STEPS WITH 1,4, INSTEAD OF 1,3
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
        print(correct1, "Correct answers so far")
        print(wrong1, "Wrong answers so far")
                    
    # MonteCristo counter
    MonteCristo.clear()
    MonteCristo.write(moveMent, font = ('Courier',15,'bold'))
    wn.listen()

    #Adding Boundary at border line 
    if not -x_size/2 < jill.xcor() < x_size/2  or not -y_size/2 < jill.ycor() < y_size/2 :
        print("new Level Boundary is go")
        jill.undo()
        jill.left(180)
        jill.forward(25)


    #Victory Pop Up and clearing new level  
    d = math.sqrt(math.pow(jill.xcor() - treasure.xcor(),2) + math.pow(jill.ycor() - treasure.ycor(),2))
    if d < 30:
        print("This is numLevels print 2", numLevels)
        treasure.hideturtle()
        wn.clear()
        wn.bgcolor('black')
        wn.bgpic("TreasureCoinsPicture.png")
        wn.update()
        time.sleep(1.5) #pauses python for 3 whole seconds (3000 milliseconds)
        wn.clear()
        #END LEVEL AND PRINT SCORES
        if numLevels <= 0:
            wn.bgcolor('black')
            write.write("You have found all the treasaures.",font = style, align = 'center')
            time.sleep(3)
            write.goto(0,-20)
            write.write("Mission Accomplished.",font = style, align = 'center')
            time.sleep(2)
            write.goto(0,80)
            write.write(("Correct answers:", correct1), font = style, align = 'right')
            write.goto(0,60)
            write.write(("Wrong answers:",  wrong1), font = style, align = 'right')
            write.goto(0,40)
            write.write(("Total Movements:",  moveScore), font = style, align = 'right')
            write.goto(0,120)
            write.write("Click to exit" , font = style, align = 'center')
            wn.exitonclick()

        ###REMAKES NEW LEVEL after treasure is found###
        wn.bgcolor('black')
                #   Hunting Turtle jill
        jill = turtle.Turtle("arrow")
        jill.color('white')
        jill.pencolor('grey')
        jill.pensize(30)
        jill.speed(10)
        jill.turtlesize(2)
        jill.pu()
        jill.setpos(random.randint(-250,250),random.randint(-250,250))
        jill.pd()
        #   Border turtle
        global border
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
        print("new border line complete")
        #   Treasure Turtle treasure
        treasure = turtle.Turtle('square')
        treasure.color('gold')
        treasure.turtlesize(1)
        treasure.speed(10)
        #treasure.hideturtle()
        treasure.pu()
        treasure.setpos(random.randint(-250,250),random.randint(-250,250))
        treasure.pd()
        print("New treasure complete")
        #   NEW Level Starting Movement
        moveMent = 5
        #   Counting Turtle MonteCristo
        MonteCristo = turtle.Turtle()
        MonteCristo.color('blue')
        MonteCristo.pu()
        MonteCristo.setpos((x_size+150)/2,(y_size+150)/2)
        MonteCristo.pd()
        MonteCristo.write(moveMent, font = ('Courier',15,'bold'))
        MonteCristo.hideturtle()
        print("New counter complete")
        print(moveMent)
        wn.onkey(up, "Up")
        wn.onkey(left, "Left")
        wn.onkey(right, "Right")
        wn.onkey(Quit, "q")
        
        numLevels = numLevels - 1

    wn.listen()

        

    
def left():
   jill.left(45)
def right():
   jill.right(45)
def Quit():
    wn.bye()
#   Windor Screen Size
x_size = 500
y_size = 500
wn = turtle.Screen()
turtle.setup(x_size+200,y_size+200)
wn.bgcolor('black')
wn.title("Treasure Quest 500")

#   Intro Title Writing Turtle
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
time.sleep(1)
write.clear()
#Choose to play or not and how many LEVELS
global numLevel
play_or_not = wn.textinput("CHOOSE", "Do you accept the mission? y \ n")
if play_or_not == 'y':
    write.clear()
    numLevels = wn.numinput("Lvl","How many levels do you want to search?", None , 1, 10) -1
elif play_or_not == 'n':
    write.clear()
    write.write("You have declined the mission.",font = style, align = 'center')
    time.sleep(1)
    wn.bye()

    
#   Hunting Turtle jill
jill = turtle.Turtle("arrow")
jill.color('white')
jill.pencolor('grey')
jill.pensize(30)
jill.speed(10)
jill.turtlesize(2)
jill.pu()
jill.setpos(random.randint(-250,250),random.randint(-250,250))
jill.pd()
#   Border turtle
global border
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
#   Treasure Turtle treasure
treasure = turtle.Turtle('square')
treasure.color('gold')
treasure.turtlesize(1)
treasure.speed(10)
#treasure.hideturtle()
treasure.pu()
treasure.setpos(random.randint(-250,250),random.randint(-250,250))
treasure.pd()
#   Starting Movement
moveMent = 5
#   Counting Turtle MonteCristo
MonteCristo = turtle.Turtle()
MonteCristo.color('blue')
MonteCristo.pu()
MonteCristo.setpos((x_size+140)/2,(y_size+140)/2)
MonteCristo.pd()
MonteCristo.write(moveMent, font = ('Courier',15,'bold'))
MonteCristo.hideturtle()
#   Key commands that access functions for movement of jill
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(Quit, "q")

#   End Mainloop
wn.listen()
wn.mainloop()

