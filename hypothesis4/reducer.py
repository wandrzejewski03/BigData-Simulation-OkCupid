#!/usr/bin/env python3
import sys

current_group = None
structured_sum = 0
total_sum = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    group, counts = line.split('\t')
    structured, total = map(int, counts.split(','))

    if group == current_group:
        structured_sum += structured
        total_sum += total
    else:
        if current_group is not None:
            print(f"{current_group}\t{structured_sum},{total_sum}")
        current_group = group
        structured_sum = structured
        total_sum = total

# Don't forget the last one
if current_group:
    print(f"{current_group}\t{structured_sum},{total_sum}")