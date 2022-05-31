def palindrome(element):
    reversed_element = ""
    for symbol in range(len(element) - 1, -1, -1):
        reversed_element += element[symbol]
    return True if reversed_element == element else False


input_text = input().split(", ")

for input_element in input_text:
    print(palindrome(input_element))