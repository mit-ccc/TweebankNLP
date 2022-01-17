# Summary

UD_English-ParTUT is a conversion of a multilingual parallel treebank developed at the University of Turin,
 and consisting of a variety of text genres, including talks, legal texts and Wikipedia articles, among others.


# Introduction

UD_English-ParTUT data is derived from the already-existing parallel treebank Par(allel)TUT.

ParTUT is a morpho-syntactically annotated collection of Italian/French/English parallel sentences,
which includes texts from different sources and representing different genres and domains, released in several formats.

The treebank comprises approximately 167,000 tokens, with an average amount
of 2,100 sentences per language. The texts of the collection currently available were
gathered from a large number of sources and domains:
* the [Creative Commons](http://creativecommons.org/licenses/by-nc-sa/2.0) open license;
* the [DGT-Translation Memory](https://ec.europa.eu/jrc/en/language-technologies/dgt-translation-memory)
* the [Europarl](http://www.statmt.org/europarl/) parallel corpus (section ep_00_01_17);
* publicly available pages from [Facebook website](https://www.facebook.com/help/345121355559712/);
* the [JRC-Acquis multilingual parallel corpus](http://optima.jrc.it/Acquis/index_2.2.html) (section jrc52006DC243);
* several articles from [Project Syndicate©](https://www.project-syndicate.org/) [ABSENT IN UD_French-ParTUT];
* the [Universal Declaration of Human Rights](http://www.ohchr.org/EN/UDHR/Pages/SearchByLang.aspx);
* Wikipedia articles retrieved in the English section and then translated into Italian only by graduate students in Translation  Studies [ABSENT IN UD_French-ParTUT];
* the [Web Inventory of Translated Talks](https://wit3.fbk.eu/mt.php?release=2012-02) .

ParTUT data can be downloaded [here](http://www.di.unito.it/~tutreeb/treebanks.html) and [here](https://github.com/msang/partut-repo).


# Acknowledgements
We are deeply grateful to Project Syndicate© for letting us download and exploit their articles as text material, under the terms of educational use.

## References

* Manuela Sanguinetti, Cristina Bosco. 2014. PartTUT: The Turin University Parallel Treebank.
  In Basili, Bosco, Delmonte, Moschitti, Simi (editors) Harmonization and development of resources and tools for Italian Natural Language Processing within the PARLI project, LNCS, Springer Verlag

* Manuela Sanguinetti, Cristina Bosco. 2014. Converting the parallel treebank ParTUT in Universal Stanford Dependencies.
  In Proceedings of the 1rst Conference for Italian Computational Linguistics (CLiC-it 2014), Pisa (Italy)

* Cristina Bosco, Manuela Sanguinetti. 2014. Towards a Universal Stanford Dependencies parallel treebank.
  In Proceedings of the 13th Workshop on Treebanks and Linguistic Theories (TLT-13), Tubingen (Germany)


# Corpus splitting

The corpus was randomly split using a script. In order to preserve the 1:1 correspondence among the three language sections, all of them were partitioned in the same way; therefore the same sentences, in the same order,
are found in the training, development and test set of the English and Italian treebanks as well.
However, considering that since v2.1 UD_Italian-ParTUT has been re-partitioned, because of overlapping sentences with UD_Italian, the English section of ParTUT now
appears as follows:

* en_partut-ud-train.conllu: 43518 words (1781 sentences)
* en_partut-ud-dev.conllu: 2722 words (156 sentences)
* en_partut-ud-test.conllu: 3408 words (153 sentences)


# Basic statistics

* Tree count:  2090
* Word count:  49648
* Token count: 49616
* Dep. relations: 46 of which 12 language specific
* POS tags: 17
* Category=value feature pairs: 34


## Changelog
2019-11-15 v2.5
* revised some non-projective structures

2019-05-15 v2.4
* various corrections to pass new validation

2018-11-15 v2.3
* no changes since last version

2018-04-15 v2.2
* few minor changes

2017-11-15 v2.1
* revised dates (now annotated as flat structures)
* changed xpos of copulas (from VA to V)
* other minor corrections
* revised splits, in order to align English sentences to Italian counterparts

2017-03-01 v2.0
* initial release


# Metadata

=== Machine-readable metadata ================================================
```
Data available since: UD v2.0
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: legal news wiki
Lemmas: converted with corrections
UPOS: converted with corrections
XPOS: converted with corrections
Features: converted with corrections
Relations: converted with corrections
Contributors: Bosco, Cristina; Sanguinetti, Manuela
Contributing: elsewhere
Contact: msanguin@di.unito.it
```
===============================================================================

