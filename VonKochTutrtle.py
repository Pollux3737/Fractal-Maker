import turtle as t

inst = "AggAggA"

l = 1
alpha = 90
n = 9


i=0
index = []

t.screensize(10000,10000)

t.delay(0)
t.pu()
t.setpos(-100,0)
t.pd()

t.color('red','yellow')
#t.begin_fill()
t.speed(0)

while i<n:
    index=inst.split('A')
    inst = "AgAddAAgA".join(index)
    i+=1

inst= "A".join(index)

for letter in inst:
    if letter == 'A':
        t.forward(l)
    elif letter == 'g':
        t.left(alpha)
    elif letter == 'd':
        t.right(alpha)

#t.end_fill()
