**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Módulo 9 – Puertos (Ports)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Bienvenido al módulo más importante de Redes II.**

Si las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> identifican **qué dispositivo** se comunica, los
**puertos** identifican **qué aplicación o servicio** está utilizando la
red.

Como Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, pasarás gran parte de tu tiempo observando logs que
contienen información como:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 3389

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 22

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 123

Cuando termines este módulo, deberías reconocer inmediatamente qué
significa cada uno de esos puertos y si su uso es normal o sospechoso.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es un puerto.

- Diferenciar <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y puerto.

- Entender cómo trabajan juntos <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y los puertos.

- Conocer la clasificación oficial de puertos.

- Memorizar los puertos más importantes para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

- Interpretar puertos en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>, Firewalls y <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

- Comprender cómo utilizan los puertos los atacantes.

- Aplicar estos conocimientos en investigaciones reales.

**1. ¿Qué es un puerto?**

Un **puerto** es un número lógico que identifica una aplicación o
servicio dentro de un dispositivo.

Piensa en una computadora como un edificio.

La dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> indica **qué edificio es**.

El puerto indica **qué oficina** o **qué departamento** dentro de ese
edificio debe recibir la comunicación.

**Analogía**

Supongamos esta dirección:

Av. Siempre Viva 742

Esa sería la **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**.

Ahora imaginemos que el edificio tiene:

Oficina 101

Oficina 202

Oficina 305

Oficina 410

Esas oficinas serían los **puertos**.

El correo debe saber:

- A qué edificio ir (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>).

- A qué oficina entregar el paquete (Puerto).

En redes sucede exactamente lo mismo.

**2. ¿Por qué existen los puertos?**

Imagina una computadora que está ejecutando al mismo tiempo:

- Google Chrome.

- Outlook.

- Teams.

- Spotify.

- Zoom.

Todos usan la red al mismo tiempo.

¿Cómo sabe el sistema operativo qué aplicación debe recibir cada
paquete?

Gracias a los **puertos**.

**3. <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> + Puerto = Destino completo**

Una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> sola **no alcanza**.

Por ejemplo:

192.168.1.10

¿A qué aplicación va el paquete?

No lo sabemos.

Ahora observa:

192.168.1.10:443

Ya sabemos que el tráfico va dirigido al servicio <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

Otro ejemplo:

192.168.1.10:22

Ahora sabemos que se dirige al servicio <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**4. ¿Cuántos puertos existen?**

Los puertos van desde:

0

↓

65535

En total existen:

**65.536 puertos**.

No significa que todos estén abiertos o en uso.

**5. Clasificación oficial de puertos**

La organización **IANA (Internet Assigned Numbers Authority)** los
divide en tres grupos.

**A. Well-Known Ports (Puertos bien conocidos)**

0 – 1023

Reservados para los servicios más importantes.

Ejemplos:

- <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

- <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

- <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

- <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

**B. Registered Ports**

1024 – 49151

Asignados a aplicaciones registradas.

Ejemplos:

- Microsoft SQL Server.

- Oracle.

- PostgreSQL.

- MySQL.

**C. Dynamic o Ephemeral Ports**

49152 – 65535

Son puertos temporales.

El sistema operativo los utiliza cuando una computadora inicia una
conexión.

**6. ¿Qué es un puerto origen y un puerto destino?**

Cada comunicación tiene <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> extremos.

Ejemplo:

Tu PC

↓

Puerto Origen

↓

52341

↓

Servidor Web

↓

Puerto Destino

↓

443

Tu computadora eligió un puerto temporal (52341).

El servidor escucha siempre en el puerto 443.

**Ejemplo real**

Origen

192.168.1.15:52120

↓

Destino

142.250.xxx.xxx:443

Interpretación:

- La PC utiliza un puerto efímero (52120).

- El servidor ofrece el servicio <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> en el puerto 443.

**7. Los puertos más importantes para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**<a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a> – 20 y 21/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Transferencia de archivos.

**Riesgo:** Si se usa sin cifrado, las credenciales viajan en texto
plano.

**<a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> – 22/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Administración remota segura de sistemas Linux.

**Riesgo:** Ataques de fuerza bruta.

**Telnet – 23/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Administración remota antigua.

**Riesgo:** Todo viaja en texto plano.

**Recomendación:** Evitar su uso.

**<a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a> – 25/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Envío de correo electrónico.

**Riesgo:** Spam, abuso y configuraciones inseguras.

**<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> – 53/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> (y a veces <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>)**

**Función:** Resolución de nombres.

**Riesgos:** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Tunneling, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification.

**<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> – 67/68 <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

**Función:** Asignación automática de direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**Riesgo:** Servidores <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> no autorizados (<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>).

**<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> – 80/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Navegación web sin cifrado.

**Riesgo:** Información visible en texto plano.

**POP3 – 110/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Recepción de correo.

**NTP – 123/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

**Función:** Sincronización de hora.

**Riesgo:** Ataques de amplificación NTP.

**IMAP – 143/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Acceso al correo.

**SNMP – 161/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

**Función:** Administración y monitoreo de dispositivos de red.

**Riesgo:** Configuraciones débiles y abuso para amplificación.

**LDAP – 389/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Servicios de directorio (como Active Directory).

**<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> – 443/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Navegación web cifrada.

**Es uno de los puertos más utilizados del mundo.**

**SMB – 445/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Compartición de archivos e impresoras en Windows.

**Muy importante para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.**

**Riesgos:**

- WannaCry.

- EternalBlue.

- Movimiento lateral.

- Robo de archivos.

**<a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a> – 514/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

**Función:** Envío de logs.

**LDAPS – 636/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** LDAP cifrado.

**IMAPS – 993/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** IMAP cifrado.

**POP3S – 995/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** POP3 cifrado.

**Microsoft SQL Server – 1433/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Base de datos.

**Oracle – 1521/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Base de datos Oracle.

**MySQL – 3306/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Base de datos MySQL.

**PostgreSQL – 5432/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Base de datos PostgreSQL.

**RDP – 3389/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Escritorio Remoto de Windows.

**Uno de los puertos más atacados del mundo.**

**VNC – 5900/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**Función:** Acceso remoto gráfico.

**<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> Alternativo – 8080/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

Frecuente en:

- Proxies.

- Servidores web.

- Aplicaciones empresariales.

**8. Puertos y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

Un mismo número de puerto puede existir para <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

Ejemplo:

53/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

53/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

No son lo mismo.

- **53/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>:** consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> normales.

- **53/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>:** respuestas grandes, transferencias de zona, DNSSEC, etc.

**9. ¿Cómo aparecen los puertos en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>?**

Ejemplo:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

192.168.1.10:52340

↓

142.250.xxx.xxx:443

Interpretación:

- Puerto origen: 52340.

- Puerto destino: 443 (<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>).

**10. Puertos en un Firewall**

Ejemplo:

Origen

192.168.10.15

↓

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

↓

3389

↓

Bloqueado

Interpretación:

El firewall bloqueó un intento de acceso por RDP.

**11. Puertos en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**

Alerta:

192.168.10.35

↓

445

↓

Miles de conexiones

Como analista pensarías:

- ¿Es un servidor de archivos?

- ¿Puede ser un ransomware propagándose?

- ¿Se trata de movimiento lateral?

**12. ¿Cómo utilizan los atacantes los puertos?**

**Ataque 1 – Escaneo de puertos**

Herramientas como **Nmap** envían solicitudes a muchos puertos para
descubrir:

- Cuáles están abiertos.

- Qué servicios ejecutan.

- Qué versiones utilizan.

**Ataque 2 – Fuerza Bruta**

Los atacantes suelen intentar credenciales sobre:

- 22 (<a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>).

- 3389 (RDP).

- 21 (<a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>).

**Ataque 3 – Explotación de vulnerabilidades**

Ejemplos:

- SMB (445).

- RDP (3389).

- SQL Server (1433).

**Ataque 4 – Puertos abiertos innecesariamente**

Un puerto abierto sin necesidad aumenta la superficie de ataque.

Principio de seguridad:

**Abrir solo los puertos estrictamente necesarios.**

**13. ¿Cómo defenderse?**

- Cerrar puertos que no se utilicen.

- Filtrar con firewall.

- Cambiar credenciales por defecto.

- Aplicar <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a> en accesos remotos.

- Mantener servicios actualizados.

- Monitorear intentos de conexión.

- Realizar escaneos internos periódicos para detectar puertos expuestos.

**14. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Caso 1**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

443

↓

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

↓

Permitido

Interpretación:

Navegación web cifrada. En principio, comportamiento esperado.

**Caso 2**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

3389

↓

Miles de intentos

↓

Desde Internet

Interpretación:

Posible ataque de fuerza bruta contra RDP.

**Caso 3**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

445

↓

Conexiones entre muchas computadoras

Interpretación:

Puede ser tráfico normal de SMB... o un indicio de movimiento lateral de
un malware.

**Caso 4**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

53

↓

Miles de consultas por minuto

Interpretación:

Puede ser actividad <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> legítima o un posible túnel <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>. Requiere
investigación.

**15. Tabla de puertos esenciales para memorizar**

| **Puerto** | **Protocolo** | **Servicio**     | **Riesgo principal**            |
|------------|---------------|------------------|---------------------------------|
| 20/21      | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>              | Credenciales sin cifrar         |
| 22         | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>              | Fuerza bruta                    |
| 23         | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | Telnet           | Texto plano                     |
| 25         | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>             | Spam                            |
| 53         | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>       | <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>              | Túneles y amplificación         |
| 67/68      | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>           | <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>             | <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>                      |
| 69         | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>           | TFTP             | Sin autenticación               |
| 80         | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>             | Sin cifrado                     |
| 110        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | POP3             | Correo sin cifrado              |
| 123        | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>           | NTP              | Amplificación                   |
| 143        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | IMAP             | Correo                          |
| 161        | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>           | SNMP             | Configuraciones débiles         |
| 389        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | LDAP             | Active Directory                |
| 443        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>            | Tráfico web seguro              |
| 445        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | SMB              | Ransomware y movimiento lateral |
| 514        | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>           | <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a>           | Logs                            |
| 636        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | LDAPS            | LDAP cifrado                    |
| 993        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | IMAPS            | Correo cifrado                  |
| 995        | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | POP3S            | Correo cifrado                  |
| 1433       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | SQL Server       | Bases de datos                  |
| 1521       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | Oracle           | Bases de datos                  |
| 3306       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | MySQL            | Bases de datos                  |
| 3389       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | RDP              | Acceso remoto, fuerza bruta     |
| 5432       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | PostgreSQL       | Bases de datos                  |
| 5900       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | VNC              | Acceso remoto                   |
| 8080       | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>           | <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> alternativo | Proxies y aplicaciones          |

**16. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando veas un log como este:

Origen:

192.168.10.50:53421

↓

Destino:

198.51.100.25:3389

↓

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

↓

Permitido

No debes limitarte a leer los números. Debes interpretar el contexto:

- ¿El puerto **3389** corresponde a RDP? Sí.

- ¿Ese equipo debería conectarse por RDP?

- ¿Es una conexión interna o hacia Internet?

- ¿El horario coincide con la jornada laboral?

- ¿El usuario está autorizado?

- ¿Hubo varios intentos fallidos antes?

- ¿El destino pertenece a la organización o es externo?

Ese análisis contextual es el trabajo diario de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**17. Resumen**

**Puerto**

- Identifica un servicio o aplicación dentro de un dispositivo.

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**

- Identifica el dispositivo.

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> + Puerto**

- Identifican exactamente a qué servicio debe llegar la comunicación.

**Clasificación**

- **0–1023:** Well-Known Ports.

- **1024–49151:** Registered Ports.

- **49152–65535:** Dynamic/Ephemeral Ports.

**Puertos críticos para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

- **22 (<a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>)**

- **53 (<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>)**

- **80 (<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>)**

- **123 (NTP)**

- **443 (<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>)**

- **445 (SMB)**

- **3389 (RDP)**

Estos son los que más verás en logs, firewalls, <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> y <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>.

**🧠 Conceptos clave para memorizar**

| **Concepto**   | **Debes recordar**                                       |
|----------------|----------------------------------------------------------|
| Puerto         | Identifica un servicio o aplicación.                     |
| <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>             | Identifica el dispositivo.                               |
| Puerto origen  | Generalmente es efímero y lo elige el sistema operativo. |
| Puerto destino | Corresponde al servicio que se quiere utilizar.          |
| 443            | <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.                                                   |
| 53             | <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.                                                     |
| 22             | <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.                                                     |
| 445            | SMB.                                                     |
| 3389           | RDP.                                                     |
| 80             | <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.                                                    |
| 123            | NTP.                                                     |

**🎓 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Este módulo marca un antes y un después.

A partir de ahora, cuando veas un log como:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 445

No quiero que pienses: *"es el puerto 445"*.

Quiero que tu mente haga automáticamente esta asociación:

**445 → SMB → Compartición de archivos en Windows → Riesgo de movimiento
lateral → Posibles ataques como WannaCry o explotación de SMB.**

Y si ves:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 3389

Que pienses inmediatamente:

**3389 → RDP → Acceso remoto → Posibles intentos de fuerza bruta →
Verificar origen, usuario, horario y cantidad de intentos.**

Ese tipo de asociaciones rápidas es una habilidad que los analistas
desarrollan con la práctica y que marca una gran diferencia durante una
investigación.

**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Evaluación – Módulo 9: Puertos (Ports)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material. Este examen está diseñado con el nivel de dificultad de una
evaluación para un **Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**. Algunas preguntas son
conceptuales y otras presentan escenarios similares a los que
encontrarás en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>, un firewall o un <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>.

**Pregunta 1**

¿Qué representa un **puerto** en una comunicación de red?

**A)** La dirección física de una computadora.

**B)** Un identificador lógico de una aplicación o servicio.

**C)** El modelo del router utilizado.

**D)** La velocidad de la conexión a Internet.

**Pregunta 2**

¿Cuál es la principal diferencia entre una **dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>** y un
**puerto**?

**A)** La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> identifica un dispositivo y el puerto identifica un
servicio o aplicación.

**B)** La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> identifica una aplicación y el puerto identifica un
dispositivo.

**C)** Ambos identifican exactamente lo mismo.

**D)** La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> solo existe en redes privadas.

**Pregunta 3**

¿Cuál es el rango de los **Well-Known Ports**?

**A)** 1024 – 49151

**B)** 49152 – 65535

**C)** 0 – 1023

**D)** 1 – 65535

**Pregunta 4**

Cuando tu computadora abre una página web segura (**<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**), ¿qué
puerto de destino utiliza normalmente el servidor?

**A)** 22

**B)** 53

**C)** 80

**D)** 443

**Pregunta 5**

¿Qué servicio utiliza normalmente el puerto **22/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**?

**A)** <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>.

**B)** <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**C)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

**D)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**Pregunta 6**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> observas el siguiente registro:

Origen:

192.168.10.15:52341

↓

Destino:

198.51.100.10:443

↓

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

¿Qué representa el puerto **52341**?

**A)** El puerto donde escucha el servidor <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**B)** Un puerto dinámico (efímero) elegido por el sistema operativo del
cliente.

**C)** El puerto reservado para <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**D)** El puerto estándar de Windows.

**Pregunta 7**

¿Cuál de los siguientes puertos suele asociarse con **RDP (Remote
Desktop Protocol)**?

**A)** 445

**B)** 3389

**C)** 8080

**D)** 1433

**Pregunta 8**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> recibes una alerta indicando:

Miles de intentos de conexión

↓

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

↓

Puerto 22

¿Cuál sería tu primera hipótesis?

**A)** Consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> normales.

**B)** Un posible ataque de fuerza bruta contra <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**C)** Una actualización automática del sistema operativo.

**D)** Un problema con el servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**Pregunta 9**

¿Cuál de los siguientes servicios utiliza normalmente el puerto
**445/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**?

**A)** <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**B)** SMB.

**C)** <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**D)** SNMP.

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

El <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> genera la siguiente alerta:

Origen:

203.0.113.45

↓

Destino:

Servidor Windows

↓

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

↓

3389

↓

4.500 intentos

↓

15 minutos

¿Cuál sería la interpretación inicial más razonable?

**A)** Tráfico normal de navegación web.

**B)** Un posible ataque de fuerza bruta contra RDP.

**C)** Sincronización horaria mediante NTP.

**D)** Una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> de gran tamaño.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

Un **puerto** identifica una **aplicación o servicio** que utiliza la
red. Permite que varias aplicaciones compartan una misma dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>
sin interferir entre sí.

**Pregunta 2**

✅ **Respuesta correcta: A**

**Justificación**

La **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>** identifica el dispositivo dentro de la red, mientras que el
**puerto** identifica el servicio o la aplicación que debe recibir la
comunicación.

Ejemplo:

192.168.1.10:443

- **192.168.1.10** → Dispositivo.

- **443** → Servicio <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

Los **Well-Known Ports** abarcan desde el **0 hasta el 1023** y están
reservados para los servicios más conocidos como <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**Pregunta 4**

✅ **Respuesta correcta: D**

**Justificación**

El protocolo **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>** utiliza por defecto el **puerto 443/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**,
permitiendo la comunicación cifrada mediante <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

El puerto **22/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** corresponde al servicio **<a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> (Secure <a href="../../GLOSARIO.md#shell" target="_blank">Shell</a>)**,
utilizado para la administración remota segura de sistemas.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

El puerto **52341** es un **puerto dinámico o efímero**. El sistema
operativo lo asigna temporalmente al cliente para iniciar una conexión
con el servidor.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

El puerto **3389/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** corresponde a **RDP (Remote Desktop Protocol)**,
utilizado para acceder remotamente a equipos Windows.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

Una gran cantidad de intentos hacia el puerto **22/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** suele indicar
un posible **ataque de fuerza bruta** intentando obtener acceso mediante
credenciales <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

El puerto **445/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** corresponde al protocolo **SMB (Server Message
Block)**, utilizado para compartir archivos e impresoras en entornos
Windows.

Es uno de los puertos más vigilados en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> por su relación con
ransomware y movimiento lateral.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Miles de intentos sobre el puerto **3389/<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>** son un fuerte indicador
de un posible **ataque de fuerza bruta contra RDP**.

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, deberías revisar:

- La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen.

- El número de intentos fallidos.

- Los usuarios afectados.

- El horario.

- Si hubo accesos exitosos posteriormente.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Reconoces rápidamente los puertos más importantes y puedes interpretar alertas típicas de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.                                 |
| **8–9**                  | 🟢 **Muy buen nivel.** Ya relacionas puertos con servicios y riesgos comunes.                                                                       |
| **6–7**                  | 🟡 **Buen progreso.** Repasa especialmente los puertos más utilizados (22, 53, 80, 123, 443, 445 y 3389).                                           |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Memoriza la clasificación de puertos y los servicios asociados.                                        |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** Los puertos son una de las herramientas fundamentales para interpretar eventos de red en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>. |
