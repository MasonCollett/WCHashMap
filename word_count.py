# Mason Collett - CS261 - Sp2020

# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap
"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # List to contain the words with the highest counts
    top_words_list = []
    for i in range(number):
        top_words_list.append((0,0))

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                # FIXME: Complete this function
                w = w.lower()
                # Check if it already exists in hash map
                if(ht.get(w) is not None):
                    # Update the value to +1 
                    ht.put(w,(ht.get(w)+1))
                else:
                    # Create a new node in hash map with val 1
                    ht.put(w,1)
                # Update the top words list
                top_words_list = check_top_words(top_words_list, w, ht.get(w))
    
    tupl_list = [tuple(i) for i in top_words_list]
    return tupl_list


def check_top_words(top_words_list, w, val):
    """
    Updates the top words list.  Checks if w is on the list,
    if so, needs to update it's value.
    """
    # if w isn't in top word's list, insert w and value as tuple.
    if(any(w in x for x in top_words_list)):
        # Convert to list to update elements
        temp_list = list(top_words_list)
        i = 0
        while(i < len(temp_list)):
            # When the word is found, update it's count by 1.
            # De-tuple the word-val pair, update, reinsert into list
            if(temp_list[i][0] == w):
                sub_temp_list = list(temp_list[i])
                sub_temp_list[1] += 1
                temp_list[i] = sub_temp_list 
                top_words_list = temp_list
                break
            i += 1
        # Sort the list and return
        top_words_list.sort(key=lambda x:x[1], reverse = True)
        return top_words_list
    # Else, check if the word has a higher count than a word currently on the list
    else:
        i = 0
        for j, k in top_words_list:
            # If it has a higher word count, insert it at the correct sorted position and
            # remove the last (lowest) value
            if(val > k):
                top_words_list.insert(i,(w,val))
                top_words_list.pop()
                break
                i += 1
        # Sort the list and return
        top_words_list.sort(key=lambda x:x[1], reverse = True)
        return top_words_list

    





# print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE