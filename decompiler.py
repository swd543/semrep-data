#!/usr/bin/python3

# This program is used for creating a CSV for each semrep output text in the dictionary
import debughash

from io import StringIO
import pandas as pd

def clean(data, seperator='|',minRows=4):
    d=pd.read_csv(StringIO(data.strip()), names=range(46), sep='|', skip_blank_lines=True, engine='python')
    to_drop=[]
    maxrowcount=0
    for index, row in d.iterrows():
        if row.count()<=minRows: to_drop.append(index)
        if row.count()>maxrowcount: maxrowcount=row.count()
    d.drop(to_drop, axis=0, inplace=True)
    d.dropna(axis=1, how='all', thresh=None, subset=None, inplace=True)
    return maxrowcount, d

import pickle
import atexit
maxrow=0


def replace(hashval, to_replace=r'{insert_hash_here}'):
    fin = open("mapping/mapmetaauto.ttl", "rt")
    data = fin.read()
    data = data.replace(to_replace, hashval)
    fin.close()
    fin = open("mapping/mapmetaauto{0}.ttl".format(hashval), "wt")
    fin.write(data)
    fin.close()

def appendtofile(ma='mapping/output/ma.nq', mb='mapping/output/mf.nq'):
    with open(mb, "a") as f:
        with open(ma, "r") as r:
            f.write(r.read())
            f.write("\n")

import os
import subprocess

def removefileifexists(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

@atexit.register
def goodbye():
    try:
        print('max cols till now',i)
        with open('lastfile.pkl'.format(i), 'wb') as f:
            pickle.dump(i, f)
    except NameError as e:
        print('Bla')
    
dictionary,data=debughash.verifyHash(0.0001)
try:
    with open('lastfile.pkl', 'rb') as f:
        lastfile=pickle.load(f)
except FileNotFoundError:
    lastfile=0
print('Last file was',lastfile)
for i,e in enumerate(dictionary.items()):

    if i<lastfile: continue    
    k=e[0]
    v=e[1]
    print(i)
    try:
        rc, d=clean(v['semrep'][0])
        d.to_csv('mapping/input/input{0}.csv'.format(k))
        replace(k)
        subprocess.run(["java","-jar","rmlmapper-4.7.0-r150.jar","-d","-m","mapping/mapmetaauto{0}.ttl".format(k),"-o","mapping/output/ma.nq"])
        appendtofile()
    except pd.errors.ParserError as e:
        print('XXXXXXXXXXX\n',v['semrep'][0].strip().encode('utf-8'))
        print(e)
        break
    except KeyError as e:
        continue
    finally:
        removefileifexists('mapping/input/input{0}.csv'.format(k))
        removefileifexists('mapping/mapmetaauto{0}.ttl'.format(k))
        
    # break