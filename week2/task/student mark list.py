# a=input("enter the name:").split()
# b=""
# for i in a:
#    b+=i[0].upper()+"."
# print(b[:-1])

# co=['a','b','c','d']
# b=co.count("c")
# print(b)


# name=input("Name" )
# sub=int(input("enter the sub:"))

# update=[]

# for i in range(1,sub+1):
#     math=int(input("enter the mark:"))
#     sci=int(input("enter the mark"))

#     update.append([math,sci])

#     for s in update:
#         print("maths",s[0])
#         print("sci",s[1])

name=input("Name" )
b=[]
sub1=int(input("enter the sub1 mark:"))
sub2=int(input("enter the sub2 mark:"))
sub3=int(input("enter the sub3 mark:"))
sub4=int(input("enter the sub4 mark:"))
sub5=int(input("enter the sub5 mark:"))
b.append([sub1,sub2,sub3,sub4,sub5])

for s in b:
    print(f"subject of maths == {sub1}")
    print(f"subject of sci == {sub2}")
    print(f"subject of ss == {sub3}")
    print(f"subject of eng == {sub4}")
    print(f"subject of tamil == {sub5}")