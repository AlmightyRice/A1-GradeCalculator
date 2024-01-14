# User input
Name = input("Please enter your name: ")
Programming_Assignments = float(input("Enter your Programming Assignments: "))
Midterm = float(input("Enter Midterm Percentage: "))
In_class_quizzes = float(input("Enter Quizz Percentage: "))
Lab_quizzes = float(input("Enter Lab quiz Percentage: "))
Ebook = float(input("Enter Ebook Percentage: "))
Participation = float(input("Enter Participation Percentage: "))

# course percentage
assignment_weight = 0.30
midterm_weight = .20
final_weight = .15
class_quizz_weight = .15
lab_weight = .15
Ebook_weight = .10
final_percentage = (Programming_Assignments * assignment_weight + Midterm * midterm_weight + In_class_quizzes * class_quizz_weight + Lab_quizzes * lab_weight + Ebook
* Ebook_weight)

# Compute
for final_exam_score in range(0, 101, 20):
    score = final_exam_score * .15
    print( Name + ", If your final exam score is " + str(final_exam_score) + " then your course percentage for Cs 1400 will be " + str(final_percentage))