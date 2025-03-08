def word_count(book_path):
    with open(book_path) as f:
        words = f.read().split()
        count = 0
        for word in words:
            count += 1
        return(f"Found {count} total words")

def char_count(text):
    lowered = text.lower()
    char_dict = {}
    for char in lowered:
        if(char not in char_dict.keys()):
            char_dict.update({f"{char}":1})
        else:
            count = char_dict.get(f"{char}")
            char_dict.update({f"{char}":count+1})
    return char_dict

def sort_on(dict):
    for value in dict.values():
        return value
    
def report(char_dict):
    dict_list = []

    for item in char_dict:
        entry = {f"{item}":char_dict.get(item)}
        dict_list.append(entry)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    