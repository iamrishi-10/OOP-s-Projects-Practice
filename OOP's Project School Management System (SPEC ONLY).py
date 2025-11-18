class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name} is {self.age} years old'


class Student(Person):
    def __init__(self,name,age,student_id,marks):
        super().__init__(name,age)
        self.student_id = student_id
        self.marks = marks

    def get_average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks)/len(self.marks),1)

    def info(self):
        return f'{self.name} has {self.marks} marks and the average is {self.get_average()}'

class Teacher(Person):
    def __init__(self, name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,amount):
        if amount < 0:
            return f'The salary cannot be negative'
        else:
            self.__salary = amount
            return f'The salary has been updated to {self.__salary}'

    def info(self):
        return f'{self.name} is {self.age} years old and teaches {self.subject}'

class Course:
    def __init__(self,course_name,teacher,):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def course_summary(self):
        summary =  f'Course {self.course_name}\n'
        summary += f'Teacher {self.teacher.name}\n'
        summary +=  "Enrolled students\n"

        if not self.students:
            summary +=  "No students enrolled yet"
        else:
            for student in self.students:
                summary += f'\nStudent {student.name}\n'

        return summary

t1 = Teacher("Neha", 30, "Math", 80000)
s1 = Student("Rishi", 21, "S101", [85, 90, 78])
s2 = Student("Asha", 20, "S102", [92, 88, 95])
people = [t1, s1, s2]
for person in people:
    print(person.info())

course = Course("Data Science", t1)
course.add_student(s1)
course.add_student(s2)

print(course.course_summary())