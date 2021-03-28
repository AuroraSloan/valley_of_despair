from string import punctuation
import sys


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters, \
        punctuation and spaces in a given text."""
    if len(args) > 1:
        return print('ERROR')
    if len(args) == 0:
        text = input('What is the text to analyse?')
    elif len(args) == 1:
        text = args[0]
    print('The text contains {} characters:'.format(len(text)))
    print('- {} upper letters'.format(sum(1 for c in text if c.isupper())))
    print('- {} lower letters'.format(sum(1 for c in text if c.islower())))
    print('- {} puncuation marks'.format(sum(1 for c in text if c in punctuation)))
    print('- {} spaces'.format(text.count(' ')))