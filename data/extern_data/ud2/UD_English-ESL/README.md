# Summary

UD English-ESL / Treebank of Learner English (TLE) contains manual POS tag and dependency annotations for 5,124 English as a Second Language (ESL) sentences drawn from the Cambridge Learner Corpus First Certificate in English (FCE) dataset.

# Introduction

UD English-ESL/TLE is a collection of 5,124 English as a Second Language (ESL) sentences (97,681 words), manually annotated with POS tags and dependency trees in the Universal Dependencies formalism. Each sentence is annotated both in its original and error corrected forms. The annotations follow the standard English UD guidelines, along with a set of supplementary guidelines for ESL. The dataset represents upper-intermediate level adult English learners from 10 native language backgrounds, with over 500 sentences for each native language. The sentences were randomly drawn from the Cambridge Learner Corpus First Certificate in English (FCE) corpus. The treebank is split randomly to a training set of 4,124 sentences, development set of 500 sentences and a test set of 500 sentences. 

A query engine and further information on the treebank is available at <esltreebank.org>.

# Obtaining the text and a treebank of error corrected sentences

Due to FCE licensing restrictions, the annotations are released without the text.

To merge the annotations with the corresponding FCE sentences, please follow these steps (require python).
1) Download the FCE dataset from <https://www.ilexir.co.uk/datasets/index.html>
to the current directory, thereby signing the FCE license agreement.
2) Unzip the downloaded file fce-released-dataset.zip.
3) Run "python merge.py" to obtain the annotation files with the FCE sentences. 

The downloaded folder will also contain a parallel treebank of error corrected sentences.

# Metadata

* sent_id = [folder_name]-[file_name]-[sent_index]: sentence identifier.
/folder_name/file_name is the path to the FCE document from which the sentence was obtained.
sent_index is the sentence number (with respect to the automatic sentence tokenization).

# Changelog

**2018-11-15 v2.3**
 - transitioned to v2 guidelines.
 - fixes to miscellaneous syntactic issues.

**2016-11-15 v1.4**
 - changed UPOS of indefinite, totality and negative pronouns from NOUN to PRON.
 - changed UPOS of demonstrative pronouns from DET to PRON.

# Acknowledgments

The dataset and the annotation guidelines were developed at MIT by Yevgeni Berzak, Jessica Kenney, Carolyn Spadine, Jing Xian Wang, Lucia Lam, Keiko Sophie Mori, Sebastian Garza, Boris Katz and Margarita Misirpashayeva.

# Citation

You are encouraged to cite the following papers when using the TLE:

    @inproceedings{berzak2016tle,
      author    = {Berzak, Yevgeni and Kenney, Jessica and Spadine, Carolyn and Wang, Jing Xian and Lam, Lucia and Mori, Keiko Sophie and Garza, Sebastian and Katz, Boris},
      title     = {Universal Dependencies for Learner English},
      booktitle = {Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
      year      = {2016},
      publisher = {Association for Computational Linguistics},
      pages     = {737--746},
      url       = {http://www.aclweb.org/anthology/P16-1070}
    }

    @inproceedings{yannakoudakis2011fce,
     title={A new dataset and method for automatically grading ESOL texts},
     author={Yannakoudakis, Helen and Briscoe, Ted and Medlock, Ben},
     booktitle={Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies-Volume 1},
     pages={180--189},
     year={2011},
     organization={Association for Computational Linguistics}
    }

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v1.3
License: CC BY-SA 4.0
Includes text: no
Genre: learner-essays
Lemmas: not available
UPOS: manual native
XPOS: manual native
Features: not available
Relations: manual native
Contributors: Berzak, Yevgeni; Kenney, Jessica; Spadine, Carolyn; Wang, Jing Xian; Lam, Lucia; Mori, Keiko Sophie; Garza, Sebastian; Katz, Boris; Misirpashayeva, Margarita;
Contributing: elsewhere
Contact: berzak@mit.edu
===============================================================================
</pre>

