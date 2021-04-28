# Пересортировка по "ID =" или любому другому значению
# f = open(fileOpen, 'r')

import chardet

#fileOpen = 'D:\BUILDS\СУПК_Хмельницкая\work\SUPK\DB\Xml\PermissionVariablesBlocking.xml'
fileOpen = input("Введи путь")

with open(fileOpen, 'rb') as codefile:
    data = codefile.read(20000)
    detect = chardet.detect(data)
    print(detect)
encoding = detect['encoding']

f = open(fileOpen, 'r', encoding=encoding)
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
    if l.strip().startswith('<!-' + '-' + ' <Variable category') or l.strip().startswith('<!-' + '-' + '<Variable category') :
        count2 += 1
        lines[index] = '<!-' + '-' + ' <Variable category="Blocking" id="' + str(count2) + '"> bBlocking' + \
                       str(count2) + '  </Variable> ' + '-'+'-'+'>\n'
f.close()

fileCreate = fileOpen[:-4] + "_out" + fileOpen[-4:]
f = open(fileCreate, 'w', encoding=encoding)

# template = string.Template
f.write(''.join(lines))
f.close()
##
