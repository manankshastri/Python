def set_first_elem_to_zero(l):
    l[0] = 0
    return l

j = [1,2,3,4,5]
print("Original list:                            " ,j)
print("After setting the first element to zero : ",set_first_elem_to_zero(j))
print("Now the original list becomes:            ",j)