year = input() #leap or normal
total_holidays = int(input()) #p
weekends_village = int(input()) #h

total_weekends = 48
weekends_sofia = total_weekends - weekends_village

sat_sofia_games = 3/4 * weekends_sofia
hol_sofia_games = 2/3 * total_holidays
sun_village_games = weekends_village
total_games = sat_sofia_games + hol_sofia_games + sun_village_games

if year == "leap":
    total_games *= 1.15
    print(int(total_games))
elif year == "normal":
    print(int(total_games))