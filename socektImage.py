import socket
import PIL

def send_Image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)
        
def main():
    server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_Socket.bind(("localhost", 2221))
    server_Socket.listen(1)
    print("서버 대기 중")
    connection, address = server_Socket.accept()
    print("클라이언트가 연결되었습니다.", address)
    image_path = '202212008462_500.jpg'
    send_Image(connection, image_path)
    connection.close()
    server_Socket.close()

if __name__ == '__main__':
    main()