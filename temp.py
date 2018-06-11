import pandas as pd
import random

a = "abcdefghijklmnopqrstuvwxyz"
org = []
for i in a:
    org.append(i)

array = []
for i in range(1000):
    cnt = random.randint(1,20)
    tup = random.sample(org, cnt)
    array.append(tup)

d = pd.DataFrame(data=array)
d.to_csv("temp.csv", index=False, header=False, sep=" ")
f = open("temp.csv")
res = open("random.dat", "w")

for line in f:
    context = line.rstrip()
    res.writelines(context+"\n")
res.close()
f = pd.read_csv("temp.csv", sep=" ", )
print(f)