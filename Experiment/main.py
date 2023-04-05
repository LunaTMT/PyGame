import pygame
  
pygame.init()
  
colour = (255,255,255)
rect_colour = (255,255,0)
Icon = pygame.image.load('images/symbol.jpeg')
image = pygame.image.load("images/image.jpg")


# CREATING CANVAS
canvas = pygame.display.set_mode((1085,814), pygame.RESIZABLE)

pygame.display.set_caption('Rock Paper Scissors ')
pygame.display.set_icon(Icon)

#canvas.fill(color)
#pygame.display.flip()




exit = False
colours = ["blue", "cyan", "green", "black", "magenta", "red", "white", "yellow"]
alpha = [i for i in range(300)]

c_idx = 0
a_idx = 0

  
while not exit:
    canvas.fill(colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    
    
    pygame.Surface.set_alpha(image, alpha[a_idx])
    pygame.time.wait(70)

    canvas.fill(colours[c_idx])
    canvas.blit(image,(0,0))
    

    #pygame.draw.rect(canvas, rect_colour, pygame.Rect(100,100,60,60))
    #pygame.draw.circle(canvas, "blue", (200,200), 25.0, 100)
    pygame.display.update()
    
    #pygame.display.flip()

    c_idx = c_idx+1 if c_idx < len(colours) - 1 else 0
    a_idx = a_idx+1 if a_idx < len(alpha) - 1 else 0

