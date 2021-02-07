###--- IMPORTS ---###
import textblob
from textblob import TextBlob, Word

'''
TextBlob is a Python (2 and 3) library for processing textual data. 
It provides a simple API for diving into common natural language processing (NLP) tasks,
such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
'''
# https://textblob.readthedocs.io/en/dev/

###--- GLOBAL VARIABLES ---###
misspellings = "Ii havv goood sspelling."
typos = "My interests include: cooking dogs, shopping, dancing, reading, and watching movies."

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


###--- DRIVER CODE ---###
if __name__ == "__main__":
    correct_spelling()
    # check_spelling()
