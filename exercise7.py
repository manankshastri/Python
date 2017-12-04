def list(n):                   #function to print the list
    return n

def list_reverse(n):           #function to print the reverse of a list
    n.reverse()
    return n

def list_count(n):             #function to print the length of the list
    count =0
    for i in n:
        count+=1
    return count


l = [1,2,3,10,234,4,5]
print("The list : ",list(l))
print("The list in reverse : ",list_reverse(l))
print("The length of the list : ",list_count(l))