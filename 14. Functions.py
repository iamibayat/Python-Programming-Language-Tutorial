def says_hi():                                          # must start with def
    print("hi there!!")


says_hi()                                               # calling the function
print("\n")


print("heyy,")
says_hi()
print("how r u?")
print("\n")


def says_name(name):                                    # sending parameters
    print("My name is " + name)


says_name("Amir")
says_name("Hamza")
print("\n")


def says_name_age(name, age):                                       # sending multiple parameters
    print("My name is " + name + " and age is " + str (age))        # here we make age as string so
                                                                    # whatever value is given it will convert to string


says_name_age("Amir", "27")                                         # age parameter given in string
says_name_age("Hamza", 28)                                          # age parameter given in integer
print("\n")


age = input("Enter age: ")

def myname(age):
    name = input("Enter name: ")
    print("My name is " + name + " and age is " + age)

myname(age)