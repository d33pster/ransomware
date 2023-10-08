#!/usr/bin/env python3

import os

def main():
    os.system('clear')
    currentDirectory = os.popen('pwd').read().replace('\n','')
    print('[OPENSSL INSTALLATION CHECK]')
    os.system(f"{os.path.join(currentDirectory, 'installREQ.py')}")
    print('[GENERATE PRIVATE AND PUBLIC KEY PAIRS]')
    os.system(f"{os.path.join(currentDirectory, 'generatekey.py')}")
    print('[GENERATE DIR MAP]')
    os.system(f"{os.path.join(currentDirectory, 'getINPUT.py')}")
    print('[VALIDATING]')
    print('validating ...')
    if not os.path.exists(os.path.join(currentDirectory, 'map')):
        print('\'map\' directory missing!')
    if not os.path.exists(os.path.join(currentDirectory, 'keys')):
        print('\'keys\' directory missing!')
    print('[DONE]')

if __name__=='__main__':main()