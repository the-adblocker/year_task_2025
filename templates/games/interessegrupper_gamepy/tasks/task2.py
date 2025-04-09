import pygame

# Fiks koden: 
# a) firkanten skal være blå
# b) alle piltastene skal funke
# c) firkanten skal være større
# d) firkanten skal ha større fart


# Initialiserer Pygame
pygame.init()

# Skjermoppsett
BREDDE, HØYDE = 800, 600
skjerm = pygame.display.set_mode((BREDDE, HØYDE))

# Farger
HVIT = (190, 180, 210)
BLÅ = (70, 50, 255)

# Spillerens posisjon
spiller_x, spiller_y = 100, 100
spiller_fart = 50

# Spill-løkken
spillet_kjører = True
while spillet_kjører:
    skjerm.fill(HVIT)
    # Håndterer hendelser
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            spillet_kjører = False

    # Bevegelse med piltaster
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller_x -= spiller_fart
    if taster[pygame.K_UP]:
        spiller_y -= spiller_fart
    if taster[pygame.K_RIGHT]:
        spiller_x += spiller_fart
    if taster[pygame.K_DOWN]:
        spiller_y += spiller_fart
        
    # Tegne spilleren
    pygame.draw.rect(skjerm, BLÅ, (spiller_x, spiller_y, 40, 40))
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()