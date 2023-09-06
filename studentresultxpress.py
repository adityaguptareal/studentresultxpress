import pandas as pd

# Initialize an empty DataFrame to store student data
student_data = pd.DataFrame(columns=["Name", "Physics", "Chemistry", "Maths", "English", "IP"])

# Input the number of students
n = int(input("Enter the number of students: "))

# Loop to collect data for each student
for i in range(n):
    student_name = input(f"Enter the Name of Student {i+1}: ")
    physics = int(input("Enter the Marks in Physics: "))
    chemistry = int(input("Enter the Marks in Chemistry: "))
    maths = int(input("Enter the Marks in Maths: "))
    english = int(input("Enter the Marks in English: "))
    ip = int(input("Enter the Marks in IP: "))
    
    # Create a dictionary with the student's data
    student_data_dict = {
        "Name": student_name,
        "Physics": physics,
        "Chemistry": chemistry,
        "Maths": maths,
        "English": english,
        "IP": ip
    }
    
    # Append the data to the DataFrame
    student_data = pd.concat([student_data, pd.DataFrame(student_data_dict, index=[0])], ignore_index=True)

# Transpose the DataFrame to display subjects as rows and student names as columns
student_data = student_data.set_index("Name")
student_data = student_data.T

# Print the DataFrame
print("\nStudent Data:")
print(student_data)
