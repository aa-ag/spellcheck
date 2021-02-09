###--- IMPORTS ---###
import textblob
from textblob import TextBlob, Word

'''
TextBlob is a Python (2 and 3) library for processing textual data. 
It provides a simple API for diving into common natural language processing (NLP) tasks,
such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
'''
# https://textblob.readthedocs.io/en/dev/

from spellchecker import SpellChecker
# https://pyspellchecker.readthedocs.io/en/latest/

import urllib.request
from bs4 import BeautifulSoup


###--- GLOBAL VARIABLES ---###
misspellings = "something is hapenning here"
typos = "My interests include: cooking dogs, shopping, dancing, reading, and watching movies."

page = 'https://legacy.theresumator.com/apply/GiLc0mCVDv/Marketing-Sales-Operations-Associate'


###--- FUNCTIONS ---###
def correct_spelling():
    '''
     Use the correct() method 
     to attempt spelling correction.
    '''
    global typos
    usable_text = TextBlob(typos)

    # for word in usable_text.split():
    #     print(word.correct())

    print(usable_text.correct())
    # I have good spelling.


def check_spelling():
    '''
     .spellcheck() method that returns a list 
     of (word, confidence) tuples with spelling suggestions.
    '''
    word = Word('fal;ibility')
    print(word.spellcheck())
    # [('fallibility', 1.0)]


def spell_checker_version():
    global misspellings

    spell = SpellChecker()

    for word in misspellings.split():
        # prints most likely word
        # print(spell.correction(word))
        # prints probable corrections
        print(spell.candidates(word))


def aggregate_text():
    # query website
    global page
    req = urllib.request.Request(page)
    with urllib.request.urlopen(req) as response:
        p = response.read()

    # parse html usig beautiful soup
        soup = BeautifulSoup(p, 'html.parser')

        with open("jobs.html", "w", encoding='utf-8') as html:
            html.write(str(soup))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # correct_spelling()
    # check_spelling()
    # spell_checker_version()
    aggregate_text()
