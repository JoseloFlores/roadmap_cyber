**Módulo de Estudio <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Módulo 6 - <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (Network Address Translation)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Antes de comenzar:** Ya dominas:

-   ✅ Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas

-   ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>

-   ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

-   ✅ Máscaras de Subred

-   ✅ Subredes

-   ✅ <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

Este módulo conecta todos esos conocimientos. **<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>** es una tecnología fundamental para entender cómo una red privada puede comunicarse con Internet y cómo un analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> interpreta el tráfico que entra y sale de una organización.

**Objetivos de aprendizaje**

Al finalizar este módulo podrás:

-   Comprender qué es <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

-   Entender por qué fue creado.

-   Saber cómo funciona internamente.

-   Diferenciar los tipos de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

-   Comprender su relación con el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

-   Saber cómo aparece en un Firewall y en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

-   Entender cómo puede ser aprovechado por un atacante.

-   Aplicarlo durante investigaciones en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?**

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (Network Address Translation)** significa:

**Traducción de Direcciones de Red.**

Es una tecnología que permite **cambiar una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> por otra** mientras un paquete atraviesa un router o un firewall.

En la mayoría de los casos:

-   Convierte una **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada** en una **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública**.

-   O convierte una **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública** en una **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada**.

**Definición sencilla**

Imagina una empresa con 500 computadoras.

Todas tienen <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas:

192.168.10.15

192.168.10.20

192.168.10.35

192.168.10.100

Pero la empresa solo contrató **una única <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública**:

181.35.220.10

La pregunta es:

**¿Cómo hacen 500 computadoras para navegar por Internet usando una sola <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública?**

La respuesta es:

**Gracias a <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.**

**2. ¿Por qué existe <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?**

Recordemos algo que vimos en el módulo de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas y privadas.

Las direcciones IPv4 son limitadas.

Solo existen aproximadamente:

4.294 millones

Parece mucho\...

Pero no alcanza para asignar una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública a cada computadora, celular, TV, consola, reloj inteligente, cámara <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, etc.

Por eso se crearon las <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas y <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**Sin <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**

Imaginemos una empresa con:

1000 computadoras

Necesitaría:

1000 <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas

Sería extremadamente costoso y prácticamente inviable.

**Con <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**

Solo necesita:

1 <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública

o unas pocas.

**3. ¿Cómo funciona <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?**

Supongamos:

Mi PC

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada

192.168.1.25

Quiere acceder a:

www.google.com

(Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública).

La PC envía el paquete al <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

Recordemos:

PC → <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> → Internet

Hasta aquí no hay nada nuevo.

Ahora aparece <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> recibe:

Origen

192.168.1.25

Destino

142.250.xxx.xxx

Pero Internet no conoce esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada.

Entonces el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> hace algo muy importante.

La reemplaza.

Antes:

Origen

192.168.1.25

Después:

Origen

181.35.220.10

Ahora sí puede viajar por Internet.

**Visualización completa**

PC

192.168.1.25 → <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> → <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> → 181.35.220.10 → Internet → Google

**4. ¿Cómo vuelve la respuesta?**

Aquí aparece la magia de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

Cuando Google responde:

Destino

181.35.220.10

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> recuerda:

Esa conexión en realidad pertenecía a:

192.168.1.25

Entonces realiza la traducción inversa.

Internet → 181.35.220.10 → <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> → <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> → 192.168.1.25 → Mi PC

La computadora nunca sabe que su dirección fue modificada.

**5. ¿Cómo recuerda el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> quién hizo cada conexión?**

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> mantiene una **Tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**.

Ejemplo:

  -------------------------------------------------------------------------
  **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada**         **Puerto**   **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública**           **Puerto**
  ---------------------- ------------ ------------------------ ------------
  192.168.1.25           50231        181.35.220.10            45001

  192.168.1.30           50122        181.35.220.10            45002

  192.168.1.45           51015        181.35.220.10            45003
  -------------------------------------------------------------------------

Observa algo importante.

Todos utilizan la misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

Lo que cambia es el puerto.

Gracias a esto el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> sabe exactamente a quién devolver cada respuesta.

**Analogía**

Imagina un edificio.

Cada departamento tiene un número:

Depto 1

Depto 2

Depto 3

Depto 4

Pero todos tienen la misma dirección postal.

Cuando llega una carta:

El portero sabe a qué departamento pertenece.

<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> funciona exactamente igual.

**6. Tipos de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Estático**

Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada siempre corresponde a la misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

Ejemplo:

192.168.10.10 → 181.35.220.15

Siempre.

Muy utilizado para servidores.

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Dinámico**

Existe un grupo de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas.

Cada equipo recibe una disponible.

Ejemplo:

192.168.10.15 → 181.35.220.20

Más tarde otro equipo podría utilizar esa misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**PAT (Port Address Translation)**

Es el más utilizado.

También llamado:

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Overload**

Miles de equipos utilizan:

Una sola <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

Se diferencian mediante los puertos.

Este es el <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> que encontrarás en casi todas las casas y empresas.

**7. <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> y el Firewall**

En muchas organizaciones:

PC → Firewall → Internet

El Firewall realiza simultáneamente:

-   <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

-   Filtrado.

-   Registro de logs.

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>.

-   <a href="../../GLOSARIO.md#vpn" target="_blank">VPN</a>.

Por eso un Firewall moderno suele ser también el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**8. ¿Cómo aparece <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

Ejemplo:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Interna

192.168.10.25 → <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> → 181.35.220.10 → 185.15.20.30

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> debes responder:

-   ¿Qué usuario utilizaba la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> 192.168.10.25?

-   ¿Qué proceso inició la conexión?

-   ¿Era una conexión autorizada?

-   ¿Qué puerto utilizó?

-   ¿Fue bloqueada por el firewall?

**Otro ejemplo**

Alerta <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública

181.35.220.10 → Descarga malware

El analista debe investigar:

¿Quién fue?

Gracias a la tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> podrá descubrir:

181.35.220.10 → 192.168.10.85 → Usuario Juan Pérez → PC-Ventas-03

Aquí se ve claramente por qué la tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> es una pieza clave durante una investigación.

**9. ¿Cómo puede aprovechar <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> un atacante?**

**Caso 1 - Ocultar el origen**

Desde Internet solo se observa:

181.35.220.10

No se sabe inmediatamente cuál equipo interno realizó la conexión.

Por eso el analista debe consultar la tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**Caso 2 - Configuración incorrecta**

Si un administrador publica accidentalmente un servidor interno mediante <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>:

Servidor → SQLInternet

Ese servidor queda expuesto.

Si además tiene una vulnerabilidad, un atacante podría comprometerlo.

**Caso 3 - Reglas de Port Forwarding inseguras**

Supongamos:

Internet → Puerto 3389 → Servidor Windows

Si el acceso está expuesto sin controles adecuados:

-   Ataques de fuerza bruta.

-   Robo de credenciales.

-   Ransomware.

Este escenario ha sido responsable de numerosos incidentes reales.

**10. ¿Cómo defender una infraestructura <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?**

-   Publicar solo los servicios necesarios.

-   Evitar exponer RDP directamente a Internet.

-   Revisar periódicamente las reglas de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

-   Utilizar <a href="../../GLOSARIO.md#vpn" target="_blank">VPN</a> para el acceso remoto.

-   Aplicar <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a> para administradores.

-   Monitorear conexiones salientes y entrantes.

-   Registrar y conservar las tablas <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> cuando sea posible.

**11. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Caso 1**

Firewall

Origen 192.168.20.25 → <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> → 181.35.220.10 → <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> → Microsoft

Interpretación:

Tráfico normal de navegación.

**Caso 2**

Firewall

Origen

192.168.30.45 → <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> → 181.35.220.10 → 185.220.xxx.xxx → Puerto 4444

Como analista pensarías:

-   ¿Qué aplicación inició la conexión?

-   ¿El puerto es habitual?

-   ¿La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> tiene mala reputación?

-   ¿Existe un proceso malicioso?

-   ¿Se trata de comunicación con un servidor de Comando y Control (C2)?

**Caso 3**

Alerta

181.35.220.10 → Miles de conexiones por minuto

No puedes concluir inmediatamente que toda la empresa está comprometida.

Primero debes revisar:

-   La tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

-   Qué equipos generaron las conexiones.

-   Qué procesos participaron.

-   Si todas pertenecen al mismo usuario o a distintos equipos.

**12. Cuadro comparativo**

  -------------------------------------------------------------------------------------------
  **Concepto**   **Función**
  -------------- ----------------------------------------------------------------------------
  <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada     Se utiliza dentro de la red local.

  <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública     Identifica a la organización en Internet.

  <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>        Conecta la red local con otras redes.

  <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>            Traduce direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> entre redes.

  PAT            Permite que muchos equipos compartan una sola <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública mediante puertos.

  Tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>      Registra la relación entre conexiones internas y externas.
  -------------------------------------------------------------------------------------------

**13. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando observes un log como este:

Origen:

192.168.10.45

↓

<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>:

181.35.220.10

↓

Destino:

104.26.xxx.xxx

↓

Puerto:

443

Debes ser capaz de responder:

-   ¿Cuál es la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada?

-   ¿Cuál es la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública?

-   ¿Quién realizó la conexión?

-   ¿Qué aplicación utilizó el puerto 443?

-   ¿El tráfico parece normal?

-   ¿Qué muestra la tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?

-   ¿Fue una conexión permitida o bloqueada?

-   ¿Debe investigarse?

**Resumen**

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**

-   Traduce direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

-   Permite que <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas accedan a Internet.

-   Conserva las direcciones IPv4 públicas.

-   Funciona normalmente en el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> o Firewall.

**PAT**

-   Es el tipo de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> más utilizado.

-   Permite que miles de dispositivos compartan una misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública utilizando distintos puertos.

**Tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**

-   Relaciona <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas con <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas y puertos.

-   Es fundamental para las investigaciones de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Como analista, nunca debes quedarte solo con la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública. Tu objetivo es reconstruir el camino completo de la comunicación:

1.  **¿Qué equipo interno originó el tráfico?**

2.  **¿Qué usuario estaba utilizando ese equipo?**

3.  **¿Qué proceso generó la conexión?**

4.  **¿Hacia qué destino se conectó?**

5.  **¿Fue un comportamiento esperado o anómalo?**

**💡 Consejo como tu entrenador para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Muchos principiantes creen que **<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> solo sirve para \"tener Internet\"**, pero en realidad es una de las primeras piezas que un analista utiliza para **atribuir una conexión a un equipo específico**.

Imagina que recibes un aviso del proveedor de Internet diciendo:

**\"Su <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública 181.35.220.10 intentó conectarse a un servidor malicioso a las 14:32.\"**

Eso no identifica al culpable. En una empresa con cientos de equipos, todos comparten esa misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública mediante PAT.

Tu trabajo como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> será seguir el rastro:

-   Revisar los **logs del firewall**.

-   Consultar la **tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**.

-   Identificar la **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada** responsable.

-   Relacionarla con el **usuario**, el **equipo** y el **proceso** que inició la conexión.

Ese razonamiento es exactamente el que utilizan los analistas durante investigaciones reales y es una habilidad muy valorada en un **<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**.

**📚 Evaluación -- Módulo 6: <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (Network Address Translation)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Al finalizar encontrarás las respuestas con su justificación. Las preguntas están diseñadas con el estilo de una evaluación para un puesto de **Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**.

**Pregunta 1**

¿Qué significa la sigla **<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**?

**A)** Network Access Technology

**B)** Network Address Translation

**C)** Network Authentication Tunnel

**D)** Network Application Transfer

**Pregunta 2**

¿Cuál es el principal objetivo de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?

**A)** Encriptar las comunicaciones entre <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> equipos.

**B)** Traducir direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> entre redes.

**C)** Asignar direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> automáticamente.

**D)** Aumentar la velocidad de Internet.

**Pregunta 3**

¿Por qué fue necesario crear <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>?

**A)** Porque las direcciones IPv4 públicas son limitadas.

**B)** Porque las direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> se agotaron.

**C)** Porque los routers no pueden trabajar con <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas.

**D)** Porque IPv6 dejó de utilizarse.

**Pregunta 4**

¿Qué ocurre cuando una computadora con <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada quiere acceder a Internet?

**A)** Cambia automáticamente su dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> por una dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>.

**B)** El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> o Firewall traduce la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada a una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública mediante <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**C)** El servidor de destino cambia su dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**D)** La computadora recibe una nueva <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública permanente.

**Pregunta 5**

¿Cuál es el tipo de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> más utilizado en hogares y empresas?

**A)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Estático.

**B)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Dinámico.

**C)** PAT (Port Address Translation o <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Overload).

**D)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Inverso.

**Pregunta 6**

¿Qué información utiliza principalmente **PAT** para diferenciar múltiples conexiones que comparten una misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública?

**A)** La dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>.

**B)** El nombre del usuario.

**C)** Los números de puerto.

**D)** El sistema operativo.

**Pregunta 7**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> recibes la siguiente alerta:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública:

181.35.220.10

↓

Conexión sospechosa

↓

Puerto 4444

¿Cuál debería ser tu siguiente paso?

**A)** Concluir inmediatamente que toda la empresa está comprometida.

**B)** Buscar en la tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada originó esa conexión.

**C)** Reiniciar el firewall.

**D)** Cambiar la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública del proveedor de Internet.

**Pregunta 8**

¿Cuál de las siguientes afirmaciones sobre <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> es correcta?

**A)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> reemplaza al firewall.

**B)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> elimina la necesidad de utilizar direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas.

**C)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> permite que varios equipos compartan una misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

**D)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> bloquea automáticamente todos los ataques.

**Pregunta 9**

¿Qué riesgo representa una regla de **Port Forwarding** mal configurada?

**A)** Que una impresora deje de funcionar.

**B)** Que un servidor interno quede expuesto directamente a Internet.

**C)** Que la dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> cambie automáticamente.

**D)** Que el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> deje de realizar <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

El <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> genera la siguiente alerta:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública:

181.35.220.10

↓

Descarga detectada desde un dominio malicioso

↓

Hora:

15:42

¿Qué información necesitas para identificar el equipo responsable?

**A)** La dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> del servidor remoto.

**B)** La tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> del firewall para conocer qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada realizó la conexión.

**C)** El modelo del router.

**D)** La versión del navegador del usuario.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (Network Address Translation)** significa **Traducción de Direcciones de Red**. Su función principal es modificar direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> cuando el tráfico pasa por un router o firewall.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> traduce direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> entre diferentes redes, generalmente de una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada a una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública (y viceversa para las respuestas).

**Pregunta 3**

✅ **Respuesta correcta: A**

**Justificación**

Las direcciones **IPv4 públicas son un recurso limitado**. <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> permite que miles de dispositivos compartan una o pocas direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas, reduciendo la necesidad de asignar una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública a cada equipo.

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

Cuando un equipo con <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada accede a Internet, el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> o Firewall realiza <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>, sustituyendo la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada por una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública para que el tráfico pueda ser enrutado en Internet.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

**PAT (Port Address Translation)**, también conocido como **<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> Overload**, es el tipo de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> más común. Permite que muchos dispositivos compartan una misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública utilizando diferentes números de puerto.

**Pregunta 6**

✅ **Respuesta correcta: C**

**Justificación**

PAT utiliza los **puertos** para distinguir las conexiones de múltiples equipos que comparten una misma dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública suele representar a toda una organización. Para identificar el equipo responsable es necesario consultar la **tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>** y determinar qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada originó la conexión.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> permite que varios dispositivos utilicen una única <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública para acceder a Internet. Esto no reemplaza al firewall ni bloquea ataques por sí mismo.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

Una regla de **Port Forwarding** puede publicar un servidor interno en Internet. Si está mal configurada o el servicio es vulnerable, un atacante podría explotarlo para acceder a la red.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

La **tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>** relaciona las conexiones entre <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas, <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas y puertos. Es una fuente fundamental para identificar el equipo responsable de una actividad detectada desde la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública de la empresa.

**🏆 Resultado**

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Respuestas Correctas**   **Nivel**
  -------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  **10/10**                  ⭐ **Excelente.** Comprendes <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> no solo desde el punto de vista de redes, sino también desde la perspectiva de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

  **8--9**                   🟢 **Muy buen nivel.** Ya puedes interpretar registros de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> y comprender cómo rastrear conexiones desde una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública hasta un equipo interno.

  **6--7**                   🟡 **Buen progreso.** Repasa los tipos de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (especialmente PAT) y el funcionamiento de la tabla <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

  **4--5**                   🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar el flujo de traducción de direcciones y el papel del <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>/Firewall.

  **0--3**                   🔴 **Es recomendable repasar el módulo completo.** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> es un concepto esencial para investigar incidentes y atribuir actividad a equipos específicos en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
