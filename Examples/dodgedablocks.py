import ConsoleEngine as CE
from random import randint

score = 0

window_width = 120
window_height = 10

CE.set_title("DOGE DA BLOCKS")
CE.set_size(window_width, window_height)

CE.start_up(5, 5)

class Blocks:
	def __init__(self): #Constructor
		self.x_positions = []
		self.y_position = 0

		self.score = 0

		self.draw_char = "#"

		self.number_of_blocks = 20

		self.fall_speed = 1

	def generate_positions(self, window_width): #Generate new x positions
		self.x_positions = []

		for i in range(self.number_of_blocks):
			self.x_positions.append(randint(1, window_width))

		self.y_position = 0

	def update(self, window_height, window_width, score): #Updating block
		self.on_ground(window_height, window_width, score)

		self.y_position += self.fall_speed

	def on_ground(self, window_height, window_width, score): #Checking if blocks are on the bottom of the screen
		self.score = score

		if (round(self.y_position) == window_height):
			self.generate_positions(window_width)
			self.score += 1

	def get_score(self):
		return self.score

	def draw(self, Player): #Draw blocks to game board
		for i in range(len(self.x_positions)):
			block = CE.Sprite([self.draw_char], self.x_positions[i], round(self.y_position))
			
			#player = CE.Sprite([Player.draw_char], Player.x, Player.y)

			if (Player.y == self.y_position):
				if (Player.x == self.x_positions[i]):
					CE.erase()
					CE.Sprite(list("GAME OVER"), 0, 0).draw()
					CE.Sprite(["SCORE:" + str(self.score)], 10, 0).draw()
					CE.render(0.1)
					input("EXIT: ")
					exit()

			block.draw()

class Player:
	def __init__(self): #Constructor
		self.directions = ["right", "left"]
		self.dir = self.directions[0]

		self.x = 5
		self.y = 9 #Start player at bottom of screen

		self.move_speed = 1

		self.draw_char = "&"

	def right(self, window_width): 
		self.dir = self.directions[0]
	
	def left(self):
		self.dir = self.directions[1]

	def update(self):
		if (self.dir == "right"):
			if (round(self.x) < window_width - 1): #Checking if player is at the edge of the screen
				self.x += 1

		else:
			if (round(self.x) > 0):
				self.x -= 1

	def draw(self): #Draw player to game board
		player = CE.Sprite([self.draw_char], self.x, self.y)
		player.draw()

Blocks = Blocks()
Blocks.generate_positions(window_width)

Player = Player()

while True:
	CE.render(0.1)
	CE.erase()

	if (CE.key_check("A")):
		Player.left()

	if (CE.key_check("D")):
		Player.right(window_width)

	Player.update()
	Player.draw()

	Blocks.update(window_height, window_width, score)
	Blocks.draw(Player)

	score = Blocks.get_score()

	CE.Sprite([str(score)], 0, 0).draw()
