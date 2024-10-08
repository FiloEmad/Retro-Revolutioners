import os.path
import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
FONT_SIZE = 32
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Text Input in Pygame')

# Font and text variables
font = pygame.font.Font(None, FONT_SIZE)
user_file = ''





input_rect = pygame.Rect(150, 300, 400, 50)
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('dodgerblue2')
color = color_inactive
active = False

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)
    Txt = (pygame.font.SysFont('None', 50).render('ENTER YOUR NAME', True, (100, 200, 250))
           )
    screen.blit(Txt,(200,50))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicks on the input box, toggle active status
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            # Change the input box color when clicked
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            # If active and the user presses a key, add it to the text
            if active:
                if event.key == pygame.K_RETURN:
                    with open('main_file.txt', 'w+') as main_file:
                        main_file.write(user_file + 'SNAAKE')
                        main_file.write('\n' + user_file + 'SUDOKU')
                        main_file.close()
                        user_file1 = user_file + 'SNAAKE'
                    if not os.path.exists(user_file1):
                        with open(user_file1, 'w+') as file:
                            file.write('Your MAX score is 0 ')
                        file.close()

                    file_to_run = "FINAL.py"
                    try:
                        with open(file_to_run, 'r') as file:
                            file_content = file.read()
                            exec(file_content)
                    except FileNotFoundError:
                        print(f"Error: File '{file_to_run}' not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

                    user_file = ''  # Clear the text after Enter is pressed
                elif event.key == pygame.K_BACKSPACE:
                    user_file = user_file[:-1]  # Delete the last character
                else:
                    user_file += event.unicode  # Add the typed character to the text

    # Render the input box and text
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = font.render(user_file, True, WHITE)
    screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))

    pygame.display.flip()
    clock.tick(30)

# Quit Pygame properly
pygame.quit()
