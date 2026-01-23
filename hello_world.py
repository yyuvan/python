# Printing Commands
print("Hi, My name is Yuvan")
print("Hi, My name is Yuvan \nAnd I like videogames")
print("I am in grade: \t10")

# String and Mathematical Applications
a , b = 50, 10
print("a + b =", a+b)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", b/a)

#F allows variables in double quotes
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b={a*b}")
print(f"b/a={b/a}")

#Input in python
#String means text ( in "")

name = input("Enter your name: ")
print(type(name))

maths_score=int(input("Enter score of Math: "))
print(maths_score, type(maths_score))

science_score = int(input("Enter score of science: "))
print(science_score, type(science_score))

literacy_score = int(input("Enter score of Literacy: "))

average = (maths_score+science_score+literacy_score)/3

print(f"The average is {average}")
