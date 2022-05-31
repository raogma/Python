countries = input().split(', ')
capitals = input().split(', ')

result = list(zip(countries, capitals))
[print(' -> '.join(element)) for element in result]