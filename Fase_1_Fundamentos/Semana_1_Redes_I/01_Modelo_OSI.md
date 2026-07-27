**Módulo de Estudio SOC**

**Módulo 2 - Modelo OSI (Open Systems Interconnection)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es el Modelo OSI.

-   Conocer las siete capas y su función.

-   Identificar dispositivos y protocolos en cada capa.

-   Entender cómo un atacante puede aprovechar cada capa.

-   Saber cómo defenderlas.

-   Aplicar estos conocimientos al trabajo diario de un Analista SOC.

**1. ¿Qué es el Modelo OSI?**

El **Modelo OSI (Open Systems Interconnection)** es un modelo teórico que divide la comunicación entre dispositivos en **7 capas**.

Cada capa tiene una función específica y se comunica únicamente con la capa inmediatamente superior e inferior.

**¿Por qué existe?**

Imagina que envías una carta.

No basta con escribirla.

También necesitas:

-   Un sobre.

-   Una dirección.

-   Un cartero.

-   Un medio de transporte.

-   Una oficina postal.

-   Un destinatario.

La comunicación en una red funciona de forma similar: cada \"paso\" tiene una responsabilidad distinta.

**¿Por qué es importante en Ciberseguridad?**

Cuando ocurre un incidente, el analista SOC debe identificar:

-   ¿En qué capa ocurre el problema?

-   ¿Qué protocolo está involucrado?

-   ¿Qué dispositivo participa?

-   ¿Qué evidencia buscar?

Pensar por capas ayuda a investigar con orden y rapidez.

**Las 7 capas del Modelo OSI**

7 Aplicación
6 Presentación
5 Sesión
4 Transporte
3 Red
2 Enlace de Datos
1 Física

Una forma clásica de memorizar el orden (de abajo hacia arriba) es:

**Física → Enlace → Red → Transporte → Sesión → Presentación → Aplicación**

**2. Capa 1 -- Física**

**Función**

Es la capa encargada de transmitir los **bits (0 y 1)** a través del medio físico.

Aquí no existen direcciones IP ni puertos.

Solo viajan señales eléctricas, ópticas o de radio.

**Ejemplos**

-   Cable Ethernet

-   Fibra óptica

-   Wi-Fi (medio físico/radio)

-   Conectores RJ-45

**Dispositivos**

-   Hub

-   Repetidor

-   Cableado

-   Antenas

**Analogía**

Es la carretera por donde circulan los vehículos.

Sin carretera, nadie puede viajar.

**Ataques posibles**

-   Corte de cables.

-   Sabotaje físico.

-   Robo de equipos.

-   Interferencia de señal inalámbrica (jamming).

**Defensa**

-   Control de acceso físico.

-   CCTV.

-   Armarios de comunicaciones cerrados.

-   Redundancia de enlaces.

-   Protección del cableado.

**3. Capa 2 -- Enlace de Datos**

**Función**

Permite que dos dispositivos conectados a la misma red local se comuniquen correctamente.

Aquí aparecen las **direcciones MAC**.

**¿Qué es una MAC?**

Es el identificador físico de una tarjeta de red.

Ejemplo:

00:1A:2B:3C:4D:5E

**Protocolos**

-   Ethernet

-   ARP

-   VLAN (802.1Q)

**Dispositivos**

-   Switch

**Ataques**

**ARP Spoofing**

El atacante engaña a otros equipos para hacerse pasar por el router.

Resultado:

Puede interceptar el tráfico (Man-in-the-Middle).

**MAC Flooding**

El atacante llena la tabla MAC del switch.

Consecuencia:

El switch comienza a comportarse como un hub y envía tráfico a todos los puertos.

**Defensa**

-   Port Security.

-   Dynamic ARP Inspection.

-   VLAN.

-   802.1X.

-   Configuración segura del switch.

**4. Capa 3 -- Red**

**Función**

Aquí aparecen las **direcciones IP**.

Esta capa decide por dónde viajarán los paquetes entre diferentes redes.

**Protocolos**

-   IPv4

-   IPv6

-   ICMP

-   IPSec

**Dispositivos**

-   Router

-   Firewall de capa 3

**Ejemplo**

192.168.1.20

↓

Router

↓

8.8.8.8

**Ataques**

-   Escaneo de red.

-   IP Spoofing.

-   ICMP Flood.

-   Reconocimiento.

**Defensa**

-   Firewalls.

-   ACL.

-   IDS/IPS.

-   Segmentación.

-   Filtrado ICMP cuando corresponda.

**5. Capa 4 -- Transporte**

**Función**

Controla cómo llegan los datos.

Aquí aparecen los **puertos**.

**Protocolos**

-   TCP

-   UDP

**Ejemplos**

HTTP → Puerto 80

HTTPS → Puerto 443

SSH → Puerto 22

DNS → Puerto 53

**Funciones**

-   Control de errores.

-   Confirmación de recepción (TCP).

-   Reenvío de paquetes.

-   Control de flujo.

**Ataques**

-   SYN Flood.

-   Escaneo de puertos.

-   Fuerza bruta sobre SSH o RDP.

**Defensa**

-   Firewall.

-   Rate limiting.

-   IDS/IPS.

-   MFA.

-   Cierre de puertos innecesarios.

**6. Capa 5 -- Sesión**

**Función**

Administra el inicio, mantenimiento y cierre de una comunicación entre dos aplicaciones.

**Ejemplo**

Cuando ingresas a un banco:

1.  Inicias sesión.

2.  Operas.

3.  Cierras sesión.

Todo eso corresponde a esta capa.

**Ataques**

-   Session Hijacking.

-   Robo de cookies.

-   Secuestro de sesiones.

**Defensa**

-   Expiración de sesiones.

-   Cookies seguras.

-   HTTPS.

-   MFA.

**7. Capa 6 -- Presentación**

**Función**

Se encarga del formato de los datos.

Realiza tareas como:

-   Cifrado.

-   Descifrado.

-   Compresión.

-   Conversión de formatos.

**Ejemplos**

-   TLS

-   SSL (obsoleto)

-   JPEG

-   PNG

-   MP3

-   UTF-8

**Ataques**

-   Certificados falsos.

-   Ataques contra cifrados débiles.

-   Interceptación si no se usa HTTPS.

**Defensa**

-   TLS actualizado.

-   Certificados válidos.

-   Algoritmos modernos.

-   Gestión adecuada de certificados.

**8. Capa 7 -- Aplicación**

**Función**

Es la capa con la que interactúa directamente el usuario.

Aquí funcionan las aplicaciones y servicios.

**Protocolos**

-   HTTP

-   HTTPS

-   FTP

-   SMTP

-   POP3

-   IMAP

-   DNS

**Ejemplos**

-   Navegador web.

-   Correo electrónico.

-   WhatsApp.

-   Teams.

-   Navegación por Internet.

**Ataques**

-   SQL Injection.

-   Cross-Site Scripting (XSS).

-   Phishing.

-   Malware.

-   Ransomware.

**Defensa**

-   WAF.

-   Validación de entradas.

-   Antivirus/EDR.

-   Capacitación de usuarios.

-   Actualizaciones de software.

**9. Cuadro comparativo de las capas**

  ------------------------------------------------------------------------------
  **Capa**         **Función**            **Ejemplo**        **Dispositivo**
  ---------------- ---------------------- ------------------ -------------------
  7 Aplicación     Servicios al usuario   HTTP, DNS          Navegador

  6 Presentación   Cifrado y formato      TLS, JPEG          Sistema operativo

  5 Sesión         Mantiene conexiones    Inicio de sesión   Servidor

  4 Transporte     Puertos y entrega      TCP, UDP           Firewall

  3 Red            Direcciones IP         IPv4, ICMP         Router

  2 Enlace         Direcciones MAC        Ethernet, ARP      Switch

  1 Física         Transmisión de bits    Cable, fibra       Hub, cableado
  ------------------------------------------------------------------------------

**10. ¿Cómo puede atacar un ciberdelincuente cada capa?**

  -------------------------------------------------------------------------
  **Capa**   **Ataque**
  ---------- --------------------------------------------------------------
  1          Corte de cables, sabotaje físico

  2          ARP Spoofing, MAC Flooding

  3          Escaneo, IP Spoofing, ICMP Flood

  4          SYN Flood, fuerza bruta, escaneo de puertos

  5          Session Hijacking

  6          Ataques a TLS, certificados falsos

  7          SQL Injection, XSS, Phishing, Malware
  -------------------------------------------------------------------------

**11. ¿Cómo defender cada capa?**

  ------------------------------------------------------------------------
  **Capa**   **Defensa**
  ---------- -------------------------------------------------------------
  1          Seguridad física y redundancia

  2          Port Security, VLAN, DAI

  3          Firewall, ACL, IDS/IPS

  4          Firewall, MFA, Rate Limiting

  5          Expiración de sesiones, HTTPS

  6          TLS moderno, certificados válidos

  7          WAF, EDR, capacitación, actualizaciones
  ------------------------------------------------------------------------

**12. Aplicación práctica en un SOC**

Un analista SOC utiliza el Modelo OSI para ubicar rápidamente dónde ocurre un incidente.

**Ejemplo 1**

**Alerta:**

Miles de paquetes SYN al puerto 443.

**Capa afectada:** **4 -- Transporte**

**Posible incidente:** Ataque SYN Flood.

**Acciones del SOC:**

-   Revisar firewall.

-   Analizar origen del tráfico.

-   Aplicar reglas de mitigación.

-   Escalar si el servicio está degradado.

**Ejemplo 2**

**Alerta:**

ARP duplicadas detectadas en la VLAN de usuarios.

**Capa afectada:** **2 -- Enlace de Datos**

**Posible incidente:** ARP Spoofing.

**Acciones del SOC:**

-   Revisar la tabla ARP.

-   Identificar la MAC sospechosa.

-   Aislar el equipo comprometido.

-   Verificar la configuración del switch.

**Ejemplo 3**

**Alerta:**

Conexiones desde una IP desconocida a múltiples servidores internos.

**Capa afectada:** **3 -- Red**

**Posible incidente:** Reconocimiento o movimiento lateral.

**Acciones del SOC:**

-   Revisar logs del firewall.

-   Validar si la IP pertenece a un activo autorizado.

-   Correlacionar eventos en el SIEM.

-   Buscar actividad similar en otros equipos.

**Ejemplo 4**

**Alerta:**

Intentos repetidos de autenticación fallida en un portal web.

**Capas involucradas:** **5 (Sesión)** y **7 (Aplicación)**

**Posible incidente:** Fuerza bruta o intento de compromiso de cuentas.

**Acciones del SOC:**

-   Revisar registros de autenticación.

-   Bloquear la IP si corresponde.

-   Verificar si hubo accesos exitosos.

-   Comprobar si el usuario tiene MFA habilitado.

**13. Lo que esperan de un Analista SOC Nivel 1**

Cuando recibas una alerta, deberías preguntarte:

-   ¿En qué capa del Modelo OSI ocurre el incidente?

-   ¿Qué protocolo está involucrado?

-   ¿Qué dispositivo interviene?

-   ¿Qué tipo de ataque podría ser?

-   ¿Qué evidencia debo buscar?

-   ¿Qué controles de seguridad pueden mitigarlo?

-   ¿Debo escalar el incidente?

**Resumen**

-   **Capa 1 -- Física:** Transmite bits por el medio físico.

-   **Capa 2 -- Enlace:** Utiliza direcciones MAC para comunicar dispositivos de la misma red.

-   **Capa 3 -- Red:** Utiliza direcciones IP para enrutar paquetes entre redes.

-   **Capa 4 -- Transporte:** Gestiona puertos, TCP y UDP.

-   **Capa 5 -- Sesión:** Administra las sesiones entre aplicaciones.

-   **Capa 6 -- Presentación:** Cifra, descifra y da formato a los datos.

-   **Capa 7 -- Aplicación:** Proporciona los servicios con los que interactúan los usuarios.

**Conceptos clave para memorizar**

  --------------------------------------------------------------------------
  **Concepto**   **Debes recordar**
  -------------- -----------------------------------------------------------
  Capa 1         Bits y medio físico

  Capa 2         MAC, Switch, Ethernet, ARP

  Capa 3         IP, Router, ICMP

  Capa 4         TCP, UDP, Puertos

  Capa 5         Sesiones y autenticación

  Capa 6         Cifrado, TLS, formatos

  Capa 7         Aplicaciones y protocolos como HTTP, HTTPS y DNS
  --------------------------------------------------------------------------

**💡 Consejo como tu entrenador para un SOC**

No intentes memorizar el Modelo OSI como una lista de siete nombres. **Entiéndelo como una herramienta de investigación.** Cada vez que veas una alerta, pregúntate: *\"¿Qué capa está fallando?\"*.

Por ejemplo:

-   Un puerto 22 atacado → piensa en **Capa 4 (Transporte)**.

-   Una IP sospechosa → **Capa 3 (Red)**.

-   Un ataque de phishing → **Capa 7 (Aplicación)**.

-   Un ARP Spoofing → **Capa 2 (Enlace)**.

Los analistas SOC experimentados no recitan las capas de memoria: las usan para acotar rápidamente dónde buscar evidencias, qué logs revisar y qué controles aplicar. Ese enfoque es el que te permitirá investigar incidentes de forma metódica y eficiente.

**Evaluación -- Módulo 2: Modelo OSI**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Lee cada pregunta cuidadosamente y selecciona **una sola respuesta correcta**. No mires las respuestas hasta terminar el cuestionario.

**Pregunta 1**

¿Cuál es el principal objetivo del Modelo OSI?

**A)** Aumentar la velocidad de Internet.

**B)** Dividir la comunicación de red en capas con funciones específicas.

**C)** Reemplazar el protocolo TCP/IP.

**D)** Crear direcciones IP públicas.

**Pregunta 2**

¿En qué capa del Modelo OSI trabajan las direcciones IP?

**A)** Capa 2 -- Enlace de Datos

**B)** Capa 3 -- Red

**C)** Capa 4 -- Transporte

**D)** Capa 7 -- Aplicación

**Pregunta 3**

¿Cuál de los siguientes dispositivos trabaja principalmente en la **Capa 2**?

**A)** Router

**B)** Firewall

**C)** Switch

**D)** Servidor DNS

**Pregunta 4**

¿Qué protocolo pertenece a la **Capa 4 -- Transporte**?

**A)** HTTP

**B)** ARP

**C)** TCP

**D)** ICMP

**Pregunta 5**

¿Qué información utiliza un switch para enviar correctamente una trama dentro de una red local?

**A)** Dirección IP

**B)** Puerto TCP

**C)** Dirección MAC

**D)** Nombre del equipo

**Pregunta 6**

Recibes la siguiente alerta en un SOC:

Miles de paquetes SYN
Destino: Puerto 443

¿En qué capa del Modelo OSI ocurre principalmente este ataque?

**A)** Capa 2

**B)** Capa 3

**C)** Capa 4

**D)** Capa 7

**Pregunta 7**

¿Cuál de los siguientes ataques corresponde principalmente a la **Capa 2**?

**A)** SQL Injection

**B)** Phishing

**C)** ARP Spoofing

**D)** Fuerza Bruta SSH

**Pregunta 8**

¿Cuál de las siguientes opciones corresponde a la **Capa 6 -- Presentación**?

**A)** Cifrado y formato de datos.

**B)** Direccionamiento IP.

**C)** Cableado de red.

**D)** Puertos TCP.

**Pregunta 9**

¿Qué capa es la más cercana al usuario final?

**A)** Física

**B)** Transporte

**C)** Red

**D)** Aplicación

**Pregunta 10 (Caso práctico SOC)**

Como analista SOC recibes una alerta indicando que un usuario ingresó a un sitio web falso y entregó sus credenciales.

¿En qué capa del Modelo OSI ocurrió principalmente el ataque?

**A)** Capa 1 -- Física

**B)** Capa 3 -- Red

**C)** Capa 4 -- Transporte

**D)** Capa 7 -- Aplicación

**Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

El Modelo OSI fue creado para **dividir la comunicación de red en siete capas**, facilitando el diseño de redes, la interoperabilidad entre fabricantes y el diagnóstico de problemas.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

La **Capa 3 (Red)** es responsable del direccionamiento lógico mediante direcciones **IP** y del enrutamiento de paquetes entre distintas redes.

**Palabra clave para memorizar:**

**IP = Capa 3**

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

El **switch** trabaja principalmente en la **Capa 2**, utilizando direcciones **MAC** para enviar las tramas únicamente al dispositivo correcto dentro de una red local.

**Regla rápida:**

-   Switch → MAC → Capa 2

-   Router → IP → Capa 3

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

Los protocolos **TCP** y **UDP** pertenecen a la **Capa 4 (Transporte)** porque gestionan la entrega de datos entre aplicaciones y utilizan **puertos**.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

Los switches construyen una **tabla MAC** para saber por qué puerto físico enviar cada trama.

No utilizan direcciones IP para tomar esa decisión.

**Pregunta 6**

✅ **Respuesta correcta: C**

**Justificación**

Un ataque **SYN Flood** explota el funcionamiento del protocolo **TCP**, que pertenece a la **Capa 4 (Transporte)**.

Como analista SOC deberías pensar inmediatamente:

-   TCP

-   Puerto

-   Capa 4

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

El **ARP Spoofing** manipula el protocolo ARP y las direcciones MAC para interceptar tráfico dentro de la red local.

Es un ataque típico de la **Capa 2**.

**Pregunta 8**

✅ **Respuesta correcta: A**

**Justificación**

La **Capa 6 (Presentación)** se encarga de:

-   Cifrar.

-   Descifrar.

-   Comprimir.

-   Convertir formatos de datos.

Ejemplo:

-   TLS

-   JPEG

-   PNG

-   UTF-8

**Pregunta 9**

✅ **Respuesta correcta: D**

**Justificación**

La **Capa 7 (Aplicación)** es la que interactúa directamente con el usuario.

Aquí funcionan aplicaciones como:

-   Navegadores web.

-   Correo electrónico.

-   WhatsApp.

-   Teams.

-   Servicios web.

**Pregunta 10**

✅ **Respuesta correcta: D**

**Justificación**

El phishing ocurre principalmente en la **Capa 7 (Aplicación)** porque engaña al usuario mediante aplicaciones, sitios web o correos electrónicos para obtener información sensible.

**Resultado**

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Respuestas Correctas**   **Nivel**
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  **10/10**                  ⭐ Excelente. Ya piensas como un Analista SOC Junior. Puedes comenzar a analizar incidentes clasificándolos por capas del Modelo OSI.

  **8--9**                   🟢 Muy buen nivel. Solo necesitas reforzar algunos conceptos antes de avanzar.

  **6--7**                   🟡 Buen progreso. Repasa especialmente qué protocolos y dispositivos pertenecen a cada capa.

  **4--5**                   🟠 Aún hay conceptos por consolidar. Relee el módulo y vuelve a intentar el cuestionario.

  **0--3**                   🔴 Te recomiendo estudiar nuevamente el Modelo OSI antes de continuar con protocolos como TCP, UDP, HTTP y DNS.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
