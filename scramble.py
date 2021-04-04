#!/usr/bin/env python3
import random
import sys

def wordPull(x):
    with open(x, "r") as f:
        words = f.read()
        words = re.sub(r'[^\w\s]', '', words).replace('\n', '')
        wordlst = list(words.split(' '))
        return wordlst

def selection(lst):
    return lst[random.randint(0, len(lst))]

def scrambleWord(word):
    wordList = list(word)
    end = len(word)
    scrambled = ''
    for i in range(0, end):
        scrambled += wordlist[random.randint(0, int(end))]
        end -= 1
    return scrambled

if __name__ == '__main__':
    wordList = wordPull(sys.argv)
    word = selection(wordList)
    scrambledWord = scrambleWord(word)
    print(scrambledWord)
