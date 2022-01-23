from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app= Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound',loop=False,autoplay=False)

window.fps_counter.enable = False # tắt thông báo FPS
window.exit_button.visible = False # ẩn nút exit

block_pick=1 # gán mặc định cho block_pick = 1

def update():
    global block_pick # Khai báo biến Block_pick trong hàm là biến toàn cục
    if held_keys['left mouse'] or held_keys['right mouse']: # Lắng nghe sự kiện người chơi click chuột phaiar hoặc chuột trái

        hand.active() # gọi hàm active() trong lớp hand
    else:  
        hand.passive() #gọi hàm passive() trong lớp hand

    if held_keys['1']: block_pick=1 # nếu người chơi bấm phím 1 thì gán block_pick=1
    if held_keys['2']: block_pick=2 # nếu người chơi bấm phím 1 thì gán block_pick=2
    if held_keys['3']: block_pick=3 # nếu người chơi bấm phím 1 thì gán block_pick=3
    if held_keys['4']: block_pick=4 # nếu người chơi bấm phím 1 thì gán block_pick=4


class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent= scene, 
            position = position,
            model = 'assets/block.obj',
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            origin_y=0.5,
            scale = 0.5
        )
    def input(self,key):
        if self.hovered: # nếu con con trỏ chuột trỏ vào Voxel
            if key == 'left mouse down': # nếu bắt được sự kiện click chuột trái sẽ tạo ra các voxel với vị trí và texture tương ứng với từng câu lệnh if
                punch_sound.play() # âm thanh game được phát
                #block_pick được hiểu là index của các text_ture được người chơi nhập vào để thay đổi các texture của voxel
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal,texture = grass_texture) #nếu block_pick = 1 texture = grass_texture  
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal,texture = stone_texture) #nếu block_pick = 2 texture = stone_texture
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal,texture = brick_texture) #nếu block_pick = 3 texture = brick_texture
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal,texture = dirt_texture) #nếu block_pick = 4 texture = dirt_texture
            if key == 'right mouse down': # nếu băt được sự kiện click chuột phải
                punch_sound.play() # âm thanh game được phát
                destroy(self) # Voxel được con trỏ chuột trỏ đến sẽ bị phá hủy


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene, 
            model = 'sphere', #cài đặt model của sky là 1 hình cầu 
            texture = sky_texture, #truyền texture từ biến đã gán
            scale = 150, # cài đặt độ lớn = 150
            double_sided = True #vì texture ta truyền vào là 1 file png nên khi texture bao quanh ta sẽ chỉ nhìn thấy mặt sau,nên ở đây ta sẽ cần cài đặt thuộc tính Double_sided = True (2 mặt)
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui, # Sử dụng không gian giao diện người dùng
            model = 'assets/arm', #cài đặt model arm từ thư mục assets
            texture = arm_texture, # Truyền texture từ biến đã gán
            scale = 0.2, # cài đặt độ lớn
            rotation = Vec3(150,-10,0), # xoay cánh tay sao cho phù hợp với không gian 3 chiều
            position = Vec2(0.4,-0.6) # cài đặt vị trí của cánh tay
        )
    def active(self): # cánh tay ở vị trí hoạt động
        self.position = Vec2(0.4,-0.5) # cài đặt vị trí khi cánh tay hoạt động
    
    def passive(self): # cánh tay ở vị trí khi không hoạt động
        self.position = Vec2(0.4,-0.6) # cài đặt vị trí khi cánh tay không hoạt động


for x in range(60):
    for z in range(60):
        voxel = Voxel(position= (x,0,z))  
player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()