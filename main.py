#!/usr/bin/python3
from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *

import random
from collections import deque

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0)
}

block_size = 25
bound_x = (800 / block_size)
bound_y = (800 / block_size)
class Fruit():
    def __init__(self, x=int(random.random() * bound_x), y=int(random.random() * bound_x)):
        self.pos = vec2d(x, y)

    def draw(self):
        r = pygame.Rect(self.pos * block_size, (block_size, block_size))
        pygame.draw.rect(s.screen, colors["red"], r)

    def reset(self):
        self.pos = vec2d(int(random.random() * bound_x),
                         int(random.random() * bound_y))


class Snake():
    def __init__(self, x=1, y=1, ):
        self.vel = vec2d(1, 0)
        self.body = deque()
        self.body.append(vec2d(x, y))

    def draw(self):
        for block in self.body:
            r = pygame.Rect(block * block_size, (block_size, block_size))
            pygame.draw.rect(s.screen, colors["white"], r)

    def move(self):
        new_head = (self.body[-1] + self.vel) % (bound_x)
        if new_head in self.body:
            self.reset()
            return
        self.body.append(new_head)
        self.body.popleft()

    def set_vel(self, x, y):
        self.vel.x = x
        self.vel.y = y

    def has_eaten(self, fruit):
        if self.body[-1] == fruit.pos:
            self.body.append((self.body[-1] + self.vel) % (bound_x))

            return True
        return False

    def reset(self):
        self.vel = vec2d(1, 0)
        self.body = deque()
        self.body.append(vec2d(int(random.random() * bound_x),
                         int(random.random() * bound_y)))


fruit = Fruit()
snake = Snake()


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 800
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((0, 0, 0)))
        self.fruit = ()

    def update(self):
        pass

    def keyDown(self, key):
        if key == 97 or key == 1073741904:
            snake.set_vel(-1, 0)
        if key == 115 or key == 1073741905:
            snake.set_vel(0, 1)
        if key == 100 or key == 1073741903:
            snake.set_vel(1, 0)
        if key == 119 or key == 1073741906:
            snake.set_vel(0, -1)

    def keyUp(self, key):
        pass

    def mouseUp(self, button, pos):
        pass

    def mouseMotion(self, buttons, pos, rel):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        snake.draw()
        snake.move()
        fruit.draw()
        if snake.has_eaten(fruit):
            fruit.reset()


s = Starter()
s.mainLoop(10)
