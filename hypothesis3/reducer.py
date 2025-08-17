#!/usr/bin/env python3
import sys

current_key = None
total = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    value = int(value)

    if key == current_key:
        total += value
    else:
        if current_key:
            print(f"{current_key}\t{total}")
        current_key = key
        total = value

# Final key
if current_key:
    print(f"{current_key}\t{total}")
