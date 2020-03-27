#!/usr/bin/python3

import pickle

def verifyHash(accuracy=0.1, filename='temp/hashdump.pkl'):
    with open(filename, 'rb') as f:
        dictionary_of_unique_text_entries=pickle.load(f)
    print(len(dictionary_of_unique_text_entries),'unique text entries')

    # Verify integrity of loaded pickle
    import pandas as pd
    data=pd.read_csv('XMLProduct_DBID_2/XMLProduct_DBID_2.csv')
    print(len(data),'entries in csv file')

    import random
    for i in range(0,int(len(dictionary_of_unique_text_entries)*accuracy)):
        index=random.randint(0, len(dictionary_of_unique_text_entries))
        t=list(dictionary_of_unique_text_entries.values())[index]
        for rowIndex in t['rowIndex']:
            assert len(data.iloc[rowIndex]['Text'].strip())==t['size']

    print('Dictionary looks good :)')
    return dictionary_of_unique_text_entries, data

if __name__ == "__main__":
    verifyHash()