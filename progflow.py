#Simple for loop
print("Simple for loop: \n")

for i in range(1,12):
	print("No.{:2} squared is {:3} and  cubed is {:4}".format(i,i**2,i**3))
	print("This print function is part of the for loop", i)
print("\nThis print function is outside the for loop \n\n")

#Simple if condition without input validation
print("Simple if condition without input validation: \n")

name = input("Please enter your name: ")
age = int(input("How old are you?, {0}? ".format(name)))
#print(age)
if age >= 16 and age <= 18:
	print("You are old enough to get a learner driving license")
elif age >=18:
	print("You are old enough to get a driving license")
else:
	print("You can get a learner's license in {} years".format(18 - age))


#Slightly  more complex if loop

print("\n\nSlightly  more complex if loop \n")

guess = int(input("Please enter a number between 1 and 10: "))

if guess < 5:
	guess = int(input("Please try a lower number: "))
	if guess == 5:
		print("You guessed correct")
	else:
		print("You guessed incorrect")
elif guess >5:
	guess = int(input("Please try a lower number: "))
	if guess == 5:
		print("You guessed correct")
	else:
		print("You guessed incorrect")
else:
	print("You got it right the first time")

