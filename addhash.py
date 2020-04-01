#!/usr/bin/python3

# This program adds a hash of the text column to the original CSV file

# Verify integrity of loaded pickle
import debughash
dictionary,data=debughash.verifyHash(0.001)
print(len(data),'entries in csv file')
d=[]
assert "hash" not in data.columns, "hashes already exist!"
import hasher
for e in data['Text']:
    hashval=hasher.hashify(e.strip())
    assert(hashval in dictionary.keys())
    d.append(hashval)
data.insert(len(data.columns),"hash",d, True)
data.to_csv('XMLProduct_DBID_2/XMLProduct_DBID_2.csv')