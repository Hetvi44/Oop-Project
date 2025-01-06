import csv

class SchoolMember:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_details(self):
        print("Name: " + self.name)
        print("Address: " + self.address)

# Teacher Class (inherits from SchoolMember)
class Teacher(SchoolMember):
    def __init__(self, name, address, department, subject, qualification, salary, past_experience, contact_no):
        super().__init__(name, address)
        self.department = department
        self.subject = subject
        self.qualification = qualification
        self.__salary = salary  # Salary is private and immutable
        self.past_experience = past_experience
        self.contact_no = contact_no

    def show_details(self):
        print("Teacher Details:")
        print("Name: " + self.name)
        print("Department: " + self.department)
        print("Subject: " + self.subject)
        print("Qualification: " + self.qualification)
        print("Salary: Rs." + str(self.__salary))
        print("Experience: " + str(self.past_experience) + " years")
        print("Contact: " + self.contact_no)
        print("Address: " + self.address)

    @staticmethod
    def input_teacher():
        name = input("Enter Teacher's Name: ")
        address = input("Enter Teacher's Address: ")
        department = input("Enter Department: ")
        subject = input("Enter Subject: ")
        qualification = input("Enter Qualification: ")
        salary = float(input("Enter Salary: "))
        past_experience = float(input("Enter Past Experience (in years): "))
        contact_no = input("Enter Contact Number: ")
        return Teacher(name, address, department, subject, qualification, salary, past_experience, contact_no)

# Non-Teaching Staff Class (inherits from SchoolMember)
class NonTeachingStaff(SchoolMember):
    def __init__(self, name, address, work, salary):
        super().__init__(name, address)
        self.work = work
        self.__salary = salary  # Salary is private and immutable

    def show_details(self):
        print("Non-Teaching Staff Details:")
        print("Name: " + self.name)
        print("Work: " + self.work)
        print("Salary: $" + str(self.__salary))
        print("Address: " + self.address)

    @staticmethod
    def input_non_teaching_staff():
        name = input("Enter Non-Teaching Staff's Name: ")
        address = input("Enter Non-Teaching Staff's Address: ")
        work = input("Enter Work Description: ")
        salary = float(input("Enter Salary: "))
        return NonTeachingStaff(name, address, work, salary)

# Student Class (inherits from SchoolMember)
class Student(SchoolMember):
    def __init__(self, name, address, age, standard, division, roll_no, fees, current_grades, previous_school, previous_std_grades, parents_phone_no):
        super().__init__(name, address)  
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
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Standard: " + self.standard)
        print("Division: " + self.division)
        print("Roll No: " + str(self.roll_no))
        print("Fees: Rs." + str(self.fees))
        print("Current Grades: " + self.current_grades)
        print("Previous School: " + self.previous_school)
        print("Previous Grades: " + self.previous_std_grades)
        print("Parents' Contact: " + self.parents_phone_no)
        print("Address: " + self.address)

    @staticmethod
    def input_student():
        name = input("Enter Student's Name: ")
        address = input("Enter Student's Address: ")
        age = int(input("Enter Student's Age: "))
        standard = input("Enter Standard: ")
        division = input("Enter Division: ")
        roll_no = int(input("Enter Roll No: "))
        fees = float(input("Enter Fees: "))  # Collecting 'fees'
        current_grades = input("Enter Current Grades: ")
        previous_school = input("Enter Previous School: ")
        previous_std_grades = input("Enter Previous Grades: ")
        parents_phone_no = input("Enter Parents' Contact Number: ")
        return Student(name, address, age, standard, division, roll_no, fees, current_grades, previous_school, previous_std_grades, parents_phone_no)

# School Class to manage all members
class School:
    def __init__(self):
        self.members = []
        self.load_data()  # Load data when School object is created

    def add_member(self, member):
        self.members.append(member)
        self.save_data()  # Save data to CSV every time a new member is added

    def show_all_members(self):
        if not self.members:
            print("No members have been added yet!")
        else:
            for member in self.members:
                member.show_details()
                print()

    def save_data(self):
        with open('school_members.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for member in self.members:
                if isinstance(member, Teacher):
                    writer.writerow(["Teacher", member.name, member.address, member.department, member.subject,
                                     member.qualification, member._Teacher__salary, member.past_experience, member.contact_no])
                elif isinstance(member, NonTeachingStaff):
                    writer.writerow(["NonTeachingStaff", member.name, member.address, member.work, member._NonTeachingStaff__salary])
                elif isinstance(member, Student):
                    writer.writerow(["Student", member.name, member.address, member.age, member.standard,
                                     member.division, member.roll_no, member.fees, member.current_grades,
                                     member.previous_school, member.previous_std_grades, member.parents_phone_no])

    def load_data(self):
        try:
            with open('school_members.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == "Teacher":
                        teacher = Teacher(row[1], row[2], row[3], row[4], row[5], float(row[6]), float(row[7]), row[8])
                        self.members.append(teacher)
                    elif row[0] == "NonTeachingStaff":
                        non_teaching_staff = NonTeachingStaff(row[1], row[2], row[3], float(row[4]))
                        self.members.append(non_teaching_staff)
                    elif row[0] == "Student":
                        student = Student(row[1], row[2], int(row[3]), row[4], row[5], int(row[6]),
                                          float(row[7]), row[8], row[9], row[10], row[11])
                        self.members.append(student)
        except FileNotFoundError:
            print("No previous data found. Starting with an empty database.")

# Main program loop
school = School() # Created a School object

while True:
    print("\n--- School Management System ---")
    print("1. Add Teacher")
    print("2. Add Non-Teaching Staff")
    print("3. Add Student")
    print("4. Show All Members")
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
    elif choice == '0':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")

# --- School Management System ---
# 1. Add Teacher
# 2. Add Non-Teaching Staff
# 3. Add Student
# 4. Show All Members
# 0. Exit
# Enter your choice: 1
# Enter Teacher's Name: manish chaturvedi
# Enter Teacher's Address: gandhinagar
# Enter Department: CSE
# Enter Subject: OOPS
# Enter Qualification: Phd
# Enter Salary: 80000
# Enter Past Experience (in years): 12
# Enter Contact Number: 9989740001

# --- School Management System ---
# 1. Add Teacher
# 2. Add Non-Teaching Staff
# 3. Add Student
# 4. Show All Members
# 0. Exit
# Enter your choice: 2
# Enter Non-Teaching Staff's Name: bhaveshbhai
# Enter Non-Teaching Staff's Address: ahm
# Enter Work Description: cleaning
# Enter Salary: 15000

# --- School Management System ---
# 1. Add Teacher
# 2. Add Non-Teaching Staff
# 3. Add Student
# 4. Show All Members
# 0. Exit
# Enter your choice: 3
# Enter Student's Name: drashvi patel
# Enter Student's Address: morbi
# Enter Student's Age: 18
# Enter Standard: 12
# Enter Division: A
# Enter Roll No: 12
# Enter Fees: 120000
# Enter Current Grades: A2
# Enter Previous School: Nirmal School
# Enter Previous Grades: A2
# Enter Parents' Contact Number: 9979786066

# --- School Management System ---
# 1. Add Teacher
# 2. Add Non-Teaching Staff
# 3. Add Student
# 4. Show All Members
# 0. Exit
# Enter your choice: 4
# Will show all the added members but they are not shown here as they are too many

# --- School Management System ---
# 1. Add Teacher
# 2. Add Non-Teaching Staff
# 3. Add Student
# 4. Show All Members
# 0. Exit
# Enter your choice: 0
# Exiting program...

