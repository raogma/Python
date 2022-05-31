text_path = r'/home/rei/Desktop/SoftUni/Advanced/02. Exercises/06. File Handling/Files/02. Line Numbers Files/text.txt'
output_path = r'/home/rei/Desktop/SoftUni/Advanced/02. Exercises/06. File Handling/Files/02. Line Numbers Files/output.txt'
line_count = 0

with open(text_path) as read_file:
    while True:
        line = read_file.readline()
        letters = [x for x in line if x.isalpha()]
        punc_marks = [x for x in line if x in ',.?!-;:\'\"']
        line_count += 1
        if not line:
            break
        with open(output_path, 'a') as write_file:
            write_file.write(f'Line {line_count}: {line[:-2]} ({len(letters)})({len(punc_marks)})\n')
