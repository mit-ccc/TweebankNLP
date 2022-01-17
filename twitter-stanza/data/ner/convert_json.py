import stanza.utils.datasets.ner.prepare_ner_file as prep
prep.process_dataset("en_tweet.train.txt","en_tweet.train.json")
prep.process_dataset("en_tweet.dev.txt","en_tweet.dev.json")
prep.process_dataset("en_tweet.test.txt","en_tweet.test.json")

# prep.process_dataset("en-ewt.train.txt","en-ewt.train.json")
# prep.process_dataset("en-ewt.dev.txt","en-ewt.dev.json")
# prep.process_dataset("en-ewt.test.txt","en-ewt.test.json")

# prep.process_dataset("en_wnut16.train.txt","en_wnut16.train.json")
# prep.process_dataset("en_wnut16.dev.txt","en_wnut16.dev.json")
# prep.process_dataset("en_wnut16.test.txt","en_wnut16.test.json")

# prep.process_dataset("en_wnut17.train.txt","en_wnut17.train.json")
# prep.process_dataset("en_wnut17.dev.txt","en_wnut17.dev.json")
# prep.process_dataset("en_wnut17.test.txt","en_wnut17.test.json")