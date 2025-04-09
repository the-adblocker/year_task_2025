import pygame


# brukt input() til å hente data fra brukeren og lagre i passende variabelnavn
navn = input("Hei! Hva heter du?")
# ??? (Bruk input for å la brukeren skrive inn sitt navn)

alder = input("Hvor gammel er du?")
# ??? (Bruk input og konverter til et heltall)

favorittfarge = input("Hva er din favorittfarge?")
# ??? (Bruk input for å lagre fargen)

print(f"Hei {navn}, du er {alder} år gammel og liker {favorittfarge}!")

# Start Pygame
pygame.init()
BREDDE, HØYDE = 500, 500
skjerm = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Pygame Test")

# Hovedløkke
kjører = True
while kjører:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False

pygame.quit()