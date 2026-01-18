f=open("funny.txt","r")              #with open("funn.txt","r") as f
f_out = open("funny_wc.txt","w")

for line in f:
    token = line.split(" ")
    f_out.write("wordcount:"+ str(len(token))+" "+ line)
    #print(len(token))

f.close()
f_out.close()