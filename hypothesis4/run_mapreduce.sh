#!/bin/bash

INPUT=/user/hadoop/data/okcupid_clean.csv
OUTPUT=/user/hadoop/output/hypo4_religion

hdfs dfs -rm -r $OUTPUT

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
    -input $INPUT \
    -output $OUTPUT \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py

hdfs dfs -cat $OUTPUT/part-00000
