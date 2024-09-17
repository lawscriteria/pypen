import pygame

pygame.init()

vw = 1300; vh = 600
screen = pygame.display.set_mode((vw, vh))

# thickness = 1
s = 3

coords = []

mousedown = False

run = True
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DELETE]:
        screen.fill((0, 0, 0))
    if keys[pygame.K_1]:
        s = 1
    if keys[pygame.K_2]:
        s = 2
    if keys[pygame.K_3]:
        s = 3
    if keys[pygame.K_4]:
        s = 4

    event_codes = pygame.event.get()
    events = []
    for event_code in event_codes:
        events.append(event_code.type)
    
    if pygame.MOUSEBUTTONDOWN in events: # 1025 is the event code for the MOUSEBUTTONDOWN event.
        mousedown = True

    if pygame.MOUSEBUTTONUP in events: # 1026 is the event code for the MOUSEBUTTONUP event.
        mousedown = False

    if mousedown:
        mousepos = pygame.mouse.get_pos()

        coords += [(mousepos[0], mousepos[1])]
        if len(coords) > 1:
            pygame.draw.line(screen, (255, 255, 255), coords[-2], coords[-1], s)

        # ink = pygame.Rect((mousepos[0], mousepos[1], thickness, thickness))
        # pygame.draw.rect(screen, (255, 255, 255), ink, 0, 50)
    else:
        coords = []

    if pygame.QUIT in events: # 256 is the event code for the QUIT event; it is run when a user decides to exit the program.
        run = False

    pygame.display.update()

pygame.quit()