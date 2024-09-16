import pgzrun

from random import randint

TITLE = "Flappy Ball"

WIDTH = 800
HEIGHT = 600

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)

CLR = R,G,B

GRAVITY = 2000.00

class Ball:
    def __init__(self, initial_x, initial_y, color, rad):

        self.x = initial_x
        self.y = initial_y
        self.vx = 300
        self.vy= 0
        self.radius = rad
        self.color = color

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)
    


ball = Ball(50, 100, "green", randint(5, 100))
ball1 = Ball(100, 100, "red",randint(5, 100))
ball2 = Ball(200,  100, "blue", randint(5, 100))

def update(dt):
    uy = ball.vy
    fy = ball.vy

    ball.vy += GRAVITY * dt 
    ball.y += (uy + ball.vy) * dt * 0.5

    if ball.y > 600- ball.radius:
        ball.y = 600- ball.radius
        ball.vy = ball.vy * -0.9
    ball.x += ball.vx * dt
    if ball.x > 800- ball.radius or  ball.x < 0 + ball.radius:
        ball.vx = ball.vx * -1

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500



def draw():
    screen.clear()
    ball.draw()
    ball1.draw()
    ball2.draw()

pgzrun.go()