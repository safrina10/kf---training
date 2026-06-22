a={"ayesha","malik","sri","hari"}
b={"ayesha","malik","dinesh","nandhu"}

print("1. the common frineds:")
print("2 Only friends with a ")
print("3. add friends")
print("4.remove friends")
print("5. union friends")
print("6. exit")

while True:
    c=int(input(" enter the option:"))

    if c==1:
        print(a&b)
    elif c==2:
        print(a-b)
    elif c==3:
        name =input("name")
        option=input("where you need to add : a or b")
        if option=='a':
         a.add(name)
        print(a)
        if option=='b':
            b.add(name)
        print(b)
    elif c==4:
        delete=input("enter the name:")
        click=input("where you need to remove:a or b")
        if click =='a':
            a.remove(delete)
            print(a)
        if click=='b':
            b.remove(delete)
            print(b)
    elif c==5:
        print(a|b)
    elif c==6:
        print(exit)
        break