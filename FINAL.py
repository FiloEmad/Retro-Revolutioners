import pygame

pygame.init()



screen =pygame.display.set_mode((700,700))
Caption = pygame.display.set_caption('Retro Revolutioners')
Run = True

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rec.collidepoint(mouse_pos):
                file_to_run = "SNAAKE.py"

                try:
                    with open(file_to_run, 'r') as file:
                        file_content = file.read()
                        exec(file_content)
                except FileNotFoundError:
                    print(f"Error: File '{file_to_run}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            if rec2.collidepoint(mouse_pos):
                file_to_run = ("TIC-TAC-TOE.py"
                               "")

                try:
                    with open(file_to_run, 'r') as file:
                        file_content = file.read()
                        exec(file_content)
                except FileNotFoundError:
                    print(f"Error: File '{file_to_run}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            if rec3.collidepoint(mouse_pos):
                file_to_run = "SUDOKU.py"

                try:
                    with open(file_to_run, 'r') as file:
                        file_content = file.read()
                        exec(file_content)
                except FileNotFoundError:
                    print(f"Error: File '{file_to_run}' not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")





    Txt1=(pygame.font.SysFont('None',36).render('Snake', True, (100,200,250))
        )
    Txt = (pygame.font.SysFont('None', 50).render('CHOOSE A GAME !!', True, (100, 200, 250))
           )
    Txt2 = (pygame.font.SysFont('None', 36).render('TIC-TAC-TOE', True, (100, 200, 250))
           )
    Txt3 = (pygame.font.SysFont('None', 36).render('SUDUKO', True, (100, 200, 250))
           )

    rec= pygame.draw.ellipse(screen, (50,150,150), (200,160,300,100))
    rec2 = pygame.draw.ellipse(screen, (50,150,150), (200,310,300,100))
    rec3=pygame.draw.ellipse(screen, (50,150,150), (200,460,300,100))
    screen.blit(Txt1,(312,200))
    screen.blit(Txt,(200,50))
    screen.blit(Txt2,(280,350))
    screen.blit(Txt3,(300,495))




    pygame.display.update()
pygame.quit()




