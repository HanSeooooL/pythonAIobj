import tkinter as tk

class ButtonApp:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Button Click Example")
        
        # Label Create
        self.label_var = tk.StringVar()
        self.label = tk.Label(self.master, textvariable=self.label_var, font=('Helvetica', 20))
        self.label.pack(pady=20)
        
        for i in range(1, 11):
            button = tk.Button(self.master, text=f"Button{i}", command=lambda buttonnumber = i: self.update_label(buttonnumber))
            button.pack(pady=5)
        
        def update_label(self):
            pass