#!/usr/bin/env bash

#directorio in/out
input_dir=/user/bberrios/twitter/raw/tweets_2018_05_01_00.txt
output_dir=/user/bberrios/output/twitter/raw/sin-filtrar

#Eliminar el directori de output
hadoop fs -rm -r $output_dir

#Ejecución del mapreduce
hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-streaming-2.6.0-cdh5.14.2.jar \
-files mapper.py,reducer.py,shows.txt -mapper mapper.py \
-reducer reducer.py \
-input $input_dir \
-output $output_dir
