import random
import sys


def listy(M=None,N=None):               #funkcja generująca ciastka i dzieci
    if M is None:
        M=random.randint(1,10)
    if N is None:
        N=random.randint(1,10)
    dzieci=[]
    ciastka=[]
    for x in range(0,M):
        dzieci.append(random.randint(1,10))
    for x in range(0,N):
        ciastka.append(random.randint(1,10))    #wypelnia tablice
    wynik=[dzieci,ciastka]
    return wynik


