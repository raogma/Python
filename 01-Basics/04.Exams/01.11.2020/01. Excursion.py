people = int(input())
overnights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

total_price = people * (overnights * 20 + transport_cards * 1.6 + museum_tickets * 6) * 1.25
print(f"{total_price:.2f}")