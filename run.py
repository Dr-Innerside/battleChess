import pygame

# 1. 기본 초기화(반드시 해야됨)
pygame.init()
#   화면 크기 설정
screen_width = 1200  # 가로
screen_height = 1000  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
#   화면 타이틀
pygame.display.set_caption("Battle Chess")
#   Frame Per Second
clock = pygame.time.Clock()

# 2. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도)
#   체스 보드
board = pygame.image.load('img/ChessBoard.png')
#   플레이어 피스
player = pygame.image.load('img/Player.png')
#   에너미 피스
enemy = pygame.image.load('img/Enemy.png')
#   킹 피스
king = pygame.image.load('img/King.png')
#   일시정지 아이콘
pause = pygame.image.load('img/Pause.png')
#   대시보드 테두리
gray = pygame.image.load('img/DarkGray.png')
#   대시보드 설명 테두리
whitegray = pygame.image.load('img/grayback.png')
#   타이틀 이미지
title = pygame.image.load('img/Title.png')
#   일시정지 테두리
wood = pygame.image.load('img/wood.png')


#   이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)

    #   이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 나가기 버튼을 누르면
            running = False  # 게임이 진행중이 아님

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(board, (200,0))
    screen.blit(title, (0,0))
    screen.blit(whitegray, (0, 200))
    screen.blit(gray, (0,300))
    screen.blit(whitegray, (0,500))
    screen.blit(gray, (0, 600))
    screen.blit(whitegray, (0, 800))
    screen.blit(wood, (0,900))
    screen.blit(pause, (58,907))



    pygame.display.update()  # 게임 화면을 다시 그리기!

# 게임 종료
pygame.quit()
