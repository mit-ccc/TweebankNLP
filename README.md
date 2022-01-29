# TweebankNLP
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![arXiv](https://img.shields.io/badge/arXiv-2201.07281-b31b1b.svg)](https://arxiv.org/abs/2201.07281)

This repo contains the new `Tweebank-NER` [dataset](./Tweebank-NER-v1.0) and off-the-shelf `Twitter-Stanza` pipeline for state-of-the-art Tweet NLP, as described in **[Annotating the Tweebank Corpus on Named Entity Recognition and Building NLP Models for Social Media Analysis](https://arxiv.org/abs/2201.07281)**:

- `Tweebank-NER V1.0` is the annotated NER dataset based on Tweebank V2, the main UD treebank for English Twitter NLP tasks
- the `Twitter-Stanza` pipeline provides pre-trained Tweet NLP models (NER, tokenization, lemmatization, POS tagging, dependency parsing) with state-of-the-art or competitive performance. The models are fully compatible with Stanza and provide both Python and command-line interfaces for users.  

## References

If you use this repository in your research, please kindly cite [our paper](https://arxiv.org/pdf/2201.07281.pdf) as well as the [Stanza paper](https://github.com/stanfordnlp/stanza). 

```bibtex
@article{jiang2022tweetnlp,
    title={Annotating the Tweebank Corpus on Named Entity Recognition and Building NLP Models for Social Media Analysis},
    author={Jiang, Hang and Hua, Yining and Beeferman, Doug and Roy, Deb},
    journal={arXiv preprint arXiv:2201.07281},
    year={2022}
}

@inproceedings{qi2020stanza,
    title={Stanza: A {Python} Natural Language Processing Toolkit for Many Human Languages},
    author={Qi, Peng and Zhang, Yuhao and Zhang, Yuhui and Bolton, Jason and Manning, Christopher D.},
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations",
    year={2020}
}
```



## Installation

```
# please install from the source
pip install -e ./twitter-stanza
pip install pythainlp

# download glove and pre-trained models
sh download_twitter_resources.sh
```

## Python Interface for Twitter-Stanza
Note that Stanza allows both BIO- and BIOES-schemed annotations for training/dev/test data, but for decoding the predictions, only BIOES is used. In the evaluation process, tags are merged and thus schemes do not affect the performance scores.

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

NER performance comparison among spaCy, FLAIR, and Twitter-Stanza:
| Models 	| Training data 	|  NER  (F-micro)	|
|:------:	|:-------------:	|:-----:	|
|**spaCy**|      TB2      	| 52.20 	|
|        	|   TB2+WNUT17  	| 53.89 	|
|**FLAIR**|      TB2      	| 62.12 	|
|        	|   TB2+WNUT17  	| 59.08 	|
|**Stanza**|      TB2      	| 60.14 	|
|        	|   TB2+WNUT17  	|**62.53**| 	|

```
source twitter-stanza/scripts/config.sh
cd twitter-stanza

shorthand=en_tweetwnut17
python stanza/utils/training/run_ner.py ${shorthand} \
--mode predict \
--score_test \
--wordvec_file ./data/wordvec/English/en.twitter100d.xz \
--eval_file ./data/ner/en_tweet.test.json \
--save_dir ./saved_models/ner \
--save_name ${shorthand}_nertagger.pt \
--scheme bio
```

### Syntactic NLP Models

We provide two pre-trained models for each NLP task, please specify the following shorthand:
- `en_tweetewt`: the model trained on `TB2+UD-English-EWT`
- `en_tweet`: the model trained on `TB2`

Syntactic NLP performance comparison among spaCy, FLAIR, and Twitter-Stanza:
| Models 	| Training data 	| Tokens 	| Lemmas 	|  UPOS 	|  UAS  	|  LAS  	|
|:------:	|:-------------:	|:------:	|:------:	|:-----:	|:-----:	|:-----:	|
|**spaCy**|      TB2      	|  98.57 	|   ---  	| 86.72 	| 66.93 	| 58.79 	|
|        	|    TB2+EWT    	|  95.57 	|   ---  	| 88.84 	| 72.06 	| 63.84 	|
|**FLAIR**|      TB2      	|   ---  	|  96.18 	| 87.85 	|  ---  	|  ---  	|
|        	|    TB2+EWT    	|   ---  	|  84.54 	| 88.19 	|  ---  	|  ---  	|
|**Stanza**|      TB2      	|**98.64**|**98.65**| 93.20 	| 79.28 	| 74.34 	|
|        	|    TB2+EWT    	|  98.59 	|  85.45 	|**93.53**|**82.13**|**77.82**|

#### 1. Tokenization
```
shorthand=en_tweet 
python stanza/utils/training/run_tokenizer.py ${shorthand} \
--mode predict \
--score_test \
--txt_file ./data/tokenize/en_tweet.test.txt \
--label_file  ./data/tokenize/en_tweet-ud-test.toklabels \
--no_use_mwt 
```

#### 2. Lemmatization
```
shorthand=en_tweet
python stanza/utils/training/run_lemma.py ${shorthand} \
--mode predict \
--score_test \
--gold_file ./data/lemma/en_tweet.test.gold.conllu \
--eval_file ./data/lemma/en_tweet.test.in.conllu 
```

#### 3. POS Tagging
```
shorthand=en_tweetewt
python stanza/utils/training/run_pos.py ${shorthand} \
--mode predict \
--score_test \
--eval_file ./data/pos/en_tweet.test.in.conllu \
--gold_file ./data/pos/en_tweet.test.gold.conllu \
--wordvec_file ./data/wordvec/English/en.twitter100d.xz \
--load_name ./saved_models/pos/${shorthand}_tagger.pt
```

#### 4. Dependency Parsing

``` 
shorthand=en_tweetewt
python stanza/utils/training/run_depparse.py ${shorthand} \
--mode predict \
--score_test \
--wordvec_file ./data/wordvec/English/en.twitter100d.xz \
--eval_file ./data/depparse/en_tweet.test.in.conllu \
--gold_file ./data/depparse/en_tweet.test.gold.conllu 
```

## Training Twitter-Stanza

Please refer to the [TRAIN_README.md](./TRAIN_README.md) for training the Twitter-Stanza neural pipeline.


## Acknowledgement

The Twitter-Stanza pipeline is a friendly fork from the [Stanza](https://github.com/stanfordnlp/stanza) libaray with a few modifications to adapt to tweets. The repository is fully compatible with Stanza. This research project is funded by MIT Center for Constructive Communication (CCC). This repository is mainly contributed by [Yining Hua](https://ningkko.wordpress.com/about-me/) (@ningkko) and [Hang Jiang](https://www.mit.edu/~hjian42/) (@hjian42). 
