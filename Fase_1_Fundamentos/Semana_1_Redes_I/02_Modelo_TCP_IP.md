**Módulo de Estudio SOC**

**Módulo 3 - Modelo TCP/IP**

**Nivel:** Principiante → Analista SOC Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es el Modelo TCP/IP.

-   Conocer sus cuatro capas y su función.

-   Entender la diferencia entre TCP/IP y el Modelo OSI.

-   Identificar los protocolos más importantes de cada capa.

-   Comprender cómo un atacante puede aprovechar cada capa.

-   Saber cómo defenderlas.

-   Aplicar este conocimiento en el trabajo diario de un Analista SOC.

**1. ¿Qué es el Modelo TCP/IP?**

El **Modelo TCP/IP (Transmission Control Protocol / Internet Protocol)** es el conjunto de protocolos que permite que Internet funcione.

A diferencia del Modelo OSI, que es un modelo teórico para comprender cómo viajan los datos, **TCP/IP es el modelo que realmente utilizan las redes modernas**, incluida Internet.

Cada vez que:

-   Navegas por una página web.

-   Envías un correo electrónico.

-   Miras un video en YouTube.

-   Usas WhatsApp.

-   Descargas un archivo.

Estás utilizando el modelo TCP/IP.

**¿Por qué es importante para un SOC?**

La mayoría de los logs, alertas y herramientas de seguridad están basados en protocolos TCP/IP.

Cuando un analista revisa:

-   Wireshark

-   Firewall

-   IDS/IPS

-   EDR

-   SIEM

está analizando tráfico TCP/IP.

Por eso, dominar este modelo es fundamental.

**Las 4 capas del Modelo TCP/IP**

4 Aplicación
3 Transporte
2 Internet
1 Acceso a la Red

Una forma sencilla de recordarlas es:

**Acceso → Internet → Transporte → Aplicación**

**Diferencia con el Modelo OSI**

OSI tiene **7 capas**.

TCP/IP tiene **4 capas**.

TCP/IP agrupa varias capas del OSI.

  -----------------------------------------------------------------------
  **Modelo TCP/IP**                   **Equivale en OSI**
  ----------------------------------- -----------------------------------
  Aplicación                          7 + 6 + 5

  Transporte                          4

  Internet                            3

  Acceso a la Red                     2 + 1
  -----------------------------------------------------------------------

**2. Capa 1 -- Acceso a la Red**

**Función**

Es la capa encargada de conectar físicamente un dispositivo a la red.

Aquí viajan las tramas.

Se utilizan:

-   Direcciones MAC

-   Ethernet

-   Wi-Fi

-   Fibra óptica

**Dispositivos**

-   Switch

-   Tarjeta de red

-   Hub

-   Access Point

**Protocolos**

-   Ethernet

-   Wi-Fi (802.11)

-   ARP

**Analogía**

Es como una calle dentro de un barrio.

Los vecinos pueden comunicarse entre ellos.

**Ataques**

**ARP Spoofing**

El atacante se hace pasar por el router.

Consecuencia:

Intercepción del tráfico.

**MAC Flooding**

Satura la tabla MAC del switch.

**Rogue Access Point**

El atacante instala un punto de acceso Wi-Fi falso para engañar a los usuarios.

**Defensa**

-   VLAN

-   Port Security

-   Dynamic ARP Inspection

-   802.1X

-   Redes Wi-Fi seguras (WPA2/WPA3)

**3. Capa 2 -- Internet**

**Función**

Es responsable del direccionamiento y del enrutamiento entre redes.

Aquí aparecen las direcciones IP.

**Protocolos**

-   IPv4

-   IPv6

-   ICMP

-   IPSec

**Dispositivos**

-   Router

-   Firewall de capa 3

**Ejemplo**

192.168.1.15

↓

Router

↓

8.8.8.8

**Analogía**

Es como el sistema de rutas que utiliza un servicio de mensajería para llevar un paquete desde una ciudad hasta otra.

**Ataques**

**Escaneo de red**

Busca equipos activos.

**IP Spoofing**

El atacante falsifica una dirección IP.

**ICMP Flood**

Envía enormes cantidades de paquetes ICMP para afectar la disponibilidad de un servicio.

**Defensa**

-   Firewalls

-   ACL

-   IDS/IPS

-   Segmentación de red

-   Filtrado de tráfico sospechoso

**4. Capa 3 -- Transporte**

**Función**

Controla cómo se envían los datos entre dos aplicaciones.

Aquí aparecen los puertos.

**Protocolos**

-   TCP

-   UDP

**TCP**

Características:

-   Orientado a conexión.

-   Confirma la recepción de los datos.

-   Reenvía paquetes perdidos.

-   Más lento pero más confiable.

Ejemplos:

-   HTTPS

-   SSH

-   FTP

-   SMTP

**UDP**

Características:

-   No confirma la recepción.

-   Más rápido.

-   Menor sobrecarga.

-   Se utiliza cuando la velocidad es más importante que la confiabilidad.

Ejemplos:

-   Streaming

-   Videollamadas

-   Juegos online

-   DNS (consultas)

**Ataques**

-   SYN Flood

-   Escaneo de puertos

-   Fuerza bruta

-   UDP Flood

**Defensa**

-   Firewall

-   IDS/IPS

-   Rate Limiting

-   MFA

-   Cierre de puertos innecesarios

**5. Capa 4 -- Aplicación**

**Función**

Es donde trabajan las aplicaciones que utilizan los usuarios.

Aquí aparecen la mayoría de los protocolos conocidos.

**Protocolos**

-   HTTP

-   HTTPS

-   DNS

-   FTP

-   SSH

-   SMTP

-   POP3

-   IMAP

-   DHCP

-   NTP

**Ejemplos**

-   Google Chrome

-   Microsoft Outlook

-   WhatsApp

-   Teams

-   Navegadores

-   Clientes FTP

**Analogía**

Es el mostrador de una empresa donde el cliente solicita un servicio.

**Ataques**

**Phishing**

Engaño al usuario.

**SQL Injection**

Manipulación de bases de datos.

**Cross-Site Scripting (XSS)**

Inyección de código en páginas web.

**Malware**

Programas maliciosos.

**Ransomware**

Secuestro de información.

**Defensa**

-   WAF

-   Antivirus

-   EDR

-   Capacitación

-   Actualizaciones

-   Validación de entradas

**6. Cuadro comparativo de las capas**

  --------------------------------------------------------------------------------------------------------------------
  **Capa TCP/IP**   **Función**                       **Protocolos**                     **Dispositivos**
  ----------------- --------------------------------- ---------------------------------- -----------------------------
  Aplicación        Servicios al usuario              HTTP, HTTPS, DNS, SMTP, FTP, SSH   Navegador, servidor web

  Transporte        Comunicación extremo a extremo    TCP, UDP                           Firewall, sistema operativo

  Internet          Direccionamiento y enrutamiento   IPv4, IPv6, ICMP                   Router

  Acceso a la Red   Comunicación física y local       Ethernet, Wi-Fi, ARP               Switch, NIC
  --------------------------------------------------------------------------------------------------------------------

**7. Comparación entre TCP/IP y OSI**

  -----------------------------------------------------------------------
  **Modelo OSI**                        **Modelo TCP/IP**
  ------------------------------------- ---------------------------------
  7 capas                               4 capas

  Modelo teórico                        Modelo práctico

  Se usa para enseñar                   Se usa en Internet

  Más detallado                         Más simple

  Divide funciones                      Agrupa funciones
  -----------------------------------------------------------------------

**8. ¿Cómo puede atacar un ciberdelincuente cada capa?**

  -----------------------------------------------------------------------
  **Capa**             **Ataques**
  -------------------- --------------------------------------------------
  Aplicación           Phishing, SQL Injection, XSS, Malware

  Transporte           SYN Flood, Fuerza Bruta, UDP Flood

  Internet             Escaneo, IP Spoofing, ICMP Flood

  Acceso a la Red      ARP Spoofing, MAC Flooding, Rogue AP
  -----------------------------------------------------------------------

**9. ¿Cómo defender cada capa?**

  -----------------------------------------------------------------------
  **Capa**                **Defensa**
  ----------------------- -----------------------------------------------
  Aplicación              WAF, EDR, Actualizaciones, MFA

  Transporte              Firewall, IDS/IPS, Rate Limiting

  Internet                ACL, Firewalls, Segmentación

  Acceso a la Red         VLAN, Port Security, WPA3
  -----------------------------------------------------------------------

**10. Aplicación práctica en un SOC**

**Ejemplo 1**

**Alerta**

Puerto 22

2000 intentos SSH

**Capa afectada**

Transporte

**Posible ataque**

Fuerza Bruta

**Acciones SOC**

-   Revisar logs.

-   Verificar origen.

-   Bloquear IP si corresponde.

-   Confirmar si hubo autenticaciones exitosas.

**Ejemplo 2**

**Alerta**

192.168.1.15

↓

8.8.8.8

Miles de consultas ICMP.

**Capa**

Internet

**Posible incidente**

ICMP Flood o reconocimiento.

**Ejemplo 3**

**Alerta**

ARP duplicadas

**Capa**

Acceso a la Red

**Posible incidente**

ARP Spoofing.

**Ejemplo 4**

**Alerta**

Usuario descarga un archivo malicioso desde una página web.

**Capa**

Aplicación

**Posible incidente**

Malware.

**11. Lo que esperan de un Analista SOC Nivel 1**

Cuando revises una alerta debes preguntarte:

-   ¿Qué protocolo está involucrado?

-   ¿En qué capa TCP/IP ocurre el problema?

-   ¿Qué dispositivo participa?

-   ¿Es tráfico normal?

-   ¿Es un intento de ataque?

-   ¿Qué evidencia necesito?

-   ¿Qué logs debo revisar?

-   ¿Debo escalar el incidente?

**12. Resumen**

**Acceso a la Red**

-   Comunicación física y local.

-   Ethernet.

-   Wi-Fi.

-   MAC.

-   ARP.

**Internet**

-   Direcciones IP.

-   Enrutamiento.

-   IPv4.

-   IPv6.

-   ICMP.

**Transporte**

-   TCP.

-   UDP.

-   Puertos.

-   Comunicación entre aplicaciones.

**Aplicación**

-   HTTP.

-   HTTPS.

-   DNS.

-   FTP.

-   SSH.

-   SMTP.

-   Servicios utilizados por el usuario.

**13. Conceptos clave para memorizar**

  -----------------------------------------------------------------------
  **Concepto**              **Debes recordar**
  ------------------------- ---------------------------------------------
  Acceso a la Red           MAC, Ethernet, Wi-Fi, ARP

  Internet                  IP, Router, ICMP

  Transporte                TCP, UDP, Puertos

  Aplicación                HTTP, HTTPS, DNS, SSH, FTP
  -----------------------------------------------------------------------

**🎯 Relación entre IP Pública, OSI y TCP/IP**

Hasta ahora ya conoces tres conceptos fundamentales. Es importante que los conectes mentalmente:

Internet
│
IP Pública (Capa Internet / Capa 3 OSI)
│
┌───────────┐
│ Router │
└───────────┘
│
─────────────────────────
Red Local (LAN)
─────────────────────────
│ │ │
PC 1 PC 2 Servidor
192.168.1.10 192.168.1.20 192.168.1.30
(MAC) (MAC) (MAC)

Cuando un usuario abre [**https://www.google.com**](https://www.google.com) ocurre, de forma simplificada, lo siguiente:

1.  **Aplicación:** el navegador genera una solicitud HTTPS.

2.  **Transporte:** TCP establece una conexión usando el puerto 443.

3.  **Internet:** el paquete recibe una dirección IP de origen y una de destino para poder ser enrutado.

4.  **Acceso a la Red:** el paquete se convierte en una trama Ethernet o Wi-Fi y viaja por la red local hasta el router.

Este proceso ocurre en milisegundos y se repite miles de veces por segundo.

**💡 Consejo como tu entrenador para un SOC**

No estudies el Modelo TCP/IP de memoria. **Aprende a relacionarlo con los logs que verás todos los días.**

Cuando abras un registro en un SIEM o en Wireshark, intenta identificar inmediatamente:

-   **¿Hay una dirección MAC?** → Piensa en **Acceso a la Red**.

-   **¿Hay direcciones IP?** → Piensa en **Internet**.

-   **¿Hay puertos TCP o UDP?** → Piensa en **Transporte**.

-   **¿Aparecen HTTP, HTTPS, DNS o SSH?** → Piensa en **Aplicación**.

Ese ejercicio mental hará que, con el tiempo, puedas interpretar una alerta en segundos y decidir qué evidencias revisar primero, una habilidad esencial para un Analista SOC.

**Evaluación -- Módulo 3: Modelo TCP/IP**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Al finalizar, revisa las respuestas y sus justificaciones.

**Pregunta 1**

¿Cuál es la principal diferencia entre el Modelo TCP/IP y el Modelo OSI?

**A)** TCP/IP tiene 7 capas y OSI tiene 4.

**B)** OSI es un modelo teórico y TCP/IP es el modelo utilizado en Internet.

**C)** TCP/IP solo funciona en redes privadas.

**D)** OSI reemplazó completamente a TCP/IP.

**Pregunta 2**

¿Cuántas capas tiene el Modelo TCP/IP?

**A)** 3

**B)** 4

**C)** 5

**D)** 7

**Pregunta 3**

¿En qué capa del Modelo TCP/IP trabajan las direcciones IP?

**A)** Acceso a la Red

**B)** Transporte

**C)** Internet

**D)** Aplicación

**Pregunta 4**

¿Cuál de los siguientes protocolos pertenece a la capa **Transporte**?

**A)** HTTP

**B)** TCP

**C)** ICMP

**D)** ARP

**Pregunta 5**

¿Qué protocolo pertenece a la capa **Aplicación**?

**A)** UDP

**B)** Ethernet

**C)** HTTP

**D)** IPv4

**Pregunta 6**

¿Cuál es la principal diferencia entre **TCP** y **UDP**?

**A)** TCP utiliza direcciones MAC y UDP utiliza direcciones IP.

**B)** TCP es orientado a conexión y confirma la recepción de los datos; UDP prioriza la velocidad y no confirma la entrega.

**C)** UDP solo funciona en Internet y TCP solo en redes locales.

**D)** No existe ninguna diferencia importante.

**Pregunta 7**

Como analista SOC recibes la siguiente alerta:

Se detectaron miles de paquetes ICMP provenientes de una misma dirección IP.

¿En qué capa del Modelo TCP/IP ocurre principalmente este incidente?

**A)** Aplicación

**B)** Transporte

**C)** Internet

**D)** Acceso a la Red

**Pregunta 8**

¿Cuál de los siguientes ataques corresponde principalmente a la capa **Acceso a la Red**?

**A)** SQL Injection

**B)** Phishing

**C)** ARP Spoofing

**D)** Fuerza Bruta SSH

**Pregunta 9**

¿Qué protocolo se utiliza normalmente para navegar de forma segura por Internet?

**A)** FTP

**B)** HTTP

**C)** HTTPS

**D)** SMTP

**Pregunta 10 (Caso práctico SOC)**

Un usuario recibe un correo electrónico falso, hace clic en un enlace e ingresa sus credenciales en una página idéntica a la del banco.

¿En qué capa del Modelo TCP/IP ocurre principalmente el ataque?

**A)** Acceso a la Red

**B)** Internet

**C)** Transporte

**D)** Aplicación

**Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

El **Modelo OSI** fue creado como un modelo de referencia para comprender cómo se comunican las redes.

El **Modelo TCP/IP** es el que realmente utilizan Internet y la mayoría de las redes actuales.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

El Modelo TCP/IP tiene **4 capas**:

1.  Acceso a la Red

2.  Internet

3.  Transporte

4.  Aplicación

**Consejo para el examen:**

OSI = **7 capas**

TCP/IP = **4 capas**

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

La capa **Internet** se encarga del direccionamiento mediante **IPv4** e **IPv6** y del enrutamiento entre redes.

**Palabra clave:**

**IP = Capa Internet**

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

Los protocolos principales de la capa **Transporte** son:

-   TCP

-   UDP

Son responsables de la comunicación entre aplicaciones y utilizan **puertos**.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

HTTP pertenece a la capa **Aplicación**.

También pertenecen:

-   HTTPS

-   DNS

-   FTP

-   SSH

-   SMTP

-   IMAP

-   POP3

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

TCP:

-   Establece una conexión.

-   Confirma la recepción.

-   Reenvía paquetes perdidos.

-   Es más confiable.

UDP:

-   No establece conexión.

-   No confirma la recepción.

-   Es más rápido.

-   Se utiliza cuando la velocidad es prioritaria, como en videollamadas o juegos en línea.

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

El protocolo **ICMP** pertenece a la capa **Internet**.

Un gran volumen de paquetes ICMP puede indicar un ataque como un **ICMP Flood** o una actividad de reconocimiento.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación**

El **ARP Spoofing** manipula las direcciones MAC y el protocolo ARP para interceptar el tráfico en una red local.

Por eso corresponde a la capa **Acceso a la Red**.

**Pregunta 9**

✅ **Respuesta correcta: C**

**Justificación**

**HTTPS** utiliza cifrado (TLS) para proteger la comunicación entre el navegador y el servidor.

Esto garantiza:

-   Confidencialidad.

-   Integridad.

-   Autenticación del servidor.

**Pregunta 10**

✅ **Respuesta correcta: D**

**Justificación**

El phishing es un ataque dirigido a las aplicaciones y a los usuarios.

El engaño ocurre mediante:

-   Correos electrónicos.

-   Sitios web falsos.

-   Formularios fraudulentos.

Por eso se clasifica principalmente dentro de la capa **Aplicación**.

**Resultado**

  ---------------------------------------------------------------------------------------------------------------------------------------------
  **Respuestas Correctas**   **Nivel**
  -------------------------- ------------------------------------------------------------------------------------------------------------------
  **10/10**                  ⭐ Excelente. Ya comienzas a relacionar protocolos, capas y tipos de ataque como lo hace un Analista SOC Junior.

  **8--9**                   🟢 Muy buen nivel. Solo necesitas afianzar algunos conceptos antes de pasar al siguiente tema.

  **6--7**                   🟡 Buen progreso. Repasa especialmente la diferencia entre las capas y los protocolos que pertenecen a cada una.

  **4--5**                   🟠 Aún hay conceptos por reforzar. Relee el módulo y vuelve a realizar el cuestionario.

  **0--3**                   🔴 Es recomendable repasar el Modelo TCP/IP antes de avanzar a protocolos específicos como DNS, HTTP o SSH.
  ---------------------------------------------------------------------------------------------------------------------------------------------
