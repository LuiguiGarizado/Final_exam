import csv

def save_csv(students):
    """Save students to studentsdata.csv"""
    # verify if the list is empty 
    if len(students) == 0:
        print("No students added yet")
        return False #returning false to say " it cannot be save"
    # save students to studentsdata.csv
    
    ruta = "studentsdata.csv"
    path = ruta.split(".")

# verify the correct format
    if len(path) != 2 or path[1].lower() != "csv":
        print(" Error: Only .CSV files allowed!")
        print(" Examples: data.csv, sales.csv")
        return False # existing the function without making any changes
    
      # Try open the file 
    try:
        # open the file "studentsdata.csv", to write ( mode "w", open the file "studentsdata".csv")
        with open("studentsdata.csv", 'w', newline='', encoding='utf-8') as file:
            # crea a file which only have 4 lines
            writer = csv.DictWriter(file, fieldnames=['name', 'id', 'course', 'status',])
            #  write the first line with the name of the rows 
            writer.writeheader()
            # write all the students (any of them in a dictionary format)
            writer.writerows(students)
        print("Inventory saved to studentsdata.csv")
        return True
    except Exception as error:
        print(f"Error: {error}")
        return False
