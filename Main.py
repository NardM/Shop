from tkinter import *
from tkinter.ttk import *
from Mac import *
from IPad import *
from IPhone import *
from Watch import *
from TV import *
from myBoolean import *
from Check import *
import re


class main:
    def __init__(self, master):
        self.master = master
        self.master.title('Магазин')
        self.master.geometry('700x270+300+200')
        #self.listBox = []
        #self.listbox = Listbox(self.master, height=10, width=70)
        #self.listbox.place(x=150, y=50)
        self.textFrom1 = Text(self.master, height=10, width=42, background='white', wrap=WORD)
        self.textFrom2 = Text(self.master, height=10, width=20, background='white', wrap=WORD)
        self.textFrom3 = Text(self.master, height=10, width=10, background='white', wrap=WORD)
        self.textFrom1.place(x=150,y=50)
        self.textFrom2.place(x=450, y=50)
        self.textFrom3.place(x=550, y=50)

        self.buttonBuy=Button(self.master, text='Чек', command=self.buy).place(x=160, y=220)

        self.Name = Label(self.master, text="Наименование").place(x=150, y=28)
        self.Price = Label(self.master, text="Цена").place(x=450, y=28)
        self.Amount = Label(self.master, text="Количество").place(x=550, y=28)

        self.Mac = Button(self.master, text="Mac", width=8, height=2, command=self.button_Mac).place(x=20, y=20)
        self.IPad = Button(self.master, text="IPad", width=8, height=2, command=self.button_IPad).place(x=20, y=60)
        self.IPhone = Button(self.master, text="IPhone", width=8, height=2, command=self.button_IPhone).place(x=20,
                                                                                                              y=100)
        self.Watch = Button(self.master, text="Watch", width=8, height=2, command=self.button_Watch).place(x=20, y=140)
        self.TV = Button(self.master, text="TV", width=8, height=2, command=self.button_TV).place(x=20, y=180)

        self.labelAmount = Label(self.master, text='ИТОГО: ').place(x=420, y=220)
        self.textPrice = Text(self.master, width=10, height=1)
        self.textPrice.place(x=480, y=220)
        self.countPrice = 0




        self.Del = Button(self.master, text="Очистить", command=self.delText).place(x=580, y=217)

        self.master.protocol('WM_DELETE_WINDOW',
                             self.exitMethod)
        self.master.mainloop()

    def buy(self):
        self.check=check(self.master,self.textFrom1.get('0.0', END),self.textFrom2.get('0.0', END),self.textFrom3.get('0.0', END), self.countPrice)

    def delText(self):
        #self.listBox.clear()
       # self.listbox.delete(0, END)
        self.textFrom1.configure(state=NORMAL)
        self.textFrom2.configure(state=NORMAL)
        self.textFrom3.configure(state=NORMAL)
        self.textFrom1.delete('0.0', END)
        self.textFrom2.delete('0.0', END)
        self.textFrom3.delete('0.0', END)
        self.textPrice.delete('0.0', END)

    def exitMethod(self):
        self.dialog = yesno(self.master)
        self.myMssg = 'Do you want to exit?'
        self.returnValue = self.dialog.go(message=self.myMssg)
        if self.returnValue:
            self.master.destroy()

    def button_Mac(self):
        self.mac = mac(self.master)
        self.textR = self.mac.go()
        if self.textR != '':
            self.correct(self.textR)

    def button_IPad(self):
        self.ipad = ipad(self.master)
        self.textR = self.ipad.go()
        if self.textR != '':
            self.correct(self.textR)

    def button_IPhone(self):
        self.iphone = iphone(self.master)
        self.textR = self.iphone.go()
        if self.textR != '':
            self.correct(self.textR)

    def button_Watch(self):
        self.watch = watch(self.master)
        self.textR = self.watch.go()
        if self.textR != '':
            self.correct(self.textR)

    def button_TV(self):
        self.tv = tv(self.master)
        self.textR = self.tv.go()
        if self.textR != '':
            self.correct(self.textR)

    def correct(self, textR):
        self.textFrom1.configure(state=NORMAL)
        self.textFrom2.configure(state=NORMAL)
        self.textFrom3.configure(state=NORMAL)
        textR = textR.replace('\n', '')
        patternPrice = re.compile(r'\((.*?)\)')
        patternCount = re.compile(r'\*(.*?)\*')
        price = str(re.findall(patternPrice, textR))
        price = price[2:len(price) - 2]+'\n'
        count = str(re.findall(patternCount, textR))
        count = count[2:len(count) - 2]+'\n'
        textR = textR[:textR.index('(')]+'\n'

        self.textFrom1.insert(END, textR)
        self.textFrom2.insert(END, price)
        self.textFrom3.insert(END, count)
        self.textFrom1.configure(state=DISABLED)
        self.textFrom2.configure(state=DISABLED)
        self.textFrom3.configure(state=DISABLED)

       # self.listBox.append(result)
       # self.listbox.insert(END, self.listBox[len(self.listBox) - 1])

        self.countPrice += int(price) * int(count)
        self.textPrice.delete('0.0', END)
        self.textPrice.insert('0.0', str(self.countPrice))


root = Tk()
main(root)
