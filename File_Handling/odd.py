file1=open("File_Handling/coding.txt", "r")
file2 = open('File_Handling/odd.txt', "w")
# print(file1.readlines())
lines=file1.readlines()

for i in range(len(lines)+1):
    print(lines[i-1])
    file2.write(lines[i-1])
