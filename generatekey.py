#!/usr/bin/env python3
#macos/linux

import os, shutil

def main():
    print('genrating keys ...')
    currentDirectory = os.popen('pwd').read().replace("\n","")
    if os.path.exists(os.path.join(currentDirectory, 'private.key')):
        os.system('rm -rf private.key')
    if os.path.exists(os.path.join(currentDirectory, 'public.key')):
        os.system('rm -rf public.key')
    os.system('openssl genrsa -out private.key 512')
    os.system('openssl rsa -in private.key -pubout -out public.key')
    print('keys generated.')
    if os.path.exists(os.path.join(currentDirectory, 'keys')):
        os.system('rm -rf keys')
    os.mkdir(os.path.join(currentDirectory, 'keys'))
    print('created directory: \'keys\'')
    shutil.copy(os.path.join(currentDirectory, 'private.key'), os.path.join(currentDirectory, 'keys', 'private.key'))
    shutil.copy(os.path.join(currentDirectory, 'public.key'), os.path.join(currentDirectory, 'keys', 'public.key'))
    os.system('rm -rf public.key private.key')
    print('moved the keys to the directory name \'keys\'.')
    print('done.')

if __name__=='__main__':main()