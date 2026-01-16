d = {"Rinky": 9098580000, "Mohit": 8349330000, "Arti": 7354060000}

print(d["Mohit"])

d["sewaram"] = 8787909000

print(d) #order does not matter in dictionarie

del d["sewaram"]
print(d)

for key in d:
    print("key =",key,"value =",d[key])


for k, v in d.items():
    print("key =",key,"value =",v)



#checking mohit in dict or not

print("Mohit" in d)
print("snehal"in d)

d.clear()
print(d)
