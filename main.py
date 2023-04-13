text = input("skriv något")
vokaler = "aeiouyåäö"
for x in text:
    if x in vokaler:
        print(x, end='')
    else:
        print(x + "o" + x, end='')
