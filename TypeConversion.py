birth_year = input("What's your birth year? ")
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print("So, you are ",age)

#Excercise: Ask for user their weight in pound and print their weight in terminal in kg
weight = input("What's your weight, brit?")
weight = float(weight) * 0.453
print("Your weight is ", weight , " kg")