import tkinter as tk

#tkinter 객체 생성
window = tk.Tk()
#창 제목 설정
window.title('app')
#창 크기
window.geometry('640x400+100+100')
#창 크기 변경 가능여부
window.resizable(False, False)
#Label: 창에 띄워지는 글씨, 주석문
label=tk.Label(window, text='ocr', width=10, height=5, fg='red', relief='solid')
label.pack()

#Countup Button
#사용될 변수
count = 0
#버튼에 사용될 함수
def countUP():
    global count
    count += 1
    #label.config -> 생성된 label의 설정 변경
    label.config(text=str(count))

#버튼에 출력될 텍스트
label=tk.Label(window, text='0')
label.pack()
button=tk.Button(window, overrelief='solid', width=15, command=countUP, repeatdelay=1000,
                 repeatinterval=100)
button.pack()

window.mainloop()

