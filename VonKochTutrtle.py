import turtle as t

#String constants defining the process occurring
inst = "AggAggA"
replacing = "AgAddAAgA"

#Numerical constants
l = 1
#l is the length of a line
alpha = 90
#alpha is the angle of rotation
n = 9
#n is the number of iterations

#Calculation constants
i=0
index = []

#Used to have scrolling bars
t.screensize(10000,10000)

#Used to change the speed of drawing (smaller <=> faster)
t.delay(0)
t.speed(0)

#Moving the turtle to another starting point (have to be adjsted depending on what you are doing)
t.pu() #Pen Up
t.setpos(-100,0)
t.pd() #Pen Down

#Cosmetic
t.color('red','yellow')
#t.begin_fill()

#Creating the instruction string
while i<n:
    index=inst.split('A') #Split the string in an array (removing the 'A')
    inst = replacing.join(index) #Join the previous array by adding the replacing string (defined above)
    i+=1

#Filling the blanks with A
inst= "A".join(index)

#Executing the instructions
# A = going forward by length l
# g = turning left by angle alpha (in degrees)
# d = turning right by angle alpha (in degrees)
for letter in inst:
    if letter == 'A':
        t.forward(l)
    elif letter == 'g':
        t.left(alpha)
    elif letter == 'd':
        t.right(alpha)

#t.end_fill()
