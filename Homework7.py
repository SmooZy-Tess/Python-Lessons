import os
print('--------------------number 1--------------------')

def read_last(lines, file):
    abstract_file = open(file, 'r', encoding='utf-8')
    row = abstract_file.readlines()
    con = row[lines:]
    for i in row[lines:]:
        print(i)


a = 'article.txt'
line = int(input('Введите целое положительное число '))
tfile = open(a, 'r', encoding='utf-8')
list_number = len(tfile.readlines())

if line > 0 and line < list_number:
    read_last(line, a)

print('--------------------number 2--------------------')

def print_docs(directory):
    all_files = os.walk(directory)
    print(all_files)

print_docs('C:/Users/Vlad/Documents')

print('--------------------number 3--------------------')

def longest_words(file):
    min = 0
    abstract_file = open(file, 'r', encoding='utf-8')
    row = abstract_file.readlines()
    for i in row:
        for j in i.split(' '):
            if len(j) > min:
                min = len(j)
    for i in row:
        for j in i.split(' '):
            if len(j) == min:
                print(j)

a = 'article.txt'
longest_words(a)

print('--------------------number 4--------------------')

file = input('Введите название файла: ')
a = f'{file}.txt'
tfile = open(a, 'w', encoding='utf-8')
text = input('Введите текст: ')
while text != '':
    tfile.write(text + '\n')
    text = input('Введите текст: ')


