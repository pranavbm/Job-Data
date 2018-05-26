number = "908,09,(2,34,fewf34,234wfwef34,/..pofvl,"
digits = "0123456789"
cleanednumber = ''
cleanednumber1 = ''
for i in range(0,len(number)):
	if  number[i] in digits:
		cleanednumber = cleanednumber + number[i]
print(cleanednumber)
for char in number:
	if char in digits:
		cleanednumber1 = cleanednumber1 + char
print(cleanednumber1)
		#print(number[i],end='')
#	print("i is now {}".format(i))
for i in range(0,101):
	if i%7 == 0:
		print(i)
list = ["A","B","C","D","E","F"]
for item in list:
	if item == "B" or item == "D":
		print("I am ignoring " + item)
		continue
	print(item)
for i in range(0,100,7):
	if i > 0 and i%11 == 0:
		print(i)
		break
	print(i)
