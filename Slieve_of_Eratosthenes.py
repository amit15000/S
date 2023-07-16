n=int(input("Enter the limit: "))
prime=[]
for i in range(n+1):
    prime.append(i)
prime[0]=0
prime[1]=0
p=2


while p*p<=n:
    if p!=0:
        for i in range(p*2,n+1,p):
            prime[i]=0
    
    p=p+1

print("All the prime numbers upto", n , "are: ")
for i in range(n+1):
    if prime[i]!=0:
        print(prime[i], end=" ")
        

        
    