#!/usr/bin/env python

import sys

currentWord = None
wordCount = 0
word = None

for line in sys.stdin:
    line = line.strip();
    word,count = line.split('\t',1)
    count = int(count)

    if currentWord == word:
        wordCount += int(count)
    else:
        if currentWord:
           print ('%s\t%s' % (currentWord,wordCount))
        wordCount = count
        currentWord = word

if currentWord == word:
	print ('%s\t%s' % (currentWord,wordCount))
