#!/usr/bin/python3
import debughash

# Load our preprocessed data
dictionary, data=debughash.verifyHash(0.001)

print("Dictionary looks like this",next(iter(dictionary.values())))

# Function to read html and get the important stuff
# Returns (output text, input text)
def clean(text):
    from bs4 import BeautifulSoup
    decodedtext=text.decode('utf-8')
    soup = BeautifulSoup(decodedtext, 'lxml')
    table = soup.find_all('pre',{'wrap':''})
    assert len(table)==2, '2 tables were expected but %d found!' %len(table)
    return table[1].text, table[0].text

def locateText(dictionaryEntry, dictionary=dictionary, rawData=data):
    for entry in dictionaryEntry['rowIndex']:
        return data.iloc[entry]['Text'].strip()

import requests
import pandas as pd
import hasher
import pickle
import shutil
lenDictionary=len(dictionary)
url='https://ii.nlm.nih.gov/cgi-bin/II/Interactive/UTS_Required/interactiveLocal.pl' 
for index, uniquetext in enumerate(dictionary.values()):
    shutil.copyfile('temp/hashdump.pkl', 'temp/hashdump2.pkl')
    print('Semrepping',index,'of',lenDictionary,'(',index*100/lenDictionary,'% )')
    if uniquetext['size']>1000: continue
    if 'semrep' in uniquetext.keys(): continue
    print('Semrepping the data for rows',uniquetext)
    text=locateText(uniquetext)
    r=requests.post(url=url, 
    headers={'Cookie':'_ga=GA1.2.2064073637.1585318918; _gid=GA1.2.1001404715.1585318918; MOD_AUTH_CAS_S=e2c3f82b3b40050fd7cc79dc2eb863fe'},
    data={
        'RUN_PROG':'SEMREP',
        'InputText':text,
        'KSource':2015,
        'LXY':2015})
    response=r.content.strip()
    cleanedResponse=clean(response)
    hashOfResponse=hasher.hashify(text)
    assert hashOfResponse in dictionary.keys(), 'Hash of response was not found in dictionary?!'
    dictionary[hashOfResponse]['semrep']=cleanedResponse
    print('Dumping response for',dictionary[hashOfResponse])
    with open('temp/hashdump.pkl', 'wb') as f:
        pickle.dump(dictionary, f)