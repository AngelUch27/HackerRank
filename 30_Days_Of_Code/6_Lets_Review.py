# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true
n = int(input())

def divisor(cad):
    even = ''
    odd= ''
    for i in range(len(cad)):
        if i%2==0:
            even+=cad[i]
        else:
            odd+=cad[i]
    print(even, odd)
        
for i in range(n):
    cad = input()

    divisor(cad)
    cad = ''
        
        
    
