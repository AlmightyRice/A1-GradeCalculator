# User input
name = input("Please enter your name: ")
Assignments = float(input( "Enter your Programming Assignments: "))
Midterm_1 = float(input("Enter Midterm 1 Percentage: "))
Midterm_2 = float(input("Enter Midterm 1 Percentage: "))
Quizzes = float(input("Enter Quizz Percentage: "))
Ebook = float(input("Enter Ebook Percentage: "))
Participation = float(input("Enter Participation Percentage: "))
# Add score
add_two = Assignments + Midterm_1
print(add_two)
print('Rae this is your score ' + str(add_two))
add_up = Assignments +Midterm_1 + Midterm_2 + Quizzes +Ebook +Participation
final_score = add_up/100
print(final_score)
print( name + " This is your final score " + str(final_score))
