a=[90,78,90,76,56]
dup=0
for i in a:
    if i not in dup and a.count(i)==1:
        dup.append(i)
print("duplicates",dup)    

a=[90,80,70,80,90]
dup=[]
seen=[]
for i in a:
    if i in seen:
        dup.append(i)
    else:
        seen.append(i)
print("duplictaes",dup)
print("seenn",seen)