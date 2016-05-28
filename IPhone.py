from tkinter import *


class iphone:
    def __init__(self, master):
        self.rootIPhone = Toplevel()
        self.rootIPhone.title('IPhone')
        self.rootIPhone.geometry('1000x170+300+200')

        self.var = StringVar()
        self.var.set("Iphone 5s 16g (21700)")
        self.rbutton1 = Radiobutton(self.rootIPhone, text="Iphone 5s 16g (21 700)", variable=self.var,
                                    value="Iphone 5s 16g (21700)").grid(row=1, column=0)
        self.rbutton2 = Radiobutton(self.rootIPhone, text="Iphone 5s 32g (33 900)", variable=self.var,
                                    value="Iphone 5s 32g (33900)").grid(row=2, column=0)
        self.rbutton3 = Radiobutton(self.rootIPhone, text="Iphone 5s 64g (40 200)", variable=self.var,
                                    value="Iphone 5s 64g (40200)").grid(row=3, column=0)
        self.rbutton4 = Radiobutton(self.rootIPhone, text='Iphone 6 32g (33 990)', variable=self.var,
                                    value="Iphone 6 32g (33990)").grid(row=1, column=1)
        self.rbutton5 = Radiobutton(self.rootIPhone, text="Iphone 6 64g (44 000)", variable=self.var,
                                    value="Iphone 6 64g (44000)").grid(row=2, column=1)
        self.rbutton6 = Radiobutton(self.rootIPhone, text="Iphone 6 128g (59 990)", variable=self.var,
                                    value="Iphone 6 128g (59990)").grid(row=3, column=1)
        self.rbutton7 = Radiobutton(self.rootIPhone, text="Iphone 6 Plus 32g (35 000)", variable=self.var,
                                    value="Iphone 6 Plus 32g (35000)").grid(row=1, column=2)
        self.rbutton8 = Radiobutton(self.rootIPhone, text="Iphone 6 Plus 64g (49 990)", variable=self.var,
                                    value="Iphone 6 Plus 64g (49990)").grid(row=2, column=2)
        self.rbutton9 = Radiobutton(self.rootIPhone, text="Iphone 6 Plus 128g (67 000)", variable=self.var,
                                    value="Iphone 6 Plus 128g (67000)").grid(row=3, column=2)
        self.rbutton10 = Radiobutton(self.rootIPhone, text="Iphone 6s 32g (41 880)", variable=self.var,
                                     value="Iphone 6s 32g (41880)").grid(row=1, column=3)
        self.rbutton11 = Radiobutton(self.rootIPhone, text="Iphone 6s 64g (47 480)", variable=self.var,
                                     value="Iphone 6s 64g (47480)").grid(row=2, column=3)
        self.rbutton12 = Radiobutton(self.rootIPhone, text="Iphone 6s 128g (53 000)", variable=self.var,
                                     value="Iphone 6s 128g (53000)").grid(row=3, column=3)
        self.rbutton13 = Radiobutton(self.rootIPhone, text="Iphone 6s Plus 32g (57 000)", variable=self.var,
                                     value="Iphone 6s Plus (57000)").grid(row=1, column=4)
        self.rbutton14 = Radiobutton(self.rootIPhone, text="Iphone 6s Plus 64g (64 200)", variable=self.var,
                                     value="Iphone 6s Plus 64g (64200)").grid(row=2, column=4)
        self.rbutton15 = Radiobutton(self.rootIPhone, text="Iphone 6s Plus 128g (70 000)", variable=self.var,
                                     value="Iphone 6s Plus 128g (70000)").grid(row=3, column=4)
        self.rbutton16 = Radiobutton(self.rootIPhone, text="Iphone 5 SE 32g (32 400)", variable=self.var,
                                     value="Iphone 5 SE 32g (32400)").grid(row=1, column=5)
        self.rbutton17 = Radiobutton(self.rootIPhone, text="Iphone 5 SE 64g (41 000)", variable=self.var,
                                     value="Iphone 5 SE 64g (41000)").grid(row=2, column=5)
        self.rbutton18 = Radiobutton(self.rootIPhone, text="Iphone 5 SE 128g (52 900)", variable=self.var,
                                     value="Iphone 5 SE 128g (52900)").grid(row=3, column=5)

        self.labelIPhone5s = Label(self.rootIPhone, text="Iphone 5s", font='Arial 14').grid(row=0, column=0)
        self.labelIPhone6 = Label(self.rootIPhone, text="Iphone 6", font='Arial 14').grid(row=0, column=1)
        self.labelIPhone6PLUS = Label(self.rootIPhone, text="Iphone 6 PLUS", font='Arial 14').grid(row=0, column=2)
        self.labelIPhone6s = Label(self.rootIPhone, text="Iphone 6s", font='Arial 14').grid(row=0, column=3)
        self.labelIPhone6sPLUS = Label(self.rootIPhone, text="Iphone 6s PLUS", font='Arial 14').grid(row=0, column=4)
        self.labelIPhone5SE = Label(self.rootIPhone, text="Iphone 5 SE", font='Arial 14').grid(row=0, column=5)

        self.textCount = Text(self.rootIPhone, width=3, height=1)
        self.textCount.place(x=130, y=120)
        self.textCount.insert('0.0', '1')
        self.labelCount = Label(self.rootIPhone, text="Количество")
        self.labelCount.place(x=60, y=120)

        self.accept_button = Button(self.rootIPhone,
                                    text='accept',
                                    command=self.accept).place(x=300, y=115)
        self.cancel_button = Button(self.rootIPhone,
                                    text='cancel',
                                    command=self.cancel).place(x=350, y=115)
        self.rootIPhone.protocol('WM_DELETE_WINDOW', self.cancel)

    def accept(self):
        self.newValue = self.var.get() + "*" + self.textCount.get('0.0', END) + "*"
        self.rootIPhone.destroy()

    def go(self):
        self.rootIPhone.grab_set()
        self.rootIPhone.focus_set()
        self.rootIPhone.wait_window()
        return self.newValue

    def cancel(self):
        self.newValue = ''
        self.rootIPhone.destroy()


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    mytest = iphone(root)
