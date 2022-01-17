# Summary

UD English_LinES is the English half of the LinES Parallel Treebank
with the original dependency annotation first automatically converted
into Universal Dependencies and then partially reviewed. Its contents cover
literature, an online manual and Europarl data.

# Introduction

UD English_LinES is the English half of the LinES Parallel Treebank with UD annotations.
The majority of segments are from literature but there is also a section with online manual
data and one section with Europarl data. All segments have an associated translation in the
UD Swedish_LinES treebank (with the same segment index). The original dependency annotation
was first automatically converted to Universal Dependencies and
then partially reviewed (Ahrenberg, 2015). In January-February 2017 it was converted to UD version 2
and again reviewed for errors. With version 2.1 lemma information has been added.

The treebank is being developed continuously.

# Acknowledgements

Three of the source texts were collected as part of the Linköping Translation Corpus Corpus
(Merkel, 1999). The treebank was first developed in the project 'Micro- and macro-level
analysis of translations' funded by the Swedish Research Council (Ahrenberg, 2007).

# Details on the source texts

UD English_LinES contains segments from seven different sources, three of which are
part of the Linköping Translation Corpus Corpus (Merkel, 1999). The
treebank was first developed in the project 'Micro- and macro-level
analysis of translations' funded by the Swedish Research Council (Ahrenberg, 2007).

Six of the sub-corpora are taken from literary works:

Paul Auster: City of Glass. The New York Trilogy, Volume One. First
published by Faber & Faber in 1985.

Saul Bellow: To Jerusalem and back: a personal accunt. First published
in 1976.

Joseph Conrad: Heart of darkness. First published in 1899 as a serial
in Blackwood's Magazine, in 1902 as a book.

Nadine Gordimer: A Guest of Honour. First published in 1970.

J. K. Rowling: Harry Potter and the Chamber of Secrets. First published
in 1998.

Jennette Winterson: Gut Symmetries. Granta Books, London, 1998.

In addition the corpus includes segments from Microsoft Access 2002
Online Help and the Englsh part of the Europarl corpus (v.7).

The segments have been word-aligned to the corresponding segments in the
UD Swedish_LinES treebank. Contact Lars Ahrenberg if you are interested in
obtaining the word alignments.

DATA SPLITS

The data has been split so that about 20% is used for the dev-file, 20% for the test file and the rest for training. In each file, segments from the same sub-corpus are held together. The files are named

 - en_lines-ud-test.conllu
 - en_lines-ud-dev.conllu
 - en_lines-ud-train.conllu

English_LinES and Swedish_LinES have been split the same way.


BASIC STATISTICS

Tree count: 4564
Word count: 82821
Token count: 82821
Dep. relations: 40 of which 7 language specific
POS tags: 17
Category=value feature pairs: 0

TOKENIZATION

The tokenization is largely based on whitespace, but punctuation marks
except word-internal hyphens are treated as separate tokens. The
original file also has several multi-word tokens, but these are
separated in the UD version with all parts except the first assigned
the UD dependency function 'fixed'. There are no blanks inside tokens.

MORPHOLOGY

From version 2.2 the UFEATS column is filled. The XPOS column has features from the original LinES
with the exception of nouns that are not annotated for case, only number.  Verbs are annotated for tense and,
adjectives for degree. Pronouns are sub-divided in the morphological
description into Personal, Demonstrative, Interrogative, Indefinite,
Relative, Total, and Expletive, and are annotated for Number, Person
and Case, when relevant.

The mapping from language-specific part-of-speech tags to universal tags
was done automatically. Errors have been corrected when found but
there may still be some errors remaining.


SYNTAX

The syntactic annotation was first automatically converted from the original
LinES annotation scheme as described in Ahrenberg (2015). Then converted again, mostly
automatically to UD version 2.0. The test sample has been thoroughly reviewed before
the release of version 2.1.

For version 2.2 the relative word 'that' is analysed as PRON and assigned dependency
relations from the clausal relations nsubj, obj, obl, xcomp.  Adposition introducing
clauses are assigned the relation 'mark' consistently. Unlike previous versions,
the relation 'obl:agent' is not used, instead 'obl' is used as in other English
treebanks.

There may still be occasional deviations from the general guidelines.


REFERENCES

Lars Ahrenberg, 2007. LinES: An English-Swedish Parallel
Treebank. Proceedings of the 16th Nordic Conference of Computational
Linguistics (NODALIDA, 2007).

Lars Ahrenberg, 2015. Converting an English-Swedish Parallel Treebank
to Universal Dependencies. Proceedings of the Third International
Conference on Dependency Linguistics (DepLing 2015), Uppsala, August
24-26, 2015, pp. 10-19. ACL Anthology W15-2103.

Magnus Merkel, 1999: Understanding and enhancing translation by
parallel text processing. Linköping Studies in Science and Technology,
Dissertation No. 607.


Changelog

From UD version 1.3 to UD version 2.0
 * changes of part-of-speech labels and dependency labels in accordance with 2.0 guidelines
 * addition of comments for sent_id, text, and document boundaries
 * addition of SpaceAfter=No features in the MISC column

 From UD version 2.0 to UD version 2.1
  * all tokens have received a lemma
  * the test data have been manually reviewed to correct errors and make data agree better with the version 2 guidelines.
    Changes affect about 14% of all tokens and some 36% of all punctuation tokens.

 From UD version 2.1 to UD version 2.2
  * features have been added to the UFEATS column. They have been mapped from UD_English v2.1 and then manually reviewed.
  * the word 'that' when introducing a relative clause is tagged PRON and assigned a clausal relation.
  * the train and dev data have been partially reviewed to correct errors and make data agree better with the
    version 2 guidelines.
    
 From UD version 2.2 to UD version 2.3
  * nouns with clitic 's has consistently been assigned the deprel 'nmod'
  * occurrences of deprel 'aux:pass' has been checked and applied consistently
  * compounds in the first doc of each (train, dev, test) file have been check and re-analysed to increase consistency
  * conjunctions 'either' and 'neither' which were wrongly analysed in 2.2 have been corrected

 From UD version 2.3 to UD version 2.4
  * corrections of errors flagged by the validation script
  * corrections of other errors discovered in the process
  * in particular, many changes from 'conj' to 'parataxis' when no coordinator is present
  
 From UD version 2.4 to version 2.5
  * Addition of 679 sentences from Winterson's book. 120 have been added to the dev corpus, 120 to the test corpus, and
    the rest to the train corpus.
  * correcting dependencies for punctuation marks to guarantee validation, 
  * correcting other erroneous annotation, in particular related to the parataxis and ccomp relations
  
 From UD version 2.5 to version 2.6
  * Only minor error corrections, specifically related to PronType
  
 For version 2.9: 
  * Negative adverbs consistently given UPOS PART and 
  * consistent annotation of 'with' as 'mark' when introducing a subordinate clause such as 'with the rush hour at full force'
  
--- Machine readable metadata ---

Documentation status: partial
Data source: semi-automatic
Data available since: UD v1.3
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: fiction nonfiction spoken
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: not available
Relations: converted with corrections
Contributors: Ahrenberg, Lars
Contributing: elsewhere
Contact: lars.ahrenberg@liu.se
