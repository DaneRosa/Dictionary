import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json")) #this is opening the dictionary Json
def translate(w): #defining the translate function
    w = w.lower() # this makes the w (word) into lowercase so it's readable
    if w in data: # if w(word) is in the data file as a key
        return data[w] #return the word data
    elif w.title() in data: #check if the first letter is capitalized
        return data[w.title()] #if so return the data
    elif w.upper() in data: #check if the input is in all uppercase
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: # len is just like length, get_close_matches is from difflab as well line3 
        yn = input("did you mean %s instead? Enter Y is yes N if no: " % get_close_matches(w, data.keys())[0]) # stores the value of the input in yn
        if yn == "Y": #checks
            return data[get_close_matches(w, data.keys())[0]] #returns the value within data of the cloase match you accepted
        elif yn =="N": #checks
            return "the word doesnt exist. please double check it" #return
        else:
            return "we didnt understand your query" #so wrong it cant be close
    else:
        return "Double check your word"
word = input("enter word: ") # enter your word

output = translate(word) #this calls the translate function we have created above
if type(output) == list: # if the type (builtin module) is equal to a list
    for item in output:
        print(item) #print the items of a list
else:
    print(output) 