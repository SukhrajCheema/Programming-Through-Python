class Student:
    def __init__(self, firstname, lastname, course):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.modules = []

    def show_details(self):
        print(f"Details of this student: {self.firstname} {self.lastname} {self.course}")
        if len(self.modules) == 0:
            print("Not enrolled on any modules")
        else:
            print("Enrolled in the following:")
            for x in self.modules:
                print(x)

    def change_course(self, new_course):
        self.course = new_course
        print(f"You have changed from {self.course} to {new_course}")


class Module:
    def __init__(self, name, code, tutor):
        self.name = name
        self.code = code
        self.tutor = tutor
        self.students = []

    def enrol_student(self, student):
        self.students.append(student)
        student.modules.append(self.code)          # Can access the empty modules list from student objects, since arguement is an instance of a student.

    def show_all_enrolled(self):
        if len(self.students) == 0:
            print(f"No students enrolled for {self.code}.")
        else:
            print(f"Enrolled on module: {self.code}")
            for x in self.students:
                print(f"{x.firstname} {x.lastname}")


def main():
    # Create some students and some modules ...
    s1 = Student('ken', 'barlow', 'english')
    s2 = Student('mike', 'baldwin', 'business')
    s3 = Student('harold', 'legg', 'medicine')

    m1 = Module('English language and semantics', 'A101', 'Wanda Pickle')
    m2 = Module('Engineering principles', 'E102', 'Buzz Jones')
    m3 = Module('Anatomy', 'M105', 'Greg House')

    # Now enrol some students on some modules ...
    m1.enrol_student(s1)
    m1.enrol_student(s2)
    m2.enrol_student(s1)
    m2.enrol_student(s3)

    # Have a look at some students and some modules ...
    s1.show_details()
    s2.show_details()
    s3.show_details()

    m1.show_all_enrolled()
    m2.show_all_enrolled()
    m3.show_all_enrolled()

    # Change a course ...
    s1.change_course('engineering')
    s1.show_details()


if __name__ == "__main__":
    main()
