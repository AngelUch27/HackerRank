#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    lista=[]
    for i in range(N):
        entrada = input().strip()
        partes = entrada.split()
        
        if partes[0] == 'print':
            print(lista)
            continue
        if partes[0] == 'sort':
            lista.sort()
            continue
        if partes[0] == 'pop':
            lista.pop()
            continue
        if partes[0] == 'reverse':
            lista.reverse()
            continue
        
        if partes[0] == 'remove':
            lista.remove(int(partes[1]))
            continue
        if partes[0] == 'append':
            lista.append(int(partes[1]))
            continue
        
        if partes[0] == 'insert':
            lista.insert(int(partes[1]),int(partes[2]))
        
