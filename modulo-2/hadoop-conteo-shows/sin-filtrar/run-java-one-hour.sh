#!/usr/bin/env bash

#directorio in/out
jar=showscount-0.0.3.jar
input_dir=/user/bberrios/twitter/raw_one_day/tweets_2018_05_01_00.txt
output_dir=/user/bberrios/output/twitter/raw/java-one-hour
output_java_shows=one_hour_java

#Eliminar el directori de output
hadoop fs -rm -r $output_dir

echo hadoop jar $jar showscount.ShowCount $input_dir $output_dir
hadoop jar $jar showscount.ShowCount $input_dir $output_dir
hadoop fs -cat $output_dir/* > $output_java_shows
