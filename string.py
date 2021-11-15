# 1․ գրել մեկ մոդուլում օրինակներ բոլոր ստրինգ մեթոդների մասով․ օրինակ՝ my_string = ‘i want to learn programming in
# the Python programming language’ print(my_string.capitalize()) capitalize(), casefold(), center(), count(),
# encode(), endswith(), expandtabs(), find(), format(), format_map(), index(), isalnum(), isalpha(), isascii(),
# isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper(),
# join(), ljust(), lower(), lstrip(), maketrans(), partition(), replace(), rfind(), rindex(), rjust(), rpartition(),
# rsplit(), rstrip(), split(), splitlines(), startswith(), strip(), swapcase(), title(), translate(), upper(), zfill()

string = 'hello     world'
print(string.capitalize())
print('hello worldß'.casefold())
print(string.center(35))
print(string.count('l'))
print(string.encode())
print(string.endswith('world'), string.endswith('sdf'))
print('efhewredferfe\t\tfichwe'.expandtabs())  # ???????????????????????????????????????????????????????????????????????
print(string.find('l'))
print('hello {}'.format('world'))
print('he{x}l{y}'.format_map({'x': '1', 'y': '2'}))
print(string.index('l'))
print(string.isalnum(), '12312342dfer'.isalnum())
print(string.isalpha(), 'gverbfurfuibgwe'.isalpha())
print(string.isascii(), ' меня, к'.isascii())
print(string.isdecimal(), '123432534'.isdecimal())
print(string.isdigit(), '124323546'.isdigit())
print(string.isidentifier(), 'fdwefr3b487frgcbgue4b'.isidentifier())
print(string.islower())
print(string.isnumeric(), '12341234.2'.isnumeric())
print(string.isprintable(), 'My name is \n Ayush'.isprintable())
print(string.isspace(), '    '.isspace())
print(string.istitle(), 'Hello World'.istitle())
print(string.isupper(), 'FCDTCSWVDY'.isupper())
print(" hello. ".join(["Borik", 'Davit', 'Karen', '']))
print(string.ljust(50, '0'))
print()

...

# Խնդիր․ 1
# A string is entered, consisting of words separated by spaces. It is required to count the number of words in it.

string = input('string:  ')
print(len(string.split()))
# Խնդիր․ 2
# Count the number of lowercase (small) and uppercase (uppercase) letters in the entered line. Consider only English letters.
string = input('string:  ')
num_of_lowercase = 0
num_of_uppercase = 0
for i in string:
    if i == i.upper():
        num_of_uppercase += 1
    else:
        num_of_lowercase += 1


# Խնդիր․ 3
# A string is entered containing letters, non-negative integers and other symbols. All numbers that occur in the string are required to be placed in a separate integer array. For example, if the string "data 48 call 9 read13 blank0a" is given, then the array should contain the numbers 48, 9, 13 and 0.

string = input()
lis = ['']
for i in string:
    if i.isdigit():
        lis[-1] += i
    else:
        if lis[-1] != '':
            lis.append('')
if lis[-1] == '':
    lis = lis[:-1:]
print(lis)


# Խնդիր․ 4
# An unnormalized string is entered, which may have spaces at the beginning, at the end and between words, more than one space. Bring it to a normalized form, i.e. remove all leading and trailing spaces and leave only one space between words.


def ex_4(l):
    return l.strip()

# Խնդիր․ 5
# A string is entered. It is required to remove duplicate characters and all spaces from it. For example, if "abc cde def" was entered, then "abcdef" should be output.


def ex_5(l):
    st = {' '}
    string = ''
    for i in l:
        if i not in st:
            string += i
    return string



# Խնդիր․ 6
# Strings are entered. Determine the longest string and display its number on the screen. If there are several longest lines, print the numbers of all such lines.

def ex_6(*args):
    indexes = []
    maximum = -float('inf')
    for i in range(len(args)):
        c = len(args[i])
        if c > maximum:
            indexes = [i]
            maximum = c
        elif c == maximum:
            indexes.append(i)
    return indexes

print(ex_6('qwer', 'qwe', 'qwer', 'qwer', 'sdvx'))


# Խնդիր․ 7
# A string is entered. Remove all spaces from it. After that, determine if it is a palindrome (shape-shifter), i.e. spelled equally from the beginning and from the end.

def ex_7(l):
    string = ''
    for i in l:
        if i != ' ':
            string += i
    return string == string[::-1]

# Խնդիր․ 8
# Find the specified substring in the string and replace it with a new one. The user enters the string, its replacement substring, and the new substring.

def ex_8_1(string, l, l_1):
    return string.replace(l, l_1)


def ex_8_2(string, l, l_1):
    for i in range(-len(string), 0, 1):
        if string[i] == l[-1] and string[i-len(l):i] == l:
            string = string[:i-len(l):] + l_1 + string[i:]
    return string

print(ex_8_1('qweeert', 'ee', 'uoiee'))
print(ex_8_2('qweeert', 'ee', 'uoiee'))




