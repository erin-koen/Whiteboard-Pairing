# input => string of opening and closing brackets
# output => boolean
# conditions => brackets must be properly nested to return True, otherwise False
# string length must be even, otherwise return false
# What is properly nested? - closing brackets must appear in the same order as opening brackets. A closing bracket for an existing open bracket is invalid if there is an existing open bracket further along in the string
# { [ ( ) ] } => True

# { [ ( ) } ] => False
# as you loop through, opening brackets are fine. As soon as you see a closing bracket, you have to confirm that it's valid. It is valid if there is an opening bracket of the same type immediately adjacent to the left, or if it's further away than one index, the indexes between the closing bracket and the unvalidated opening bracket are all valid
# so - if indexs between are valid and bracket is correct, mark index as valid and break loop
# if indexes between are valid and bracket is incorrect, return false

# { [ ( ) ( ) ] } => True
# { [ ( ] ) } => False


def opposites(bracket):
    if bracket is '(':
        return ')'
    if bracket is ')':
        return '('
    if bracket is '{':
        return '}'
    if bracket is '}':
        return '{'
    if bracket is '[':
        return ']'
    if bracket is ']':
        return '['


def balanced_brackets(input_str):
    if len(input_str) % 2 is not 0:
        return False
    valid_indices = {}
    for idx, bracket in enumerate(input_str):
        if bracket in ['}', ']', ')']:
            for i in range(idx-1, -1, -1):
                # if it's the index immediately preceding the closing bracket and it's the corresponding opening bracket, it's valid. You dno't actually need htis but it's good to help me visualize
                if i in valid_indices:
                    continue
                # else the indices between i and index are valid, and i hasn't been logged yet, and it is the right type of bracket, which means that i and index are valid. So stick them in the dictionary, break the loop, and move on
                elif i not in valid_indices and input_str[i] == opposites(bracket):
                    valid_indices[i] = True
                    valid_indices[idx] = True
                    break
                # else the indices between index and i are valid and it's not the right kind of bracket, which makes it invalid, return false
                else:
                    return False
    return True


print('THE ANSWER', balanced_brackets('[]{}()'))
print('THE ANSWER', balanced_brackets('[{[()]}]'))
print('THE ANSWER', balanced_brackets('[({}}]'))
