def get_grades_from_user():
    grades = []
    ask_for_grades = True  # boolean
    while ask_for_grades:  # while loop
        grade = int(input("Next grade: "))
        if grade == -1:
            ask_for_grades = False
        else:
            if (grade >= 0) and (grade <= 10):
                grades.append(grade)
            else:
                print("Please provide a grade between " + \
                      "0 and 10 (-1 to stop)")
    return grades


def compute_list_minimum(number_list):
    minimum = number_list[0]
    for number in number_list:
        if number < minimum:
            minimum = number
    return minimum


def compute_list_maximum(number_list):
    maximum = number_list[0]
    for number in number_list:
        if number > maximum:
            maximum = number
    return maximum


def compute_list_average(number_list):
    sum = 0
    for number in number_list:
        sum += number
    average = sum / len(number_list)
    return average


grades = get_grades_from_user()
if len(grades) == 0:
    print("You've not given any grade! ")
    exit()
print(grades)
print("You've given " + str(len(grades)) + " grades.")
minimum = compute_list_minimum(grades)
print(minimum)
maximum = compute_list_maximum(grades)
print(maximum)
average = compute_list_average(grades)
print(average)
print("Min:  " + str(minimum) + \
      ", Max:  " + str(maximum) + \
      ", Average:  " + str(average))