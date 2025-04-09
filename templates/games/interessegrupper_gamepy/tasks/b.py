
print("Velkommen til tallspillet!")

bruker_tall = int(input("Skriv inn et tall mellom 1 og 10: "))

# denne if-testen gjør ikke helt det den skal. hvordan kan du fikse det?
if bruker_tall >= 1 and bruker_tall <= 10:
    print("Bra valg!")
else:
    print("Tallet er ikke mellom 1 og 10, prøv igjen!")

# denne løkka skal telle opp tallet brukeren har oppgitt, men den stopper for tidlig?
print("Vi teller opp til ditt tall:")
for i in range(1, bruker_tall):  # Feil: stopper for tidlig
    print(i)

# hvorfor øker ikke denne telleren?
teller = 0
while teller < bruker_tall:  
    teller += 1
    print("Teller: ", teller)

# hva skjer hvis du tester med 18?
alder = int(input("Hvor gammel er du? "))
if alder >= 18:
    print("Du har tilgang!")
if alder < 18:
    print("Beklager, du må være over 18 for tilgang.")

# hvorfor stopper denne løkka ikke på 1?
print("Vi teller ned fra ditt tall til 1:")
for i in range(bruker_tall, 0, -1):  # Feil: range() er satt feil
    print(i)
    

print("Programmet er ferdig. Fiks feilene for å få det til å kjøre riktig!")