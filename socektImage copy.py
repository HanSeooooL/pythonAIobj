import socket
import PIL
import tkinter as tk
from threading import Thread
from tkinter import filedialog

def send_Image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)
        
def main(image_path):
    server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_Socket.bind(("localhost", 2221))
    server_Socket.listen(1)
    print("서버 대기 중")
    connection, address = server_Socket.accept()
    print("클라이언트가 연결되었습니다.", address)
    send_Image(connection, image_path)
    connection.close()
    server_Socket.close()

def runtk():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title='이미지 파일 선택', filetypes=[('이미지 파일', '*.jpg')], initialdir='/')
    if file_path:
        t = Thread(target=main, args=(file_path,))
        t.start()

if __name__ == '__main__':
    runtk()