totalDollars = 0
try:
	dollar=int(raw_input('Enter a dollar amount:'))
except ValueError:
	print "Not a number"
	
for week in range(1,53):
	totalDollars = totalDollars + (dollar * week)
	print 'After ', week, ' weeks, you will have saved $', totalDollars
	
