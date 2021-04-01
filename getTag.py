#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

for line in sys.stdin:
    columns = []
    for column in line.split('\t'):
        if '|' in column:
            if ';' not in column:
                column = (column.split('|')[-2])
            else:
                column = (column.split('|')[-2]).split(';')[1]
        else: column = column
        columns.append(column.strip('\n'))
    print('\t'.join(columns))