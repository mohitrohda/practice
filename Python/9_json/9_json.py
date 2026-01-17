book= {}

book["tom"] = {
    "name" : "tom",
    "adress" : "1 red street",
    "phone" : 2323232323
}

book["bob"] = {
    "name" : "bob",
    "adress" : "1 green street",
    "phone" : 9898989898
}

import json

s= json.dumps(book)
#print(s)

with open ("contacts", "w") as f:
    f.write(s)

g = open ("contacts","r")
h = g.read()
print(h)

import json

json.loads(s) # convert string to dict

print(book)

print(book["bob"])
print(book["bob"]["phone"])

for persons in book:
    print(book[persons])



