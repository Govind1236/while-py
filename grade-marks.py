# calculate to find average marks
def average_marks(marks):
# The sum of marks = [55, 80 , 75 , 65 , 95]
    sum_marks = sum(marks)
    total_subject = len(marks)
    result_ = sum_marks / total_subject
    return result_
# calculate the grade of marks
def grade_obtain(result_):
    if result_ >= 80:
        grade = "A"
    elif result_ >= 70:
        grade = "B"
    elif result_ >= 60:
        grade = "C" 
    else:
        grade = "D"
    return grade

marks = [55, 80 , 75 , 65 , 95]
result_ = average_marks(marks)
print("The average of marks is:", result_)
grade = grade_obtain(result_)
print("The Grade of marks is:", grade)
