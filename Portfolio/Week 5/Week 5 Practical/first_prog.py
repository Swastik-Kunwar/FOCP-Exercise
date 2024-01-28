# user inputs a number
number = input("Enter a number: ")

#type conversion from string to int
number = int(number)

# prints the number inputed
print("The numbered entered was", number)

# checks if the remainder of the number divided by 2 is 0 or not
if (number % 2) == 0:
	#if the remainder is 0
	print("That is an even number")
else:
	# if the remainder is not 0
	print("That is an odd number")

# checks if the number is divisible by 10
if number % 10 == 0:
    print("number is divisible by 10")
