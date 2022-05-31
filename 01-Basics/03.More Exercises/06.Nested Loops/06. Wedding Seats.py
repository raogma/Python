last_sector = input()   # 65 -> 91
first_sector_rows = int(input())
odd_row_seats = int(input())
even_row_seats = odd_row_seats + 2
total_seats = 0

for sector in range(65, ord(last_sector) + 1):
    for row in range(1, first_sector_rows + 1):
        if row % 2 != 0:
            total_seats += odd_row_seats
            for seat in range(97, 97 + odd_row_seats):
                print(f"{chr(sector)}{row}{chr(seat)}")
        else:
            total_seats += even_row_seats
            for seat in range(97, 97 + even_row_seats):
                print(f"{chr(sector)}{row}{chr(seat)}")
    first_sector_rows += 1
print(total_seats)