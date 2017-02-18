# Thomas Rochman (ttr5n)
'''

Character designs and running animations by Hope Radel

'''

import random, gamebox, pygame

camera = gamebox.Camera(1280, 800)
p1 = gamebox.from_color(100, 50, "red", 30, 60)
p2 = gamebox.from_color(700, 50, "red", 30, 60)
ground = gamebox.from_color(400, 450, "black", 750, 100)
backgroundimg = gamebox.from_image(640, 300, "background.png")
groundimg = gamebox.from_image(400, 600, "Ground.png")
on_button = gamebox.from_color(550, 650, "red", 100, 50)
off_button = gamebox.from_color(730, 650, "green", 100, 50)
platform_1 = gamebox.from_color(200, 250, "black", 100, 10)
platform_2 = gamebox.from_color(600, 250, "black", 100, 10)
platform_3 = gamebox.from_color(400, 100, "black", 200, 10)
platform_4 = gamebox.from_color(750, 300, "black", 200, 10)
platform_5 = gamebox.from_color(50, 300, "black", 200, 10)
platforms = [platform_1, platform_2, platform_3, platform_4, platform_5]
platformimage1 = gamebox.from_image(platform_1.x, platform_1.y, "platform_image1.png")
platformimage2 = gamebox.from_image(platform_2.x, platform_2.y, "platform_image1.png")
platformimage3 = gamebox.from_image(platform_3.x, platform_3.y, "platform_image2.png")
platformimage4 = gamebox.from_image(platform_4.x, platform_4.y, "platform_image2.png")
platformimage5 = gamebox.from_image(platform_5.x, platform_5.y, "platform_image2.png")
platformimages = [platformimage1, platformimage2, platformimage3, platformimage4, platformimage5]

p1.yspeed = 0
p2.yspeed = 0
p1_direction = "right"
p2_direction = "left"
punch = gamebox.from_color(550, 50, "green", 10, 10)
count = 0
temp = 0
menu = -1
p2_on = False
p1_death = False
p2_death = False
p1_stat = 0
p2_stat = 0
p1_xhitspeed = 0
p2_xhitspeed = 0
p1_yhitspeed = 0
p2_yhitspeed = 0
p1_punches = {"punch1": 0, "punch2": 0, "punch3": 0}
p2_punches = {"punch1": 0, "punch2": 0, "punch3": 0}
stock_box = gamebox.from_color(320, 300, "red", 125, 70)
time_box = gamebox.from_color(960, 300, "green", 125, 70)
mode = "time"
submode = 1
winner = ""
p1_airjump = True
p2_airjump = True

p1_charsheet = gamebox.load_sprite_sheet("Char1_Spritesheet.png", 2, 9)
p2_charsheet = gamebox.load_sprite_sheet("Char2_spritesheet.png", 2, 9)
p2_char = gamebox.from_image(0, 0, p2_charsheet[0])
p1_char = gamebox.from_image(0, 0, p1_charsheet[0])
extra_hit1 = gamebox.from_image(0, 0, p1_charsheet[7])
extra_hit2 = gamebox.from_image(0, 0, p2_charsheet[7])
p1_showtime = 0
p1_hitshowtime = 0
p2_showtime = 0
p2_hitshowtime = 0
p1_hittime = 0
p2_hittime = 0
p2_charrunning = gamebox.load_sprite_sheet("Char2_running.png", 2, 15)
p1_charrunning = gamebox.load_sprite_sheet("Char1_running.png", 2, 11)
r2 = 0
r1 = 0

p1_points = 0
p2_points = 0

hitsound = gamebox.load_sound("Explosion.wav")
clicksound = gamebox.load_sound("Click Sound.wav")
jumpsound = gamebox.load_sound("Jump.wav")


def tick(keys):
    global count, temp, p1_direction, p2_direction, menu, p2_on, p1_stat, p2_stat, p1_death, p2_death, p1_xhitspeed, \
        p1_yhitspeed, p2_xhitspeed, p2_yhitspeed, p1_punches, p2_punches, mode, submode, winner, p1_points, p2_points, \
        p1_char, p1_showtime, p2_showtime, p1_airjump, p2_airjump, p1_hitshowtime, p2_hitshowtime, p1_hittime, \
        p2_hittime, r2, r1

    if menu == -1:
        camera.clear("white")

        # Words
        camera.draw(gamebox.from_text(640, 725, "Press 'Enter' to Start", "Arial", 24, "blue"))
        camera.draw(gamebox.from_text(640, 300, "Controls:", "Arial", 48, "blue"))
        camera.draw(gamebox.from_text(640, 350, "Player 1       Player 2", "Arial", 24, "blue"))
        camera.draw(gamebox.from_text(640, 375, "Movement : Arrow Keys       Movement : WASD", "Arial", 24, "blue"))
        camera.draw(gamebox.from_text(640, 400, "Attack : Z       Attack : .", "Arial", 24, "blue"))
        camera.draw(gamebox.from_text(640, 200, "Battle Royal", "Arial", 96, "blue"))

        # Player 2 Choice
        camera.draw(gamebox.from_text(640, 600, "Player 2:", "Arial", 24, "blue"))
        camera.draw(on_button)
        camera.draw(off_button)
        camera.draw(gamebox.from_text(550, 650, "ON", "Arial", 24, "black"))
        camera.draw(gamebox.from_text(730, 650, "OFF", "Arial", 24, "black"))

        leftmouse, middlemouse, rightmouse = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 500 <= mouse_x <= 600 and 625 <= mouse_y <= 675:
            if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                p2_on = True
                on_button.color = "green"
                off_button.color = "red"
                clicksound.play()
        if 580 <= mouse_x <= 780 and 625 <= mouse_y <= 675:
            if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                p2_on = False
                on_button.color = "red"
                off_button.color = "green"
                clicksound.play()

        if pygame.K_RETURN in keys:
            menu = 1
            keys.remove(pygame.K_RETURN)

    elif menu == 1:
        camera.clear("white")
        camera.draw(gamebox.from_color(320, 300, "black", 150, 80))
        camera.draw(gamebox.from_color(960, 300, "black", 150, 80))
        camera.draw(stock_box)
        camera.draw(time_box)
        camera.draw(gamebox.from_text(640, 200, "Settings", "Arial", 48, "black"))
        camera.draw(gamebox.from_text(320, 300, "Lives", "Arial", 48, "black"))
        camera.draw(gamebox.from_text(960, 300, "Time", "Arial", 48, "black"))
        camera.draw(gamebox.from_text(640, 750, "Press 'Enter' to Start", "Arial", 48, "black"))
        camera.draw(gamebox.from_color(640, 500, "black", 400, 140))
        camera.draw(gamebox.from_color(640, 500, "white", 300, 120))
        camera.draw(gamebox.from_color(800, 500, "blue", 60, 120))
        camera.draw(gamebox.from_color(480, 500, "blue", 60, 120))
        if submode == 1:
            camera.draw(gamebox.from_color(480, 500, "grey", 60, 120))
        if submode == 99:
            camera.draw(gamebox.from_color(800, 500, "grey", 60, 120))
        leftmouse, middlemouse, rightmouse = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 270 <= mouse_x <= 370 and 250 <= mouse_y <= 350:
            if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                mode = "stock"
                stock_box.color = "green"
                time_box.color = "red"
                clicksound.play()
        if 910 <= mouse_x <= 1010 and 250 <= mouse_y <= 350:
            if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                mode = "time"
                time_box.color = "green"
                stock_box.color = "red"
                clicksound.play()
        if mode == "stock":
            camera.draw(gamebox.from_text(640, 500, str(submode) + " Lives", "Arial", 48, "black"))
            if 730 <= mouse_x <= 830 and 440 <= mouse_y <= 560 and submode != 99:
                if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                    submode += 1
                    camera.draw(gamebox.from_color(800, 500, "green", 60, 120))
            if 450 <= mouse_x <= 510 and 440 <= mouse_y <= 560 and submode != 1:
                if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                    submode -= 1
                    camera.draw(gamebox.from_color(480, 500, "green", 60, 120))
        elif mode == "time":
            camera.draw(gamebox.from_text(640, 500, str(submode) + ":00", "Arial", 48, "black"))
            if 730 <= mouse_x <= 830 and 440 <= mouse_y <= 560 and submode != 99:
                if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                    submode += 1
                    camera.draw(gamebox.from_color(800, 500, "green", 60, 120))
            if 450 <= mouse_x <= 510 and 440 <= mouse_y <= 560 and submode != 1:
                if leftmouse == 1 or middlemouse == 1 or rightmouse == 1:
                    submode -= 1
                    camera.draw(gamebox.from_color(480, 500, "green", 60, 120))
        if pygame.K_RETURN in keys:
            menu = 0

    elif menu == 0:
        if p1.x < -500 or p1.x > 1400 or p1.y < -200 or p1.y > 800:
            camera.center = [p2.x, p2.y]
        elif p2.x < -500 or p2.x > 1400 or p2.y < -200 or p2.y > 800:
            camera.center = [p1.x, p1.y]
        else:
            camera.center = [(p1.x + p2.x)/2, (p1.y + p2.y)/2]
        camera.clear("white")
        camera.draw(backgroundimg)
        # camera.draw(ground)
        for platformimage in platformimages:
            camera.draw(platformimage)
        camera.draw(groundimg)
        count += float(1/30)
        if p1_death is False:
            p1.yspeed += 5
        elif p1_death is True:
            p1.yspeed = 0
        if p2_death is False:
            p2.yspeed += 5
        elif p2_death is True:
            p2.yspeed = 0
        p1.y += p1.yspeed
        p2.y += p2.yspeed
        p1_punch = gamebox.from_color(400, 600, "black", 1, 1)
        p2_punch = gamebox.from_color(400, 600, "black", 1, 1)

        # Hit movement
        if p1_xhitspeed != 0:
            p1.x += p1_xhitspeed
            if p1_xhitspeed > 0:
                p1_xhitspeed -= 1
            elif p1_xhitspeed < 0:
                p1_xhitspeed += 1
        if p1_yhitspeed != 0:
            p1.y += p1_yhitspeed
            if p1_yhitspeed > 0:
                p1_yhitspeed -= 1
            elif p1_yhitspeed < 0:
                p1_yhitspeed += 1
        if p2_xhitspeed != 0:
            p2.x += p2_xhitspeed
            if p2_xhitspeed > 0:
                p2_xhitspeed -= 1
            elif p2_xhitspeed < 0:
                p2_xhitspeed += 1
        if p2_yhitspeed != 0:
            p2.y += p2_yhitspeed
            if p2_yhitspeed > 0:
                p2_yhitspeed -= 1
            elif p2_yhitspeed < 0:
                p2_yhitspeed += 1

        # p1 actions
        if p1_direction == "right":
            p1.color = "red"
        elif p1_direction == "left":
            p1.color = "green"
        if pygame.K_RIGHT in keys and p2_punch.touches(p1) == False and count > p1_hittime + 1/4:
            p1.x += 15
            p1_direction = "right"
            p1_death = False
        if pygame.K_LEFT in keys and p2_punch.touches(p1) == False and count > p1_hittime + 1/4:
            p1.x -= 15
            p1_direction = "left"
            p1_death = False
        if pygame.K_DOWN in keys:
            p1_death = False
        if pygame.K_DOWN not in keys:
            for platform in platforms:
                if p1.bottom_touches(platform):
                    p1.move_to_stop_overlapping(platform)
                    p1_airjump = True
                    if p1.yspeed > 0:
                        p1.yspeed = 0
                    if pygame.K_UP in keys and count > p1_hittime + 1/4:
                        p1.yspeed -= 45
                        jumpsound.play()
                        keys.remove(pygame.K_UP)
        if p1.touches(ground):
            p1.move_to_stop_overlapping(ground)
            p1.yspeed = 0
            p1_airjump = True
        if pygame.K_UP in keys and p1.touches(ground) and count > p1_hittime + 1/4:
            p1.yspeed -= 45
            keys.remove(pygame.K_UP)
            jumpsound.play()
        elif pygame.K_UP in keys and p1_airjump:
            jumpsound.play()
            p1.yspeed -= 45
            if p1.touches(ground) is False:
                p1_airjump = False
        if p1.bottom_touches(ground) and pygame.K_z in keys and p1_punches["punch3"] == 0 and \
                        count > p1_punches["punch1"] + 1/4 and count > p1_punches["punch2"] + 1/4 or pygame.K_z in \
                keys and p1.bottom_touches(ground) is False:
            p1_death = False
            if pygame.K_UP in keys:
                p1_punch = gamebox.from_color(p1.x, p1.y - 40, "blue", 30, 40)
                # camera.draw(p1_punch)
            elif pygame.K_RIGHT in keys:
                p1_punch = gamebox.from_color(p1.x + 20, p1.y, "blue", 40, 30)
                # camera.draw(p1_punch)
            elif pygame.K_LEFT in keys:
                p1_punch = gamebox.from_color(p1.x - 20, p1.y, "blue", 40, 30)
                # camera.draw(p1_punch)
            elif pygame.K_DOWN in keys and p1.touches(ground) == False:
                p1_punch = gamebox.from_color(p1.x, p1.y + 40, "blue", 30, 40)
                # camera.draw(p1_punch)
            else:
                if p1_direction == "right":
                    p1_punch = gamebox.from_color(p1.x + 20, p1.y, "blue", 40, 30)
                    # camera.draw(p1_punch)
                elif p1_direction == "left":
                    p1_punch = gamebox.from_color(p1.x - 20, p1.y, "blue", 40, 30)
                    # camera.draw(p1_punch)

        # p2 actions
        if p2_on:
            if p2_direction == "right":
                p2.color = "red"
            elif p2_direction == "left":
                p2.color = "green"
            if pygame.K_d in keys and p1_punch.touches(p2) == False and count > p2_hittime + 1/4:
                p2.x += 15
                p2_direction = "right"
                p2_death = False
            if pygame.K_a in keys and p1_punch.touches(p2) == False and count > p2_hittime + 1/4:
                p2.x -= 15
                p2_direction = "left"
                p2_death = False
            if pygame.K_s in keys:
                p2_death = False
            if pygame.K_s not in keys:
                for platform in platforms:
                    if p2.bottom_touches(platform):
                        p2.move_to_stop_overlapping(platform)
                        p2_airjump = True
                        if p2.yspeed > 0:
                            p2.yspeed = 0
                        if pygame.K_w in keys and count > p2_hittime + 1/4:
                            p2.yspeed -= 45
                            jumpsound.play()
                            keys.remove(pygame.K_w)
            if p2.touches(ground):
                p2.move_to_stop_overlapping(ground)
                p2.yspeed = 0
                p2_airjump = True
            if pygame.K_w in keys and p2.touches(ground) and count > p2_hittime + 1/4:
                p2.yspeed -= 45
                keys.remove(pygame.K_w)
                jumpsound.play()
            elif pygame.K_w in keys and p2_airjump:
                p2.yspeed -= 45
                jumpsound.play()
                if p2.touches(ground) is False:
                    p2_airjump = False
            if p2.bottom_touches(ground) and pygame.K_PERIOD in keys and p2_punches["punch3"] == 0 and \
                            count > p2_punches["punch1"] + 1/4 and count > p2_punches["punch2"] + 1/4 or \
                            pygame.K_PERIOD in keys and p2.bottom_touches(ground) is False:
                p2_death = False
                if pygame.K_w in keys:
                    p2_punch = gamebox.from_color(p2.x, p2.y - 40, "blue", 30, 40)
                    # camera.draw(p2_punch)
                elif pygame.K_d in keys:
                    p2_punch = gamebox.from_color(p2.x + 20, p2.y, "blue", 40, 30)
                    # camera.draw(p2_punch)
                elif pygame.K_a in keys:
                    p2_punch = gamebox.from_color(p2.x - 20, p2.y, "blue", 40, 30)
                    # camera.draw(p2_punch)
                elif pygame.K_s in keys and p2.touches(ground) == False:
                    p2_punch = gamebox.from_color(p2.x, p2.y + 40, "blue", 30, 40)
                    # camera.draw(p2_punch)
                else:
                    if p2_direction == "right":
                        p2_punch = gamebox.from_color(p2.x + 20, p2.y, "blue", 40, 30)
                        # camera.draw(p2_punch)
                    elif p2_direction == "left":
                        p2_punch = gamebox.from_color(p2.x - 20, p2.y, "blue", 40, 30)
                        # camera.draw(p2_punch)
            camera.draw(gamebox.from_text(p2.x, p2.y - 40, "Player 2", "Arial", 12, "blue", bold=True))

        elif p2_on is False:
            if p2.touches(ground):
                p2.move_to_stop_overlapping(ground)
                p2.yspeed = 0
            for platform in platforms:
                if p2.bottom_touches(platform) and p1.y <= p2.y:
                    p2.move_to_stop_overlapping(platform)
                    if p2.yspeed > 0:
                        p2.yspeed = 0
            if p2_death is False:
                p2.yspeed += 5
                if 775 > p1.x > p2.x and p1_punch.touches(p2) is False and count > p2_hittime + 1/4:
                    p2.x += 10
                    p2_direction = "right"
                elif 25 < p1.x < p2.x and p1_punch.touches(p2) is False and count > p2_hittime + 1/4:
                    p2.x -= 10
                    p2_direction = "left"
                if p2.touches(p1) and p1_punch.touches(p2) is False and count > p2_hittime + 1/4:
                    p2.move_to_stop_overlapping(p1)
                    rand = random.randint(0,70)
                    if rand < 10:
                        if p1.y < p2.y:
                            p2_punch = gamebox.from_color(p2.x, p2.y - 40, "blue", 30, 40)
                            # camera.draw(p2_punch)
                        elif p1.y > p2.y:
                            p2_punch = gamebox.from_color(p2.x, p2.y + 40, "blue", 30, 40)
                            # camera.draw(p2_punch)
                        elif p2_direction == "right":
                            p2_punch = gamebox.from_color(p2.x + 20, p2.y, "blue", 30, 40)
                            # camera.draw(p2_punch)
                        elif p2_direction == "left":
                            p2_punch = gamebox.from_color(p2.x - 20, p2.y, "blue", 30, 40)
                            # camera.draw(p2_punch)
                if p1.y < p2.y and p2.bottom_touches(ground) and count > p2_hittime + 1/4:
                    p2.yspeed -= 60
            elif p2_death:
                p2_death = False


            camera.draw(gamebox.from_text(p2.x, p2.y - 40, "COMPUTER", "Arial", 12, "blue", bold=True))

        # Hit Mechanics
        if p1_punch.touches(p2):
            p2_hittime = count
            hitsound.play()
        if p2_punch.touches(p1):
            p1_hittime = count
            hitsound.play()
        if p1_punch.touches(p2) and p1.bottom_touches(ground) is False:
            p2_stat += 1
            if p1.x > p2.x:
                p2_xhitspeed -= p2_stat
            elif p1.x < p2.x:
                p2_xhitspeed += p2_stat
            if p1.y >= p2.y:
                p2_yhitspeed -= p2_stat
            elif p1.y < p2.y:
                p2_yhitspeed += p2_stat
        elif p1_punch.touches(p2) and p1_punches["punch1"] == 0 and p2_death is False:
            p2_stat += 1
            p2.yspeed = 0
            p1_punches["punch1"] = count
        elif p1_punch.touches(p2) and p1_punches["punch1"] != 0 and p1_punches["punch2"] == 0 and \
                        count > p1_punches["punch1"] + 1/4:
            p2_stat += 2
            p2.yspeed = 0
            p1_punches["punch2"] = count
        elif p1_punch.touches(p2) and p1_punches["punch2"] != 0 and count > p1_punches["punch2"] + 1/4:
            p2_stat += 3
            p2.yspeed = 0
            if p1.x > p2.x:
                p2_xhitspeed -= p2_stat
            elif p1.x < p2.x:
                p2_xhitspeed += p2_stat
            if p1.y >= p2.y:
                p2_yhitspeed -= p2_stat
            elif p1.y < p2.y:
                p2_yhitspeed += p2_stat
            p1_punches["punch3"] = count

        if p1_punches["punch1"] != 0 and p1_punches["punch2"] == 0 and p1_punches["punch3"] == 0:
            if count > p1_punches["punch1"] + 1:
                p1_punches["punch1"] = 0
        elif p1_punches["punch2"] != 0 and p1_punches["punch3"] == 0:
            if count > p1_punches["punch2"] + 1:
                p1_punches["punch1"] = 0
                p1_punches["punch2"] = 0
        elif p1_punches["punch3"] != 0:
            if count > p1_punches["punch3"] + 1:
                p1_punches["punch1"] = 0
                p1_punches["punch2"] = 0
                p1_punches["punch3"] = 0

        if p2_punch.touches(p1) and p2.bottom_touches(ground) == False:
            p1_stat += 1
            if p2.x > p1.x:
                p1_xhitspeed -= p1_stat
            elif p2.x < p1.x:
                p1_xhitspeed += p1_stat
            if p2.y >= p1.y:
                p1_yhitspeed -= p1_stat
            elif p2.y < p1.y:
                p1_yhitspeed += p1_stat
        elif p2_punch.touches(p1) and p2_punches["punch1"] == 0 and p2_punches["punch2"] == 0 and p1_death is False:
            p1_stat += 1
            p1.yspeed = 0
            p2_punches["punch1"] = count
        elif p2_punch.touches(p1) and p2_punches["punch1"] != 0 and p2_punches["punch2"] == 0 and \
                        count > p2_punches["punch1"] + 1/4:
            p1_stat += 2
            p1.yspeed = 0
            p2_punches["punch2"] = count
        elif p2_punch.touches(p1) and p2_punches["punch2"] != 0 and count > p2_punches["punch2"] + 1/4:
            p1_stat += 3
            p1.yspeed = 0
            if p2.x > p1.x:
                p1_xhitspeed -= p1_stat
            elif p2.x < p1.x:
                p1_xhitspeed += p1_stat
            if p2.y >= p1.y:
                p1_yhitspeed -= p1_stat
            elif p2.y < p1.y:
                p1_yhitspeed += p1_stat
            p2_punches["punch3"] = count

        if p2_punches["punch1"] != 0 and p2_punches["punch2"] == 0 and p2_punches["punch3"] == 0:
            if count > p2_punches["punch1"] + 1:
                p2_punches["punch1"] = 0
        elif p2_punches["punch1"] != 0 and p2_punches["punch2"] != 0 and p2_punches["punch3"] == 0:
            if count > p2_punches["punch2"] + 1:
                p2_punches["punch1"] = 0
                p2_punches["punch2"] = 0
        elif p2_punches["punch1"] != 0 and p2_punches["punch2"] != 0 and p2_punches["punch3"] != 0:
            if count > p2_punches["punch3"] + 1:
                p2_punches["punch1"] = 0
                p2_punches["punch2"] = 0
                p2_punches["punch3"] = 0


        # Die Mechanics
        if p1.x > 1500 or p1.x < -500 or p1.y > 1000 or p1.y < -500:
            p1.x = 350
            p1.y = 50
            p1_xhitspeed = 0
            p1_yhitspeed = 0
            p1_stat = 0
            p2_points += 1
            p1_death = True
        if p2.x > 1500 or p2.x < -500 or p2.y > 1000 or p2.y < -500:
            p2.x = 450
            p2.y = 50
            p2_xhitspeed = 0
            p2_yhitspeed = 0
            p2_stat = 0
            p1_points += 1
            p2_death = True

        # Extra Camera
        if p1_direction == "left":
            left1 = 9
            lr1 = 11
        else:
            left1 = 0
            lr1 = 0
        extra_hit1.center = (p1_punch.x, p1_punch.y)
        if p2_punch.touches(p1):
            p1_char.image = p1_charsheet[1 + left1]
            p1_hitshowtime = count
        elif count < p1_hitshowtime + 1/4:
            p1_char.image = p1_charsheet[1 + left1]
        elif p1.bottom_touches(ground) is False and pygame.K_z in keys or pygame.K_UP in keys and pygame.K_z in keys:
            p1_char.image = p1_charsheet[3 + left1]
            p1_showtime = count
            camera.draw(extra_hit1)
        elif count < p1_showtime + 1/4:
            p1_char.image = p1_charsheet[3 + left1]
        elif p1_punches["punch2"] != 0 and count < p1_punches["punch3"] + 1/4:
            p1_char.image = p1_charsheet[6 + left1]
        elif p1_punches["punch1"] != 0 and count < p1_punches["punch2"] + 1/4:
            p1_char.image = p1_charsheet[5 + left1]
        elif pygame.K_z in keys and p1_punches["punch3"] == 0 or count < p1_punches["punch1"] + 1/4:
            p1_char.image = p1_charsheet[4 + left1]
        elif p1.bottom_touches(ground) is False and p1_char.bottom_touches(platform_1) is False and \
                        p1_char.bottom_touches(platform_2) is False and p1_char.bottom_touches(platform_3) is False \
                and p1_char.bottom_touches(platform_4) is False and p1_char.bottom_touches(platform_5) is False:
            p1_char.image = p1_charsheet[2 + left1]
        elif pygame.K_RIGHT in keys or pygame.K_LEFT in keys:
            p1_char.image = p1_charrunning[r1 + lr1]
            r1 += 1
            if r1 == 10:
                r1 = 0
        else:
            p1_char.image = p1_charsheet[0 + left1]
            r1 = 0
        if pygame.K_z in keys:
            keys.remove(pygame.K_z)

        if p2_direction == "left":
            left2 = 9
            lr2 = 15
        else:
            left2 = 0
            lr2 = 0
        extra_hit2.center = (p2_punch.x, p2_punch.y)
        if p1_punch.touches(p2):
            p2_char.image = p2_charsheet[1 + left2]
            p2_hitshowtime = count
        elif count < p2_hitshowtime + 1/4:
            p2_char.image = p2_charsheet[1 + left2]
        elif p2.bottom_touches(ground) is False and pygame.K_PERIOD in keys or pygame.K_w in keys and pygame.K_PERIOD \
                in keys:
            p2_char.image = p2_charsheet[3 + left2]
            p2_showtime = count
            camera.draw(extra_hit2)
        elif count < p2_showtime + 1/4:
            p2_char.image = p2_charsheet[3 + left2]
        elif p2_punches["punch2"] != 0 and count < p2_punches["punch3"] + 1/4:
            p2_char.image = p2_charsheet[6 + left2]
        elif p2_punches["punch1"] != 0 and count < p2_punches["punch2"] + 1/4:
            p2_char.image = p2_charsheet[5 + left2]
        elif pygame.K_PERIOD in keys and p2_punches["punch1"] == 0 or count < p2_punches["punch1"] + 1/4:
            p2_char.image = p2_charsheet[4 + left2]
        elif p2.bottom_touches(ground) is False and p2_char.bottom_touches(platform_1) is False and \
                        p2_char.bottom_touches(platform_2) is False and p2_char.bottom_touches(platform_3) is False \
                and p2_char.bottom_touches(platform_4) is False and p2_char.bottom_touches(platform_5) is False:
            p2_char.image = p2_charsheet[2 + left2]
        elif pygame.K_d in keys or pygame.K_a in keys:
            p2_char.image = p2_charrunning[r2 + lr2]
            r2 += 1
            if r2 == 14:
                r2 = 1
        elif p2_on is False:
            if p2.bottom_touches(ground) or p2.bottom_touches(platform_1) or p2.bottom_touches(platform_2) or \
                            p2.bottom_touches(platform_3) or p2.bottom_touches(platform_4) or \
                            p2.bottom_touches(platform_5):
                    p2_char.image = p2_charrunning[r2 + lr2]
                    r2 += 1
                    if r2 == 14:
                        r2 = 1
        else:
            p2_char.image = p2_charsheet[0 + left2]
            r2 = 0

        if pygame.K_PERIOD in keys:
            keys.remove(pygame.K_PERIOD)

        camera.draw(gamebox.from_text(p1.x, p1.y - 40, "Player 1", "Arial", 12, "red", bold=True))
        # camera.draw(p1)
        p1_char.center = (p1.x, p1.y)
        camera.draw(p1_char)
        # camera.draw(p2)
        p2_char.center = (p2.x, p2.y)
        camera.draw(p2_char)
        camera.draw(gamebox.from_color(camera.x - 400, camera.y + 300, "red", 150, 300))
        camera.draw(gamebox.from_color(camera.x + 400, camera.y + 300, "blue", 150, 300))
        camera.draw(gamebox.from_text(camera.x - 400, camera.y + 200, "Player 1", "Arial", 24, "white", bold=True))
        camera.draw(gamebox.from_text(camera.x - 400, camera.y + 250, "Hit Rate", "Arial", 24, "white", bold=True))
        camera.draw(gamebox.from_text(camera.x + 400, camera.y + 250, "Hit Rate", "Arial", 24, "white", bold=True))
        if p1_stat < 36:
            camera.draw(gamebox.from_color(camera.x - 400, camera.y + 275, "green", p1_stat*3, 30))
            camera.draw(gamebox.from_text(camera.x - 400, camera.y + 275, str(p1_stat * 5), "Arial", 24,
                                      "white", bold=True))
        else:
            camera.draw(gamebox.from_text(camera.x - 400, camera.y + 275, "DANGER", "Arial", 24,
                                      "white", bold=True))
        if p2_stat < 36:
            camera.draw(gamebox.from_color(camera.x + 400, camera.y + 275, "green", p2_stat*3, 30))
            camera.draw(gamebox.from_text(camera.x + 400, camera.y + 275, str(p2_stat * 5), "Arial", 24,
                                      "white", bold=True))
        else:
            camera.draw(gamebox.from_text(camera.x + 400, camera.y + 275, "DANGER", "Arial", 24,
                                      "white", bold=True))
        if mode == "time":
            second_time = submode * 60 - count
            if second_time < 10:
                zero = "0"
            else:
                zero = ""
            timer = str(format(second_time // 60, '2.0f')) + ":" + zero + str(format(second_time % 60, '.0f'))
            camera.draw(gamebox.from_text(camera.x, camera.y - 370, timer, "Arial", 48, "blue", bold=True))
            if second_time <= 0:
                if p1_points > p2_points:
                    winner = "Player 1"
                elif p2_points > p1_points:
                    winner = "Player 2"
                elif p2_points == p1_points:
                    winner = "Tie"
                menu = 2
        if mode == "stock":
            p1_lives = submode - p2_points
            p2_lives = submode - p1_points
            camera.draw(gamebox.from_text(camera.x - 400, camera.y + 350, str(p1_lives) + " Lives", "Arial", 24,
                                          "white", bold=True))
            camera.draw(gamebox.from_text(camera.x + 400, camera.y + 350, str(p2_lives) + " Lives", "Arial", 24,
                                          "white", bold=True))
            if p1_lives == 0:
                winner = "Player 2"
                menu = 2
            elif p2_lives == 0:
                winner = "Player 1"
                menu = 2

        if p2_on:
            camera.draw(gamebox.from_text(camera.x + 400, camera.y + 200, "Player 2", "Arial", 24, "white", bold=True))
        elif p2_on is False:
            camera.draw(gamebox.from_text(camera.x + 400, camera.y + 200, "COM", "Arial", 24, "white", bold=True))
    elif menu == 2:
        camera.clear("white")
        camera.draw(gamebox.from_text(camera.x, camera.y - 100, "Winner:", "Arial", 24, "black", bold=True))
        if winner == "Player 1":
            camera.draw(gamebox.from_text(camera.x, camera.y, winner + " with " + str(p1_points) + " kills", "Arial",
                                          48, "black", bold=True))
        elif winner == "Player 2":
            camera.draw(gamebox.from_text(camera.x, camera.y, winner + " with " + str(p2_points) + " kills", "Arial",
                                          48, "black", bold=True))
        elif winner == "Tie":
            camera.draw(gamebox.from_text(camera.x, camera.y, winner + " by " + str(p1_points) + " kills", "Arial",
                                          48, "black", bold=True))
        camera.draw(gamebox.from_text(camera.x, camera.y + 300, "Press 'Enter' to End", "Arial", 24, "black"))
        if pygame.K_RETURN in keys:
            gamebox.stop_loop()
    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
