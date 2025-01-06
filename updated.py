import csv

class SchoolMember:
    def __init__(self, first_name, middle_name, last_name, address):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address

    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def show_details(self):
        print("Name: " + self.full_name())
        print("Address: " + self.address)

# Teacher Class
class Teacher(SchoolMember):
    def __init__(self, first_name, middle_name, last_name, address, department, subject, qualification, salary, past_experience, contact_no):
        super().__init__(first_name, middle_name, last_name, address)
        self.department = department
        self.subject = subject
        self.qualification = qualification
        self.__salary = salary  # Salary is private and immutable
        self.past_experience = past_experience
        self.contact_no = contact_no

    def show_details(self):
        print("Teacher Details:")
        super().show_details()
        print("Department: " + self.department)
        print("Subject: " + self.subject)
        print("Qualification: " + self.qualification)
        print("Salary: Rs." + str(self.__salary))
        print("Experience: " + str(self.past_experience) + " years")
        print("Contact: " + self.contact_no)

    @staticmethod
    def input_teacher():
        first_name, middle_name, last_name = input("Enter Name (First Middle Last): ").split()
        address = input("Enter Teacher's Address: ")
        department = input("Enter Department: ")
        subject = input("Enter Subject: ")
        qualification = input("Enter Qualification: ")
        salary = float(input("Enter Salary: "))
        past_experience = float(input("Enter Past Experience (in years): "))
        contact_no = input("Enter Contact Number: ")
        return Teacher(first_name, middle_name, last_name, address, department, subject, qualification, salary, past_experience, contact_no)

# Non-Teaching Staff Class
class NonTeachingStaff(SchoolMember):
    def __init__(self, first_name, middle_name, last_name, address, work, salary):
        super().__init__(first_name, middle_name, last_name, address)
        self.work = work
        self.__salary = salary  # Salary is private and immutable

    def show_details(self):
        print("Non-Teaching Staff Details:")
        super().show_details()
        print("Work: " + self.work)
        print("Salary: Rs." + str(self.__salary))

    @staticmethod
    def input_non_teaching_staff():
        first_name, middle_name, last_name = input("Enter Name (First Middle Last): ").split()
        address = input("Enter Staff's Address: ")
        work = input("Enter Work Description: ")
        salary = float(input("Enter Salary: "))
        return NonTeachingStaff(first_name, middle_name, last_name, address, work, salary)

# Student Class
class Student(SchoolMember):
    def __init__(self, first_name, middle_name, last_name, address, age, standard, division, roll_no, fees, current_grades, previous_school, previous_std_grades, parents_phone_no):
        super().__init__(first_name, middle_name, last_name, address)
        self.age = age
        self.standard = standard
        self.division = division
        self.roll_no = roll_no
        self.fees = fees
        self.current_grades = current_grades
        self.previous_school = previous_school
        self.previous_std_grades = previous_std_grades
        self.parents_phone_no = parents_phone_no

    def show_details(self):
        print("Student Details:")
        super().show_details()
        print("Age: " + str(self.age))
        print("Standard: " + self.standard)
        print("Division: " + self.division)
        print("Roll No: " + str(self.roll_no))
        print("Fees: Rs." + str(self.fees))
        print("Current Grades: " + self.current_grades)
        print("Previous School: " + self.previous_school)
        print("Previous Grades: " + self.previous_std_grades)
        print("Parents' Contact: " + self.parents_phone_no)

    @staticmethod
    def input_student():
        first_name, middle_name, last_name = input("Enter Name (First Middle Last): ").split()
        address = input("Enter Student's Address: ")
        age = int(input("Enter Age: "))
        standard = input("Enter Standard: ")
        division = input("Enter Division: ")
        roll_no = int(input("Enter Roll No: "))
        fees = float(input("Enter Fees: "))
        current_grades = input("Enter Current Grades: ")
        previous_school = input("Enter Previous School: ")
        previous_std_grades = input("Enter Previous Grades: ")
        parents_phone_no = input("Enter Parents' Contact Number: ")
        return Student(first_name, middle_name, last_name, address, age, standard, division, roll_no, fees, current_grades, previous_school, previous_std_grades, parents_phone_no)

# School Class
class School:
    def __init__(self):
        self.members = []
        self.load_data()

    def add_member(self, member):
        if self.check_duplicate_name(member.full_name()):
            print(f"Error: Member with name {member.full_name()} already exists!")
        else:
            self.members.append(member)
            self.save_data()

    def check_duplicate_name(self, name):
        return any(member.full_name() == name for member in self.members)

    def show_all_members(self):
        if not self.members:
            print("No members have been added yet!")
        else:
            for member in self.members:
                member.show_details()
                print()

    def edit_member(self, name):
        for member in self.members:
            if member.full_name() == name:
                print("Editing Details...")
                member.show_details()
                # Edit logic can be added based on specific fields and type
                return
        print("Member not found.")

    def save_data(self):
        with open('school_members_gujarat.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for member in self.members:
                if isinstance(member, Teacher):
                    writer.writerow(["Teacher", member.first_name, member.middle_name, member.last_name, member.address,
                                     member.department, member.subject, member.qualification, member._Teacher__salary,
                                     member.past_experience, member.contact_no])
                elif isinstance(member, NonTeachingStaff):
                    writer.writerow(["NonTeachingStaff", member.first_name, member.middle_name, member.last_name,
                                     member.address, member.work, member._NonTeachingStaff__salary])
                elif isinstance(member, Student):
                    writer.writerow(["Student", member.first_name, member.middle_name, member.last_name, member.address,
                                     member.age, member.standard, member.division, member.roll_no, member.fees,
                                     member.current_grades, member.previous_school, member.previous_std_grades,
                                     member.parents_phone_no])

    def load_data(self):
        try:
            with open('school_members_gujarat.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == "Teacher":
                        self.members.append(Teacher(row[1], row[2], row[3], row[4], row[5], row[6], row[7], float(row[8]), 
                                                     float(row[9]), row[10]))
                    elif row[0] == "NonTeachingStaff":
                        self.members.append(NonTeachingStaff(row[1], row[2], row[3], row[4], row[5], float(row[6])))
                    elif row[0] == "Student":
                        self.members.append(Student(row[1], row[2], row[3], row[4], int(row[5]), row[6], row[7], 
                                                     int(row[8]), float(row[9]), row[10], row[11], row[12], row[13]))
        except FileNotFoundError:
            print("No previous data found. Starting with an empty database.")

# Main Program Loop
school = School()

while True:
    print("\n--- School Management System ---")
    print("1. Add Teacher")
    print("2. Add Non-Teaching Staff")
    print("3. Add Student")
    print("4. Show All Members")
    print("5. Edit Member")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        teacher = Teacher.input_teacher()
        school.add_member(teacher)
    elif choice == '2':
        non_teaching_staff = NonTeachingStaff.input_non_teaching_staff()
        school.add_member(non_teaching_staff)
    elif choice == '3':
        student = Student.input_student()
        school.add_member(student)
    elif choice == '4':
        school.show_all_members()
    elif choice == '5':
        name = input("Enter the full name of the member to edit: ")
        school.edit_member(name)
    elif choice == '0':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
