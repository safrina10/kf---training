'''
5
54
543
5432
54321
'''
for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j,end="")
    print()