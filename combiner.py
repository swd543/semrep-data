#!/usr/bin/python3

# This program is used for combining the split-processed semrep dictionary into one big dictionary
import pickle
import os
import debughash

dictionary,_=debughash.verifyHash(0.001,'temp/hashdump.pkl')
print(len(dictionary), 'entries should be present in total')
for filename in os.listdir('parallel'):
    if not filename.endswith(".pkl"): continue
    lildictionary,_=debughash.verifyHash(0.001,'parallel/{0}'.format(filename))
    print(len(lildictionary),'total entries')
    newDict = dict(filter(lambda e: 'semrep' in e[1].keys(), lildictionary.items()))
    print(len(newDict),'are semrepped')
    print(next(iter(newDict.items())))
    for key, value in newDict.items():
        assert key in dictionary.keys()
        dictionary[key]['semrep']=value['semrep']

import shutil
shutil.copyfile('temp/hashdump.pkl', 'temp/hashdump2.pkl')
with open('temp/hashdump.pkl', 'wb') as f:
    pickle.dump(dictionary, f)

newDict = dict(filter(lambda e: 'semrep' in e[1].keys(), dictionary.items()))
a=len(newDict)
b=len(dictionary)
print(a,'/',b,'done',a*100/b,'%')