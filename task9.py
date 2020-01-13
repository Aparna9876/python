odd=0
even=0
for i in (5,6,7,8,9,2,3,1):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("number of even numbers:",even);
print("number of odd numbers:",odd)
