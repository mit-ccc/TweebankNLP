# Training Twitter-Stanza

## NER

You can specify two data setttings:
- `en_tweenut17`: trained on `TB2+WNUT17`
- `en_tweet`: trained on `TB2`

```
python stanza/utils/training/run_ner.py en_tweenut17 \
--wordvec_file ../data/wordvec/English/en.twitter100d.xz \
--eval_file data/ner/en_tweet.dev.json
```

## Syntactic NLP Models
You can specify two data settings:
- `tweet_ewt`: trained on `TB2+UD-English-EWT`
- `en_tweet`: trained on `TB2`

#### 1. Tokenizer
```
## Data Preparation
python -m stanza.utils.datasets.prepare_tokenizer_treebank tweet_ewt --no_use_mwt

## Train
python stanza/utils/training/tokenizer.py tweet_ewt --no_use_mwt
```
#### 2. Lemmatization
```
## Data Preparation
python -m stanza.utils.datasets.prepare_lemma_treebank tweet_ewt 

## Train
python stanza/utils/training/run_lemma.py tweet_ewt 
```
#### 3. POS Tagging
```
## Data Preparation
python -m stanza.utils.datasets.prepare_pos_treebank tweet_ewt 

## Train
python stanza/utils/training/run_pos.py tweet_ewt --wordvec_file ../data/wordvec/English/en.twitter100d.txt --no_pretrain
```

#### 4. Dependency Parser

```
## Data Preparation
## --gold would give you gold data. But according to conventions we did not use gold data for our depparse model
python -m stanza.utils.datasets.prepare_depparse_treebank tweet_ewt 

## Train
python -m stanza.utils.datasets.prepare_depparse_treebank tweet_ewt 
```

## Summary 

In general, we follow these steps:

### 1. Prepare the treebank
- {shorthand} should be selected from `en_tweet`, `tweet_ewt`
- {model} should be one of `tokenizer`, `lemma`, `pos`, `depparse`

```
python -m stanza.utils.datasets.prepare_{model}_treebank {shorthand} 
```

### 2. Train and evaluate on the default dev set

```
python stanza/utils/training/{model}.py {shorthand}
```

Compared to Stanza, we do not include sentence splitting, so we commented out the error check for `stanza.utils.conll18_ud_eval.UDError: There are multiple roots in a sentence`.


### 3. Evaluate on the tweetbank v2 test set
```
python stanza/utils/training/run_{model}.py {shorthand} --mode predict --score_test 
```
