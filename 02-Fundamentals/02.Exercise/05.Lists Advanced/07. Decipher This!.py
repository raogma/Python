secret = input().split()

for element in secret:
    num = ''
    real_msg_l = []
    real_msg = ''
    for i in range(len(element)):
        if 48 <= ord(element[i]) <= 57:
           num += element[i]
           continue
        elif i == len(num):
            real_msg_l += element[-1]
        elif i == len(element) - 1:
            real_msg_l += element[len(num)]
        else:
            real_msg_l += element[i]
    real_msg_l.insert(0, chr(int(num)))
    for word in real_msg_l:
        real_msg += word
    print(real_msg, end=' ')