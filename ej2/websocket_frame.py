import hashlib
import base64


MAGIC_STRING = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def calculate_accept_key(sec_key: str) -> str:
    # Completar
    pass


def parse_frame(data: bytes) -> dict:
    # Completar
    pass


def build_frame(message: str, opcode: int = 1) -> bytes:
    # Completar
    pass


def unmask_payload(masked_data: bytes, masking_key: bytes) -> bytes:
    # Completar
    pass
