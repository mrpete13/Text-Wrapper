#! /usr/bin/python3

"""
text_wrapper.py by Matt Petersen 
mrpete13 on Github


This program wraps text to a certain number of characters per line in a text
file. This program is currently only functional in windows. 
"""

import textwrap

def wrap(file, length):
    file_object = open(file, 'r+')
    text = file_object.read()
    text = textwrap.fill(text, length)
    wrapped = open(file, 'w')
    wrapped.write(text)


file = input('Which file would you like to wrap the text of?\n')
length = int(input('How many characters would you like the text to wrap at?\n'))
print('Great! Wrapping your file now...\n')

if __name__ == "__main__":
	wrap(file, length)

print('All done. Please ensure your file has been formatted properly.')