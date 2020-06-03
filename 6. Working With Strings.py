# string is just a plain text

print("This is a python tutorial.")

print("\n")

# \n character creates a new line
print("This is a \npython tutorial.")

print("\n")

# if we want to print out a quotation mark inside string, we use \"
print("This is a \"python tutorial\". ")

print("\n")

# we can create a string variable
var = "Python"
print(var)

print("\n")

# Concatination
print(var + " is a cool language.")

print("\n")

# FUNCTIONS
var2 = "Python Language"
var3 = "CODING"
print(var2.lower())                         # this will make all the character lower case
print(var2.upper())                         # this will make all the character upper case

print("\n")

print(var2.isupper())
print(var2.islower())
print(var3.isupper())

print("\n")

# MULTIPLE FUNCTIONS
print(var2.upper().isupper())               # it at first made var2 Upper case then run test is it upper or not

print("\n")

print(len(var2))                            # this will find the length of characters
print(len(var2) + len(var3))

print("\n")

print(var2[0])                              # finding an index number from a character
print(var2[7])
print(var2.index("L"))                      # finding a character
print(var2.index("Language"))               # finding a start of a character

print("\n")

print(var2.replace("Python","Java"))        # this function will replace a character with another one