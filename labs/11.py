numbers=[]
def remove_dup(numbers):
    i=0
    while i<len(numbers):
        j=i+1
        while j<len(numbers):
            if numbers[i]==numbers[j]:
                del numbers[j]
            elif numbers[i]!=numbers[j]:
                j=j+1
    i=i+1
print numbers
        
