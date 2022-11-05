import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import main

class PushButton(qtw.QPushButton):
	def __init__(self, text, board, parent=None): 
		#need to make widget a child of a window or will 
		#generate a new window every instance class is called
		super(PushButton, self).__init__(text, parent)

		self.inner_text = text
		self.setText('')		
		self.setFixedSize(qtc.QSize(50, 50))
		self.setFont(qtg.QFont('Helvetica', 18))

		self.clicked.connect(lambda: self.reveal_button(board))

		self.show()
	

	def reveal_button(self, board):
		self.setEnabled(False)
		self.setText(self.inner_text)
		
		if self.inner_text == 'X':
			self.setStyleSheet("background-color: red;")
			BoardWindow.lose_msg()
		elif self.inner_text != '0':
			self.setStyleSheet("color: blue;")

		PushButton.revealed += 1
		self.check_win(board)		


	def check_win(self, board):
		if self.revealed == board.wd * board.ht - board.bombs:
			msg = qtw.QMessageBox()
			msg.setText("You Win!")
			msg.exec_()			
		
	revealed = 0
   	

class BoardWindow(qtw.QWidget):
	def __init__(self, board):
		super().__init__()
		self.setWindowTitle("Minesweeper Clone")		
		self.layout = qtw.QGridLayout(self)


		for x, row in enumerate(board.grid): #iterates the list of lists generated in main.py
			print(row)
			for y, column in enumerate(row):
				square = PushButton(str(column), board, self)
				self.layout.addWidget(square, x, y)


	def lose_msg():
		msg = qtw.QMessageBox()
		msg.setText("You Lose!")
		msg.exec_()



class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Minesweeper Clone")
		form_layout = qtw.QFormLayout()
		self.setLayout(form_layout)
		self.error_message = qtw.QErrorMessage()

		self.width_input = qtw.QLineEdit(self)
		self.height_input = qtw.QLineEdit(self)	
		self.bombs_input = qtw.QLineEdit(self)

		form_layout.addRow("Width", self.width_input)
		form_layout.addRow("Height", self.height_input)
		form_layout.addRow("Bombs", self.bombs_input)
		form_layout.addRow(qtw.QPushButton("Generate",
			clicked = lambda: self.generate_board()))

		self.show()

	
	def generate_board(self):
		try: #checks for correct inputs/ error handles
			width = int(self.width_input.text())
			height = int(self.height_input.text())
			bombs = int(self.bombs_input.text())
			if bombs > width * height:
				self.error_message.showMessage('Too Many Bombs!')
			else:
				self.board = main.populate_board(main.Board(width, height, bombs)) #initializing board instance
				self.show_board(self.board)
		except ValueError:
			self.error_message.showMessage('Invalid Input')


	def show_board(self, board): #creates new window with minesweeper board
		self.new_board_window = BoardWindow(board)
		self.new_board_window.show()


if __name__ == '__main__':
	import sys
	app = qtw.QApplication([])
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec_())