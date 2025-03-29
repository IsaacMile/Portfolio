def extractText(text, keys):
    '''takes in two strings and determines which words from text only contain
       letters from keys

    Args:
        text (str): string of words to be tested and returned
        keys (str): string of chracters to be used for the test

    Returns:
        tested_words (str): a string containing the words in text that contain
            letters of keys
    '''
    word_list = text.split()
    tested_words = ""
    keys = keys.lower()
    for word in word_list:
        # for every word in the word list created, test every letter
        word_test = True
        for letter in word:
            if not (letter.lower() in keys):
                word_test = False
        if word_test is True:
            # if none of the letters are invalid add the word to final output
            tested_words += word + " "
    return tested_words[:-1]
    # return removed reduntand space at the end of tested_words
