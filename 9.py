file1 = open('myfile.txt', 'r')
words = file1.read().split(" ")
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

v = list(d.values())
k = list(d.keys())

print(k[v.index(max(v))])
print(
    f"Number of words: {len(words)}\nNumber of different words: {len(d.keys())}\nMaximum Occuring word is : {k[v.index(max(v))]}")

d1 = {}
for word in words:
    if len(word) in d1.keys():
        d1[len(word)].append(word)

    else:
        d1[len(word)] = [word]


def find_longest_word(dictionary):
    return dictionary[max(dictionary.keys())]


print(f'The longest word is: {find_longest_word(d1)}')


def filter_long_words(dictionary, n):
    keys = dictionary.keys()
    words = []
    for key in keys:
        if key >= n:
            for word in dictionary[key]:
                words.append(word)
    return words


print(filter_long_words(d1, 7))

'''
Output:
the
Number of words: 67
Number of different words: 56
Maximum Occuring word is : the
The longest word is: ['butterflies,\nwhile']
['bustling', 'Children', 'reminder', 'enduring', 'vibrant', 'breeze,', 'secrets', 'joggers', 'winding', 'moments', 'sway\ngently', "of\nnature's", 'whispering', 'importance', 'preserving', 'centuries', 'butterflies,\nwhile', 'tranquility."']
'''
