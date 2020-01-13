month=input("enter the month:");
list1=["january","march","may","july","august","october","december"];
list2=["april","june","september","november"];
if month in list1:
    days=31;
elif month in list2:
    days=30;
else:
    days=28;
print("no. of days=",days);
