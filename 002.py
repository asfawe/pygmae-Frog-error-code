import pygame as pg

pg.init()

# 게임 기초 설정
실행여부 = True
화면가로길이,화면세로길이 = 800, 450
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('동족을 노역장에서 구출하라!')

배경이미지 = pg.image.load('img/배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))

개리뛰기이미지 = pg.image.load('img/개리-뛰는-모습1.png')
개리뛰기이미지 = pg.transform.scale(개리뛰기이미지, (100, 100))

돌이미지 = pg.image.load('img/돌.png')
돌이미지 = pg.transform.scale(돌이미지, (100, 100))   

while 실행여부:
    화면.blit(배경이미지, (0,0))

    화면.blit(개리뛰기이미지, (70,255))

    화면.blit(돌이미지, (500,280))

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            실행여부 = False

    pg.display.update()

pg.display.quit()