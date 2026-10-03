# Create student.txt and write name and college name
file = open("student.txt", "w")

file.write("Name: Pritam\n")
file.write("College: TIMT College\n")

file.close()


# Read the content of student.txt
file = open("student.txt", "r")

print(file.read())

file.close()


# Add course name to the same file
file = open("student.txt", "a")

file.write("Course: BCA\n")

file.close()