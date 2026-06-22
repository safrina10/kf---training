a=[90,78,90,76,56]
print(max(a))
print(min(a))

a=[90,78,90,76,56]

high=a[0]
low=a[0]
for i in a:
    if i>high:
        high=i
    if i<low:
        low=i
print("highmark:",high)
print("lowmark :",low)
