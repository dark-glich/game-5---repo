import pygame
import random
import math

pygame.init()
time = pygame.time.Clock()
screen_width = 600
screen_height = 400
state = "none"
number = 3
block = 20
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)
point_x = random.randint(30, 550)
point_y = random.randint(40, 360)
point = pygame.image.load("apple.png")
x = screen_width / 2
y = screen_height / 2
x_change = 0
y_change = 0
score = 0
display = pygame.display.set_mode((screen_width, screen_height))
caption = pygame.display.set_caption("Snake")
game_end = False
running = True
snake = []
movement = True
fonti = pygame.font.Font("Cartoon cookies.ttf", 60)
font_x, font_y = 200, 3
st = "score : "
player_color = (0, 180, 0)
backgound = (255, 255, 255)
font_2 = pygame.font.Font("Cartoon cookies.ttf", 100)
font_2_x, font_2_y = 55, 150


def scores(p_1, p_2):
    s = fonti.render(str(st) + str(score), True, (0, 0, 0))
    display.blit(s, (p_1, p_2))


def over(p_3, p_4):
    f = font_2.render("GAME OVER", True, (0, 0, 0))
    display.blit(f, (p_3, p_4))


def points(xi, yi, z):
    display.blit(xi, (yi, z))


def structure():
    for x1 in snake:
        pygame.draw.rect(display, player_color, (x1[0], x1[1], block, block))


def difference(a, b, c, d):
    d = math.sqrt((a - c) ** 2 + (b - d) ** 2)
    if d <= 25:
        return True
    else:
        return False


while running:
    display.fill(backgound)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state != "left" and state != "right" and movement:
                if event.key == pygame.K_LEFT:
                    state = "left"
                    x_change -= block
                    y_change = 0
            if state != "right" and state != "left" and movement:
                if event.key == pygame.K_RIGHT:
                    state = "right"
                    x_change += block
                    y_change = 0
            if state != "up" and state != "down" and movement:
                if event.key == pygame.K_UP:
                    state = "up"
                    y_change -= block
                    x_change = 0
            if state != "down" and state != "up" and movement:
                if event.key == pygame.K_DOWN:
                    state = "down"
                    y_change += block
                    x_change = 0
            if event.key == pygame.K_1:
                backgound = (255, 0, 75)
            if event.key == pygame.K_2:
                backgound = (46, 83, 181)
            if event.key == pygame.K_3:
                backgound = (141, 14, 202)
            if event.key == pygame.K_4:
                player_color = (243, 14, 0)
            if event.key == pygame.K_5:
                player_color = (0, 0, 0)
            if event.key == pygame.K_6:
                player_color = (0, 0, 77)
            if event.key == pygame.K_7:
                point = pygame.image.load("pineapple.png")
            if event.key == pygame.K_8:
                point = pygame.image.load("fruit.png")
            if event.key == pygame.K_9:
                point = pygame.image.load("watermelon.png")
            if event.key == pygame.K_0:
                point = pygame.image.load("apple.png")
                player_color = (0, 180, 0)
                backgound = (255, 255, 255)

    x += x_change
    y += y_change
    la = [x, y]

    snake.append(la)

    collide = difference(x, y, point_x, point_y)
    if collide:
        number += 1
        score += 1
        point_x, point_y = random.randint(30, 550), random.randint(40, 360)

    if x > 580 or x < 10 or y < 10 or y > 380:
        game_end = True

    if len(snake) > number:
        del snake[0]

    if game_end:
        structure()
        number = 1
        st = "final score : "
        x, y = -1000, -200
        point_y, font_x = 1000, 160
        del snake[0]
        x_change, y_change = 0, 0
        over(font_2_x, font_2_y)
        movement = False

    time.tick(12)
    structure()
    points(point, point_x, point_y), scores(font_x, font_y), pygame.display.update()

