"""
Author - Sai Sunil Akurathi
Created Date - 12-Feb-2022
File Name - main.py
"""

from datetime import date
import database as db


def continue_app():  # function to continue to display main menu
    continue_to_app = str(input("Do you want to continue(y/n): "))
    if continue_to_app.lower() == 'y':
        main_menu()
    elif continue_to_app.lower() == 'n':
        print("*******************************")
        print("Thanks for using application...")
        exit
    else:
        print("*******************************")
        print("Please enter only(y/n)!")
        print("*******************************")
        continue_app()


def main_menu():    # main menu to display when program starts
    menu_list = ['1. Add undergraduate student', '2. Add graduate student', '3. View all the students',
                 '4. View only eligible students for graduation', '5. exit']
    print('**************************************')
    print('********* Sri Sai University *********')
    print('**************************************')
    for menu in menu_list:
        print(menu)
    while True:
        try:
            option = int(input('Enter an option in the above menu[ex: 1 or 2 or 3,...]: '))
            main_options(option)
            break
        except ValueError:
            print("That's not a valid option, please try again...")


def get_student_details(degree):  # function to read new student details
    marks = []
    student_details = {'first_name': str(input('Enter student first name: ')),
                       'last_name': str(input('Enter student last name: ')),
                       'subject': str(input('Enter student Subject: '))}

    print("Enter student marks below...")
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f'Enter marks in major {i}: '))
                if mark < 0 or mark > 100:
                    raise ValueError("The marks must be in between 0 and 100")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("That's not a valid input.. Try again...")
    student_details['marks'] = marks
    while True:
        try:
            student_details['year_of_entry'] = int(input('Enter year of entry: '))
            if 1900 < student_details['year_of_entry'] <= date.today().year:
                break
            else:
                raise ValueError('Enter a valid year...')
        except ValueError:
            print("That's not a valid year.. Try again...")
    if degree == "pg":
        student_details['thesis_topic'] = str(input('Enter Thesis topic: '))
    print('Enter Student''s Address below: ')
    street_info = str(input('Enter street address: '))
    city = str(input('Enter city: '))
    postal_code = str(input('Enter postal code: '))
    province = str(input('Enter province: '))
    country = str(input('Enter country: '))
    address = db.Address(street_info, city, postal_code, province, country)
    student_details['address'] = address.__str__()
    return student_details


def register_new_student(student_details, degree):  # function to save new students
    if degree == "ug":
        new_student = db.UndergraduateStudent(student_details['first_name'], student_details['last_name'],
                                              student_details['marks'], student_details['address'],
                                              student_details['subject'], student_details['year_of_entry'])
    if degree == "pg":
        new_student = db.GraduateStudent(student_details['first_name'], student_details['last_name'],
                                         student_details['marks'], student_details['address'],
                                         student_details['subject'], student_details['year_of_entry'],
                                         student_details['thesis_topic'])
    create_students = db.CreateStudents(degree)
    create_students.save_new_student(new_student)
    return new_student


def print_all_students(view_all_students, degree):  # function to print all students
    for key, value in view_all_students[degree].items():
        print(f'******** Details of student - {key} ********')
        for k, v in value.items():
            if k != "Graduate":
                print(k + "\t: " + str(v))
        print()


def display_all_students():  # function to display all students
    view_all_students = db.CreateStudents.all_students("all")
    if bool(view_all_students["ug"]) or bool(view_all_students["pg"]):
        print("******* Undergraduate students details *******")
        if bool(view_all_students["ug"]):
            print_all_students(view_all_students, "ug")
        else:
            print("No students admitted in undergraduate")

        print("********* Graduate students details *********")
        if bool(view_all_students["pg"]):
            print_all_students(view_all_students, "pg")
        else:
            print("No students admitted in Graduate")
    else:
        print("No students are admitted in the university!")


def print_eligible_students(view_all_students, degree):  # function to print all eligible students
    print(f"********** Eligible Graduate students in {degree} **********")
    counter = 0
    if bool(view_all_students):
        for student, details in view_all_students.items():
            if details['Graduate']:
                counter = counter + 1
                for k, v in details.items():
                    if k == 'Graduate':
                        print(k + "\t\t:" + "Yes")
                    else:
                        print(k + "\t:" + str(v))
        print()
    else:
        print("No graduate students found..")
    if counter == 0:
        print('No Students Found')


def display_eligible_students():  # function to display all eligible students
    view_all_students = db.CreateStudents.all_students("all")
    if bool(view_all_students['ug']):
        print_eligible_students(view_all_students["ug"], "ug")
    else:
        print("No Undergraduate students in University")

    if bool(view_all_students["pg"]):
        print_eligible_students(view_all_students["pg"], "pg")
    else:
        print("No Graduate students in University")


def main_options(option=0):
    if option == 1:  # Add undergraduate student
        print("Please provide undergraduate student details below")
        student_details = get_student_details("ug")
        new_ug_student = register_new_student(student_details, "ug")
        print(f"New undergraduate student added to database successfully, with id:{new_ug_student.studentId}")
        continue_app()
    elif option == 2:  # Add graduate student
        print("Please provide postgraduate student details below")
        student_details = get_student_details("pg")
        new_pg_student = register_new_student(student_details, "pg")
        print(f"New graduate student added to database successfully, with id:{new_pg_student.studentId}")
        continue_app()
    elif option == 3:  # View all the students
        display_all_students()
        continue_app()
    elif option == 4:  # View only eligible students for graduation
        display_eligible_students()
        continue_app()
    elif option == 5:  # exit
        print("Thanks for using the application")
        exit
    else:
        print('Please enter only available options in the list')
        main_menu()


main_menu()  # main function - program drives from here
