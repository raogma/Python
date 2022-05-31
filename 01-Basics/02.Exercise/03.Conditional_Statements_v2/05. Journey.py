budget = float(input())
season = input()

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        print(f"Camp - {budget * 0.3:.2f}")
    elif season == "winter":
        print(f"Hotel - {budget * 0.7:.2f}")
elif 100 < budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        print(f"Camp - {budget * 0.4:.2f}")
    elif season == "winter":
        print(f"Hotel - {budget * 0.8:.2f}")

elif budget > 1000:
    print("Somewhere in Europe")
    print(f"Hotel - {budget * 0.9:.2f}")
