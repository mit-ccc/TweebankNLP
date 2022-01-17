# download glove.twitter.27B.100d.txt and convert the format
wget https://nlp.stanford.edu/data/glove.twitter.27B.zip
unzip glove.twitter.27B.zip -d ./data/wordvec/English

python ./data/wordvec/English/convert_vectors.py \
--source_file ./data/wordvec/English/glove.twitter.27B.100d.txt \
--dest_file ./data/wordvec/English/en.twitter100d.xz


# download saved_models
pip install gdown
gdown https://drive.google.com/drive/folders/1_LMRVFs0xpQIoSLVanof4cqsLF0Yu3JC -O ./twitter-stanza/saved_models --folder