#changes [[1,3],[3,6]] to [1,3,3,6], only works if the list is similar to list j.
def list_sep(n):
    return sum(n,[])

j = [[1,3],[3,6]]
print("Before : ",j)
print("After  : ",list_sep(j))
