#Import library
import json

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet

fin = open("dictionary.json", "r")
data = json.load(fin)

#Function for retriving definition
def retrive_definition(word):
    return data[word]

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))
