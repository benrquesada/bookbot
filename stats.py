def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    character_dict = {}
    lower_text = text.lower()
    words = lower_text.split()
    for word in words:
        for character in word:
            if character in character_dict:
                character_dict[character] = character_dict[character] + 1
            else:
                character_dict[character] = 1 
    return character_dict


def sorted_caracter_dicts(character_dict):
    def sort_on(dict):
        return dict["count"]
    dict_list = []
    for key,value in character_dict.items():
        dict_list.append({"character": key, "count": value})
    dict_list.sort(reverse=True, key=sort_on)
            
    return dict_list