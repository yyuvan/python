with open ("Codingal.txt","w") as file :
    file.write("Hi, I am a penguin!. I am a fluffy and live in Antartica. I like to swim and slide on slow. I walk by following others in a straight line. I am 10 years old and I am mainly white, black and orange")
file.close()
with open("Codingal.txt","r") as file:
    data=file.readlines()
    for line in data:
        word = line.split()
        print("The number of lines is ", word)
file.close()