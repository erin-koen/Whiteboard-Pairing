'''

Given an array of positive and negative integers, write a function to
find the contiguous sequence (in other words, a non-empty subarray of
adjacent elements) with the largest sum. Return the sum.

Sample input: [2, 3, -8, -1, 2, 4, -2, 3] </br>
Expected output: 7, from summing up the sequence 2, 4, -2, 3

Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] </br>
Expected output: 19, from summing up the sequence 1, 3, -2, 3, 4, 7, 2,
-9, 6, 3, 1

Analyze the time and space complexity of your solution.


Analyze:


'''

def LCM(arr):
    # output = []
    largest_sum = None
    current_sum = None

    for i in range (0, len(arr)-1):
        if  largest_sum is None:
            largest_sum = arr[i]
        if  arr[i] > largest_sum:
            largest_sum = arr[i]
        for j in range (i+1, len(arr)):
            if current_sum == None:
                current_sum = arr[i]+arr[j]
            else:
                current_sum += arr[j]
                print('current sum: ', current_sum)
                if current_sum > largest_sum:
                    largest_sum = current_sum            
        current_sum = None      
    
    return largest_sum
            
       
    
print(LCM([2, 3, -8, -1, 2, 4, -2, 3]))

