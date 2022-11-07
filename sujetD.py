print("*****Sujet C : Premier circulaire*****")

# Saisir deux entiers bi et bs (10<bi<bs<=500)

while True:
    bi = int(input("Donner un nombre supperieur a 10: "))
    bs = int(input("Donner un nombre inferieur ou egal a 500: "))
    if bi<bs and bi>10 and bs<=500:
        break

#Determiner et afficher les nombres premiers circulaires

for i in range(bi,bs+1):
    c=0
    #determiner si le nombre premier ou non
    for j in range(1,i+1):
        if i % j == 0 :
            c=c+1
    m=i
    s=0
    #determiner les nombres inferieur strict a 100 si premier circulaire ou non
    if c == 2 and i<100:
        q=1
        #determiner le symetrique de nombre
        while q != 0:
            q = m//10
            r=m % 10
            s=s*10 + r
            m = q
        k=0
        #verifier si le symetrique s et premier ou non
        for j in range(1,s+1):
            if s%j == 0:
                k=k+1
        if k==2 : #afficher le nombre i si son symetrique est premier
            print(i)
    #determiner les nombres superieur ou egal a 100 si premier circulaire ou non
    elif c == 2 and i>=100:
        ch = str(i)   #convertir le nombre au chaine caractere
        cir1 = ch[1]+ch[2]+ch[0] # premier changement du contenu de la chaine caractere a l'aide des indices et l'affecter dans la variable cir1
        cir2 = ch[2]+ch[0]+ch[1] # deuxieme changement du contenu de la chaine caractere a l'aide des indices et l'affecter dans la variable cir2
        a = int(cir1) # convertir la chaine de caractere cir1 au entier
        b = int(cir2) # convertir la chaine de caractere cir2 au entier
        x=0
        #Verifier si a et b sont premier
        for l in range(1,a+1):
            if a % l == 0:
                x=x+1
        for l in range(1,b+1):
            if b % l == 0:
                x=x+1
        if x == 4:
            print(i) # Afficher le nombre i si les deux nombres a et b sont premiers
            
        
    
