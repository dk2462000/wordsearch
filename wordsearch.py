import json
from difflib import get_close_matches
data=json.load("data.json")

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
            ys=input("did you mean %s instead of enter y if prediction is correct else N") % get_close_matches(w,data.keys())[0]
            if ys=="y":           
                return data[w]
            
            elif ys=="n":
                print("we couldn't understand the word")
            
            else:
                print("there is no such word")
    else:
        print("there is no such word")                

word=input("enter word")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
