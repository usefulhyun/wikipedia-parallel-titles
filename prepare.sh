SRC_LANG=$1
TGT_LANG=$2

DATE=20231201

for lang in $SRC_LANG $TGT_LANG
do
    wget --no-clobber https://dumps.wikimedia.org/${lang}wiki/${DATE}/${lang}wiki-${DATE}-page.sql.gz
    wget --no-clobber https://dumps.wikimedia.org/${lang}wiki/${DATE}/${lang}wiki-${DATE}-langlinks.sql.gz
done

bash build-corpus.sh $TGT_LANG ${SRC_LANG}wiki-${DATE} > wiki-titles.$SRC_LANG-$TGT_LANG
bash build-corpus.sh $SRC_LANG ${TGT_LANG}wiki-${DATE} > wiki-titles.$TGT_LANG-$SRC_LANG

python combine.py 