# TweebankNLP
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repo contains the new `Tweebank-NER` [dataset](./Tweebank-NER-v1.0) and `Twitter-Stanza` pipeline for state-of-the-art Tweet NLP. `Tweebank-NER V1.0` is the annotated NER dataset based on Tweebank V2, the main UD treebank for English Twitter NLP tasks. The `Twitter-Stanza` pipeline provides pre-trained Tweet NLP models (NER, tokenization, lemmatization, POS tagging, dependency parsing) with state-of-the-art or competitive performance. The models are fully compatible with Stanza and provide both Python and command-line interfaces for users.  


## Installation

```
# please install from the source
pip install -e ./twitter-stanza
pip install pythainlp

# download glove and pre-trained models
sh download_twitter_resources.sh
```

## Python Interface for Twitter-Stanza

```python
import stanza

# config for the `en_tweet` models (models trained only on Tweebank)
config = {
          'processors': 'tokenize,lemma,pos,depparse,ner',
          'lang': 'en',
          'tokenize_pretokenized': True, # disable tokenization
          'tokenize_model_path': './twitter-stanza/saved_models/tokenize/en_tweet_tokenizer.pt',
          'lemma_model_path': './twitter-stanza/saved_models/lemma/en_tweet_lemmatizer.pt',
          "pos_model_path": './twitter-stanza/saved_models/pos/en_tweet_tagger.pt',
          "depparse_model_path": './twitter-stanza/saved_models/depparse/en_tweet_parser.pt',
          "ner_model_path": './twitter-stanza/saved_models/ner/en_tweet_nertagger.pt',
          "scheme": "bio"
}

# Initialize the pipeline using a configuration dict
stanza.download("en")
nlp = stanza.Pipeline(**config)
doc = nlp("Oh ikr like Messi better than Ronaldo but we all like Ronaldo more")
print(doc) # Look at the result
```

## Command-line Interface for Twitter-Stanza

### NER

We provide two pre-trained Stanza NER models:
- `en_tweetwnut17`: trained on `TB2+WNUT17`
- `en_tweet`: trained on `TB2`

```
source twitter-stanza/scripts/config.sh
cd twitter-stanza

shorthand=en_tweetwnut17
python stanza/utils/training/run_ner.py ${shorthand} \
--mode predict \
--score_test \
--wordvec_file ../data/wordvec/English/en.twitter100d.xz \
--eval_file data/ner/en_tweet.test.json \
--save_dir ./saved_models/ner \
--save_name ${shorthand}_nertagger.pt \
--scheme bio
```

### Syntactic NLP Models

We provide two pre-trained models for each NLP task, please specify the following shorthand:
- `en_tweetewt`: the model trained on `TB2+UD-English-EWT`
- `en_tweet`: the model trained on `TB2`

#### 1. Tokenization
```
shorthand=en_tweet 
python stanza/utils/training/run_tokenizer.py ${shorthand} \
--mode predict \
--score_test \
--txt_file data/tokenize/en_tweet.test.txt \
--label_file  data/tokenize/en_tweet-ud-test.toklabels \
--no_use_mwt 
```

#### 2. Lemmatization
```
shorthand=en_tweet
python stanza/utils/training/run_lemma.py ${shorthand} \
--mode predict \
--score_test \
--gold_file data/lemma/en_tweet.test.gold.conllu \
--eval_file data/lemma/en_tweet.test.in.conllu 
```

#### 3. POS Tagging
```
shorthand=en_tweetewt
python stanza/utils/training/run_pos.py ${shorthand} \
--mode predict \
--score_test \
--eval_file data/pos/en_tweet.test.in.conllu \
--gold_file data/pos/en_tweet.test.gold.conllu \
--wordvec_file ../data/wordvec/English/en.twitter100d.xz \
--load_name ./saved_models/pos/${shorthand}_tagger.pt
```

#### 4. Dependency Parsing

``` 
shorthand=en_tweetewt
python stanza/utils/training/run_depparse.py ${shorthand} \
--mode predict \
--score_test \
--wordvec_file ../data/wordvec/English/en.twitter100d.xz \
--eval_file data/depparse/en_tweet.test.in.conllu \
--gold_file data/depparse/en_tweet.test.gold.conllu 
```

## Training Twitter-Stanza

Please refer to the [TRAIN_README.md](./TRAIN_README.md) for training the Twitter-Stanza neural pipeline.

## References

If you use this repository in your research, please kindly cite our paper as well as the [Stanza papers](https://github.com/stanfordnlp/stanza). 

```bibtex
@article{jiang2022tweebank,
    title={Annotating the Tweebank Corpus on Named Entity Recognition and Building NLP Models for Social Media Analysis},
    author={Jiang, Hang and Hua, Yining and Beeferman, Doug and Roy, Deb},
    journal={arXiv preprint arXiv:2201.07281},
    year={2022}
}
```

## Acknowledgement

The Twitter-Stanza pipeline is a friendly fork from the [Stanza](https://github.com/stanfordnlp/stanza) libaray with a few modifications to adapt to tweets. The repository is fully compatible with Stanza. This research project is funded by MIT Center for Constructive Communication (CCC).
