# input => square 2d matrix, a list of lists of integers
# output => square 2d matrix, a list of lists of the same integers, rotated 90deg CCW
# conditions => top row of original matrix becomes first column, second row becomes second column, etc... First column of original matrix becomes bottom row. Second column becomes second from bottom, third becomes 3rd from bottom

# Observations =>

# inner arrays are same length as outer array

# top row = array of length n at index 0 of outer array
# second row= array of length n at index 1 of outer array
# bottom row = array of length n at index[main array length - 1] of outer array
# second row from bottom = array of length n at index[main array length - 2] of outer array

# first column = index 0 of all inner arrays
# second column = index 1 of all inner arrays
# ...
# second to last column = array length - 2
# last column = array length - 1

# [          [
# [1,2,3],    [3, 6, 9]
# [4,5,6],    [2, 5, 8]
# [7,8,9]     [1, 4, 7]
# ]         ]

# coord = outer, inner (row, column)
# number   coord before    coord after
#  1            0, 0             2, 0
#  2            0, 1             1, 0
#  3            0, 2             0, 0
#  4            1, 0             2, 1
#  5            1, 1             1, 1
#  6            1, 2             0, 1
#  7            2, 0             2, 2
#  8            2, 1             1, 2
#  9            2, 2             0, 2

# for each inner array, the inner coordinate in the new format equals the outer coord in the original and does not vary per item. The outer coordinate in the new format varies per item in the inner arrays - new outer = original inner for opposite end of row array.


def rotate_image(arr):
    new_matrix = [[0]*len(arr)]*len(arr)
    print(new_matrix)

    # i = original row coordinate = new array column coordinate
    for i in range(len(arr)):
        # k = original column coordinate, referenced then incremented in inner loop, reset to zero for each row
        k = 0
        # j = new row coordinate, starts at end of array (n) and decrements with each loop
        for j in range(len(arr)-1, -1, -1):
            print(f'i: {i}, k: {k}, j: {j}, i: {i}')
            new_matrix[j][i] = arr[i][k]
            k += 1
    return new_matrix


print(rotate_image([
    [1, 1, 5, 9, 9],
    [2, 2, 6, 0, 0],
    [3, 3, 7, 1, 1],
    [4, 4, 8, 2, 2],
    [5, 5, 9, 3, 3]
]))
