

def strip_text(input_text):
    import re

    re_no_puncs = re.compile("[^\w]", re.MULTILINE)
    re_no_under = re.compile("_", re.MULTILINE)

    no_puncs = re_no_puncs.sub("", input_text)
    no_puncs_or_under = re_no_under.sub("", no_puncs)

    clean_text = no_puncs_or_under

    return clean_text


