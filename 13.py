def push(item,list_name):
    list_name.append(item)
def pop(list_name):
    if list_name != []:
        list_name.pop()
    else:
        pass

string_1 = list(input("Input the string 1: "))
string_2= list(input("Input the string 2: "))
def AreEqual(string_1,string_2):
    str_1 = []
    str_2 = []
    def abc(string_name,final_string):
        temp_str_list = []
        for chara in string_name:
            if chara == "#":
                pop(temp_str_list)
            else:
                push(chara, temp_str_list)
        final_str = ""
        for chara in temp_str_list:
            final_str += chara
        return final_str

    if abc(string_1,final_string=str_1) ==abc(string_2,final_string=str_2):
        return True
    else:
        return False
if __name__ == "__main__":
    print(AreEqual(string_1,string_2))

'''
Output:
1 ---
Input the string 1: ab#c
Input the string 2: ad#c
True

Process finished with exit code 0
2 ---
Input the string 1: ab##
Input the string 2: c#d#
True
3 ---
Input the string 1: a#c
Input the string 2: b
False

Process finished with exit code 0
'''
