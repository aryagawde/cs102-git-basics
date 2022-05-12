# Hangman Game - try?
# Rough structure



def position(word: str, letter: str) -> list:
    # determining the position of a particular letter in a word, especially if more than one occurrence 

    list_word = []
    for index in range(0, len(word), 1):
        if word[index] == letter:
            list_word.append(index)
    return list_word

def replace_string(list_str: list, letter: str) -> str:
    newVar = position(word, letter)
    for i in newVar:
        list_str[i] = letter
    final_res = " ".join(list_str)
    return final_res

def win(string: str, actual_word: str) -> bool:
    newWord = list(actual_word)
    x = " ".join(newWord)
    return x == string
    
print("Welcome to the Hangman Game!")
print("In this game, you need to guess the word individually by identifying its letters.")
print("You will have (number of letters)+2 chances to prove your mettle at the game.")
print("All the best!!")

word = "interview"
list_empty_word = list((str("_")) * len(word))
empty_space_word = str(("_ ")*len(word))
counter = len(word)+2

print("WORD: ", empty_space_word)
print("You have", counter, "chances to guess the letters.")

for attempt in range(1, counter + 1, 1):
    letter = str(input("Enter a letter to guess:"))
    counter -= 1
    res = replace_string(list_empty_word, letter)
    print(res)
    if win(res, word):
        print("Congratulations, you won!")
        break
    else:
        print("You have", counter, "chances left!")   
