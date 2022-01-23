import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600 # chiều cao màn hình
SCREEN_WIDTH = 1100 #chiều ngnang màn hình
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     #đưa màn hình ra

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),  #tải hoạt ảnh khi run
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))    #tải hoạt ảnh khi jump
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))] #tải hoạt ảnh khi ducking

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),   #tải vật cản nhỏ
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),   #tải vật cản lớn
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),    #tải hình ảnh vật cản chim
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))     #hình ảnh mây

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))   #background
DINO_0=pygame.image.load(os.path.join("Assets/Dino", "none.png"))
DINO_1=pygame.image.load(os.path.join("Assets/Dino", "sword_0.png"))
DINO_2=pygame.image.load(os.path.join("Assets/Dino", "rifle_0.png"))
DINO_3=pygame.image.load(os.path.join("Assets/Dino", "grenade_0.png"))
DINO_4=pygame.image.load(os.path.join("Assets/Dino", "halberd_0.png"))
DINO_5=pygame.image.load(os.path.join("Assets/Dino", "chainsaw_1.png"))
DINO_6=pygame.image.load(os.path.join("Assets/Dino", "bow_1.png"))
DINO_7=pygame.image.load(os.path.join("Assets/Dino", "cig_on_0.png"))
DINO_8=pygame.image.load(os.path.join("Assets/Dino", "hammer_0.png"))
DINO_9=pygame.image.load(os.path.join("Assets/Dino", "bat_still.png"))
dino_pick = 1

class Dinosaur:
    X_POS = 80  #vị trí X của khủng long
    Y_POS = 310 #vị trí Y của khủng long
    Y_POS_DUCK = 340    #vị trí Y khi khủng long duck
    JUMP_VEL = 8.5   #chỉ số tăng Y khi khủng long jump

    def __init__(self):             #khởi tạo khủng long bất cứ khi nào khủng long được tạo lại
        self.duck_img = DUCKING         #hình ảnh khủng long cúi
        self.run_img = RUNNING            #hình ảnh khủng long chạy
        self.jump_img = JUMPING           #hình ảnh khủng long chạy
        self.dino_duck = False
        self.dino_run = True                #cài đặt mặc định khủng long running
        self.dino_jump = False
        self.dino_style = DINO_0
        self.step_index = 0                      #chỉ số bước chân = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]               #hình ảnh đầu tiên khi con khủng long được chạy
        self.dino_rect = self.image.get_rect()      #hình chữ nhật làm khung cảm ứng va chạm cho hình ảnh khủng long
        self.dino_rect.x = self.X_POS         #tọa độ x và y của hình chữ nhật = tọa độ khủng long
        self.dino_rect.y = self.Y_POS


    def update(self, userInput):                      #hàm cập nhật khủng long mỗi lần lặp lại vòng while
        if self.dino_duck:          #Kiểm tra trạng thái khủng long
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:              #chỉ số bước mỗi 10 bước thì reset về 0
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:     #khi bấm up mà khủng long không jump thì khủng long jump
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:   #khi bấm down mà khủng long không duck thì khủng long duck
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):  #ếu không jump hay duck thì run
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
        if userInput[pygame.K_1]: self.dino_style = DINO_1
        if userInput[pygame.K_2]: self.dino_style = DINO_2
        if userInput[pygame.K_3]: self.dino_style = DINO_3
        if userInput[pygame.K_4]: self.dino_style = DINO_4
        if userInput[pygame.K_5]: self.dino_style = DINO_5
        if userInput[pygame.K_6]: self.dino_style = DINO_6
        if userInput[pygame.K_7]: self.dino_style = DINO_7
        if userInput[pygame.K_8]: self.dino_style = DINO_8
        

        

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]       #hình ảnh tương ứng của khủng long(khi số bước chân tứ 0 - 5 hình ảnh 1 hiển thị , từ 5 -10 hình ảnh 2 hiển thị vượt quá 10 chỉ số được đặt lại)
        self.dino_rect = self.image.get_rect()                 #tọa độ hình chữ nhật của hình ảnh khủng long
        self.dino_rect.x = self.X_POS             #đặt hình chữ nhật vào vị trí khủng long hiển thị
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1                          #tăng chỉ số bước chân lên 1

    def run(self):
        self.image = self.run_img[self.step_index // 5] #hình ảnh tương ứng của khủng long(khi số bước chân tứ 0 - 5 hình ảnh 1 hiển thị , từ 5 -10 hình ảnh 2 hiển thị vượt quá 10 chỉ số được đặt lại)
        self.dino_rect = self.image.get_rect()       #tọa độ hình chữ nhật của hình ảnh khủng long
        self.dino_rect.x = self.X_POS            #đặt hình chữ nhật vào vị trí khủng long hiển thị
        self.dino_rect.y = self.Y_POS
        self.step_index += 1                      #tăng chỉ số bước chân lên 1

    def jump(self):
        self.image = self.jump_img                                #khi khủng long jump tăng độ cao sau đố trừ dần 
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            

    def draw(self, SCREEN):                                    #hàm vẽ lên màn hình


        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        if(self.dino_style == DINO_1):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-45, self.dino_rect.y-180 )) #dino 1
        elif(self.dino_style == DINO_2):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-20, self.dino_rect.y-180 )) #dino 2
        elif(self.dino_style == DINO_3):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-40, self.dino_rect.y-180 )) #dino 3
        elif(self.dino_style == DINO_4):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-40, self.dino_rect.y-180 )) #dino 4
        elif(self.dino_style == DINO_5):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-40, self.dino_rect.y-170 )) #dino 5
        elif(self.dino_style == DINO_6):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-20, self.dino_rect.y-170 )) #dino 6
        elif(self.dino_style == DINO_7):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-25, self.dino_rect.y-160 )) #dino 7
        elif(self.dino_style == DINO_8):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-45, self.dino_rect.y-170 )) #dino 8
        elif(self.dino_style == DINO_9):
            SCREEN.blit(self.dino_style, (self.dino_rect.x-30, self.dino_rect.y-140 )) #dino 9
        else:
            SCREEN.blit(self.dino_style, (self.dino_rect.x-45, self.dino_rect.y-170 )) #dino 0

class Cloud:                                       #vẽ mây
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)            #vị trí x của mây
        self.y = random.randint(50, 100)                #vịt trí y của mây
        self.image = CLOUD                        #hình ảnh mây
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed                             #vị trí x của mây trừ theo tốc độ của game
        if self.x < -self.width:                              #khi mây vượt khỏi màn hình thì tạo lại mây
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):                         #vẽ mây lên màn hình
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:                   #vật cản
    def __init__(self, image, type):
        self.image = image                         #hình ảnh
        self.type = type                         #loại vật cản
        self.rect = self.image[self.type].get_rect()           #tọa độ hình chự nhật của vật cản
        self.rect.x = SCREEN_WIDTH         #tọa độ vật cản = độ ngang màn hình

    def update(self):                            #di chuyển chướng ngại vật trên màn hình
        self.rect.x -= game_speed                 #giảm tọa độ x của vật cản bằng tốc độ game
        if self.rect.x < -self.rect.width:          #nếu x ra khỏi màn hình thì loại bỏ
            obstacles.pop()

    def draw(self, SCREEN):                        #vẽ vật cản lên màn hình
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):                     #xương rồng nhở
        self.type = random.randint(0, 2)               #chọn ngẫu nhiên 1 trong 3 loại
        super().__init__(image, self.type)              #đưa về lớp cha
        self.rect.y = 325


class LargeCactus(Obstacle):                  #xương rồng lớn
    def __init__(self, image): 
        self.type = random.randint(0, 2)      #chọn ngẫu nhiên 1 trong 3 loại
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):                     #chim cũng kế thừa từ lớp obstacle
    def __init__(self, image):
        self.type = 0                       #có 1 loại chim nên đặt là 0
        super().__init__(image, self.type)
        self.rect.y = 200                        #tọa độ y con chim sẽ bay
        self.index = 0                     #chỉ mục để tạo hoạt ảnh

    def draw(self, SCREEN):
        if self.index >= 9:              #nếu chỉ mục lớn hơn 9 thì reset về 0
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)       #từ 0 - 4 chim dùng 1 hình , từ 5 - 9 chim dùng 1 hình
        self.index += 1                 #tăng chỉ số lên 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True  #công tắc cho vòng lặp
    clock = pygame.time.Clock()  #đồng hồ cho trò chơi
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 20           #tốc độ ban đầu 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0                #điểm ban đầu 0
    font = pygame.font.Font('freesansbold.ttf', 20)            #font cho chữ score
    obstacles = []
    death_count = 0             #số lần chết = 0

    def score():
        global points, game_speed
        points += 1               #cộng 1 point theo tg
        if points % 100 == 0:
            game_speed += 1             #mỗi 100 point thì tăng tốc gốc

        text = font.render("Points: " + str(points), True, (0, 0, 0))       #text sẽ in ra point và điểm
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)     #vẽ point lên màn hình

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()          #chiều dài image = độ dài bg
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:                 #khi bg chạy quá gần hết màn hình thì vẽ lại
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():                 #dấu X thoát trò chơi
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))        #tô màu màn hình thành màu trắng
        userInput = pygame.key.get_pressed()   #biến đầu vào người dùng

        player.draw(SCREEN)             #vẽ lên màn hình
        player.update(userInput)          #cập nhật khủng long trên mỗi vòng lặp

        if len(obstacles) == 0:                                           #tạo ngẫu nhiên 1 chim hoặc 1 xương rồng nếu độ dài của list vật cản = rỗng
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:                                  #lấy ra vật cản để vẽ và update
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):                   #câu lệnh thể hiện va chạm
                pygame.time.delay(2000)               #sau khi va chạm thì chờ 2s để hiện menu
                death_count += 1          #va chạm death +1
                menu(death_count)

        background()

        cloud.draw(SCREEN)           #vẽ mây
        cloud.update()

        score()

        clock.tick(30)       #cài đặt thời gian cho game
        pygame.display.update()    #đưa lên màn hình


def menu(death_count):
    global points            #lấy point
    run = True
    while run:
        SCREEN.fill((255, 255, 255))               #nền trắng
        font = pygame.font.Font('freesansbold.ttf', 30)     #font chữ

        if death_count == 0:        #số lần chết = 0 thì bấm để bắt đầu
            text = font.render("Press any Key to Start and Press 0-8 to choose style", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart and Press 0-8 to choose style", True, (0, 0, 0))                  #số lần chết lớn hơn 0 in bấm để chơi lại
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))  #in ra số điểm đã đạt được
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():                        #nếu bấm nút thoát thì sẽ out game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:               #bấm nút thì tiếp tục choi
                main()


menu(death_count=0)
