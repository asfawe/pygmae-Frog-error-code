import pygame as pg
import random

# 이미지 초기화
def 스프라이트생성(이미지):
    스프라이트 = pg.sprite.Sprite()
    스프라이트.image = 이미지
    스프라이트.rect = 스프라이트.image.get_rect()
    return 스프라이트

pg.init()

# 게임 기초 설정
실행여부 = True
화면가로길이,화면세로길이 = 800, 450
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('동족을 노역장에서 구출하라!')

배경이미지 = pg.image.load('img/배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))

개리점프이미지 = pg.image.load('img/개리-뛰는-모습5(점프).png')
개리점프이미지 = pg.transform.scale(개리점프이미지, (100, 100))
개리착지이미지 = pg.image.load('img/개리-뛰는-모습6(착지).png')
개리착지이미지 = pg.transform.scale(개리착지이미지, (100, 100))

개리뛰기이미지리스트 = [pg.image.load(f'img/개리-뛰는-모습{인덱스}.png') for 인덱스 in range(1,5)]
for 인덱스 in range(len(개리뛰기이미지리스트)):
    개리뛰기이미지리스트[인덱스] = pg.transform.scale(개리뛰기이미지리스트[인덱스], (100,100))
개리스프라이트 = 스프라이트생성(개리뛰기이미지리스트[0])

돌이미지 = pg.image.load('img/돌.png')
돌이미지 = pg.transform.scale(돌이미지, (100, 100)) 

개리동료이미지 = pg.image.load('img/동료_구출 전.png')
개리동료이미지 = pg.transform.scale(개리동료이미지, (100,100))
개리동료구출이미지 = pg.image.load('img/동료_구출-후.png')
개리동료구출이미지 = pg.transform.scale(개리동료구출이미지, (100,100))
개리동료스프라이트 = 스프라이트생성(개리동료이미지)

포탈이미지 = pg.image.load('img/포탈.png')
포탈이미지 = pg.transform.scale(포탈이미지, (100,100))
포탈스프라이트 = 스프라이트생성(포탈이미지)

# 게임 요소 초기화
게임여부 = True
개리시작높이 = 255
점수 = 0

개리뛰기상태 = 0
개리뛰는흐름 = 1
개리동작업데이트시간 = 0
점프기본속도 = 0.1
점프속도 = 점프기본속도
점프상태 = False
개리위치 = [70, 개리시작높이]

요소들속도 = 300
돌멩이생성시간 = 1
돌멩이시작높이 = 280
돌멩이위치리스트 = [[500, 돌멩이시작높이]]
돌멩이스프라이트리스트 = [스프라이트생성(돌이미지) for _ in 돌멩이위치리스트]

개리동료구출상태 = False
개리동료최초위치 = 900
개리동료위치 = [개리동료최초위치, 개리시작높이]

포탈최초위치 = 900
포탈위치 = [포탈최초위치, 개리시작높이]

시계 = pg.time.Clock()

while 실행여부:
    if 게임여부:

        화면.blit(배경이미지, (0,0))

        # 게임 시간 계산
        경과시간 = 시계.tick(60) / 1000

        개리스프라이트.rect.x, 개리스프라이트.rect.y = 개리위치[0], 개리위치[1]
        화면.blit(개리스프라이트.image, 개리스프라이트.rect) # 개리스프라이트.image는 개리-뛰는b-모습1.png 이 들어있다.왜냐 스프라이트로 줬기 때문에다. 개리스프라이트.rect는 개리위치가 들어있다.

        # 개리 동족 및 포탈 그리기, 개리 동족 구출하기
        개리동료스프라이트.rect.x, 개리동료스프라이트.rect.y = 개리동료위치[0], 개리동료위치[1]
        화면.blit(개리동료스프라이트.image, 개리동료스프라이트.rect)

        포탈스프라이트.rect.x, 포탈스프라이트.rect.y = 포탈위치[0], 포탈위치[1]
        화면.blit(포탈스프라이트.image, 포탈스프라이트.rect)
        


        if not 개리동료구출상태:
            개리스프라이트.image = 개리동료이미지
            if pg.sprite.collide_mask(개리스프라이트, 개리동료스프라이트):
                개리동료구출상태 = True
                개리동료위치[0] = 15 # 개리 뒤 위치
                개리동료위치[1] = 개리위치[1]

            개리동료위치[0] -= 요소들속도 * 경과시간
            if 개리동료위치[0] < -50:
                개리동료위치[0] = 개리동료최초위치

        else:
            개리동료스프라이트.image = 개리동료구출이미지
            if pg.sprite.collide_mask(개리동료스프라이트, 포탈스프라이트):
                개리동료위치[0] = 개리동료최초위치
                개리동료위치[1] = 개리시작높이
                점수 += 1
                포탈위치[0] = 포탈최초위치
                개리동료구출상태 = False
                print(f'점수 = {점수}') # 점수 확인용

            포탈위치[0] -= 요소들속도 * 경과시간
            if 포탈위치[0] < -50:
                포탈위치[0] = 포탈최초위치

        for 돌멩이위치, 돌멩이스프라이트 in zip(돌멩이위치리스트, 돌멩이스프라이트리스트):
            돌멩이스프라이트.rect.x, 돌멩이스프라이트.rect.y = 돌멩이위치[0], 돌멩이위치[1]
            화면.blit(돌멩이스프라이트.image, 돌멩이스프라이트.rect)

            if pg.sprite.collide_mask(개리스프라이트, 돌멩이스프라이트) != None:
                게임여부 = False

            돌멩이위치[0] -= 요소들속도 * 경과시간
            if 돌멩이위치[0] < -100:
                돌멩이스프라이트리스트.remove(돌멩이스프라이트)
                돌멩이위치리스트.remove(돌멩이위치)

        # 개리 점프
        if 점프상태:
            개리스프라이트.image = 점프속도 > 0 and 개리점프이미지 or 개리착지이미지 # 개리스프라이트.image 에다가 개리 점프 이미지를 추가 한다.
            개리위치[1] -= 점프속도 * 경과시간 * 1000 # 마이너스가 될수록 개리는 위로 간다.
            점프속도 -= 점프기본속도 * 경과시간 * 2 # 점프속도 - 0.12 = -0.2
            if 개리동료구출상태:
                개리동료위치[1] = 개리위치[1]
            if 개리위치[1] >= 개리시작높이:
                개리위치[1] = 개리시작높이
                점프상태 = False
                점프속도 = 점프기본속도
        else:
            개리동작업데이트시간 += 경과시간
            if 개리동작업데이트시간 > 0.2:
                개리동작업데이트시간 = 0
                개리스프라이트.image = 개리뛰기이미지리스트[개리뛰기상태]
                개리뛰기상태 += 개리뛰는흐름
                if 개리뛰기상태 == len(개리뛰기이미지리스트) - 1 or 개리뛰기상태 == 0:
                    개리뛰는흐름 *= -1
        
        돌멩이생성시간 -= 경과시간
        if 돌멩이생성시간 <= 0:
            돌멩이스프라이트리스트.append(스프라이트생성(돌이미지))
            돌멩이위치리스트.append([900, 돌멩이시작높이])
            돌멩이생성시간 = random.random() * 2 + 1

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            실행여부 = False
        elif 이벤트.type == pg.KEYDOWN:
            if 게임여부 and 이벤트.key == pg.K_SPACE and not 점프상태:
                점프상태 = True

    pg.display.update()

pg.display.quit()