# TweebankNLP
[![License: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/)

This repo contains the new `Tweebank-NER` dataset and `Twitter-Stanza` pipeline for Tweet NLP.

## Tweebank-NER dataset
`Tweebank-NER V1.0` is the annotated NER dataset based on Tweebank V2, the main UD treebank for English Twitter NLP tasks.

## Installation

```
# please install from the source
pip install -e .

# download glove and pre-trained models
sh download_twitter_resources.sh
```

## Running Twitter-Stanza

### NER

We provide two pre-trained Stanza NER models:
- `en_tweenut17`: trained on `TB2+WNUT17`
- `en_tweet`: trained on `TB2`

```
source twitter-stanza/scripts/config.sh

python stanza/utils/training/run_ner.py en_tweenut17 \
--mode predict \
--score_test \
--wordvec_file ../data/wordvec/English/en.twitter100d.xz \
--eval_file data/ner/en_tweet.test.json
```

### Syntactic NLP Models

We provide two pre-trained models for the following NLP tasks:
- `tweet_ewt`: trained on `TB2+UD-English-EWT`
- `en_tweet`: trained on `TB2`

#### 1. Tokenization
```
python stanza/utils/training/run_tokenizer.py tweet_ewt \
--mode predict \
--score_test \
--txt_file data/tokenize/en_tweet.test.txt \
--label_file  data/tokenize/en_tweet-ud-test.toklabels \
--no_use_mwt 
```

#### 2. Lemmatization
```
python stanza/utils/training/run_lemma.py tweet_ewt \
--mode predict \
--score_test \
--gold_file data/depparse/en_tweet.test.gold.conllu \
--eval_file data/depparse/en_tweet.test.in.conllu 
```

#### 3. POS Tagging
```
python stanza/utils/training/run_pos.py tweet_ewt \
--mode predict \
--score_test \
--eval_file data/pos/en_tweet.test.in.conllu \
--gold_file data/depparse/en_tweet.test.gold.conllu 
```

#### 4. Dependency Parsing

``` 
python stanza/utils/training/run_depparse.py tweet_ewt \
--mode predict \
--score_test \
--wordvec_file ../data/wordvec/English/en.twitter100d.txt \
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
    publisher={arXiv},
    year={2022}
}
```

## Acknowledgement

The Twitter-Stanza pipeline is a friendly fork from the [Stanza](https://github.com/stanfordnlp/stanza) libaray with a few modifications to adapt to tweets. The repository is fully compatible with Stanza. This research project is funded by MIT Center for Constructive Communication (CCC).
