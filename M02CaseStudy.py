# Joseph Basile
# M02CaseStudy.py
# App determines if student made honor roll or dean's list.

# Asks the user to enter their last name
last_name = str(input("Please enter your last name. Enter ZZZ to quit."))


# Enters the loop, only leavable by entering ZZZ.
while last_name != "ZZZ":
    # Asks for users first name and gpa
    first_name = str(input("Please enter your first name."))
    student_gpa = float(input("Please enter your GPA"))

    # if else statement to determine if user is on honor roll or dean's list.
    if student_gpa >= 3.25 and student_gpa < 3.5:
        print("Congratulations, ", first_name, last_name, " you made the Honor Roll.")
    elif student_gpa >= 3.5:
        print("Congratulations, ", first_name, last_name, " you made the Dean's List.")
    else:
        print("Sorry, ", first_name, last_name, " you did not make the Honor Roll or Dean's List.")

    # Restarts or exits the loop.
    last_name = str(input("Please enter your last name. Enter ZZZ to quit."))