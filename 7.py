file1 = open('file1.txt')
words = file1.read().split()
new_words = []
for word in words:
    if not word.lower().startswith('a') and not word.lower().startswith('e') and not word.lower().startswith(
            'i') and not word.lower().startswith('o') and not word.lower().startswith('u'):
        new_words.append(f'{word} ')
new_str = ''.join(new_words)
file2 = open('file2.txt', 'w')
file2.write(new_str)
file1.close()
file2.close()
'''
input file: Carry Umbrella and overcoat when it rains
output file: Carry when rains 
'''
