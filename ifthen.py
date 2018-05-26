name = input("Please enter you name: ")

print("Hello {}".format(name))

age = int(input("Please enter your age {}: ".format(name)))

if (age > 17) and (age <31):
	print("You are eligible to go on a holiday {}".format(name))
else:
	print("You are not eligible to go on a holiday {}".format(name))
