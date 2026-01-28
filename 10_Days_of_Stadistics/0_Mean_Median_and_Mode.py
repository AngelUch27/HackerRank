# https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())
x = list(map(int, input().strip().split()))

# Mean
media = sum(x) / n
x.sort()
# median
mitad = n//2
if n%2 ==1:
    mediana = x[mitad]
else:
    mediana = (x[mitad]+x[mitad-1])/2
    
# mode
contador = 0
maximo =0
moda = 0

i =0

while i < n:
    if x[i] == x[i - 1]:
        contador += 1
    else:
        if contador > maximo or (contador == maximo and x[i - 1] < moda):
            maximo = contador
            moda = x[i - 1]
        contador = 1
    i += 1

    
            
            
    
print(media)
print(mediana)
print(moda)

        

    
