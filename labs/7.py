l=[4, 3, 2, 1, 1, 7, 5, 4, 4, 1, 0, 2]
def findall(l, val):
    found=[]
    for i in range(len(l)):
        if l[i]==val:
            found.append(i)
    return found
print findall(l,4)
