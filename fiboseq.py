n=int(input("Enter the no.of.terms:"))
n1,n2=0,1
count=0
if n<=0:
    print("Enter a positive integer: ")
elif n==1:
    print("Fibonacci sequence upto",n,":")
    print(n1,end=' ')
else:
    print("Fibonacci sequence:")
    while count<n:
        print(n1,end=' ')
        t=n1+n2
        n1=n2
        n2=t
        count=count+1
