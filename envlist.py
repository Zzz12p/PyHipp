#!/data/miniconda3/envs/env1/bin/python
import sys
import hickle
from filelock import FileLock

envfile = '/data/picasso/envlist.hkl'
lockfile = envfile + '.lock'

with FileLock(lockfile):
    if len(sys.argv) == 3:
        # Generate: envlist.py cenv 64
        prefix = sys.argv[1]
        count = int(sys.argv[2])
        envs = [prefix + str(i) for i in range(count)]
        hickle.dump(envs, envfile)
    elif len(sys.argv) == 2:
        # Return: envlist.py cenv0
        envname = sys.argv[1]
        envs = hickle.load(envfile)
        envs.append(envname)
        hickle.dump(envs, envfile)
    else:
        # Request: envlist.py
        envs = hickle.load(envfile)
        envname = envs.pop(0)
        hickle.dump(envs, envfile)
        print(envname)
