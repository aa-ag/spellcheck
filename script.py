###--- IMPORTS ---###
import sys
import textblob
from textblob import TextBlob

'''
TextBlob is a Python (2 and 3) library for processing textual data. 
It provides a simple API for diving into common natural language processing (NLP) tasks,
such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
'''
# https://textblob.readthedocs.io/en/dev/

###--- GLOBAL VARIABLES ---###
text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''


###--- FUNCTIONS ---###
def sentiment_and_polarity():
    blob = TextBlob(text)
    blob.tags
    # [('The', 'DT'), ('titular', 'JJ'), ('threat', 'NN'), ('of', 'IN'), ...]

    blob.noun_phrases
    # WordList(['titular threat', 'blob',
    # 'ultimate movie monster', 'amoeba-like mass', ...])

    for sentence in blob.sentences:
        print(sentence.sentiment.polarity)

    '''
    0.06000000000000001
    -0.34166666666666673
    '''


###--- DRIVER CODE ---###
if __name__ == "__main__":
    sentiment_and_polarity()
