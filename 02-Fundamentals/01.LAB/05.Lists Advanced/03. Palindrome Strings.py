string = input()
keyword = input()

str_l = string.split()
palindrome_l = []
counter = 0


def reverse(text):
    reversed_text = ''
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text


for element in str_l:
    if keyword == element:
        counter += 1
    if element == reverse(element):
        palindrome_l.append(element)

print(palindrome_l)
print(f"Found palindrome {counter} times")
