from random import randint

WIDTH = 800
HEIGHT = 600
#center = [400, 300] #coordonnée du centre du cercle
#brick = Actor("brick", anchor = ["left", "top"]) #nom de l'image dans la parenthèse 
#tout ce qui est sensé intéragir doit être Actor
lines = 7
player = Actor("player")
player.pos = [400, 550]

ball = Actor("ball")
ball.pos = [400, 500]

ball_speed = [3, -3]
power_up_speed = [0, 3]

power_up_apparition = 50
time_bigger_player = 0

all_bricks =[]
all_super_bricks =[]
all_power_up_bigger_player = []

for x in range (0, 800, 100):
    for y in range (0, 30*lines, 30):
        brick = Actor("brick", anchor = ["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)

for x in range (0, 800, 100):
    super_brick = Actor("brick2-1", anchor = ["left", "top"])
    super_brick.pos = [x, 30 * lines + 1]
    all_super_bricks.append(super_brick)

#dessine un cercle
def draw(): 
    screen.clear() #nettoie l'écran précédent (les anciennes frames)
    #screen.draw.circle(center, 50, "blue")
    for brick in all_bricks:
        brick.draw()
    for super_brick in all_super_bricks:
        super_brick.draw()

    for power_up_bigger_player in all_power_up_bigger_player:
        power_up_bigger_player.draw()

    player.draw()
    ball.draw()


    
def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]] #la position est fournie sous forme de liste [0,1,...] index 0 = axe x, index 1 = axe y

def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

def upgrade_ball_speed(upgrade):
    if ball_speed[0] > 0:
        ball_speed[0] = ball_speed[0] + upgrade
    else:
        ball_speed[0] = ball_speed[0] - upgrade
    if ball_speed[1] > 0:
        ball_speed[1] = ball_speed[1] + upgrade
    else:
        ball_speed[1] = ball_speed[1] - upgrade
# def change_speed()

#update les frames
def update(dt):
    global time_bigger_player
    global player

    if time_bigger_player > 0:
        time_bigger_player = time_bigger_player - dt
        print(time_bigger_player)
        if time_bigger_player <=0:
            player = Actor("player", player.pos)

    #vitesse de la balle
    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]

    ball.pos = [new_x, new_y]
    
    for power_up_bigger_player in all_power_up_bigger_player:
        new_x = power_up_bigger_player.pos[0] + power_up_speed[0]
        new_y = power_up_bigger_player.pos[1] + power_up_speed[1]

        power_up_bigger_player.pos = [new_x, new_y]

    if ball.right >= WIDTH or ball.left <= 0: #ball.right= la droite de la balle
        invert_horizontal_speed()
    if ball.top <= 0:
        invert_vertical_speed()

    if ball.colliderect(player):
        invert_vertical_speed()
        upgrade_ball_speed(0.10)

    for brick in all_bricks:
        if ball.colliderect(brick):
            all_bricks.remove(brick)
            invert_vertical_speed()
            
            rdm = randint(0, 100)
            if rdm <= power_up_apparition:
                power_up = Actor("powerup1", anchor = ["left", "top"])
                power_up.pos = brick.pos 
                all_power_up_bigger_player.append(power_up)
                

    for super_brick in all_super_bricks:
        if super_brick.colliderect(ball):
            all_super_bricks.remove(super_brick)
            invert_vertical_speed()
            
            brick = Actor("brick2-2", anchor = ["left", "top"])
            brick.pos = super_brick.pos 
            all_bricks.append(brick)

    for power_up_bigger_player in all_power_up_bigger_player:
        if player.colliderect(power_up_bigger_player):
            all_power_up_bigger_player.remove(power_up_bigger_player)
            time_bigger_player = 6
            player = Actor ("bigger_player", player.pos)

