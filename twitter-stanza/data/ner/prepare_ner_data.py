import stanza.utils.datasets.ner.prepare_ner_file as prep
import json
from types import new_class

# convert tweebank-ner data from txt to json format
prep.process_dataset("../nerbase/en_tweet.train.txt","en_tweet.train.json")
prep.process_dataset("../nerbase/en_tweet.dev.txt","en_tweet.dev.json")
prep.process_dataset("../nerbase/en_tweet.test.txt","en_tweet.test.json")

# convert wnut17 from txt to json format
prep.process_dataset("../nerbase/en_wnut17.train.txt","en_wnut17.train.json")
prep.process_dataset("../nerbase/en_wnut17.dev.txt","en_wnut17.dev.json")

# convert 6 classes of WNUT17 into 4 classes used in Tweebank-NER
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

# WNUT17
yr = [17]
type = ["train","dev"]

# saved as en_wnut17.train.json and en_wnut17.dev.json
for y in yr:
    for t in type:
        f_in = f"en_wnut{y}.{t}.json"
        f_out = f"en_4cwnut{y}.{t}.json"
        with open(f_in, "r")as file:
            wnut = json.load(file)
            for sent in wnut:
                for word in sent:
                    word["ner"] = map(word["ner"])
        with open(f_out, "w") as file:
            print("Generating {}".format(f_out))
            json.dump(wnut,file,indent=4)


# combine the training data of tweebank-ner and wnut17 (4 class)
combined_train = []
f = f"en_4cwnut17.train.json"
with open(f, "r")as file:
    wnut = json.load(file)
    combined_train.extend(wnut)
    print("Number of instances in WNUT17:", f, len(wnut))

with open("en_tweet.train.json", "r")as file:
    tweet = json.load(file)
    print("Number of instances in Tweebank-NER:", len(tweet))

combined_train.extend(tweet)
print("Number of instances in combined WNUT17+Tweebank-NER:", len(combined_train))


with open("en_tweetwnut17.train.json", "w") as file:
    print("en_tweetwnut17.train.json")
    json.dump(combined_train,file,indent=4)