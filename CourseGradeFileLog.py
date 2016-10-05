#CourseGradeFileLog Assignment by Zach Mills
filename = raw_input("Input File Name: ")
f = file( filename, "a" )

print "Please input the following: "
name = raw_input("Student's Name: ")
mgs = float(raw_input("Median Group Score: "))*0.14
quiz = float(raw_input("Individual Quiz Score: "))*0.14
assignment = float(raw_input("Assignment Score: "))*0.12
exam1 = float(raw_input("First Exam Score: "))*0.15
exam2 = float(raw_input("Second Exam Score: "))*0.20
final = float(raw_input("Final Exam Score: "))*0.25
grade = mgs + quiz + assignment + exam1 + exam2 + final

f.write("%s %.2f %.2f %.2f %.2f %.2f %.2f %.2f\n" % (name, grade, final, exam1, exam2, assignment, quiz, mgs))
f.close()

print name, " has a grade of ", grade
