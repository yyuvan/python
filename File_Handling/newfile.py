# newfile=open("new_file.txt","x")
# newfile.close()

import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("File does not exist")


my_file=open("my_file.txt","w")
my_file.write("Hi, I am a penguin!.")
my_file.close()
os.remove('test.txt')
os.rmdir('File_Handling/ok')