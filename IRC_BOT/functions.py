""" Contains auxillary functions that are used in bot.py. """

def read_data(filename):
    """ read a list of words from a file """
    data_list = []
    with open(filename) as file:
        for line in file:
            if line.lower() not in data_list:
                data_list.append(line.rstrip().lower())
    return data_list

def test_match(word_list, text):
    """ Test list of words against text for matches """
    for word in word_list:
        if text.lower().find(word) > 0:
            return True
    return False

def test_max(str_int_dict, max_value):
    """ Check whether an element in the dictionary has the max value """
    for element in str_int_dict:
        if str_int_dict[element] > max_value:
            return True
    return False
