**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Módulo 13 – <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> (Domain Name System)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Antes de comenzar**

Hasta ahora aprendiste que para comunicarse por Internet las
computadoras utilizan **direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**.

El problema es que las personas no recordamos fácilmente direcciones
como:

142.250.184.78

En cambio, sí recordamos nombres como:

www.google.com

Aquí es donde entra en juego **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**, conocido como **"la agenda
telefónica de Internet"**.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Entender cómo funciona una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Diferenciar los tipos de servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Conocer los principales registros <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Comprender cuándo <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> usa <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y cuándo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

- Entender la caché <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Identificar ataques relacionados con <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Interpretar eventos <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?**

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> significa:

**Domain Name System**

Es el sistema encargado de traducir nombres de dominio a direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

Ejemplo:

www.google.com

↓

142.250.184.78

Sin <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> tendríamos que recordar la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de cada sitio web.

**2. ¿Por qué existe <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?**

Imagina que quieres llamar a un amigo.

No recuerdas su número de teléfono.

Entonces buscas su nombre en la agenda.

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> hace exactamente lo mismo.

Nombre

↓

www.openai.com

↓

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

↓

Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

↓

104.xxx.xxx.xxx

**3. ¿Dónde trabaja <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?**

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> pertenece a la **Capa de Aplicación**.

**Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>**

7 Aplicación ← <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

6 Presentación

5 Sesión

4 Transporte ← <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

3 Red ← <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

2 Enlace

1 Física

**4. ¿Qué puerto utiliza <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?**

Normalmente utiliza:

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53

Pero también utiliza:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 53

**¿Por qué <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> protocolos?**

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

Se utiliza para:

- Consultas normales.

- Mayor velocidad.

- Menor consumo de recursos.

Ejemplo:

Cliente

↓

¿Dónde está www.google.com?

↓

Servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

↓

142.250.xxx.xxx

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

Se utiliza cuando:

- La respuesta es muy grande.

- Transferencia de zonas (Zone Transfer).

- Algunas respuestas con DNSSEC.

- La consulta <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> supera el tamaño permitido.

**5. ¿Cómo funciona una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?**

Supongamos que escribes:

www.openai.com

Lo que realmente ocurre es:

**Paso 1**

El navegador pregunta:

¿Tengo la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> guardada en caché?

Si la respuesta es sí:

Se utiliza inmediatamente.

Si la respuesta es no:

Continúa.

**Paso 2**

El sistema operativo consulta su caché <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**Paso 3**

Pregunta al servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> configurado (por ejemplo, el del router o el de
tu proveedor de Internet).

**Paso 4**

Si el servidor no conoce la respuesta, inicia una búsqueda recursiva.

**Paso 5**

Obtiene la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**Paso 6**

La devuelve al navegador.

**Paso 7**

El navegador ya puede establecer la conexión <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> o <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**6. Tipos de servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**

**Resolver (Recursivo)**

Es el servidor al que consulta tu computadora.

Ejemplos:

- Google Public <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Cloudflare.

- El <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> de tu ISP.

Su trabajo consiste en buscar la respuesta por ti.

**<a href="../../GLOSARIO.md#root" target="_blank">Root</a> Server**

Es el punto de partida.

No conoce la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> final.

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

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> oficial

**7. Flujo completo de una resolución <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**

Usuario

↓

Resolver <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

↓

<a href="../../GLOSARIO.md#root" target="_blank">Root</a> Server

↓

Servidor .com

↓

Servidor Autoritativo

↓

Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

↓

Resolver

↓

Usuario

**8. Registros <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**

Los registros <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> son distintos tipos de información almacenada en un
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

Indica cuáles son los servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> autoritativos.

**Registro TXT**

Permite almacenar información de texto.

Muy utilizado para:

- SPF.

- DKIM.

- Verificación de dominios.

**Registro PTR**

Hace la resolución inversa.

En lugar de:

Dominio → <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

Hace:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> → Dominio

**9. ¿Qué es la caché <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?**

Para no repetir consultas innecesarias, las respuestas se almacenan
temporalmente.

Ejemplo:

www.google.com

↓

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> obtenida

↓

Guardada durante un tiempo

↓

Próxima consulta mucho más rápida

**10. TTL (Time To Live)**

Cada registro <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> posee un tiempo de vida.

Ejemplo:

TTL

↓

3600 segundos

Después de ese tiempo, la información debe consultarse nuevamente.

**11. <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>**

Podrías observar:

Standard Query

www.openai.com

Y luego:

Standard Query Response

104.xxx.xxx.xxx

Esto indica una resolución <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> exitosa.

**12. <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en un Firewall**

Ejemplo:

Origen:

192.168.10.15

↓

Destino:

Servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53

↓

Permitido

**13. <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**

Un evento típico podría mostrar:

Equipo:

PC-VENTAS

↓

Consulta:

random-abcd1234.xyz

↓

Resultado:

NXDOMAIN

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> deberías preguntarte:

- ¿Por qué ese equipo consulta dominios aleatorios?

- ¿Hay muchas consultas fallidas?

- ¿Ese patrón coincide con un algoritmo de generación de dominios (DGA)?

**14. ¿Cómo utilizan <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> los atacantes?**

**Ataque 1 – <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Spoofing**

El atacante responde con una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> falsa antes que el servidor legítimo.

Ejemplo:

www.banco.com

↓

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> del atacante

El usuario cree estar en el sitio correcto.

**Ataque 2 – <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Cache Poisoning**

El atacante modifica la caché <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para que las futuras consultas
devuelvan direcciones falsas.

**Ataque 3 – <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification**

Aprovecha servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> abiertos para amplificar un ataque <a href="../../GLOSARIO.md#ddos" target="_blank">DDoS</a>.

El atacante envía una consulta pequeña con la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de la víctima
falsificada.

El servidor responde con una respuesta mucho mayor hacia la víctima.

**Ataque 4 – <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling**

Uno de los ataques más importantes para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

El atacante utiliza consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para transportar información.

Ejemplo:

usuario123.password.secreto.dominio-malicioso.com

A simple vista parece una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

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

- Bloquear servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> abiertos.

- Monitorear consultas inusuales.

- Detectar dominios recién registrados.

- Analizar patrones de consultas.

- Implementar listas de bloqueo (Threat Intelligence).

- Registrar y revisar los logs <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**16. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

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

Posible **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling** o intento de engaño.

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

**17. <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> vs <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> vs <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**

| **Característica** | **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**               | **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**               | **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**                              |
|--------------------|-----------------------|------------------------|----------------------------------------|
| Función            | Resolver nombres      | Transferir páginas web | Transferir páginas web de forma segura |
| Puerto             | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 53            | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80                 | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443                                |
| Cifrado            | No (tradicionalmente) | No                     | Sí (<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>)                               |
| Capa <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>           | Aplicación            | Aplicación             | Aplicación                             |

**18. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Imagina que el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> genera esta alerta:

Equipo:

PC-RRHH

↓

4.500 consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

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

- ¿El <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> detectó procesos sospechosos?

- ¿Las consultas comenzaron después de ejecutar un archivo?

Ese razonamiento es el que se espera en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**19. Resumen**

**<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**

- Traduce nombres de dominio a direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

- Trabaja en la **Capa de Aplicación**.

- Utiliza **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53** para la mayoría de las consultas.

- Utiliza **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 53** para transferencias de zona y respuestas grandes.

**Registros más importantes**

- A

- AAAA

- CNAME

- MX

- NS

- TXT

- PTR

**Riesgos**

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Spoofing.

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Cache Poisoning.

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification.

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling.

- DGA.

**🧠 Conceptos clave para memorizar**

| **Concepto**      | **Debes recordar**                            |
|-------------------|-----------------------------------------------|
| <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>               | Domain Name System.                           |
| Función           | Traducir nombres de dominio a direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>. |
| Puerto principal  | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53.                                       |
| Puerto secundario | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 53.                                       |
| Registro A        | Dominio → IPv4.                               |
| Registro AAAA     | Dominio → IPv6.                               |
| Registro MX       | Servidor de correo.                           |
| Registro NS       | Servidor autoritativo.                        |
| Registro TXT      | Información de texto (SPF, DKIM, etc.).       |
| Registro PTR      | Resolución inversa (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> → Dominio).            |
| TTL               | Tiempo que un registro permanece en caché.    |

**🎓 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Si tuviera que elegir **los tres protocolos más importantes para un
Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**, serían:

1.  **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>** → Permite detectar malware, phishing, DGA, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling y
    comunicaciones con servidores C2.

2.  **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>/<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>** → Ayuda a analizar conexiones cifradas mediante
    metadatos y certificados.

3.  **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>** → Fundamental para interpretar ataques a aplicaciones web.

En investigaciones reales, es muy común reconstruir una línea de tiempo
como esta:

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> sospechosa

↓

Conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> al dominio resuelto

↓

Descarga de un archivo

↓

Ejecución del malware

↓

Comunicación periódica con un servidor C2

Entender cómo se relacionan **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**, **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>** y **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>** te permitirá
seguir el recorrido de un incidente desde la primera resolución del
dominio hasta la actividad maliciosa posterior.

**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Evaluación – Módulo 13: <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> (Domain Name System)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material de estudio. Este cuestionario está diseñado con un nivel
similar al de una entrevista técnica para un **Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**.
Encontrarás preguntas teóricas y casos prácticos basados en situaciones
reales.

**Pregunta 1**

¿Qué significa la sigla **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**?

**A)** Data Network Service

**B)** Domain Name System

**C)** Digital Network Server

**D)** Domain Network Security

**Pregunta 2**

¿Cuál es la función principal de <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?

**A)** Cifrar las comunicaciones entre cliente y servidor.

**B)** Traducir nombres de dominio en direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**C)** Asignar direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> automáticamente.

**D)** Enviar correos electrónicos.

**Pregunta 3**

¿Cuál es el puerto utilizado normalmente por <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para realizar
consultas?

**A)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80

**B)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443

**C)** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53

**D)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 22

**Pregunta 4**

¿En cuál de los siguientes casos <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> utiliza normalmente **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** en
lugar de <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** Para enviar un ping.

**B)** Para consultas <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

**C)** Para transferencias de zona (Zone Transfer) o respuestas
demasiado grandes para <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

**D)** Nunca utiliza <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**Pregunta 5**

¿Qué registro <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> relaciona un nombre de dominio con una dirección
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

**D)** Resolver una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> hacia un nombre de dominio.

**Pregunta 7**

¿Qué representa el valor **TTL (Time To Live)** en un registro <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?

**A)** El tiempo máximo que un paquete puede permanecer en Internet.

**B)** El tiempo que un registro puede permanecer almacenado en caché
antes de volver a consultarse.

**C)** El tiempo que tarda una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en completarse.

**D)** El tiempo que tarda un servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en iniciar.

**Pregunta 8**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> observas el siguiente evento:

Equipo:

PC-VENTAS

↓

5.000 consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

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

**D)** Un problema con el servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**Pregunta 9**

¿Cuál de los siguientes ataques consiste en utilizar consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para
transportar información robada o establecer comunicaciones ocultas?

**A)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification.

**B)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling.

**C)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing.

**D)** SYN Flood.

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

Durante una investigación observas el siguiente patrón:

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

↓

Dominio recién registrado

↓

Conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

↓

Gran volumen de datos enviados

¿Cuál sería la hipótesis más razonable?

**A)** El usuario abrió un documento PDF.

**B)** Posible comunicación con un servidor de Comando y Control (C2) o
exfiltración de datos.

**C)** Un error en el servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**D)** Un problema con la resolución <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> significa **Domain Name System**. Es el sistema encargado de
traducir nombres de dominio, como www.openai.com, en direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> para
que los equipos puedan comunicarse.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

La función principal de <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> es convertir nombres fáciles de recordar en
direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> que entienden las computadoras.

Ejemplo:

www.openai.com

↓

104.xxx.xxx.xxx

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> utiliza principalmente el **puerto <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53**, ya que las consultas
suelen ser pequeñas y requieren rapidez.

**Memoriza:**

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> → **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53**

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> también puede usar **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 53** en casos específicos.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> utiliza **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** cuando:

- Se realiza una **transferencia de zona (Zone Transfer)**.

- La respuesta es demasiado grande para <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

- Algunas implementaciones con **DNSSEC** requieren <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

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

El **TTL (Time To Live)** define cuánto tiempo un registro <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> puede
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

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> deberías revisar:

- Si otros equipos muestran el mismo patrón.

- Qué proceso generó las consultas.

- Si hubo conexiones posteriores a algún dominio resuelto.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

El **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling** utiliza consultas y respuestas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para transportar
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

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

↓

Dominio recién registrado

↓

Conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

↓

Gran volumen de datos

es un patrón que merece una investigación inmediata.

No confirma por sí solo un incidente, pero podría indicar:

- Exfiltración de datos.

- Comunicación con un servidor C2.

- Descarga de malware.

- Infraestructura de phishing.

En un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, deberías complementar el análisis con:

- Reputación del dominio.

- Edad del dominio.

- Logs del proxy.

- Eventos del <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>.

- Historial de conexiones del equipo.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Dominas el funcionamiento de <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> y puedes identificar patrones de ataque relevantes para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.                                                       |
| **8–9**                  | 🟢 **Muy buen nivel.** Comprendes la resolución <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> y los principales registros y amenazas.                                                                              |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los tipos de registros, el uso de <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y ataques como DGA y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling.                                                               |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Revisa el flujo de resolución <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> y la función de los registros A, MX, NS, TXT y PTR.                                       |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> es uno de los protocolos más importantes para un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> y aparece constantemente en investigaciones reales. |

**🧠 Preguntas rápidas de memorización**

Responde mentalmente en menos de **5 segundos**:

| **Pregunta**                                    | **Respuesta esperada**                        |
|-------------------------------------------------|-----------------------------------------------|
| ¿Qué significa <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?                             | Domain Name System.                           |
| ¿Cuál es su función?                            | Traducir nombres de dominio a direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>. |
| ¿Puerto principal de <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>?                       | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53.                                       |
| ¿Cuándo usa <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>?                                | Transferencias de zona y respuestas grandes.  |
| ¿Qué hace un registro A?                        | Dominio → IPv4.                               |
| ¿Qué hace un registro AAAA?                     | Dominio → IPv6.                               |
| ¿Qué hace un registro MX?                       | Define el servidor de correo.                 |
| ¿Qué hace un registro PTR?                      | Resolución inversa (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> → dominio).            |
| ¿Qué significa TTL?                             | Tiempo que un registro permanece en caché.    |
| ¿Qué ataque utiliza <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para transportar datos? | <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling.                                |

Muchos ataques modernos dejan sus primeras evidencias en los registros
<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, incluso antes de que se establezca una conexión <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> o <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

Hasta este punto ya has construido una base sólida en:

- ✅ Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas y privadas.

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

- ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

- ✅ Máscaras y subredes.

- ✅ <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

- ✅ <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

- ✅ <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

- ✅ Puertos.

- ✅ <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

- ✅ <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- ✅ <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

Esa base será la que utilizarás cuando empieces a analizar tráfico con
herramientas como **<a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>**, **Zeek**, **Suricata**, **Splunk** o
**Microsoft Sentinel**, y cuando pases a la siguiente etapa de tu
formación centrada en **Linux** y el análisis de incidentes desde la
línea de comandos.
