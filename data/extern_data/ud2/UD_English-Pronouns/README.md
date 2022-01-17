# Summary

UD English-Pronouns is dataset created to make pronoun identification more accurate and with a more balanced distribution across genders. The dataset is initially targeting the Independent Genitive pronouns, "hers", (independent) "his", (singular) "theirs", "mine", and (singular) "yours".

# Introduction

The Independent Genitive pronoun "hers" is wrongly classified as a noun or adjective by the most widely used parsers (in October of 2019). This includes (alphabetically) Amazon Comprehend, Google Natural Language API, and the Stanford Parser. This error was traced to the data - not the algorithms themselves - and so this dataset was created to fix these errors.

## Cause of errors: missing examples and annotations

The main cause of the errors in widely used syntactic parsers is most likely because "hers" is rare in the existing datasets and completely absent from any standard test data. The pronoun "hers" only occurs three times in the entire Universal Dependencies datasets (in of October 2019). Of those three times, it is never marked with "Case=Gen", "Poss=Yes", or "PronType=Prs", which would be the correct list of morphological features (FEATS) for "hers" in any context. 

In one case of the three occurrences, "hers" was correctly annotated as "P3SG-GEN-INDEP" in the Language-specific part-of-speech tag (XPOS) field. But this field is largely ignored by general purpose syntactic parsers. 

The three examples are in the training data, so the complete absense of "hers" in the development and test data might have let this error slip under the radar. 

In general, Masculine pronouns are 4x more frequent than Feminine pronouns in the UD English datasets that have been compiled to date (October 2019). So this also contributes to the why it might have been missed. 

So, the errors are a combination of the inherent imbalance in the datasets, and by extension the sources they are drawn from, and gaps annotation to-date. There are also linguistic reasons for the gap, as outlined below.

## Inherent gender bias 

### Feminine Independent Genitive pronoun

The Feminine Dependent and Independent Genitive pronouns differ from the Masculine Genitive pronouns by having two forms, "her" and "hers", instead of using the same for both, "his". For example: "her car", "car of her**s**" / "his car", "car of his".

It is almost certain that the most popular syntactic parsers correctly identify the Masculine Independent Genitive pronoun correctly because "his" is the same form as the Dependent Genitive. 

So, while the errors result from arbitrary linguistic distinctions that are not any person's fault, they have resulted in a situation that patterns with gender bias. For example, if you are building an information extraction system that relies on pronouns to know who possesses what, it will be more accurate for information about people referred to by Masculine pronouns than by Feminine ones.

### Singular Neutral Genitive pronoun

Every instance of "they/them/their/theirs" in the existing datasets are annotated as plurals, so this also presents a potential gender bias in the data. Many individuals prefer "they/them/their/theirs" as their singular personal pronouns. So, this dataset is also targeting examples of singular "theirs". 

## Other Genitive pronouns

For comprehensiveness across the most widely used Independent Genitive Singular pronouns, "mine", and (singular) "yours" are also included. There are a very large number of additional variations of singular pronouns used in variants of English (like "ze"). Their existence is acknowledged here and the dataset can be extended to these with find-and-replace for the "they/them/their/theirs" variants in the dataset. 

## Grammatical Diversity

The Independent Genitives can occur in more syntactic contexts than any other pronoun: more than all the other pronouns combined. So, the new dataset is adding a lot more grammatical diversity to the overall Universal Dependencies dataset, too! 

## How the dataset was created and is structured

The dataset was created manually, targeting grammatical diversity. For example, there are sentences with "hers" appearing as the subject, object, indirect object, and oblique arguments; sentences with "hers" in a conjunction; sentences with "hers" in a complement clause; etc. 

The Majority sentences are completely unique in terms of their dependency tree and constituents. For the sentences that share the same dependency tree and constituent structure, they alternate an important linguistic feature in English, like regular and irregular verbs, or linguistic features that would have different syntax and/or morphology in other languages, like the locative/ablative case distinction.

The "comment" field describes exactly what grammatical structure(s) are captured in each sentence. The Independent Genitive is the most flexible pronoun, able to appear in a sentence almost anywhere any noun phrase can appear. 

A "previous" field is also added to include a viable previous sentence. Independent pronouns refer to non-syntactically local entities and those entities are typically made salient through context. It is too unnatural for the sentences to have an explicit entity that it refers to within the same sentence. So, the previous sentence should help. Here are two examples of these comments:

```
# sent_id = 20
# text = Hers accelerated.
# comment = subject to regular intransitive verb
# previous = What did Alex's car do?
...
# sent_id = 55
# text = Hers is easy to clean.
# comment = extraction/raising via "tough extraction" and clausal subject
# previous = What did the dealer like about Alex's car?
```

The "previous" sentence should also make it clear that the "theirs" and "yours" variants are unambiguously singular in this context. Many pre-trained models rely on sentence adjacency prediction, so this means that these sentence pairs can also be used for these models to held create context vector representations that are more gender balanced.

It was simply for lack of time that the previous sentences did't also get annotations in this corpus, or that the entire dataset was turned into a believable sequence: either would be good extensions! 

In version 1.0, 57 unique sentences were created with an Independent Genitive pronoun and they were copied with all pronoun alternations to make 285 total sentences with 1695 total words. Experiments to semi-automate the expansion of the dataset are ongoing.

## Files

There is only one file in the initia release, a test set:
```
en_pronouns-ud-test.conllu
```

Work to expand the dataset to be large enough to include development and training sets is ongoing. 

If you need to train on this dataset, then you can split train/test on even/odd sentences. For example, if your widely used application misses the "hers" and singular "theirs" pronouns, then it is recommended that you split the dataset 50/50 and train on the sentences with an even sentence id.


# Acknowledgments

The dataset was created by [Robert Munro](http://www.robertmunro.com) while writing [Human-in-the-Loop Machine Learning](http://bit.ly/huml_book) (Manning Publications)

Please cite this book if using this dataset.

# Changelog

* 2021-05-15 v2.8
  * Removed Case=Gen. This feature is not documented for English and not used in the other English UD treebanks.
* 2019-10-17 v1.0
  * First release in UD


# Data Statement for English Pronouns Universal Dependencies 

This is the data statement to accompany the [English Pronouns Universal Dependencies dataset](https://github.com/UniversalDependencies/UD_English-Pronouns/)

The data statements follows the structure recommended in "Data Statements for Natural Language Processing:
[Toward Mitigating System Bias and Enabling Better Science](https://techpolicylab.uw.edu/wp-content/uploads/2018/10/Data-Statements-TACL.pdf) by Emily M. Bender and Batya Friedman:

## Curation Rationale

The Independent Genitive pronoun "hers" is wrongly classified as a noun or adjective by the most widely used parsers (in October of 2019). This includes (alphabetically) Amazon Comprehend, Google Natural Language API, and the Stanford Parser. This error was traced to the data - not the algorithms themselves - and so this dataset was created to fix these errors.

## Language Variety

The dataset is in English and has examples of the five most common singular Independent Genitive pronouns "hers", "hers", "yours", "mine", "theirs". 

There is code released with the dataset that allows someone to extend the dataset programmatically to other pronouns.

## Speaker/Annotator Demographic

The dataset set is synthetic examples created and annotated by Robert Munro whose English is from Australia, UK, Sierra Leone, and the USA. 

## Speech Situation and Text Characteristics

The dataset consists of synthetic examples that aimed to maximize the diversity of linguistic contexts that  Independent Genitive pronouns can occur in: Subject, Object, Relative clauses, Conjunctions, etc. 

The examples cover a range of registers, from formal speech to informal speech.

One set of sentences were created, each with a Independent pronoun in them (like "theirs") and the other sentences were created programmatically from those original sentences and then hand-checked.



<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.5
License: CC BY-SA 4.0
Includes text: yes
Genre: grammar-examples
Lemmas: manual native
UPOS: manual native
XPOS: manual native
Features: manual native
Relations: manual native
Contributors: Munro, Robert
Contributing: elsewhere
Contact: rmunro@alumni.stanford.edu
===============================================================================
</pre>
