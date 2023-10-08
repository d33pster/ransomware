#!/usr/bin/env python3
#macos/linux

import os
from pathlib import Path

def scanRecurse(baseDIR):
    for entry in os.scandir(baseDIR):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)

def main():
    inputDIR = input('Enter input Directory: ')
    currentDirectory = os.popen('pwd').read().replace('\n','')
    print('generating directory map ...')
    if os.path.exists(os.path.join(currentDirectory, 'map')):
        os.system('rm -rf map')
    os.mkdir(os.path.join(currentDirectory, 'map'))
    with open(os.path.join(currentDirectory, 'map', 'dir.map'), 'w') as dmap:
        for item in scanRecurse(inputDIR):
            dmap.write(f"{Path(item)}\n")
    print('done.')

if __name__=='__main__':main()