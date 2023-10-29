class Exam:
    def __init__(self):
        # Initialize lists to store students and exam questions
        self.students = []
        self.questions = []
        self.roll = 1  # Initialize student roll number

    def start(self):
        while True:
            # Display the main menu options
            print("Examination System")
            print("1. Staff")
            print("2. Student")
            print("3. Exit")
            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.staff_menu()
            elif choice == "2":
                self.student_menu()
            elif choice == "3":
                print("Exiting the Examination System. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def staff_menu(self):
        while True:
            # Display staff menu options
            print("1. Approve Students")
            print("2. Create Exam")
            print("3. Report")
            print("4. Back to Main Menu")
            choice = input("Enter Your choice: ")

            if choice == "1":
                self.approve_students()
            elif choice == "2":
                self.create_exam()
            elif choice == "3":
                self.generate_report()
            elif choice == "4":
                break
            else:
                print("Invalid Choice. Please choose a valid option.")

    def student_menu(self):
        while True:
            # Display student menu options
            print("1. Create Student")
            print("2. Attend Exam")
            print("3. Report")
            print("4. Back to Main Menu")
            choice = input("Enter Your choice: ")

            if choice == "1":
                self.create_student()
            elif choice == "2":
                self.attend_exam()
            elif choice == "3":
                self.student_report()
            elif choice == "4":
                break
            else:
                print("Invalid Choice. Please choose a valid option.")

    def approve_students(self):
        if not self.students:
            print("No students found.")
        else:
            # Display students that need approval and handle approval
            for std in self.students:
                if not std['approved']:
                    print(f"Student ID: {std['std_roll']} || Student Name: {std['std_name']}")

            for std in self.students:
                opt = input("Want to continue approving students? (Y/N): ")
                if opt.upper() == "Y":
                    std_id = input("Enter Roll no: ")
                    for std in self.students:
                        if std['std_roll'] == std_id:
                            std['approved'] = True
                            print("Student approved successfully.")

    def create_exam(self):
        # Create exam by adding questions and options
        no_of_questions = int(input("Enter the number of questions: "))
        for i in range(no_of_questions):
            question = input(f"Enter question {i+1}: ")
            options = [input(f"Option {j+1}: ") for j in range(3)]
            correct_answer = input("Correct Answer (option number): ")
            self.questions.append([question, options, correct_answer])

    def generate_report(self):
        # Display a report with student information and exam status
        print("{:<15} {:<10} {:<10} {:<10} {:<15}".format("Student Name", "Roll", "Mark", "Status", "Exam Attended"))
        print("=" * 65)
        for std in self.students:
            attended_exam = "Yes" if std["status"] else "No"
            status = "Approved" if std["approved"] else "Not Approved"
            print("{:<15} {:<10} {:<10} {:<10} {:<15}".format(std['std_name'], std['std_roll'], std['mark'], status,
                                                              attended_exam))
            print("=" * 65)

    def create_student(self):
        # Create a new student and assign a roll number
        std_name = input("Enter your Name: ")
        std_roll = str(self.roll)
        student = {'std_name': std_name, 'std_roll': std_roll, 'mark': 0, 'approved': False, 'status': False}
        self.students.append(student)
        print("Your Roll no is:", std_roll)
        self.roll += 1

    def attend_exam(self):
        # Allow a student to attend the exam and record their answers
        s_roll = input("Enter Your Roll No: ")
        mark = 0

        for std in self.students:
            if s_roll == std['std_roll'] and std['approved']:
                std['status'] = True
                print("Sign-in Successful")
                for i in self.questions:
                    print(i[0])
                    for j, option in enumerate(i[1], start=1):
                        print(f"{j}. {option}")
                    stud_answer = input("Enter Your Answer (option number): ")
                    if stud_answer == i[2]:
                        print("Correct answer!")
                        mark += 1
                    else:
                        print("Wrong Answer!")
                print("Your Mark is", mark)
                std['mark'] = mark
                break
        else:
            print("Invalid ID or Not Approved for the Exam")

    def student_report(self):
        # Display the report of a specific student based on roll number
        roll_no = input("Enter Roll No: ")
        for std in self.students:
            if std['std_roll'] == roll_no:
                print('Student Name:', std['std_name'], '|| Student Mark:', std['mark'])

# Main code
if __name__ == "__main__":
    obj = Exam()
    obj.start()
