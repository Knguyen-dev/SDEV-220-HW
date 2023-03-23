'''
Author: Kevin Nguyen
File Name: Nguyen_Honor_Roll_App.py
Program Description: The program accepts input for students in the form of a student's first name, last name, and their gpa. Test if student has made the dean's list or honor roll if their gpa is greater than or equal to 
3.5 or 3.25 respectively, and output a message indicating so. If the student doesn't make either then still output a message to show the user the results. Let the user do enter as many student entries as they want and 
let them quit the program by typing "ZZZ".
Description of Variables Used:
- QUIT_PROCESSING_RECORDS: A string that allows the user to quit the program if they input it for last name. It's  compared to lastName, if they're the same then let the user quit the loop.
- lastName: String representing the lastName of a given student.
- firstName: String representing the firstName of a given student
- gpa: Floating point number representing the gpa of a given studnet 
'''

# Declare and initialize constant for quitting the while loop
QUIT_PROCESSING_RECORDS = "ZZZ"

# Prompt user for input of last name for user to enter the loop
lastName = input(f"Enter student's last name or '{QUIT_PROCESSING_RECORDS}' to quit: ")
while (lastName != QUIT_PROCESSING_RECORDS): # iterate while the lastName doesn't equal "ZZZ"
	# Prompt input for the rest of the student's information
	firstName = input("Enter student's first name: ") 
	gpa = float(input("Enter student's gpa: "))

	# Test if student has made the Dean's list
	if (gpa >= 3.5):
		print(f"{firstName} {lastName} has made the Dean's list")	
	# Test if student has made the honor roll 
	elif (gpa >= 3.25):
		print(f"{firstName} {lastName} has made the honor roll")
	else: # gpa < 3.25, so they don't quality for either dean's list or honor roll, so output a message saying so
		print(f"{firstName} {lastName} doesn't qualify for either Dean's list or honor roll")

	# Re-prompt input for last name to let user continue or exit the loop
	lastName = input("Enter student's last name or 'ZZZ' to quit: ")

# Output to signal the end of the program
print("Finished Processing")