# download glove.twitter.27B.100d.txt and convert the format
wget https://nlp.stanford.edu/data/glove.twitter.27B.zip
unzip glove.twitter.27B.zip -d ./twitter-stanza/data/wordvec/English
rm glove.twitter.27B.zip

python ./data/wordvec/English/convert_vectors.py \
--source_file ./twitter-stanza/data/wordvec/English/glove.twitter.27B.100d.txt \
--dest_file ./twitter-stanza/data/wordvec/English/en.twitter100d.xz

# download saved_models
wget https://ccc-hjian42.s3.amazonaws.com/public/TweebankNLP/tweebanknlp_saved_models.zip
unzip tweebanknlp_saved_models.zip -d twitter-stanza
rm tweebanknlp_saved_models.zip
