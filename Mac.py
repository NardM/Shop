from tkinter import *


class mac:
    def __init__(self, master):
        self.rootMac = Toplevel()
        self.rootMac.title('Mac')
        self.rootMac.geometry('950x200+300+200')
        self.var = StringVar()
        self.var.set("MacBook (129990)")

        self.rbutton1 = Radiobutton(self.rootMac, text="MacBook (129 990)", variable=self.var,
                                    value="MacBook (129990)").grid(row=0, column=0)
        self.rbutton2 = Radiobutton(self.rootMac, text="11-дюймовый MacBook Air (85 990)", variable=self.var,
                                    value="11-дюймовый MacBook Air (85990)").grid(row=0, column=1)
        self.rbutton3 = Radiobutton(self.rootMac, text='13-дюймовый MacBook Air (92 990)', variable=self.var,
                                    value='13-дюймовый MacBook Air (92990)').grid(row=0, column=2)
        self.rbutton4 = Radiobutton(self.rootMac, text='13-дюймовый MacBook Pro (106 990)', variable=self.var,
                                    value='13-дюймовый MacBook Pro (106990)').grid(row=1, column=0)
        self.rbutton5 = Radiobutton(self.rootMac, text='13-дюймовый MacBook Pro с дисплеем Retina (146 990)',
                                    variable=self.var, value='13-дюймовый MacBook Pro с дисплеем Retina (146990)').grid(
            row=1, column=1)
        self.rbutton6 = Radiobutton(self.rootMac, text='15-дюймовый MacBook Pro с дисплеем Retina (199 990)',
                                    variable=self.var, value='15-дюймовый MacBook Pro с дисплеем Retina (199990)').grid(
            row=1, column=2)
        self.rbutton7 = Radiobutton(self.rootMac, text='21,5-дюймовый iMac (106 990)', variable=self.var,
                                    value='21,5-дюймовый iMac (106990)').grid(row=2, column=0)
        self.rbutton8 = Radiobutton(self.rootMac, text='21,5-дюймовый iMac с дисплеем Retina 4K (122 990)',
                                    variable=self.var, value='21,5-дюймовый iMac с дисплеем Retina 4K (122990)').grid(
            row=2, column=1)
        self.rbutton9 = Radiobutton(self.rootMac, text='27-дюймовый iMac с дисплеем Retina 5K (189 990)',
                                    variable=self.var, value='27-дюймовый iMac с дисплеем Retina 5K (189990)').grid(
            row=2, column=2)
        self.rbutton10 = Radiobutton(self.rootMac, text='Mac mini (75 190)', variable=self.var,
                                     value='Mac mini (75190)').grid(row=3, column=0)
        self.rbutton11 = Radiobutton(self.rootMac, text='Mac Pro (329 990)', variable=self.var,
                                     value='Mac Pro (329990)').grid(row=3, column=1)

        self.textCount = Text(self.rootMac, width=3, height=1)
        self.textCount.place(x=270, y=120)
        self.textCount.insert('0.0', '1')
        self.labelCount = Label(self.rootMac, text="Количество")
        self.labelCount.place(x=200, y=120)

        self.accept_button = Button(self.rootMac,
                                    text='accept',
                                    command=self.accept).place(x=330, y=115)
        self.cancel_button = Button(self.rootMac,
                                    text='cancel',
                                    command=self.cancel).place(x=380, y=115)
        self.rootMac.protocol('WM_DELETE_WINDOW', self.cancel)

    def accept(self):
        self.newValue = self.var.get() + "*" + self.textCount.get('0.0', END) + "*"
        self.rootMac.destroy()

    def cancel(self):
        self.newValue = ''
        self.rootMac.destroy()

    def go(self):
        self.rootMac.grab_set()
        self.rootMac.focus_set()
        self.rootMac.wait_window()
        return self.newValue


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    mytest = mac(root)
