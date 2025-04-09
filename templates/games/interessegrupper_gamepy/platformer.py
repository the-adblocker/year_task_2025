import pygame
import random

pygame.font.init()

FONT = pygame.font.SysFont("micro 5 regular", 60)

# framerate
clock = pygame.time.Clock()
fps = 24

frames_alive = 0

# set screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("the awesomesauce")

# colors
lblu = (190, 180, 210)
blu = (70, 50, 255)
red = (225, 40, 70)
gred = (200, 45, 80)
gray = (50, 35, 50)


# moving
player_x, player_y = 400, 400
player_speed = 10
player_jump = 5
gforce = 0.1
jump_buffer = 0

ground_xl = 300
ground_xr = 500
ground_y = 400
ground_move = 1

dangerzone_xl = 0
dangerzone_xr = 50
dangerzone_y = 390
dangerzone_move = 1.5

pushzone_xl = 700
pushzone_xr = 770
pushzone_y = 350
pushzone_move = 1.8

dangerdif = 400


#images
bg_img = pygame.image.load('img/bg.png').convert_alpha()
player = pygame.image.load('img/mr_eggr.png').convert_alpha()
ground_img = pygame.image.load('img/ground.png').convert_alpha()

score = frames_alive/2

# jump
# def jump(plusheight):
#     gforce = 0
#     player_jump = 20 + plusheight
#     jump_buffer = 0
#     player_jump -=1
#     player_y -= player_jump
    # elif jump_buffer > 0:
    #     if grounded:
    #         if player_jump <= 0:
    #             player_jump = 20
    #         else:
    #             player_jump -=1
    #             player_y -= player_jump
    #     jump_buffer -= 1




# gameplay
game_playing = True
while game_playing:
    screen.fill(lblu)
    
    # gforce = gforce+0.3
    gforce = gforce+0.4
    gforce = gforce*1.03
    # if gforce >= 20:
    #     gforce = 20


    # collision and grounding of player
    if (player_y >= ground_y + 30) and (player_x <= ground_xr)and (player_x >= ground_xl):
        if (player_x >= ground_xr-5) and (player_y >= ground_y+40): 
            player_x = ground_xr+15 # need finetuning with numbers
        elif (player_x <= ground_xl+5) and (player_y >= ground_y+40):
            player_x = ground_xl-15
        else:
            gforce = 0 
            grounded = True
            player_y = ground_y+30
    elif (player_y <= ground_y + 40) and (gforce == 1):
        gforce += 0.1
        grounded = False
    else:
        grounded = False

    if (player_y >= pushzone_y + 30) and (player_x <= pushzone_xr)and (player_x >= pushzone_xl):
        if (player_x >= pushzone_xr-5) and (player_y >= pushzone_y+40): 
            player_x = pushzone_xr+15 # need finetuning with numbers
        elif (player_x <= pushzone_xl+5) and (player_y >= pushzone_y+40):
            player_x = pushzone_xl-15


    if (player_y >= dangerzone_y + 30) and (player_x <= dangerzone_xr)and (player_x >= dangerzone_xl):
        game_playing = False
    if (player_y >= dangerzone_y + 30) and (player_x <= dangerzone_xr+dangerdif)and (player_x >= dangerzone_xl+dangerdif):
        game_playing = False
    if (player_y >= dangerzone_y + 30) and (player_x <= dangerzone_xr-dangerdif)and (player_x >= dangerzone_xl-dangerdif):
        game_playing = False


    #applies gravity    
    player_y += gforce



    # move
    keyinput = pygame.key.get_pressed()
    if keyinput[pygame.K_LEFT]:
        if grounded:
            player_x -= player_speed
            player = pygame.image.load('img/mr_eggl.png').convert_alpha()
        else:
            player_x -= player_speed*0.91 # multiply by something other than 1 for air drift


    if keyinput[pygame.K_RIGHT]:
        if grounded:
            player = pygame.image.load('img/mr_eggr.png').convert_alpha()
            player_x += player_speed
        else:
            player_x += player_speed*0.91


    if keyinput[pygame.K_UP]:
        if grounded:
            player = pygame.image.load('img/mr_egg_jump.png').convert_alpha()
            # jump(0)
            gforce = 0
            player_jump = 20
        else:
            jump_buffer = 4

    
    # reset position
    if keyinput[pygame.K_r]:
        player_x = (ground_xl+ground_xr)/2
        player_y = ground_y + 30



     
    # # jump
    if player_jump > 0:
        jump_buffer = 0
        player_jump -=1
        player_y -= player_jump
    elif jump_buffer > 0:
        if grounded:
            if player_jump <= 0:
                player_jump = 20
            else:
                player_jump -=1
                player_y -= player_jump
        jump_buffer -= 1


    #ground_move = random.randint(-5, 5)

    ground_xl += ground_move
    ground_xr += ground_move

    if grounded:
        player_x += ground_move*0.9

    if ground_xl <= (-30):
        ground_move = ground_move * (-1.08)
    elif ground_xr >= width:
        ground_move = ground_move * (-1.08)



    dangerzone_xl += dangerzone_move
    dangerzone_xr += dangerzone_move
    if dangerzone_xl <= (-30):
        dangerzone_move = dangerzone_move * (-1.2)
        dangerzone_y = dangerzone_y*0.99
    elif dangerzone_xr >= width:

        #loop
        dangerzone_xl -= 400
        dangerzone_xr -= 400
        dangerzone_move = dangerzone_move * (1.1)

        #ping pong
        # dangerzone_move = dangerzone_move * (-1.2)

        dangerzone_y = dangerzone_y*0.99

    pushzone_xl += pushzone_move
    pushzone_xr += pushzone_move
    if pushzone_xl <= (-30):
        pushzone_move = pushzone_move * (-1.1)
        pushzone_y = pushzone_y*(1+(random.randint(-2, 2)/150))
    elif pushzone_xr >= width:
        pushzone_move = pushzone_move * (-1.1)
        pushzone_y = pushzone_y*(1+(random.randint(-2, 2)/150))

    # make the guy


    #draw_guy(player_x, player_y)
    # pygame.draw.rect(screen, red, (ground_xl+30, ground_y+60, ground_xr-ground_xl-30, 290))
    
    # pygame.draw.rect(screen, blu, (player_x, player_y, 30, 30))
    screen.blit(bg_img, (0, 0))
    screen.blit(ground_img, (ground_xl+30, ground_y+60))
    screen.blit(player, (player_x, player_y))
    pygame.draw.rect(screen, blu, (pushzone_xl+30, pushzone_y+60, pushzone_xr-pushzone_xl-30, 290))
    pygame.draw.rect(screen, red, (dangerzone_xl+30, dangerzone_y+60, dangerzone_xr-dangerzone_xl-30, 290))
    pygame.draw.rect(screen, gred, (dangerzone_xl+30+dangerdif, dangerzone_y+60, dangerzone_xr-dangerzone_xl-30, 290))
    pygame.draw.rect(screen, gred, (dangerzone_xl+30-dangerdif, dangerzone_y+60, dangerzone_xr-dangerzone_xl-30, 290))
    
    score = int(frames_alive/12)
    score = str(score)
    score_text = FONT.render((score), 1, gray)
    screen.blit(score_text, (width-20-score_text.get_width(), 20))

    pygame.display.flip()

    clock.tick(fps)
    frames_alive += 1 

    for happens in pygame.event.get():
        if happens.type == pygame.QUIT:
            game_playing = False
    
    if player_y >= height + 20:
        game_playing = False

pygame.quit()
print("frames alive:", frames_alive)
print("score:", score)