import tkinter as tk

class Calculator:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Calculator")
        self.master.geometry('350x400+100+100')
        
        self.cal = ''
        self.text = ''
        
        #Label
        self.result = tk.Label(self.master, text=self.text)
        self.result.pack(pady=10)
        
        #숫자버튼
        bu1 = tk.Button(self.master, text="1", command=lambda: self.addNumber(number=1))
        bu2 = tk.Button(self.master, text="2", command=lambda: self.addNumber(number=2))
        bu3 = tk.Button(self.master, text="3", command=lambda: self.addNumber(number=3))
        bu4 = tk.Button(self.master, text="4", command=lambda: self.addNumber(number=4))
        bu5 = tk.Button(self.master, text="5", command=lambda: self.addNumber(number=5))
        bu6 = tk.Button(self.master, text="6", command=lambda: self.addNumber(number=6))
        bu7 = tk.Button(self.master, text="7", command=lambda: self.addNumber(number=7))
        bu8 = tk.Button(self.master, text="8", command=lambda: self.addNumber(number=8))
        bu9 = tk.Button(self.master, text="9", command=lambda: self.addNumber(number=9))
        bucomma = tk.Button(self.master, text='.', command=self.addComma)
        bu1.place(x=130,y=100, width=30, height=30)
        bu2.place(x=160,y=100, width=30, height=30)
        bu3.place(x=190,y=100, width=30, height=30)
        bu4.place(x=130,y=130, width=30, height=30)
        bu5.place(x=160,y=130, width=30, height=30)
        bu6.place(x=190,y=130, width=30, height=30)
        bu7.place(x=130,y=160, width=30, height=30)
        bu8.place(x=160,y=160, width=30, height=30)
        bu9.place(x=190,y=160, width=30, height=30)
        bucomma.place(x=160,y=190, width=30, height=30)
        
        #연산버튼
        # +
        buop1 = tk.Button(self.master, text="+", command=lambda: self.operation(operation='+'))
        buop1.place(x=220, y=100, width=30, height=30)
        # -
        buop2 = tk.Button(self.master, text="-", command=lambda: self.operation(operation='-'))
        buop2.place(x=220, y=130, width=30, height=30)
        # *
        buop3 = tk.Button(self.master, text="*", command=lambda: self.operation(operation='*'))
        buop3.place(x=220, y=160, width=30, height=30)
        # /
        buop4 = tk.Button(self.master, text="/", command=lambda: self.operation(operation='/'))
        buop4.place(x=220, y=190, width=30, height=30)
        # =
        buop5 = tk.Button(self.master, text="=", command=self.calc)
        buop5.place(x=130, y=190, width=30, height=30)
    
    
    def calc(self):
        self.cal = self.cal + self.text
        self.result.config(text=str(eval(self.cal)))
        self.cal = ''
    
    def addNumber(self, number):
        self.text = (self.text + str(number))
        self.result.config(text=self.text)
    
    def addComma(self):
        self.text = self.text + '.'
        self.result.config(text=self.text)
    
    def operation(self, operation):
        self.cal = self.cal + self.text
        self.cal = self.cal + operation
        self.text=''
        self.result.config(text=self.text)
        
root = tk.Tk()

main = Calculator(root)
main.master.mainloop()


