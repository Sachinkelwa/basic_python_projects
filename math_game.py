import random
def number():
    m=random.randint(1,10015)
    n=random.randint(1,15014)
    o=random.randint(1,505)
    return m,n,o
def opre():
    lis= ["x","+","-","/"]
    d = random.choice(lis)
    f = random.choice(lis)
    return d,f
a,b,c = number()     
x,y = opre()   
print("let's start the game :")  

ans = 0
if x == "x":
    if y == "x":
        ans = a * b * c 
    elif y == "+":
        ans = a * b + c
    elif y == "-":
        ans = a * b - c
    else:
        ans = a * b / c
elif x == "+":
    if y == "x":
        ans = a + b * c 
    elif y == "+":
        ans = a + b + c
    elif y == "-":
        ans = a + b - c
    else:
        ans = a + b / c
elif x == "-":
    if y == "x":
        ans = a - b * c 
    elif y == "+":
        ans = a - b + c
    elif y == "-":
        ans = a - b - c
    else:
        ans = a - b / c
else :
    if y == "x":
        ans = a / b * c 
    elif y == "+":
        ans = a / b + c
    elif y == "-":
        ans = a / b - c
    else:
        ans = a / b / c
user_answer = int(input(f"what is {a} {x} {b} {y} {c} = "))
if user_answer == int(ans):
    print("congratulation your answer is correct")
    print(f"currect naswer is : {ans}") 
else:
    print("ohho! wrong answer")
    print(f"correct naswer is : {ans}")