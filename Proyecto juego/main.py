import pygame
import random
import math
from pygame import mixer
import io


def fuente_a_byte(fuente):
    with open(fuente, 'rb') as f:
        ttf_byte = f.read()
    return io.BytesIO(ttf_byte)



# inicializar pygame
pygame.init()

#crear pantalla
pantalla = pygame.display.set_mode((800,600))

#titulo e icono
pygame.display.set_caption("Invación espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

#agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)
#Jugador
img_jugador = pygame.image.load("cohete.png")
pos_jugador_x = 368
pos_jugador_y = 520
jugador_x_cambio = 0

def jugador(x, y):
    pantalla.blit(img_jugador,(x,y))
#Enemigo
img_enemigo = []
pos_enemigo_x = []
pos_enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    pos_enemigo_x.append(random.randint(0,736))
    pos_enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))
    
#bala   
img_bala = pygame.image.load("bala.png")
pos_bala_x = 0
pos_bala_y = 500
bala_y_cambio = 3
bala_visible = False


def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16,y + 10))


#colision
def colision(x1,y1,x2,y2):
    distancia = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    if distancia < 27:
        return True
    else:
        return False
    
#puntaje
puntaje = 0
fuente_como_byte = fuente_a_byte("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_byte, 32)
texto_x = 10
texto_y = 10

def mostrar_puntaje(x,y):
    texto = fuente.render(f"puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))
    
    
#texto final juego    
fuente_final = pygame.font.Font(fuente_como_byte, 40)
def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60,200))    
    
    
#loop del juego
se_ejecuta = True

while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
            
        #Evento precionar y soltar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
            if evento.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound("disparo.mp3")
                sonido_disparo.play()
                if not bala_visible:
                    pos_bala_x = pos_jugador_x
                    disparar_bala(pos_bala_x, pos_bala_y)
        if evento.type == pygame.KEYUP:
             if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                 jugador_x_cambio = 0
            
                 
                 
    #fondo de pantalla
    pantalla.blit(fondo, (0,0))

    #Modificar ubicacion
    pos_jugador_x += jugador_x_cambio
    
    #Mantener dentro pantalla
    if pos_jugador_x <=0:
        pos_jugador_x = 0
    elif pos_jugador_x >=736:
        pos_jugador_x = 736
        
    for e in range(cantidad_enemigos):
        
        #fin del juego
        if pos_enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                pos_enemigo_y[k]=1000
            texto_final()
            break
        pos_enemigo_x[e] += enemigo_x_cambio[e]
    
        if pos_enemigo_y[e] >= 600:
            pos_enemigo_y[e] = pos_enemigo_y[e]
        #Mantener dentro pantalla
        if pos_enemigo_x[e] <=0:
            enemigo_x_cambio[e] = 0.3
            pos_enemigo_y[e] += enemigo_y_cambio[e]
        elif pos_enemigo_x[e] >=736:
            enemigo_x_cambio[e] = -0.3
            pos_enemigo_y[e] += enemigo_y_cambio[e]
            #verificacion colision
        colisionar = colision(pos_enemigo_x[e], pos_enemigo_y[e],pos_bala_x,pos_bala_y)
        if colisionar:
            sonido_colision = mixer.Sound("golpe.mp3")
            sonido_colision.play()
            pos_bala_y = 500
            bala_visible = False
            puntaje += 1
            pos_enemigo_x[e] = random.randint(0,736)
            pos_enemigo_y[e] = random.randint(50,200)
            #Meter enemigo en pantalla
        enemigo(pos_enemigo_x[e], pos_enemigo_y[e],e)
            
    if pos_bala_y <= -64:
        pos_bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(pos_bala_x, pos_bala_y)
        pos_bala_y -= bala_y_cambio
        
    mostrar_puntaje(texto_x, texto_y)
    #Meter jugador en pantalla
    jugador(pos_jugador_x,pos_jugador_y)

    
    #Actualizar juego
    pygame.display.update()
            
