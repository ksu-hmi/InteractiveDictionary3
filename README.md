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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
