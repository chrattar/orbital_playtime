import pygame
import numpy as np

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Constants
G = 6.67430e-11  # Gravitational constant
M = 5.972e24  # Mass of the central body (Earth)
dt = 6000  # Time step (1 minute per frame)
scale_factor = 2e7  # Scaling to fit the simulation on screen

# Initial Conditions
r_initial = 4.2e9  # 42,000 km from the center (geostationary orbit)
satellite_pos = np.array([width / 2 - r_initial / scale_factor, height / 2], dtype=float)
central_pos = np.array([width / 2, height / 2], dtype=float)  # Center of screen

# Compute correct orbital velocity
r_mag = r_initial  # Actual distance in meters
v_initial = np.sqrt(G * M / r_mag)  # Circular orbit velocity

# Initial velocity should be **perpendicular** to the radius
satellite_vel = np.array([0, -v_initial / scale_factor], dtype=float)

# Simulation Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Compute gravitational force
    r = central_pos - satellite_pos  # Vector from satellite to center
    r_mag = np.linalg.norm(r) * scale_factor  # Actual distance in meters
    F = (G * M / r_mag**3) * r  # Force per unit mass (acceleration)

    # Update velocity and position
    satellite_vel += F * dt
    satellite_pos += satellite_vel * dt

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), tuple(central_pos.astype(int)), 20)  # Central body
    pygame.draw.circle(screen, (255, 0, 255), tuple(satellite_pos.astype(int)), 5)  # Satellite

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
