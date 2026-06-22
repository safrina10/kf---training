a=input("Enter The Name :")

maths=int(input("enter the maths mark: "))
science=int(input("enter the science mark: "))
social=int(input("enter the social mark: "))
marks=[maths,science,social]

print(f"pnd adarsh vidlayala school"
f"\n 1.report card view: ")
print(f"2. delete the mark: ")
print(f"3.add the mark: ")
print(f"4.remove dupliactes: ")
print("5.exit")

while True:
    n=int(input("enter the choice "))
    if n==1:
        print("\n REPORT CARD ")
        print("Name Student: ", a)
        print("Maths Mark:",maths)
        print("Science Mark:",science)
        print("Social Mark",social)
    if n==2:
        index = int(input("Enter index to delete: "))
        if 0 <= index < len(marks):
            marks.pop(index)
            print("Maths Mark:",maths)
            print("Science Mark:",science)
            print("Social Mark",social)
            print("Updated list:", marks)
        else:
            print("Invalid index")

    if n==3:
        number=int(input("enter the number : "))    
        if number not in marks:
            marks.append(number)
            print("upadates lits",marks)
        else:
            print("valid number")  
    if n==4:
        original=[]
        for i in marks:
            if marks not in original:
                original.append(i)
        print(original)
    if n==5:
        exit()
        print("Thank You")




