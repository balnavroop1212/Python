student_scores = []


total_students = int(input("How many scores would you like to enter? "))


for i in range(total_students):
    score = int(input(f"Enter score #{i + 1}: "))
    student_scores.append(score)


if len(student_scores) > 0:
    max_score = student_scores[0] 
    for score in student_scores:
        if score > max_score:
            max_score = score
    
    print(f"\nThe highest score is: {max_score}")
else:
    print("No scores were entered.")
