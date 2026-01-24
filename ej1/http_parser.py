def parse_request_line(line: str) -> dict:
    # Completar
    pass


def parse_headers(header_lines: list[str]) -> dict:
    # Completar
    pass


def parse_request(raw_data: bytes) -> dict:
    # Completar
    pass


STATUS_MESSAGES = {
    200: "OK",
    201: "Created",
    404: "Not Found",
    500: "Internal Server Error",
}


def build_response(status_code: int, body: bytes, content_type: str = "text/plain") -> bytes:
    # Completar
    pass
