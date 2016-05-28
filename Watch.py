from tkinter import *


class watch:
    def __init__(self, master):
        self.rootWatch = Toplevel()
        self.rootWatch.title('Watch')
        self.rootWatch.geometry('350x120+300+200')

        self.var = StringVar()
        self.var.set("Watch 38mm (38000)")

        self.rbutton1 = Radiobutton(self.rootWatch, text="Watch 38mm (38 000)", variable=self.var,
                                    value="Watch 38mm (38000)").grid(row=1, column=0)
        self.rbutton2 = Radiobutton(self.rootWatch, text="Watch 42mm (40 000)", variable=self.var,
                                    value="Watch 42mm (40000)").grid(row=1, column=1)

        self.labelWatch38mm = Label(self.rootWatch, text="Watch 38mm", font='Arial 14').grid(row=0, column=0)
        self.labelWatch42mm = Label(self.rootWatch, text="Watch 42mm", font='Arial 14').grid(row=0, column=1)

        self.textCount = Text(self.rootWatch, width=3, height=1)
        self.textCount.place(x=100, y=70)
        self.textCount.insert('0.0', '1')
        self.labelCount = Label(self.rootWatch, text="Количество")
        self.labelCount.place(x=30, y=70)

        self.accept_button = Button(self.rootWatch,
                                    text='accept',
                                    command=self.accept).place(x=150, y=65)
        self.cancel_button = Button(self.rootWatch,
                                    text='cancel',
                                    command=self.cancel).place(x=200, y=65)
        self.rootWatch.protocol('WM_DELETE_WINDOW', self.cancel)

    def accept(self):
        self.newValue = self.var.get() + "*" + self.textCount.get('0.0', END) + "*"
        self.rootWatch.destroy()

    def cancel(self):
        self.newValue = ''
        self.rootWatch.destroy()

    def go(self):
        self.rootWatch.grab_set()
        self.rootWatch.focus_set()
        self.rootWatch.wait_window()
        return self.newValue


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    mytest = watch(root)
