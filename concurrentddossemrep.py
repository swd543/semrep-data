#!/usr/bin/python3
import os
import atexit

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
     cookie='_ga=GA1.2.2064073637.1585318918; _gid=GA1.2.1001404715.1585318918; MOD_AUTH_CAS_S=28741a3a79cefcf1d4e81d62deee84b3')
    break