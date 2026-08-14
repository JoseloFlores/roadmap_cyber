**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Módulo 8 – UDP (User Datagram Protocol)**

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

- ✅ TCP

Ahora aprenderemos el "hermano" de TCP: **UDP**.

Comprender la diferencia entre ambos es una de las preguntas más
frecuentes en entrevistas para SOC y uno de los conocimientos que más
utilizarás cuando analices tráfico de red.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es UDP.

- Entender por qué existe.

- Diferenciar UDP de TCP.

- Saber cuándo conviene utilizar UDP.

- Conocer los protocolos que utilizan UDP.

- Comprender cómo aparece en Wireshark y en un SIEM.

- Entender cómo los atacantes aprovechan UDP.

- Aplicar estos conocimientos en investigaciones de un SOC.

**1. ¿Qué es UDP?**

UDP significa:

**User Datagram Protocol**

**Protocolo de Datagramas de Usuario**

Es un protocolo de la **Capa 4 (Transporte)** del modelo OSI, igual que
TCP.

Sin embargo, su filosofía es completamente diferente.

Mientras TCP dice:

"Voy a asegurarme de que todo llegue correctamente."

UDP dice:

"Voy a enviarlo lo más rápido posible."

**La diferencia en una frase**

**TCP**

**La confiabilidad es lo más importante.**

**UDP**

**La velocidad es lo más importante.**

**2. ¿Por qué existe UDP?**

Imagina que estás viendo un partido de fútbol en vivo.

¿Qué prefieres?

**Opción A**

La transmisión llega con **10 segundos de retraso**, pero nunca pierde
una imagen.

**Opción B**

La transmisión llega **en tiempo real**, aunque durante un segundo la
imagen se pixele.

La mayoría elegiría la segunda opción.

Eso hace UDP.

Prefiere perder algunos datos antes que retrasar toda la comunicación.

**3. ¿Cómo funciona UDP?**

UDP es muy simple.

La computadora envía el paquete.

Y listo.

No pregunta si el otro equipo está disponible.

No espera confirmaciones.

No retransmite.

Visualmente:

Cliente

↓

Paquete

↓

Servidor

Nada más.

**TCP hacía esto:**

SYN

↓

SYN ACK

↓

ACK

↓

Datos

UDP hace esto:

Datos

No existe Three-Way Handshake.

**4. ¿Qué NO hace UDP?**

UDP **NO**:

❌ Garantiza la entrega.

❌ Reenvía paquetes perdidos.

❌ Mantiene el orden.

❌ Espera confirmaciones (ACK).

❌ Controla la congestión.

❌ Controla el flujo.

Todo esto lo sacrifica para ganar velocidad.

**5. Entonces...**

¿Por qué alguien usaría UDP?

Porque hay aplicaciones donde la velocidad es mucho más importante que
la perfección.

Ejemplos:

Videollamadas.

Juegos Online.

Streaming.

DNS.

VoIP.

**Analogía**

TCP sería:

Enviar un contrato por correo certificado.

Si falta una hoja:

La vuelven a enviar.

UDP sería:

Una conversación telefónica.

Si una palabra no se escucha:

Nadie detiene la conversación.

Simplemente continúan hablando.

**6. Protocolos que utilizan UDP**

Muchísimos protocolos importantes utilizan UDP.

| **Protocolo**        | **Puerto** | **Utiliza UDP** |
|----------------------|------------|-----------------|
| DNS                  | 53         | ✅              |
| DHCP                 | 67-68      | ✅              |
| TFTP                 | 69         | ✅              |
| SNMP                 | 161        | ✅              |
| NTP                  | 123        | ✅              |
| Syslog (tradicional) | 514        | ✅              |
| RTP (audio/video)    | Variable   | ✅              |

**7. ¿Por qué DNS utiliza UDP?**

Cuando escribes:

www.google.com

Solo necesitas una respuesta pequeña.

Ejemplo:

Google

↓

142.250.xxx.xxx

No tiene sentido realizar un Three-Way Handshake para algo tan corto.

Por eso DNS normalmente utiliza UDP.

**Nota importante:** Cuando la respuesta DNS es muy grande (por ejemplo,
transferencias de zona o algunas respuestas con DNSSEC), puede utilizar
TCP.

**8. ¿Por qué los videojuegos usan UDP?**

Imagina un juego de disparos.

Cada jugador envía:

- Posición.

- Movimiento.

- Dirección.

- Disparo.

Todo el tiempo.

Si un paquete se pierde...

No importa.

Un instante después llegará otro con la posición actualizada.

Esperar una retransmisión haría que el juego se sintiera lento.

**9. ¿Cómo aparece UDP en Wireshark?**

Verás algo como:

UDP

192.168.1.15

↓

8.8.8.8

↓

53

Interpretación:

Consulta DNS.

Otro ejemplo:

UDP

192.168.1.15

↓

Servidor NTP

↓

123

Interpretación:

Sincronización de hora.

**10. UDP en un Firewall**

Ejemplo:

Origen

192.168.10.20

↓

Destino

8.8.8.8

↓

UDP

↓

Puerto 53

↓

Permitido

Interpretación:

Consulta DNS permitida.

**11. UDP en un SIEM**

Evento:

192.168.10.50

↓

Miles de paquetes UDP

↓

Puerto 123

Como analista pensarías:

- ¿Es tráfico NTP legítimo?

- ¿Existe una configuración incorrecta?

- ¿Puede tratarse de un ataque?

**12. ¿Cómo utilizan UDP los atacantes?**

**Ataque 1 – UDP Flood**

El atacante envía millones de paquetes UDP.

Resultado:

El servidor consume recursos intentando procesarlos.

Puede producir una denegación de servicio (DoS o DDoS).

**Ataque 2 – DNS Amplification**

Uno de los ataques más famosos.

El atacante:

1.  Envía una consulta DNS pequeña.

2.  Falsifica (spoofea) la IP de origen para que parezca la de la
    víctima.

3.  El servidor DNS responde con una respuesta mucho más grande hacia la
    víctima.

Atacante

↓

Consulta pequeña

↓

Servidor DNS

↓

Respuesta grande

↓

Víctima

Con poco tráfico generado por el atacante se consigue mucho tráfico
hacia la víctima.

**Ataque 3 – NTP Amplification**

Muy similar.

Se aprovecha de servidores NTP mal configurados para amplificar el
tráfico dirigido a la víctima.

**Ataque 4 – SNMP Amplification**

También utiliza servidores SNMP expuestos para multiplicar el volumen
del ataque.

**13. ¿Cómo defenderse?**

- Deshabilitar servicios UDP innecesarios.

- Configurar correctamente servidores DNS y NTP.

- Aplicar filtros anti-spoofing.

- Limitar el tráfico UDP en el firewall cuando corresponda.

- Mantener servicios actualizados.

- Implementar protección contra DDoS.

- Monitorear el tráfico UDP en el SIEM.

**14. Aplicación práctica en un SOC**

**Caso 1**

Firewall:

Origen

192.168.10.15

↓

UDP

↓

53

↓

8.8.8.8

Interpretación:

Consulta DNS normal.

**Caso 2**

Firewall:

192.168.10.15

↓

UDP

↓

123

↓

Miles de paquetes

Interpretación:

Puede ser tráfico NTP legítimo... o el inicio de un abuso del servicio.

Habrá que investigar el contexto.

**Caso 3**

SIEM:

Servidor

↓

500.000 paquetes UDP

↓

30 segundos

Interpretación:

Posible UDP Flood.

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

**16. ¿Cuándo elegir TCP y cuándo UDP?**

**Elegir TCP cuando:**

- No puede perderse información.

- Se necesita integridad.

- Es importante el orden de los datos.

Ejemplos:

- Banca online.

- Compras por Internet.

- Correo electrónico.

- Transferencia de archivos.

- Acceso remoto por SSH o RDP.

**Elegir UDP cuando:**

- La velocidad es más importante.

- Se tolera alguna pérdida de datos.

Ejemplos:

- Juegos online.

- Videollamadas.

- Streaming en vivo.

- Consultas DNS.

- Sincronización horaria (NTP).

**17. Lo que esperan de un Analista SOC Nivel 1**

Cuando veas un log como:

Origen:

192.168.10.35

↓

UDP

↓

Puerto:

53

↓

Destino:

8.8.8.8

Debes preguntarte:

- ¿Es una consulta DNS esperada?

- ¿La frecuencia es normal?

- ¿El servidor DNS es confiable?

- ¿El volumen de tráfico es habitual?

Si ves:

Origen:

203.0.113.10

↓

UDP

↓

Puerto:

123

↓

500.000 paquetes

Deberías pensar inmediatamente en un posible **UDP Flood** o en un
ataque de amplificación relacionado con NTP.

**18. Resumen**

**UDP**

- Es un protocolo de la **Capa 4 (Transporte)**.

- Es **no orientado a conexión**.

- No utiliza Three-Way Handshake.

- No garantiza la entrega ni el orden de los datos.

- Es muy rápido y consume pocos recursos.

**UDP es ideal para:**

- DNS.

- DHCP.

- NTP.

- SNMP.

- VoIP.

- Juegos online.

- Streaming.

**Riesgos asociados**

- UDP Flood.

- DNS Amplification.

- NTP Amplification.

- SNMP Amplification.

**🧠 Conceptos clave para memorizar**

| **Concepto**     | **Debes recordar**                       |
|------------------|------------------------------------------|
| UDP              | Protocolo rápido y sin conexión.         |
| Handshake        | UDP no utiliza Three-Way Handshake.      |
| ACK              | UDP no espera confirmaciones.            |
| Retransmisión    | UDP no retransmite paquetes perdidos.    |
| DNS              | Normalmente utiliza UDP/53.              |
| DHCP             | Utiliza UDP/67 y UDP/68.                 |
| NTP              | Utiliza UDP/123.                         |
| SNMP             | Utiliza UDP/161.                         |
| Streaming y VoIP | Priorizan velocidad sobre confiabilidad. |

**🎓 Consejo como tu instructor de SOC**

Este es uno de los temas que más aparece en entrevistas técnicas. Es muy
común que te pregunten:

**"¿Qué diferencia hay entre TCP y UDP?"**

Una buena respuesta no es solo decir que **TCP es confiable y UDP es
rápido**. Como analista SOC, debes relacionarlo con el tipo de tráfico y
con los riesgos asociados.

Por ejemplo:

- Si observas miles de paquetes **TCP SYN**, podrías pensar en un **SYN
  Flood** o en un **escaneo de puertos**.

- Si observas un volumen inusualmente alto de **UDP/53**, podrías
  investigar un posible **DNS Amplification**.

- Si detectas un gran flujo de **UDP/123**, considerarías un posible
  abuso de **NTP**.

Ese razonamiento basado en **puertos, protocolos y comportamiento del
tráfico** es el que utilizarás todos los días en un SOC para distinguir
una actividad normal de un incidente de seguridad.

**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Evaluación – Módulo 8: UDP (User Datagram Protocol)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material de estudio. Piensa como si estuvieras realizando una prueba
para ingresar a un **SOC Nivel 1**. Al finalizar encontrarás las
respuestas con su justificación.

**Pregunta 1**

¿Qué significa la sigla **UDP**?

**A)** Universal Data Protocol

**B)** User Datagram Protocol

**C)** Unified Data Protocol

**D)** User Data Process

**Pregunta 2**

¿Cuál es la principal característica de UDP?

**A)** Garantiza la entrega de todos los paquetes.

**B)** Utiliza Three-Way Handshake.

**C)** Prioriza la velocidad sobre la confiabilidad.

**D)** Reenvía automáticamente los paquetes perdidos.

**Pregunta 3**

¿En qué capa del modelo **OSI** trabaja UDP?

**A)** Capa 2 – Enlace de Datos.

**B)** Capa 3 – Red.

**C)** Capa 4 – Transporte.

**D)** Capa 7 – Aplicación.

**Pregunta 4**

¿Cuál de las siguientes características **NO** pertenece a UDP?

**A)** No utiliza ACK.

**B)** No garantiza la entrega.

**C)** No mantiene el orden de los paquetes.

**D)** Utiliza Three-Way Handshake.

**Pregunta 5**

¿Cuál de los siguientes protocolos utiliza normalmente **UDP**?

**A)** HTTPS.

**B)** SSH.

**C)** DNS.

**D)** FTP.

**Pregunta 6**

¿Por qué las videollamadas y los videojuegos suelen utilizar UDP?

**A)** Porque necesitan confirmar cada paquete enviado.

**B)** Porque la velocidad es más importante que recuperar cada paquete
perdido.

**C)** Porque UDP cifra automáticamente toda la comunicación.

**D)** Porque UDP consume más ancho de banda que TCP.

**Pregunta 7**

Como analista SOC observas el siguiente registro:

Origen:

192.168.10.15

↓

Destino:

8.8.8.8

↓

UDP

↓

Puerto 53

¿Cuál es la interpretación más probable?

**A)** Una conexión HTTPS.

**B)** Una consulta DNS.

**C)** Una conexión SSH.

**D)** Un acceso RDP.

**Pregunta 8**

¿Qué tipo de ataque aprovecha servidores DNS para enviar grandes
cantidades de tráfico hacia una víctima utilizando UDP?

**A)** SYN Flood.

**B)** DNS Amplification.

**C)** SQL Injection.

**D)** Cross-Site Scripting (XSS).

**Pregunta 9**

¿Cuál de las siguientes afirmaciones describe correctamente a UDP?

**A)** Es más lento que TCP porque verifica todos los paquetes.

**B)** Siempre retransmite los paquetes perdidos.

**C)** Es un protocolo no orientado a conexión.

**D)** Solo puede utilizarse en redes privadas.

**Pregunta 10 (Caso práctico SOC)**

El SIEM genera la siguiente alerta:

Origen:

203.0.113.25

↓

UDP

↓

Puerto 123

↓

750.000 paquetes

↓

45 segundos

¿Cuál sería tu primera hipótesis?

**A)** Un usuario sincronizando la hora de su computadora.

**B)** Un posible ataque UDP Flood o un abuso del servicio NTP.

**C)** Una transferencia FTP.

**D)** Un problema con el servidor web.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

UDP significa **User Datagram Protocol**. Es un protocolo de transporte
diseñado para ofrecer comunicaciones rápidas con una mínima sobrecarga.

**Pregunta 2**

✅ **Respuesta correcta: C**

**Justificación**

UDP fue diseñado para **priorizar la velocidad**, aceptando que algunos
paquetes puedan perderse sin ser retransmitidos.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

UDP trabaja en la **Capa 4 (Transporte)** del modelo OSI, al igual que
TCP.

**Pregunta 4**

✅ **Respuesta correcta: D**

**Justificación**

UDP **no utiliza Three-Way Handshake**. Esa es una característica
exclusiva de TCP.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

El protocolo **DNS** utiliza normalmente **UDP/53** porque las consultas
suelen ser pequeñas y requieren respuestas rápidas.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

En aplicaciones como videojuegos y videollamadas, es preferible perder
ocasionalmente un paquete antes que introducir retrasos esperando
retransmisiones.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

Una comunicación hacia **UDP/53** suele corresponder a una **consulta
DNS**, utilizada para resolver nombres de dominio en direcciones IP.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

En un ataque de **DNS Amplification**, el atacante envía pequeñas
consultas con la IP de la víctima falsificada, logrando que el servidor
DNS envíe respuestas mucho más grandes hacia esa víctima.

**Pregunta 9**

✅ **Respuesta correcta: C**

**Justificación**

UDP es un protocolo **no orientado a conexión**. No establece una sesión
antes de enviar datos ni verifica que estos lleguen correctamente.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Un volumen tan elevado de tráfico **UDP/123 (NTP)** es un fuerte
indicador de un posible **UDP Flood** o de un ataque de **amplificación
NTP**. Como analista SOC, deberías investigar el origen, el destino y el
contexto antes de sacar conclusiones.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Comprendes UDP y puedes diferenciar claramente su funcionamiento del de TCP, además de reconocer ataques comunes asociados.                            |
| **8–9**                  | 🟢 **Muy buen nivel.** Ya puedes interpretar tráfico UDP habitual y detectar patrones anómalos en un SOC.                                                                |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los protocolos que utilizan UDP y los conceptos de protocolo orientado/no orientado a conexión.                                             |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar las diferencias entre TCP y UDP y los casos de uso de cada uno.                                           |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** UDP es esencial para comprender el funcionamiento de DNS, DHCP, NTP, VoIP y muchos ataques de denegación de servicio. |
