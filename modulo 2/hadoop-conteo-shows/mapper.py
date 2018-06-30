#!/usr/bin/env python

import sys
import re
import calendar

#fechas del mes
day_from, month_from = sys.argv[1].split("/")
day_to, month_to = sys.argv[2].split("/")

month_to = int(month_to)
day_to = int(day_to)
day_from = int(day_from)
month_from = int(month_from)


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
    date = fields[2]
    dateFields = date.split(' ')
    month = dateFields[1]
    day = int(dateFields[2])
    number_month = list(calendar.month_abbr).index(month)
    normalized_day = (number_month - 1) * 31 + day

    if ( (month_from - 1) * 31 + day_from <= normalized_day and normalized_day <= (month_to - 1) * 31 + day_to):
            for band in bands:
                if band in tweet_message:
                    print '%d %d %s\t%s' % (day, number_month, band, 1)
