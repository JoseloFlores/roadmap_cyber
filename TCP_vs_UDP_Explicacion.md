# ¿Qué protocolo es mejor? TCP vs. UDP: descubre cuándo usar cada uno

*Por Sergio De Luz*

TCP y UDP son dos protocolos fundamentales para las comunicaciones a través de Internet. Ambos se sitúan en la **capa de transporte** del modelo TCP/IP, siendo la primera capa donde el origen y el destino se comunican directamente (las capas inferiores, red y acceso al medio, no realizan esta función). 

El tráfico de red se compone de un gran número de transferencias de datos entre dispositivos y servidores que utilizan estos dos protocolos para transmitir la información.

---

## Tabla comparativa: TCP vs. UDP

| Característica | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Orientación** | Orientado a conexión (requiere *3-way handshake*) | Sin conexión (envío directo) |
| **Fiabilidad** | Alta (entrega ordenada y sin errores) | Baja (sin garantía de entrega ni orden) |
| **Velocidad** | Más lento (debido a la sobrecarga de control) | Más rápido (mínima sobrecarga) |
| **Control de Flujo** | Sí (evita saturar al receptor) | No |
| **Control de Congestión** | Sí (algoritmos como BBRv2/Cubic) | No |
| **Tamaño de Cabecera** | 20 bytes (mínimo) | 8 bytes (fijo) |
| **Casos de Uso Típicos** | Web (HTTP/S), Email (SMTP/POP3), Archivos (FTP/SFTP), SSH | Streaming de vídeo/audio, VoIP, videojuegos online, DNS, DHCP |

---

## Protocolo TCP: ¿qué es y cómo funciona?

El **protocolo TCP (Protocolo de Control de Transmisión)** es un protocolo orientado a conexión que permite a las aplicaciones comunicarse con garantías, independientemente de las capas inferiores del modelo TCP/IP. 

Soporta múltiples protocolos de la capa de aplicación como HTTP, HTTPS, POP3, SMTP, FTP, SFTP y SSH.

### Principales características
* **Retransmisión de datos e integridad:** Si un segmento se corrompe o se pierde, TCP inicia su retransmisión automáticamente sin intervención de la capa de aplicación.
* **Tamaño Máximo de Segmento (MSS):** Es el tamaño máximo en bytes que TCP puede recibir en un solo segmento. Se calcula restando la cabecera TCP (mínimo 20 bytes) e IP (mínimo 20 bytes) al MTU:
  $$	ext{MSS} = 	ext{MTU (1500 bytes)} - 20	ext{ bytes (TCP)} - 20	ext{ bytes (IP)} = 1460	ext{ bytes}$$
* **Control de errores (Ventana Deslizante):**
  * *Checksum* para detección de errores.
  * Numeración de segmentos para mantener el control.
  * Confirmaciones ACK selectivas o acumulativas.
  * Temporizadores de retransmisión.
  * Descarte automático de segmentos duplicados.
* **Garantía de orden:** Si un segmento llega desordenado, TCP lo retiene hasta recibir el segmento faltante o solicita su retransmisión.
* **Control de flujo:** Ajusta la velocidad de transmisión según la capacidad del receptor mediante la ventana de recepción.
* **Control de congestión:** Previene la pérdida de paquetes en routers saturados gestionando la ventana de congestión en tres fases: *Arranque lento (Slow Start)*, *Evitación de congestión* y *Fase constante*. Utiliza algoritmos como TCP BBR, CUBIC, Tahoe, Reno o Vegas.
* **Multiplexado y Full-Dúplex:** Permite recibir datos de múltiples *hosts* en paralelo y transmitir/recibir simultáneamente por el mismo canal.

### Establecimiento y cierre de conexión
1. **Establecimiento (*3-Way Handshake*):**
   * **Cliente $ightarrow$ Servidor:** Envío de paquete `SYN`.
   * **Servidor $ightarrow$ Cliente:** Respuesta con `SYN-ACK`.
   * **Cliente $ightarrow$ Servidor:** Confirmación con `ACK`.
2. **Cierre de conexión:** El host que desea terminar envía un `FIN`, el receptor responde con `ACK` + `FIN`, y el iniciador confirma con un último `ACK`.

### Cabecera de TCP (Mínimo 20 bytes)
Incluye:
* Puerto de origen y puerto de destino (sockets).
* Número de secuencia y número de ACK.
* *Flags* (SYN, ACK, RST, FIN, URG, etc.).
* Campo de 16 bits para el tamaño de la ventana de recepción.

---

## Protocolo UDP: ¿qué es y cómo funciona?

El **protocolo UDP (Protocolo de Datagramas de Usuario)** es un protocolo **no orientado a conexión** y no fiable. Los datagramas se envían directamente al destino sin un aviso o negociación previa.

Se utiliza principalmente en aplicaciones como DNS, DHCP, VoIP, streaming y juegos en línea, donde la velocidad y la baja latencia son preferibles a la fiabilidad absoluta.

### Principales características
* **Sin control de flujo ni congestión:** No limita la velocidad de envío ni gestiona la saturación de la red.
* **Sin garantía de entrega u orden:** No retransmite paquetes perdidos ni garantiza el orden de llegada. La gestión de errores o pérdidas debe implementarse en la capa de aplicación.
* **Cabecera reducida (8 bytes):** Contiene únicamente los puertos de origen y destino, la longitud del datagrama y el *checksum*.
* **Baja latencia:** Al carecer de negociación inicial (*handshake*), ofrece un rendimiento extremadamente rápido y ágil.

---

## TCP vs. UDP en VPN, Web y Aplicaciones

### Protocolos VPN
* **OpenVPN:** Permite operar tanto en TCP como en UDP. Se recomienda **UDP** por mayor velocidad y eficiencia. Si se pierden paquetes, las capas superiores dentro del túnel (como HTTP en TCP) se encargan de retransmitirlos. Además, UDP soporta un mayor número de conexiones simultáneas en el servidor.
* **WireGuard:** Utiliza exclusivamente **UDP**. Esto permite un rendimiento superior y soporte nativo para *roaming VPN* (cambio ágil entre Wi-Fi y redes móviles sin perder la sesión).

### La Web: HTTP/1.1, HTTP/2 y HTTP/3
* **HTTP/1.1 y HTTP/2:** Operan sobre **TCP** (puertos 80 para HTTP y 443 para HTTPS con TLS).
* **HTTP/3:** Utiliza el protocolo **QUIC**, el cual funciona sobre **UDP**. Integra cifrado TLS 1.2/1.3 de forma obligatoria y elimina los problemas de bloqueo de cabeza de línea (*Head-of-Line Blocking*) de TCP.

### Videoconferencias y Juegos Online
Las aplicaciones en tiempo real (como videoconferencias o videojuegos multijugador) priorizan UDP. Un paquete perdido en una llamada de voz o juego es irrelevante medio segundo después, por lo que retransmitirlo mediante TCP solo añadiría latencia y retrasos en la comunicación.

---

## Vulnerabilidades y Seguridad en TCP/IP

* **Ataques SYN Flood (DoS):** Inundación de peticiones `SYN` para agotar los recursos de conexiones pendientes del servidor. Mitigaciones:
  * Limitación de conexiones por IP o globales.
  * Uso de *SYN Cookies* y *SYN Cache*.
  * Filtrado de IP y firewall.
* **Predicción de Secuencia TCP:** El atacante deduce los números de secuencia TCP de un host para inyectar paquetes falsificados o cerrar conexiones legítimas.
* **Manipulación de Puertos y Spoofing:** Intercepción o alteración de datos (*Man-in-the-Middle*), falsificación de direcciones/puertos de origen (*Spoofing*), redirección de puertos (*Port Forwarding*) y encapsulamiento (*Tunneling*).

---

## Otros protocolos de la Capa de Transporte

* **SCTP (Stream Control Transmission Protocol):** Combina características de TCP y UDP. Soporta múltiples flujos de datos (*multistreaming*) y multihoming. Usado en telefonía IP y VoIP.
* **DCCP (Datagram Congestion Control Protocol):** Funciona como UDP pero añade mecanismos de control de congestión.
* **RDP (Reliable Data Protocol):** Diseñado para aplicaciones militares y científicas que requieren confiabilidad sin la complejidad de TCP.
* **QUIC:** Base de HTTP/3, aporta multiplexación, cifrado integrado y menor latencia sobre UDP.

> **¿Por qué dominan TCP y UDP?**
> Fueron los primeros en adoptarse universalmente en los inicios de Internet. Aunque existen alternativas avanzadas, cambiar la infraestructura global de red y resolver incompatibilidades con *firewalls* existentes representa un alto costo operativo.
