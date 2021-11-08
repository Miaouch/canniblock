from random import randint

WIDTH = 800
HEIGHT = 600
#center = [400, 300] #coordonnée du centre du cercle
#brick = Actor("brick", anchor = ["left", "top"]) #nom de l'image dans la parenthèse 
#tout ce qui est sensé intéragir doit être Actor
lives = 3
player = Actor("block_player")
player.pos = [400, 550]
background = Actor("background")
background.pos = [400, 300]

victory = Actor("victory_dead")
victory.pos = [400, 300]
game_over = Actor("game_over_eat")
game_over.pos = [400, 300]
game__over = False
win = False
second_ball = Actor("ball_red")
ball = Actor("ball_blue")
ball.pos = [400, 500]

second_ball_speed = [3, -3]
ball_speed = [3, -3]
power_up_speed = [0, 3]
balls_multiples_speed = [0, 3]

two_balls_apparition = 90
power_up_apparition = 10
time_bigger_player = 0
time_two_balls = 0
time_game_reboot = 0

all_bricks =[]
all_bricks_bis = []
all_super_bricks =[]
all_super_bricks_bis = []
all_hyper_bricks = []
all_power_up_bigger_player = []
all_balls_multiples = []
all_second_balls = []
all_second_ball_speed = []
all_lives = []


music.play("canon-in-d-interstellar-mix-by-kevin-macleod-from-filmmusic-io")
music.set_volume(0.1)

for x in range (0, 800, 100):
    for y in range (0, 30 * 3, 30):
        super_brick = Actor("block_happy", anchor = ["left", "top"])
        super_brick.pos = [x, y * 1.5]
        all_super_bricks.append(super_brick)

for x in range (0, 800, 100):
    hyper_brick = Actor("block_cute", anchor = ["left", "top"])
    hyper_brick.pos = [100 + (x * 2), 30 * 6]
    all_hyper_bricks.append(hyper_brick)

for x in range (0, 800, 100):
    hyper_brick = Actor("block_cute", anchor = ["left", "top"])
    hyper_brick.pos = [x * 2, 30 * 7]
    all_hyper_bricks.append(hyper_brick)

for l in range (lives):
    lives_show = Actor ("heart_red", anchor = ["left", "top"])
    lives_show.pos = [ 10 + (l * 30), 560]
    all_lives.append(lives_show)

def game_reboot():
    global lives
    global game__over
    global win
    global ball
    global ball_speed
    global player
    global all_bricks
    global all_bricks_bis
    global all_super_bricks
    global all_super_bricks_bis
    global all_hyper_bricks
    global all_power_up_bigger_player
    global all_balls_multiples
    global all_second_balls
    global all_second_ball_speed
    global all_lives
    
    # global music.play("canon-in-d-interstellar-mix-by-kevin-macleod-from-filmmusic-io")
    # global music.set_volume(0.1)
    all_bricks = []
    all_bricks_bis = []
    all_super_bricks = []
    all_super_bricks_bis = []
    all_hyper_bricks = []
    all_power_up_bigger_player = []
    all_balls_multiples = []
    all_second_balls = []
    all_second_ball_speed = []
    all_lives = []
    
    lives = 3
    win = False
    game__over = False
    ball = Actor("ball_blue")
    ball.pos = [400, 500]
    ball_speed = [3, -3]
    player = Actor("block_player")
    player.pos = [400, 550] 

    for x in range (0, 800, 100):
        for y in range (0, 30 * 3, 30):
            super_brick = Actor("block_happy", anchor = ["left", "top"])
            super_brick.pos = [x, y * 1.5]
            all_super_bricks.append(super_brick)

    for x in range (0, 800, 100):
        hyper_brick = Actor("block_cute", anchor = ["left", "top"])
        hyper_brick.pos = [100 + (x * 2), 30 * 6]
        all_hyper_bricks.append(hyper_brick)

    for x in range (0, 800, 100):
        hyper_brick = Actor("block_cute", anchor = ["left", "top"])
        hyper_brick.pos = [x * 2, 30 * 7]
        all_hyper_bricks.append(hyper_brick)

    for l in range (lives):
        lives_show = Actor ("heart_red", anchor = ["left", "top"])
        lives_show.pos = [ 10 + (l * 30), 560]
        all_lives.append(lives_show)



def reboot():
    ball.pos = [400, 450]
    ball_speed = [3, -3]


def draw(): 
    global second_ball
    screen.clear() #nettoie l'écran précédent (les anciennes frames)
    #screen.draw.circle(center, 50, "blue")
    background.draw()

    for brick in all_bricks:
        brick.draw()

    for brick_bis in all_bricks_bis:
        brick_bis.draw()

    for super_brick in all_super_bricks:
        super_brick.draw()

    for super_brick_bis in all_super_bricks_bis:
        super_brick_bis.draw()

    for hyper_brick in all_hyper_bricks:
        hyper_brick.draw()

    for power_up_bigger_player in all_power_up_bigger_player:
        power_up_bigger_player.draw()

    for balls_multiples in all_balls_multiples:
        balls_multiples.draw()

    for second_ball in all_second_balls:
        second_ball.draw()    

    for lives_show in all_lives:
        lives_show.draw()

    player.draw()
    ball.draw()

    if game__over:
        game_over.draw()
          
    if win:
        victory.draw()
        sounds.game_over_fart.stop()
        sounds.game_bump.stop()
        sounds.impact5.stop()
    
def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]] #la position est fournie sous forme de liste [0,1,...] index 0 = axe x, index 1 = axe y

def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_horizontal_speed_second_ball(i):
    all_second_ball_speed[i][0] = all_second_ball_speed[i][0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

def invert_vertical_speed_second_ball(i):
    all_second_ball_speed[i][1] = all_second_ball_speed[i][1] * -1

def upgrade_ball_speed(upgrade):
    if ball_speed[0] > 0:
        ball_speed[0] = ball_speed[0] + upgrade
    else:
        ball_speed[0] = ball_speed[0] - upgrade
    if ball_speed[1] > 0:
        ball_speed[1] = ball_speed[1] + upgrade
    else:
        ball_speed[1] = ball_speed[1] - upgrade

def upgrade_second_ball_speed(upgrade, index):
    if all_second_ball_speed[index][0] > 0:
        all_second_ball_speed[index][0] = all_second_ball_speed[index][0] + upgrade
    else:
        all_second_ball_speed[index][0] = all_second_ball_speed[index][0] - upgrade
    if all_second_ball_speed[index][1] > 0:
        all_second_ball_speed[index][1] = all_second_ball_speed[index][1] + upgrade
    else:
        all_second_ball_speed[index][1] = all_second_ball_speed[index][1] - upgrade

def on_key_down(key):
    if key == keys.SPACE:
        game_reboot()

#update les frames
def update(dt):
    global win
    global game__over
    global time_bigger_player
    global time_game_reboot
    global player
    global ball
    global second_ball
    global lives

    if time_bigger_player > 0:
        time_bigger_player = time_bigger_player - dt
        print(time_bigger_player)
        if time_bigger_player <=0:
            player = Actor("block_player", player.pos)

    

    #vitesse de la balle 1
    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]

    ball.pos = [new_x, new_y]

    for lives_show in all_lives:
        if ball.bottom >= HEIGHT and lives >= 1:
            sounds.game_over_fart.play()
            lives = lives - 1
            all_lives.remove(lives_show)
            lives_gray = Actor("heart_gray", anchor = ["left", "top"])
            lives_gray.pos = lives_show.pos 
            all_lives.append(lives_gray)
            if lives > 0:
                reboot()
            

    for power_up_bigger_player in all_power_up_bigger_player:
        new_x = power_up_bigger_player.pos[0] + power_up_speed[0]
        new_y = power_up_bigger_player.pos[1] + power_up_speed[1]

        power_up_bigger_player.pos = [new_x, new_y]

    for balls_multiples in all_balls_multiples:
        new_x = balls_multiples.pos[0] + balls_multiples_speed[0]
        new_y = balls_multiples.pos[1] + balls_multiples_speed[1]

        balls_multiples.pos = [new_x, new_y]

    if ball.right >= WIDTH or ball.left <= 0: #ball.right= la droite de la balle
        invert_horizontal_speed()
    
    if ball.top <= 0:
        invert_vertical_speed()

    if ball.colliderect(player):
        
        sounds.game_bump.play()
        invert_vertical_speed()
        upgrade_ball_speed(0.10)

            
    for brick in all_bricks:
        if ball.colliderect(brick):
            sounds.impact5.play()
            all_bricks.remove(brick)
            invert_vertical_speed()
            
            rdm = randint(0, 100)
            if rdm <= power_up_apparition:
                power_up = Actor("powerup_bigger_player", anchor = ["left", "top"])
                power_up.pos = brick.pos 
                all_power_up_bigger_player.append(power_up)
            
            if rdm >= two_balls_apparition:
                balls_multiples = Actor("balls_multiples", anchor = ["left", "top"])
                balls_multiples.pos = brick.pos
                all_balls_multiples.append(balls_multiples)             


    for super_brick in all_super_bricks:
        if super_brick.colliderect(ball):
            sounds.impact5.play()
            all_super_bricks.remove(super_brick)
            invert_vertical_speed()

            #joue un son
            #sounds.explosion.play()
            
            brick = Actor("block_broken", anchor = ["left", "top"])
            brick.pos = super_brick.pos 
            all_bricks.append(brick)

    for brick_bis in all_bricks_bis:
        if ball.colliderect(brick_bis):
            sounds.impact5.play()
            all_bricks_bis.remove(brick_bis)
            invert_vertical_speed()
            
            rdm = randint(0, 100)
            if rdm <= power_up_apparition:
                power_up = Actor("powerup_bigger_player", anchor = ["left", "top"])
                power_up.pos = brick_bis.pos 
                all_power_up_bigger_player.append(power_up)
            
            if rdm >= two_balls_apparition:
                balls_multiples = Actor("balls_multiples", anchor = ["left", "top"])
                balls_multiples.pos = brick_bis.pos
                all_balls_multiples.append(balls_multiples) 

    for super_brick_bis in all_super_bricks_bis:
        if super_brick_bis.colliderect(ball):
            sounds.impact5.play()
            all_super_bricks_bis.remove(super_brick_bis)
            invert_vertical_speed()

            #joue un son
            #sounds.explosion.play()
            
            brick_bis = Actor("block_sad", anchor = ["left", "top"])
            brick_bis.pos = super_brick_bis.pos 
            all_bricks_bis.append(brick_bis)

    for hyper_brick in all_hyper_bricks:
        if hyper_brick.colliderect(ball):
            sounds.impact5.play()
            all_hyper_bricks.remove(hyper_brick)
            invert_vertical_speed()
            super_brick_bis = Actor("block_dum", anchor = ["left", "top"])
            super_brick_bis.pos = hyper_brick.pos 
            all_super_bricks_bis.append(super_brick_bis)

    for power_up_bigger_player in all_power_up_bigger_player:
        if player.colliderect(power_up_bigger_player):
            sounds.power_up_bigger.play()
            all_power_up_bigger_player.remove(power_up_bigger_player)
            time_bigger_player = 6
            player = Actor ("block_player_bigger", player.pos)

    for balls_multiples in all_balls_multiples:                
        if player.colliderect(balls_multiples):
            if second_ball in all_second_balls and lives == 0: #---------------pour avoir d'autre balle en plus quand la balle du jouer est morte----------------
                for i in range(len(all_second_balls)):
                    second_ball = Actor ("ball_red")
                    second_ball.pos = all_second_balls[i].pos
                    all_second_balls.append(second_ball)
                    all_second_ball_speed.append([3, -3])
                    
           
            all_balls_multiples.remove(balls_multiples)
            second_ball = Actor ("ball_red")
            second_ball.pos = ball.pos
            all_second_balls.append(second_ball)
            all_second_ball_speed.append([3, -3])
           
    # if ball.bottom > HEIGHT:
    #     ball = None----cacher la balle
        

    for n in range(len(all_second_balls)):  
        if n < len(all_second_balls):     
            if all_second_balls[n].bottom > HEIGHT:
                all_second_balls.remove(all_second_balls[n])

    if ball.bottom > HEIGHT and all_second_balls == [] and lives == 0 and not game__over:
        sounds.game_over_fart.play()
        game__over = True


    if all_bricks == [] and all_super_bricks == [] and not win:
        sounds.win.play()
        win = True
        
    #----------------------------------------------------------------------------------------------------------------------------------
    #fait bouger les balles 2 et gère tout de la suite des balles 2
    for i in range(len(all_second_balls)):    

        new_x = all_second_balls[i].pos[0] + all_second_ball_speed[i][0]
        new_y = all_second_balls[i].pos[1] + all_second_ball_speed[i][1]

        all_second_balls[i].pos = [new_x, new_y]

        
        if all_second_balls[i].right >= WIDTH or all_second_balls[i].left <= 0: #ball.right= la droite de la balle
            invert_horizontal_speed_second_ball(i)

            
        if all_second_balls[i].top <= 0:
            invert_vertical_speed_second_ball(i)

            
        if all_second_balls[i].colliderect(player):
            sounds.game_bump.play()
            invert_vertical_speed_second_ball(i)
            upgrade_second_ball_speed(0.05, i)

        for brick in all_bricks:
            if all_second_balls[i].colliderect(brick):
                sounds.impact5.play()
                all_bricks.remove(brick)
                invert_vertical_speed_second_ball(i)
                
                rdm = randint(0, 100)
                if rdm <= power_up_apparition:
                    power_up = Actor("powerup_bigger_player", anchor = ["left", "top"])
                    power_up.pos = brick.pos 
                    all_power_up_bigger_player.append(power_up)
                
                if rdm >= two_balls_apparition:
                    balls_multiples = Actor("balls_multiples", anchor = ["left", "top"])
                    balls_multiples.pos = brick.pos
                    all_balls_multiples.append(balls_multiples)             


        for super_brick in all_super_bricks:
            if super_brick.colliderect(all_second_balls[i]):
                sounds.impact5.play()
                all_super_bricks.remove(super_brick)
                invert_vertical_speed_second_ball(i)

                #joue un son
                #sounds.explosion.play()
                
                brick = Actor("block_broken", anchor = ["left", "top"])
                brick.pos = super_brick.pos 
                all_bricks.append(brick)

        for brick_bis in all_bricks_bis:
            if all_second_balls[i].colliderect(brick_bis):
                sounds.impact5.play()
                all_bricks_bis.remove(brick_bis)
                invert_vertical_speed_second_ball(i)
                
                rdm = randint(0, 100)
                if rdm <= power_up_apparition:
                    power_up = Actor("powerup_bigger_player", anchor = ["left", "top"])
                    power_up.pos = brick_bis.pos 
                    all_power_up_bigger_player.append(power_up)
                
                if rdm >= two_balls_apparition:
                    balls_multiples = Actor("balls_multiples", anchor = ["left", "top"])
                    balls_multiples.pos = brick_bis.pos
                    all_balls_multiples.append(balls_multiples) 

        for super_brick_bis in all_super_bricks_bis:
            if super_brick_bis.colliderect(all_second_balls[i]):
                sounds.impact5.play()
                all_super_bricks_bis.remove(super_brick_bis)
                invert_vertical_speed_second_ball(i)
                            
                brick_bis = Actor("block_sad", anchor = ["left", "top"])
                brick_bis.pos = super_brick_bis.pos 
                all_bricks_bis.append(brick_bis)

        for hyper_brick in all_hyper_bricks:
            if hyper_brick.colliderect(all_second_balls[i]):
                sounds.impact5.play()
                all_hyper_bricks.remove(hyper_brick)
                invert_vertical_speed_second_ball(i)
                super_brick_bis = Actor("block_dum", anchor = ["left", "top"])
                super_brick_bis.pos = hyper_brick.pos 
                all_super_bricks_bis.append(super_brick_bis)

        

    
    


        


