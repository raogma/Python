price_per_kilo_skumriq = float(input())
price_per_kilo_caca = float(input())
kilos_palamud = float(input())
kilos_safrid = float(input())
kilos_midi = int(input())

price_per_kilo_palamud = price_per_kilo_skumriq + 0.6 * price_per_kilo_skumriq
price_per_kilo_safrid = price_per_kilo_caca + 0.8 * price_per_kilo_caca
price_per_kilo_midi = 7.5

total_price = price_per_kilo_palamud * kilos_palamud + price_per_kilo_safrid * kilos_safrid\
    + price_per_kilo_midi * kilos_midi
print(f"{total_price:.2f}")
