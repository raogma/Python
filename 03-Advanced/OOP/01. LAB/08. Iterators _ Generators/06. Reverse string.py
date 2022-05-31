# I.
def reverse_text(string):
    index = len(string) - 1
    while index >= 0:
        yield string[index]
        index -= 1


# II.
# reverse_text = lambda string: (string[i] for i in range(len(string) - 1, -1, -1))

# for char in reverse_text("step"):
#     print(char, end='')

print(''.join(reverse_text('step')))

# връща всичко наведнъж без да излиза от fn... вижда се с дебъг