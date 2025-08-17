#!/usr/bin/env python3
import sys

# List of keywords to search for
keywords = [
    'children', 'kids', 'want kids', 'have kids', 'want children', 'have children',
    'thinking about kids', 'thinking about children', 'raising kids', 'raising children',
    'planning to have kids', 'planning to have children', 'no kids yet', 'trying for kids',
    'trying for children', 'expecting a child', 'expecting kids', 'starting a family',
    'family planning', 'parenting', 'becoming a parent', 'being a parent',
    'childfree', 'childless', 'don’t want kids', 'don’t want children', 'have a baby',
    'having a baby', 'want a baby', 'kids someday', 'someday want kids'
]

for line in sys.stdin:
    try:
        line = line.strip()
        fields = line.split(",")

        sex = fields[3].strip().lower()
        full_profile = fields[34].strip().lower()

        if sex not in ['f', 'm']:
            continue

        if any(kw in full_profile for kw in keywords):
            print(f"{sex}\t1")
    except:
        continue
