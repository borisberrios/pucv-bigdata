#!/usr/bin/env python

import sys
import re

# se carga lista de bandas
f = open('shows.txt')
bands = []
for line in f:
    band = line.strip().lower()
    bands.append(band)

#proceso map
#por cada linea en el archivos de twitter
#se verifica si existe alguna de las bandas de la
#lista cargada previamente, si es asi se imprime
#nombre de la banda (para el reduce)
for line in sys.stdin:
  line = line.strip().lower();

  fields = line.split('\t')
  nfields = len(fields)
#  print ":", line
  if nfields == 17:
    date=fields[2]
    dateFields = date.split(' ')

    for b in bands:
        #print fields[16]
        if b in fields[16]:
            print '%s %s %s\t%s' % (dateFields[1], dateFields[2], b, 1)
