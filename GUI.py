import tkinter as tk
from tkinter import filedialog
import pandas as pd     #CSV불러오기, 저장
from io import StringIO 

class CSVEditor:
    #생성자 master=Window객체
    def __init__(self, master) -> None:
        self.master = master
        self.master.title('CSV Editor')
        
        #CSV파일 불러오기 버튼
        self.load_button = tk.Button(self.master, text='Load CSV', command=self.load_csv)
        self.load_button.pack(pady=10)
        
        #텍스트 박스
        self.text_box = tk.Text(self.master, height=10, width=50)
        self.text_box.pack(pady=10)
        
        #저장
        self.save_button = tk.Button(self.master, text="save Changes", command=self.save_change)
        self.save_button.pack(pady=10)
        
    
    def load_csv(self):
        #파일 다이얼로그를 통해 CSV파일 선택
        file_path = filedialog.askopenfilename(filetypes=[('CSVFiles', '*.csv')])
        if file_path:
            try:
                self.df = pd.read_csv(file_path,encoding='cp949')
            except:
                self.df = pd.read_csv(file_path, encoding='utf-8')
            self.text_box.delete(0.0, tk.END)
            self.text_box.insert(tk.END, self.df.to_string(index=False))
    
    def save_change(self):
        if hasattr(self, 'df'): #hasattr로 self라는 객체가 df속성을 가졌는지 체크하는 if문 반환이 트루가 아닐 시 버튼이 반응하지 않음
            #텍스트 박스의 내용을 DataFrame으로 변환
            edited_data = self.text_box.get('0.0', tk.END)  #edited_data는 문자열 상태
            edited_df = pd.read_csv(StringIO(edited_data))  
            #StringIO -> 문자열을 파일처럼 다룰 수 있도록 하는 클래스 
            
            file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
            if file_path:
                edited_df.to_csv(file_path, index=False)
                tk.messagebox.showinfo('Success', 'Changes saved successfully')

ins = []
root = tk.Tk()

csv_editor = CSVEditor(root)
ins.append()

csv_editor.master.mainloop()


#동적 변수
#locals()[] -> 지역
#globals()[] -> 전역
# for i in range(1, 3)
# globals()['num_{}.format(i)'] = 0