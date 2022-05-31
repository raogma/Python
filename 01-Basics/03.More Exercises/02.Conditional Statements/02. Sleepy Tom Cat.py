free_days = int(input())
total_days = 365
play_limit = 30000
work_days = total_days - free_days
play_work = work_days * 63
play_free = free_days * 127
total_play = play_work + play_free
difference_mins = abs(total_play - play_limit)
hours = difference_mins // 60
minutes = difference_mins % 60

if total_play <= play_limit:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
