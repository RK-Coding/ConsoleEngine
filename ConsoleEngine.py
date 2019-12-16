import os
import time as t
import keyboard
import winsound

title = 'ConsoleGame'
b_color = 'black'
height = 0
width = 0
board = []
lines = []
color = '2'

def set_size(width_, height_):
    global board
    global lines
    global height
    global width

    for i in range(height_):
        board.append([])

    for i in range(len(board)):
        for n in range(width_):
            board[i].append(' ')

    for i in range(height_):
            lines.append('')

    height = height_
    width = width_

def set_draw_color(color_):
    global color

    color = color_

def set_title(string):
    global title

    title = string

def start_up(marginX, marginY):
    global height
    global width

    global color
    global title

    cmd = 'mode' + ' ' + str(width + marginX) + ',' + str(height + marginY)
    os.system(cmd)

    cmd = 'color' + ' ' + color
    os.system(cmd)

    cmd = 'title' + ' ' + title
    os.system(cmd)

def apply_changes(marginX, marginY):
    global height
    global width

    global color
    global title

    cmd = 'mode' + ' ' + str(width + marginX) + ',' + str(height + marginY)
    os.system(cmd)

    cmd = 'color' + ' ' + color
    os.system(cmd)

    cmd = 'title' + ' ' + title
    os.system(cmd)

def render(delay, colous_to_clear = True):
    t.sleep(delay)

    if (colous_to_clear):
        cmd = 'colous 0 0 1,1'
        os.system(cmd)

    else:
        cmd = 'cls'
        os.system(cmd)

    global board
    global lines

    for i in range(len(board)):
        temp = ''
        for n in range(len(board[i])):
            temp += board[i][n]

        lines[i] = temp

    for i in range(len(lines)):
        print(lines[i])

def erase():
    global board

    for i in range(len(board)):
        for n in range(len(board[i])):
            board[i][n] = ' '

def play_sound(wav_file):
	winsound.PlaySound(wav_file, winsound.SND_FILENAME|winsound.SND_NOWAIT)

def key_check(key_):
    try:
        if keyboard.is_pressed(key_):
            return True

        else:
            return False

    except:
        pass

class Sprite:
    def __init__(self, strings, x, y):
        self.x = x
        self.y = y
        self.strings = strings
        self.positions = []

    def draw(self):
        global board

        x_target = 0
        y_target = 0

        for i in range(len(board)):
            for n in range(len(board[i])):
                if (n == self.x and i == self.y):
                    x_target = n
                    y_target = i

        temp = 0
        temp2 = 0

        self.positions = []

        for i in range(len(self.strings)):
            temp2 = 0
            for l in range(len(self.strings[i])):
                board[y_target + temp][x_target + temp2] = self.strings[i][l]
                self.positions.append([y_target + temp, x_target + temp2])
                temp2 += 1
            temp += 1

    def right(self, unit, frame = True):
        global width

        inFrame = True

        for i in range(len(self.positions)):
            if (self.positions[i][1] == width - 1):
                inFrame = False

        if (inFrame):
            self.x += unit

    def left(self, unit):
        if (self.x != 0):
            self.x -= unit

    def down(self, unit):
        global height

        if (self.y != height - 1):
            self.y += unit

    def up(self, unit):
        if (self.y != 0):
            self.y -= unit

    def check_collision(self, otherSprite):
        collison = False

        for i in range(len(otherSprite.positions)):
            if otherSprite.positions[i] in self.positions:
                collison = True

        return collison
