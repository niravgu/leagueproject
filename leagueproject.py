import random
name = input("hey, what's your name?")
print("hey",name,"now I will think of a number and you have to guess it.")
compuselect = str(random.randint(2500,9999))
print("guess a digit")
guesses = ''
x = 8
while x>0:
    failed =0
    for n in compuselect:
        if n in guesses:
            print(n)
        else :
            print("*")
            failed += 1
    if failed == 0:
        print("hah! you beat me. You are smart")
        print("Yes!the number was",compuselect)
        print("you did it in ",8-x,"turns")
        break
    guess =  input("any number please ")
    guesses += guess
    if guess not in compuselect:
        x -= 1
        print("sorry friend,It is wrong")
        print ("well,you have",x,"turns left")
        if x ==0:
            print("haha I won fair and square")
            print("the number was",compuselect)