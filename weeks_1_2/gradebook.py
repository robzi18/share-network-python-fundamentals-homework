
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = list(zip(subjects, grades))
print(gradebook)

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])
for index, entry in enumerate(gradebook):
    subject, grade = entry
    if subject == "visual arts":
        gradebook[index] = ["visual arts", grade+5]

print(gradebook)
for index, entry in enumerate(gradebook):
    subject, grade = entry
    if subject == "poetry":
        gradebook[index] = ["poetry", None]
        print("grade is removed.")

for index, entry in enumerate(gradebook):
    subject, grade = entry
    if subject == "poetry":
        gradebook[index] = ["poetry", "Pass"]
        print("Pass, result is added.")
print(gradebook)

last_semester_gradebook = [["politics", 80], [
    "latin", 96], ["dance", 97], ["architecture", 65]]

full_gradebook = gradebook + last_semester_gradebook
print(f"full gradebook is: {full_gradebook}")

print("Subject   |    Grade ")
print("---------------------")
for subject, grade in full_gradebook:
    print(f"{subject}  |    {grade}")
