def append_to_dict(key, value, dictionary):
    if key not in dictionary.keys():
         dictionary[key] = value
    else:
        dictionary[key] += value



def append_to_dict_list(key, value, dictionary):
    if key not in dictionary.keys():
         dictionary[key] = []
    else:
        dictionary[key].append(value)
