import math
class bank_account():
    def __init__(self,owner,balance,dep_amt,withdraw_amt):
        self.owner=owner
        self.balance=balance
        self.dep_amt=dep_amt
        self.withdraw_amt=withdraw_amt
    def deposit(self):
        self.balance=self.balance+self.dep_amt
        print("Toatal Amount:",self.balance)
    def withdraw(self):
        self.balance=self.balance-self.withdraw_amt
        print("Remaining Amount:",self.balance)
import math
class cone():
    def __init__(s,r,h):
        s.r=r
        s.h=h
    def volume(s):
        v=math.pi*s.r*s.r*(s.h/3)
        print(v)
    def surface_area(s):
        sa=math.pi*s.r*s.r
        print(sa)
    def side(s):
        s=math.pi*s.r*math.sqrt(s.r*s.r+s.h*s.h)
        print(s)
