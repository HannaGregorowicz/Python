from string import ascii_letters
from random import choice, randint

def compress(string):
    if string.isalpha()==False:
        return None
    else:
        a=0
        liczba=0
        compressed=""
        for i in range(a,len(string)):
            if(string[a] is string[i]):
                liczba+=1
            if string[a] is not string[i]:
                compressed+=string[a]+str(liczba)
                liczba=1
                a=i
            if i==len(string)-1:
                compressed+=string[a]+str(liczba)
    return compressed


def decompress(string):
    decomp=""
    for i in range(0,len(string),2):
        decomp+=string[i]*int(string[i+1])
    return decomp


def test(n):
    wynik=[]
    for y in range(0,n):
        ra=randint(0, len(ascii_letters)-1)
        wynik.append(ascii_letters[ra])
    wynik="".join(wynik)
    kompres = compress(str(wynik))
    dekompres = decompress(str(kompres))
    if wynik == dekompres:
        print("Test zakonczony pomyślnie")
    else:
        print("Błąd!")

