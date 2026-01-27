import socket
import threading
import sys
sys.path.append('../ej1')
from http_parser import parse_request
from websocket_frame import calculate_accept_key, parse_frame, build_frame


def handle_handshake(client_socket):
    # Completar
    pass


def handle_messages(client_socket):
    # Completar
    pass


class WebSocketServer:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.socket = None
    
    def start(self):
        print(f"Servidor WebSocket en {self.host}:{self.port}")
        
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
            if handle_handshake(client_socket):
                handle_messages(client_socket)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()


if __name__ == "__main__":
    server = WebSocketServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServidor detenido")
