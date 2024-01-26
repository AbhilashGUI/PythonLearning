##Write a progam to find out how may days, weeks and months. We have left, if we live for util 90 years

##Input=Currentage
##1year=365 days,12months,52weeks



age=int(input("Enter the current age :"))

years_left=60-age
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52

print(f"You have left {years_left} years,{days_left} days,{months_left} months and {weeks_left} weeks")
