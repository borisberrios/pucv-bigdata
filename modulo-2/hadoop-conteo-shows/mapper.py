#!/usr/bin/env python

import sys
import re

# se carga lista de bandas
file = open('shows.txt')
bands = set()
for line in file:
    band = line.strip().lower()
    bands.add(band)

#proceso map
#por cada linea en el archivos de twitter
#se verifica si existe alguna de las bandas de la
#lista cargada previamente, si es asi se imprime
#nombre de la banda (para el reduce)
for line in sys.stdin:
  line = line.strip()
  fields = line.split('\t')
  nfields = len(fields)

  if nfields == 17:
    tweet_message = fields[16].lower()

    for band in bands:
        if band in tweet_message:
            print '%s\t%s' % (band, 1)
