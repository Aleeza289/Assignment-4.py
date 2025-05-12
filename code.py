# Question 1:
#Write a Python program that takes a person's age and categories it as:
#Child (<13)
#Teen (13–19)
#Adult (20–59)
#Senior (60+)

age= int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("senior")

# Question 2:
#Write a Python program to check if a given number is positive, negative or zero .

number = float(input("Enter the Number: "))
if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
elif number == 0:
    print("Zero")

# Question 3:
#Write a Python program to:
#Print the first and last item of a number list
#Print the number in the list

# First part of quetison number 3:
numbers = [10, 20, 30, 40, 50, 60, 70]
print("First Number:" , numbers[0])
print("Last Number:" , numbers[-1])

# Second part of question number 3:
numbers = [3, 6, 9, 12, 15]
print("Total numbers are present in the list:", len(numbers))

# Question 4:
# Write a Python program to Create a Dictionary and then update its value.
subjects = {"subject1": "math", "subject2": "english", "subjects3": "science"}
print(subjects)
subjects["subject2"] = "physics"
print (subjects)
