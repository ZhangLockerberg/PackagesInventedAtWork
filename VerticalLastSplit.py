#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

for line in sys.stdin:
    columns = []
    for i, column in enumerate(line.split('\t')):
        if '|' in column and i == 0:
            column = column.split("|")[-2]
        else: column = column
        columns.append(column.strip('\n'))
    print('\t'.join(columns))