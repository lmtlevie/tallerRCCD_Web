from typing import List

def parse_request_line(line: str) -> dict:
    # Completar
    pass


def parse_headers(header_lines: List[str]) -> dict:
    # Completar
    pass


def parse_request(lines: List[str]) -> dict:
    # Completar
    pass

STATUS_MESSAGES = {
    200: "OK",
    201: "Created",
    404: "Not Found",
    500: "Internal Server Error",
}

def build_response(
    status_code: int,
    body: bytes,
    headers: dict = None
) -> bytes:
    VERSION = "HTTP/1.1"
    # Completar



