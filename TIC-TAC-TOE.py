import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
LINE_WIDTH = 6
BOARD_ROWS, BOARD_COLS = 3, 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (0, 100, 200)
X_COLOR = (255, 69, 0)
O_COLOR = (65, 105, 225)
FPS = 60

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-tac-toe")

# Game variables
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player_turn = 'O'
game_over = False
winner = None
font = pygame.font.SysFont(None, 75)

def draw_lines():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)

def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col * WIDTH // 3 + 30, row * HEIGHT // 3 + 30),
                                 ((col + 1) * WIDTH // 3 - 30, (row + 1) * HEIGHT // 3 - 30), 5)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * WIDTH // 3 - 30, row * HEIGHT // 3 + 30),
                                 (col * WIDTH // 3 + 30, (row + 1) * HEIGHT // 3 - 30), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6),
                                   HEIGHT // 6 - 30, 3)

def check_winner():
    global game_over, winner
    # Check rows, columns, and diagonals for a win
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player_turn for j in range(BOARD_COLS)):  # Check rows
            game_over = True
            winner = player_turn
            break
        if all(board[j][i] == player_turn for j in range(BOARD_COLS)):  # Check columns
            game_over = True
            winner = player_turn
            break
    if all(board[i][i] == player_turn for i in range(BOARD_ROWS)) or all(
            board[i][2 - i] == player_turn for i in range(BOARD_ROWS)):  # Check diagonals
        game_over = True
        winner = player_turn

def check_board_full():
    # Check if the board is full
    return all(board[i][j] != '' for i in range(BOARD_ROWS) for j in range(BOARD_COLS))

def draw_winner(winner):
    if winner:
        text = font.render(f"Player {winner} wins!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def draw_tie():
    if not winner and check_board_full():
        text = font.render("It's a tie!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def reset_game():
    global board, game_over, winner, player_turn
    board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    game_over = False
    winner = None
    player_turn = 'X'


running = True
while running:
        screen.fill(WHITE)
        draw_lines()
        draw_symbols()
        draw_winner(winner)
        draw_tie()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                file_to_run = "FINAL.py"

                try:
                    with open(file_to_run, 'r') as file:
                        file_content = file.read()
                        exec(file_content)
                except FileNotFoundError:
                    print(f"Error: File '{file_to_run}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                col = x // (WIDTH // 3)
                row = y // (HEIGHT // 3)

                if board[row][col] == '':
                    board[row][col] = player_turn
                    check_winner()
                    if not game_over:
                        player_turn = 'O' if player_turn == 'X' else 'X'
                    else:
                        break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    file_to_run = "FINAL.py"

                    try:
                        with open(file_to_run, 'r') as file:
                            file_content = file.read()
                            exec(file_content)
                    except FileNotFoundError:
                        print(f"Error: File '{file_to_run}' not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

        pygame.display.flip()


