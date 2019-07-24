def minJumps(arr):
    # given an array of integers, returning an integer
    # set a variable equal to the length of the array, use a while loop to increment another (index?) variable by the integer stored at that index, increment counter by 1 every time it loops
    # not sure what "if an element is zero, then we cannot move through that element" means. If we land on that element, or even if it's one we skip over?
    counter = 0
    index = 0
    length = len(arr)-1

    while index < length:
        if arr[index]==0:
            return "The calculation cannot be completed. We have landed on a 0."
        index += arr[index]
        counter +=1
    return counter

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))