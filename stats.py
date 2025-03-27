def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dictionary = {}
    for letter in text:
        letter = letter.lower()
        if letter in dictionary:
            dictionary[letter] = dictionary[letter] + 1
        else:
            dictionary[letter] = 1
    return dictionary

def sort_on(dictionary):
    return dictionary["num"]

def sorted_list(dictionary):
    list = []
    for i in dictionary:
        list.append({"char": i, "num": dictionary[i]})
    list.sort(reverse=True, key=sort_on)
    return list

