import PyQt5.QtWidgets as qtw
import main

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Minesweeper Clone")
		form_layout = qtw.QFormLayout()
		self.setLayout(form_layout)
		error_message = qtw.QErrorMessage()

		width_input = qtw.QLineEdit(self)
		height_input = qtw.QLineEdit(self)	
		bombs_input = qtw.QLineEdit(self)

		form_layout.addRow("Width", width_input)
		form_layout.addRow("Height", height_input)
		form_layout.addRow("Bombs", bombs_input)
		form_layout.addRow(qtw.QPushButton("Generate",
			clicked = lambda: generate_board()))

		self.show()

		def generate_board():
			try:
				width = int(width_input.text())
				height = int(height_input.text())
				bombs = int(bombs_input.text())
				if bombs > width * height:
					error_message.showMessage('Too Many Bombs!')
				else:
					main.draw_board(main.Board(width, height, bombs))
			except ValueError:
				error_message.showMessage('Invalid Input')


if __name__ == '__main__':
	app = qtw.QApplication([])

mw = MainWindow()
mw.show()
app.exec_()