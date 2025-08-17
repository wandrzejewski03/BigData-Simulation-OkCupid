#!/usr/bin/env python3
import sys
import csv

# Define structured religion keywords
structured_keywords = ['catholicism', 'christianity', 'judaism', 'buddhism', 'islam', 'hinduism']

# Define education groups
high_ed = {
    'graduated from masters program', 'graduated from ph.d program',
    'graduated from law school', 'graduated from med school',
    'working on masters program', 'working on ph.d program',
    'working on law school', 'working on med school',
    'masters program', 'ph.d program', 'law school', 'med school'
}

general_ed = {
    'graduated from college/university', 'working on college/university',
    'dropped out of college/university', 'college/university',
    'graduated from two-year college', 'working on two-year college',
    'dropped out of two-year college', 'two-year college'
}

lower_ed = {
    'graduated from high school', 'working on high school',
    'dropped out of high school', 'high school'
}

reader = csv.reader(sys.stdin)
for row in reader:
    if len(row) < 19:  # Must contain at least 19 fields
        continue

    education = row[9].strip().lower()
    religion = row[18].strip().lower()

    # Determine education group
    if education in high_ed:
        group = "higher"
    elif education in general_ed:
        group = "general"
    elif education in lower_ed:
        group = "lower"
    else:
        continue  # Skip unrecognized

    # Check if religion is structured
    is_structured = any(keyword in religion for keyword in structured_keywords)

    print(f"{group}\t{1 if is_structured else 0},1")