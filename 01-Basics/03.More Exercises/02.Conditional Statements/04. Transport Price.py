total_kms = int(input())
time = input()

price = 0

if total_kms < 20:
    if time == "day":
        price = 0.7 + total_kms * 0.79
    elif time == "night":
        price = 0.7 + total_kms * 0.9

elif 20 <= total_kms < 100:
    price = total_kms * 0.09

elif total_kms >= 100:
    price = total_kms * 0.06

print(f"{price:.2f}")
