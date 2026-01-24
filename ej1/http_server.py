import socket
import threading
from http_parser import parse_request_line, parse_request, build_response


def get_content_type(path: str) -> str:
    pass


def handle_get(request: dict) -> bytes:
    pass


def handle_post(request: dict) -> bytes:
    pass


def handle_head(request: dict) -> bytes:
    pass


class HTTPServer:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.socket = None
    
    def start(self):
        print(f"Servidor HTTP en {self.host}:{self.port}")
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        
        while True:
            client_socket, address = self.socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            thread.start()
    
    def handle_client(self, client_socket, address):
        try:
            data = client_socket.recv(4096)
            request_text = data.decode('utf-8')
            
            # Completar
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()


if __name__ == "__main__":
    server = HTTPServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServidor detenido")
