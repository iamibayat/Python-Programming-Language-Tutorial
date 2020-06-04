'''file = open("File_Test.txt", "a")
file.write("\nToby - HR Dept.")       # the no. of times we will run this program, it will append that many times
file.close()
print("\n")'''


'''file = open("File_Test 2.txt", "w")
file.write("\nTony - HR Dept.")       # this will clear any previous data in file and override with new data
file.close()
print("\n")'''


'''file = open("File_Test 4.txt", "w")   # by writing a new file name, this will create a new text file and write
file.write("\nTony - HR Dept.")
file.close()
print("\n")'''


file = open("index.html", "w")   # by writing a new file name, this will create a new text file and write
file.write("<h1>This is a Heading</h1>")
file.write("<p1>This is a Paragraph</p1>")
file.close()
print("\n")
