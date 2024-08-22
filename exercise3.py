import math

a=float(input("enter your number:"))
b=float(input("enter your number:"))
c=float(input("enter your number:"))
d=float(input("enter your number:"))

Max= -1*math.inf
Min= math.inf

if a>Max:
    Max=a
if a<Min:
    Min=a

if b>Max:
    Max=b
if b<Min:
    Min=b

if c>Max:
    Max=c
if c<Min:
    Min=c

if d>Max:
    Max=d
if d<Min:
    Min=d

print(Min)
print(Max)

avg=(a+b+c+d)/4
varians=(((a-avg)**2)+((b-avg)**2)+((c-avg)**2)+((d-avg)**2))
print(avg)
print(varians)