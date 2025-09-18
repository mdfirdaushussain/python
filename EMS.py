def view_employee(employee_data):
    for i,j in employee_data.items():
        if not employee_data:
            print("Employee not found!")
            break
        print(i,":",j)


def search_employee(employee_data):
    i=input("Enter employee ID:")
    if i not in employee_data.keys():
        print("Employee not found!")
    print(employee_data[i])

def add_employee(employee_data):
        
    while True:
        imp_id=input("Enter Employee ID:")
    
        if imp_id in employee_data.keys():
            print("Enter a new ID:")
        else:
            break    
        
    val={
        "Name":input("Enter employee name:"),
        "Age":input("Enter Employee Age:"),
        "Department":input("Enter Department Name:"),
        "salary":input("Enter salary:")
        
    }
    employee_data[imp_id]=val
    print("Employee was successfully added!")

employee_data={}    
while True:
    print("menu: \n1. Add Employee\n2. View All Employees\n3. Search for Employee\n4. Exit")
    n=int(input("Enter a number:"))  
    if n==4:
        print("Thank You!")
        break
    elif n>4 or n<1:
        print("Invalid choice!") 
    elif n==1:
        add_employee(employee_data) 
    elif n==2:
        view_employee(employee_data) 
    elif n==3:
        search_employee(employee_data)          
         
