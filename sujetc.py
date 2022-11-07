print("********SujetC*********")
n = 0
#Saisir un nombre superieur a 0
while n<=0:
    n = int(input("Donner un nombre sup a 0: "))
m=n
s=0
i=0
q=n
while True :
    i=i+1
    q = n//10
    r = n % 10 
    if i == 1:
        l=r    #Conserver le premier reste pour la multiplication
    s = s*10+r #determiner le symetrique de i
    n = q
    if q==0:
        break
if s == m and s == m*l : #Verifier si le symetrique egal le nombre saisi n et egal la multiplication de n a le premier reste l
    print(f"{m} est un entier propre et symetrique")
elif s==m : #Verifier si le symetrique egal le nombre saisi n 
    print(f"{m} est un entier symetrique")
elif s == m*l: #Verifier si la multiplication de n a le premier reste l = le symetrique s
    print(f"{m} est un entier propre")
else: #si le nombre ni symetrique ni propre
    print(f"{m} ni symetrique ni propre")
