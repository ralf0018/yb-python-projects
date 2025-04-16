import numpy as np

# Create scores arrey
scores = np.array([[78,85,90],
                  [88,79,92],
                  [84,76,88],
                  [90,93,94],
                  [75,80,70]])

# Calculate and print the average score for each student
avg_stu = np.mean(scores, axis=1).round(2)
print(f"the average score of each student: {avg_stu}")

# Calculate and print the average score for each subject
avg_sub = np.mean(scores, axis=0).round(2)
print(f"the average score for each subject: {avg_sub}")

# Identify the student (row index) with the highest total score
# calculate total score for each student
sum = np.sum(scores,axis=1)
# find the index of student with highest score
max = np.argmax(sum)+1
print(f"student {max} has the highest total score")

# Add 5 bonus points to the third subject for all students
new_scores = scores.copy()
new_scores[:,2] += 5
print(new_scores)