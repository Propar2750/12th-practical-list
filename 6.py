# Part a
file_1 = open('text_1.txt')
print(file_1.read())
file_1.close()
# Part b
file_1 = open('text_1.txt', 'a')
file_1.writelines(input("Enter the line"))
file_1.close()
file_1 = open('text_1.txt')
lines = file_1.readlines()
for i in range(0, len(lines)):
    print(f'{i + 1} , {lines[i]}')
# Part c
print(lines[-1])
# Part d
print(file_1.read()[10:])
# Part e
line_number = int(input("Enter which line number to read: "))
if line_number < len(lines):
    print(lines[line_number - 1])
# Part f
txt = file_1.read().split(" ")
num = 0
for word in txt:
    if word.lower().startswith('e'):
        num += 1
print(f"{num} words begin with e")


'''
Output:

Neither apple nor pine are in pineapple. Boxing rings are square.
Writers write but fingers dont fing. Overlook and oversee  are opposites.
A house can burn up as it burns down. An alarm goes off by going on.
Enter the linelove is gr8
1 , Neither apple nor pine are in pineapple. Boxing rings are square.

2 , Writers write but fingers dont fing. Overlook and oversee  are opposites.

3 , A house can burn up as it burns down. An alarm goes off by going on.love is gr8
A house can burn up as it burns down. An alarm goes off by going on.love is gr8

Enter which line number to read: 2
Writers write but fingers dont fing. Overlook and oversee  are opposites.

0 words begin with e
'''
