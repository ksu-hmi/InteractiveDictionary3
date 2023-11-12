# InteractiveDictionary3
Allows users to find the meaning of a word in seconds as well aws provide word suggestion in case of a misspelling

## 1. Installing dependencies

Installing dependencies is the first thing you want to do before using Interactive Dictionary.

import json
import difflib

## 2. Understanding files in the directory

### Data
The data is in .json format. If you are not aware what JSON is and how it works I recommend referring to this [article](https://developers.squarespace.com/what-is-json/).

dictionary.json

### Step by Step Solution
I have created different files for each step in creating the interactive dictionary, here's the description of what each file does. 


dictionary_1.py

> Load the data.

dictionary_2.py

> Check for non-existing words. This ensures that the word can be found in the dictionary. Also, it make sure the word is an actual word.

dictionary_3.py

> Removing the case-sensitivity from the program. For example 'Rain' and 'rain' will give same output. Using .lower will do the same thing in python code. 

dictionary_4-1.py
dictionary_4-2.py

> Learn how 'difflib' works in order to suggest a similar word.

dictionary_5.py

> Use 'difflib' in our code to retrieve closest match

dictionary_6.py

> If the suggested word is what user wants, retrive the meaning of suggested word.

dictionary_7.py

> If the word has more than 1 definition, retrive all by iterating.

Note: All files are integrated with comments to help you understand each and every line/command of the code.

### Run All Together
Even though the dictionary_7.py is the complete file, I made a new copy of that file namely interactive_dictionary.py to serve as a final file.

python3 interactive_dictionary.py


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

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
