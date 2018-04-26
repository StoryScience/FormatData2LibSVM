#!/usr/bin/python3
import os
import sys
import pandas as pd

para1 = str(sys.argv[1])
para2 = int(sys.argv[2])

file = para1
if para2 == 0:
    delimiter = ' '
elif para2 == 1:
    delimiter = '\t'
elif para2 == 2:
    delimiter = ','
else:
    print('please input 0/1/2 as the parameter.')
    sys.exit()

# file = 'test_data'
# delimiter = '\t'

file_name = os.path.splitext(file)[0]
file_suffix = os.path.splitext(file)[1]
df = pd.read_csv(file, sep=delimiter, header=None)

column_num = df.columns.size
if column_num == 1:
    print('delimiter is wrong!')
else:
    for i in range(column_num-1):
        df[i] = str(i+1)+':'+df[i].astype('str')
    column_name = df.columns.tolist()
    column_name = column_name[-1:] + column_name[:-1]
    df = df[column_name]
    df.to_csv(file_name+'_formated'+file_suffix, sep=delimiter, header=None, index=None)
    print('file was formated!')
