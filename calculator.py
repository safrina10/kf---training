
a=int(input("enter the number:"))
b=int(input("enter the number:"))
exp=input("enter the exp:+,-,%,*")

if exp == "+":
    print(a+b)
elif exp == "-":
    print(a-b)
elif exp == "%":
    print(a%b)
else:
    print(a*b)

a=int(input("enter the number:"))
b=int(input("enter the number:"))
exp=input("enter the operation:+-*%")
match exp:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "%":
        print(a%b)
    case "*":
        print(a*b)

