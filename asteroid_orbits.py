import pygame
import numpy as np

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

##VARIBALE
G = 6.67430e-11 
M = 5.972e24  # Eatrth
dt = 6000  # Timestep 1 min/frame == 365/86,400
scale_factor = 2e7  # scale for scrn

#INITIAL 
r_initial = 4.2e9
satellite_pos = np.array([width / 2 - r_initial / scale_factor, height / 2], dtype=float)
central_pos = np.array([width / 2, height / 2], dtype=float)
#ORBITABL VELOCITY - CORRECT and put int meters to start
r_mag = r_initial 
v_initial = np.sqrt(G * M / r_mag) 
satellite_vel = np.array([0, -v_initial / scale_factor], dtype=float)

#MAIN()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#G froce
    r = central_pos - satellite_pos
    r_mag = np.linalg.norm(r) * scale_factor
    F = (G * M / r_mag**3) * r  

    # Update velocity and position
    satellite_vel += F * dt
    satellite_pos += satellite_vel * dt

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), tuple(central_pos.astype(int)), 20)  # CENTRAL BODY
    pygame.draw.circle(screen, (255, 0, 255), tuple(satellite_pos.astype(int)), 5)  # SATELLITE

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
