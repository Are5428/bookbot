def words_count(message):
    list_message = message.split()
    count = len(list_message)
    return count

def char_count(message):
    text = message.lower()
    char_counter = {}
    for char in text:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    for char in char_counter:
        print(f"'{char}': {char_counter[char]}")
    return char_counter

def sort_on(dict):
    return dict["num"]

def dict_list(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
