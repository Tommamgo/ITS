import itertools
summe = 0
würfel = 7  
zähler = 15 
wunsch_sum = 28
betrag_möglichkeiten = 0

omega = itertools.product(range(1,zähler + 1), repeat=würfel)
for x in omega:
    for y in x:
        summe = summe + y 
    if(summe == wunsch_sum):
        betrag_möglichkeiten+=1
    summe = 0
    print(x)
print("So viele Möglichkeiten gibt es: " + str(betrag_möglichkeiten))

warsch = betrag_möglichkeiten / zähler**würfel
print("die Warscheinlichkeit liegt bei: " + str(warsch))
    

