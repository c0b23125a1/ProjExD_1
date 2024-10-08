import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    bj_img = pg.transform.flip(bg_img, True, False)
    img_rct = kt_img.get_rect()
    img_rct.center = 300, 200
    tmr = 0
    a = 0
    b = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        a = 0
        b = 0
        # if key_lst[pg.K_UP]:
        #     img_rct.move_ip((0, -1))
        # if key_lst[pg.K_DOWN]:
        #     img_rct.move_ip((0, 1))
        # if key_lst[pg.K_LEFT]:
        #     img_rct.move_ip((-1, 0))
        # if key_lst[pg.K_RIGHT]:
        #     img_rct.move_ip((2, 0))
        # img_rct.move_ip((-1, 0))
        if key_lst[pg.K_UP]:
            a = -1
        if key_lst[pg.K_DOWN]:
            a = 1
        if key_lst[pg.K_LEFT]:
            b = -1
        if key_lst[pg.K_RIGHT]:
            b = 2
        img_rct.move_ip((-1+b, 0+a))
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bj_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bj_img, [x+4800, 0])
        screen.blit(kt_img, img_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()