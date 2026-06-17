import random
number=random.randint(1,100)
attempt=0
while (attempt<5):
    a=int(input("enter the guessing number:"))
    if number == a:
       break
    elif number > a:
        print("low")
    elif number < a:
        print("high")
    else:
        print("give hit")
    attempt+=1
if attempt==5:
    print("Get Lost")
       
