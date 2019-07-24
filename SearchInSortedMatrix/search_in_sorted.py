def search(target, arr):
    output = [-1, -1]
    row = 0
    column = 0

    while column < len(arr)-1:
        if arr[column][row] > target:
            for i in range(column, len(arr[row])):
                if arr[i][row-1] == target:
                    output[0] = row-1
                    output[1] = column
                    return output
        
        if row == len(arr) - 1:
            column +=1
            row = 0
        else:
            row += 1
    return output


    # for i in range(0, len(arr)):        
    #     if arr[i][column] > target:
    #         for j in range(0, len(arr[0])):
    #             if arr[i-1][j]==target:
    #                 output[0] = i-1
    #                 output[1] = j
    #     if output == [-1,-1]:
    #         for j in range(0, len(arr[0])):
    #             if arr[i-1][j]==target:
    #                     output[0] = i-1
    #                     output[1] = j
    # return output

print(search(101, [
    [1, 4, 7, 12, 15, 999], 
    [2, 5, 19, 32, 35, 1001], 
    [4, 8, 24, 34, 36, 1002], 
    [40, 41, 42, 44, 45, 1003], 
    [98, 99, 101, 104, 190, 1009], 
]))