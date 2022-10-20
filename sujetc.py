bi = 10
bs= 1
while bi>bs :
    bi = int(input("Donner un nombre supperieur a 10: "))
    bs = int(input("Donner un nombre inferieur ou egal a 500: "))
for i in range(bi,bs+1):
    c=0
    for j in range(1,i+1):
        if i % j == 0 :
            c=c+1
    m=i
    s=0
    if c == 2 and i<100:
        q=1
        while q != 0:
            q = m//10
            r=m % 10
            s=s*10 + r
            m = q
        k=0
        for j in range(1,s+1):
            if s%j == 0:
                k=k+1
        if k==2 :
            print(i)
    elif c == 2 and i>=100:
        ch = str(i)
        cir1 = ch[1]+ch[2]+ch[0]
        cir2 = ch[2]+ch[0]+ch[1]
        a = int(cir1)
        b = int(cir2)
        x=0
        for l in range(1,a+1):
            if a % l == 0:
                x=x+1
        for l in range(1,b+1):
            if b % l == 0:
                x=x+1
        if x == 4:
            print(i)
            
        
    