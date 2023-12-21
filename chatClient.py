#TCP 방식 Socket 통신
#Wifi=TCP방식
#연결하는 꼭짓점을 Endpoint, 연결하는 망을 네트워크
#슬라이딩 윈도우 기법: 송신 측이 전송할 수 있는 데이터 양, 수신 측이 처리할 수 있는 데이터 양을 동적으로 조절
import socket
from threading import Thread
import tkinter
tk = tkinter.Tk()
tk.geometry("1000x1000")
entry = tkinter.Entry(tk)
entry2 = tkinter.Listbox(tk, height=15, width=50)
HOST = "localhost"  #IP주소
PORT = 4401

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
            entry2.insert(-1, data.decode() + "\n")
            entry2.update()
            entry2.see(0)
        except:
            pass

def runChat():
    #sock객체를 sock으로 명칭화
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # sock을 tuple 형태로 던져줌(Thread의 args는 tuple 형태로 던져주는 것을 권장함)
        t = Thread(target=rcvMsg, args=(sock,))
        # daemon thread로 설정 -> 메인 thread(tk) 종료시 자동으로 함께 종료
        t.daemon = True
        t.start()
        def okClick():
            sock.send(entry.get().encode())
        def onEnter(event):
            okClick()
            entry.delete(0, tkinter.END)
        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
        label = tkinter.Label(tk, text='채팅.')
        entry.pack()
        label.pack()
        btn = tkinter.Button(tk, text='OK', command=okClick)
        btn.pack()
        entry.bind("<Return>", onEnter)
        tk.mainloop()

runChat()
            