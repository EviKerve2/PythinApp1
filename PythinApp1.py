from keyboard import*
from random import*
def start()
"""Teeme valik kellega mängime
Tagastame m muutuja int formaadis

:rtype: int
"""
print("Kivi, Käärid, Paber")
m=3
while m not in [1,2]:
    try:
        m=int(input("Kellega mängimine?\n1-botid \n2-robotiga"))
    except:
        ValueError
return m
m=start()
if m==1:
    while True:
        print("Kas ")