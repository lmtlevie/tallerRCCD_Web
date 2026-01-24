import pytest
import socket
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ej1'))

from websocket_frame import calculate_accept_key, parse_frame, build_frame, unmask_payload


def test_calculate_accept_key():
    key = "dGhlIHNhbXBsZSBub25jZQ=="
    expected = "s3pPLMBiTxaQ9kYGzzhZRbK+xOo="
    result = calculate_accept_key(key)
    assert result == expected


def test_unmask_payload():
    masked = b'\x7f\x9f\x4d\x51\x58'
    key = b'\x37\xfa\x21\x3d'
    unmasked = unmask_payload(masked, key)
    assert unmasked == b'Hello'


def test_build_frame():
    frame = build_frame("Hi")
    assert frame[0] == 0x81
    assert frame[1] == 2
    assert frame[2:4] == b'Hi'


def test_parse_frame_unmasked():
    frame = b'\x81\x02Hi'
    result = parse_frame(frame)
    assert result["opcode"] == 1
    assert result["payload"] == "Hi" or result["payload"] == b"Hi"


def test_parse_frame_masked():
    masking_key = b'\x00\x00\x00\x00'
    frame = b'\x81\x82' + masking_key + b'Hi'
    result = parse_frame(frame)
    assert result["opcode"] == 1


def send_websocket_handshake(port: int = 8080) -> bytes:
    sock = socket.socket()
    sock.settimeout(2.0)
    try:
        sock.connect(("127.0.0.1", port))
        handshake = b"GET / HTTP/1.1\r\nHost: localhost\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: test\r\nSec-WebSocket-Version: 13\r\n\r\n"
        sock.sendall(handshake)
        response = sock.recv(4096)
        return response
    finally:
        sock.close()


def test_server_handshake():
    # Completar
    pass


def test_server_echo():
    # Completar
    pass


if __name__ == "__main__":
    print("Tests de frames: python -m pytest test_websocket.py::test_calculate_accept_key -v")
    print("Tests de servidor: python -m pytest test_websocket.py::test_server_handshake -v")
