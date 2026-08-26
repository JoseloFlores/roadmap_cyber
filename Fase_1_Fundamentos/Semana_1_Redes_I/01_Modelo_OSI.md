**Módulo de Estudio <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Módulo 1 - Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> (Open Systems Interconnection)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

-   Conocer las siete capas y su función.

-   Identificar dispositivos y protocolos en cada capa.

-   Entender cómo un atacante puede aprovechar cada capa.

-   Saber cómo defenderlas.

-   Aplicar estos conocimientos al trabajo diario de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>?**

El **Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> (Open Systems Interconnection)** es un modelo teórico que divide la comunicación entre dispositivos en **7 capas**.

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

Cuando ocurre un incidente, el analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> debe identificar:

-   ¿En qué capa ocurre el problema?

-   ¿Qué protocolo está involucrado?

-   ¿Qué dispositivo participa?

-   ¿Qué evidencia buscar?

Pensar por capas ayuda a investigar con orden y rapidez.

**Las 7 capas del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**

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

Aquí no existen direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> ni puertos.

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

-   CCTV (Circuito Cerrado de Televisión).

-   Armarios de comunicaciones cerrados.

-   Redundancia de enlaces.

-   Protección del cableado.

**3. Capa 2 -- Enlace de Datos**

**Función**

Permite que <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> dispositivos conectados a la misma red local se comuniquen correctamente.

Aquí aparecen las **direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>**.

**¿Qué es una <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>?**

Es el identificador físico de una tarjeta de red.

Ejemplo:

00:1A:2B:3C:4D:5E

**Protocolos**

-   Ethernet

-   <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>

-   <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a> (802.1Q)

**Dispositivos**

-   Switch

**Ataques**

**<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing**

El atacante engaña a otros equipos para hacerse pasar por el router.

Resultado:

Puede interceptar el tráfico (Man-in-the-Middle).

**<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> Flooding**

El atacante llena la tabla <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> del switch.

Consecuencia:

El switch comienza a comportarse como un hub y envía tráfico a todos los puertos.

**Defensa**

-   <a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>.

-   Dynamic <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Inspection.

-   <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a>.

-   <a href="../../GLOSARIO.md#802-1x" target="_blank">802.1X</a>.

-   Configuración segura del switch.

**4. Capa 3 -- Red**

**Función**

Aquí aparecen las **direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**.

Esta capa decide por dónde viajarán los paquetes entre diferentes redes.

**Protocolos**

-   IPv4

-   IPv6

-   <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>

-   IPSec

**Dispositivos**

-   Router

-   Firewall de capa 3

**Ejemplo**

192.168.1.20 → Router → 8.8.8.8

**Ataques**

-   Escaneo de red.

-   <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Spoofing.

-   <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> Flood.

-   Reconocimiento.

**Defensa**

-   Firewalls.

-   ACL (Lista de Control de Acceso, o Access Control List).

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a> (Sistema de Detección de Intrusiones) y un <a href="../../GLOSARIO.md#ips" target="_blank">IPS</a> (Sistema de Prevención de Intrusiones).

-   Segmentación.

-   Filtrado <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> cuando corresponda.

**5. Capa 4 -- Transporte**

**Función**

Controla cómo llegan los datos.

Aquí aparecen los **puertos**.

**Protocolos**

-   <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

-   <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

**Ejemplos**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> → Puerto 80

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> → Puerto 443

<a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> → Puerto 22

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> → Puerto 53

*(Nota los numeros de puertos para cada protocolo son convenciones)*

**Funciones**

-   Control de errores.

-   Confirmación de recepción (<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>).

-   Reenvío de paquetes.

-   Control de flujo.

**Ataques**

-   SYN Flood.

-   Escaneo de puertos.

-   Fuerza bruta sobre <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> o RDP.

**Defensa**

-   Firewall.

-   Rate limiting.

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>.

-   <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>.

-   Cierre de puertos innecesarios.

**6. Capa 5 -- Sesión**

**Función**

Administra el inicio, mantenimiento y cierre de una comunicación entre <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> aplicaciones.

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

-   <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

-   <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>.

**7. Capa 6 -- Presentación**

**Función**

Se encarga del formato de los datos.

Realiza tareas como:

-   Cifrado.

-   Descifrado.

-   Compresión.

-   Conversión de formatos.

**Ejemplos**

-   <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>

-   <a href="../../GLOSARIO.md#ssl" target="_blank">SSL</a> (obsoleto)

-   JPEG

-   PNG

-   MP3

-   UTF-8

**Ataques**

-   Certificados falsos.

-   Ataques contra cifrados débiles.

-   Interceptación si no se usa <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**Defensa**

-   <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> actualizado.

-   Certificados válidos.

-   Algoritmos modernos.

-   Gestión adecuada de certificados.

**8. Capa 7 -- Aplicación**

**Función**

Es la capa con la que interactúa directamente el usuario.

Aquí funcionan las aplicaciones y servicios.

**Protocolos**

-   <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

-   <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

-   <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

-   <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>

-   POP3

-   IMAP

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

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

-   <a href="../../GLOSARIO.md#waf" target="_blank">WAF</a>.

-   Validación de entradas.

-   Antivirus/<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>.

-   Capacitación de usuarios.

-   Actualizaciones de software.

**9. Cuadro comparativo de las capas**

  ------------------------------------------------------------------------------
  **Capa**         **Función**            **Ejemplo**        **Dispositivo**
  ---------------- ---------------------- ------------------ -------------------
  7 Aplicación     Servicios al usuario   <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>          Navegador

  6 Presentación   Cifrado y formato      <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>, JPEG          Sistema operativo

  5 Sesión         Mantiene conexiones    Inicio de sesión   Servidor

  4 Transporte     Puertos y entrega      <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>, <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>           Firewall

  3 Red            Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>         IPv4, <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>         Router

  2 Enlace         Direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>        Ethernet, <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>      Switch

  1 Física         Transmisión de bits    Cable, fibra       Hub, cableado
  ------------------------------------------------------------------------------

**10. ¿Cómo puede atacar un ciberdelincuente cada capa?**

  -------------------------------------------------------------------------
  **Capa**   **Ataque**
  ---------- --------------------------------------------------------------
  1          Corte de cables, sabotaje físico

  2          <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing, <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> Flooding

  3          Escaneo, <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Spoofing, <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> Flood

  4          SYN Flood, fuerza bruta, escaneo de puertos

  5          Session Hijacking

  6          Ataques a <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>, certificados falsos

  7          SQL Injection, XSS, Phishing, Malware
  -------------------------------------------------------------------------

**11. ¿Cómo defender cada capa?**

  ------------------------------------------------------------------------
  **Capa**   **Defensa**
  ---------- -------------------------------------------------------------
  1          Seguridad física y redundancia

  2          <a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>, <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a>, DAI

  3          Firewall, ACL, <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>

  4          Firewall, <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>, Rate Limiting

  5          Expiración de sesiones, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

  6          <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> moderno, certificados válidos

  7          <a href="../../GLOSARIO.md#waf" target="_blank">WAF</a>, <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>, capacitación, actualizaciones
  ------------------------------------------------------------------------

**12. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Un analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> utiliza el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> para ubicar rápidamente dónde ocurre un incidente.

**Ejemplo 1**

**Alerta:**

Miles de paquetes SYN al puerto 443.

**Capa afectada:** **4 -- Transporte**

**Posible incidente:** Ataque SYN Flood.

**Acciones del <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>:**

-   Revisar firewall.

-   Analizar origen del tráfico.

-   Aplicar reglas de mitigación.

-   Escalar si el servicio está degradado.

**Ejemplo 2**

**Alerta:**

<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> duplicadas detectadas en la <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a> de usuarios.

**Capa afectada:** **2 -- Enlace de Datos**

**Posible incidente:** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing.

**Acciones del <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>:**

-   Revisar la tabla <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>.

-   Identificar la <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> sospechosa.

-   Aislar el equipo comprometido.

-   Verificar la configuración del switch.

**Ejemplo 3**

**Alerta:**

Conexiones desde una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> desconocida a múltiples servidores internos.

**Capa afectada:** **3 -- Red**

**Posible incidente:** Reconocimiento o movimiento lateral.

**Acciones del <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>:**

-   Revisar logs del firewall.

-   Validar si la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pertenece a un activo autorizado.

-   Correlacionar eventos en el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

-   Buscar actividad similar en otros equipos.

**Ejemplo 4**

**Alerta:**

Intentos repetidos de autenticación fallida en un portal web.

**Capas involucradas:** **5 (Sesión)** y **7 (Aplicación)**

**Posible incidente:** Fuerza bruta o intento de compromiso de cuentas.

**Acciones del <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>:**

-   Revisar registros de autenticación.

-   Bloquear la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> si corresponde.

-   Verificar si hubo accesos exitosos.

-   Comprobar si el usuario tiene <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a> habilitado.

**13. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando recibas una alerta, deberías preguntarte:

-   ¿En qué capa del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> ocurre el incidente?

-   ¿Qué protocolo está involucrado?

-   ¿Qué dispositivo interviene?

-   ¿Qué tipo de ataque podría ser?

-   ¿Qué evidencia debo buscar?

-   ¿Qué controles de seguridad pueden mitigarlo?

-   ¿Debo escalar el incidente?

**Resumen**

-   **Capa 1 -- Física:** Transmite bits por el medio físico.

-   **Capa 2 -- Enlace:** Utiliza direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> para comunicar dispositivos de la misma red.

-   **Capa 3 -- Red:** Utiliza direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> para enrutar paquetes entre redes.

-   **Capa 4 -- Transporte:** Gestiona puertos, <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

-   **Capa 5 -- Sesión:** Administra las sesiones entre aplicaciones.

-   **Capa 6 -- Presentación:** Cifra, descifra y da formato a los datos.

-   **Capa 7 -- Aplicación:** Proporciona los servicios con los que interactúan los usuarios.

**Conceptos clave para memorizar**

  --------------------------------------------------------------------------
  **Concepto**   **Debes recordar**
  -------------- -----------------------------------------------------------
  Capa 1         Bits y medio físico

  Capa 2         <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>, Switch, Ethernet, <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>

  Capa 3         <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, Router, <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>

  Capa 4         <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>, <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>, Puertos

  Capa 5         Sesiones y autenticación

  Capa 6         Cifrado, <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>, formatos

  Capa 7         Aplicaciones y protocolos como <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>
  --------------------------------------------------------------------------

**💡 Consejo como tu entrenador para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

No intentes memorizar el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> como una lista de siete nombres. **Entiéndelo como una herramienta de investigación.** Cada vez que veas una alerta, pregúntate: *\"¿Qué capa está fallando?\"*.

Por ejemplo:

-   Un puerto 22 atacado → piensa en **Capa 4 (Transporte)**.

-   Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> sospechosa → **Capa 3 (Red)**.

-   Un ataque de phishing → **Capa 7 (Aplicación)**.

-   Un <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing → **Capa 2 (Enlace)**.

Los analistas <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> experimentados no recitan las capas de memoria: las usan para acotar rápidamente dónde buscar evidencias, qué logs revisar y qué controles aplicar. Ese enfoque es el que te permitirá investigar incidentes de forma metódica y eficiente.

**Evaluación -- Módulo 2: Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Lee cada pregunta cuidadosamente y selecciona **una sola respuesta correcta**. No mires las respuestas hasta terminar el cuestionario.

**Pregunta 1**

¿Cuál es el principal objetivo del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>?

**A)** Aumentar la velocidad de Internet.

**B)** Dividir la comunicación de red en capas con funciones específicas.

**C)** Reemplazar el protocolo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**D)** Crear direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas.

**Pregunta 2**

¿En qué capa del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> trabajan las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

**A)** Capa 2 -- Enlace de Datos

**B)** Capa 3 -- Red

**C)** Capa 4 -- Transporte

**D)** Capa 7 -- Aplicación

**Pregunta 3**

¿Cuál de los siguientes dispositivos trabaja principalmente en la **Capa 2**?

**A)** Router

**B)** Firewall

**C)** Switch

**D)** Servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

**Pregunta 4**

¿Qué protocolo pertenece a la **Capa 4 -- Transporte**?

**A)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

**B)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>

**C)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

**D)** <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>

**Pregunta 5**

¿Qué información utiliza un switch para enviar correctamente una trama dentro de una red local?

**A)** Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

**B)** Puerto <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

**C)** Dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>

**D)** Nombre del equipo

**Pregunta 6**

Recibes la siguiente alerta en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>:

Miles de paquetes SYN
Destino: Puerto 443

¿En qué capa del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> ocurre principalmente este ataque?

**A)** Capa 2

**B)** Capa 3

**C)** Capa 4

**D)** Capa 7

**Pregunta 7**

¿Cuál de los siguientes ataques corresponde principalmente a la **Capa 2**?

**A)** SQL Injection

**B)** Phishing

**C)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing

**D)** Fuerza Bruta <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

**Pregunta 8**

¿Cuál de las siguientes opciones corresponde a la **Capa 6 -- Presentación**?

**A)** Cifrado y formato de datos.

**B)** Direccionamiento <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**C)** Cableado de red.

**D)** Puertos <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**Pregunta 9**

¿Qué capa es la más cercana al usuario final?

**A)** Física

**B)** Transporte

**C)** Red

**D)** Aplicación

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> recibes una alerta indicando que un usuario ingresó a un sitio web falso y entregó sus credenciales.

¿En qué capa del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> ocurrió principalmente el ataque?

**A)** Capa 1 -- Física

**B)** Capa 3 -- Red

**C)** Capa 4 -- Transporte

**D)** Capa 7 -- Aplicación

**Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

El Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> fue creado para **dividir la comunicación de red en siete capas**, facilitando el diseño de redes, la interoperabilidad entre fabricantes y el diagnóstico de problemas.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

La **Capa 3 (Red)** es responsable del direccionamiento lógico mediante direcciones **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>** y del enrutamiento de paquetes entre distintas redes.

**Palabra clave para memorizar:**

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> = Capa 3**

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

El **switch** trabaja principalmente en la **Capa 2**, utilizando direcciones **<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>** para enviar las tramas únicamente al dispositivo correcto dentro de una red local.

**Regla rápida:**

-   Switch → <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> → Capa 2

-   Router → <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> → Capa 3

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

Los protocolos **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** y **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>** pertenecen a la **Capa 4 (Transporte)** porque gestionan la entrega de datos entre aplicaciones y utilizan **puertos**.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

Los switches construyen una **tabla <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>** para saber por qué puerto físico enviar cada trama.

No utilizan direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> para tomar esa decisión.

**Pregunta 6**

✅ **Respuesta correcta: C**

**Justificación**

Un ataque **SYN Flood** explota el funcionamiento del protocolo **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**, que pertenece a la **Capa 4 (Transporte)**.

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> deberías pensar inmediatamente:

-   <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

-   Puerto

-   Capa 4

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

El **<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing** manipula el protocolo <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> y las direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> para interceptar tráfico dentro de la red local.

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

-   <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>

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
  **10/10**                  ⭐ Excelente. Ya piensas como un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Junior. Puedes comenzar a analizar incidentes clasificándolos por capas del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

  **8--9**                   🟢 Muy buen nivel. Solo necesitas reforzar algunos conceptos antes de avanzar.

  **6--7**                   🟡 Buen progreso. Repasa especialmente qué protocolos y dispositivos pertenecen a cada capa.

  **4--5**                   🟠 Aún hay conceptos por consolidar. Relee el módulo y vuelve a intentar el cuestionario.

  **0--3**                   🔴 Te recomiendo estudiar nuevamente el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> antes de continuar con protocolos como <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>, <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>, <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
