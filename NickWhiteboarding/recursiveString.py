'''
input => a string
output => the same string in reverse
conditions => must be recursive solution
'''


def recursive_string(str1):

    if len(str1) <= 1:
        return str1
    return str1[-1]+recursive_string(str1[:-1])

print(recursive_string('erin'))
