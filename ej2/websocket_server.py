import socket
import threading
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ej1'))

from http_parser import parse_request
from websocket_frame import calculate_accept_key, parse_frame, build_frame


class WebSocketServer:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.socket = None
    
    def start(self):
        print(f"Servidor WebSocket en ws://{self.host}:{self.port}")
        
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
            # Completar: hacer handshake y manejar mensajes
            pass
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
    
    def handle_handshake(self, client_socket) -> bool:
        # Completar
        pass
    
    def handle_messages(self, client_socket):
        # Completar
        pass


if __name__ == "__main__":
    server = WebSocketServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServidor detenido")
