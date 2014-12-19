from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.button = Button(self, text="Quit", fg="red", command=self.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(self, text="Hello", command= self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.pack()
    def say_hi(self):
        print("hi there, everyone!")

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
