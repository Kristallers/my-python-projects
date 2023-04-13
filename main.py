from random import *
# gissa talet
tal = 14
# problem, kommer alltid bli 14, men vi vill slumpa fram, kan ha 14 så länge
gissning = int(input("gissa vilket tal det är: "))
# så länge denna person inte gissat på rätt tal vill vi ge den ett meddelande
# så länge det här () villkoret är uppfyllt är vi kvar i loopen
while (gissning != tal):
    if (gissning > tal):
        print("Fel, du gissade för högt! Försök igen: ")
        gissning = (int(input()))
    else:
        print("Fel, du gissade för lågt! Försök igen: ")
        gissning = (int(input()))
# om man kommer ur loopen har man ju gissat rätt, så länge man inte gissar 14 är man fast i loopen
print("Ja, det var rätt!")
# nu ska vi göra svårare, måste kunna slumpa ett tal

talet = randint(1, 100)
gissningen = int(input("gissa vilket tal det är: "))
# så länge denna person inte gissat på rätt tal vill vi ge den ett meddelande
# så länge det här () villkoret är uppfyllt är vi kvar i loopen
while (gissningen != talet):
    if (gissningen > talet):
        print("Fel, du gissade för högt! Försök igen: ")
        gissningen = (int(input()))
    else:
        print("Fel, du gissade för lågt! Försök igen: ")
        gissningen = (int(input()))
# om man kommer ur loopen har man ju gissat rätt, så länge man inte gissar 14 är man fast i loopen
print("Ja, det var rätt!")

# vi använder while för vi vet inte hur länge vi ska vara kvar i loopen
