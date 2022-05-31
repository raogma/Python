words = input().split()
keyword = input()
counter = 0

palindromes_l = [word for word in words if word == word[::-1]]

print(palindromes_l)
print(f"Found palindrome {palindromes_l.count(keyword)} times")
