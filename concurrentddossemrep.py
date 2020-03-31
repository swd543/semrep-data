#!/usr/bin/python3
import os
import atexit

# This program is used for concurrently getting data from semrep based on hashed text entries
path='parallel'
for filename in os.listdir(path):
    if not filename.endswith(".pkl"): continue
    lockfile='{0}/{1}.lock'.format(path,filename)
    if os.path.isfile(lockfile): continue
    print(filename, 'needs doing')

    with(open(lockfile, 'w')):
        print('lock created for',lockfile)

    @atexit.register
    def goodbye():
        print('deleting lock',lockfile)
        os.remove(lockfile)
    
    import ddossemrepcopy
    ddossemrepcopy.process(os.path.join(path, filename),
    cookie='_ga=GA1.2.2064073637.1585318918; _gid=GA1.2.1001404715.1585318918; _ga=GA1.4.2064073637.1585318918; ncbi_sid=8A1AC971E7F50ED1_0805SID; pmc.article.report=; books.article.report=; _ga=GA1.3.2064073637.1585318918; _gid=GA1.3.1001404715.1585318918; QSI_HistorySession=https%3A%2F%2Fwww.nlm.nih.gov%2Fresearch%2Fumls%2Fknowledge_sources%2Fmetathesaurus%2Findex.html~1585439813961; _gat_UA-137948717-1=1; MOD_AUTH_CAS_S=a97c4d65c00b25c53ad0077dd3508504')
    break