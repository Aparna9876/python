list=[];
i=0;
while(i<3):
    a=int(input("enter the number one by one:\n"));
    list.append(a);
    i=i+1;
list.sort();
print(list);
print("\n The median of the given values is:",list[1]);

        
