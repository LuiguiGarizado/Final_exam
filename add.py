students= []

def add_student(students):
    """  Add students"""
    running =  "yes" # repetitive cicle to confim user enters the requested information
    while running.lower() == "yes":
            name = input("student's name : ").strip()
            if name == "":  
                print("Error: Student name cannot be empty")
                continue
    
            id = int(input("Enter your ID : "))
    
            course = input(" Enter your course ")
            if course == "":
                print("Error: course cannot be empty")
                continue
        
            status= input(" what is the student's status: ")
            if status == "":
                print(" You must enter an status")
        
    
    # verify if the student exist, avoid duplicated
            existing_student= None # no found a student yet
            for student in students:
                if student['name'].lower() == name.lower(): # lowercase(minúscula)
                    existing_student = student
                    break
    
        # add new students
            student = {
                "name": name.capitalize(),
                "id": id,
                "course": course,
                "status" : status
                }

            students.append(student)
            print(f"student '{name}' added successfully!")

            running = input(" do you want to add another student (yes,no)").strip() .upper()


