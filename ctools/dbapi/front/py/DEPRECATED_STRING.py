from string import *

def atof(s):
    '''Deprecated since release 2.0. Use the float() built-in function.'''
    return float(s)

def atoi(s, base=0):
    '''Deprecated since release 2.0. Use the int() built-in function.'''
    return int(s)

def atol(s, base=0):
    '''Deprecated since release 2.0. Use the long() built-in function.'''
    return long(s)

def capitalize(word):
    '''Return a copy of word with only its first character capitalized.'''
    return word.capitalize()

def expandtabs(s, tabsize=8):
    '''Expand tabs in a string replacing them by one or more spaces, depending on the current column and the given tab size.
       The column number is reset to zero after each newline occurring in the string.
       This doesn't understand other non-printing characters or escape sequences.
       The tab size defaults to 8.
    '''
    return s.expandtabs(tabsize)

def find(s, sub, start=None, end=None):
    '''Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end].
       Return -1 on failure.
       Defaults for start and end and interpretation of negative values is the same as for slices.
    '''
    if start == None:
        return s.find(sub)
    if end == None:    
        return s.find(sub, start)
    return s.find(sub, start, end)

def rfind(s, sub, start=None, end=None):
    '''Like find() but find the highest index.'''
    if start == None:
        return s.rfind(sub)
    if end == None:    
        return s.rfind(sub, start)
    return s.rfind(sub, start, end)

def index(s, sub, start=None, end=None):
    '''Like find() but raise ValueError when the substring is not found.'''
    if start == None:
        return s.index(sub)
    if end == None:    
        return s.index(sub, start)
    return s.index(sub, start, end)

def rindex( s, sub, start=None, end=None):
    '''Like rfind() but raise ValueError when the substring is not found.'''
    if start == None:
        return s.rindex(sub)
    if end == None:    
        return s.rindex(sub, start)
    return s.rindex(sub, start, end)

def count(s, sub, start=None, end=None):
    '''Return the number of (non-overlapping) occurrences of substring sub in string s[start:end].
       Defaults for start and end and interpretation of negative values are the same as for slices.
    '''
    if start == None:
        return s.count(sub)
    if end == None:    
        return s.count(sub, start)
    return s.count(sub, start, end)

def lower(s):
    '''Return a copy of s, but with upper case letters converted to lower case.'''
    return s.lower()

def split(s, sep=None, maxsplit=None):
    '''Return a list of the words of the string s.
       If the optional second argument sep is absent or None, the words are separated by arbitrary strings of whitespace characters (space, tab, newline, return, formfeed).
       If the second argument sep is present and not None, it specifies a string to be used as the word separator.
       The returned list will then have one more item than the number of non-overlapping occurrences of the separator in the string. The optional third argument maxsplit defaults to 0. If it is nonzero, at most maxsplit number of splits occur, and the remainder of the string is returned as the final element of the list (thus, the list will have at most maxsplit+1 elements).
       The behavior of split on an empty string depends on the value of sep.
       If sep is not specified, or specified as None, the result will be an empty list.
       If sep is specified as any string, the result will be a list containing one element which is an empty string.
    '''
    if sep == None:
        return s.split()
    if maxsplit == None:          
        return s.split(sep)
    return s.split(sep, maxsplit)

def rsplit(s, sep=None, maxsplit=None):
    '''Return a list of the words of the string s, scanning s from the end.
       To all intents and purposes, the resulting list of words is the same as returned by split(), except when the optional third argument maxsplit is explicitly specified and nonzero.
       When maxsplit is nonzero, at most maxsplit number of splits - the rightmost ones - occur,
       and the remainder of the string is returned as the first element of the list (thus, the list will have at most maxsplit+1 elements).
       New in version 2.4.
    '''   
    if sep == None:
        return s.rsplit()
    if maxsplit == None:          
        return s.rsplit(sep)
    return s.rsplit(sep, maxsplit)

def splitfields(s, sep=None, maxsplit=None):
    '''This function behaves identically to split().
       (In the past, split() was only used with one argument, while splitfields() was only used with two arguments.)
    '''
    if sep == None:
        return s.splitfields()
    if maxsplit == None:          
        return s.splitfields(sep)
    return s.splitfields(sep, maxsplit)

def join(words, sep=None):
    ''' Concatenate a list or tuple of words with intervening occurrences of sep.
        The default value for sep is a single space character.
        It is always true that "string.join(string.split(s, sep), sep)" equals s.
    '''
    if sep == None:
        return words.join()
    return words.join(sep)    

def joinfields(words, sep=None):
    '''This function behaves identically to join().
       (In the past, join() was only used with one argument, while joinfields() was only used with two arguments.)
       Note that there is no joinfields() method on string objects;
       use the join() method instead.
    '''
    if sep == None:
        return words.join()
    return words.join(sep)    

def lstrip(s, chars=None):
    '''Return a copy of the string with leading characters removed.
       If chars is omitted or None, whitespace characters are removed.
       If given and not None, chars must be a string; the characters in the string will be stripped from the beginning of the string this method is called on.
       Changed in version 2.2.3: The chars parameter was added.
       The chars parameter cannot be passed in earlier 2.2 versions.
    '''   
    if chars == None:
        return s.lstrip()
    return s.lstrip(chars)    

def rstrip(s, chars=None):
    '''Return a copy of the string with trailing characters removed.
       If chars is omitted or None, whitespace characters are removed.
       If given and not None, chars must be a string; the characters in the string will be stripped from the end of the string this method is called on.
       Changed in version 2.2.3: The chars parameter was added.
        The chars parameter cannot be passed in earlier 2.2 versions.
    '''   
    if chars == None:
        return s.rstrip()
    return s.rstrip(chars)    

def strip(s, chars=None):
    '''Return a copy of the string with trailing characters removed.
       If chars is omitted or None, whitespace characters are removed.
       If given and not None, chars must be a string; the characters in the string will be stripped from the end of the string this method is called on.
       Changed in version 2.2.3: The chars parameter was added.
        The chars parameter cannot be passed in earlier 2.2 versions.
    '''   
    if chars == None:
        return s.strip()
    return s.strip(chars)    

def swapcase(s):
    '''Return a copy of s, but with lower case letters converted to upper case and vice versa.'''
    s.swapcase()

def translate(s, table, deletechars=None):
    '''Delete all characters from s that are in deletechars (if present),
       and then translate the characters using table,
       which must be a 256-character string giving the translation for each character value,
       indexed by its ordinal.
    '''   
    if chars == None:
        return s.translate(table)
    return s.translate(table, deletechars)    

def upper(s):
    '''Return a copy of s, but with lower case letters converted to upper case.'''
    return s.upper()

def ljust(s, width):
    '''Left-justify a string in a field of given width.
       They return a string that is at least width characters wide,
       created by padding the string s with spaces until the given width on the right side.
       The string is never truncated.
    '''
    return s.ljust(width)   

def rjust(s, width):
    '''Left-justify a string in a field of given width.
       They return a string that is at least width characters wide,
       created by padding the string s with spaces until the given width on the left side.
       The string is never truncated.
    '''
    return s.rjust(width)   

def center(s, width):
    '''Left-justify a string in a field of given width.
       They return a string that is at least width characters wide,
       created by padding the string s with spaces until the given width on both sides.
       The string is never truncated.
    '''
    return s.center(width)   

def zfill(s, width):
    '''Pad a numeric string on the left with zero digits until the given width is reached.
       Strings starting with a sign are handled correctly.
    '''   
    return s.zfill(width)   

def replace(str, old, new, maxreplace=None):
    '''Return a copy of string str with all occurrences of substring old replaced by new.
       If the optional argument maxreplace is given,
       the first maxreplace occurrences are replaced.
    '''
    if maxreplace == None:
        return str.replace(old, new)
    return str.replace(old, new, maxreplace)        