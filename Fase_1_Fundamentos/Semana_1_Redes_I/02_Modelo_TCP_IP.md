**Módulo de Estudio <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Módulo 3 - Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es el Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

-   Conocer sus cuatro capas y su función.

-   Entender la diferencia entre <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

-   Identificar los protocolos más importantes de cada capa.

-   Comprender cómo un atacante puede aprovechar cada capa.

-   Saber cómo defenderlas.

-   Aplicar este conocimiento en el trabajo diario de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es el Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?**

El **Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> (Transmission Control Protocol / Internet Protocol)** es el conjunto de protocolos que permite que Internet funcione.

A diferencia del Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>, que es un modelo teórico para comprender cómo viajan los datos, **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> es el modelo que realmente utilizan las redes modernas**, incluida Internet.

Cada vez que:

-   Navegas por una página web.

-   Envías un correo electrónico.

-   Miras un video en YouTube.

-   Usas WhatsApp.

-   Descargas un archivo.

Estás utilizando el modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**¿Por qué es importante para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

La mayoría de los logs, alertas y herramientas de seguridad están basados en protocolos <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

Cuando un analista revisa:

-   <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>

-   Firewall

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>

-   <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>

-   <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>

está analizando tráfico <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

Por eso, dominar este modelo es fundamental.

**Las 4 capas del Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**

4 Aplicación
3 Transporte
2 Internet
1 Acceso a la Red

Una forma sencilla de recordarlas es:

**Acceso → Internet → Transporte → Aplicación**

**Diferencia con el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**

<a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> tiene **7 capas**.

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> tiene **4 capas**.

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> agrupa varias capas del <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

  -----------------------------------------------------------------------
  **Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**                   **Equivale en <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**
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

-   Direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>

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

-   <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>

**Analogía**

Es como una calle dentro de un barrio.

Los vecinos pueden comunicarse entre ellos.

**Ataques**

**<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing**

El atacante se hace pasar por el router.

Consecuencia:

Intercepción del tráfico.

**<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> Flooding**

Satura la tabla <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> del switch.

**Rogue Access Point**

El atacante instala un punto de acceso Wi-Fi falso para engañar a los usuarios.

**Defensa**

-   <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a>

-   <a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>

-   Dynamic <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Inspection

-   <a href="../../GLOSARIO.md#802-1x" target="_blank">802.1X</a>

-   Redes Wi-Fi seguras (WPA2/WPA3)

**3. Capa 2 -- Internet**

**Función**

Es responsable del direccionamiento y del enrutamiento entre redes.

Aquí aparecen las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**Protocolos**

-   IPv4

-   IPv6

-   <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>

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

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Spoofing**

El atacante falsifica una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**<a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> Flood**

Envía enormes cantidades de paquetes <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> para afectar la disponibilidad de un servicio.

**Defensa**

-   Firewalls

-   ACL

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>

-   Segmentación de red

-   Filtrado de tráfico sospechoso

**4. Capa 3 -- Transporte**

**Función**

Controla cómo se envían los datos entre <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> aplicaciones.

Aquí aparecen los puertos.

**Protocolos**

-   <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

-   <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

Características:

-   Orientado a conexión.

-   Confirma la recepción de los datos.

-   Reenvía paquetes perdidos.

-   Más lento pero más confiable.

Ejemplos:

-   <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

-   <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

-   <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

-   <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

Características:

-   No confirma la recepción.

-   Más rápido.

-   Menor sobrecarga.

-   Se utiliza cuando la velocidad es más importante que la confiabilidad.

Ejemplos:

-   Streaming

-   Videollamadas

-   Juegos online

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> (consultas)

**Ataques**

-   SYN Flood

-   Escaneo de puertos

-   Fuerza bruta

-   <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood

**Defensa**

-   Firewall

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>

-   Rate Limiting

-   <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>

-   Cierre de puertos innecesarios

**5. Capa 4 -- Aplicación**

**Función**

Es donde trabajan las aplicaciones que utilizan los usuarios.

Aquí aparecen la mayoría de los protocolos conocidos.

**Protocolos**

-   <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

-   <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

-   <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

-   <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

-   <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>

-   POP3

-   IMAP

-   <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

-   NTP

**Ejemplos**

-   Google Chrome

-   Microsoft Outlook

-   WhatsApp

-   Teams

-   Navegadores

-   Clientes <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

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

-   <a href="../../GLOSARIO.md#waf" target="_blank">WAF</a>

-   Antivirus

-   <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>

-   Capacitación

-   Actualizaciones

-   Validación de entradas

**6. Cuadro comparativo de las capas**

  --------------------------------------------------------------------------------------------------------------------
  **Capa <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**   **Función**                       **Protocolos**                     **Dispositivos**
  ----------------- --------------------------------- ---------------------------------- -----------------------------
  Aplicación        Servicios al usuario              <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>, <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>, <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>   Navegador, servidor web

  Transporte        Comunicación extremo a extremo    <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>, <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>                           Firewall, sistema operativo

  Internet          Direccionamiento y enrutamiento   IPv4, IPv6, <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>                   Router

  Acceso a la Red   Comunicación física y local       Ethernet, Wi-Fi, <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>               Switch, NIC
  --------------------------------------------------------------------------------------------------------------------

**7. Comparación entre <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**

  -----------------------------------------------------------------------
  **Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**                        **Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**
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

  Transporte           SYN Flood, Fuerza Bruta, <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood

  Internet             Escaneo, <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Spoofing, <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> Flood

  Acceso a la Red      <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing, <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> Flooding, Rogue AP
  -----------------------------------------------------------------------

**9. ¿Cómo defender cada capa?**

  -----------------------------------------------------------------------
  **Capa**                **Defensa**
  ----------------------- -----------------------------------------------
  Aplicación              <a href="../../GLOSARIO.md#waf" target="_blank">WAF</a>, <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>, Actualizaciones, <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>

  Transporte              Firewall, <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>, Rate Limiting

  Internet                ACL, Firewalls, Segmentación

  Acceso a la Red         <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a>, <a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>, WPA3
  -----------------------------------------------------------------------

**10. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Ejemplo 1**

**Alerta**

Puerto 22

2000 intentos <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

**Capa afectada**

Transporte

**Posible ataque**

Fuerza Bruta

**Acciones <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

-   Revisar logs.

-   Verificar origen.

-   Bloquear <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> si corresponde.

-   Confirmar si hubo autenticaciones exitosas.

**Ejemplo 2**

**Alerta**

192.168.1.15

↓

8.8.8.8

Miles de consultas <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>.

**Capa**

Internet

**Posible incidente**

<a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> Flood o reconocimiento.

**Ejemplo 3**

**Alerta**

<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> duplicadas

**Capa**

Acceso a la Red

**Posible incidente**

<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing.

**Ejemplo 4**

**Alerta**

Usuario descarga un archivo malicioso desde una página web.

**Capa**

Aplicación

**Posible incidente**

Malware.

**11. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando revises una alerta debes preguntarte:

-   ¿Qué protocolo está involucrado?

-   ¿En qué capa <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> ocurre el problema?

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

-   <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>.

-   <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>.

**Internet**

-   Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

-   Enrutamiento.

-   IPv4.

-   IPv6.

-   <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>.

**Transporte**

-   <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

-   <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

-   Puertos.

-   Comunicación entre aplicaciones.

**Aplicación**

-   <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

-   <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

-   <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>.

-   <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

-   <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>.

-   Servicios utilizados por el usuario.

**13. Conceptos clave para memorizar**

  -----------------------------------------------------------------------
  **Concepto**              **Debes recordar**
  ------------------------- ---------------------------------------------
  Acceso a la Red           <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>, Ethernet, Wi-Fi, <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>

  Internet                  <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, Router, <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>

  Transporte                <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>, <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>, Puertos

  Aplicación                <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>, <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>
  -----------------------------------------------------------------------

**🎯 Relación entre <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública, <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**

Hasta ahora ya conoces tres conceptos fundamentales. Es importante que los conectes mentalmente:

Internet
│
<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública (Capa Internet / Capa 3 <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>)
│
┌───────────┐
│ Router │
└───────────┘
│
─────────────────────────
Red Local (<a href="../../GLOSARIO.md#lan" target="_blank">LAN</a>)
─────────────────────────
│ │ │
PC 1 PC 2 Servidor
192.168.1.10 192.168.1.20 192.168.1.30
(<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>) (<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>) (<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>)

Cuando un usuario abre [**https://www.google.com**](https://www.google.com) ocurre, de forma simplificada, lo siguiente:

1.  **Aplicación:** el navegador genera una solicitud <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

2.  **Transporte:** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> establece una conexión usando el puerto 443.

3.  **Internet:** el paquete recibe una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen y una de destino para poder ser enrutado.

4.  **Acceso a la Red:** el paquete se convierte en una trama Ethernet o Wi-Fi y viaja por la red local hasta el router.

Este proceso ocurre en milisegundos y se repite miles de veces por segundo.

**💡 Consejo como tu entrenador para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

No estudies el Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de memoria. **Aprende a relacionarlo con los logs que verás todos los días.**

Cuando abras un registro en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> o en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>, intenta identificar inmediatamente:

-   **¿Hay una dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>?** → Piensa en **Acceso a la Red**.

-   **¿Hay direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?** → Piensa en **Internet**.

-   **¿Hay puertos <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> o <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?** → Piensa en **Transporte**.

-   **¿Aparecen <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> o <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>?** → Piensa en **Aplicación**.

Ese ejercicio mental hará que, con el tiempo, puedas interpretar una alerta en segundos y decidir qué evidencias revisar primero, una habilidad esencial para un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**Evaluación -- Módulo 3: Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Al finalizar, revisa las respuestas y sus justificaciones.

**Pregunta 1**

¿Cuál es la principal diferencia entre el Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y el Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>?

**A)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> tiene 7 capas y <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> tiene 4.

**B)** <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> es un modelo teórico y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> es el modelo utilizado en Internet.

**C)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> solo funciona en redes privadas.

**D)** <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> reemplazó completamente a <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**Pregunta 2**

¿Cuántas capas tiene el Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

**A)** 3

**B)** 4

**C)** 5

**D)** 7

**Pregunta 3**

¿En qué capa del Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> trabajan las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

**A)** Acceso a la Red

**B)** Transporte

**C)** Internet

**D)** Aplicación

**Pregunta 4**

¿Cuál de los siguientes protocolos pertenece a la capa **Transporte**?

**A)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

**B)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

**C)** <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>

**D)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>

**Pregunta 5**

¿Qué protocolo pertenece a la capa **Aplicación**?

**A)** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

**B)** Ethernet

**C)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

**D)** IPv4

**Pregunta 6**

¿Cuál es la principal diferencia entre **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** y **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**?

**A)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> utiliza direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> utiliza direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**B)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> es orientado a conexión y confirma la recepción de los datos; <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> prioriza la velocidad y no confirma la entrega.

**C)** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> solo funciona en Internet y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> solo en redes locales.

**D)** No existe ninguna diferencia importante.

**Pregunta 7**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> recibes la siguiente alerta:

Se detectaron miles de paquetes <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> provenientes de una misma dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

¿En qué capa del Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> ocurre principalmente este incidente?

**A)** Aplicación

**B)** Transporte

**C)** Internet

**D)** Acceso a la Red

**Pregunta 8**

¿Cuál de los siguientes ataques corresponde principalmente a la capa **Acceso a la Red**?

**A)** SQL Injection

**B)** Phishing

**C)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing

**D)** Fuerza Bruta <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

**Pregunta 9**

¿Qué protocolo se utiliza normalmente para navegar de forma segura por Internet?

**A)** <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

**B)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

**C)** <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

**D)** <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

Un usuario recibe un correo electrónico falso, hace clic en un enlace e ingresa sus credenciales en una página idéntica a la del banco.

¿En qué capa del Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> ocurre principalmente el ataque?

**A)** Acceso a la Red

**B)** Internet

**C)** Transporte

**D)** Aplicación

**Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

El **Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>** fue creado como un modelo de referencia para comprender cómo se comunican las redes.

El **Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>** es el que realmente utilizan Internet y la mayoría de las redes actuales.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

El Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> tiene **4 capas**:

1.  Acceso a la Red

2.  Internet

3.  Transporte

4.  Aplicación

**Consejo para el examen:**

<a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> = **7 capas**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> = **4 capas**

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

La capa **Internet** se encarga del direccionamiento mediante **IPv4** e **IPv6** y del enrutamiento entre redes.

**Palabra clave:**

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> = Capa Internet**

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

Los protocolos principales de la capa **Transporte** son:

-   <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

-   <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

Son responsables de la comunicación entre aplicaciones y utilizan **puertos**.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> pertenece a la capa **Aplicación**.

También pertenecen:

-   <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

-   <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

-   <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

-   <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>

-   IMAP

-   POP3

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>:

-   Establece una conexión.

-   Confirma la recepción.

-   Reenvía paquetes perdidos.

-   Es más confiable.

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>:

-   No establece conexión.

-   No confirma la recepción.

-   Es más rápido.

-   Se utiliza cuando la velocidad es prioritaria, como en videollamadas o juegos en línea.

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

El protocolo **<a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>** pertenece a la capa **Internet**.

Un gran volumen de paquetes <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> puede indicar un ataque como un **<a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a> Flood** o una actividad de reconocimiento.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación**

El **<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing** manipula las direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> y el protocolo <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> para interceptar el tráfico en una red local.

Por eso corresponde a la capa **Acceso a la Red**.

**Pregunta 9**

✅ **Respuesta correcta: C**

**Justificación**

**<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>** utiliza cifrado (<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>) para proteger la comunicación entre el navegador y el servidor.

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
  **10/10**                  ⭐ Excelente. Ya comienzas a relacionar protocolos, capas y tipos de ataque como lo hace un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Junior.

  **8--9**                   🟢 Muy buen nivel. Solo necesitas afianzar algunos conceptos antes de pasar al siguiente tema.

  **6--7**                   🟡 Buen progreso. Repasa especialmente la diferencia entre las capas y los protocolos que pertenecen a cada una.

  **4--5**                   🟠 Aún hay conceptos por reforzar. Relee el módulo y vuelve a realizar el cuestionario.

  **0--3**                   🔴 Es recomendable repasar el Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> antes de avanzar a protocolos específicos como <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> o <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.
  ---------------------------------------------------------------------------------------------------------------------------------------------
