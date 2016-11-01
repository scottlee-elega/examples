# This file will demonstrate naming objects in a sequence, 
# particularly giving them a prefix and then assigning 
# them a number, which requires some tricks.

# Initially, designate a prefix, which will be a part of
# an object's naming convention.
objectNamePrefix = "Object"

# Initialize a starting number. For numbers, we always use
# their actual values instead of wrapping them in quotes the
# way we did with the word, or STRING, above.

# In the below example, we start at zero
startingNumber = 0

# Performs a loop from a range of 1 through to 10
for object in range(1, 10):

	# Increment the startingNumber variable up by 1.
	# The first time this is done, it takes the number
	# from 0 to 1. Next time, 1 to 2, and so on.
	startingNumber += 1

	# The startingNumberAsString variable will convert this
	# whole number, an int data type (or representing an 
	# integer), to a string so that it can be printed back
	# to the console in the ending print function call.
	startingNumberAsString = str(startingNumber)

	# An object name variable will combine the prefix with
	# the actual number.
	objectName = objectNamePrefix + startingNumberAsString

	# Print the combined strings to the console.
	print (objectName)


# The console output will then look something like:
# Object1
# Object2
# Object3
# Object4
# Object5
# Object6
# Object7
# Object8
# Object9