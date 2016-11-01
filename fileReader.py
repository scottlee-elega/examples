# This is an example of a script that will print
# each line in a text file. The 'r' represents
# that we are doing a read operation as opposed to
# say, a write. 'open' is a built in Python function
# for this process. 
with open('FileReaderData.txt', 'r') as file:
    read_data = file.read()
    print(read_data)