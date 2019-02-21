import pygame
import random
from Project1 import AStar
from Project1 import AStarLast
pygame.init()

display_width = 600
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

dot_size = 30
speed_game = 5


font = pygame.font.SysFont(None, 25)
point1 = 0
# Biến đánh dấu để gọi rắn ra khi chơi với máy
computer = 0
point_computer = 0
point_player = 0

point_high = 0



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Hunting Snake')
clock = pygame.time.Clock()
# Lưu ảnh vào đối tượng

dotImg = pygame.image.load('apple.png')
appleImg = pygame.image.load('head.png')
gameIcon = pygame.image.load('snake.png')
snakeIntro = pygame.image.load('xxxxx.png')
snakeHelp = pygame.image.load('help.png')
snakeAuthor = pygame.image.load('author.png')
pygame.display.set_icon(gameIcon)
# Biến global dùng để tạm dừng trò chơi
pause = False

# Modul tính điểm
def pointAcount(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Point: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
def pointAcount1(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Point: " + str(count), True, black)
    gameDisplay.blit(text, (dot_size, dot_size))
# Hiện hình ảnh lên gameDisplay
def showImage(image, x, y):
    gameDisplay.blit(image, (x, y))

# Tạo đối tượng text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Viết chữ tại vị trí (z, y) cỡ chữ z
def message_display(text, x, y, z):
   largeText = pygame.font.SysFont("comicsansms",z)
   TextSurf, TextRect = text_objects(text, largeText)
   TextRect.center = (x, y)
   gameDisplay.blit(TextSurf, TextRect)

# Xây dựng nút button
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    message_display(msg, (x + (w / 2)), (y + (h / 2)), 20)
# Hàm được gọi khi rắn chết
def game_over():
    global  point1
    global  point_high
    if(point1 > point_high):
        point_high = point1
        game_over_high_point()
    message_display("Game Over", 300, 200, 80)
    message_display("Your Point: " + str(point1), 300, 350, 45)
    point1 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 50, 450, 100, 50, green, bright_green, game_loop)
        button("Return", 250, 450, 100, 50, green, bright_green, show_sellect_option)
        button("Quit", 450, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)
def game_over_player():
    if(point_player < point_computer):
        show_loss()
    if(point_player > point_computer):
        show_victory()
def game_over_computer():

    message_display("Computer End", 300, 200, 80)
    message_display("Computer's Point: " + str(point_computer), 300, 350, 45)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Your Turn", 50, 450, 100, 50, green, bright_green, game_loop_player)
        button("Return", 250, 450, 100, 50, green, bright_green, show_sellect_option)
        button("Quit", 450, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


# Hàm kết thúc trò chơi
def quitgame():
    pygame.quit()
    quit()

# Hàm hủy tạm dừng trò chơi
def unpause():
    global pause
    pause = False
 #Hàm để tạm dừng trò chơi
def paused():


    message_display("Paused", display_width / 2, display_height / 2, 115)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()


        button("Continue", 50, 450, 100, 50, green, bright_green, unpause)
        button("Return", 250, 450, 100, 50, green, bright_green, show_sellect_option)
        button("Quit", 450, 450, 100, 50, red, bright_red, quitgame)



        pygame.display.update()
        clock.tick(15)

# Hàm hiện ra hướng dẫn chơi
def show_help():

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeHelp, 50, 30)

        message_display("Press left key, right key, up key and", 300, 170, 30)
        message_display("and down key to control the snake.", 300, 220, 30)
        message_display(" If eaten, one point is added.", 300, 270, 30)
        message_display("If you want to stop the game", 300, 320, 30)
        message_display("press the p key.", 300, 370, 30)
        message_display("When the snake hit the wall or itself,", 300, 420, 30)
        message_display("the game will end.", 300, 470, 30)
        button("Return", 250, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)
# Hàm hiện ra tác giả
def show_author():

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)
        message_display("BY", 300, 325, 50)
        message_display("NGUYEN ANH PHUONG", 300, 400, 50)
        button("Return", 250, 500, 100, 50, green, bright_green, game_intro)


        pygame.display.update()
        clock.tick(15)


# Hàm xây dựng màn hình khi vào game
def game_intro():
    global speed_game
    global point_high
    f = open("pointHight.txt", "r")
    point_high = int(f.read())
    f.close()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        showImage(snakeIntro, display_width / 15, display_height / 10)
        message_display("A", 450, 100, 60)
        message_display("Hunting", 450, 200, 60)
        message_display("Snake", 450, 300, 60)

        button("New Game", 350, 380, 100, 50, green, bright_green, show_sellect_option)
        if(speed_game == 5):
            button("Setting", 475, 380, 100, 50, green, bright_green, speed1)
        if(speed_game == 10):
            button("Setting", 475, 380, 100, 50, green, bright_green, speed2)
        if (speed_game == 15):
            button("Setting", 475, 380, 100, 50, green, bright_green, speed3)
        button("Help", 350, 455, 100, 50, green, bright_green, show_help)
        button("HighScore", 475, 455, 100, 50, green, bright_green, show_high_point)
        button("About", 350, 530, 100, 50, green, bright_red, show_author)
        button("Quit", 475, 530, 100, 50, red, bright_red, quitgame)




        pygame.display.update()
        clock.tick(15)
# Khi chết hiện ra điểm cao
def game_over_high_point():
    global point_high
    message_display("Game Over", 300, 200, 80)
    message_display("New High Score: " + str(point_high), 300, 350, 45)
    f = open('pointHight.txt', 'w')
    f.write(str(point_high))
    f.close()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 50, 450, 100, 50, green, bright_green, game_loop)
        button("Return", 250, 450, 100, 50, green, bright_green, show_sellect_option)
        button("Quit", 450, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

# Hiện ra điểm cao
def show_high_point():
    global point_high
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)
        message_display("HIGH SCORE: " + str(point_high), 300, 375, 50)
        button("Return", 250, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)

# Hàm in ra các đốt rắn
def show_dot(snakeList):
    for XY in snakeList:
        showImage(dotImg, XY[0], XY[1])
def show_wall(x, y , w, h, color):
    pygame.draw.rect(gameDisplay, color, (x, y, w, h))
# def setting_speed():
#     global speed_game
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         gameDisplay.fill(white)
#
#         showImage(snakeAuthor, 10, 100)
#
#         button("Speed 5", 100, 375, 100, 50, red, bright_green, speed1)
#         button("Speed 10", 250, 375, 100, 50, green, bright_green, speed2)
#         button("Speed 15", 400, 375, 100, 50, green, bright_green, speed3)
#         button("Return", 250, 500, 100, 50, green, bright_green, game_intro)
#
#         pygame.display.update()
#         clock.tick(15)

def speed1():
    global  speed_game
    speed_game = 5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)

        button("Speed 5", 100, 375, 100, 50, red, bright_green, speed1)
        button("Speed 10", 250, 375, 100, 50, green, bright_green, speed2)
        button("Speed 15", 400, 375, 100, 50, green, bright_green, speed3)
        button("Return", 250, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(20)

def speed2():
    global  speed_game
    speed_game = 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)

        button("Speed 5", 100, 375, 100, 50, green, bright_green, speed1)
        button("Speed 10", 250, 375, 100, 50, red, bright_green, speed2)
        button("Speed 15", 400, 375, 100, 50, green, bright_green, speed3)
        button("Return", 250, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(20)
def speed3():
    global  speed_game
    speed_game = 15
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)

        button("Speed 5", 100, 375, 100, 50, green, bright_green, speed1)
        button("Speed 10", 250, 375, 100, 50, green, bright_green, speed2)
        button("Speed 15", 400, 375, 100, 50, red, bright_green, speed3)
        button("Return", 250, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(20)
# Vòng lặp khi chơi game
def game_loop():
    global  pause
    global point1
    gameExit = False
    gameOver = False
    head_x = display_width / 2
    head_y = display_height / 2
    head_x_change = 0
    head_y_change = 0

    snakeList = []
    snake_length = 1

    rand_food_x = random.randrange(0, display_width - dot_size, 30)
    rand_food_y = random.randrange(0, display_height - dot_size, 30)
    point = 0
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            game_over()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_LEFT:
                    head_x_change = -dot_size
                    head_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    head_x_change = dot_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change = -dot_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change = dot_size
                    head_x_change = 0


        gameDisplay.fill(white)
        pointAcount(point)
        showImage(appleImg, rand_food_x, rand_food_y)


        head_x += head_x_change
        head_y += head_y_change

        snakeHead = []
        snakeHead.append(head_x)
        snakeHead.append(head_y)
        snakeList.append(snakeHead)




        if len(snakeList) > snake_length:
            del snakeList[0]

        show_dot(snakeList)

        for snake in snakeList[:-1]:
            if snake == snakeHead:
                gameOver = True

        if head_x >= display_width:
            head_x = -dot_size
        elif head_x < 0:
            head_x = display_width
        elif head_y >= display_height:
            head_y = -dot_size
        elif head_y < 0:
            head_y = display_height


        pygame.display.update()


        if head_x == rand_food_x and head_y == rand_food_y:
            rand_food_x = random.randrange(0, display_width - dot_size, 30)
            rand_food_y = random.randrange(0, display_height - dot_size, 30)
            while check_position(snakeList, rand_food_x, rand_food_y):
                rand_food_x = random.randrange(0, display_width - dot_size, 30)
                rand_food_y = random.randrange(0, display_height - dot_size, 30)
            snake_length += 1
            point += 1
            point1 = point

        if point == 5:
            game_loop5()

        clock.tick(speed_game)

    pygame.quit()
    quit()


def game_loop1():
    global  pause
    global point1
    gameExit = False
    gameOver = False
    head_x = display_width / 2
    head_y = display_height / 2
    head_x_change = 0
    head_y_change = 0
    snakeList = []
    snake_length = 1

    rand_food_x = random.randrange(dot_size, display_width - 2*dot_size, 30)
    rand_food_y = random.randrange(dot_size, display_height - 2*dot_size, 30)

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            game_over()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_LEFT:
                    head_x_change = -dot_size
                    head_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    head_x_change = dot_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change = -dot_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change = dot_size
                    head_x_change = 0

        gameDisplay.fill(white)
        show_wall(0, 0, display_width, dot_size, black)
        show_wall(0, dot_size, dot_size, display_height , black)
        show_wall(0, display_height - dot_size, display_width, dot_size, black)
        show_wall(display_height - dot_size, 0, dot_size, display_height,  black)
        pointAcount1(point1)
        showImage(appleImg, rand_food_x, rand_food_y)


        head_x += head_x_change
        head_y += head_y_change

        snakeHead = []
        snakeHead.append(head_x)
        snakeHead.append(head_y)
        snakeList.append(snakeHead)


        if len(snakeList) > snake_length:
            del snakeList[0]

        show_dot(snakeList)

        for snake in snakeList[:-1]:
            if snake == snakeHead:
                gameOver = True
        if head_x >= display_width - dot_size or head_x < dot_size or head_y >= display_height - dot_size or head_y < dot_size:
            gameOver = True



        pygame.display.update()


        if head_x == rand_food_x and head_y == rand_food_y:
            rand_food_x = random.randrange(dot_size, display_width - 2*dot_size, 30)
            rand_food_y = random.randrange(dot_size, display_height - 2*dot_size, 30)
            while check_position(snakeList, rand_food_x, rand_food_y):
                rand_food_x = random.randrange(dot_size, display_width - 2*dot_size, 30)
                rand_food_y = random.randrange(dot_size, display_height - 2*dot_size, 30)
            snake_length += 1
            point1 += 1

        if(point1 == 10):
            game_loop5()
        clock.tick(speed_game)

    pygame.quit()
    quit()


def check_position(XY, x, y):
    for n in XY:
        if(x == n[0] and y == n[1]):
            return True
    return False
def game_loop2():
    global  pause
    global point1
    gameExit = False
    gameOver = False
    head_x = display_width / 2
    head_y = display_height / 2
    head_x_change = 0
    head_y_change = 0
    snakeList = []
    snake_length = 1
    rand_food_x = random.randrange(0, display_width - dot_size, 30)
    rand_food_y = random.randrange(0, display_height - dot_size, 30)

    m = []
    for index in range(0, 50):
        n = []
        randX = random.randrange(0, display_width - dot_size, 30)
        randY = random.randrange(0, display_height - dot_size, 30)
        while((randX == display_width / 2 and randY == display_height / 2) or (randX == 0 and randY == 0) or (randX == dot_size and randY == 0) or (randX == 2*dot_size and randY == 0)):
            randX = random.randrange(0, display_width - dot_size, 30)
            randY = random.randrange(0, display_height - dot_size, 30)
        n.append(randX)
        n.append(randY)
        m.append(n)
    while check_position(m, rand_food_x, rand_food_y):
        rand_food_x = random.randrange(0, display_width - dot_size, 30)
        rand_food_y = random.randrange(0, display_height - dot_size, 30)


    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            game_over()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_LEFT:
                    head_x_change = -dot_size
                    head_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    head_x_change = dot_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change = -dot_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change = dot_size
                    head_x_change = 0

        gameDisplay.fill(white)
        for n in m:
            show_wall(n[0], n[1], dot_size, dot_size, black)
        pointAcount(point1)
        showImage(appleImg, rand_food_x, rand_food_y)


        head_x += head_x_change
        head_y += head_y_change

        snakeHead = []
        snakeHead.append(head_x)
        snakeHead.append(head_y)
        snakeList.append(snakeHead)


        if len(snakeList) > snake_length:
            del snakeList[0]

        show_dot(snakeList)

        for snake in snakeList[:-1]:
            if snake == snakeHead:
                gameOver = True
        if head_x >= display_width:
            head_x = -dot_size
        elif head_x < 0:
            head_x = display_width
        elif head_y >= display_height:
            head_y = -dot_size
        elif head_y < 0:
            head_y = display_height

        for n in m:
            if(head_x == n[0] and head_y == n[1]):
                gameOver = True


        pygame.display.update()


        if head_x == rand_food_x and head_y == rand_food_y:
            rand_food_x = random.randrange(0, display_width - dot_size, 30)
            rand_food_y = random.randrange(0, display_height - dot_size, 30)
            while check_position(snakeList, rand_food_x, rand_food_y) or check_position(m, rand_food_x, rand_food_y):
                rand_food_x = random.randrange(0, display_width - dot_size, 30)
                rand_food_y = random.randrange(0, display_height - dot_size, 30)
            snake_length += 1
            point1 += 1
        clock.tick(speed_game)

    pygame.quit()
    quit()
def show_sellect_option():
    global computer
    computer = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.fill(white)
        showImage(snakeAuthor, 10, 100)
        message_display("CHOOSE THE TYPE", 300, 330, 60)
        # button("Player", 50, 450, 200, 50, green, bright_green, game_loop)
        # button("Player - Computer", 350, 450, 200, 50, green, bright_green, show_sellect)
        # button("Return", 250, 540, 100, 50, green, bright_green, game_intro)

        button("Player", 50, 425, 200, 50, green, bright_green, game_loop)
        button("Player - Computer", 350, 425, 200, 50, green, bright_green, show_sellect)
        button("Return", 250, 525, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)



def show_sellect():
    global computer
    computer = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)

        message_display("SNAKE IS SLEEPING", 300, 370, 50)

        button("Call Snake", 100, 450, 120, 50, green, bright_green, game_loop5)
        button("Return", 400, 450, 120, 50, green, bright_green,  show_sellect_option)

        pygame.display.update()
        clock.tick(15)
def show_sellect1():
    global computer
    computer = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        showImage(snakeAuthor, 10, 100)

        message_display("SNAKE DOESN'T", 300, 325, 50)
        message_display("WAKE UP", 300, 400, 50)

        button("ReCall", 100, 450, 120, 50, green, bright_green, game_loop5)
        button("Return", 400, 450, 120, 50, green, bright_green, show_sellect_option)

        pygame.display.update()
        clock.tick(15)
def show_victory():
    showImage(snakeAuthor, 10, 100)

    message_display("YOU ARE VICTORY!", 300, 325, 50)
    message_display("Your Point: " + str(point_player), 300, 400, 45)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 100, 520, 120, 50, green, bright_green, show_sellect)
        button("Return", 400, 520, 120, 50, green, bright_green, show_sellect_option)

        pygame.display.update()
        clock.tick(15)

def show_loss():

    showImage(snakeAuthor, 10, 100)

    message_display("YOU ARE LOST!", 300, 325, 50)
    message_display("Your Point: " + str(point_player), 300, 400, 45)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 100, 520, 120, 50, green, bright_green, show_sellect)
        button("Return", 400, 520, 120, 50, green, bright_green, show_sellect_option)

        pygame.display.update()
        clock.tick(15)

# def game_loop3():
#     global pause
#     gameExit = False
#     astar = AStar.AStar(20)
#     size = len(astar.map)
#     source = [0, 0]
#     target = [19, 19]
#     # Mang luu tru cac vat can = -1
#     wall = []
#     for r in range(0, size):
#         for c in range(0, size):
#             n = []
#             if astar.map[r][c] == -1:
#                 n.append(r)
#                 n.append(c)
#                 wall.append(n)
#     # Mang luu tru duong di bang 1
#     route = []
#     # Goi ham a*
#     node = astar.solve(source, target)
#     if(node != -1):
#         while (node):
#             tmp = []
#             r = node.row
#             c = node.col
#             if (r == source[0] and c == source[1]):
#                 astar.map[r][c] = 1
#                 tmp.append(source[0])
#                 tmp.append(source[1])
#                 route.append(tmp)
#                 break
#             astar.map[r][c] = 1
#             tmp.append(r)
#             tmp.append(c)
#             route.append(tmp)
#             node = node.parent
#         route.reverse()
#         for i in range(size):
#             print()
#             for r in range(size):
#                 print(astar.map[i][r], end="      ")
#     else:
#         show_sellect1()
#     while not gameExit:
#         gameDisplay.fill(white)
#         for XY in route:
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         quitgame()
#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_p:
#                             pause = True
#                             paused()
#                 gameDisplay.fill(white)
#                 showImage(appleImg, display_width - dot_size, display_height - dot_size)
#                 for MN in wall:
#                     show_wall(MN[1]*dot_size, MN[0]*dot_size, dot_size, dot_size, black)
#                 showImage(dotImg, XY[1]*dot_size, XY[0]*dot_size)
#                 if(XY[0] == target[0] and XY[1] == target[1]):
#                     show_victory()
#                 pygame.display.update()
#                 clock.tick(speed_game)
#
#
#     pygame.quit()
#     quit()
#
#


def game_loop3():
    global pause
    global  computer
    computer = 1
    gameExit = False
    astar = AStar.AStar(20)
    size = len(astar.map)
    source = [0, 0]
    target = [19, 19]
    head_x = source[1]*dot_size
    head_y = source[0]*dot_size
    snake_list = []
    snake_length = 5
    # Mang luu tru cac vat can = -1
    wall = []
    for r in range(0, size):
        for c in range(0, size):
            n = []
            if astar.map[r][c] == -1:
                n.append(r)
                n.append(c)
                wall.append(n)
    # Mang luu tru duong di bang 1
    route = []
    # Goi ham a*
    node = astar.solve(source, target)
    if(node != -1):
        while (node):
            tmp = []
            r = node.row
            c = node.col
            if (r == source[0] and c == source[1]):
                astar.map[r][c] = 1
                tmp.append(source[0])
                tmp.append(source[1])
                route.append(tmp)
                break
            astar.map[r][c] = 1
            tmp.append(r)
            tmp.append(c)
            route.append(tmp)
            node = node.parent
        route.reverse()
        for i in range(size):
            print()
            for r in range(size):
                print(astar.map[i][r], end="      ")
    else:
        show_sellect1()
    while not gameExit:
        gameDisplay.fill(white)
        for XY in route:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quitgame()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pause = True
                            paused()
                gameDisplay.fill(white)
                showImage(appleImg, display_width - dot_size, display_height - dot_size)
                for MN in wall:
                    show_wall(MN[1]*dot_size, MN[0]*dot_size, dot_size, dot_size, black)
                snake_head = []
                snake_head.append(XY[1]*dot_size)
                snake_head.append(XY[0]*dot_size)
                snake_list.append(snake_head)
                if(len(snake_list) > snake_length):
                    del snake_list[0]
                show_dot(snake_list)
                if(XY[0] == target[0] and XY[1] == target[1]):
                    game_loop5()
                pygame.display.update()
                clock.tick(15)


    pygame.quit()
    quit()

def solve_route(source, target, wall):
    astar = AStarLast.AStar(20)
    for XY in wall:
        astar.map[XY[0]][XY[1]] = -1
    route = []
    node = astar.solve(source, target)
    if (node != -1):
        while (node):
            tmp = []
            r = node.row
            c = node.col
            if (r == source[0] and c == source[1]):
                astar.map[r][c] = 1
                tmp.append(source[0])
                tmp.append(source[1])
                route.append(tmp)
                break
            astar.map[r][c] = 1
            tmp.append(r)
            tmp.append(c)
            route.append(tmp)
            node = node.parent
        route.reverse()
    else:
        gameDisplay.fill(white)
        game_over_computer()
    return route


def game_loop4():
    global pause
    gameExit = False
    gameOver = False
    global  point_computer
    point_computer = 0
    head_x = display_width / 2
    head_y = display_height / 2
    source = [int(head_y / dot_size), int(head_x / dot_size)]
    rand_food_x = random.randrange(0, display_width - dot_size, 30)
    rand_food_y = random.randrange(0, display_height - dot_size, 30)
    while (rand_food_x == head_x and rand_food_y == head_y):
        rand_food_x = random.randrange(0, display_width - dot_size, 30)
        rand_food_y = random.randrange(0, display_height - dot_size, 30)

    target = [int(rand_food_y / dot_size), int(rand_food_x / dot_size)]
    snake_list = []
    snake_length = 1
    wall = []
    route = solve_route(source, target, wall)



    while not gameExit:
        for XY in route:
            while gameOver == True:
                gameDisplay.fill(white)
                game_over()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = True
                        paused()

            gameDisplay.fill(white)
            showImage(appleImg, rand_food_x, rand_food_y)
            pointAcount(point_computer)

            head_x = XY[1]*dot_size
            head_y = XY[0]*dot_size
            snake_head = []
            snake_head.append(XY[1]*dot_size)
            snake_head.append(XY[0]*dot_size)
            snake_list.append(snake_head)

            if(len(snake_list) > snake_length):
                del snake_list[0]
                wall = []
                for snake in snake_list[:-1]:
                    n = []
                    n.append(int(snake[1] / dot_size))
                    n.append(int(snake[0] / dot_size))
                    wall.append(n)
                source = [int(head_y / dot_size), int(head_x / dot_size)]
            show_dot(snake_list)
            pygame.display.update()
            if head_x == rand_food_x and head_y == rand_food_y:
                rand_food_x = random.randrange(0, display_width - dot_size, 30)
                rand_food_y = random.randrange(0, display_height - dot_size, 30)
                while check_position(snake_list, rand_food_x, rand_food_y):
                    rand_food_x = random.randrange(0, display_width - dot_size, 30)
                    rand_food_y = random.randrange(0, display_height - dot_size, 30)

                snake_length += 1
                point_computer += 1
                target = [int(rand_food_y / dot_size), int(rand_food_x / dot_size)]

            route = solve_route(source, target, wall)

            clock.tick(100)


    pygame.quit()
    quit()


def game_loop5():
    global pause
    gameExit = False
    astar = AStarLast.AStar(20)
    size = len(astar.map)
    source = [11, 0]
    target = [11, 19]
    snake_list = []
    snake_length = 5
    # Mang luu tru duong di bang 1
    route = []
    # Goi ham a*
    node = astar.solve(source, target)
    if(node != -1):
        while (node):
            tmp = []
            r = node.row
            c = node.col
            if (r == source[0] and c == source[1]):
                astar.map[r][c] = 1
                tmp.append(source[0])
                tmp.append(source[1])
                route.append(tmp)
                break
            astar.map[r][c] = 1
            tmp.append(r)
            tmp.append(c)
            route.append(tmp)
            node = node.parent
        route.reverse()
        for i in range(size):
            print()
            for r in range(size):
                print(astar.map[i][r], end="      ")
    else:
        show_sellect1()
    while not gameExit:
        gameDisplay.fill(black)
        for XY in route:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quitgame()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pause = True
                            paused()
                gameDisplay.fill(white)
                showImage(snakeAuthor, 10, 100)

                snake_head = []
                snake_head.append(XY[1]*dot_size)
                snake_head.append(XY[0]*dot_size)
                snake_list.append(snake_head)
                if(len(snake_list) > snake_length):
                    del snake_list[0]
                show_dot(snake_list)
                if(XY[0] == target[0] and XY[1] == target[1]) and point1 == 5:
                    game_loop1()
                if (XY[0] == target[0] and XY[1] == target[1]) and point1 == 10:
                    game_loop2()
                if (XY[0] == target[0] and XY[1] == target[1]) and computer == 0:
                    game_loop3()
                if (XY[0] == target[0] and XY[1] == target[1]) and computer == 1:
                    game_loop4()
                pygame.display.update()
                clock.tick(15)


    pygame.quit()
    quit()

def game_loop_player():
    global  pause
    global point_player
    gameExit = False
    gameOver_player = False
    head_x = display_width / 2
    head_y = display_height / 2
    head_x_change = 0
    head_y_change = 0

    snakeList = []
    snake_length = 1

    rand_food_x = random.randrange(0, display_width - dot_size, 30)
    rand_food_y = random.randrange(0, display_height - dot_size, 30)
    point_player = 0
    while not gameExit:

        while gameOver_player == True or point_player > point_computer:
            gameDisplay.fill(white)
            game_over_player()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver_player = False
                    gameExit = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_LEFT:
                    head_x_change = -dot_size
                    head_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    head_x_change = dot_size
                    head_y_change = 0
                elif event.key == pygame.K_UP:
                    head_y_change = -dot_size
                    head_x_change = 0
                elif event.key == pygame.K_DOWN:
                    head_y_change = dot_size
                    head_x_change = 0


        gameDisplay.fill(white)
        pointAcount(point_player)
        showImage(appleImg, rand_food_x, rand_food_y)


        head_x += head_x_change
        head_y += head_y_change

        snakeHead = []
        snakeHead.append(head_x)
        snakeHead.append(head_y)
        snakeList.append(snakeHead)




        if len(snakeList) > snake_length:
            del snakeList[0]

        show_dot(snakeList)

        for snake in snakeList[:-1]:
            if snake == snakeHead:
                gameOver_player = True

        if head_x >= display_width:
            head_x = -dot_size
        elif head_x < 0:
            head_x = display_width
        elif head_y >= display_height:
            head_y = -dot_size
        elif head_y < 0:
            head_y = display_height


        pygame.display.update()


        if head_x == rand_food_x and head_y == rand_food_y:
            rand_food_x = random.randrange(0, display_width - dot_size, 30)
            rand_food_y = random.randrange(0, display_height - dot_size, 30)
            while check_position(snakeList, rand_food_x, rand_food_y):
                rand_food_x = random.randrange(0, display_width - dot_size, 30)
                rand_food_y = random.randrange(0, display_height - dot_size, 30)
            snake_length += 1
            point_player += 1



        clock.tick(speed_game)

    pygame.quit()
    quit()


game_intro()
# show_sellect1()
# pygame.quit()
# game_loop5()
# show_loss()
# quit()
# game_over()