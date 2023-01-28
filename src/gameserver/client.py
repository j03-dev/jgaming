import threading

from const import SOCKET, BUFFER_SIZE, ENCODING


def receive_message():
    message = SOCKET.recv(BUFFER_SIZE).decode(ENCODING)
    print(message)


def connect(host: str, port: int) -> None:
    addr = (host, port)
    try:
        SOCKET.connect(addr)

        while True:
            try:
                message = input('message: ').encode(ENCODING)
                SOCKET.send(message)
                thread = threading.Thread(receive_message())
                thread.start()
            except KeyboardInterrupt:
                SOCKET.send('close'.encode(ENCODING))
                break
            except BrokenPipeError:
                print('you are disconnected')
                break

    except ConnectionRefusedError:
        print('you should run sever befor')


if __name__ == '__main__':
    connect('localhost', 5555)
