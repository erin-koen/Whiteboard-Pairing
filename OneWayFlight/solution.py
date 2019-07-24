def reconstructTrip(arr):
    tripDict = {}
    returnArr = []
    # put everything in a dictionary - key = source, value = dest
    for item in arr:
        tripDict[item[0]] = item[1]
    test = tripHelper(tripDict, None, returnArr )
    return test


def tripHelper(dic, source, arr):
    if len(dic) -1 == len(arr):
        return arr
    if dic[source] is not None:        
        arr.append(dic[source])
    return tripHelper(dic, dic[source], arr)

print(reconstructTrip([
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
])
    
)