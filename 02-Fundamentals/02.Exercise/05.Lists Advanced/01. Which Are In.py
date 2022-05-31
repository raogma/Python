first_words = input().split(', ')
second_words = input()

new_list = [word for word in first_words if word in second_words]

print(new_list)