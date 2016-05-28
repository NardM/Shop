from tkinter import *


class ipad:
    def __init__(self, master):
        self.rootIPad = Toplevel()
        self.rootIPad.title('IPad')
        self.rootIPad.geometry('800x250+300+200')
        self.var = StringVar()
        self.var.set("iPad mini 2 16Gb Wi-Fi (18899)")

        self.rbutton1 = Radiobutton(self.rootIPad, text="iPad mini 2 16Gb Wi-Fi (18 899)", variable=self.var,
                                    value="iPad mini 2 16Gb Wi-Fi (18899)").grid(row=1, column=0)
        self.rbutton2 = Radiobutton(self.rootIPad, text="iPad mini 2 16Gb Wi-Fi + Cellular (24 999)", variable=self.var,
                                    value="iPad mini 2 16Gb Wi-Fi + Cellular (24 99)").grid(row=2, column=0)
        self.rbutton3 = Radiobutton(self.rootIPad, text="iPad mini 2 32Gb Wi-Fi (22 000)", variable=self.var,
                                    value="iPad mini 2 32Gb Wi-Fi (22000)").grid(row=3, column=0)
        self.rbutton4 = Radiobutton(self.rootIPad, text="iPad mini 2 32Gb Wi-Fi + Cellular (28 000)", variable=self.var,
                                    value="iPad mini 2 32Gb Wi-Fi + Cellular (28000)").grid(row=4, column=0)
        self.rbutton5 = Radiobutton(self.rootIPad, text="iPad mini 4 16Gb Wi-Fi (21 000)", variable=self.var,
                                    value="iPad mini 4 16Gb Wi-Fi (21000)").grid(row=1, column=1)
        self.rbutton6 = Radiobutton(self.rootIPad, text="iPad mini 4 16Gb Wi-Fi + Cellular (23 700)", variable=self.var,
                                    value="iPad mini 4 16Gb Wi-Fi + Cellular (23700)").grid(row=2, column=1)
        self.rbutton7 = Radiobutton(self.rootIPad, text="iPad mini 4 64Gb Wi-Fi (27 000)", variable=self.var,
                                    value="iPad mini 4 64Gb Wi-Fi (27000)").grid(row=3, column=1)
        self.rbutton8 = Radiobutton(self.rootIPad, text="iPad mini 4 64Gb Wi-Fi + Cellular (33 000)", variable=self.var,
                                    value="iPad mini 4 64Gb Wi-Fi + Cellular (33000)").grid(row=4, column=1)
        self.rbutton9 = Radiobutton(self.rootIPad, text="iPad mini 4 128Gb Wi-Fi (25 000)", variable=self.var,
                                    value="iPad mini 4 128Gb Wi-Fi (25000)").grid(row=5, column=1)
        self.rbutton10 = Radiobutton(self.rootIPad, text="iPad mini 4 128Gb Wi-Fi + Cellular (38 000)",
                                     variable=self.var, value="iPad mini 4 128Gb Wi-Fi + Cellular (38000)").grid(row=6,
                                                                                                                 column=1)
        self.rbutton11 = Radiobutton(self.rootIPad, text="iPad Air 2 16Gb Wi-Fi (27 000)", variable=self.var,
                                     value="iPad Air 2 16Gb Wi-Fi (27000)").grid(row=1, column=2)
        self.rbutton12 = Radiobutton(self.rootIPad, text="iPad Air 2 16Gb Wi-Fi + Cellular (34 000)", variable=self.var,
                                     value="iPad Air 2 16Gb Wi-Fi + Cellular (34000)").grid(row=2, column=2)
        self.rbutton13 = Radiobutton(self.rootIPad, text="iPad Air 2 64Gb Wi-Fi (35 000)", variable=self.var,
                                     value="iPad Air 2 64Gb Wi-Fi (35000)").grid(row=3, column=2)
        self.rbutton14 = Radiobutton(self.rootIPad, text="iPad Air 2 64Gb Wi-Fi + Cellular (43 000)", variable=self.var,
                                     value="iPad Air 2 64Gb Wi-Fi + Cellular (43000)").grid(row=4, column=2)
        self.rbutton15 = Radiobutton(self.rootIPad, text="iPad Air 2 128Gb Wi-Fi (55 000)", variable=self.var,
                                     value="iPad Air 2 128Gb Wi-Fi (55000)").grid(row=5, column=2)
        self.rbutton16 = Radiobutton(self.rootIPad, text="iPad Air 2 128Gb Wi-Fi + Cellular (67 000)",
                                     variable=self.var, value="iPad Air 2 128Gb Wi-Fi + Cellular (67000)").grid(row=6,
                                                                                                                column=2)

        self.labelIPadMini2 = Label(self.rootIPad, text="iPad mini 2", font='Arial 14').grid(row=0, column=0)
        self.labeIPadMini4 = Label(self.rootIPad, text="iPad mini 4", font='Arial 14').grid(row=0, column=1)
        self.labelIPadAir2 = Label(self.rootIPad, text="iPad Air 2", font='Arial 14').grid(row=0, column=2)

        self.textCount = Text(self.rootIPad, width=3, height=1)
        self.textCount.place(x=130, y=200)
        self.textCount.insert('0.0', '1')
        self.labelCount = Label(self.rootIPad, text="Количество")
        self.labelCount.place(x=60, y=200)

        self.accept_button = Button(self.rootIPad, text='accept',
                                    command=self.accept).place(x=300, y=200)
        self.cancel_button = Button(self.rootIPad,
                                    text='cancel',
                                    command=self.cancel).place(x=350, y=200)
        self.rootIPad.protocol('WM_DELETE_WINDOW', self.cancel)

    def accept(self):
        self.newValue = self.var.get() + "*" + self.textCount.get('0.0', END) + "*"
        self.rootIPad.destroy()

    def cancel(self):
        self.newValue = ''
        self.rootIPad.destroy()

    def go(self):
        self.rootIPad.grab_set()
        self.rootIPad.focus_set()
        self.rootIPad.wait_window()
        return self.newValue


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    mytest = ipad(root)
