# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
total = int(input())
for i in range(total):
    n = int(input())
    aux = 2
    condicion = True
    
    if n<=1:
        print("Not prime")
        continue
    while aux<=n**.5:
        if n%aux==0:
            condicion = False
            print("Not prime")
            break
        aux+=1
    if condicion:
        print('Prime')
        
