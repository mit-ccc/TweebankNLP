d = {"company": "ORG",
     "creative-work": "MISC",
     "facility": "MISC",
     "geo-loc": "LOC",
     "group": "ORG",
     "location": "LOC", 
     "movie": "MISC",
     "musicartist": "PER",
     "other": "MISC",
     "person": "PER",
     "product": "MISC",
     "sportsteam": "ORG",
     "corporation": "ORG",
     "tvshow": "MISC"} 

def map(x):
    for i,v in d.items():
        if i in x:
            return x.replace(i, v)
    return x

import json
yr = [16,17]
type = ["train","dev","test"]

for y in yr:
    for t in type:
        f = f"en_wnut{y}.{t}.json"
        print(f)
        with open(f, "r")as file:
            wnut = json.load(file)
            for sent in wnut:
                for word in sent:
                    word["ner"] = map(word["ner"])
        with open(f, "w") as file:
            json.dump(wnut,file,indent=4)
        # print(wnut[0])
