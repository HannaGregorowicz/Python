def test(listadzieci,listaciastek):
    listahelpdzieci=[]
    listahelpciastka=[]
    liczbazadowolonychdzieci=0

    for x in range(0,10):                   #Dodaje dzieci i ciastka do listy pomocnicznej
        listahelpdzieci.append(0)
        listahelpciastka.append(0)

    for x in range(0,len(listadzieci)):
        listahelpdzieci[listadzieci[x]-1]+=1

    for x in range(0,len(listaciastek)):
        listahelpciastka[listaciastek[x]-1]+=1  #dla każdego ciastka/dziecka zwiększa liczbę w tablicy indexowej

    print("Ciastka: "+str(listaciastek))
    print("Dzieci: "+str(listadzieci))

    for x in range(0,len(listahelpdzieci)): #dla każdej liczby
        y=len(listahelpdzieci)-x-1
        for z in range(0,listahelpdzieci[y]):   #dla każdego dziecka
            for a in range(0,len(listahelpdzieci)-y): #dla każdego ciastka większego od łakomstwa dziecka
                if listahelpciastka[len(listahelpdzieci)-a-1]>0:
                    listahelpciastka[len(listahelpdzieci)-a-1]-=1
                    liczbazadowolonychdzieci+=1
                    break

    print("\nMaksymalna liczba zadowolonych dzieci: "+str(liczbazadowolonychdzieci)+"\n")
