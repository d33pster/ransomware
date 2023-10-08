#!/usr/bin/env python3

import os, platform

def main():
    if platform.system()=='Darwin':
        os.system('brew install openssl')
    elif platform.system()=='Linux':
        os.system('sudo apt-get install openssl')
    else:
        print('OS not supported')

if __name__=='__main__':main()