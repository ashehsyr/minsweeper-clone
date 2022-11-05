import random as r


class Board(): #Create a grid object based on input dimensions
	def __init__(self, width, height, bombs):
		self.wd = width
		self.ht = height
		self.grid = [[0 for x in range(width)] for x in range(height)]
		self.bombs = bombs

	
class Bomb(): #create bomb object
	def __init__(self, board):
		self.name = 'X'
		#create random coordinates when bomb object is initialized
		self.x = r.randint(0, board.wd-1)
		self.y = r.randint(0, board.ht-1)


def increment_tile(board, tile_y, tile_x):
	#increment the tile at the coordinates pass in
	if tile_y in range(board.ht) and tile_x in range(board.wd):
		try:
			board.grid[tile_y][tile_x] += 1
		except (IndexError, TypeError):
			pass


def increment_surrounding(board, y , x):
	#target every tile within 1 of the targeted coordinate
	increment_tile(board, y + 1,x + 1)
	increment_tile(board, y - 1,x - 1)
	increment_tile(board, y + 1, x - 1)
	increment_tile(board, y - 1,x + 1)
	increment_tile(board, y + 1, x)
	increment_tile(board, y - 1, x)
	increment_tile(board, y, x + 1)
	increment_tile(board, y, x - 1)


def populate_board(board):
	i = board.bombs
	while i != 0:
		#create new bombs based on bomb value in board object
		new_bomb = Bomb(board)

		#add bombs to the grid
		if board.grid[new_bomb.y][new_bomb.x] != new_bomb.name:
			board.grid[new_bomb.y][new_bomb.x] = new_bomb.name	
			increment_surrounding(board, new_bomb.y, new_bomb.x)
			i -= 1								
	return board
