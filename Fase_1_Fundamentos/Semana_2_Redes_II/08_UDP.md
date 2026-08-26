**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Módulo 8 – <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> (User Datagram Protocol)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>

- ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

- ✅ Máscaras

- ✅ Subredes

- ✅ <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

- ✅ <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>

- ✅ <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

Ahora aprenderemos el "hermano" de <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>: **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**.

Comprender la diferencia entre ambos es una de las preguntas más
frecuentes en entrevistas para <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> y uno de los conocimientos que más
utilizarás cuando analices tráfico de red.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

- Entender por qué existe.

- Diferenciar <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> de <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

- Saber cuándo conviene utilizar <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

- Conocer los protocolos que utilizan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

- Comprender cómo aparece en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a> y en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

- Entender cómo los atacantes aprovechan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

- Aplicar estos conocimientos en investigaciones de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> significa:

**User Datagram Protocol**

**Protocolo de Datagramas de Usuario**

Es un protocolo de la **Capa 4 (Transporte)** del modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>, igual que
<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

Sin embargo, su filosofía es completamente diferente.

Mientras <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> dice:

"Voy a asegurarme de que todo llegue correctamente."

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> dice:

"Voy a enviarlo lo más rápido posible."

**La diferencia en una frase**

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**

**La confiabilidad es lo más importante.**

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

**La velocidad es lo más importante.**

**2. ¿Por qué existe <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

Imagina que estás viendo un partido de fútbol en vivo.

¿Qué prefieres?

**Opción A**

La transmisión llega con **10 segundos de retraso**, pero nunca pierde
una imagen.

**Opción B**

La transmisión llega **en tiempo real**, aunque durante un segundo la
imagen se pixele.

La mayoría elegiría la segunda opción.

Eso hace <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

Prefiere perder algunos datos antes que retrasar toda la comunicación.

**3. ¿Cómo funciona <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> es muy simple.

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

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> hacía esto:**

SYN

↓

SYN ACK

↓

ACK

↓

Datos

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> hace esto:

Datos

No existe <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>.

**4. ¿Qué NO hace <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> **NO**:

❌ Garantiza la entrega.

❌ Reenvía paquetes perdidos.

❌ Mantiene el orden.

❌ Espera confirmaciones (ACK).

❌ Controla la congestión.

❌ Controla el flujo.

Todo esto lo sacrifica para ganar velocidad.

**5. Entonces...**

¿Por qué alguien usaría <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

Porque hay aplicaciones donde la velocidad es mucho más importante que
la perfección.

Ejemplos:

Videollamadas.

Juegos Online.

Streaming.

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

VoIP.

**Analogía**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> sería:

Enviar un contrato por correo certificado.

Si falta una hoja:

La vuelven a enviar.

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> sería:

Una conversación telefónica.

Si una palabra no se escucha:

Nadie detiene la conversación.

Simplemente continúan hablando.

**6. Protocolos que utilizan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

Muchísimos protocolos importantes utilizan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

| **Protocolo**        | **Puerto** | **Utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>** |
|----------------------|------------|-----------------|
| <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>                  | 53         | ✅              |
| <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>                 | 67-68      | ✅              |
| TFTP                 | 69         | ✅              |
| SNMP                 | 161        | ✅              |
| NTP                  | 123        | ✅              |
| <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a> (tradicional) | 514        | ✅              |
| RTP (audio/video)    | Variable   | ✅              |

**7. ¿Por qué <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

Cuando escribes:

www.google.com

Solo necesitas una respuesta pequeña.

Ejemplo:

Google

↓

142.250.xxx.xxx

No tiene sentido realizar un <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a> para algo tan corto.

Por eso <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> normalmente utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

**Nota importante:** Cuando la respuesta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> es muy grande (por ejemplo,
transferencias de zona o algunas respuestas con DNSSEC), puede utilizar
<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**8. ¿Por qué los videojuegos usan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

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

**9. ¿Cómo aparece <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>?**

Verás algo como:

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

192.168.1.15

↓

8.8.8.8

↓

53

Interpretación:

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

Otro ejemplo:

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

192.168.1.15

↓

Servidor NTP

↓

123

Interpretación:

Sincronización de hora.

**10. <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> en un Firewall**

Ejemplo:

Origen

192.168.10.20

↓

Destino

8.8.8.8

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

Puerto 53

↓

Permitido

Interpretación:

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> permitida.

**11. <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**

Evento:

192.168.10.50

↓

Miles de paquetes <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

Puerto 123

Como analista pensarías:

- ¿Es tráfico NTP legítimo?

- ¿Existe una configuración incorrecta?

- ¿Puede tratarse de un ataque?

**12. ¿Cómo utilizan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> los atacantes?**

**Ataque 1 – <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood**

El atacante envía millones de paquetes <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

Resultado:

El servidor consume recursos intentando procesarlos.

Puede producir una denegación de servicio (<a href="../../GLOSARIO.md#dos" target="_blank">DoS</a> o <a href="../../GLOSARIO.md#ddos" target="_blank">DDoS</a>).

**Ataque 2 – <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification**

Uno de los ataques más famosos.

El atacante:

1.  Envía una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> pequeña.

2.  Falsifica (spoofea) la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen para que parezca la de la
    víctima.

3.  El servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> responde con una respuesta mucho más grande hacia la
    víctima.

Atacante

↓

Consulta pequeña

↓

Servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

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

- Deshabilitar servicios <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> innecesarios.

- Configurar correctamente servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> y NTP.

- Aplicar filtros anti-spoofing.

- Limitar el tráfico <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> en el firewall cuando corresponda.

- Mantener servicios actualizados.

- Implementar protección contra <a href="../../GLOSARIO.md#ddos" target="_blank">DDoS</a>.

- Monitorear el tráfico <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> en el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

**14. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Caso 1**

Firewall:

Origen

192.168.10.15

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

53

↓

8.8.8.8

Interpretación:

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> normal.

**Caso 2**

Firewall:

192.168.10.15

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

123

↓

Miles de paquetes

Interpretación:

Puede ser tráfico NTP legítimo... o el inicio de un abuso del servicio.

Habrá que investigar el contexto.

**Caso 3**

<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>:

Servidor

↓

500.000 paquetes <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

30 segundos

Interpretación:

Posible <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood.

**15. <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> vs <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

| **Característica**    | **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**               | **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**                      |
|-----------------------|-----------------------|------------------------------|
| Orientado a conexión  | ✅ Sí                 | ❌ No                        |
| <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>   | ✅ Sí                 | ❌ No                        |
| Garantiza la entrega  | ✅ Sí                 | ❌ No                        |
| Mantiene el orden     | ✅ Sí                 | ❌ No                        |
| Reenvía paquetes      | ✅ Sí                 | ❌ No                        |
| ACK                   | ✅ Sí                 | ❌ No                        |
| Control de flujo      | ✅ Sí                 | ❌ No                        |
| Control de congestión | ✅ Sí                 | ❌ No                        |
| Velocidad             | Más lenta             | Más rápida                   |
| Confiabilidad         | Muy alta              | Baja                         |
| Uso típico            | Web, <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>, correo, RDP | <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, VoIP, juegos, streaming |

**16. ¿Cuándo elegir <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y cuándo <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?**

**Elegir <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> cuando:**

- No puede perderse información.

- Se necesita integridad.

- Es importante el orden de los datos.

Ejemplos:

- Banca online.

- Compras por Internet.

- Correo electrónico.

- Transferencia de archivos.

- Acceso remoto por <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> o RDP.

**Elegir <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> cuando:**

- La velocidad es más importante.

- Se tolera alguna pérdida de datos.

Ejemplos:

- Juegos online.

- Videollamadas.

- Streaming en vivo.

- Consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Sincronización horaria (NTP).

**17. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando veas un log como:

Origen:

192.168.10.35

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

Puerto:

53

↓

Destino:

8.8.8.8

Debes preguntarte:

- ¿Es una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> esperada?

- ¿La frecuencia es normal?

- ¿El servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> es confiable?

- ¿El volumen de tráfico es habitual?

Si ves:

Origen:

203.0.113.10

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

Puerto:

123

↓

500.000 paquetes

Deberías pensar inmediatamente en un posible **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood** o en un
ataque de amplificación relacionado con NTP.

**18. Resumen**

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**

- Es un protocolo de la **Capa 4 (Transporte)**.

- Es **no orientado a conexión**.

- No utiliza <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>.

- No garantiza la entrega ni el orden de los datos.

- Es muy rápido y consume pocos recursos.

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> es ideal para:**

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

- NTP.

- SNMP.

- VoIP.

- Juegos online.

- Streaming.

**Riesgos asociados**

- <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood.

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification.

- NTP Amplification.

- SNMP Amplification.

**🧠 Conceptos clave para memorizar**

| **Concepto**     | **Debes recordar**                       |
|------------------|------------------------------------------|
| <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>              | Protocolo rápido y sin conexión.         |
| Handshake        | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> no utiliza <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>.      |
| ACK              | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> no espera confirmaciones.            |
| Retransmisión    | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> no retransmite paquetes perdidos.    |
| <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>              | Normalmente utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/53.              |
| <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>             | Utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/67 y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/68.                 |
| NTP              | Utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/123.                         |
| SNMP             | Utiliza <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/161.                         |
| Streaming y VoIP | Priorizan velocidad sobre confiabilidad. |

**🎓 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Este es uno de los temas que más aparece en entrevistas técnicas. Es muy
común que te pregunten:

**"¿Qué diferencia hay entre <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?"**

Una buena respuesta no es solo decir que **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> es confiable y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> es
rápido**. Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, debes relacionarlo con el tipo de tráfico y
con los riesgos asociados.

Por ejemplo:

- Si observas miles de paquetes **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> SYN**, podrías pensar en un **SYN
  Flood** o en un **escaneo de puertos**.

- Si observas un volumen inusualmente alto de **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/53**, podrías
  investigar un posible **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification**.

- Si detectas un gran flujo de **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/123**, considerarías un posible
  abuso de **NTP**.

Ese razonamiento basado en **puertos, protocolos y comportamiento del
tráfico** es el que utilizarás todos los días en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> para distinguir
una actividad normal de un incidente de seguridad.

**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Evaluación – Módulo 8: <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> (User Datagram Protocol)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material de estudio. Piensa como si estuvieras realizando una prueba
para ingresar a un **<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**. Al finalizar encontrarás las
respuestas con su justificación.

**Pregunta 1**

¿Qué significa la sigla **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**?

**A)** Universal Data Protocol

**B)** User Datagram Protocol

**C)** Unified Data Protocol

**D)** User Data Process

**Pregunta 2**

¿Cuál es la principal característica de <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** Garantiza la entrega de todos los paquetes.

**B)** Utiliza <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>.

**C)** Prioriza la velocidad sobre la confiabilidad.

**D)** Reenvía automáticamente los paquetes perdidos.

**Pregunta 3**

¿En qué capa del modelo **<a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>** trabaja <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** Capa 2 – Enlace de Datos.

**B)** Capa 3 – Red.

**C)** Capa 4 – Transporte.

**D)** Capa 7 – Aplicación.

**Pregunta 4**

¿Cuál de las siguientes características **NO** pertenece a <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** No utiliza ACK.

**B)** No garantiza la entrega.

**C)** No mantiene el orden de los paquetes.

**D)** Utiliza <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>.

**Pregunta 5**

¿Cuál de los siguientes protocolos utiliza normalmente **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>**?

**A)** <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**B)** <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**C)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**D)** <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>.

**Pregunta 6**

¿Por qué las videollamadas y los videojuegos suelen utilizar <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** Porque necesitan confirmar cada paquete enviado.

**B)** Porque la velocidad es más importante que recuperar cada paquete
perdido.

**C)** Porque <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> cifra automáticamente toda la comunicación.

**D)** Porque <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> consume más ancho de banda que <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**Pregunta 7**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> observas el siguiente registro:

Origen:

192.168.10.15

↓

Destino:

8.8.8.8

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

Puerto 53

¿Cuál es la interpretación más probable?

**A)** Una conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**B)** Una consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**C)** Una conexión <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

**D)** Un acceso RDP.

**Pregunta 8**

¿Qué tipo de ataque aprovecha servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> para enviar grandes
cantidades de tráfico hacia una víctima utilizando <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** SYN Flood.

**B)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification.

**C)** SQL Injection.

**D)** Cross-Site Scripting (XSS).

**Pregunta 9**

¿Cuál de las siguientes afirmaciones describe correctamente a <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>?

**A)** Es más lento que <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> porque verifica todos los paquetes.

**B)** Siempre retransmite los paquetes perdidos.

**C)** Es un protocolo no orientado a conexión.

**D)** Solo puede utilizarse en redes privadas.

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

El <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> genera la siguiente alerta:

Origen:

203.0.113.25

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

↓

Puerto 123

↓

750.000 paquetes

↓

45 segundos

¿Cuál sería tu primera hipótesis?

**A)** Un usuario sincronizando la hora de su computadora.

**B)** Un posible ataque <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood o un abuso del servicio NTP.

**C)** Una transferencia <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>.

**D)** Un problema con el servidor web.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> significa **User Datagram Protocol**. Es un protocolo de transporte
diseñado para ofrecer comunicaciones rápidas con una mínima sobrecarga.

**Pregunta 2**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> fue diseñado para **priorizar la velocidad**, aceptando que algunos
paquetes puedan perderse sin ser retransmitidos.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> trabaja en la **Capa 4 (Transporte)** del modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>, al igual que
<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**Pregunta 4**

✅ **Respuesta correcta: D**

**Justificación**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> **no utiliza <a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>**. Esa es una característica
exclusiva de <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

El protocolo **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>** utiliza normalmente **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/53** porque las consultas
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

Una comunicación hacia **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/53** suele corresponder a una **consulta
<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**, utilizada para resolver nombres de dominio en direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

En un ataque de **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification**, el atacante envía pequeñas
consultas con la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de la víctima falsificada, logrando que el servidor
<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> envíe respuestas mucho más grandes hacia esa víctima.

**Pregunta 9**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> es un protocolo **no orientado a conexión**. No establece una sesión
antes de enviar datos ni verifica que estos lleguen correctamente.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Un volumen tan elevado de tráfico **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>/123 (NTP)** es un fuerte
indicador de un posible **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> Flood** o de un ataque de **amplificación
NTP**. Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, deberías investigar el origen, el destino y el
contexto antes de sacar conclusiones.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Comprendes <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y puedes diferenciar claramente su funcionamiento del de <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>, además de reconocer ataques comunes asociados.                            |
| **8–9**                  | 🟢 **Muy buen nivel.** Ya puedes interpretar tráfico <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> habitual y detectar patrones anómalos en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.                                                                |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los protocolos que utilizan <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y los conceptos de protocolo orientado/no orientado a conexión.                                             |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar las diferencias entre <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y los casos de uso de cada uno.                                           |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> es esencial para comprender el funcionamiento de <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>, NTP, VoIP y muchos ataques de denegación de servicio. |
