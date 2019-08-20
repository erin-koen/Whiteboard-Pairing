wordlist1 = ['APPLE', 'PLEAS', 'PLEASE']

puzzles1 = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPXY', 'XAELPSY']

# Input => two lists of strings, wordlist and puzzles
# Output => a list of integers, equal in length to the list of puzzles
# Conditions => integers in the returned list will represent how many words in the word list can be spelled using the letters in each respective puzzle. i.e. return[0] = number of words in the wordlist that can be spelled using the letters in puzzles[0]
# bonus condition => if the first letter in the puzzle is not in a word, it's an automatic fail for that word

# word = apple
# puzzle = AELPXYZ



# loop through apple: 
# letter || present in puzzle || toggle boolean
#   a           yes                     no 
#   p           yes                     no
#   p           yes                     no
#   l           yes                     no
#   e           yes                     no
# boolean not toggled, increment count for puzzle[index], move to next word

# loop through pleas:
# letter || present in puzzle || toggle boolean
#   p           yes                     no
#   l           yes                     no
#   e           yes                     no
#   a           yes                     no
#   s           no                      yes
# boolean toggled, do not increment count, move to next word

# loop through please:
# letter || present in puzzle || toggle boolean
#   p           yes                     no
#   l           yes                     no
#   e           yes                     no
#   a           yes                     no
#   s           no                      yes
# boolean toggled, do not increment count, move to next word



def spelling_bee(wordlist, puzzles):
    #instantiate a two list of sets, one set for each word in the first list and one set for each letter in the second list
    word_sets = []
    puzzle_sets = []
    return_list = [0]*(len(puzzles))

    # O(n^2) fill the sets with letters for each word and puzzle
    for idx, word in enumerate(wordlist):
        word_sets.append(set())
        for letter in word:
            word_sets[idx].add(letter)
    
    for idx, puzzle in enumerate(puzzles):
        puzzle_sets.append(set())
        for letter in puzzle:
            puzzle_sets[idx].add(letter)
    
    for idx, puzzle in enumerate(puzzle_sets): #O(n)
        count = 0
        for word in word_sets: # O(n)
            if word.issubset(puzzle): # O(n)
                count +=1

        return_list[idx] = count

    # bonus condition - check the first letter of each puzzle against each word set, if not in any of them, the return_list[idx] = 0

    for idx, puzzle, in enumerate(puzzles): # O(n)
        for word in word_sets: # O(n)
            if puzzle[0] not in word:
                return_list[idx] -= 1

    return return_list        



    


print(spelling_bee(wordlist1, puzzles1))
    