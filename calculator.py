from math import sqrt
from tkinter import *
from tkmacosx import Button


class TinyCalculatorApp:
    def __init__(self, master):
        master.title("Tiny Calculator")
        master.configure(bg='light gray')
        master.geometry("240x150")
        self.exp = self.num = ''
        self.calcScreen = Label(master, bd=5, wraplength=40, textvariable=self.exp,
                                bg='white', font=("Arial Bold", 16), relief='sunken')
        self.calcScreen.grid(row=0, column=1, columnspan=2, sticky='ew')

        # row 4 buttons
        self.bt1 = Button(master, text='1', height=20, width=60, borderless=1,
                          command=lambda: self.click('1'))
        self.bt1.grid(column=0, row=4)
        self.bt2 = Button(master, text='2', height=20, width=60,
                          borderless=1, command=lambda: self.click('2'))
        self.bt2.grid(column=1, row=4)
        self.bt3 = Button(master, text='3', height=20, width=60,
                          borderless=1, command=lambda: self.click('3'))
        self.bt3.grid(column=2, row=4)

        # row 3 buttons
        self.bt4 = Button(master, text='4', height=20, width=60,
                          borderless=1, command=lambda: self.click('4'))
        self.bt4.grid(column=0, row=3)
        self.bt5 = Button(master, text='5', height=20, width=60,
                          borderless=1, command=lambda: self.click('5'))
        self.bt5.grid(column=1, row=3)
        self.bt6 = Button(master, text='6', height=20, width=60,
                          borderless=1, command=lambda: self.click('6'))
        self.bt6.grid(column=2, row=3)

        # row 2 buttons
        self.bt7 = Button(master, text='7', height=20, width=60,
                          borderless=1, command=lambda: self.click('7'))
        self.bt7.grid(column=0, row=2)
        self.bt8 = Button(master, text='8', height=20, width=60,
                          borderless=1, command=lambda: self.click('8'))
        self.bt8.grid(column=1, row=2)
        self.bt9 = Button(master, text='9', height=20, width=60,
                          borderless=1, command=lambda: self.click('9'))
        self.bt9.grid(column=2, row=2)

        # row 5 buttons
        self.btc = Button(master, text='on/c', height=20, width=60,
                          bg='red', fg='white', borderless=1, command=lambda: self.click('c'))
        self.btc.grid(column=0, row=5)
        self.bt0 = Button(master, text='0', height=20, width=60,
                          borderless=1, command=lambda: self.click('0'))
        self.bt0.grid(column=1, row=5)
        self.btdec = Button(master, text='.', height=20, width=60,
                            borderless=1, command=lambda: self.click('.'))
        self.btdec.grid(column=2, row=5)

        # operation buttons
        self.btneg = Button(master, text='+/-', height=20, width=60,
                            bg='red', fg='white', borderless=1, command=lambda: self.click("+/-"))
        self.btneg.grid(column=0, row=1)
        self.btplus = Button(master, text='+', height=20, width=60,
                             bg='red', fg='white', borderless=1, command=lambda: self.click('+'))
        self.btplus.grid(column=3, row=4)
        self.btminus = Button(master, text='-', height=20, width=60,
                              bg='red', fg='white', borderless=1, command=lambda: self.click('-'))
        self.btminus.grid(column=3, row=3)
        self.bttimes = Button(master, text='*', height=20, width=60,
                              bg='red', fg='white', borderless=1, command=lambda: self.click('*'))
        self.bttimes.grid(column=3, row=2)
        self.btdiv = Button(master, text='/', height=20, width=60,
                            bg='red', fg='white', borderless=1, command=lambda: self.click('/'))
        self.btdiv.grid(column=3, row=1)
        self.btmod = Button(master, text='%', height=20, width=60,
                            bg="red", fg='white', borderless=1, command=lambda: self.click('%'))
        self.btmod.grid(column=2, row=1)
        self.btequals = Button(master, text='=', height=20, width=60,
                               bg='red', fg='white', borderless=1, command=lambda: self.click('='))
        self.btequals.grid(column=3, row=5)
        self.btsqrt = Button(master, text='sqrt', height=20, width=60,
                             bg='red', fg='white', borderless=1, command=lambda: self.click('sqrt'))
        self.btsqrt.grid(column=1, row=1)

    def click(self, val):
        if val == 'c':
            self.exp = self.num = ''
            self.calcScreen.configure(text=self.exp)
        elif val == '=':
            self.exp += self.num
            self.calcScreen.configure(text=eval(self.exp))
            self.num = str(eval(self.exp))
            self.exp = ''
        elif val == 'sqrt':
            sqrt_num = sqrt(float(self.num))
            self.num = str(sqrt_num)
        elif val == '+/-':
            self.exp += '-'
        else:
            self.num += val
            if not val.isdigit():
                self.exp += self.num
                self.num = ''
            self.calcScreen.configure(text=self.num)


window = Tk()
obj = TinyCalculatorApp(window)
window.mainloop()
