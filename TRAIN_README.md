# Training Twitter-Stanza

## NER

You can specify two data setttings:
- `en_tweetwnut17`: trained on `TB2+WNUT17`
- `en_tweet`: trained on `TB2`

```
shorthand=en_tweetwnut17
python stanza/utils/training/run_ner.py ${shorthand} \
--wordvec_file ../data/wordvec/English/en.twitter100d.xz \
--eval_file data/ner/en_tweet.dev.json
```

## Syntactic NLP Models
You can specify two data settings:
- `en_tweetewt`: trained on `TB2+UD-English-EWT`
- `en_tweet`: trained on `TB2`

#### 1. Tokenizer
```
## assign the shorthand name
shorthand=en_tweet

## Data Preparation
python -m stanza.utils.datasets.prepare_tokenizer_treebank ${shorthand} --no_use_mwt

## Train
python stanza/utils/training/run_tokenizer.py ${shorthand} --no_use_mwt
```
#### 2. Lemmatization
```
## assign the shorthand name
shorthand=en_tweet

## Data Preparation
python -m stanza.utils.datasets.prepare_lemma_treebank ${shorthand} 

## Train
python stanza/utils/training/run_lemma.py ${shorthand} 
```
#### 3. POS Tagging
Note that for POS and depparse, if there are a pretrained word2vec files in the target folders, Stanza will prioritize using them even if you give the --wordvec_file argument. To avoid accidentally using a wrong word2vec, remember to add --no_pretrain.
```
## assign the shorthand name
shorthand=en_tweetewt

## Data Preparation
python -m stanza.utils.datasets.prepare_pos_treebank ${shorthand} 

## Train
python stanza/utils/training/run_pos.py ${shorthand} --wordvec_file ../data/wordvec/English/en.twitter100d.xz --no_pretrain
## We didn't use a pretrained wordvec file in our training process. To specify one, use --wordvec_pretrain_file.
```

#### 4. Dependency Parser

```
## assign the shorthand name
shorthand=en_tweet

## Data Preparation
## --gold would give you gold data. But according to conventions we did not use gold data for our depparse model.
python -m stanza.utils.training.prepare_depparse_treebank ${shorthand} 

## Train
python stanza/utils/training/run_depparse.py ${shorthand} --wordvec_file ../data/wordvec/English/en.twitter100d.xz --no_pretrain 
## We didn't use pretrained word2vec file in our parser training, but the pretrain.pt generated in training the pos_tagger can be re-used here.
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
