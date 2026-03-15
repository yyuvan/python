with open('Repeated.txt') as fp:
    data1=fp.read()
with open('File_Handling/coding.txt') as fp:
    data2=fp.read()

data1 += "\n"
data1 += data2
print("Merging...")
with open ("Mergedfile.txt", 'w') as fp:
    fp.write(data1)