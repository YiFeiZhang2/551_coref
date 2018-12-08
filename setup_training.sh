#!/bin/bash

# dlx() {
#   #wget $1/$2
#   curl $1/$2 > $2
#   tar -xvzf $2
#   #rm $2
# }

# conll_url=http://conll.cemantix.org/2011/download
# dlx $conll_url conll-2011-train.v4.tar.gz
# dlx $conll_url conll-2011-development.v4.tar.gz
# dlx $conll_url/test conll-2011-test-key.tar.gz
# dlx $conll_url/test conll-2011-test-official.v9.tar.gz

# dlx $conll_url conll-2011-scripts.v3.tar.gz

# dlx http://conll.cemantix.org/download reference-coreference-scorers.v8.01.tar.gz
# mv reference-coreference-scorers conll-2011/scorer

# ontonotes_path=/projects/WebWare6/ontonotes-release-5.0

# echo "HIHIHI"

# bash conll-2011/v3/scripts/skeleton2conll.sh -D ./conll.trial/data conll-2011

# echo "HIHIHIHI!!!"

# function compile_partition() {
#     echo $3
#     echo $4
#     rm -f $2.$5.$3$4
#     cat conll-2011/$3/data/$1/data/$5/annotations/*/*/*/*.$3$4 >> $2.$5.$3$4
# }

# function compile_language() {
#     echo "The variable in 1 si"
#     echo $1
#     compile_partition development dev v4 _gold_conll $1
#     compile_partition train train v4 _gold_conll $1
#     compile_partition test test v4 _gold_conll $1
# }

# compile_language english
# compile_language chinese
# compile_language arabic

python minimize.py
python get_char_vocab.py

# echo "Just finished getting char vocab"

python filter_embeddings.py glove.840B.300d.txt train.english.jsonlines dev.english.jsonlines
python cache_elmo.py train.english.jsonlines dev.english.jsonlines
