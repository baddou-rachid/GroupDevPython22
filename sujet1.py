m=0
n=1
while m<n:
    n = int(input('Donner un nombre supperieur à 4000 '))
    m = int(input('Donner un nombre inferieur à 10000 '))
c=0
s=0
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
        c=0
    else:
        c=0
print("Au revoir si l'éran est vide alors n'existe pas")



