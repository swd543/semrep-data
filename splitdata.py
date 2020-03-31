#!/usr/bin/python3

import pickle
import atexit
import os

# This program is used for splitting the dictionary to be processed in parallel
# 1000 entries will be split in 8 files, which will each contain 125 entries
# To fill up the data, run concurrentddossemrep.py x 8
# To combine the split data, run combiner.py
import argparse
parser = argparse.ArgumentParser(description='Super secret task.')
parser.add_argument("-n", "--numberoffiles", help="Number of files to split in", default=1, type=int)
args = parser.parse_args()

with(open('a.lock', 'w')):
    print('lock created')

@atexit.register
def goodbye():
    print('deleting lock')
    os.remove('a.lock')

import debughash
dictionary, data=debughash.verifyHash(0.001)
newDict = dict(filter(lambda e: 'semrep' not in e[1].keys(), dictionary.items()))
del(dictionary)
print(len(newDict), 'entries not yet semrepped')
import math
eachlength=math.ceil(len(newDict)/args.numberoffiles)
print(eachlength,'entries per task')

i_dump= [{} for i in range(0,args.numberoffiles)]
count=0
for f in newDict.items():
    i_dump[count%args.numberoffiles][f[0]]=f[1]
    count+=1
for i in range(0,args.numberoffiles):
    with open('parallel/{0}-dump.pkl'.format(i), 'wb') as f:
        pickle.dump(i_dump[i], f)