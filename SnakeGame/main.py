import pygame
import time
import random
SIZE = 40
class Apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load('apple.jpg')
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,38)*SIZE
        self.y = random.randint(1,20)*SIZE
        print(f"x = {self.x} , y = {self.y}")


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((1550, 820))
        self.snake = Snake(self.surface,2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.speed = 0.2

    def render_background(self):
        bg = pygame.image.load('background.jpg')
        self.surface.blit(bg,(0,0))

    def display_score(self):
        font = pygame.font.SysFont('arial',40)
        score = font.render(f"Score: {self.snake.length - 2}",True ,(255,0,255))
        self.surface.blit(score,(775,10))

    def show_game_over(self):
        self.render_background( )
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Game Over : Your Score is : {self.snake.length-2}",True,(255,255,255))
        self.surface.blit(line1,(200,350))
        line2 = font.render(f"Press Enter to Play Again or Esc to Quit", True, (255,255,255))
        self.surface.blit(line2,(200,400))
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        pygame.display.flip()
        pygame.mixer.music.pause()
        self.speed = 0.2

    def play_background_music(self):
        pygame.mixer.music.load('bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self,sound):
        sound = pygame.mixer.Sound(f"{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake collision with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
                    self.play_sound('ding')
                    self.snake.increase_length()
                    self.apple.move()
                    self.speed += 0.05
                    print(self.speed,' speed')

        # snake collision with itself
        for i in range(2,self.snake.length):
         if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
             self.play_sound('crash')
             print("collision with snake")
             raise 'Game Over'

        #snake collision with wall
        for i in range(1550//40, 820//40):
            if self.is_collision(self.snake.x[0],self.snake.y[0],i*40,i*40):
             self.play_sound('crash')
             print("collision with snake")
             raise 'Game Over'

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < (x2 + SIZE):
            if y1 >= y2 and y1 < (y2 + SIZE):
                print(f"x1:{x1},y1:{y1} x2:{x2},y2:{y2}")
                return True
        return False

    def run(self):
        run = True
        pause = False

        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

                    if event.key == pygame.K_RETURN:
                        pause = False
                        pygame.mixer.music.unpause()

                    if not pause:
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()
                        if event.key == pygame.K_UP:
                            self.snake.move_up()
                        if event.key == pygame.K_DOWN:
                            self.snake.move_down()

                elif event.type == pygame.QUIT:
                    run = False


            try:
                if not pause:
                    self.play()
            except Exception as e:
                print(e)
                self.show_game_over()
                pause = True

            time.sleep(self.speed)

class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('block.jpg')
        self.length = length
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        for i in range(self.length):
          self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'left':
            self.x[0] -= SIZE
        elif self.direction == 'right':
            self.x[0] += SIZE
        elif self.direction == 'up':
            self.y[0] -= SIZE
        elif self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
