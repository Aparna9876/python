def fibonacci():
    n=int(input("Enter,how many terms"))
    n1=0
    n2=1
    count=0
    if n<=0:
        print("Please enter positive integer")
    elif n==1:
        print("Fibonacci sequence up to",n,":")
        print(n1)
    else:
        print("Fibonaccisequence:")
        while count<n:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
