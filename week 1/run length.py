a=input("enter:" )

result=""
count=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        count+=1
    else:
        result+=a[i-1]+str(count)
        count=1
result+=a[-1]+str(count)
print(result)