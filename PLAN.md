Objetivo Principal
Que los alumnos comprendan profundamente cómo funcionan los protocolos de comunicación en la web, implementándolos desde cero a nivel de bytes.
Objetivos Específicos
Conceptuales:

Entender la arquitectura cliente-servidor
Comprender el modelo OSI/TCP-IP (enfoque en capa de aplicación)
Diferenciar protocolos stateless (HTTP) vs stateful (WebSockets)
Entender el concepto de handshake y upgrade de protocolos
Comprender comunicación síncrona vs asíncrona

Técnicos:

Implementar parsing de protocolos de texto
Manejar sockets TCP a bajo nivel
Trabajar con protocolos binarios (WebSocket frames)
Gestionar concurrencia y múltiples conexiones
Implementar broadcasting en tiempo real

Prácticos:

Debugging de comunicación en red
Testing de servicios distribuidos
Construcción de aplicaciones cliente-servidor completas


Módulo 1: Protocolo HTTP
Objetivos del Módulo
Conceptuales:

Comprender la estructura de mensajes HTTP (request/response)
Entender el ciclo de vida de una conexión HTTP
Diferenciar métodos HTTP (GET, POST, PUT, DELETE) y sus semánticas
Comprender headers HTTP y su propósito (Content-Type, Content-Length, Host, etc.)
Entender códigos de estado HTTP y su significado (2xx, 3xx, 4xx, 5xx)
Conocer el concepto de statelessness en HTTP

Técnicos:

Implementar un parser de HTTP requests desde strings raw
Construir HTTP responses válidos manualmente
Manejar diferentes content-types (text/html, application/json, text/plain)
Implementar routing básico (mapeo de paths a handlers)
Gestionar query parameters y path parameters
Manejar el body en requests POST
Implementar servido de archivos estáticos

Prácticos:

Debuggear requests HTTP usando herramientas (curl, Postman, DevTools)
Leer y entender logs de servidor HTTP
Testear endpoints con diferentes métodos y payloads
Inspeccionar tráfico HTTP raw con tcpdump/Wireshark

Entregables del Módulo

Servidor HTTP funcional que:

Parsea requests correctamente
Responde con códigos de estado apropiados
Sirve archivos estáticos
Maneja rutas dinámicas
Soporta GET y POST


Cliente HTTP funcional que:

Construye requests válidos
Parsea responses
Maneja diferentes content-types
Implementa timeout y manejo de errores




Módulo 2: Protocolo WebSockets
Objetivos del Módulo
Conceptuales:

Comprender las limitaciones de HTTP para comunicación en tiempo real
Entender el proceso de upgrade de HTTP a WebSocket
Conocer la diferencia entre polling, long-polling y WebSockets
Comprender el concepto de conexión full-duplex
Entender qué es el framing y por qué es necesario
Conocer los diferentes tipos de frames (text, binary, ping, pong, close)

Técnicos:

Implementar el handshake de WebSocket (HTTP Upgrade)
Calcular el Sec-WebSocket-Accept header (SHA-1 + Base64)
Parsear la estructura binaria de frames WebSocket:

FIN bit, RSV bits, opcode
Mask bit y masking key
Payload length (7-bit, 16-bit, 64-bit extended)
Payload data


Implementar enmascaramiento/desenmascaramiento de payloads
Manejar fragmentación de mensajes largos
Implementar control frames (ping/pong, close handshake)
Gestionar múltiples conexiones simultáneas
Implementar broadcasting a todos los clientes conectados
Manejar desconexiones y reconexiones

Prácticos:

Debuggear handshakes WebSocket
Inspeccionar frames binarios con herramientas
Implementar heartbeat/keep-alive con ping/pong
Manejar errores de conexión y timeouts
Testing de comunicación bidireccional en tiempo real

Entregables del Módulo

Servidor WebSocket funcional que:

Acepta upgrade requests HTTP → WebSocket
Parsea y envía frames correctamente
Mantiene múltiples conexiones activas
Implementa broadcasting
Maneja ping/pong automáticamente
Cierra conexiones gracefully


Aplicación de Stock Trading en tiempo real que incluye:

Backend:

Servidor WebSocket con simulación de precios
Broadcasting de actualizaciones de precios cada N segundos
Manejo de órdenes de compra/venta
Sistema de portfolios por usuario


Frontend:

Interfaz web con gráficos de precios en tiempo real
Panel de trading (compra/venta)
Visualización de portfolio personal
Historial de transacciones
Indicadores de conexión/desconexión