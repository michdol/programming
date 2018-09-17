from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.master.title("Lines")
		self.pack(fill=BOTH, expand=1)
		self.canvas = Canvas(self)

		self.squares(5, 350, 15, 15)

		self.canvas.pack(fill=BOTH, expand=1)

	def squares(self, n, lg, x, y):
		if n > 0:
			self.canvas.create_line(x, y, 					x + lg, y)
			self.canvas.create_line(x + lg, y, 				x + lg, y + lg)
			self.canvas.create_line(x + lg, y + lg, 		x, y + lg) 		# third point
			self.canvas.create_line(x, y + lg, 				x, y + lg / 2) 	# half of length on left side
			self.canvas.create_line(x, y + lg / 2, 			x + lg / 2, y + lg)
			self.canvas.create_line(x + lg / 2, y + lg, 	x + lg, y + lg / 2)
			self.canvas.create_line(x + lg, y + lg / 2, 	x + lg / 2, y)
			self.canvas.create_line(x + lg / 2, y, 			x + lg / 4, y + lg / 4)
			self.squares(n - 1, lg / 2, x + lg / 4, y + lg / 4)
			self.canvas.create_line(x + lg / 4, y + lg / 4, x, y + lg / 2)
			self.canvas.create_line(x, y + lg / 2, 			x, y)


def main():
	root = Tk()
	ex = Example()
	root.geometry("720x480+300+300")
	root.mainloop()


if __name__ == '__main__':
	main()
