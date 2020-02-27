import json
data=data.load("076 data.json")

def translate(w)
    w=w.lower()
    if w in data:
        return data[w]
    else:
        