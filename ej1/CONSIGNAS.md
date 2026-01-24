# Ejercicio 1: Protocolo HTTP

## Objetivo

Implementar un servidor HTTP básico parseando requests manualmente para entender el protocolo a nivel de bytes.

## Metodología

Para cada consigna:
1. Escribís el request HTTP en `requests/`
2. Implementás el código correspondiente
3. Probás con netcat: `cat archivo.http | nc localhost 8080`
4. Validás con tests

---

## CONSIGNA 1.1

**Archivo:** `http_parser.py`

Completá `parse_request_line()`. 

Entrada: `"GET /index.html HTTP/1.1"`
Salida: `{"method": "GET", "path": "/index.html", "version": "HTTP/1.1"}`

**Validar:**
```bash
pytest test_http.py::test_parse_request_line -v
```

---

## CONSIGNA 1.2

**Archivo:** `http_parser.py`

Completá `build_response()`. Formatea respuestas HTTP correctamente.

Recibe: status code, body (bytes), content-type.

Construye:
```
HTTP/1.1 CÓDIGO MENSAJE\r\n
Content-Type: tipo\r\n
Content-Length: tamaño\r\n
\r\n
body
```

Usar `STATUS_MESSAGES` para el mensaje del código.

**Validar:**
```bash
pytest test_http.py::test_build_response -v
```

---

## CONSIGNA 1.3

GET simple.

**Request:** Creá `requests/01_get.http` que pida `/index.html`.

Estructura:
```
MÉTODO PATH VERSIÓN
Host: valor

```

**Archivos:** `http_server.py`

Completá:
1. `handle_client()`: parsear primera línea con `parse_request_line()`, ruteo, enviar response
2. `handle_get()`: retornar response simple con `build_response(200, b"Hola!", "text/plain")`

**Probar:**
```bash
python http_server.py
cat requests/01_get.http | nc localhost 8080
```

---

## CONSIGNA 1.4

Servir archivos con Content-Type.

**Request:** Creá `requests/02_get_json.http` que pida `/users.json`.

**Archivos:** `http_server.py`

Completá:
1. `get_content_type()`: según extensión retornar Content-Type
   - `.html` → `"text/html"`
   - `.json` → `"application/json"`
   - `.css` → `"text/css"`
   - default → `"application/octet-stream"`

2. `handle_get()`: modificar para servir archivos
   - Construir filepath: `"resources" + path`
   - Abrir archivo (binario)
   - Si existe: leer, detectar tipo, usar `build_response()` con 200
   - Si no existe: `build_response()` con 404
   - Usar `try/except FileNotFoundError`

**Probar:**
```bash
cat requests/02_get_json.http | nc localhost 8080
pytest test_http.py::test_get_content_type -v
```

---

## CONSIGNA 1.5

**Archivo:** `http_parser.py`

Completá `parse_request()`. Parsear request completo incluyendo body.

Separar headers del body (línea vacía). Retornar dict con `method`, `path`, `version`, `body`.

**Validar:**
```bash
pytest test_http.py::test_parse_request_simple -v
```

---

## CONSIGNA 1.6

POST con body.

**Request:** Creá `requests/03_post.http`:
```
POST /users HTTP/1.1
Host: localhost:8080
Content-Length: [calcular bytes]

{"name": "Charlie"}
```

**Archivos:** `http_server.py`

Completá:
1. `handle_client()`: actualizar para usar `parse_request()` completo
2. `handle_post()`: procesar body, retornar `build_response(201, b"Created", "text/plain")`
3. Ruteo: llamar a `handle_post()` cuando método sea POST

**Probar:**
```bash
cat requests/03_post.http | nc localhost 8080
pytest test_http.py::test_parse_request_with_body -v
```

---

## CONSIGNA 1.7

HEAD sin body en response.

**Request:** Creá `requests/04_head.http` igual a GET pero método HEAD.

**Archivos:** `http_server.py`

Completá:
1. `handle_head()`: construir response con headers (incluyendo Content-Length) pero sin body
2. Ruteo: llamar a `handle_head()` cuando método sea HEAD

**Probar:**
```bash
cat requests/04_head.http | nc localhost 8080
```

---

## CONSIGNA 1.8

Headers completos.

**Request:** Creá `requests/05_headers.http` con múltiples headers (Host, User-Agent, Accept, Connection).

**Archivos:** `http_parser.py`

Completá:
1. `parse_headers()`: lista de strings → dict. Separar por `': '`
2. `parse_request()`: modificar para incluir headers en dict retornado

**Probar:**
```bash
cat requests/05_headers.http | nc localhost 8080
pytest test_http.py::test_parse_headers -v
```

---

## CONSIGNA 1.9

Error 404.

**Request:** Creá `requests/06_not_found.http` pidiendo `/noexiste.html`.

**Verificar:** El `try/except FileNotFoundError` de la consigna 1.4 ya maneja 404.

**Probar:**
```bash
cat requests/06_not_found.http | nc localhost 8080
pytest test_http.py::test_not_found -v
```

---

## Validación Final

```bash
pytest test_http.py -v
```

## Estructura del Código

**`http_parser.py`:**
- `parse_request_line()`: primera línea → dict
- `parse_headers()`: lista headers → dict
- `parse_request()`: bytes completos → dict
- `build_response()`: crear response formateado (usar siempre)

**`http_server.py`:**
- `get_content_type()`: extensión → Content-Type
- `handle_get()`: lógica GET
- `handle_post()`: lógica POST
- `handle_head()`: lógica HEAD
- `handle_client()`: ruteo + enviar response

## Conceptos

**Request:**
```
Método Path Versión
Headers
[línea vacía]
Body
```

**Response:**
```
Versión Código Mensaje
Headers
[línea vacía]
Body
```

**Separador:** `\r\n` entre líneas, `\r\n\r\n` entre headers y body.

**Métodos:** GET (obtener), POST (enviar), HEAD (metadata).

**Códigos:** 200 (OK), 201 (Created), 404 (Not Found).
