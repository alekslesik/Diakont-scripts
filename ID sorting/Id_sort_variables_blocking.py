# Пересортировка по "ID =" или любому другому значению


from Utils import Utils

file_open = 'D:\BUILDS\СУПК_Хмельницкая\work\SUPK\DB\Xml\PermissionVariablesBlocking.xml'
# fileOpen = input("Введи путь")

encoding = Utils.define_ini_encoding(file_open)

f = open(file_open, 'r', encoding=encoding)
lines = [line for line in f]

count1 = 0
count2 = 0

for index, l in enumerate(lines):
    if l.startswith('<Variable name'):
        count1 += 1
        lines[index] = '<Variable name="bBlocking' + str(count1) + '">\n'
    if l.strip().startswith('<Variable category'):
        count2 += 1
        lines[index] = '<Variable category="Blocking" id="' + str(count2) + '"> bBlocking' + str(count2) +\
                       '  </Variable>\n'
    if l.strip().startswith('<!-' + '-' + ' <Variable category') or \
            l.strip().startswith('<!-' + '-' + '<Variable category'):
        count2 += 1
        lines[index] = '<!-' + '-' + ' <Variable category="Blocking" id="' + str(count2) + '"> bBlocking' + \
                       str(count2) + '  </Variable> ' + '-'+'-'+'>\n'
f.close()

fileCreate = file_open[:-4] + "_out" + file_open[-4:]
f = open(fileCreate, 'w', encoding=encoding)


f.write(''.join(lines))
f.close()
