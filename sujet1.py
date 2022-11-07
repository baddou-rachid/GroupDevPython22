while True:
    n = int(input('Donner un nombre supperieur à 4000 '))
    m = int(input('Donner un nombre inferieur à 10000 '))
    if n<m and n>4000 and m<=10000:
        break
c=0
s=0
trouve = False
print(f"les nombres super premier s'il existe entre {n} et {m} sont:")
for i in range(n,m+1) :
    for j in range(1,i+1) :
        if i % j == 0 :
            c = c+1
    s=0
    if c == 2 :
        z=i
        q=i
        while q != 0 :
            q = z//10
            z = q
            
            for k in range(1,q+1) :
                if q%k == 0 :
                    s = s+1
        if s==6 :
            print(i)
            trouve = True
        c=0
    else:
        c=0
if trouve == False :
    print(f"Aucun nombre super premier entre {n} et {m}")



