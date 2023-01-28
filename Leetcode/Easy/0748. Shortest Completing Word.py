#748. Shortest Completing Word
#https://leetcode.com/problems/shortest-completing-word/description/
#first need to create hashmap from licensePlate 
#"1s3 PSt" => {s:2,p:1,t:1}
#ignore spaces and numbers; lower the chars

#iterate through the words
#   create temp_hashmap copy of the hashmap
#   iterate through word
#       decrement temp_hashmap[char] if exists
#   check if temp_hashmap doesn't have any value more than 0
#   if so Add the word to list
#check which list item is shortest and return it
#if list [] return ""

#TC - O(N+M) - N-licensePlate.len, M-words.len
#SC - O(N+M 
import sys

def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    print(licensePlate, words)
    hashmap = {}
    for i in licensePlate:
        key = i.lower()
        if key.isalpha():
            if key in hashmap:
                hashmap[key] += 1
            else:
                hashmap[key] = 1
    #print("hashmap:",hashmap)
    arr = []
    for word in words:
        #print("word:",word)
        temp_hashmap = hashmap.copy()
        for i in word:
            if i in temp_hashmap:
                temp_hashmap[i] -= 1 #decrement
        licensePlate_passed = True
        #print("temp_hashmap(updated):",temp_hashmap)
        for v in temp_hashmap.values():
            if v > 0:
                licensePlate_passed = False
        if licensePlate_passed:
            #print(word,"- added")
            arr.append(word)
    #print(arr)
    min_word_len = sys.maxsize
    min_word_index = 0
    for i in range(len(arr)):
        if len(arr[i]) < min_word_len:
            min_word_len = len(arr[i])
            min_word_index = i
    return arr[min_word_index]

licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
print(shortestCompletingWord(licensePlate, words))
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.
#temp_hashmap = hashmap.copy()


licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]
print(shortestCompletingWord(licensePlate, words))
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. 
# All the words contain 's', but among these "pest", "stew", and "show" are shortest. 
# The answer is "pest" because it is the word that appears earliest of the 3.

