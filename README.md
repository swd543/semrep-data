
Read https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3540517/

UMLS unique concept identifier (CUI), which is linked to one or more UMLS semantic types in the files MRSTY and SRSTRE1.

http://europepmc.org/article/PMC/4765595

CUI references
https://www.ncbi.nlm.nih.gov/books/NBK9676/pdf/Bookshelf_NBK9676.pdf
https://www.ncbi.nlm.nih.gov/books/NBK9685/pdf/Bookshelf_NBK9685.pdf


# Workflow

- [x] Create dictionary of unique paragraphs in CSV (ddossemrep.py)
- [x] Split data to be processed in parallel (splitdata.py)
- [x] Fill up the dictionary with output from semrep (concurrentddossemrep.py)
- [x] Combine split data into one big dictionary (combiner.py)
- [x] Verify if our dictionary is consistent and valid (debughash.py)
- [x] view generated pickle dictionary (viewpickle.py)
- [x] Generate CSV for each semrep output in dictionary (decompiler.py)

# Generated files
- The most important data is (./temp/hashdump.pkl). This holds the filled dictionary in python pickle format!
- After running (decompiler.py), the generated csv are outputted to (./mapping/input/input{hash}.csv)
- Mapping files are located at (./mapping/myfirstmapping.ttl) (drug-active ingredient) and (./mapping/mapmeta.ttl) (semrep)
- Outputted nt files are located at (./mapping/m.nt) (semrep) and (./mapping/o.nt) (drug-active ingredients)