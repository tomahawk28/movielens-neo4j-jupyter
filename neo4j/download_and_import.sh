#!/bin/bash
if [ -d "/data/databases/graph.db/" ]; then
	rm -rf /data/databases/graph.db/
fi

echo "Download and unzip ml-20m.zip"
mkdir -p /data/ml
wget http://files.grouplens.org/datasets/movielens/ml-20m.zip -O /data/ml/ml-20m.zip
unzip /data/ml/ml-20m.zip -d /data/ml

echo "generating users.csv based on ratings.csv"
cat /data/ml/ml-20m/ratings.csv | cut -f1 -d , | uniq > /data/ml/ml-20m/users.csv

echo "remove original header and copy to it"
for i in /data/headers/*.csv; do
	var=`cat $i`
	sed -i "1s/.*/$var/" /data/ml/ml-20m/$(basename $i)
done

neo4j-admin import --nodes:User /data/ml/ml-20m/users.csv --nodes:Movie /data/ml/ml-20m/movies.csv --relationships:Rate /data/ml/ml-20m/ratings.csv --array-delimiter "|"  --ignore-missing-nodes=true

echo "removing all temp files.."
rm -rf /data/ml
