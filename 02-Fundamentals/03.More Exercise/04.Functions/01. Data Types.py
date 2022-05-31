def rules_acc_to_type(raw_data, type_data):
    if type_data == 'int':
        return int(raw_data) * 2
    elif type_data == 'real':
        return f'{float(raw_data) * 1.5:.2f}'
    elif type_data == 'string':
        return f'${raw_data}$'


type = input()
data = input()

print(rules_acc_to_type(data, type))