import ConsoleEngine as CE
import random as r

screenWidth = 120
screenHeight = 30

CE.set_title('Snake')
CE.set_size(screenWidth, screenHeight)

class Food:
    def __init__(self):
        self.pos = [0, 0]
        self.drawChar = '#'
        self.sprite = CE.Sprite([self.drawChar], self.pos[0], self.pos[1])

    def pickPos(self):
        self.pos[0] = r.randint(0, screenWidth)
        self.pos[1] = r.randint(0, screenHeight)

        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]

    def drawFood(self):
        self.sprite.draw()

class Snake:
    def __init__(self):
        self.pos = [0, 0]
        self.length = 5
        self.drawChar = '*'
        self.prevPositions = []
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] #DOWN, UP, RIGHT, LEFT
        self.dir = self.directions[0]

    def move(self):
        temp = self.pos[:]
        self.prevPositions.insert(0, temp)

        if (len(self.prevPositions) > self.length):
            del(self.prevPositions[len(self.prevPositions) - 1])

        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]

    def drawSnake(self):
        for i in range(len(self.prevPositions)):
            temp = CE.Sprite([self.drawChar], self.prevPositions[i][0], self.prevPositions[i][1])
            temp.draw()

    def check(self, food):
        if (food.pos in self.prevPositions):
            self.length += 1
            food.pickPos()

        for i in range(len(self.prevPositions)):
            if i != 0:
                if self.pos == self.prevPositions[i]:
                    # CE.erase()
                    # temp = CE.Sprite(['Game Over'], 0, 0)
                    # temp.draw()
                    # CE.render(0)
                    # CE.render(1)
                    # #t.sleep(1)
                    # self.length = 5
                    # self.pos = [0, 0]
                    # #self.prevPositions = []
                    # self.dir = self.directions[0]
                    # food.pickPos()
                    exit()



food = Food()
food.pickPos()
snake = Snake()

CE.start_up(5, 5)
while True:
    if (CE.key_check("w")):
        snake.dir = snake.directions[1]

    if (CE.key_check("s")):
        snake.dir = snake.directions[0]

    if (CE.key_check("d")):
        snake.dir = snake.directions[2]

    if (CE.key_check("a")):
        snake.dir = snake.directions[3]

    CE.render(0.01)
    CE.erase()
    snake.move()
    snake.check(food)
    snake.drawSnake()
    food.drawFood()
