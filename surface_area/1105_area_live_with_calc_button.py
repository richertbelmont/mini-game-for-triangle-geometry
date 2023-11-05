import pygame
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Surface Area Calculator")

# List to store the vertices of the user-defined shape
vertices = []

# Function to calculate the surface area in pixel unit
def calculate_area(vertices):
    if len(vertices) <= 0:
        return 0
    elif len(vertices) == 3:
        # Calculate area of a triangle using Heron's formula
        a = math.dist(vertices[0], vertices[1])
        b = math.dist(vertices[1], vertices[2])
        c = math.dist(vertices[2], vertices[0])
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    elif len(vertices) == 4:
        # Handle the case of four vertices (a rectangle)
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        x3, y3 = vertices[2]
        x4, y4 = vertices[3]
        width = abs(x2 - x1)
        height = abs(y3 - y1)
        return width * height
    else:
        # Calculate area of a convex polygon 
        area = 0
        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]
            area += (x1 * y2 - x2 * y1)
        return 0.5 * abs(area)

# Create "Calculate" and "Clear" buttons
calculate_button = pygame.Rect(10, 10, 120, 30)
clear_button = pygame.Rect(140, 10, 80, 30)
button_color = (100, 100, 100)
font = pygame.font.Font(None, 36)
calculate_text = font.render("Calculate", True, WHITE)
clear_text = font.render("Clear", True, WHITE)

# Flags for buttons
calculate_clicked = False
drawing = False
selected_vertex = None

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if calculate_button.collidepoint(x, y):
                # Calculate the area when the "Calculate" button is clicked
                calculate_clicked = True
                drawing = False  # Disable drawing mode
            elif clear_button.collidepoint(x, y):
                vertices = []  # Clear vertices
                area = 0  # Clear the calculated area
                calculate_clicked = False  # Re-enable drawing mode
            else:
                if not calculate_clicked:
                    vertices.append((x, y))
                    selected_vertex = None
                else:
                    selected_vertex = None
            drawing = not drawing
        elif event.type == MOUSEMOTION:
            if drawing and selected_vertex is not None:
                x, y = event.pos
                vertices[selected_vertex] = (x, y)
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the shape
    if len(vertices) > 1:
        pygame.draw.polygon(screen, BLACK, vertices, 1)

    # Draw the "Calculate" and "Clear" buttons
    pygame.draw.rect(screen, button_color, calculate_button)
    screen.blit(calculate_text, (15, 15))
    pygame.draw.rect(screen, button_color, clear_button)
    screen.blit(clear_text, (145, 15))

    if calculate_clicked:
        # Display the calculated area on the screen
        area = round(calculate_area(vertices) / 100) # For scalability
        font = pygame.font.Font(None, 36)
        text = font.render(f"Area: {area}", True, BLACK)
        screen.blit(text, (10, 50))

    # Draw vertices as small circles
    for vertex in vertices:
        pygame.draw.circle(screen, BLACK, vertex, 5)

    pygame.display.update()

# Quit Pygame
pygame.quit()
