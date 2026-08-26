**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Módulo 9 – Puertos (Ports)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Bienvenido al módulo más importante de Redes II.**

Si las direcciones IP identifican **qué dispositivo** se comunica, los
**puertos** identifican **qué aplicación o servicio** está utilizando la
red.

Como Analista SOC, pasarás gran parte de tu tiempo observando logs que
contienen información como:

TCP 443

UDP 53

TCP 3389

TCP 22

UDP 123

Cuando termines este módulo, deberías reconocer inmediatamente qué
significa cada uno de esos puertos y si su uso es normal o sospechoso.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es un puerto.

- Diferenciar IP y puerto.

- Entender cómo trabajan juntos TCP/UDP y los puertos.

- Conocer la clasificación oficial de puertos.

- Memorizar los puertos más importantes para un SOC.

- Interpretar puertos en Wireshark, Firewalls y SIEM.

- Comprender cómo utilizan los puertos los atacantes.

- Aplicar estos conocimientos en investigaciones reales.

**1. ¿Qué es un puerto?**

Un **puerto** es un número lógico que identifica una aplicación o
servicio dentro de un dispositivo.

Piensa en una computadora como un edificio.

La dirección IP indica **qué edificio es**.

El puerto indica **qué oficina** o **qué departamento** dentro de ese
edificio debe recibir la comunicación.

**Analogía**

Supongamos esta dirección:

Av. Siempre Viva 742

Esa sería la **IP**.

Ahora imaginemos que el edificio tiene:

Oficina 101

Oficina 202

Oficina 305

Oficina 410

Esas oficinas serían los **puertos**.

El correo debe saber:

- A qué edificio ir (IP).

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

**3. IP + Puerto = Destino completo**

Una dirección IP sola **no alcanza**.

Por ejemplo:

192.168.1.10

¿A qué aplicación va el paquete?

No lo sabemos.

Ahora observa:

192.168.1.10:443

Ya sabemos que el tráfico va dirigido al servicio HTTPS.

Otro ejemplo:

192.168.1.10:22

Ahora sabemos que se dirige al servicio SSH.

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

- HTTP

- HTTPS

- SSH

- DNS

- FTP

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

Cada comunicación tiene dos extremos.

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

- El servidor ofrece el servicio HTTPS en el puerto 443.

**7. Los puertos más importantes para un SOC**

**FTP – 20 y 21/TCP**

**Función:** Transferencia de archivos.

**Riesgo:** Si se usa sin cifrado, las credenciales viajan en texto
plano.

**SSH – 22/TCP**

**Función:** Administración remota segura de sistemas Linux.

**Riesgo:** Ataques de fuerza bruta.

**Telnet – 23/TCP**

**Función:** Administración remota antigua.

**Riesgo:** Todo viaja en texto plano.

**Recomendación:** Evitar su uso.

**SMTP – 25/TCP**

**Función:** Envío de correo electrónico.

**Riesgo:** Spam, abuso y configuraciones inseguras.

**DNS – 53/UDP (y a veces TCP)**

**Función:** Resolución de nombres.

**Riesgos:** DNS Tunneling, DNS Amplification.

**DHCP – 67/68 UDP**

**Función:** Asignación automática de direcciones IP.

**Riesgo:** Servidores DHCP no autorizados (Rogue DHCP).

**HTTP – 80/TCP**

**Función:** Navegación web sin cifrado.

**Riesgo:** Información visible en texto plano.

**POP3 – 110/TCP**

**Función:** Recepción de correo.

**NTP – 123/UDP**

**Función:** Sincronización de hora.

**Riesgo:** Ataques de amplificación NTP.

**IMAP – 143/TCP**

**Función:** Acceso al correo.

**SNMP – 161/UDP**

**Función:** Administración y monitoreo de dispositivos de red.

**Riesgo:** Configuraciones débiles y abuso para amplificación.

**LDAP – 389/TCP**

**Función:** Servicios de directorio (como Active Directory).

**HTTPS – 443/TCP**

**Función:** Navegación web cifrada.

**Es uno de los puertos más utilizados del mundo.**

**SMB – 445/TCP**

**Función:** Compartición de archivos e impresoras en Windows.

**Muy importante para un SOC.**

**Riesgos:**

- WannaCry.

- EternalBlue.

- Movimiento lateral.

- Robo de archivos.

**Syslog – 514/UDP**

**Función:** Envío de logs.

**LDAPS – 636/TCP**

**Función:** LDAP cifrado.

**IMAPS – 993/TCP**

**Función:** IMAP cifrado.

**POP3S – 995/TCP**

**Función:** POP3 cifrado.

**Microsoft SQL Server – 1433/TCP**

**Función:** Base de datos.

**Oracle – 1521/TCP**

**Función:** Base de datos Oracle.

**MySQL – 3306/TCP**

**Función:** Base de datos MySQL.

**PostgreSQL – 5432/TCP**

**Función:** Base de datos PostgreSQL.

**RDP – 3389/TCP**

**Función:** Escritorio Remoto de Windows.

**Uno de los puertos más atacados del mundo.**

**VNC – 5900/TCP**

**Función:** Acceso remoto gráfico.

**HTTP Alternativo – 8080/TCP**

Frecuente en:

- Proxies.

- Servidores web.

- Aplicaciones empresariales.

**8. Puertos y TCP/UDP**

Un mismo número de puerto puede existir para TCP y UDP.

Ejemplo:

53/TCP

53/UDP

No son lo mismo.

- **53/UDP:** consultas DNS normales.

- **53/TCP:** respuestas grandes, transferencias de zona, DNSSEC, etc.

**9. ¿Cómo aparecen los puertos en Wireshark?**

Ejemplo:

TCP

192.168.1.10:52340

↓

142.250.xxx.xxx:443

Interpretación:

- Puerto origen: 52340.

- Puerto destino: 443 (HTTPS).

**10. Puertos en un Firewall**

Ejemplo:

Origen

192.168.10.15

↓

TCP

↓

3389

↓

Bloqueado

Interpretación:

El firewall bloqueó un intento de acceso por RDP.

**11. Puertos en un SIEM**

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

- 22 (SSH).

- 3389 (RDP).

- 21 (FTP).

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

- Aplicar MFA en accesos remotos.

- Mantener servicios actualizados.

- Monitorear intentos de conexión.

- Realizar escaneos internos periódicos para detectar puertos expuestos.

**14. Aplicación práctica en un SOC**

**Caso 1**

TCP

443

↓

HTTPS

↓

Permitido

Interpretación:

Navegación web cifrada. En principio, comportamiento esperado.

**Caso 2**

TCP

3389

↓

Miles de intentos

↓

Desde Internet

Interpretación:

Posible ataque de fuerza bruta contra RDP.

**Caso 3**

TCP

445

↓

Conexiones entre muchas computadoras

Interpretación:

Puede ser tráfico normal de SMB... o un indicio de movimiento lateral de
un malware.

**Caso 4**

UDP

53

↓

Miles de consultas por minuto

Interpretación:

Puede ser actividad DNS legítima o un posible túnel DNS. Requiere
investigación.

**15. Tabla de puertos esenciales para memorizar**

| **Puerto** | **Protocolo** | **Servicio**     | **Riesgo principal**            |
|------------|---------------|------------------|---------------------------------|
| 20/21      | TCP           | FTP              | Credenciales sin cifrar         |
| 22         | TCP           | SSH              | Fuerza bruta                    |
| 23         | TCP           | Telnet           | Texto plano                     |
| 25         | TCP           | SMTP             | Spam                            |
| 53         | UDP/TCP       | DNS              | Túneles y amplificación         |
| 67/68      | UDP           | DHCP             | Rogue DHCP                      |
| 69         | UDP           | TFTP             | Sin autenticación               |
| 80         | TCP           | HTTP             | Sin cifrado                     |
| 110        | TCP           | POP3             | Correo sin cifrado              |
| 123        | UDP           | NTP              | Amplificación                   |
| 143        | TCP           | IMAP             | Correo                          |
| 161        | UDP           | SNMP             | Configuraciones débiles         |
| 389        | TCP           | LDAP             | Active Directory                |
| 443        | TCP           | HTTPS            | Tráfico web seguro              |
| 445        | TCP           | SMB              | Ransomware y movimiento lateral |
| 514        | UDP           | Syslog           | Logs                            |
| 636        | TCP           | LDAPS            | LDAP cifrado                    |
| 993        | TCP           | IMAPS            | Correo cifrado                  |
| 995        | TCP           | POP3S            | Correo cifrado                  |
| 1433       | TCP           | SQL Server       | Bases de datos                  |
| 1521       | TCP           | Oracle           | Bases de datos                  |
| 3306       | TCP           | MySQL            | Bases de datos                  |
| 3389       | TCP           | RDP              | Acceso remoto, fuerza bruta     |
| 5432       | TCP           | PostgreSQL       | Bases de datos                  |
| 5900       | TCP           | VNC              | Acceso remoto                   |
| 8080       | TCP           | HTTP alternativo | Proxies y aplicaciones          |

**16. Lo que esperan de un Analista SOC Nivel 1**

Cuando veas un log como este:

Origen:

192.168.10.50:53421

↓

Destino:

198.51.100.25:3389

↓

TCP

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

Ese análisis contextual es el trabajo diario de un Analista SOC.

**17. Resumen**

**Puerto**

- Identifica un servicio o aplicación dentro de un dispositivo.

**IP**

- Identifica el dispositivo.

**IP + Puerto**

- Identifican exactamente a qué servicio debe llegar la comunicación.

**Clasificación**

- **0–1023:** Well-Known Ports.

- **1024–49151:** Registered Ports.

- **49152–65535:** Dynamic/Ephemeral Ports.

**Puertos críticos para un SOC**

- **22 (SSH)**

- **53 (DNS)**

- **80 (HTTP)**

- **123 (NTP)**

- **443 (HTTPS)**

- **445 (SMB)**

- **3389 (RDP)**

Estos son los que más verás en logs, firewalls, SIEM y EDR.

**🧠 Conceptos clave para memorizar**

| **Concepto**   | **Debes recordar**                                       |
|----------------|----------------------------------------------------------|
| Puerto         | Identifica un servicio o aplicación.                     |
| IP             | Identifica el dispositivo.                               |
| Puerto origen  | Generalmente es efímero y lo elige el sistema operativo. |
| Puerto destino | Corresponde al servicio que se quiere utilizar.          |
| 443            | HTTPS.                                                   |
| 53             | DNS.                                                     |
| 22             | SSH.                                                     |
| 445            | SMB.                                                     |
| 3389           | RDP.                                                     |
| 80             | HTTP.                                                    |
| 123            | NTP.                                                     |

**🎓 Consejo como tu instructor de SOC**

Este módulo marca un antes y un después.

A partir de ahora, cuando veas un log como:

TCP 445

No quiero que pienses: *"es el puerto 445"*.

Quiero que tu mente haga automáticamente esta asociación:

**445 → SMB → Compartición de archivos en Windows → Riesgo de movimiento
lateral → Posibles ataques como WannaCry o explotación de SMB.**

Y si ves:

TCP 3389

Que pienses inmediatamente:

**3389 → RDP → Acceso remoto → Posibles intentos de fuerza bruta →
Verificar origen, usuario, horario y cantidad de intentos.**

Ese tipo de asociaciones rápidas es una habilidad que los analistas
desarrollan con la práctica y que marca una gran diferencia durante una
investigación.

**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Evaluación – Módulo 9: Puertos (Ports)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material. Este examen está diseñado con el nivel de dificultad de una
evaluación para un **Analista SOC Nivel 1**. Algunas preguntas son
conceptuales y otras presentan escenarios similares a los que
encontrarás en un SIEM, un firewall o un EDR.

**Pregunta 1**

¿Qué representa un **puerto** en una comunicación de red?

**A)** La dirección física de una computadora.

**B)** Un identificador lógico de una aplicación o servicio.

**C)** El modelo del router utilizado.

**D)** La velocidad de la conexión a Internet.

**Pregunta 2**

¿Cuál es la principal diferencia entre una **dirección IP** y un
**puerto**?

**A)** La IP identifica un dispositivo y el puerto identifica un
servicio o aplicación.

**B)** La IP identifica una aplicación y el puerto identifica un
dispositivo.

**C)** Ambos identifican exactamente lo mismo.

**D)** La IP solo existe en redes privadas.

**Pregunta 3**

¿Cuál es el rango de los **Well-Known Ports**?

**A)** 1024 – 49151

**B)** 49152 – 65535

**C)** 0 – 1023

**D)** 1 – 65535

**Pregunta 4**

Cuando tu computadora abre una página web segura (**HTTPS**), ¿qué
puerto de destino utiliza normalmente el servidor?

**A)** 22

**B)** 53

**C)** 80

**D)** 443

**Pregunta 5**

¿Qué servicio utiliza normalmente el puerto **22/TCP**?

**A)** FTP.

**B)** SSH.

**C)** HTTP.

**D)** DNS.

**Pregunta 6**

Como analista SOC observas el siguiente registro:

Origen:

192.168.10.15:52341

↓

Destino:

198.51.100.10:443

↓

TCP

¿Qué representa el puerto **52341**?

**A)** El puerto donde escucha el servidor HTTPS.

**B)** Un puerto dinámico (efímero) elegido por el sistema operativo del
cliente.

**C)** El puerto reservado para DNS.

**D)** El puerto estándar de Windows.

**Pregunta 7**

¿Cuál de los siguientes puertos suele asociarse con **RDP (Remote
Desktop Protocol)**?

**A)** 445

**B)** 3389

**C)** 8080

**D)** 1433

**Pregunta 8**

Como analista SOC recibes una alerta indicando:

Miles de intentos de conexión

↓

TCP

↓

Puerto 22

¿Cuál sería tu primera hipótesis?

**A)** Consultas DNS normales.

**B)** Un posible ataque de fuerza bruta contra SSH.

**C)** Una actualización automática del sistema operativo.

**D)** Un problema con el servidor DHCP.

**Pregunta 9**

¿Cuál de los siguientes servicios utiliza normalmente el puerto
**445/TCP**?

**A)** HTTPS.

**B)** SMB.

**C)** SSH.

**D)** SNMP.

**Pregunta 10 (Caso práctico SOC)**

El SIEM genera la siguiente alerta:

Origen:

203.0.113.45

↓

Destino:

Servidor Windows

↓

TCP

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

**D)** Una consulta DNS de gran tamaño.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

Un **puerto** identifica una **aplicación o servicio** que utiliza la
red. Permite que varias aplicaciones compartan una misma dirección IP
sin interferir entre sí.

**Pregunta 2**

✅ **Respuesta correcta: A**

**Justificación**

La **IP** identifica el dispositivo dentro de la red, mientras que el
**puerto** identifica el servicio o la aplicación que debe recibir la
comunicación.

Ejemplo:

192.168.1.10:443

- **192.168.1.10** → Dispositivo.

- **443** → Servicio HTTPS.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

Los **Well-Known Ports** abarcan desde el **0 hasta el 1023** y están
reservados para los servicios más conocidos como HTTP, HTTPS, SSH y DNS.

**Pregunta 4**

✅ **Respuesta correcta: D**

**Justificación**

El protocolo **HTTPS** utiliza por defecto el **puerto 443/TCP**,
permitiendo la comunicación cifrada mediante TLS.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

El puerto **22/TCP** corresponde al servicio **SSH (Secure Shell)**,
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

El puerto **3389/TCP** corresponde a **RDP (Remote Desktop Protocol)**,
utilizado para acceder remotamente a equipos Windows.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

Una gran cantidad de intentos hacia el puerto **22/TCP** suele indicar
un posible **ataque de fuerza bruta** intentando obtener acceso mediante
credenciales SSH.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

El puerto **445/TCP** corresponde al protocolo **SMB (Server Message
Block)**, utilizado para compartir archivos e impresoras en entornos
Windows.

Es uno de los puertos más vigilados en un SOC por su relación con
ransomware y movimiento lateral.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Miles de intentos sobre el puerto **3389/TCP** son un fuerte indicador
de un posible **ataque de fuerza bruta contra RDP**.

Como analista SOC, deberías revisar:

- La IP de origen.

- El número de intentos fallidos.

- Los usuarios afectados.

- El horario.

- Si hubo accesos exitosos posteriormente.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Reconoces rápidamente los puertos más importantes y puedes interpretar alertas típicas de un SOC.                                 |
| **8–9**                  | 🟢 **Muy buen nivel.** Ya relacionas puertos con servicios y riesgos comunes.                                                                       |
| **6–7**                  | 🟡 **Buen progreso.** Repasa especialmente los puertos más utilizados (22, 53, 80, 123, 443, 445 y 3389).                                           |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Memoriza la clasificación de puertos y los servicios asociados.                                        |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** Los puertos son una de las herramientas fundamentales para interpretar eventos de red en un SOC. |
