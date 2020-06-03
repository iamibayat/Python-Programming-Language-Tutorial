file = open("File_Test.txt", "+r")       # here r is read mode, also w as write, a as append, r+ as both read and write
print(file.writable())                   # this checks whether it is writable
print(file.readable())                   # this checks whether it is readable
print("\n")

'''print(file.read())                       # this reads whole text
print("\n")'''


'''print(file.readline())                   # this reads first line
print(file.readline())                      # this reads the line after it
print("\n")'''


# print(file.readlines())                   # this prints out all the line as a list


print(file.readlines()[2])

file.close()                                # this code closes the file after finishing working with it
