#!/usr/bin/python3

import pickle
import sys
import argparse

# A utility to view the pickled files
parser = argparse.ArgumentParser(description='Super secret task.')
parser.add_argument("-s", "--supersecret", help="Super Secret Task", action='store_true')
parser.add_argument("-i", "--input", help="Input file location")
args = parser.parse_args()

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) <= 1:
        print('Specify pickle file as parameter.')
    else:
        thing=pickle.load(open(args.input, 'rb'))
        if isinstance(thing, dict) and args.supersecret:
            print(len(thing))
            newDict = list(filter(lambda e: 'semrep' in e.keys(), thing.values()))
            print('Semrepped attributes ->',len(newDict))
        else:   
            import pprint as pp
            pp.pprint(thing, indent=2, width=600)

