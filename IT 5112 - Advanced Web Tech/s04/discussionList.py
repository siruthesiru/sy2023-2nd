# I was late to the class because I got caught in traffic after going home from a previous class

# Initializing and printing a list

students = ['Bryan','Bonnie', 'Corey', 'Janice', 'Luke']
grades = [94,97,96,96,93]

# for i, j in zip(students, grades):
#     print("The grade of",str(i),"is ", str(j))

# List Manipulation
# List has methods that can be used to manipulate the elements within

programs = ["IT"]
durations = [420, 240]

# Adding lists with "append()"

programs.append('Global')

print(programs)

# Deleting items with "del"
durations.append(360)
print(durations)

del durations[-1]
print(durations)

# Checking membership with "in" (returns True if found and False if not)
print(20 in durations)
print(240 in durations)

# Sorting lists alphanumerically with "sort()" (ascending by default)
print(students)
students.sort()
print(students)

# Emptying lists with "clear()"

test_list = [1,2,3,4,5]
print(test_list)
test_list.clear()
print(test_list)