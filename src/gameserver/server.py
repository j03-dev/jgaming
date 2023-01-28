import threading
from const import socket, SOCKET, BUFFER_SIZE, ENCODING, LISTEN_N


class ThreadForClient(threading.Thread):
    def __init__(self, socket_client: socket, clients: list[socket]):
        threading.Thread.__init__(self)
        self.socket = socket_client
        self.clients = clients

    def run(self) -> None:
        while True:
            try:
                message = self.socket.recv(BUFFER_SIZE).decode(ENCODING)
                print(message)
                if message == "quit":
                    self.socket.close()
                    break
                else:
                    for client in self.clients:
                        client.send(message.encode(ENCODING))
            except ConnectionResetError:
                self.clients.remove(self.socket)
                break


def serve(host: str, port: int) -> None:
    addr = (host, port)
    SOCKET.bind(addr)
    SOCKET.listen(LISTEN_N)
    print(f"the server is start at: {host}:{port}")
    clients: list[socket] = []
    run = True
    while run:
        try:
            socket_client, addr = SOCKET.accept()
            print(f"{addr} is connected")
            clients.append(socket_client)
            thread_for_client = ThreadForClient(socket_client, clients)
            thread_for_client.start()
        except KeyboardInterrupt:
            run = False
    SOCKET.close()


if __name__ == "__main__":
    serve("localhost", 5555)
