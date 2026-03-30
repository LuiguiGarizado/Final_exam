# Final_examSimulator management students

Description

This program is a simulator of management students structure with knowledge in python, the program ask the user that enters their name, Id, course and status, after validation to avoid margen of error, and finally, it will print on consola all the information added.

## Tecnologías y Conceptos Utilizados

Language: Python 3.x Conditional Logic and Flow Control: * Use of try-except blocks for data type validation.

## Implemented Python functions

    input(): To capture the information write by the user
    float():To convert the input in ID to a float number 3.print(): To show the messages or any script error on consola
    try, except: To verify invalid data
    innumerate() and string formatting for aligned and better organized tables.
    use of functions define with "def" to organize the code in a reusable manner

## logic about save csv

The function save csv (option 6) which offers two modes: Replace: clear the students data and replace it. Merge: compare name of the students, add to the stock and update the information added if needed.

## How it works

    add student (add_student) : allows to register the user name, ID, status and course, the system validates the infomation is correct( e.g if the user writes a letter instead of number on id, it will print a error)
    Show student (show_student): Generates a list of all saved products with a pleasing and aligned design for easy reading.
    Search student (search_student): Find a specific item by name and display its details on screen. It doesn't matter if you type in uppercase or lowercase.
    Delete student (delete_student): Permanently deletes an item from the list after searching for it by name.
    Update student (update_student): Allows you to modify the status of an existing student. If the name does not exist, the program will notify you.

## status of the project

> The program is currently a project of standard knowledge in python, demonstrating the manage of input and validating of data in python
