#Simple Authentication
correct_username="resultmanagement"
correct_Password="resultmanagement"

while True:
    username=input("Enter your Username: ")
    password=input("Enter your password: ")

    if username==correct_username and password==correct_Password:
        print("\n Authentical Succeful ! Welcome to the Program")
        break
    else:
        print("\n Authentication failed. Please try again.")

# Main Program

import pandas as pd

#creating an empty data from with columns
student_data=pd.DataFrame(columns=["Name","Physics", "Chemistry","Maths","English","Ip"])

#Checking Data of integer or not
while True:
    total_students=(input("Enter the total number of students: "))
    if total_students.isdigit():
        total_students=int(total_students)
        break
    else:
        print("\nPlease Enter the Number of Students in Integer ")
for i in range(total_students):
    student_name=input(f"\nEnter the Name of Student {i+1} : ")
    physics=int(input(f"\nEnter the marks of {student_name} in physics: "))
    chemistry=int(input(f"Enter the marks of {student_name} in chemistry: "))
    maths=int(input(f"Enter the marks of {student_name} in maths: "))
    english=int(input(f"Enter the marks of {student_name} in english: "))
    ip=int(input(f"Enter the marks of {student_name} in ip: "))

# Getting data in dictionary of each students
    student_dict_data={
        "Name": student_name,
        "Physics": physics,
        "Chemistry":chemistry,
        "Maths":maths,
        "English":english,
        "Ip":ip,
    }
#concatenating the program
    student_data=pd.concat([student_data,pd.DataFrame(student_dict_data,index=[0])],ignore_index=True)
student_data=student_data.set_index("Name")

#transposing rows and columns for vaild output
student_data=student_data.T
student_data.to_csv("student_data.csv")
print(f'\n{student_data}')
# while True:
#     search_name = input("\nEnter the name of the student to retrieve their subject marks (or type 'exit' to quit): ")
#     if search_name.lower() == "exit":
#         break

#     # Check if the student name exists in the DataFrame
#     if search_name in student_data.columns:
#         print(f"\nSubject marks for {search_name}:")
#         print(student_data[search_name])
#     else:
#         print(f"\nStudent '{search_name}' not found in the records. Please enter a valid student name.")

