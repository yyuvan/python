file1 =open("File_Handling/coding.txt","r")
fiel2=open('File_Handling/cu.txt', 'w')
for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        fiel2.write(line)
fiel2.close()
file1.close()