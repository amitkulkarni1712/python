##TUPPLES##

#l1=["a","b","c","d"]
#l2=["x","y","z"]

#t1=(l1,l2,5,6,7,8)

#print(t1)

##### SET ###


#s1={"a","c","b",1,2,3,"a",2}


#print(s1)


s1={"a","c","b",1,2,3}
s2={"b",3,4,5,"d","e"}


s3=s1.union(s2)
print("UNION")
print(s3)

s3=s1.intersection(s2)
print("INTERSECTION")
print(s3)

s3=s1.difference(s2)
print("DIFFERENCE")


print(s3)


s3=s1^s2
print("EXOR")
print(s3)


s3=s1.discard(3)

print(s1)

### Dictionary

d1={"name":"Amit","addr":"Katraj","mob":999}

d1["addr"]="Deccan"

print(d1)


print(d1.keys())

print(d1.values())




t1=tuple(d1.keys())
print(t1)

t2=list(d1.values())
print(t2)



