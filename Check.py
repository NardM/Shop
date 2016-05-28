from tkinter import *
import datetime
import random


class check:
    def __init__(self, master, textFrom1, textFrom2, textFrom3, countPrice):
        self.rootCheck = Toplevel()
        self.rootCheck.title('Оплата')
        self.rootCheck.geometry('700x270+300+200')
        self.textFrom1 = Text(self.rootCheck, height=10, width=42, background='white', wrap=WORD)
        self.textFrom2 = Text(self.rootCheck, height=10, width=20, background='white', wrap=WORD)
        self.textFrom3 = Text(self.rootCheck, height=10, width=10, background='white', wrap=WORD)
        self.textFrom1.place(x=150, y=50)
        self.textFrom2.place(x=450, y=50)
        self.textFrom3.place(x=550, y=50)

        self.Name = Label(self.rootCheck, text="Наименование").place(x=150, y=28)
        self.Price = Label(self.rootCheck, text="Цена").place(x=450, y=28)
        self.Amount = Label(self.rootCheck, text="Количество").place(x=550, y=28)

        self.labelAmount = Label(self.rootCheck, text='ИТОГО: ').place(x=420, y=220)
        self.textPrice = Text(self.rootCheck, width=10, height=1)
        self.textPrice.place(x=480, y=220)
        self.textPrice.delete('0.0', END)
        self.textPrice.insert('0.0', str(countPrice))

        self.textFrom1.configure(state=NORMAL)
        self.textFrom2.configure(state=NORMAL)
        self.textFrom3.configure(state=NORMAL)
        self.textFrom1.insert(END, textFrom1)
        self.textFrom2.insert(END, textFrom2)
        self.textFrom3.insert(END, textFrom3)
        self.textFrom1.configure(state=DISABLED)
        self.textFrom2.configure(state=DISABLED)
        self.textFrom3.configure(state=DISABLED)

        self.result = datetime.datetime.now()
        self.result = self.result.strftime("%d-%m-%Y %H:%M")
        self.result1 = str(random.randint(1, 100))
        self.labelData = Label(self.rootCheck, text="Номер заказа: " + self.result1 + " от " + self.result).place(x=150,
                                                                                                                  y=7)


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    mytest = check(root)
