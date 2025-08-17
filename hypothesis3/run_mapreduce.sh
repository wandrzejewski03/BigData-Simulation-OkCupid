#!/bin/bash

# Set HDFS input and output paths
INPUT=/user/hadoop/data/okcupid_clean.csv
OUTPUT=/user/hadoop/output/hypo3_children

# Remove old output if it exists
hdfs dfs -rm -r $OUTPUT

# Run Hadoop MapReduce
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
    -input $INPUT \
    -output $OUTPUT \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py

# Show output
echo "Results:"
hdfs dfs -cat $OUTPUT/part-00000