# receives a sorted array
# take the middle item in the array, that's the root node
# create two more arrays, left and right
# middle item in each array is Root.left and root.right
# two more arrays - left and right


class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def findMid(arr):
    return len(arr)//2

def treeFromArray(arr):
    middle = findMid(arr) # middle index
    left = arr[:middle] # confirm this is exclusive
    right = arr[middle+1:] # confirm this is inclusive
    
    if len(arr) is 0:
        return
    
    root = BinaryTreeNode(arr[middle], findMid(left), findMid(right))
    return treeFromArray(left), treeFromArray(right)
    
