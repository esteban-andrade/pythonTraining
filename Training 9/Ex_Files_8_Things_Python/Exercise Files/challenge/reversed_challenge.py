import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    '''Palindromes are case insensitive, so both radar and Radar are valid'''
    reverse_words = "".join(reversed(words))
    
    if remove_punctuation(words.lower()) == remove_punctuation(reverse_words.lower()):
        return True
    else:
        return False
