total_pages = int(input())
pages_per_hour = int(input())
days = int(input())
hours_per_day = total_pages / days / pages_per_hour
#totalpages = pages_per_hour * hours_per_day * days
#hours_per_day = total_pages/days/pages_per_hour
print(hours_per_day)