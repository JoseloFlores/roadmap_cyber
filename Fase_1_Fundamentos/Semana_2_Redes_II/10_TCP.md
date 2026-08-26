**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Módulo 10 – TCP (Transmission Control Protocol)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ IP Públicas y Privadas

- ✅ Modelo OSI

- ✅ Modelo TCP/IP

- ✅ Máscaras

- ✅ Subredes

- ✅ Gateway

- ✅ NAT

- ✅ UDP

- ✅ Puertos

Ahora estudiaremos al protocolo más importante que verás en un SOC: **TCP**.

En el módulo de UDP aprendiste que existe un protocolo rápido pero poco confiable.

TCP es su "hermano", pero con una filosofía totalmente opuesta: es **orientado a conexión** y **confiable**.

Es la base de la web, del correo electrónico y de la administración remota.

Prácticamente todos los logs que revisarás en tu trabajo diario contendrán conexiones TCP.

Comprenderlo a fondo es esencial para interpretar capturas, firewall, SIEM y ataques como **SYN Flood** o los **escaneos de puertos**.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es TCP y por qué existe.

- Explicar el Three-Way Handshake paso a paso.

- Diferenciar los flags de TCP (SYN, ACK, FIN, RST, PSH, URG).

- Entender qué garantías ofrece TCP y cuáles no.

- Conocer los protocolos que utilizan TCP.

- Reconocer TCP en Wireshark, firewall y SIEM.

- Identificar ataques contra TCP como SYN Flood y escaneos.

- Relacionar TCP con el movimiento lateral y la fuerza bruta.

- Aplicar estos conocimientos en investigaciones de un SOC.

- Responder preguntas técnicas de una entrevista para Analista SOC Nivel 1.

**1. ¿Qué es TCP?**

TCP significa **Transmission Control Protocol** (Protocolo de Control de Transmisión).

Es un protocolo de la **Capa 4 (Transporte)** del modelo OSI, igual que UDP.

Su filosofía es completamente diferente a la de UDP.

Mientras UDP dice "voy a enviarlo lo más rápido posible", TCP dice "voy a asegurarme de que todo llegue completo, en orden y sin errores".

**La diferencia en una frase**

**TCP:** La confiabilidad es lo más importante.

**UDP:** La velocidad es lo más importante.

Para lograr esa confiabilidad, TCP necesita algo que UDP no tiene: una **conexión establecida** entre los dos equipos.

Por eso se dice que TCP es un protocolo **orientado a conexión**.

**2. ¿Por qué existe TCP?**

Imagina que estás haciendo una transferencia bancaria, descargando el respaldo de toda una empresa o enviando un correo importante.

¿Quieres perder parte de esos datos en el camino? Claro que no.

Cuando la información **no puede perderse**, necesitas TCP.

**Ejemplos de aplicaciones que necesitan TCP**

- Navegación web (HTTP y HTTPS).

- Correo electrónico (SMTP, POP3, IMAP).

- Transferencia de archivos (FTP).

- Acceso remoto (SSH y RDP).

- Bases de datos (SQL Server, MySQL, PostgreSQL).

Todas estas aplicaciones usan TCP porque no pueden permitirse perder información.

**Analogía**

UDP sería una conversación telefónica: si una palabra no se escucha, nadie detiene la conversación.

TCP sería enviar un contrato por **correo certificado**: si falta una hoja la vuelven a enviar, si llega desordenada la reacomodan, y al final el destinatario firma un acuse de recibo.

Ese acuse de recibo, en TCP, se llama **ACK**.

**3. El Three-Way Handshake**

Antes de enviar datos, TCP debe establecer una conexión.

Ese proceso se llama **Three-Way Handshake** (saludo de tres vías) y tiene tres pasos:

1. Cliente envía **SYN**.

2. Servidor responde con **SYN-ACK**.

3. Cliente confirma con **ACK**.

Visualmente:

Cliente

↓

SYN

↓

Servidor

↓

SYN-ACK

↓

Cliente

↓

ACK

↓

Servidor

↓

Datos

**Paso 1 – SYN**

El cliente dice: "¿Estás ahí? Quiero hablar contigo."

**Paso 2 – SYN-ACK**

El servidor responde: "Sí, estoy aquí y también quiero hablar contigo."

**Paso 3 – ACK**

El cliente confirma: "Perfecto, la comunicación quedó establecida."

Desde ese momento pueden fluir los datos.

**Analogía del restaurante**

Llamas a un restaurante para reservar una mesa: "¿Está abierto?" (SYN).

El restaurante responde: "Sí, ¿desea reservar?" (SYN-ACK).

Tú confirmas: "Sí, quiero reservar." (ACK).

A partir de ahí empiezas a pedir la comida (los datos).

**¿Por qué esto importa en un SOC?**

Porque verás este saludo en cada captura de red, y porque los atacantes abusan de él.

Si alguien envía miles de **SYN** sin completar el saludo, tienes un posible **SYN Flood**.

**4. ¿Qué NO garantiza TCP?**

Es importante ser honesto: TCP es muy confiable, pero no es mágico.

**TCP NO:**

❌ Cifra la información.

❌ Oculta quién se comunica con quién.

❌ Protege contra ataques a las aplicaciones.

❌ Impide que un atacante intercepte o modifique el tráfico.

TCP garantiza la **entrega correcta**, pero no la **seguridad**.

Los datos viajan en texto plano por la red; la confidencialidad la aporta otro protocolo: **TLS (Transport Layer Security)**, el cifrado que usa HTTPS.

Es como el empleado del banco que revisa que el dinero llegue completo y en orden, pero si nadie sella el sobre, cualquiera en el camino podría abrirlo; ese sello es TLS.

Por eso verás siempre: HTTP + TCP → texto plano, y HTTPS + TCP + TLS → cifrado.

En un SOC, puedes ver los metadatos de la conexión (qué IP, qué puerto, cuándo); para ver el contenido cifrado necesitas otras herramientas o la decodificación del tráfico.

**5. Cierre de conexión**

Cuando la comunicación termina, la conexión debe cerrarse.

El cierre tiene su propio proceso en cuatro pasos:

1. Un equipo envía **FIN**: "ya terminé de enviar datos."

2. El otro responde **ACK**: "acepto que terminaste."

3. El otro equipo también envía **FIN**: "yo también terminé."

4. El primero responde **ACK**: "perfecto, conexión cerrada."

Visualmente:

Cliente → FIN → Servidor → ACK → Servidor → FIN → Cliente → ACK → Conexión cerrada

Esto se conoce como **Four-Way Handshake**.

**¿Por qué importa verlo en capturas?**

Una conexión que nunca se cierra puede significar: un programa colgado, malware manteniendo un canal con su servidor, un equipo apagado de golpe o un corte de red.

En Wireshark observarás los flags FIN, FIN-ACK y ACK.

Si la conexión termina de forma brusca, verás un **RST**.

**RST significa Reset**, es la "interrupción violenta" de una conexión; TCP la usa cuando algo sale mal.

**6. Cabecera TCP y flags**

Cada paquete TCP tiene una **cabecera** con información importante.

El analista no memoriza todo el campo, pero sí lo esencial.

**Campos más importantes de la cabecera TCP**

| **Campo**               | **Qué indica**                                                    |
|-------------------------|-------------------------------------------------------------------|
| Puerto origen           | Puerto del equipo que envía.                                      |
| Puerto destino          | Puerto del servicio al que se dirige.                             |
| Número de secuencia     | Posición del dato dentro del flujo.                               |
| Número de confirmación  | Confirma qué datos ya recibió el otro extremo.                    |
| Flags                   | Controlan el estado de la conexión (SYN, ACK, FIN, RST, etc.).    |
| Window (ventana)        | Cuántos datos puede recibir sin saturarse.                        |

**Los flags son los que más verás en logs.**

- **SYN:** inicia una conexión; es el primer paso del saludo.

- **ACK:** confirma que se recibieron datos.

- **FIN:** termina la conexión de forma ordenada.

- **RST:** cancela o rechaza la conexión; es la "respuesta violenta".

- **PSH:** empuja los datos de inmediato, sin esperar más.

- **URG:** marca datos como urgentes; se usa muy poco.

**En la práctica** verás combinaciones como:

- SYN → Inicio de conexión.

- SYN, ACK → Respuesta del servidor.

- ACK → Confirmación.

- FIN, ACK → Cierre de conexión.

- RST, ACK → Conexión rechazada o cancelada.

**¿Por qué importa RST?**

Si ves muchas conexiones respondidas con **RST**, el servicio está rechazando conexiones.

Puede significar: puerto cerrado, servicio caído, firewall bloqueando o aplicación que rechaza el acceso.

**7. Garantías de TCP**

TCP ofrece cuatro garantías principales.

**Garantía 1 – Retransmisión**

Si un paquete se pierde, TCP lo vuelve a enviar.

**Garantía 2 – Confirmación (ACK)**

Cada grupo de datos recibido se confirma; si no llega confirmación, TCP asume que algo se perdió y reenvía.

**Garantía 3 – Orden**

Si los paquetes llegan desordenados, TCP los ordena antes de entregarlos a la aplicación.

**Garantía 4 – Control de flujo**

El receptor indica cuántos datos puede recibir a la vez mediante el campo **Window** (ventana).

Es como un semáforo que dice: "manda datos, pero no me satures."

Además, TCP tiene **control de congestión**: cuando la red está saturada, reduce la velocidad de envío.

Es como recibir un libro por partes: si una parte se pierde, TCP nota que falta, la vuelve a enviar, ordena las partes y recién entonces entrega el libro completo.

**¿Cuándo ves esto en un SOC?**

Cuando en una captura ves **Retransmisión**, **Dup ACK** o **Out-of-Order**, la red está perdiendo o retrasando paquetes.

Puede ser por saturación... o un indicio de algo más grave.

**8. Protocolos que utilizan TCP**

La gran mayoría de los servicios importantes utilizan TCP.

| **Protocolo**  | **Puerto**  | **Utiliza TCP** |
|----------------|-------------|-----------------|
| HTTP           | 80          | ✅              |
| HTTPS          | 443         | ✅              |
| SSH            | 22          | ✅              |
| FTP            | 21          | ✅              |
| SMTP           | 25          | ✅              |
| POP3           | 110         | ✅              |
| IMAP           | 143         | ✅              |
| SMB            | 445         | ✅              |
| RDP            | 3389        | ✅              |
| SQL Server     | 1433        | ✅              |

**Para un SOC, los más importantes son:**

- **TCP 443 (HTTPS):** navegación web cifrada; el puerto más común del mundo.

- **TCP 22 (SSH):** administración remota de Linux; muy atacado con fuerza bruta.

- **TCP 445 (SMB):** compartición de archivos en Windows; relacionado con ransomware y movimiento lateral.

- **TCP 3389 (RDP):** escritorio remoto de Windows; uno de los principales blancos de ataque.

- **TCP 1433 (SQL Server):** bases de datos; atractivo para robar información.

**Regla de oro**

Si un servicio necesita que la información llegue completa, casi siempre usará TCP.

**9. TCP en Wireshark**

Wireshark te mostrará los paquetes del Three-Way Handshake.

**Captura típica de una conexión HTTPS**

Paquete 1: TCP [SYN] — 192.168.1.15:52341 → 142.250.xxx.xxx:443

Paquete 2: TCP [SYN, ACK] — 142.250.xxx.xxx:443 → 192.168.1.15:52341

Paquete 3: TCP [ACK] — 192.168.1.15:52341 → 142.250.xxx.xxx:443

Después de eso fluyen los datos de la conversación.

**Interpretación**

- El puerto origen (52341) es efímero.

- El puerto destino (443) es HTTPS.

- La secuencia SYN → SYN-ACK → ACK confirma una conexión exitosa.

**Señales que debes saber reconocer**

| **Evento en Wireshark**   | **Posible significado**                        |
|---------------------------|------------------------------------------------|
| SYN, SYN-ACK, ACK         | Conexión establecida correctamente.            |
| SYN sin respuesta         | Servicio caído o puerto filtrado.              |
| RST después del SYN       | Puerto cerrado o conexión rechazada.           |
| Retransmisión             | Paquete perdido o red saturada.                |
| Dup ACK                   | Paquetes desordenados o perdidos.              |
| Out-of-Order              | Paquetes fuera de secuencia.                   |
| Muchos SYN sin ACK final  | Posible SYN Flood o escaneo de puertos.        |

**10. TCP en un Firewall**

El firewall decide qué conexiones TCP se permiten.

**Regla típica de firewall**

Origen 192.168.10.15 → Destino Servidor Web → TCP → Puerto 443 → **Permitido**

Interpretación: navegación web permitida.

**Otro ejemplo**

Origen 203.0.113.50 → Destino Servidor interno → TCP → Puerto 3389 → **Bloqueado**

Interpretación: el firewall bloqueó un intento de acceso RDP.

**Log de un firewall**

Registro típico:

Origen

192.168.10.20:53412

↓

Destino

198.51.100.30:3389

↓

TCP

↓

Acción: DENY

↓

Motivo: Regla de bloqueo de RDP externo

Como analista:

- Notas el puerto 3389 (RDP).

- Verificas si la regla corresponde.

- Compruebas cuántos intentos similares hubo.

- Investigas si la IP origen es conocida.

**Regla de oro del firewall**

Solo abrir los puertos estrictamente necesarios; todo lo demás se deniega por defecto.

**11. TCP en un SIEM**

Un SIEM recopila y correlaciona los eventos de red.

**Alerta típica 1**

30.000 paquetes SYN → TCP → Puerto 443 → en 60 segundos.

Como analista pensarías:

- ¿Es tráfico legítimo de un sitio muy visitado?

- ¿Puede ser un SYN Flood?

- ¿El origen es interno o externo?

**Alerta típica 2**

192.168.10.45 → Conexiones TCP → Puerto 445 → hacia 50 equipos distintos.

Como analista pensarías:

- ¿Es un servidor de archivos?

- ¿Puede ser movimiento lateral?

- ¿Está relacionado con un ransomware?

**Alerta típica 3**

203.0.113.10 → TCP → Puerto 22 → 10.000 intentos fallidos.

Como analista pensarías:

- ¿Hay fuerza bruta contra SSH?

- ¿Alguna conexión fue exitosa?

- ¿Qué usuarios se intentaron usar?

**12. ¿Cómo aprovechan TCP los atacantes?**

TCP es confiable, pero esa misma fiabilidad es usada en su contra.

**Ataque 1 – SYN Flood**

Es un ataque de denegación de servicio (DoS).

El atacante envía miles de paquetes **SYN** sin completar el Three-Way Handshake y sin esperar la respuesta.

El servidor responde con SYN-ACK y espera el ACK final que nunca llega.

Cada SYN pendiente ocupa recursos del servidor.

Con suficientes SYN, el servidor se satura y no puede atender a usuarios legítimos.

Atacante → SYN → SYN → SYN → Servidor saturado → Usuarios legítimos sin servicio

**Analogía**

Imagina que cientos de personas llaman a tu puerta y nadie se queda: cada vez que abres no hay nadie, y no puedes atender a quienes realmente quieren entrar.

**Ataque 2 – Escaneo de puertos (Nmap)**

Los atacantes escanean puertos para descubrir servicios con herramientas como **Nmap**.

Nmap envía paquetes TCP a muchos puertos y analiza las respuestas:

- Si recibe SYN-ACK: el puerto está abierto.

- Si recibe RST: el puerto está cerrado.

- Si no recibe respuesta: el puerto está filtrado.

Atacante → SYN al 22 → SYN al 80 → SYN al 443 → SYN al 445 → SYN al 3389 → Descubre servicios abiertos

Con esa información, el atacante sabe qué atacar.

**Ataque 3 – Session Hijacking (Secuestro de sesión)**

Un atacante intenta hacerse pasar por un equipo en una conexión activa.

Para eso necesita adivinar los **números de secuencia** de TCP.

Si lo logra, puede inyectar paquetes como si fuera el equipo legítimo.

Es un ataque avanzado, menos común hoy, pero se estudia en un SOC.

**Ataque 4 – Fuerza bruta sobre SSH y RDP**

TCP 22 (SSH) y TCP 3389 (RDP) son los favoritos de los atacantes.

Miles de intentos de conexión probando usuarios y contraseñas.

Si logran una credencial válida, obtienen acceso al sistema.

**Ataque 5 – RST injection (Inyección de RST)**

El atacante envía paquetes **RST** falsos para interrumpir conexiones.

Resultado: las conexiones legítimas se cortan.

Es una forma de sabotear servicios o de forzar reconexiones.

**13. ¿Cómo defenderse?**

**Defensa 1 – Firewall**

Filtrar el tráfico entrante y permitir solo los puertos necesarios.

**Defensa 2 – Rate limiting**

Limitar la cantidad de conexiones por segundo.

**Defensa 3 – SYN Cookies**

Una técnica para resistir SYN Flood: el servidor no guarda la conexión pendiente en memoria, responde con una "cookie" especial y libera recursos.

**Defensa 4 – IDS/IPS**

Detectar patrones anómalos: muchos SYN en poco tiempo, escaneos de puertos y comportamiento inusual.

**Defensa 5 – MFA**

Autenticación multifactor: aunque se robe una contraseña, el atacante no puede acceder.

Especialmente importante para SSH y RDP.

**Defensa 6 – Cerrar puertos innecesarios**

Cada puerto abierto es una puerta más al atacante.

**Defensa 7 – Segmentación de red**

Separar redes críticas de las no críticas; si una parte se compromete, el atacante no se mueve libremente.

**Defensa 8 – Monitoreo constante**

Revisar logs de firewall y SIEM para detectar lo anómalo antes de que escale.

**14. Aplicación práctica en un SOC**

**Caso 1 – SYN Flood al 443**

El SIEM muestra: 200.000 paquetes SYN → TCP → Puerto 443 → 60 segundos → desde muchas IP externas.

Interpretación: posible ataque DDoS o SYN Flood contra el servidor web.

Investigación:

- Verificar si el servidor responde.

- Confirmar que no hay usuarios legítimos afectados.

- Analizar si hay más IPs comprometidas.

- Activar mitigación (rate limiting, filtrado).

**Caso 2 – Escaneo masivo desde una IP interna**

El firewall muestra: 192.168.10.200 → TCP SYN → 500 puertos distintos → en 10 minutos.

Interpretación: posible escaneo de puertos desde un equipo interno.

Investigación:

- ¿Ese equipo debería hacer eso?

- ¿Qué proceso lo genera?

- ¿El equipo está comprometido?

- ¿Hay otros equipos escaneando?

**Caso 3 – Retransmisiones excesivas**

Wireshark muestra: 3.000 retransmisiones → 2 minutos → misma conexión.

Interpretación: la red pierde muchos paquetes.

Investigación:

- ¿Es un enlace saturado?

- ¿Hay interferencia o fallo de hardware?

- ¿El equipo emisor está sobrecargado?

- ¿Alguien está inyectando RST o interferencias?

**Caso 4 – Fuerza bruta al 22**

El SIEM muestra: 203.0.113.150 → TCP → Puerto 22 → 50.000 intentos fallidos → 3 horas.

Interpretación: posible fuerza bruta contra SSH.

Investigación:

- ¿Algún intento fue exitoso?

- ¿Qué usuarios se probaron?

- ¿El firewall debería bloquear esa IP?

- ¿Se puede añadir la IP a una lista de bloqueo?

**15. TCP vs UDP**

| **Característica**    | **TCP**               | **UDP**                      |
|-----------------------|-----------------------|------------------------------|
| Orientado a conexión  | ✅ Sí                 | ❌ No                        |
| Three-Way Handshake   | ✅ Sí                 | ❌ No                        |
| Garantiza la entrega  | ✅ Sí                 | ❌ No                        |
| Mantiene el orden     | ✅ Sí                 | ❌ No                        |
| Reenvía paquetes      | ✅ Sí                 | ❌ No                        |
| ACK                   | ✅ Sí                 | ❌ No                        |
| Control de flujo      | ✅ Sí                 | ❌ No                        |
| Control de congestión | ✅ Sí                 | ❌ No                        |
| Velocidad             | Más lenta             | Más rápida                   |
| Confiabilidad         | Muy alta              | Baja                         |
| Uso típico            | Web, SSH, correo, RDP | DNS, VoIP, juegos, streaming |

**La diferencia en una frase**

**TCP:** "Necesito asegurarme de que todo llegue."

**UDP:** "Necesito que llegue rápido, aunque algo se pierda."

**16. Lo que esperan de un Analista SOC Nivel 1**

Cuando veas un log TCP como este:

Origen:

203.0.113.25:50001

↓

Destino:

192.168.10.30:3389

↓

TCP

↓

Flags: SYN

↓

Acción: Bloqueado

No debes solo leer los números; debes preguntarte:

- ¿Quién es el origen y el destino?

- ¿Qué puerto se usa y qué servicio representa?

- ¿Qué flags tiene la conexión?

- ¿El volumen de conexiones es normal?

- ¿El horario es habitual?

- ¿El origen debería comunicarse con ese destino?

- ¿Hubo intentos fallidos anteriores?

- ¿Es un patrón de fuerza bruta o de escaneo?

Ese razonamiento es el trabajo diario de un analista.

**Regla práctica**

Muchos SYN al 443 → posible SYN Flood.

Conexiones a 445 entre muchos equipos → posible movimiento lateral.

RST en respuestas → puerto cerrado o conexión rechazada.

Miles de intentos al 22 → posible fuerza bruta.

**17. Resumen**

**TCP**

- Es un protocolo de la **Capa 4 (Transporte)**.

- Es **orientado a conexión**.

- Utiliza el **Three-Way Handshake** para establecer la conexión.

- Garantiza la entrega, el orden y la confirmación de los datos.

- No cifra la información.

**El Three-Way Handshake**

SYN → SYN-ACK → ACK

**Los flags principales**

- SYN: inicia la conexión.

- ACK: confirma datos.

- FIN: cierra la conexión.

- RST: cancela o rechaza la conexión.

- PSH: empuja los datos de inmediato.

- URG: marca datos urgentes.

**Garantías**

- Retransmisión.

- Confirmación (ACK).

- Orden.

- Control de flujo.

- Control de congestión.

**Ataques típicos**

- SYN Flood.

- Escaneo de puertos.

- Session Hijacking.

- Fuerza bruta sobre SSH y RDP.

- RST injection.

**¿Cómo se ve en un SOC?**

- Wireshark: flags, handshake, retransmisiones.

- Firewall: reglas allow/deny por puerto.

- SIEM: alertas por volumen, origen y puerto.

**🧠 Conceptos clave para memorizar**

| **Concepto**          | **Debes recordar**                                           |
|-----------------------|--------------------------------------------------------------|
| TCP                   | Transmission Control Protocol.                               |
| Capa                  | Capa 4 (Transporte).                                         |
| Orientado a conexión  | Establece una sesión antes de enviar datos.                  |
| Three-Way Handshake   | SYN → SYN-ACK → ACK.                                         |
| SYN                   | Solicita iniciar la conexión.                                |
| ACK                   | Confirma la recepción de datos.                              |
| FIN                   | Cierra la conexión de forma ordenada.                        |
| RST                   | Cancela o rechaza la conexión.                               |
| Retransmisión         | TCP reenvía los paquetes perdidos.                           |
| 443                   | HTTPS (web cifrada).                                         |
| 22                    | SSH (administración remota).                                 |
| 445                   | SMB (archivos en Windows).                                   |
| 3389                  | RDP (escritorio remoto).                                     |
| SYN Flood             | Inundar con SYN para saturar el servidor.                    |
| Escaneo de puertos    | Enviar SYN a muchos puertos para descubrir servicios.        |

**🎓 Consejo como tu instructor de SOC**

TCP es el protocolo que verás en casi todos los logs.

Por eso, cuando analices una alerta, entrena tu mente para hacer asociaciones rápidas.

**Por ejemplo:**

- Si ves muchos **SYN al puerto 443** desde muchas IPs: posible **SYN Flood** o ataque DDoS.

- Si ves **puerto 445** con conexiones entre muchas computadoras: posible **movimiento lateral** de un malware.

- Si ves **RST** como respuesta: conexión **rechazada** o puerto cerrado.

- Si ves miles de intentos al **puerto 22**: posible **fuerza bruta** contra SSH.

- Si ves **retransmisiones** constantes: red con pérdida de paquetes o interferencia.

Ese razonamiento basado en **puertos, flags y comportamiento** es el que te diferenciará como analista.

No memorices los números sin contexto; asócialos siempre con el servicio y con el riesgo.

Y recuerda la base de todo: **el Three-Way Handshake**.

Si entiendes ese saludo, entenderás los logs de firewall, las capturas de Wireshark y las alertas del SIEM.

---

**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Evaluación – Módulo 10: TCP (Transmission Control Protocol)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Piensa como si estuvieras realizando una prueba para ingresar a un **SOC Nivel 1**. Encontrarás preguntas teóricas y casos prácticos. Al finalizar encontrarás las respuestas con su justificación.

**Pregunta 1**

¿Qué significa la sigla **TCP**?

**A)** Transmission Control Protocol

**B)** Transfer Control Process

**C)** Transmission Communication Protocol

**D)** Transport Control Program

**Pregunta 2**

¿En qué capa del modelo **OSI** trabaja TCP?

**A)** Capa 2 – Enlace de Datos.

**B)** Capa 3 – Red.

**C)** Capa 4 – Transporte.

**D)** Capa 7 – Aplicación.

**Pregunta 3**

¿Cuál es el orden correcto del **Three-Way Handshake**?

**A)** ACK → SYN → SYN-ACK

**B)** SYN → SYN-ACK → ACK

**C)** SYN-ACK → ACK → SYN

**D)** FIN → ACK → SYN

**Pregunta 4**

¿Cuál de las siguientes afirmaciones es **correcta** sobre TCP?

**A)** No garantiza la entrega de los paquetes.

**B)** Cifra automáticamente toda la comunicación.

**C)** Es un protocolo orientado a conexión y confiable.

**D)** No utiliza confirmaciones.

**Pregunta 5**

Un paquete TCP con el flag **RST** indica:

**A)** El inicio de una conexión.

**B)** La confirmación de datos recibidos.

**C)** La cancelación o rechazo de una conexión.

**D)** El envío de datos urgentes.

**Pregunta 6**

¿Cuál de los siguientes protocolos utiliza normalmente **TCP**?

**A)** HTTPS.

**B)** NTP.

**C)** DHCP.

**D)** SNMP.

**Pregunta 7 (Caso práctico SOC)**

Como analista SOC observas el siguiente registro:

Origen:

203.0.113.150

↓

TCP

↓

Puerto 22

↓

Miles de intentos

¿Cuál sería tu primera hipótesis?

**A)** Consultas DNS normales.

**B)** Un posible ataque de fuerza bruta contra SSH.

**C)** Una transferencia FTP.

**D)** Sincronización horaria mediante NTP.

**Pregunta 8**

En Wireshark observas el siguiente patrón:

TCP [SYN]

↓

TCP [SYN, ACK]

↓

TCP [ACK]

¿Qué indica?

**A)** Una conexión TCP establecida correctamente.

**B)** Una conexión rechazada por RST.

**C)** Un error de cifrado TLS.

**D)** Un fallo en la resolución DNS.

**Pregunta 9**

¿Qué es un ataque **SYN Flood**?

**A)** Enviar miles de consultas DNS para saturar un servidor.

**B)** Enviar miles de paquetes SYN sin completar el handshake para agotar los recursos del servidor.

**C)** Enviar paquetes con credenciales falsas por SSH.

**D)** Interceptar el tráfico cifrado de una conexión HTTPS.

**Pregunta 10 (Caso práctico SOC)**

El SIEM genera la siguiente alerta:

500.000 paquetes SYN

↓

TCP

↓

Puerto 443

↓

Desde 2.000 IP externas

↓

60 segundos

¿Cuál sería la hipótesis más razonable?

**A)** Un usuario descargando archivos.

**B)** Un posible SYN Flood o ataque DDoS contra el servidor web.

**C)** Una consulta DNS de gran tamaño.

**D)** Una actualización automática de Windows.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: A**

**Justificación**

TCP significa **Transmission Control Protocol**.

Es el protocolo de transporte orientado a conexión que garantiza la entrega fiable de los datos.

**Pregunta 2**

✅ **Respuesta correcta: C**

**Justificación**

TCP trabaja en la **Capa 4 (Transporte)** del modelo OSI, al igual que UDP.

La diferencia es que TCP añade fiabilidad, orden y control de flujo.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

El **Three-Way Handshake** sigue este orden:

SYN

↓

SYN-ACK

↓

ACK

Primero el cliente pide iniciar la conexión (SYN).

Luego el servidor acepta (SYN-ACK).

Finalmente el cliente confirma (ACK).

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

TCP es un protocolo **orientado a conexión** que **garantiza la entrega** de los datos mediante confirmaciones y retransmisiones.

Sin embargo, **no cifra** la información.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

El flag **RST (Reset)** se utiliza para **cancelar o rechazar** una conexión.

Lo verás, por ejemplo, cuando un puerto está cerrado o un servicio no acepta la conexión.

**Pregunta 6**

✅ **Respuesta correcta: A**

**Justificación**

**HTTPS** utiliza **TCP 443**.

NTP, DHCP y SNMP utilizan UDP, ya que priorizan la velocidad.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

Miles de intentos hacia el puerto **TCP 22 (SSH)** son un fuerte indicador de un posible **ataque de fuerza bruta**.

Como analista, deberías verificar:

- Si alguna conexión fue exitosa.

- Qué usuarios se intentaron usar.

- Si la IP origen está en listas de bloqueo.

**Pregunta 8**

✅ **Respuesta correcta: A**

**Justificación**

La secuencia SYN → SYN-ACK → ACK es el **Three-Way Handshake**.

Indica que la conexión TCP se estableció correctamente y que los datos pueden fluir.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

Un **SYN Flood** consiste en enviar miles de paquetes **SYN** sin completar el Three-Way Handshake.

El servidor responde con SYN-ACK y queda esperando confirmaciones que nunca llegan.

Con suficientes paquetes:

- Los recursos del servidor se agotan.

- Los usuarios legítimos quedan sin servicio.

Es un ataque de denegación de servicio (DoS).

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

500.000 SYN al puerto 443 desde miles de IP en 60 segundos es un patrón clásico de **SYN Flood** o **ataque DDoS**.

Como analista SOC deberías:

- Confirmar si el servidor web sigue respondiendo.

- Verificar el estado de los usuarios legítimos.

- Activar las mitigaciones disponibles (rate limiting, filtrado).

- Documentar la alerta y escalar si es necesario.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                        |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Comprendes TCP y puedes identificar ataques asociados como SYN Flood y escaneos de puertos.    |
| **8–9**                  | 🟢 **Muy buen nivel.** Ya interpretas correctamente los flags y el Three-Way Handshake en capturas y logs.      |
| **6–7**                  | 🟡 **Buen progreso.** Repasa el Three-Way Handshake y los ataques más comunes contra TCP.                       |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar las diferencias entre TCP y UDP.                 |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** TCP es la base de la mayoría de los logs que verás en un SOC. |
