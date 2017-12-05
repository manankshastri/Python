#function to print the list
def list(n):                   
    return n

#function to print the reverse of a list
def list_reverse(n):           
    n.reverse()
    return n

#function to print the length of the list
def list_count(n):             
    count =0
    for i in n:
        count+=1
    return count


l = [1,2,3,10,234,4,5]
print("The list : ",list(l))
print("The list in reverse : ",list_reverse(l))
print("The length of the list : ",list_count(l))
