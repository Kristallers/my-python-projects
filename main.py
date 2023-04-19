def binärsökning(lista, söktal):
    index_början = 0
    index_slut = len(lista) - 1

    while index_början <= index_slut:
        mittpunkt = index_början + (index_slut-index_början) // 2
        mittenvärde = lista[mittpunkt]
        if mittenvärde == söktal:
            print(f"talet finns på plats {mittenvärde} i listan")
            break

        elif söktal < mittenvärde:
            index_slut = mittpunkt - 1

        else:
            index_början = mittpunkt + 1

    return None


tallista = [3, 7, 14, 19, 21, 40, 47, 47, 69, 72, 83, 94, 101]

sök = int(input("Vad vill du söka på?: "))
print(binärsökning(tallista, sök))
