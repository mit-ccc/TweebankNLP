import json
from types import new_class
datasets = ["en_4cwnut16","en_4cwnut17"]
types = ["train","dev"]

combined_train = []
for t in types:
    for d in datasets:
        f = f"{d}.{t}.json"
        with open(f, "r")as file:
            wnut = json.load(file)
            combined_train.extend(wnut)
            print(len(wnut))
with open("en_tweet.train.json", "r")as file:
    tweet = json.load(file)
    print(len(tweet))

combined_train.extend(tweet)

print(len(combined_train))

with open("en_combined.train.json", "w") as file:
    json.dump(combined_train,file,indent=4)