# download glove.twitter.27B.100d.txt and convert the format
wget https://nlp.stanford.edu/data/glove.twitter.27B.zip
unzip glove.twitter.27B.zip -d ./data/wordvec/English
rm glove.twitter.27B.zip

python ./data/wordvec/English/convert_vectors.py \
--source_file ./data/wordvec/English/glove.twitter.27B.100d.txt \
--dest_file ./data/wordvec/English/en.twitter100d.xz

# download saved_models
wget https://lsm-data.s3.amazonaws.com/ccc-hang/TweebankNLP/tweebanknlp_saved_models.zip
unzip tweebanknlp_saved_models.zip -d twitter-stanza
rm tweebanknlp_saved_models.zip