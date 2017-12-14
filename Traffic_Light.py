import pygame

screenx = 500
screeny = 600

pygame.init()

screen = pygame.display.set_mode((screenx,screeny))

pygame.display.set_caption("Traffic Light made with Pygame")

pygame.display.update()

green =(0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (208,242,41)
light_yellow = (212,255,2)
circle1=[255,140]
circle2=[255,300]
circle3=[255,460]

def showlight():
    #Draw yellow background for box
    lightbackground = [130,50,250,500]
    pygame.draw.rect(screen,yellow,lightbackground)

    #Draw circle 1
    pygame.draw.circle((screen),(green),circle1,70)

    #Draw circle 2
    pygame.draw.circle((screen),(light_yellow),circle2,70)

    #Draw circle 3
    pygame.draw.circle((screen),(red),circle3,70)

screen_exit = False

while not screen_exit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            screen_exit = True



        screen.fill(blue)

        showlight()
        
        pygame.display.update()
       # clock.tick(60)





pygame.quit()
quit()
