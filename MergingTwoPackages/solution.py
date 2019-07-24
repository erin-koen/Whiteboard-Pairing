def merge(arr, limit):
    hash = {}
    for idx, item in enumerate(arr):
        hash[item]=idx
    print(hash)
    for idx, item in enumerate(arr):
        diff = limit - item
        if diff in hash:
            if idx >= hash[diff]:
                return [idx, hash[diff]]
            else:
                return [hash[diff], idx]
       
    return []

print(merge([4, 6, 10, 15, 16], 21))