from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.master.title("Lines")
		self.pack(fill=BOTH, expand=1)
		self.canvas = Canvas(self)

		self.spiral1(15, 15, 200, 10, True)
		self.spiral(15, 15, 200, 10)
		self.book_spiral(15, 15, 200, 10)

		self.canvas.pack(fill=BOTH, expand=1)

	def spiral1(self, x1, y1, lg, dlg, first):
		"""

		:param x1: starting point x
		:param y1: starting point y
		:param lg: length of the line to draw
		:param dlg: length difference, next function call length will be shorter by dlg
		:param first: used to make correct turns while drawing line.
		first = True means from starting point go to the right until new point
		then turn "right" and go down
		first = False means from starting point go to the left until new point
		then turn "right" and go up
		"""
		if lg <= dlg:
			return

		x2 = x1 + lg if first else x1 - lg
		self.canvas.create_line(x1, y1, x2, y1)
		last_y = y1 + lg if first else y1 - lg
		self.canvas.create_line(x2, y1, x2, last_y)
		self.spiral1(x2, last_y, lg - dlg, dlg, not first)

	def spiral(self, x1, y1, lg, dlg):
		if lg <= dlg:
			return

		self.canvas.create_line(x1, y1, x1 + lg, y1)	# y1 = y2
		x2 = x1 + lg
		y3 = y1 + lg
		self.canvas.create_line(x2, y1, x2, y3)		# x2 = x3

		new_lg = lg - dlg
		x4 = x2 - new_lg
		self.canvas.create_line(x2, y3, x4, y3)		# y3 = y4

		y5 = y3 - new_lg
		self.canvas.create_line(x4, y3, x4, y5)
		self.spiral(x4, y5, new_lg - dlg, dlg)

	def book_spiral(self, x, y, lg, dlg):
		if lg <= dlg:
			return
		self.canvas.create_line(x, y, 				x + lg, y)
		self.canvas.create_line(x + lg, y,  		x + lg, y + lg)
		self.canvas.create_line(x + lg, y + lg,  	x + dlg, y + lg)
		self.canvas.create_line(x + dlg, y + lg,  	x + dlg, y + dlg)

		self.book_spiral(x + dlg, y + dlg, lg - 2 * dlg, dlg)


def main():
	root = Tk()
	ex = Example()
	root.geometry("720x480+300+300")
	root.mainloop()


if __name__ == '__main__':
	main()
