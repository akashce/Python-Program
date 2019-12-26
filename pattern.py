'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
def pattern():
    for i in range(1,6):
        for j in range(i):
            print(i,end=" ")
        print("\n")

print(pattern())
