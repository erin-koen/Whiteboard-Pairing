# take in an array of integers
# return an array of integers

# returned array will have the same number of indexes as the passed array. Each index in the returned array will be equal to the product of all the other indexes in the passed array. 

# O(n^2) => loop through each index in passed array, for each index, loop again through the rest of the array. If i = j, pass

def PAONUMS(arr):
    new_arr = []
    for i in arr:
        product = 1
        for j in arr:
            if j == i:
                pass
            else:
                product = product * j
        new_arr.append(product)
    return new_arr


def frontAndBack(arr):
    new_arr = [0]*len(arr)
    


print(PAONUMS([1, 7, 3, 4]))