employees=()

for i in range(2):
    id=int(input("Enter The Id No: "))
    Name=input("Enter The Name : ")
    salary=int(input("Enter The Salary: "))
    emp=(id,Name,salary)
    employees=employees+(emp,)

while True:
       
    print("1.See All Employee Records: ")
    print("2.View The Employee")
    print("3.Employee Details By Name: ")
    print("4.High Salary And Low Salary: ")
    print("5. count the employees")
    print("6. exit")

    ac=int(input("enter the choice: "))
    if ac==1:
        print("Record Of Employees:")
        print(employees)
    elif ac==2:
        emp_id=int(input("Enter The Id: "))
        
        for i in employees:
            id,Name,salary=i
            if emp_id == id:
                print(id,Name,salary)
                
            else:
                print("pls enter valid id")
                continue
    elif ac==3:
        b=input("Enter the name: ")
        for i in employees:
            id,Name,salary=emp
            if b==Name:
                print(id,Name,salary)
                break
    elif ac==4:
        hike=input("enter the opition: max, mini")
        salaries = []
        for emp in employees:
          salaries.append(emp[3])
        if hike=="max":
            print("highest salary:",max(salaries))
        else:
            print("minimun salary:",min(salaries)) 
    elif ac==5:
        id=employees
        print(len(employees))
    elif ac==6:
        print(exit)
        print("Thank You")

