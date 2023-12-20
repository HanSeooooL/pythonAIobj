import socket
from threading import Thread
import tkinter
tk = tkinter.Tk()
tk.geometry("1000x1000")
entry = tkinter.Entry(tk)
entry2 = tkinter.Listbox(tk, height=15, width=50)
HOST = "192.168.214.51"  #IP주소
PORT = 9900

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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
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
            