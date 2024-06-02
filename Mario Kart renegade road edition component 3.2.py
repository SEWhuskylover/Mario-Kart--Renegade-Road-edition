# importing the pygame program
import pygame
import random

# Initialize Pygame
pygame.init()

# colors that are going to be used in the program, set with rgb
GREEN = (100, 250, 140)
DARKGREY = (70, 70, 70)
WHITE = (250, 250, 250)


# class for ai cars that will come down the screen
class EnemyCar:
    def __init__(self, lane, img, ai_speed):
        # there is random.radint here to help stop cars overlapping and make the game feel less simulated
        self.y = -200 + random.randint(-200, 100)
        self.lane = lane
        self.img = img
        self.speed = ai_speed

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(self.img, [self.lane, self.y])

    # function for ai cars that have gone off the screen to come back to the top
    def respawn(self):
        # there is random.radint here to help stop cars overlapping and make the game feel less simulated
        self.y = -200 + random.randint(-200, 100)
        self.lane = random.choice(ai_lane)
        # this is to make sure that cars cannot spawn in lanes that are already occupied
        occupied_lanes = [car.lane for car in ai_car_list if car != self]
        while self.lane in occupied_lanes:
            self.lane = random.choice(ai_lane)
        self.img = random.choice(ai_car_imgs)
        self.speed = 1.5 + random.random()


# frames per second that the game will run in
fps = 200
clock = pygame.time.Clock()

# creating the display
display_width = 700
display_height = 900
screen = pygame.display.set_mode((display_width, display_height))
# naming the display
pygame.display.set_caption('Mario Kart: Renegade Road Edition')


# for making the road lines
line_marker_move_y = 0
# defines line width
line_width = 10
# defines line height
line_height = 50


# main game loop
# sets the speed the game is going to run at
speed = 2

# road lane places (variables to define where the diffirent lanes are)
lane_1 = 110
lane_2 = 210
lane_3 = 310
lane_4 = 410
lane_5 = 510

# player car variables
player_x = lane_3  # sets the players X co-ordinate to start in the third lane
player_y = 700  # sets the players Y co-ordinate
car_coords = [player_x, player_y]
current_lane = 3  # the lane the player car is currently in

# ai car variables
ai_lane = [lane_1, lane_2, lane_3, lane_4, lane_5]
ai_car_imgs = [pygame.transform.smoothscale(pygame.image.load(
    car), [90, 150]) for car in ("car_cyan.png", "car_purple.png", "car_green.png")]
ai_car_y = -150
ai_car_width = 90
ai_car_height = 150


def create_car_list():
    car_list = []
    for i in range(4):
        next_lane = random.choice(ai_lane)
        img = random.choice(ai_car_imgs)
        occupied_lanes = [car.lane for car in car_list]
        while next_lane in occupied_lanes:
            next_lane = random.choice(ai_lane)
        # car_list.append(EnemyCar(next_lane, img, 1.75 + random.random()/4))
        car_list.append(EnemyCar(next_lane, img, 1.5 + random.random()))
    return car_list


def ai_cars():
    for car in ai_car_list:
        car.move()
        car.draw()


# exiting variable allows game loop to run and allows game to close when exiting = true
exiting = False
spawn_lane = lane_1
ai_car_list = create_car_list()
while not exiting:
    # sets the fps
    clock.tick(fps)

    for event in pygame.event.get():
        # allows the player to quit by pressing esc
        if event.type == pygame.QUIT:
            exiting = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exiting = True
            # if the player inputs the left arrow the current lane will decrease unless the current lane is already 1
            if event.key == pygame.K_a and current_lane >= 2:
                current_lane -= 1
            # if the player inputs the right arrow the current lane will increase unless the current lane is already 5
            if event.key == pygame.K_d and current_lane <= 4:
                current_lane += 1

    # changes the color of the screen to green
    screen.fill(GREEN)
    # creating a rectangle to be the road, road position = 700 - 500(road width) = 200/2 = 100 on each side
    pygame.draw.rect(screen, DARKGREY, [100, 1, 500, 900])

    # creating road lines
    line_marker_move_y += speed * 2
    if line_marker_move_y >= line_height * 2:
        line_marker_move_y = 0
    for y in range(line_height * -2, display_height, line_height * 2):
        pygame.draw.rect(
            screen, WHITE, (200, y + line_marker_move_y, line_width, line_height))
        pygame.draw.rect(
            screen, WHITE, (300, y + line_marker_move_y, line_width, line_height))
        pygame.draw.rect(
            screen, WHITE, (400, y + line_marker_move_y, line_width, line_height))
        pygame.draw.rect(
            screen, WHITE, (500, y + line_marker_move_y, line_width, line_height))

    # creating the player car
    player_car = pygame.image.load("car_1.png")
    player_car = pygame.transform.scale(player_car, (90, 150))
    screen.blit(player_car, car_coords)

    # car movement
    # will set the cars position to the lane set by the current lane variable
    if current_lane == 1:
        player_x = lane_1
    if current_lane == 2:
        player_x = lane_2
    if current_lane == 3:
        player_x = lane_3
    if current_lane == 4:
        player_x = lane_4
    if current_lane == 5:
        player_x = lane_5
    car_coords = [player_x, player_y]
    # creating the ai cars
    for car in ai_car_list:
        if car.y > 950:
            car.respawn()

    ai_cars()

    # updating the display so that changes will show up
    pygame.display.update()

# exits the program
pygame.quit()
