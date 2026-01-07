# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true
n = int(input())
agenda = {}
for _ in range(n):
    entrada = str(input())
    name, phone = entrada.split()
    agenda[name] = phone
    

while True:
    try:
        linea = input().strip()
        
        valor = agenda.get(linea)
        if valor is not None:
            print(linea+"="+valor)
        else:
            print("Not found")

    except EOFError:
        break

