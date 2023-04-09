#https://leetcode.com/problems/keyboard-row/description/

# check in which line first char of word is located
# and then check if other chars are located in that row
#   if char is not found in the row, skip the word
# then add word to final array
#for convenience, each letter with char should be stored in one dict
# {q:1,w:1,..a:2,s:2..z:3,x:3..}

#TC - O(N*M) - N-words.length, M-words[i].length
#SC - O(N)
def findWords(words: list[str]) -> list[str]:
    print(words)
    keyboard = {}
    for i in "qwertyuiop":
        keyboard[i] = 1
    for i in "asdfghjkl":
        keyboard[i] = 2
    for i in "zxcvbnm":
        keyboard[i] = 3
    #print(keyboard)
    #.lower()
    final = []
    for word in words:
        #print(word[0].lower() )
        fChRN = keyboard[ word[0].lower()  ] #first_char_row_number
        add_word_flag = True
        for i in word[1:]:
            if fChRN != keyboard[i.lower()]:
                add_word_flag = False
                break
        if(add_word_flag):
            final.append(word)
    return final
            
        

print(findWords(["Hello","Alaska","Dad","Peace"]))
#["Alaska","Dad"]
print(findWords(["omk"]))
#[]
        

#word[0].lower()
