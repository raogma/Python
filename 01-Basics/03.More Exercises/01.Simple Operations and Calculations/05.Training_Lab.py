length_m = float(input())
width_m = float(input())

length_cm = length_m * 100
width_cm = width_m * 100

tables = (width_cm - 100) // 70
rows = length_cm // 120

workspaces = tables * rows - 3
print(int(workspaces))

