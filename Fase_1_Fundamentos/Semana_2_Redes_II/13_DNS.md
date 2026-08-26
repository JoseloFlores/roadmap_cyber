**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Módulo 13 – DNS (Domain Name System)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Hasta ahora aprendiste que para comunicarse por Internet las
computadoras utilizan **direcciones IP**.

El problema es que las personas no recordamos fácilmente direcciones
como:

142.250.184.78

En cambio, sí recordamos nombres como:

www.google.com

Aquí es donde entra en juego **DNS**, conocido como **"la agenda
telefónica de Internet"**.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es DNS.

- Entender cómo funciona una consulta DNS.

- Diferenciar los tipos de servidores DNS.

- Conocer los principales registros DNS.

- Comprender cuándo DNS usa UDP y cuándo TCP.

- Entender la caché DNS.

- Identificar ataques relacionados con DNS.

- Interpretar eventos DNS en un SOC.

**1. ¿Qué es DNS?**

DNS significa:

**Domain Name System**

Es el sistema encargado de traducir nombres de dominio a direcciones IP.

Ejemplo:

www.google.com

↓

142.250.184.78

Sin DNS tendríamos que recordar la IP de cada sitio web.

**2. ¿Por qué existe DNS?**

Imagina que quieres llamar a un amigo.

No recuerdas su número de teléfono.

Entonces buscas su nombre en la agenda.

DNS hace exactamente lo mismo.

Nombre

↓

www.openai.com

↓

Consulta DNS

↓

Dirección IP

↓

104.xxx.xxx.xxx

**3. ¿Dónde trabaja DNS?**

DNS pertenece a la **Capa de Aplicación**.

**Modelo OSI**

7 Aplicación ← DNS

6 Presentación

5 Sesión

4 Transporte ← UDP/TCP

3 Red ← IP

2 Enlace

1 Física

**4. ¿Qué puerto utiliza DNS?**

Normalmente utiliza:

UDP 53

Pero también utiliza:

TCP 53

**¿Por qué dos protocolos?**

**UDP**

Se utiliza para:

- Consultas normales.

- Mayor velocidad.

- Menor consumo de recursos.

Ejemplo:

Cliente

↓

¿Dónde está www.google.com?

↓

Servidor DNS

↓

142.250.xxx.xxx

**TCP**

Se utiliza cuando:

- La respuesta es muy grande.

- Transferencia de zonas (Zone Transfer).

- Algunas respuestas con DNSSEC.

- La consulta UDP supera el tamaño permitido.

**5. ¿Cómo funciona una consulta DNS?**

Supongamos que escribes:

www.openai.com

Lo que realmente ocurre es:

**Paso 1**

El navegador pregunta:

¿Tengo la IP guardada en caché?

Si la respuesta es sí:

Se utiliza inmediatamente.

Si la respuesta es no:

Continúa.

**Paso 2**

El sistema operativo consulta su caché DNS.

**Paso 3**

Pregunta al servidor DNS configurado (por ejemplo, el del router o el de
tu proveedor de Internet).

**Paso 4**

Si el servidor no conoce la respuesta, inicia una búsqueda recursiva.

**Paso 5**

Obtiene la IP.

**Paso 6**

La devuelve al navegador.

**Paso 7**

El navegador ya puede establecer la conexión HTTP o HTTPS.

**6. Tipos de servidores DNS**

**Resolver (Recursivo)**

Es el servidor al que consulta tu computadora.

Ejemplos:

- Google Public DNS.

- Cloudflare.

- El DNS de tu ISP.

Su trabajo consiste en buscar la respuesta por ti.

**Root Server**

Es el punto de partida.

No conoce la IP final.

Solo indica dónde encontrar el servidor del TLD.

**Servidor TLD**

TLD significa:

Top Level Domain.

Ejemplos:

.com

.org

.net

.ar

Este servidor indica dónde está el servidor autoritativo.

**Servidor Autoritativo**

Es quien posee la información oficial del dominio.

Ejemplo:

openai.com

↓

IP oficial

**7. Flujo completo de una resolución DNS**

Usuario

↓

Resolver DNS

↓

Root Server

↓

Servidor .com

↓

Servidor Autoritativo

↓

Dirección IP

↓

Resolver

↓

Usuario

**8. Registros DNS**

Los registros DNS son distintos tipos de información almacenada en un
dominio.

**Registro A**

Relaciona un dominio con una dirección IPv4.

Ejemplo:

www.ejemplo.com

↓

192.168.1.10

**Registro AAAA**

Hace lo mismo que el registro A, pero para IPv6.

**Registro CNAME**

Es un alias.

Ejemplo:

mail.ejemplo.com

↓

servidor01.ejemplo.com

**Registro MX**

Indica qué servidor recibe el correo electrónico del dominio.

**Registro NS**

Indica cuáles son los servidores DNS autoritativos.

**Registro TXT**

Permite almacenar información de texto.

Muy utilizado para:

- SPF.

- DKIM.

- Verificación de dominios.

**Registro PTR**

Hace la resolución inversa.

En lugar de:

Dominio → IP

Hace:

IP → Dominio

**9. ¿Qué es la caché DNS?**

Para no repetir consultas innecesarias, las respuestas se almacenan
temporalmente.

Ejemplo:

www.google.com

↓

IP obtenida

↓

Guardada durante un tiempo

↓

Próxima consulta mucho más rápida

**10. TTL (Time To Live)**

Cada registro DNS posee un tiempo de vida.

Ejemplo:

TTL

↓

3600 segundos

Después de ese tiempo, la información debe consultarse nuevamente.

**11. DNS en Wireshark**

Podrías observar:

Standard Query

www.openai.com

Y luego:

Standard Query Response

104.xxx.xxx.xxx

Esto indica una resolución DNS exitosa.

**12. DNS en un Firewall**

Ejemplo:

Origen:

192.168.10.15

↓

Destino:

Servidor DNS

↓

UDP 53

↓

Permitido

**13. DNS en un SIEM**

Un evento típico podría mostrar:

Equipo:

PC-VENTAS

↓

Consulta:

random-abcd1234.xyz

↓

Resultado:

NXDOMAIN

Como analista SOC deberías preguntarte:

- ¿Por qué ese equipo consulta dominios aleatorios?

- ¿Hay muchas consultas fallidas?

- ¿Ese patrón coincide con un algoritmo de generación de dominios (DGA)?

**14. ¿Cómo utilizan DNS los atacantes?**

**Ataque 1 – DNS Spoofing**

El atacante responde con una IP falsa antes que el servidor legítimo.

Ejemplo:

www.banco.com

↓

IP del atacante

El usuario cree estar en el sitio correcto.

**Ataque 2 – DNS Cache Poisoning**

El atacante modifica la caché DNS para que las futuras consultas
devuelvan direcciones falsas.

**Ataque 3 – DNS Amplification**

Aprovecha servidores DNS abiertos para amplificar un ataque DDoS.

El atacante envía una consulta pequeña con la IP de la víctima
falsificada.

El servidor responde con una respuesta mucho mayor hacia la víctima.

**Ataque 4 – DNS Tunneling**

Uno de los ataques más importantes para un SOC.

El atacante utiliza consultas DNS para transportar información.

Ejemplo:

usuario123.password.secreto.dominio-malicioso.com

A simple vista parece una consulta DNS.

En realidad puede contener datos robados.

**Ataque 5 – DGA (Domain Generation Algorithm)**

Mucho malware genera miles de dominios aleatorios como:

abc123xyz.com

↓

qwe456asd.net

↓

xrt998bbb.org

Solo uno necesita existir para contactar con el servidor C2.

**15. ¿Cómo defenderse?**

- Utilizar DNSSEC cuando sea posible.

- Bloquear servidores DNS abiertos.

- Monitorear consultas inusuales.

- Detectar dominios recién registrados.

- Analizar patrones de consultas.

- Implementar listas de bloqueo (Threat Intelligence).

- Registrar y revisar los logs DNS.

**16. Aplicación práctica en un SOC**

**Caso 1**

Log:

Consulta:

www.microsoft.com

↓

Respuesta válida

Interpretación:

Actividad normal.

**Caso 2**

Log:

10.000 consultas

↓

abc123.xyz

↓

xyz987.xyz

↓

asd456.xyz

Interpretación:

Posible malware utilizando un **DGA**.

**Caso 3**

Log:

Consulta:

login.banco.com.seguridad-maliciosa.xyz

Interpretación:

Posible **DNS Tunneling** o intento de engaño.

**Caso 4**

Log:

Dominio:

nuevo-update-security.xyz

↓

Registrado hace 24 horas

↓

500 consultas

Interpretación:

Posible infraestructura de phishing o servidor de Comando y Control
(C2).

**17. DNS vs HTTP vs HTTPS**

| **Característica** | **DNS**               | **HTTP**               | **HTTPS**                              |
|--------------------|-----------------------|------------------------|----------------------------------------|
| Función            | Resolver nombres      | Transferir páginas web | Transferir páginas web de forma segura |
| Puerto             | UDP/TCP 53            | TCP 80                 | TCP 443                                |
| Cifrado            | No (tradicionalmente) | No                     | Sí (TLS)                               |
| Capa OSI           | Aplicación            | Aplicación             | Aplicación                             |

**18. Lo que esperan de un Analista SOC Nivel 1**

Imagina que el SIEM genera esta alerta:

Equipo:

PC-RRHH

↓

4.500 consultas DNS

↓

30 minutos

↓

Dominios aleatorios

↓

Todos NXDOMAIN

Como analista no deberías pensar únicamente en un problema de red.

Debes formular hipótesis:

- ¿Se trata de malware con DGA?

- ¿El equipo está intentando contactar con un C2?

- ¿Hay otros equipos con el mismo comportamiento?

- ¿El EDR detectó procesos sospechosos?

- ¿Las consultas comenzaron después de ejecutar un archivo?

Ese razonamiento es el que se espera en un SOC.

**19. Resumen**

**DNS**

- Traduce nombres de dominio a direcciones IP.

- Trabaja en la **Capa de Aplicación**.

- Utiliza **UDP 53** para la mayoría de las consultas.

- Utiliza **TCP 53** para transferencias de zona y respuestas grandes.

**Registros más importantes**

- A

- AAAA

- CNAME

- MX

- NS

- TXT

- PTR

**Riesgos**

- DNS Spoofing.

- DNS Cache Poisoning.

- DNS Amplification.

- DNS Tunneling.

- DGA.

**🧠 Conceptos clave para memorizar**

| **Concepto**      | **Debes recordar**                            |
|-------------------|-----------------------------------------------|
| DNS               | Domain Name System.                           |
| Función           | Traducir nombres de dominio a direcciones IP. |
| Puerto principal  | UDP 53.                                       |
| Puerto secundario | TCP 53.                                       |
| Registro A        | Dominio → IPv4.                               |
| Registro AAAA     | Dominio → IPv6.                               |
| Registro MX       | Servidor de correo.                           |
| Registro NS       | Servidor autoritativo.                        |
| Registro TXT      | Información de texto (SPF, DKIM, etc.).       |
| Registro PTR      | Resolución inversa (IP → Dominio).            |
| TTL               | Tiempo que un registro permanece en caché.    |

**🎓 Consejo como tu instructor de SOC**

Si tuviera que elegir **los tres protocolos más importantes para un
Analista SOC**, serían:

1.  **DNS** → Permite detectar malware, phishing, DGA, DNS Tunneling y
    comunicaciones con servidores C2.

2.  **HTTPS/TLS** → Ayuda a analizar conexiones cifradas mediante
    metadatos y certificados.

3.  **HTTP** → Fundamental para interpretar ataques a aplicaciones web.

En investigaciones reales, es muy común reconstruir una línea de tiempo
como esta:

Consulta DNS sospechosa

↓

Conexión HTTPS al dominio resuelto

↓

Descarga de un archivo

↓

Ejecución del malware

↓

Comunicación periódica con un servidor C2

Entender cómo se relacionan **DNS**, **HTTPS** y **HTTP** te permitirá
seguir el recorrido de un incidente desde la primera resolución del
dominio hasta la actividad maliciosa posterior.

**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Evaluación – Módulo 13: DNS (Domain Name System)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material de estudio. Este cuestionario está diseñado con un nivel
similar al de una entrevista técnica para un **Analista SOC Nivel 1**.
Encontrarás preguntas teóricas y casos prácticos basados en situaciones
reales.

**Pregunta 1**

¿Qué significa la sigla **DNS**?

**A)** Data Network Service

**B)** Domain Name System

**C)** Digital Network Server

**D)** Domain Network Security

**Pregunta 2**

¿Cuál es la función principal de DNS?

**A)** Cifrar las comunicaciones entre cliente y servidor.

**B)** Traducir nombres de dominio en direcciones IP.

**C)** Asignar direcciones IP automáticamente.

**D)** Enviar correos electrónicos.

**Pregunta 3**

¿Cuál es el puerto utilizado normalmente por DNS para realizar
consultas?

**A)** TCP 80

**B)** TCP 443

**C)** UDP 53

**D)** TCP 22

**Pregunta 4**

¿En cuál de los siguientes casos DNS utiliza normalmente **TCP** en
lugar de UDP?

**A)** Para enviar un ping.

**B)** Para consultas HTTP.

**C)** Para transferencias de zona (Zone Transfer) o respuestas
demasiado grandes para UDP.

**D)** Nunca utiliza TCP.

**Pregunta 5**

¿Qué registro DNS relaciona un nombre de dominio con una dirección
**IPv4**?

**A)** MX

**B)** AAAA

**C)** A

**D)** PTR

**Pregunta 6**

¿Cuál es la función del registro **MX**?

**A)** Resolver direcciones IPv6.

**B)** Indicar el servidor responsable de recibir correos electrónicos
del dominio.

**C)** Almacenar texto para SPF o DKIM.

**D)** Resolver una IP hacia un nombre de dominio.

**Pregunta 7**

¿Qué representa el valor **TTL (Time To Live)** en un registro DNS?

**A)** El tiempo máximo que un paquete puede permanecer en Internet.

**B)** El tiempo que un registro puede permanecer almacenado en caché
antes de volver a consultarse.

**C)** El tiempo que tarda una consulta DNS en completarse.

**D)** El tiempo que tarda un servidor DNS en iniciar.

**Pregunta 8**

Como analista SOC observas el siguiente evento:

Equipo:

PC-VENTAS

↓

5.000 consultas DNS

↓

Dominios aleatorios

↓

Resultado:

NXDOMAIN

¿Cuál sería la hipótesis más probable?

**A)** Un usuario navegando normalmente.

**B)** Un posible malware utilizando un **DGA (Domain Generation
Algorithm)**.

**C)** Una actualización de Windows.

**D)** Un problema con el servidor DHCP.

**Pregunta 9**

¿Cuál de los siguientes ataques consiste en utilizar consultas DNS para
transportar información robada o establecer comunicaciones ocultas?

**A)** DNS Amplification.

**B)** DNS Tunneling.

**C)** ARP Spoofing.

**D)** SYN Flood.

**Pregunta 10 (Caso práctico SOC)**

Durante una investigación observas el siguiente patrón:

Consulta DNS

↓

Dominio recién registrado

↓

Conexión HTTPS

↓

Gran volumen de datos enviados

¿Cuál sería la hipótesis más razonable?

**A)** El usuario abrió un documento PDF.

**B)** Posible comunicación con un servidor de Comando y Control (C2) o
exfiltración de datos.

**C)** Un error en el servidor DHCP.

**D)** Un problema con la resolución ARP.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

DNS significa **Domain Name System**. Es el sistema encargado de
traducir nombres de dominio, como www.openai.com, en direcciones IP para
que los equipos puedan comunicarse.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

La función principal de DNS es convertir nombres fáciles de recordar en
direcciones IP que entienden las computadoras.

Ejemplo:

www.openai.com

↓

104.xxx.xxx.xxx

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

DNS utiliza principalmente el **puerto UDP 53**, ya que las consultas
suelen ser pequeñas y requieren rapidez.

**Memoriza:**

- DNS → **UDP 53**

- DNS también puede usar **TCP 53** en casos específicos.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

DNS utiliza **TCP** cuando:

- Se realiza una **transferencia de zona (Zone Transfer)**.

- La respuesta es demasiado grande para UDP.

- Algunas implementaciones con **DNSSEC** requieren TCP.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

El registro **A** asocia un nombre de dominio con una dirección
**IPv4**.

Ejemplo:

www.ejemplo.com

↓

192.168.1.10

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

El registro **MX (Mail Exchange)** indica qué servidor recibe el correo
electrónico para un dominio determinado.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

El **TTL (Time To Live)** define cuánto tiempo un registro DNS puede
permanecer almacenado en la caché antes de que deba realizarse una nueva
consulta.

Esto ayuda a reducir el tráfico y acelerar las respuestas.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

Miles de consultas a dominios aleatorios que terminan en **NXDOMAIN**
(dominio inexistente) son un comportamiento típico de malware que
utiliza un **DGA (Domain Generation Algorithm)** para intentar localizar
su servidor de Comando y Control (C2).

Como analista SOC deberías revisar:

- Si otros equipos muestran el mismo patrón.

- Qué proceso generó las consultas.

- Si hubo conexiones posteriores a algún dominio resuelto.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

El **DNS Tunneling** utiliza consultas y respuestas DNS para transportar
información o mantener comunicaciones ocultas entre un equipo
comprometido y un servidor remoto.

Es una técnica utilizada por algunos malware para:

- Exfiltrar datos.

- Evadir controles de seguridad.

- Comunicarse con un C2.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

La secuencia:

Consulta DNS

↓

Dominio recién registrado

↓

Conexión HTTPS

↓

Gran volumen de datos

es un patrón que merece una investigación inmediata.

No confirma por sí solo un incidente, pero podría indicar:

- Exfiltración de datos.

- Comunicación con un servidor C2.

- Descarga de malware.

- Infraestructura de phishing.

En un SOC, deberías complementar el análisis con:

- Reputación del dominio.

- Edad del dominio.

- Logs del proxy.

- Eventos del EDR.

- Historial de conexiones del equipo.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Dominas el funcionamiento de DNS y puedes identificar patrones de ataque relevantes para un SOC.                                                       |
| **8–9**                  | 🟢 **Muy buen nivel.** Comprendes la resolución DNS y los principales registros y amenazas.                                                                              |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los tipos de registros, el uso de UDP/TCP y ataques como DGA y DNS Tunneling.                                                               |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Revisa el flujo de resolución DNS y la función de los registros A, MX, NS, TXT y PTR.                                       |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** DNS es uno de los protocolos más importantes para un Analista SOC y aparece constantemente en investigaciones reales. |

**🧠 Preguntas rápidas de memorización**

Responde mentalmente en menos de **5 segundos**:

| **Pregunta**                                    | **Respuesta esperada**                        |
|-------------------------------------------------|-----------------------------------------------|
| ¿Qué significa DNS?                             | Domain Name System.                           |
| ¿Cuál es su función?                            | Traducir nombres de dominio a direcciones IP. |
| ¿Puerto principal de DNS?                       | UDP 53.                                       |
| ¿Cuándo usa TCP?                                | Transferencias de zona y respuestas grandes.  |
| ¿Qué hace un registro A?                        | Dominio → IPv4.                               |
| ¿Qué hace un registro AAAA?                     | Dominio → IPv6.                               |
| ¿Qué hace un registro MX?                       | Define el servidor de correo.                 |
| ¿Qué hace un registro PTR?                      | Resolución inversa (IP → dominio).            |
| ¿Qué significa TTL?                             | Tiempo que un registro permanece en caché.    |
| ¿Qué ataque utiliza DNS para transportar datos? | DNS Tunneling.                                |

Muchos ataques modernos dejan sus primeras evidencias en los registros
DNS, incluso antes de que se establezca una conexión HTTP o HTTPS.

Hasta este punto ya has construido una base sólida en:

- ✅ Direcciones IP públicas y privadas.

- ✅ Modelo OSI.

- ✅ Modelo TCP/IP.

- ✅ Máscaras y subredes.

- ✅ Gateway.

- ✅ NAT.

- ✅ TCP y UDP.

- ✅ Puertos.

- ✅ DHCP.

- ✅ HTTP y HTTPS.

- ✅ DNS.

Esa base será la que utilizarás cuando empieces a analizar tráfico con
herramientas como **Wireshark**, **Zeek**, **Suricata**, **Splunk** o
**Microsoft Sentinel**, y cuando pases a la siguiente etapa de tu
formación centrada en **Linux** y el análisis de incidentes desde la
línea de comandos.
