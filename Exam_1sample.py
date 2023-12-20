import tkinter as tk

class CalculatorApp:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Calculator")
        #계산 결과를 나타내는 Entry
        self.result_entry = tk.Entry(self.master, font=('Helvetica', 20), justify='right')
        self.result_entry.grid(row=0,column=0,columnspan=0,pady=10)
        #버튼 생성 
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+'
        ]
        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(self.master, text=button_text, width=5, height=2, command=lambda btn=button_text: self.on_button_click(btn))
            col_val +=1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        #'='
        tk.Button(self.master, text='=', width=5, height=2, command=self.on_equals_button_click).grid(row=row_val, column=col_val, padx=5, pady=5)
        tk.Button(self.master, text='C', width=5, height=2, command=self.on_clear_button_click).grid(row=row_val, column=col_val - 1, padx=5, pady=5)
        
        
                