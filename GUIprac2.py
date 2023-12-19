import tkinter as tk

#tkinter 객체 생성
window = tk.Tk()
#창 제목 설정
window.title('app')
#창 크기
window.geometry('640x400+100+100')
#창 크기 변경 가능여부
window.resizable(False, False)

b1=tk.Button(window, text='(50, 50)')
b2=tk.Button(window, text='(50, 100)')
b3=tk.Button(window, text='(100, 150)')
b4=tk.Button(window, text='(0, 200)')
b5=tk.Button(window, text='(0, 300)')
b6=tk.Button(window, text='(0, 300)')
b1.place(x=50, y=50)
b2.place(x=50, y=100, width=50, height=50)
b3.place(x=100, y=150, bordermode='inside')
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx=0.5)
b6.place(x=0, y=300,relx=0.5, anchor='s')

window.mainloop()
