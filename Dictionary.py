import os, sys

#dictionary Key value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#key value pair
print(thisdict["brand"])

# get() method
#x = thisdict.get("model")
#print(x)

# # keys() method 
x = thisdict.keys()
# # values() method
y = thisdict.values()
# # items() method
z = thisdict.items()
print(x)

print(y)

print(z)

for i in z:
 print(i)
