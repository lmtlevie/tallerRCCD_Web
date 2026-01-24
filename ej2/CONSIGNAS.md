# Ejercicio 2: Protocolo WebSocket

## Objetivo

Agregar soporte para WebSocket al servidor HTTP del Ejercicio 1, entendiendo el proceso de upgrade y la comunicación bidireccional con frames binarios.

---

## CONSIGNA 2.1

Handshake WebSocket: de HTTP a WebSocket.

### El Request de Upgrade

El archivo `handshake_example.http` muestra un ejemplo. Es un GET request HTTP con headers especiales:

- `Upgrade: websocket`
- `Connection: Upgrade`
- `Sec-WebSocket-Key` - valor aleatorio en Base64
- `Sec-WebSocket-Version: 13`

El servidor debe responder calculando `Sec-WebSocket-Accept`.

### Calcular el Accept Key

Algoritmo del RFC 6455:
1. Tomar el `Sec-WebSocket-Key` del cliente
2. Concatenarlo con `"258EAFA5-E914-47DA-95CA-C5AB0DC85B11"`
3. Calcular SHA-1 hash
4. Encodear en Base64

En `websocket_frame.py`, completá `calculate_accept_key()`. Necesitás: `hashlib.sha1()`, `.digest()`, `base64.b64encode()`.

### Implementar el Handshake

En `websocket_server.py`, el servidor ya acepta conexiones y crea threads. Tu tarea en `handle_handshake()`:

1. Recibir datos del socket
2. Parsear con `parse_request()` del ej1
3. Verificar headers: `upgrade` sea `"websocket"`, `sec-websocket-key` exista
4. Calcular accept key
5. Construir y enviar response 101:

```
HTTP/1.1 101 Switching Protocols\r\n
Upgrade: websocket\r\n
Connection: Upgrade\r\n
Sec-WebSocket-Accept: [accept key]\r\n
\r\n
```

6. Retornar `True` si exitoso

El servidor se encarga de enviar los bytes. Vos solo construís el response.

### Validar

```bash
python -m pytest test_websocket.py::test_calculate_accept_key -v
```

---

## CONSIGNA 2.2

Frames binarios.

### Estructura de Frame

```
Byte 0: FIN (bit 7) + Opcode (bits 0-3)
Byte 1: MASK (bit 7) + Length (bits 0-6)
Bytes 2-5: Masking key (si MASK=1)
Resto: Payload
```

Opcodes: `0x1` (text), `0x8` (close), `0x9` (ping), `0xA` (pong).

### Desenmascarar

Cliente → Servidor: enmascarado. Algoritmo:
```
unmasked[i] = masked[i] XOR masking_key[i % 4]
```

En `websocket_frame.py`, completá `unmask_payload()`. Usá `bytearray` y operador `^`.

### Parsear Frame

Completá `parse_frame()`. Extraer bits con operaciones bitwise:
- `data[0] & 0x80` para FIN
- `data[0] & 0x0F` para opcode
- `data[1] & 0x80` para MASK
- `data[1] & 0x7F` para length

Si MASK=1: bytes 2-5 son masking key, payload en byte 6.
Si MASK=0: payload en byte 2.

Desenmascarar si es necesario. Si opcode=1, decodificar UTF-8.

Retornar: `{"opcode": int, "payload": str o bytes}`

### Construir Frames

Servidor → Cliente: sin mask. Completá `build_frame()`:
1. Byte 0: `0x80 | opcode`
2. Byte 1: longitud
3. Payload en UTF-8

### Validar

```bash
python -m pytest test_websocket.py::test_unmask_payload -v
python -m pytest test_websocket.py::test_parse_frame_unmasked -v
```

---

## CONSIGNA 2.3

Echo server: comunicación bidireccional.

### Handle Messages

En `websocket_server.py`, completá `handle_messages()`. El servidor ya recibe datos del socket. Tu tarea:

Loop:
1. Si no hay datos: break
2. Parsear frame
3. Si opcode=1 (text):
   - Imprimir payload
   - Construir frame de respuesta
   - Enviar (el servidor ya tiene el socket)
4. Si opcode=8 (close): break

### Integrar

En `handle_client()`, el servidor ya acepta la conexión. Completá:
1. Llamar `handle_handshake()`
2. Si exitoso: llamar `handle_messages()`

El servidor cierra el socket automáticamente.

### Probar

El archivo `client.html` es un cliente JavaScript completo.

1. Iniciá: `python websocket_server.py`
2. Abrí `client.html` en browser
3. Escribí mensajes

### Validar

```bash
python -m pytest test_websocket.py -v
```

---

## Comparación

### HTTP (Ejercicio 1)
- Texto plano
- Unidireccional
- Stateless
- Alto overhead

### WebSocket (Ejercicio 2)
- Binario
- Bidireccional
- Stateful
- Bajo overhead

### Cuándo Usar

**HTTP:** request-response simple, APIs REST.

**WebSocket:** baja latencia, tiempo real, push del servidor.

## Reflexión

Implementaste dos protocolos desde cero. Entendés exactamente cómo funcionan.

El servidor maneja los sockets (crear, aceptar, recibir, enviar, cerrar). Vos implementaste el protocolo: parsear requests/frames, construir responses, manejar handshake.

No hay magia: son bytes con formato específico.

## Conceptos Clave

**Handshake:** HTTP request que "upgradea" a WebSocket (código 101).

**Accept Key:** SHA-1 + Base64 para probar que el servidor entiende WebSocket.

**Frames:** estructura binaria que empaqueta mensajes.

**Masking:** Cliente enmascara (XOR), servidor no.

**Bidireccional:** ambos pueden enviar cuando quieran.
