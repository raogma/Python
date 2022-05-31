length = int(input())
width = int(input())
height = int(input())
percent_taken_space = float(input())

V_whole = length / 10 * width / 10 * height / 10
V_water = V_whole - percent_taken_space / 100 * V_whole

print(V_water)

# mistake 1: forgot to divide by 10...the user inputs the size in cms so it's gotta be converted in dms (1l = 1dm^3)
