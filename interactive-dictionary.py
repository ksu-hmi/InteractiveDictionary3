#Import library
import json
from difflib import get_close_matches

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet

fin = open("dictionary.json", "r")
data = json.load(fin)

#Function for retriving definition
def retrive_definition(word):
    #Removing the case-sensitivity from the program
    #For example 'Rain' and 'rain' will give same output
    #Converting all letters to lower because out data is in that format
    word = word.lower()

    #Check for non existing words
    #1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
    #3rd elif: To find a similar word
    #-- len > 0 because we can print only when the word has 1 or more close matches
    #-- In the return statement, the last [0] represents the first element from the list of close matches
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        #-- If the answers is yes, retrive definition of suggested word
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
output = retrive_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
#For words having single definition
else:
    print("-",output)


#A function used to help the user find words that are three letterslong
def find_first_30_three_letter_words():
#if statement checks the length of the word
    three_letter_words = [word for word in data.keys() if len(word) == 3]
#return is going to print the output of the 1-29 words that are 3 letters 
#in length. The :is a slicer operation
    return three_letter_words[:30]
#calling the function
first_30_three_letter_words = find_first_30_three_letter_words()
#print gives us the ouput
print("First 30 three-letter words:", first_30_three_letter_words)

#defines a function named find_words_with_prefix.
def find_words_with_prefix():
#for statement goes through each word in the data dictionary, if statement
#Checks if the current word starts with the prefix "pre"
    words_with_prefix = [word for word in data.keys() if word.startswith("pre")]
#uses slicing operation to give the first 1-49 words that start with "pre"
    return words_with_prefix[:50]
#calls the function
words_with_prefix = find_words_with_prefix()
#prints the function
print("Words with the prefix 'pre' (first 50):", words_with_prefix)

#defines a function name find_words_with_synonyms():
def find_words_with_synonyms():
    words_with_synonyms = []

#starts a loop that iterates over each word in the keys of the "data" dictionary
    for word in data.keys():
        synonyms = get_close_matches(word, data.keys(), n=2, cutoff=0.8)
        if synonyms and word != synonyms[0]:
            words_with_synonyms.append(word)

    return words_with_synonyms

words_with_synonyms = find_words_with_synonyms()
print("Words with synonyms:", words_with_synonyms) 

