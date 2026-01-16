key_location= "chair"
locations= ["garage", "bedroom","closet","chair","living room"]

for i in locations:
    if i == key_location:
        print("Key is founf in",i)
        break
    else:
        print("key is not found in", i)

 