# input => array of strings
# output => one string
# conditions => The string that's returned is the one that shows up most frequently in the array. If there's a tie, it's the one that shows up most frequently in the array and comes last alphabetically

# sample input => input: ['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael'];
# expected output: 'michael'

# strategy: loop through array and add names to a dictionary. If name not in dictionary, dictionary[name]: 1, else dictionary[name]+=1
#this'll provide a count

# loop through dictionary, declare two variables - count and winner. If dictionary[key]:value >= count, value = count and winner = key

def counting_votes(arr):
    vote_dict = {}
    for name in arr:
        if name not in vote_dict:
            vote_dict[name] = 1
        else:
            vote_dict[name] = vote_dict[name] + 1
    
    count = 0
    winners = []
    
    # figure out the largest number of votes
    for value in vote_dict.values():
        if value > count:
            count = value
    # find the name(s) of the people who got that many votes
    for key in vote_dict.keys():
        if vote_dict[key] == count:
            winners.append(key)
    
    return sorted(winners, reverse=True)[0]
    
    
    
print(counting_votes(['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael']))