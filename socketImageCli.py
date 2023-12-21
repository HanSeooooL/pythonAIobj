import socket
from PIL import Image
from io import BytesIO

def receive_image(connection, save_path):
    with open(save_path, 'wb') as image_file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            image_file.write(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect(("localhost", 2221))
    save_path = 'recive.jpg'
    receive_image(client_socket, save_path)
    print("이미지를 성공적으로 수신하였습니다.")
    with open(save_path, 'rb') as file:
        image_data = file.read()
    binaryToobj = BytesIO(image_data)
    imgForshow = Image.open(binaryToobj)
    imgForshow.show()
    client_socket.close()

if __name__ == '__main__':
    main()
    