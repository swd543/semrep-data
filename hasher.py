#!/usr/bin/python3

import pandas as pd
data=pd.read_csv('XMLProduct_DBID_2/XMLProduct_DBID_2.csv')
# print(data)
# print(data.columns)
# print(data['Text'][100])

import hashlib

def hashify(entry):
    hash_object = hashlib.md5(entry.encode('utf-8'))
    hash=hash_object.hexdigest()
    return hash


if __name__ == "__main__":
    dictionary_of_unique_text_entries={}
    for d in data.iterrows():
        # hash the text
        text=d[1]['Text'].strip()
        index=d[0]
        hash_object = hashlib.md5(text.encode('utf-8'))
        hash=hash_object.hexdigest()
        if hash not in dictionary_of_unique_text_entries.keys(): 
            dictionary_of_unique_text_entries[hash]={'size':0, 'rowIndex':[]}
        dictionary_of_unique_text_entries[hash]['rowIndex'].append(index)
        dictionary_of_unique_text_entries[hash]['size']=len(text)
    print(dictionary_of_unique_text_entries)
    print(len(dictionary_of_unique_text_entries),'unique text entries found!')

    import pickle
    with open('temp/hashdump.pkl', 'wb') as f:
        pickle.dump(dictionary_of_unique_text_entries, f)
