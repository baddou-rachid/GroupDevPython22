print("********SujetC*********")
n = 0
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
        l=r
    s = s*10+r
    n = q
    if q==0:
        break
if s == m and s == m*l :
    print(f"{m} est un entier propre et symetrique")
elif s==m :
    print(f"{m} est un entier symetrique")
elif s == m*l:
    print(f"{m} est un entier propre")
else:
    print(f"{m} ni symetrique ni propre")
