###--- IMPORTS ---###
import sys
import textblob
from textblob import TextBlob, Word

'''
TextBlob is a Python (2 and 3) library for processing textual data. 
It provides a simple API for diving into common natural language processing (NLP) tasks,
such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
'''
# https://textblob.readthedocs.io/en/dev/

###--- GLOBAL VARIABLES ---###
txt = "I havv good spelling."


###--- FUNCTIONS ---###
def correct_spelling():
    '''
     Use the correct() method 
     to attempt spelling correction.
    '''
    global txt
    usable = TextBlob(txt)
    return usable.correct()


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
    # correct_spelling()
    check_spelling()
