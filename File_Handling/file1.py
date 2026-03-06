first=input("Enter the name of the first file: ")
second=input("Enter the name of the second file: ")

f1=open(f"File_Handling/{first}", "a+")
f2=open(f"File_Handling/{second}", "r")

print("Content of the first file before appending -\n", f1.read())
print("Content of the second file before appending -\n", f2.read())

f1.seek(0)
f2.seek(0)

print("Conetent of frist file after appending -\n", f1.read())

print("Conetent of second file after appending -\n", f2.read())

f1.close()
f2.close()