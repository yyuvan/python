records=[("Suranth","Maths",76),("Suresh","English",64),("Yuvan","Science",82),("Suranth","History",98),("Adam","Science",41),("Vivaan","Maths",100),("Alex","Geopraphy",68),("Suranth","Maths",76)]
print(len(records))
urecords=set(records)
print(urecords)
print(len(urecords))
f=len(records)
i=0
while i<f:
    print(records[i])
    i=i+1