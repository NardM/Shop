from tkinter import *


class tv:
    def __init__(self, master):
        self.rootTV = Toplevel()
        self.rootTV.title('TV')
        self.rootTV.geometry('500x140+300+200')

        self.var = StringVar()
        self.var.set("Apple TV Gen 3 32g (15000)")

        self.rbutton1 = Radiobutton(self.rootTV, text="Apple TV Gen 3 32g (15 000)", variable=self.var,
                                    value="Apple TV Gen 3 32g (15000)").grid(row=1, column=0)
        self.rbutton2 = Radiobutton(self.rootTV, text="Apple TV Gen 3 64g (20 000)", variable=self.var,
                                    value="Apple TV Gen 3 64g (20000)").grid(row=2, column=0)
        self.rbutton3 = Radiobutton(self.rootTV, text="Apple TV Gen 4 32g (17 000)", variable=self.var,
                                    value="Apple TV Gen 4 32g (17000)").grid(row=1, column=1)
        self.rbutton4 = Radiobutton(self.rootTV, text="Apple TV Gen 4 64g (22 999)", variable=self.var,
                                    value="Apple TV Gen 4 64g (22999)").grid(row=2, column=1)

        self.labelTVGen3 = Label(self.rootTV, text="Apple TV Gen 3", font='Arial 14').grid(row=0, column=0)
        self.labelTVGen4 = Label(self.rootTV, text="Apple TV Gen 4", font='Arial 14').grid(row=0, column=1)

        self.textCount = Text(self.rootTV, width=3, height=1)
        self.textCount.place(x=120, y=85)
        self.textCount.insert('0.0', '1')
        self.labelCount = Label(self.rootTV, text="Количество")
        self.labelCount.place(x=40, y=85)

        self.accept_button = Button(self.rootTV,
                                    text='accept',
                                    command=self.accept).place(x=170, y=80)
        self.cancel_button = Button(self.rootTV,
                                    text='cancel',
                                    command=self.cancel).place(x=220, y=80)
        self.rootTV.protocol('WM_DELETE_WINDOW', self.cancel)

    def accept(self):
        self.newValue = self.var.get() + "*" + self.textCount.get('0.0', END) + "*"
        self.rootTV.destroy()

    def cancel(self):
        self.newValue = ''
        self.rootTV.destroy()

    def go(self):
        self.rootTV.grab_set()
        self.rootTV.focus_set()
        self.rootTV.wait_window()
        return self.newValue


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    mytest = tv(root)
