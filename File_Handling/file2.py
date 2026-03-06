file_write=open('ball2.txt','w')
file_write.write("File in write mode...")
file_write.write("Hi! I am Penguin. I am 1 yr. old")
file_write.close()

file_read=open('ball2.txt','r')
print("File in Read Mode -")
print(file_read.read())

file_write=open('ball2.txt','w')
file_write.write("File in write mode...")
file_write.write("Hi! I am Penguin. I am 1 yr. old")
file_write.close()


file_append = open("ball2.txt","a")

file_append.write("\n File in append mode ...")
file_append.write("Hi! I am penguin i am 1000 years old!")
file_append.close()

# file = open('ball2.txt')

# print(file.read())

# file.close()