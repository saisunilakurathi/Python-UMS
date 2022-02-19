"""
Author - Sai Sunil Akurathi
Created Date - 12-Feb-2022
File Name - database.py
"""
import math


class Student:  # Student class
    __studentId = 1000

    def __init__(self, stdFirstName, stdLastName, stdMarks, stdAddress):
        self.stdFirstName = stdFirstName
        self.stdLastName = stdLastName
        self.stdMarks = stdMarks
        self.stdAddress = stdAddress
        self.studentId = Student.__studentId
        Student.__studentId += 1

    def average(self):
        total_marks = 0
        for marks in self.stdMarks:
            total_marks += marks
        average_grade = total_marks / 3
        return math.ceil(average_grade)

    def __str__(self):
        return f'Student ID: {self.studentId} \nStudent Name: {self.stdFirstName} {self.stdLastName} ' \
               f'\nStudent Marks: {self.stdMarks} \nAverage Grade: {self.average()} \nStudent Address: {self.stdAddress}'


class Address:  # Address Class for student aggregation
    def __init__(self, streetInfo, city, postalCode, province, country):
        self.streetInfo = streetInfo
        self.city = city
        self.postalCode = postalCode
        self.province = province
        self.country = country

    def __str__(self):
        return f'Street - {self.streetInfo}, city - {self.city}, PostalCode - {self.postalCode},' \
               f'Province - {self.province}, Country - {self.country}'


class UndergraduateStudent(Student):  # UndergraduateStudent class inherits student class
    def __init__(self, stdFirstName, stdLastName, stdMarks, stdAddress, subject, yearOfEntry):
        super().__init__(stdFirstName, stdLastName, stdMarks, stdAddress)
        self.subject = subject
        self.yearOfEntry = yearOfEntry

    def graduate(self, average):
        if average > 50:
            return True
        else:
            return False

    def __str__(self):
        return super(UndergraduateStudent, self).__str__() + f'\nSubject: {self.subject} ' \
                                                             f'\nYear of Entry: {self.yearOfEntry}' \
                                                             f'\nGraduate: {self.graduate(self.average())}'


class GraduateStudent(Student):  # GraduateStudent class inherits student class
    def __init__(self, stdFirstName, stdLastName, stdMarks, stdAddress, subject, yearOfEntry, thesisTopic):
        super().__init__(stdFirstName, stdLastName, stdMarks, stdAddress)
        self.subject = subject
        self.yearOfEntry = yearOfEntry
        self.thesisTopic = thesisTopic

    def graduate(self, average):
        if average > 70:
            return True
        else:
            return False

    def __str__(self):
        return super(GraduateStudent, self).__str__() + f'\nSubject: {self.subject} \nYear of Entry: {self.yearOfEntry}' \
                                                        f'\nThesis Topic: {self.thesisTopic}, ' \
                                                        f'\nGraduate: {self.graduate(self.average())}'


class CreateStudents:  # CreateStudents class to save all students data
    __stuDict = {"ug": "", "pg": ""}

    def __init__(self, degree):
        self.degree = degree

    def save_new_student(self, new_student):
        if self.degree == "ug":
            new_student_list = {'Student ID\t': new_student.studentId, 'First Name\t': new_student.stdFirstName,
                                'Last Name\t': new_student.stdLastName, 'Marks\t\t': new_student.stdMarks,
                                'Average\t\t': new_student.average(), 'Address\t\t': new_student.stdAddress,
                                'Subject\t\t': new_student.subject, 'Year of Entry': new_student.yearOfEntry,
                                'Graduate': new_student.graduate(new_student.average())}
        elif self.degree == "pg":
            new_student_list = {'Student ID\t': new_student.studentId, 'First Name\t': new_student.stdFirstName,
                                'Last Name\t': new_student.stdLastName, 'Marks\t\t': new_student.stdMarks,
                                'Average\t\t': new_student.average(), 'Address\t\t': new_student.stdAddress,
                                'Subject\t\t': new_student.subject, 'Year of Entry': new_student.yearOfEntry,
                                'Thesis Topic': new_student.thesisTopic,
                                'Graduate': new_student.graduate(new_student.average())}
        if bool(CreateStudents.__stuDict.get(self.degree)):
            CreateStudents.__stuDict[self.degree].update({new_student.studentId: new_student_list})
        else:
            CreateStudents.__stuDict[self.degree] = {new_student.studentId: new_student_list}
        return CreateStudents.__stuDict

    def all_students(self):
        return CreateStudents.__stuDict
