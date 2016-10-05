#CourseGrade Assignment by Zach Mills
f = file( "CourseGrade.txt", "a" )

print "Please input the following: "
name = raw_input("Student's Name: ")
mgs = int(raw_input("Median Group Score: "))*0.14
quiz = int(raw_input("Individual Quiz Score: "))*0.14
assignment = int(raw_input("Assignment Score: "))*0.12
exam1 = int(raw_input("First Exam Score: "))*0.15
exam2 = int(raw_input("Second Exam Score: "))*0.20
final = int(raw_input("Final Exam Score: "))*0.25
grade = mgs + quiz + assignment + exam1 + exam2 + final
print name, " has a grade of ", grade
