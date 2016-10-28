# This forms an array of dictionary objects, which designate
# what could potentially be field names from a database or
# something similar.
records = [{"name":"Jones"}, {"name":"Walter"}, {"name":"Dude"}]

# This top line creates an empty array called "names"
names = []

# This for statement initializes a variable 
# called 'record' within the larger array called
# 'records', and then instructs the computer to
# iterate through each record.
for record in records:

	# The variable "name" is initialized here and 
	# designated as whatever value results from the 
	# key "name" on the dictionary object. If there
	# is anything to return, that becomes name.
    name = record["name"]

    # Prints the variable as a string to the console
    print(name)

    # Adds the variable "name" to the array "names"
    names.append(name)

# Prints the entire array "names" as a string to 
# the console.
print ("names: " + str(names))