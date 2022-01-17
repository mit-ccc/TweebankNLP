# Summary

Universal Dependencies syntax annotations from the Reddit portion of the GUM corpus (https://corpling.uis.georgetown.edu/gum/) 

# Introduction

**This repository only contains annotations, without the underlying textual data from Reddit**

In order to obtain the underlying text, you will need to use the script `get_text.py`. For more information on the underlying Reddit text see [this page](https://github.com/amir-zeldes/gum/blob/master/README_reddit.md). For Universal Dependencies annotations of other genres from GUM, see https://github.com/UniversalDependencies/UD_English-GUM

GUM, the Georgetown University Multilayer corpus, is an open source collection of richly annotated texts from multiple text types. The corpus is collected and expanded by students as part of the curriculum in the course LING-367 "Computational Corpus Linguistics" at Georgetown University. The selection of text types is meant to represent different communicative purposes, while coming from sources that are readily and openly available (usually Creative Commons licenses), so that new texts can be annotated and published with ease.

The dependencies in the corpus up to GUM version 5 were originally annotated using Stanford Typed Depenencies (de Marneffe & Manning 2013) and converted automatically to UD using DepEdit (https://corpling.uis.georgetown.edu/depedit/). The rule-based conversion took into account gold entity annotations found in other annotation layers of the GUM corpus (e.g. entity annotations), and has since been corrected manually in native UD. The original conversion script used can found in the GUM build bot code from version 5, available from the (non-UD) GUM repository. Documents from version 6 of GUM onwards were annotated directly in UD, and subsequent manual error correction to all GUM data has also been done directly using the UD guidelines. Enhanced dependencies were added semi-automatically from version 7.1 of the corpus. For more details see the [corpus website](https://corpling.uis.georgetown.edu/gum/).

# Additional annotations in MISC

The MISC column contains **entity, coreference, information status, Wikification and discourse** annotations from the full GUM corpus, encoded using the annotations `Entity`, `Split`, `Bridge` and `Discourse`. 

## Entity

The `Entity` annotation uses the CoNLL 2012 shared task bracketing format, which identifies potentially coreferring entities using round opening and closing brackets as well as a unique ID per entity, repeated across mentions. In the following example, actor Jared Padalecki appears in a single token mention, labeled `(person-1-giv:act-1-coref-Jared_Padalecki)` indicating the entity type (`person`) combined with the unique ID of all mentions of Padalecki in the text (`person-1`). Because Padalecki is a named entity with a corresponding Wikipedia page, the Wikification identifier corresponding to his Wikipedia page is given after the last hyphen (`person-1-Jared_Padalecki`). We can also see an information status annotation (`giv:act`, indicating an aforementioned or 'given' entity, actively mentioned last no farther than the previous sentences; see Dipper et al. 2007), as well as minimum token ID information indicating the head tokens for fuzzy matching (in this case `1`, the first and only token  in this span) and the coreference type `coref`, indicating lexical subsequent mention. The labels for each part of the hyphen-separated annotation is given at the top of each document in a comment `# global.Entity = entity-GRP-infstat-MIN-coref_type-identity`, indicating that these annotations consist of the entity type, coreference group, information status, minimal tokens for head matching, the coreference type, and named entity identity (if available). 

Multi-token mentions receive opening brackets on the line in which they open, such as `(person-97-giv:inact-1,3-coref-Jensen_Ackles`, and a closing annotation `97)` at the token on which they end. Multiple annotations are possible for one token, corresponding to nested entities, e.g. `(time-175-giv:inact-1-coref)189)` below corresponds to the single token and last token of the time entities "2015" and "April 2015" respectively. 

```CoNLL-U
# global.Entity = entity-GRP-infstat-MIN-coref_type-identity
...
1	For	for	ADP	IN	_	4	case	4:case	Discourse=sequence_m:104->98:2
2	the	the	DET	DT	Definite=Def|PronType=Art	4	det	4:det	Bridge=173<188|Entity=(event-188-acc:inf-3,6,8-sgl
3	second	second	ADJ	JJ	Degree=Pos|NumType=Ord	4	amod	4:amod	_
4	campaign	campaign	NOUN	NN	Number=Sing	16	obl	16:obl:for	_
5	in	in	ADP	IN	_	10	case	10:case	_
6	the	the	DET	DT	Definite=Def|PronType=Art	10	det	10:det	Entity=(abstract-173-giv:inact-2,4,5-coref
7	Always	Always	ADV	NNP	Number=Sing	8	advmod	8:advmod	XML=<hi rend:::"italic">
8	Keep	Keep	PROPN	NNP	Number=Sing	10	compound	10:compound	_
9	Fighting	Fighting	PROPN	NNP	Number=Sing	8	xcomp	8:xcomp	XML=</hi>
10	series	series	NOUN	NN	Number=Sing	4	nmod	4:nmod:in	Entity=173)
11	in	in	ADP	IN	_	12	case	12:case	_
12	April	April	PROPN	NNP	Number=Sing	4	nmod	4:nmod:in	Entity=(time-189-new-1-sgl|XML=<date when:::"2015-04">
13	2015	2015	NUM	CD	NumForm=Digit|NumType=Card	12	nmod:tmod	12:nmod:tmod	Entity=(time-175-giv:inact-1-coref)189)188)|SpaceAfter=No|XML=</date>
14	,	,	PUNCT	,	_	4	punct	4:punct	_
15	Padalecki	Padalecki	PROPN	NNP	Number=Sing	16	nsubj	16:nsubj	Entity=(person-1-giv:act-1-coref-Jared_Padalecki)
16	partnered	partner	VERB	VBD	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	0:root	_
17	with	with	ADP	IN	_	18	case	18:case	_
18	co-star	co-star	NOUN	NN	Number=Sing	16	obl	16:obl:with	Entity=(person-97-giv:inact-1,3-coref-Jensen_Ackles
19	Jensen	Jensen	PROPN	NNP	Number=Sing	18	appos	18:appos	XML=<ref target:::"https://en.wikipedia.org/wiki/Jensen_Ackles">
20	Ackles	Ackles	PROPN	NNP	Number=Sing	19	flat	19:flat	Entity=97)|XML=</ref>
21	to	to	PART	TO	_	22	mark	22:mark	Discourse=purpose:105->104:0
22	release	release	VERB	VB	VerbForm=Inf	16	advcl	16:advcl:to	_
23	a	a	DET	DT	Definite=Ind|PronType=Art	24	det	24:det	Entity=(object-190-new-2-coref
24	shirt	shirt	NOUN	NN	Number=Sing	22	obj	22:obj	Entity=190)
25	featuring	feature	VERB	VBG	VerbForm=Ger	24	acl	24:acl	Discourse=elaboration:106->105:0
26	both	both	DET	DT	_	25	obj	25:obj	Entity=(object-191-new-1-sgl
27	of	of	ADP	IN	_	29	case	29:case	_
28	their	their	PRON	PRP$	Number=Plur|Person=3|Poss=Yes|PronType=Prs	29	nmod:poss	29:nmod:poss	Entity=(person-192-acc:aggr-1-coref)|Split=1<192,97<192
29	faces	face	NOUN	NNS	Number=Plur	26	nmod	26:nmod:of	Entity=191)|SpaceAfter=No
```

Possible values for the annotations mentioned above are:

  * entity type: abstract, animal, event, object, organization, person, place, plant, substance, time
  * information status 
    * new - not previously mentioned
    * giv:act - mentioned no further than one sentence ago
    * giv:inact - mentioned earlier
    * acc:inf - accessible, inferable from some previous mention (e.g. the house... [the door]) 
    * acc:aggr - accessible, aggregate, i.e. split antecedent mediated by a set of previous mentions
    * acc:com - accessible, common ground, i.e. generic ([the world]) or situationally accessible ("pass [the salt]", first mention of "you" or "I")
  * coref_type: 
    * ana - pronominal anaphora (the dancers ... [they])
    * appos - apposition (Kim, [the lawyer])
    * cata - cataphora ("In [their] speech, the athletes said", or expletive cataphora: "[it] is easy [to dance]")
    * coref - lexical coreference (e.g. [Kim] ... [Kim])
    * disc - discourse deixis, non-NP, e.g. verbal antecedent as in "[Kim arrived] - [this] delighted the children
    * pred - predication, e.g. Kim is [a teacher] (but NOT definite identification: This is Kim)
    * sgl - singleton, not mentioned again in document
  * identity: any Wikipedia article title
  * MIN: a number or set of comma-separated numbers indicating indices of minimal head tokens within the span of the mention (first in span: 1, etc.)

## Split antecedent and bridging

The annotations `Split` and `Bridge` mark non-strict identity anaphora (see the [Universal Anaphora](http://universalanaphora.org/) project for more details). For example, at token 28 in the example, the pronoun "their" refers back to two non-adjacent entities, requiring a split antecedent annotation. The value `Split=1<192,97<192` indicates that `person-192` (the pronoun "their") refers back to two previous Entity annotations, with pointers separatated by a comma: `1` (`person-1-Jared_Padalecki`) and `97` (`person-97-Jensen_Ackles`). 

Bridging anaphora is annotated when an entity has not been mentioned before, but is resolvable in context by way of a different entity: for example, token 2 has the annotation `Bridge=173<188`, which indicates that although `event-188` ("the second campaign...") has not been mentioned before, its identity is mediated by the previous mention of another entity, `abstract-173` (the project "Always Keep Fighting", mentioned earlier in the document, to which the campaign event belongs). In other words, readers can infer that "the second campaign" is part of the already introduced larger project, which also had a first campaign. This inference also leads to the information status label `acc:inf`, accessible-inferable.

## RST discourse trees

Discourse annotations are given in RST dependencies following the conversion from RST constituent trees as suggested by Li et al. (2014) - for the original RST constituent parses of GUM see the [source repo](https://github.com/amir-zeldes/gum/). At the beginning of each Elementary Discourse Unit (EDU), and annotation `Discourse` gives the discourse function of the unit beginning with that token, followed by a colon, the ID of the current unit, and an arrow pointing to the ID of the parent unit in the discourse parse. For instance, `Discourse=purpose:105->104:0` at token 21 in the example below means that this token begins discourse unit 105, which functions as a `purpose` to unit 104, which begins at token 1 in this sentence ("Padalecki partnered with co-star Jensen Ackles --purpose-> to release a shirt..."). The final `:0` indicates that the attachment has a depth of 0, without an intervening span in the original RST constituent tree (this information allows deterministic reconstruction of the RST constituent discourse tree from the conllu file). The unique `ROOT` node of the discourse tree has no arrow notation, e.g. `Discourse=ROOT:2:0` means that this token begins unit 2, which is the Central Discourse Unit (or discourse root) of the current document. Although it is easiest to recover RST constituent trees from the source repo, it is also possible to generate them automatically from the dependencies with depth information, using the scripts in the [rst2dep repo](https://github.com/amir-zeldes/rst2dep/).

Discourse relations in GUM are defined based on the effect that W (a writer/speaker) has on R (a reader/hearer) by modifying a Nucleus dicourse unit (N) with another discourse unit (a Satellite, S, or another N). Relations include:

  * Antithesis - R is meant to prefer N as an alternative to S
  * Attribution - S provides the source of information in N
  * Background - S provides information to increase R's understanding of N
  * Cause - S is the cause of N (and N is more prominent)
  * Circumstance - S details circumstances (often spatio-temporal) under which N applies
  * Concession - R is meant to look past an incompatibility of N with S
  * Condition - N occurs depending on S
  * Contrast - W presents multiple Ns as incompatible, but of equal prominence
  * Elaboration - S gives additional information about N
  * Evaluation - S provides an assessment of N by W (R does not have to share this assemssment)
  * Evidence - S provides evidence which increases R's belief in N
  * Joint - any other collection of discourse units of equal prominence at the same level of hierarchy
  * Justify - S increases R's acceptance of W's right to say N
  * Manner - S indicates the manner in which N happens
  * Means - S indicates the means by which N happens
  * Motivation - S is meant to influence R's willingness to act according to N
  * Preparation - S makes R more prepared for the appearance of N
  * Purpose - N is initiated or exists in order to realize S
  * Question - N is the answer to the question posed by S
  * Restatement - Multiple Ns realize the same role and content
  * Restatement - S partly realizes the same role and content as a previous N
  * Result - S is the result of N (or: N is the cause of S, and N is more prominent)
  * ROOT - central discourse unit of the document (not properly a discourse relation)
  * Same-unit - indicates a discontinuous discourse unit (not properly a discourse relation)
  * Sequence - Multiple Ns form a temporally ordered sequence of events in order
  * Solutionhood - N is a solution to a problem presented by S

## XML

Markup from the original XML annotations using TEI tags is available in the XML MISC annotation, which indicates which XML tags, if any, were opened or closed before or after the current token, and in what order. In tokens 7-9 in the example above, the XML annotations indicate the words "Always Keep Fighting" were originally italicized using the tag pair `<hi rend="italic">...</hi>`, which opens at token 7 and closes after token 9. To avoid confusion with the `=` sign in MISC annotations, XML `=` signs are escaped and represented as `:::`.

```CoNLL-U
7	Always	Always	ADV	NNP	Number=Sing	8	advmod	8:advmod	XML=<hi rend:::"italic">
8	Keep	Keep	PROPN	NNP	Number=Sing	10	compound	10:compound	_
9	Fighting	Fighting	PROPN	NNP	Number=Sing	8	xcomp	8:xcomp	XML=</hi>
```

XML block tags spanning whole sentences (i.e. not beginning or ending mid sentence), such as paragraphs (`<p>`) or headings (`<head>`) are instead represented using the standard UD `# newpar` comment, which may however feature nested tags, for example:

```CoNLL-U
# newpar = list type:::"unordered" (10 s) | item (4 s)
```

This comment indicates the opening of a `<list type="unordered">` block element, which spans 10 sentences (`(10 s)`). However, the list begins with a nested block, a list item (i.e. a bullet point), which spans 4 sentences, as indicated after the pipe separator. For documentation of XML elements in GUM, please see the [GUM wiki](http://corpling.uis.georgetown.edu/wiki/doku.php?id=gum:tei_markup_in_gum).

More information and additional annotation layers can also be found in the GUM [source repo](https://github.com/amir-zeldes/gum/).

# Metadata

Document metadata is given at the beginning of each new document in key-value pair comments beginning with the prefix `meta::`, as in:

```
# newdoc id = GUM_bio_padalecki
# global.Entity = entity-GRP-identity
# meta::dateCollected = 2019-09-10
# meta::dateCreated = 2004-08-14
# meta::dateModified = 2019-09-11
# meta::shortTitle = padalecki
# meta::sourceURL = https://en.wikipedia.org/wiki/Jared_Padalecki
# meta::speakerCount = 0
# meta::title = Jared Padalecki
```

# Documents and splits

The training, development and test sets contain truncated, but contiguous pages from Reddit forum discussions, in the order in which they were presented to annotators by the Reddit interface on the date of collection. For more information on thread structure and metadata, see the main GUM (non-UD) repository. Test and dev contain similar amounts of data to the other GUM genre partitions, usually around 1,800 tokens; the rest is assigned to training. For the exact file lists in each split for the Reddit genre see:

https://github.com/UniversalDependencies/UD_English-GUMReddit/tree/master/not-to-release/file-lists

# Acknowledgments

GUM annotation team (so far - thanks for participating!)

Adrienne Isaac, Akitaka Yamada, Alex Giorgioni, Alexandra Berends, Alexandra Slome, Amani Aloufi, Amelia Becker, Andrea Price, Andrew O\'Brien, Anna Runova, Anne Butler, Arianna Janoff, Ayan Mandal, Aysenur Sagdic, Bertille Baron, Bradford Salen, Brandon Tullock, Brent Laing, Candice Penelton, Chenyue Guo, Colleen Diamond, Connor O\'Dwyer, Cristina Lopez, Dan Simonson, Didem Ikizoglu, Edwin Ko, Emily Pace, Emma Manning, Ethan Beaman, Felipe De Jesus, Han Bu, Hana Altalhi, Hang Jiang, Hannah Wingett, Hanwool Choe, Hassan Munshi, Helen Dominic, Ho Fai Cheng, Hortensia Gutierrez, Jakob Prange, James Maguire, Janine Karo, Jehan al-Mahmoud, Jemm Excelle Dela Cruz, Jessica Kotfila, Joaquin Gris Roca, John Chi, Jongbong Lee, Juliet May, Jungyoon Koh, Katarina Starcevic, Katelyn MacDougald, Katherine Vadella, Khalid Alharbi, Lara Bryfonski, Leah Northington, Lindley Winchester, Linxi Zhang, Logan Peng, Lucia Donatelli, Luke Gessler, Mackenzie Gong, Margaret Borowczyk, Margaret Anne Rowe, Maria Stoianova, Mariko Uno, Mary Henderson, Maya Barzilai, Md. Jahurul Islam, Michael Kranzlein, Michaela Harrington, Minnie Annan, Mitchell Abrams, Mohammad Ali Yektaie, Naomee-Minh Nguyen, Nicholas Mararac, Nicholas Workman, Nicole Steinberg, Rachel Thorson, Rebecca Childress, Rebecca Farkas, Riley Breslin Amalfitano, Rima Elabdali, Robert Maloney, Ruizhong Li, Ryan Mannion, Ryan Murphy, Sakol Suethanapornkul, Sarah Bellavance, Sasha Slone, Sean Macavaney, Sean Simpson, Seyma Toker, Shane Quinn, Shannon Mooney, Shelby Lake, Shira Wein, Sichang Tu, Siddharth Singh, Siyu Liang, Stephanie Kramer, Sylvia Sierra, Talal Alharbi, Tatsuya Aoyama, Timothy Ingrassia, Trevor Adriaanse, Ulie Xu, Wenxi Yang, Xiaopei Wu, Yang Liu, Yi-Ju Lin, Yilun Zhu, Yingzhu Chen, Yiran Xu, Young-A Son, Yuhang Hu, Yushi Zhao, Yu-Tzu Chang, Zhuosi Luo, Zhuxin Wang, Amir Zeldes

... and other annotators who wish to remain anonymous!

## References

To cite the Reddit subset of GUM in particular, please use this citation:

* Behzad, Shabnam and Zeldes, Amir (2020) "A Cross-Genre Ensemble Approach to Robust Reddit Part of Speech Tagging". In: Proceedings of the 12th Web as Corpus Workshop (WAC-XII).

```
@InProceedings{BehzadZeldes2020,
  author    = {Shabnam Behzad and Amir Zeldes},
  title     = {A Cross-Genre Ensemble Approach to Robust {R}eddit Part of Speech Tagging},
  booktitle = {Proceedings of the 12th Web as Corpus Workshop (WAC-XII)},
  pages     = {50--56},
  year      = {2020},
}
```

As a scholarly citation for the GUM corpus as a whole, please use this article (note that this paper predates the inclusion of Reddit data in GUM):

* Zeldes, Amir (2017) "The GUM Corpus: Creating Multilayer Resources in the Classroom". Language Resources and Evaluation 51(3), 581–612.

```
@Article{Zeldes2017,
  author    = {Amir Zeldes},
  title     = {The {GUM} Corpus: Creating Multilayer Resources in the Classroom},
  journal   = {Language Resources and Evaluation},
  year      = {2017},
  volume    = {51},
  number    = {3},
  pages     = {581--612},
  doi       = {http://dx.doi.org/10.1007/s10579-016-9343-x}
}
```

# Changelog

* 2021-11-01
  * Add annotated newpar comments representing possibly nesting blocks
  * Add XML MISC attribute for XML markup in source data which does not correspond to paragraph blocks
  * Shorten Entity mention span closers in MISC
  * Add information status and coref type annotations to spans incl. discourse deixis, predicatives, singletons etc.
  * Add MIN IDs for fuzzy coref matching scores (mostly NP heads, but more for coordinations and proper names)

* 2021-09-23
  * split hyphenated tokens to match EWT tokenization, added `HYPH` xpos tag
  * added tree depth information in discourse dependencies, allowing reconstruction of RST constituents
  * added `_m` suffix to multinuclear discourse dependencies (distinguishes multinuclear and satellite restatements)

* 2021-05-01
  * Added MWTs
  * Added metadata
  * Comprehensive corrections

* 2021-03-10
  * Added enhanced dependencies

* 2021-01-20
  * Added Wikification annotations
  * Added bridging and split antecedent anaphora to MISC
  * Improved FEATS, now including Abbr and NumForm
  * Added sentence addressee annotations
  * Rebalanced splits to account for new genres in complete GUM corpus

* 2020-10-31
  * Major improvements to entity and coreference consistency
  * Removed 'quantity' entity type
  * Added discourse dependency information in MISC column
  * Moved Typo annotation from MISC to FEATS

* 2020-05-15 v2.6
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.6
License: CC BY 4.0
Includes text: no
Genre: blog social
Lemmas: manual native
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: manual native
Contributors: Peng, Siyao;Zeldes, Amir
Contributing: elsewhere
Contact: amir.zeldes@georgetown.edu
===============================================================================
</pre>
