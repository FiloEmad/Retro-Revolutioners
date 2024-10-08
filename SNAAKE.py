import pygame
import time
import random


speed = 10

window_x =900
window_y =720

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('snake game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# displaying Score function
def show_score( color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)





# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    time.sleep(2)



    # setting position of the text

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)
    # deactivating pygame library
    Run = False
    # quit the program


def movment(x):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            x = 'UP'
        if event.key == pygame.K_DOWN:
            x = 'DOWN'
        if event.key == pygame.K_LEFT:
            x = 'LEFT'
        if event.key == pygame.K_RIGHT:
            x = 'RIGHT'


    return x

def maxscore():
    with open('main_file.txt', 'r') as file:
        first_line = file.readline()
        if first_line:
            first_line = first_line[:len(first_line)-1]
            with open(first_line , 'r') as user_file :
                max = user_file.readline()
    Txt = (pygame.font.SysFont('None', 50).render(max, True, (100, 200, 250))
           )
    game_window.blit(Txt, (200, 50))
    pygame.display.flip()







Run = True
# Main Function
while Run == True :
    with open('main_file.txt', 'r') as file:
        first_line = file.readline()
        if first_line:
            first_line = first_line[:len(first_line)-1]
            with open(first_line , 'r') as user_file :
                max = user_file.readline()
    Txt = (pygame.font.SysFont('None', 50).render(max, True, (100, 200, 250))
           )
    game_window.blit(Txt, (200, 50))
    pygame.display.flip()
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            file_to_run = "FINAL.py"

            try:
                with open(file_to_run, 'r') as file:
                    file_content = file.read()
                    exec(file_content)
            except FileNotFoundError:
                print(f"Error: File '{file_to_run}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            quit()
    change_to=movment(change_to)


    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        with open('main_file.txt', 'r') as file:
            first_line = file.readline()
            if first_line:
                first_line= first_line[:len(first_line)-1]
            with open(first_line, 'r+') as user_file:
                user_data = user_file.readline().split()
                if int(user_data[4]) < score:
                        user_file.seek(0)  # Move the cursor to the beginning of the file
                        user_file.write('Your MAX score is ' + str(score) + '\n')
                        user_file.truncate()  # Remove the remaining content (if any)
                user_file.close()

            file.close()

        speed+=2
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        maxscore()
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        Run = False
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        Run = False

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            Run = False

    # displaying score continuously
    show_score(white, 'times new roman', 50)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(speed)
pygame.quit()
file_to_run = "FINAL.py"

try:
    with open(file_to_run, 'r') as file:
        file_content = file.read()
        exec(file_content)
except FileNotFoundError:
    print(f"Error: File '{file_to_run}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


