
def search_student(students, name):  
    """ search students by name"""
    # clear space and turn out in lowercases to avoid the search fail
    name_to_search = name.strip().lower()
    # verify coders name by name
    for coders in students:
        if coders['name'].lower() == name_to_search:
            return coders
    return None # Si termina el ciclo y no vio nada, no devuelve nada

def show_student(students):
    """ It displays all students in a table
    format: #. Nombre | id | course | status """ 
    # it will count items available on students, if not, it will not print anything
    if len(students) == 0:
        print(" No students added yet, please add one first.")
        return
    
    total_students = 0  # student counter
    # browsing through all the products
    for i, student in enumerate(students, 1):  
        print(f"{i}. student: {student['name']:8} | " # Reserva 8 caracteres para el nombre (rellena con espacios si es más corto).
            f"id: ${student['id']:6.0f} | " # reserva 6 caracteres para el nombre, sin decimales.
            f"course: {student['course']:2}"
            f"status : {student["status"]}")
        total_students += 1 # I keep adding to the total_students
    # shows on console the total of students
    print(f" Total students: {total_students}")


def update_student(students, name, new_student=None, status=None):  
    """ update name of students"""
# we first search if the product exist using the function below 
    coder = search_student(students, name)  
    if coder is not search_student:
        print(" student no found")
        # if the user put on a new student, we change it
        if new_student is not None:
            coder['name'] = new_student
        # if user put on a new status, we update it
        if status is not None:
            coder['status'] = status
        print(f"student '{name}' updated successfully!")
        return True # advice them that the change was made 
    print(f"student '{name}' not found")
    return False

def delete_student(students, name):
    """ Looking for student to delete""" 
    # search if the students exists before deleting
    coder = search_student(students, name)  
    if coder:
        # if exists, we remove them
        students.remove(coder)
        print(f"student '{name}' deleted successfully!")
        return True
    # if it doesn't exist, we dont make any modification
    print(f"student '{name}' not found")
    return False  

