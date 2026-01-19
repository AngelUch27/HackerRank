#https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true 
# Enter your code here. Read input from STDIN. Print output to STDOUT
r_day, r_month, r_year = map(int, input().split())

er_day, er_month, er_year = map(int, input().split())


if r_year > er_year: 
    
    print(10000)
elif r_month > er_month and r_year==er_year:
    print(500*(r_month-er_month))

elif r_day > er_day and r_year==er_year and r_month == er_month:
    print(15*(r_day-er_day))
else:
    print(0)
    
