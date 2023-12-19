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

#Entry
#실행함수 -> Event Handler
def calc(event):
    #entry.get() -> 입력한 문자열을 읽어오는 것
    label.config(text='결과='+str(eval(entry.get())))
    
def printtexts(event):
    label.config(text='입력값='+str(entry.get()))

#생성
entry=tk.Entry(window)
#entry.bind(키설정, 실행함수) -> Event Listener
entry.bind("<Return>", calc)
entry.pack()
label=tk.Label(window)
label.pack()

#Listbox
listbox = tk.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "2번")
listbox.insert(3, "2번")
listbox.insert(4, "3번")
listbox.pack()

#Element Delete
listbox.delete(1, 2)

#listboxSize 반환함수
print(listbox.size())
    
#checkBox
def flash():
    checkbutton1.flash()
    checkVariety_2.set(1)
    checkbutton1.config(text=checkVariety_2.get())

def deselect():
    checkbutton1.deselect()
    checkbutton2.deselect()
    checkbutton3.deselect()

#checkVariety -> 체크됐는지 안됐는지 체크하는 변수
#IntVar -> 2개의 값(1, 0)만 존재. True(1) or False(0)
checkVariety_1=tk.IntVar()
checkVariety_2=tk.IntVar()
checkVariety_3=tk.IntVar()

#버튼 생성
checkbutton1=tk.Checkbutton(window, text='O',variable=checkVariety_1,activebackground='blue')
checkbutton2=tk.Checkbutton(window, text='?', variable=checkVariety_2, command=deselect)
checkbutton3=tk.Checkbutton(window, text='X', variable=checkVariety_3, command=flash)
checkbutton1.pack(side='left', padx=10)
checkbutton2.pack(side='left')
checkbutton3.pack(side='left')
window.mainloop()


