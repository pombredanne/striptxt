#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, time, sys
from sys import argv, stdout

# Global variables
INPUT = None
OUTPUT = None
LENGTH = None
VERBOSE = False
AUTOOUT = False
AUTOLEN = False

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[92m' # green
B  = '\033[34m' # blue
O  = '\033[91m' # orange
GR  = '\033[94m' # gray
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
BO = '\033[1m'  #bold

def Credits():
    os.system('clear')
    print(O + '   _____ _        _    _______   _      \n' +   
              '  / ____| |      (_)  |__   __| | |     \n' + 
              ' | (___ | |_ _ __ _ _ __ | |_  _| |_    \n' + 
              '  \___ \| __| \'__| | \'_ \| \ \/ / __| \n' + 
              '  ____) | |_| |  | | |_) | |>  <| |_    \n' + 
              ' |_____/ \__|_|  |_| .__/|_/_/\_\\__|   \n' + 
              '                   | |                  \n' + 
              '                   |_|                  \n' + W)
    print(W + BO + ' StripTxt v1' + W)
    print(C + ' - automated text file word length limiter' + W)
    print(C + ' - designed for Linux, for extracting passwords\n of desired length from dictionary files' + W + '\n')
    print(B + ' https://github.com/NulledGravity/striptxt' + W + '\n\n')

def VerifyGlobals():
    global INPUT, OUTPUT, LENGTH, VERBOSE, AUTOOUT, AUTOLEN
    cwd = os.getcwd()
    if not INPUT:
        print(GR + ' [+] ' + R + 'You must define an input file!')
        ExitLikeABitch(0)
    if not os.path.isfile(INPUT):
        print(GR + ' [+] ' + R + 'The input file was not found at the following path!')
        print(GR + '     ' + cwd + os.sep + INPUT)
    if not OUTPUT:
        OUTPUT = 'out.txt'
        AUTOOUT = True
    if not LENGTH:
        LENGTH = 8
        AUTOLEN = True
    if VERBOSE:
        if AUTOOUT:
            print(GR + ' [+] ' + W + 'You have not defined an output file!')
            print(GR + ' [+] ' + 'The file will be created automatically at:')
            print(GR + '     ' + cwd + os.sep + OUTPUT)
        if AUTOLEN:
            print(GR + ' [+] ' + W + 'You have not defined the desired string length')
            print(GR + ' [+] ' + 'The default length will be ' + W + '8')

def ProcessTextFile():
    try:
        bunchsize = 1000000
        bunch = []
        with open(INPUT, 'r', encoding='latin-1') as r, open(OUTPUT, 'w', encoding='latin-1') as w:
            print('\n' + GR + ' [+] ' + BO + 'starting processing' + W)
            i = 0
            for line in r:
                if len(line) < (LENGTH + 1): continue
                bunch.append(line)
                PrintStatus(i)
                if len(bunch) == bunchsize:
                    w.writelines(bunch)
                    bunch = []
                i += 1
            w.writelines(bunch)
        print('\n')
    except KeyboardInterrupt:
        print('\n' + R + ' (^C) ' + O + 'interrupted\n' + W)
        ExitLikeABitch(0)

def PrintStatus(index):
    print(GR + ' [+] ' + W + BO + str(index) + W + ' lines processed', end='')
    sys.stdout.write('\r')
    sys.stdout.flush()

def HandleArguments():
    global INPUT, OUTPUT, LENGTH, VERBOSE

    args = argv[1:]
    if args.count('?') + args.count('-h') + args.count('-help') + args.count('--help') > 0:
        Help()
        ExitLikeABitch(0)

    try:
        for i in range(0, len(args)):
            if args[i] == '-l':
                i += 1
                LENGTH = int(args[i])
            elif args[i] == '-i':
                i += 1
                INPUT = args[i]
            elif args[i] == '-o':
                i += 1
                OUTPUT = args[i]
            elif args[i] == '-v':
                VERBOSE = True
    except IndexError:
        print('error')
        print('\n' + R + '[!]' + W + 'indexerror\n\n')

def Help():
    HelpIndent('Commands')  
    HelpIndent('-i' + W + ' <file>' + GR + '      set path to the dictionary', type=1)
    HelpIndent('-o' + W + ' <file>' + GR + '      specify path for output, otherwise the file', type=1)
    HelpIndent(GR + 'will be saved in the current directory', type=1, spaces=23)
    HelpIndent('-l' + W + ' <lenght>' + GR + '    the lenght of strings to be saved, default value: 8', type=1)
    HelpIndent('-v' + GR + '             show extra info on run', type=1)
    print()
    HelpIndent('Example')
    HelpIndent(W + 'striptxt.py -i dictionary.txt', type=1)
    HelpIndent(W + 'striptxt.py -i dictionary.txt -l 10', type=1)
    HelpIndent(W + 'striptxt.py -i dictionary.txt -o newDictionary.txt -l 5', type=1)
    print()
    HelpIndent('-h, ?, --help, -help' + GR + ' show this help message', type=2)
    print()

def HelpIndent(message="", type=0, spaces=4, insidePrint=True):
    if type == 1 and spaces == 4: spaces = 8
    out = ""
    i = 0
    for i in range(spaces):
        out += ' '
        i += 1
    if type == 0: out += GR + message.upper()
    if type == 1 or type == 2: out += O + message
    out += W
    if insidePrint:
        print(out)
    else:
        return out

def ExitLikeABitch(code=0):
    print(GR + ' [+] ' + W + 'quitting\n')
    # GFY BITCH <3
    exit(code)

def main():
    Credits()
    HandleArguments()
    VerifyGlobals()
    ProcessTextFile()

if __name__ == '__main__':
    main()