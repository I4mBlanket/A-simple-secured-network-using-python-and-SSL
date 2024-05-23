import socket
import ssl

def create_secure_client():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection(('localhost', 8443)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssoc>
            ssock.sendall(b"Hello, server!")
            data = ssock.recv(1024)
            print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    create_secure_client()
