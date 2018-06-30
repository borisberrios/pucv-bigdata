#!/usr/bin/env bash

#directorio in/out
input_dir=/user/bberrios/twitter/raw/*
output_dir=/user/bberrios/output/twitter/raw

#Eliminar el directori de output
hadoop fs -rm -r $output_dir

#Ejecución del mapreduce
hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-streaming-2.6.0-cdh5.14.2.jar \
-files mapper.py,reducer.py,shows.txt -mapper mapper.py \
-reducer reducer.py \
-input $input_dir \
-output $output_dir


file:/home/bberrios/tareas/modulo 2/hadoop-conteo-shows/mapper.py
