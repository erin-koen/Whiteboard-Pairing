# input => array of integers
# output => number of non-zero integers array of the same integers, with all 0s at the end of the array
# loop through the array - if an item = zero, append it to a new array of zeros
# else append it to a new array of non-zeros
# return non zeros + zeros in a new array

def zeros_to_right(arr):
    zeros = []
    non_zeros = []
    for item in arr:
        if item == 0:
            zeros.append(item)
        else: 
            non_zeros.append(item)
    return len(non_zeros)

print(zeros_to_right([0, 3, 1, 0, -2]))
print(zeros_to_right([4, 2, 1, 5]))