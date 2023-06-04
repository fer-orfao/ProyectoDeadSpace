import pygame
import pygame as pg
import random
import time



# INICIA EL JUEGO
pygame.init()

# DIMENSIONES PANTALLA
screen_width = 800
screen_height = 600

# CREAR LA PANTALLA
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dead Space')

# TIPO DE LETRA
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 60)

# COLORES
blanco = (196, 227, 238)
negro = (3, 17, 21)
colorfondo = (8, 99, 130)

# NIVELES

nivel = 1
tick = 2

# POSICION INICIAL NAVE
nave_x = 50
nave_y = screen_height / 2

# POSICION INICIAL Y VELOCIDAD DE ASTEROIDE
asteroide_x = screen_width - 50
asteroide_y = random.randint(20, 580)
asteroide_speed = 3

# POSICION INICIAL Y VELOCIDAD DE ASTEROIDE 2
asteroide2_x = screen_width - 50
asteroide2_y = random.randint(20, 580)
asteroide2_speed = 4

# POSICION INICIAL Y VELOCIDAD DE ASTEROIDE 3
asteroide3_x = screen_width - 50
asteroide3_y = random.randint(20, 580)
asteroide3_speed = 5

# PUNTOS Y VIDAS
puntos = 0
vidas = 3

# BUCLE (LOOP)
game_over = False
clock = pygame.time.Clock()

# RANDOM PARA GENERAR ASTEROIDES
num = random.randint(10,40)

# PANTALLA INICIO
fondopantalla = pygame.image.load("deadspace.jpg").convert() #*********************
screen.blit(fondopantalla, [0,0])  

text = font2.render("DEAD SPACE", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

presionax = font.render("Presiona X para continuar", True, (250,250,250))

pygame.display.flip()


waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                waiting = False

    screen.fill((0, 0, 0))      
    screen.blit(fondopantalla, [0,0])                
    
    screen.blit(text, text_rect)
    screen.blit(presionax, (500, 500)) 
    
    pygame.display.flip()



# PANTALLA 1 

text = font.render("Después de perder nuestro planeta tras el desastre medioambiental...", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

presionax = font.render("Presiona X para continuar", True, (250,250,250))

pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                waiting = False
                   
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(presionax, (500, 500)) 
    pygame.display.flip()

# PANTALLA 2

text = font.render("Eres tu quien debe encontrar un nuevo planeta donde vivir...", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

presionax = font.render("Presiona X para continuar", True, (250,250,250))

pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                waiting = False
                   
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(presionax, (500, 500)) 
    pygame.display.flip()


    
# PANTALLA 3

text = font.render("Solo deberás usar las teclas arriba y abajo para abrirte paso", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

presionax = font.render("Solo si estás preparado, presiona X para continuar", True, (250,250,250))

pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                waiting = False
                   
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(presionax, (255, 500)) 
    pygame.display.flip()

    
# PRIMER NIVEL 

while not game_over:
    # EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True

    # IMAGENES: NAVES Y ASTEROIDES 
    #pygame.display.set_caption('nave')
    nave = pygame.image.load(r'navejuego.png')
    tamaño_cambiado = pygame.transform.scale(nave, (80,50))
    pygame.display.flip() 

    #pygame.display.set_caption('asteroide')
    asteroide = pygame.image.load(r'asteroide.png')
    tamaño_cambiadoasteroide = pygame.transform.scale(asteroide, (50,50))
    pygame.display.flip() 

    #pygame.display.set_caption('asteroide2')
    asteroide2 = pygame.image.load(r'asteroide2.png')
    tamaño_cambiadoasteroide2 = pygame.transform.scale(asteroide2, (60,60))
    pygame.display.flip() 

    #pygame.display.set_caption('asteroide3')
    asteroide3 = pygame.image.load(r'asteroide3.png')
    tamaño_cambiadoasteroide3 = pygame.transform.scale(asteroide3, (40,40))
    pygame.display.flip() 

    #pygame.display.set_caption('fondo juego')
    #imagendefondo = pygame.image.load(r'fondojuego.jpn')
    fondopantalla = pygame.image.load("iniciojuego.jpg").convert() 
   
    # MOVIMIENTO DE LA NAVE 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        nave_y -= 5
    elif keys[pygame.K_DOWN]:
        nave_y += 5

#COLICIONES Y MOVIMIENTOS 

    # COLISION *
    nave_rect = pygame.Rect(nave_x, nave_y, 35, 25)
    asteroide_rect = pygame.Rect(asteroide_x, asteroide_y, 25, 25)
    if nave_rect.colliderect(asteroide_rect):
        vidas -= 1
        if vidas == 0:
            game_over = True
        else:
            asteroide_x = screen_width - 50
            asteroide_y = random.randint(0, screen_height)
    
    # COLISION 2
    nave_rect = pygame.Rect(nave_x, nave_y, 35, 25)
    asteroide2_rect = pygame.Rect(asteroide2_x, asteroide2_y, 25, 25)
    if nave_rect.colliderect(asteroide2_rect):
        vidas -= 1
        if vidas == 0:
            game_over = True
        else:
            asteroide2_x = screen_width - 50
            asteroide2_y = random.randint(0, screen_height)

    # COLISION 3
    nave_rect = pygame.Rect(nave_x, nave_y, 35, 25)
    asteroide3_rect = pygame.Rect(asteroide3_x, asteroide3_y, 25, 25)
    if nave_rect.colliderect(asteroide3_rect):
        vidas -= 1
        if vidas == 0:
            game_over = True
        else:
            asteroide3_x = screen_width - 50
            asteroide3_y = random.randint(0, screen_height)
      

    # MOVIMIENTO ASTEROIDE TAMAÑO 1
    asteroide_x -= asteroide_speed*tick
    if asteroide_x < 0:
        asteroide_x = screen_width - 50
        asteroide_y = random.randint(0, screen_height)
        puntos +=1

    # MOVIMIENTO ASTEROIDE TAMAÑO 2
    asteroide2_x -= asteroide2_speed*tick
    if asteroide2_x < 0:
        asteroide2_x = screen_width - 50
        asteroide2_y = random.randint(0, screen_height)    
        puntos +=1

    # MOVIMIENTO ASTEROIDE TAMAÑO 3
    asteroide3_x -= asteroide3_speed*tick
    if asteroide3_x < 0:
        asteroide3_x = screen_width - 50
        asteroide3_y = random.randint(0, screen_height)   
        puntos +=1

          
# DIBUJOS
    
    #screen.fill(colorfondo)
    screen.blit(fondopantalla, [0,0])
    
    # DIBUJAR NAVECITA
    #pygame.draw.rect(screen, blanco, (nave_x, nave_y, 40, 40))
    screen.blit(tamaño_cambiado, (nave_x, nave_y))

    # DIBUJAR ASTEROIDES
    #asteroide = pygame.draw.circle(screen, negro, (int(asteroide_x), int(asteroide_y)), 25)
    screen.blit(tamaño_cambiadoasteroide, (asteroide_x, asteroide_y))
    #asteroide2 = pygame.draw.circle(screen, negro, (int(asteroide2_x), int(asteroide2_y)), 20)
    screen.blit(tamaño_cambiadoasteroide2, (asteroide2_x, asteroide2_y))
    #asteroide3 = pygame.draw.ellipse(screen, negro, (asteroide3_x, asteroide3_y, 20, 50), 10)
    screen.blit(tamaño_cambiadoasteroide3, (asteroide3_x, asteroide3_y))

    # DUBIJAR VIDAS Y PUNTOS
    puntos_text = font.render('Puntos: ' + str(puntos), True, blanco)
    screen.blit(puntos_text, (10, 10))
    vidas_text = font.render('Vidas: ' + str(vidas), True, blanco)
    screen.blit(vidas_text, (10, 40))

    # ACTUALIZAR PANTALLA
    pygame.display.update()


# SISTEMA DE PUNTOS
    if puntos == 15: #cantidad de asteroides esquivados
        tick +=1 #velocidad 
        puntos = 0
        nivel +=1
        asteroide_x = screen_width - 50
        asteroide2_x = screen_width - 50
        asteroide3_x = screen_width - 50
        if nivel == 4:
            text = font.render("Felicidades, ganaste el juego :)".format(nivel), True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

            screen.fill((0, 0, 0))
            screen.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(3)
            exit()


        text = font.render("NIVEL {}".format(nivel), True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(3)



# PANTALLA FIN DE LA PARTIDA
screen.fill((0, 0, 0))
game_over_text = font.render('Fin del juego :(', True, blanco)
screen.blit(game_over_text, (screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2))

pygame.display.update()


# TIEMPO ANTES DE SALIR
pygame.time.wait(3000)

#
# FIN
#

pygame.quit()