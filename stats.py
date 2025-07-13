import string

def count_words(a_string):
    return len(a_string.split())

def construct_char_count(a_string):
    result = {}
    # for c in string.ascii_lowercase:
    #    result[c] = 0
    for c in a_string.lower():
        if c.isalpha():
            if not c in result:
                result[c] = 1
            else:
                result[c] += 1
    return result

def sort_char_count_aux(item):
    return item["num"]

def sort_char_count( char_count ):
    result = []
    for k,v in char_count.items():
        result.append({"char": k, "num": v})
    result.sort(reverse=True, key=sort_char_count_aux)
    return result