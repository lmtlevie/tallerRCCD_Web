import hashlib
import base64


MAGIC_STRING = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def sha1_hash(data: str) -> bytes:
    return hashlib.sha1(data.encode()).digest()


def base64_encode(data: bytes) -> str:
    return base64.b64encode(data).decode()


def calculate_accept_key(sec_key: str) -> str:
    # Completar
    pass


def unmask_payload(masked_payload: bytes, masking_key: bytes) -> bytes:
    
    unmasked = bytearray()
    for i in range(len(masked_payload)):
        j = i % 4
        unmasked.append(masked_payload[i] ^ masking_key[j])
    return bytes(unmasked)


def parse_frame(data: bytes) -> dict:

    if len(data) < 2:
        raise ValueError("Frame demasiado corto")
    
    # Primer byte: FIN (bit 7) y opcode (bits 0-3)
    first_byte = data[0]
    opcode = first_byte & 0x0F
    
    # Segundo byte: MASK (bit 7) y payload length (bits 0-6)
    second_byte = data[1]
    masked = (second_byte & 0x80) != 0
    payload_len = second_byte & 0x7F
    
    if payload_len >= 126:
        raise ValueError("Solo se soportan payloads < 126 bytes")
    
    # Extraer masking key si está presente
    offset = 2
    masking_key = None
    if masked:
        if len(data) < offset + 4:
            raise ValueError("Frame incompleto: falta masking key")
        masking_key = data[offset:offset + 4]
        offset += 4
    
    # Extraer payload
    if len(data) < offset + payload_len:
        raise ValueError("Frame incompleto: falta payload")
    payload = data[offset:offset + payload_len]
    
    # Desenmascarar si es necesario
    if masked and masking_key:
        payload = unmask_payload(payload, masking_key)
    
    # Decodificar a string si es texto
    if opcode == 0x1:
        payload = payload.decode('utf-8')
    
    return {"opcode": opcode, "payload": payload}


def build_frame(message: str, opcode: int = 1) -> bytes:
    # Completar
    pass
