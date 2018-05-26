IP = input("Please enter the IP address: ")
count = 0
len = 0
for char in IP:
	if char != ".":
		len += 1
	else:
		print("Length of segment {} is: {}".format(count+1,len))
		len = 0
		count += 1
print("Length of segment {} is: {}".format(count+1,len))
