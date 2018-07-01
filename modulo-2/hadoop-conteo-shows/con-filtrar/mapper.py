#!/usr/bin/env python

import sys
import re

#obteniendo filtro
filter = re.compile(sys.argv[1])

# se carga lista de bandas
file = open('shows.txt')
bands = set()
for line in file:
    band = line.strip().lower()
    bands.add(band)

file.close()

#proceso map
#por cada linea en el archivos de twitter
#se verifica si existe alguna de las bandas de la
#lista cargada previamente, si es asi se imprime
#nombre de la banda (para el reduce)
counts = {}
for line in sys.stdin:
  line = line.strip()
  fields = line.split('\t')
  nfields = len(fields)

  if nfields == 17:
    tweet_message = fields[16].lower()

    if len(filter.findall(tweet_message)) == 0:
        continue;

    for band in bands:
        if band in tweet_message:
            if band in counts:
                counts[band] = counts[band] + 1
            else:
                counts[band] = 1

for band in counts:
    print ('%s\t%s' % (band, counts[band]))
