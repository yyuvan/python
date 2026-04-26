#Making a list
fruits=["banana","apple","strawberry","lychee","pineapple"]
# print(len(fruits))

#Appending items
fruits.append("pineapple")
# print(fruits)

#Inserting into lists
fruits.insert(3, "Orange")
# print(fruits)

# print(fruits.count("pineapple"))
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[0:3])
# print(fruits[:3])
# print(fruits[:])
# print(fruits[::-1])
# print(fruits[-1::-1])

# print(fruits[4:6])

# fruits.remove('pineapple')
# print(fruits)

# fruits.pop(1)
# print(fruits)

# fruits.reverse()
# print(fruits)

mynum=[123,32,59,38,65,928,9827]
mynum.sort()
print(mynum)


l=[34,43,33,2,["bannas","apples", "pears", "grapes",[32.0,21.1,17.8,12.5,15.7]]]
# print(len(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
print(l[4][4][0])

v=l[4]
print(v[0])

p=v[4]
print(p[0])

'''
myset={1,2,3,4,5,6,7,8,9,10,1,3,6,9,3}
myset2={2,3,45,32,78,5,34,76,2,4,245,4,88,5,24,4,24,24}

print(myset.union(myset2))
print(myset.intersection(myset2))
print(myset.difference(myset2))
print(myset.isdisjoint(myset2))











# print(myset)
# myset.add(22)
# print(myset)
# myset.add(50)
# print(myset)
# myset.update([33,43,21,43,21,443,22,43,1,3,4,5,6,7,8,31,3])
# print(myset)


# myset.remove(2)
# print(myset)

# myset.discard(20202)
# print(myset)'''

'''
mydict=dict()
print(mydict)
mydict["Yuvan"]=15
mydict["Rayan"]=15
mydict["Adam"]=14
mydict["Kaya"]=16

print(mydict)

mydict.update({"Che":14, "Mahi": 14})
print(mydict)

mydict["Yuvan"]=16
print(mydict)

mydict.clear()
print(mydict)
# print(mydict["Yuvan"])'''

'''records=[("Suranth","Maths",76),("Suresh","English",64),("Yuvan","Science",82),("Suranth","History",98),("Adam","Science",41),("Vivaan","Maths",100),("Alex","Geopraphy",68),("Suranth","Maths",76)]
print(len(records))
urecords=set(records)
print(urecords)
print(len(urecords))
f=len(records)
i=0
while i<f:
    print(records[i])
    i=i+1'''