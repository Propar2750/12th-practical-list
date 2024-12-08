file1 = open('student.txt', 'r')
lines = file1.readlines()
list_of_tuples = []
for line in lines:
    tuple_list = []
    for t in line.split('\t'):
        if t != "":
            tuple_list.append(t)
    list_of_tuples.append(tuple(tuple_list))

print(list_of_tuples)
file1.close()

'''
Output: [('Rajat   Sen     12345   1   CSEE\n',), ('Jagat   Narain  13467   3   CSEE\n',), ('Anu     Sharma  11756 
  2   Biology\n',), ('Sumita  Trikha  23451   4   Biology\n',), ('Sumder  Kumra   11234   3   MME\n',), 
  ('Kanti   Bhushan 23211   3   CSEE',)] 
'''
