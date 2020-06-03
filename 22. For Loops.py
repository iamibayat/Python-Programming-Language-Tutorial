# 1 
for letter in "Python Language.":
    print(letter)
print("\n")    
 
    
    
# 2 
friends = ["Noman", "Abhi", "Tanjir"]
for friend in friends:
    print(friend)
print("\n")



# 3 
friends = ["Noman", "Abhi", "Tanjir"]
for name in friends:
    print(name)
print("\n")



# 4 
for index in range(10):
    print(index)
print("\n")



# 5 
for index in range(2, 10):              # starts from 2, ends before 10
    print(index)
print("\n")



# 6 
friends = ["Noman", "Abhi", "Tanjir"]
for i in range(len(friends)):
    print(i)
print("\n")



# 7 
friends = ["Noman", "Abhi", "Tanjir"]
for i in range(len(friends)):
    print(friends[i])
print("\n")



# 8 
for i in range(5):
    if i == 0:
        print("1st loop", i)
    elif i == 4:
        print("Last loop", i)
    else:
        print(i)