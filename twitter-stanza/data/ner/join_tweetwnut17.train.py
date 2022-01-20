import json
from types import new_class

combined_train = []
f = f"en_4cwnut17.train.json"
with open(f, "r")as file:
    wnut = json.load(file)
    combined_train.extend(wnut)
    print(len(wnut))

with open("en_tweet.train.json", "r")as file:
    tweet = json.load(file)
    print(len(tweet))

combined_train.extend(tweet)

print(len(combined_train))

with open("en_tweetwnut17.train.json", "w") as file:
    json.dump(combined_train,file,indent=4)