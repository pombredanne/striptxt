# striptxt
A simple python script to extract strings with length equal or greater to a certain value. The purpose of the script is to shorten wordlists that have values shorter than the password length. Some dictionary attack software doesn't have the option, so this script will shorten the wordlist in seconds.

Designed for linux, in python3. It's a small script for personal use that can work with big files, tested on wordlist rockyou.txt

# Available commands
`-i <input file>`

`-o <output file>`

`-l <string length>`

`-v display additional info`

`-h show help`

# Usage example
`striptxt.py -i dictionary.txt -l 10`
