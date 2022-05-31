import os


def build_dict(dictionary, data):
    for root, dirs, files in os.walk(data):
        if root.count(os.path.sep) > 1:
            continue
        for file in files:
            name, extension = file.rsplit('.', maxsplit=1)
            if extension not in dictionary:
                dictionary[extension] = [name]
            else:
                dictionary[extension].append(name)


def build_text(dictionary, txt=str()):
    for extension in dict(sorted(dictionary.items(), key=lambda x: x[0])):
        txt += '.' + extension + '\n'
        for name in list(sorted(dictionary[extension])):
            txt += '- - - ' + name + '.' + extension + '\n'
    return txt


path = input()
info = dict()

build_dict(info, path)
text = build_text(info)

report_path = r'/home/rei/Desktop/SoftUni/Advanced/02. Exercises/06. File Handling/report.txt'

with open(report_path, 'w') as x:
    x.write(text)
