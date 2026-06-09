"""
a=input("enter the name:")
b=int(input("age"))
c=input("enter the collage:")

print(f"my name is {a}")
print(f"i'm {b} old")
print(c)
"""
"""
a=int(input())
b=0
for i in range(a+1):
    b=b+i
print(b)
"""
"""
a=int(input())
for i in range(2,a+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count == 2:
        print(i,"prime number")
"""
"""
a=int(input("enter the number:"))
for i in range(1,a+1):
    if (i%2==0):
        print(i,"even")
    else:
        print(i,"odd")
"""
"""
a=int(input("enter the number:"))
if (a>0):
    print("positive")
else:
    print("negative")
"""
"""
a=int(input("enter the number:"))
if (a%400==0)or(a%4==0 and 100!=0):
    print("leap")
else:
    print("not a leap")
"""
"""
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c
"""