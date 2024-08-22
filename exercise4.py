#inverse of a three-digit number
import math

num=int(input("enter your number:"))
i=2
res=0

while i>-1:
    r=num%10
    num=num//10
    res=res+r*10**i
    i=i-1
else: print(res)