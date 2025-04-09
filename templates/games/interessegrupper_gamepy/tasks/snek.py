import pygame
import random

# Initialiser pygame
pygame.init()

# Skjermstørrelse
BREDDE, HØYDE = 600, 400
BLOKK_STØRRELSE = 20

# Farger
HVIT = (190, 180, 210)
GRØNN = (30, 190, 50)
RØD = (190, 30, 50)
SVART = (15, 10, 20)

# Opprette skjerm
skjerm = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Snake Spill")

# Klokke for FPS
klokke = pygame.time.Clock()

# Slange - starter med tre segmenter
slange = [(100, 100), (80, 100), (60, 100)]
slange_retning = (BLOKK_STØRRELSE, 0)

# Funksjon for å generere mat på et tilfeldig sted
def generer_mat():
    maks_x = (BREDDE - BLOKK_STØRRELSE) // BLOKK_STØRRELSE
    maks_y = (HØYDE - BLOKK_STØRRELSE) // BLOKK_STØRRELSE
    tilfeldig_x = random.randint(0, maks_x) * BLOKK_STØRRELSE
    tilfeldig_y = random.randint(0, maks_y) * BLOKK_STØRRELSE
    return (tilfeldig_x, tilfeldig_y)

# Mat
# mangler kode her
poengsum = 0
mat_posisjon = generer_mat()
# Spill-løkke
spiller_kjører = True
while spiller_kjører:
    skjerm.fill(SVART)
    
    # Håndtere hendelser fra brukerinput
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            # Avslutter spillet dersom brukeren lukker vinduet
            spiller_kjører = False
        elif hendelse.type == pygame.KEYDOWN:
            # Endrer slangeretningen basert på piltaster
            if hendelse.key == pygame.K_LEFT and slange_retning != (BLOKK_STØRRELSE, 0):
                slange_retning = (-BLOKK_STØRRELSE, 0)
            elif hendelse.key == pygame.K_RIGHT and slange_retning != (-BLOKK_STØRRELSE, 0):
               slange_retning = (BLOKK_STØRRELSE, 0)
            elif hendelse.key == pygame.K_UP and slange_retning != (0, BLOKK_STØRRELSE):
                slange_retning = (0, -BLOKK_STØRRELSE)
            elif hendelse.key == pygame.K_DOWN and slange_retning != (0, -BLOKK_STØRRELSE):
               slange_retning = (0, BLOKK_STØRRELSE)
    
    # Flytte slangen i gjeldende retning
    nytt_hode = (slange[0][0] + slange_retning[0], slange[0][1] + slange_retning[1])
    
    # Sjekke kollisjon med seg selv eller vegger
    if nytt_hode in slange or nytt_hode[0] < 0 or nytt_hode[0] >= BREDDE or nytt_hode[1] < 0 or nytt_hode[1] >= HØYDE:
        print(f"Game Over! Poengsum: {poengsum}")
        spiller_kjører = False
        break
    
    # Legge til nytt hode i slangen
    slange.insert(0, nytt_hode)
    
    # Sjekke om mat blir spist
    if nytt_hode == mat_posisjon:
        poengsum += 1
        mat_posisjon = generer_mat()  # Generere ny mat
    else:
        slange.pop()  # Fjerne siste segment hvis mat ikke ble spist
    
    # Tegne slangen på skjermen
    for segment in slange:
        pygame.draw.rect(skjerm, GRØNN, (segment[0], segment[1], BLOKK_STØRRELSE, BLOKK_STØRRELSE))
    
    # Tegne mat på skjermen
    pygame.draw.rect(skjerm, RØD, (mat_posisjon[0], mat_posisjon[1], BLOKK_STØRRELSE, BLOKK_STØRRELSE))
    
    # Oppdatere skjermen med nye endringer
    pygame.display.flip()
    
    # Kontrollere spillets hastighet (10 bilder per sekund)
    klokke.tick(10)

# Avslutte pygame etter spillets slutt
pygame.quit()