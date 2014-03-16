unigram = {'a':100}
digram = {'aa':100}
trigram = {'aaa':100}
quadgram = {'aaaa':100}

def strip_text(input_text):
    import re

    re_no_puncs = re.compile("[^\w]", re.MULTILINE)
    re_no_under = re.compile("_", re.MULTILINE)

    no_puncs = re_no_puncs.sub("", input_text)
    no_puncs_or_under = re_no_under.sub("", no_puncs)

    clean_text = no_puncs_or_under

    return clean_text

def return_xgram_sig(len_of_string):
    step = 50
    factor = float(len_of_string)/float(step)
    print("Factor: %f" % factor)
    
    if factor <= 1:
        return unigram
    if 1 < factor <= 2:
        return digram
    if 2 < factor <= 3:
        return trigram
    if factor > 3:
        return quadgram
