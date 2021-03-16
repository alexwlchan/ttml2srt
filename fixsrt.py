#!/usr/bin/env python3
""" Get rid of overlaps """
import sys
import csv

# We have four-line groups.
def gettext(f):
  f.readline()
  ts = f.readline()
  text = f.readline().strip()
  f.readline()
  
  return (ts, text)

outfile = open('out.csv', 'w')
writer = csv.writer(outfile)
last = ''
while True:
   (ts, t) = gettext(sys.stdin)
   if not ts:
     break
   maxover = 0
   i = 0
   while (i < len(t)):
     i += 1
     if last.endswith(t[:i]):
       maxover = i
   last = t[maxover:]
   writer.writerow((ts.split(',')[0], last))


