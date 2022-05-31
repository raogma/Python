from re import findall, IGNORECASE

path_words = r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\05. Word Count\words.txt'
path_text = r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\05. Word Count\input.txt'
path_output = r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\05. Word Count\output.txt'
with open(path_words) as searched:
    words = searched.read().split()

info = dict()

with open(path_text) as text:
    for line in text:
        for word in words:
            count = findall(fr'\b{word}\b', line, IGNORECASE)
            if word not in info:
                info[word] = len(count)
            else:
                info[word] += len(count)

sorted_info = dict(sorted(info.items(), key=lambda el: el[1], reverse=True))

output_text = str()
for word in sorted_info:
    output_text += f'{word} - {sorted_info[word]}\n'

with open(path_output, 'w') as file:
    file.write(output_text)