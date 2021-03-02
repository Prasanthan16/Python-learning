student_scores = input("Input a list of student heights ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0
for maximum in student_scores:
    if maximum > highest:
        highest = maximum
print(f"the highest score is,{highest}")
