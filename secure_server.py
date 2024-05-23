import socket
import ssl

def create_secure_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='/data/data/com.termux/files/home/pyth>

    bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bindsocket.bind(('localhost', 8443))
    bindsocket.listen(5)

    while True:
        newsocket, fromaddr = bindsocket.accept()
        connstream = context.wrap_socket(newsocket, server_side=True)
        try:
            handle_client(connstream)
        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()

def handle_client(connstream):
    data = connstream.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
    connstream.sendall(b"Hello, client!")

if __name__ == "__main__":
    create_secure_server()
