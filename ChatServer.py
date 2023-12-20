import socketserver
import threading
HOST = 'localhost'   # 서버가 구동될 IP
PORT = 4400 # 포트번호
lock = threading.Lock()

class UserManager:
    def __init__(self) -> None:
        self.users = {} 
    
    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send("이미 등록된 사용자입니다. \n".encode())
            return None
    
        lock.acquire()
        self.users[username] = (conn, addr)
        lock.release()
        self.sendMessagetoAll('[%s]님이 입장했습니다' % username)
        return username
    
    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessagetoAll('[%s]님이 퇴장했습니다' % username)
        print('대화 참여자 수 [%d]' % len(self.users))
        
    def messageHandler(self, username, msg):
        if msg[0] != '/':
            self.sendMessagetoAll('[%s] %s' %(username, msg))
            return
        
        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1
    
    def sendMessagetoAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()
    def handle(self):
        print(self, "self memory")
        print('client [%s] 연결' % self.client_address[0])
        try:
            username = self.registerUsername()
            print(username, " username")
            msg = self.request.recv(1024)
            print(self.request)
            print(self.client_address)
            print(self.server)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)
        print('[%s] 접속 종료' % self.client_address[0])
        self.userman.removeUser(username)
        
    def registerUsername(self):
        while True:
            self.request.send('ID'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username

# ThreadingMixIn과 TCPServer를 상속받은 클래스 선언
class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():
    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('채팅 서버를 종료합니다.')
        server.shutdown()
        server.server_close()
        
runServer()
        