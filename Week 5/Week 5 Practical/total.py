# Imports sys module
import sys

# The length of the argument is assigned to count variable
count = len(sys.argv)
# Initializing total variable to 0
total = 0
# Initializing lenth variable to 0
length = 0

# Checks if the length of argument is greater than 1
if len(sys.argv) > 1:
    # A while loop that ends when count is less than 1
    while count > 1:
	    # Count deceases by 1
	    count -= 1
	    # The total variable has a conversion of the string argument to float and adds the total to it
	    total += float(sys.argv[count])
	    # The length is increased by 1 every iteration
	    length += 1
    # Prints the total
    print("Total is", total)
    # Prints the Average
    print("Average is", total/length)

# if the length is less than 1
else:
    print("no arguments were provided")