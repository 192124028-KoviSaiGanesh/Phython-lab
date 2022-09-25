month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))
season=" "
if (month == 'March') and (day > 20):
	season = 'summer'
elif (month == 'June') and (day > 21):
	season = 'spring'
elif (month == 'September') and (day > 22):
	season = 'fall'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)
