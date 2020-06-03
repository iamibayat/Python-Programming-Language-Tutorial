list1 = ["Paul", "Karen", "Jeremy", "David", "Mike"]
list2 = [14, 45, 14, 12, 52]

print(list1)
print("\n")


list1.extend(list2)             # extend one list with another
print(list1)
print("\n")


list1.append("Washington")      # append new items or values at the end
print(list1)
print("\n")


list1.insert(1, "Walker")       # insert items in any place, insert(index no, item name
print(list1)
print("\n")


list1.remove("Washington")      # removes items
print(list1)
print("\n")


list1.pop()                     # pops up the last element
print(list1)
print("\n")

print (list1.index("Walker"))   # shows index number of given element
print("\n")

list1 = ["Paul", "Karen", "Paul", "Jeremy", "David", "Mike"]

print(list1.count("Paul"))      # counts number of same elements
print("\n")

list1.sort()                    # arranges in ascending order
list2.sort()
print(list1)
print(list2)
print("\n")


list1.reverse()                 # will reverse the whole list of elements
list2.reverse()
print(list1)
print(list2)
print("\n")

list3 = list1.copy()            # copies another list elements
print(list3)
print("\n")


list1.clear()                   # clears everything in the lists
print(list1)
print("\n")