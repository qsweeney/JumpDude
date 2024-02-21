import pygame
from incriment import Counter

pygame.init()

player_ocilate = Counter(400, 500)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Jump Dude')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Resources/mountain_background.png')
sky_surface = pygame.transform.scale(sky_surface, (800, 400))

ground_surface = pygame.image.load('Resources/ground.png')

player_surface = pygame.image.load('Resources/Player/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom = (100,290))
player_gravity = 0

snail_surface =pygame.image.load('Resources/Snail/snail1.png')
snail_rect = snail_surface.get_rect(midbottom = (500,290))

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Game Over', True, 'Black')
textRect = text.get_rect()

game_active = True 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 290:
                player_gravity = -20

            
                
        
    if game_active:
        screen.blit(ground_surface, (0, 280))
        screen.blit(sky_surface, (0,-110))
        
        snail_rect.left -= 5
        if snail_rect.left < -100:
            snail_rect.left = 900
        screen.blit(snail_surface, snail_rect)
        

        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom > 290:
            player_rect.bottom = 290

        screen.blit(player_surface, player_rect)
    
        if snail_rect.colliderect(player_rect):
            game_active = False

        pygame.display.update()
        clock.tick(60)
    
    else: 
        screen.blit(text, textRect)