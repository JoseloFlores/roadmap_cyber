**Módulo de Estudio SOC**

**Módulo 6 - NAT (Network Address Translation)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar:** Ya dominas:

-   ✅ Direcciones IP Públicas y Privadas

-   ✅ Modelo OSI

-   ✅ Modelo TCP/IP

-   ✅ Máscaras de Subred

-   ✅ Subredes

-   ✅ Gateway

Este módulo conecta todos esos conocimientos. **NAT** es una tecnología fundamental para entender cómo una red privada puede comunicarse con Internet y cómo un analista SOC interpreta el tráfico que entra y sale de una organización.

**Objetivos de aprendizaje**

Al finalizar este módulo podrás:

-   Comprender qué es NAT.

-   Entender por qué fue creado.

-   Saber cómo funciona internamente.

-   Diferenciar los tipos de NAT.

-   Comprender su relación con el Gateway.

-   Saber cómo aparece en un Firewall y en un SIEM.

-   Entender cómo puede ser aprovechado por un atacante.

-   Aplicarlo durante investigaciones en un SOC.

**1. ¿Qué es NAT?**

**NAT (Network Address Translation)** significa:

**Traducción de Direcciones de Red.**

Es una tecnología que permite **cambiar una dirección IP por otra** mientras un paquete atraviesa un router o un firewall.

En la mayoría de los casos:

-   Convierte una **IP privada** en una **IP pública**.

-   O convierte una **IP pública** en una **IP privada**.

**Definición sencilla**

Imagina una empresa con 500 computadoras.

Todas tienen IP privadas:

192.168.10.15

192.168.10.20

192.168.10.35

192.168.10.100

Pero la empresa solo contrató **una única IP pública**:

181.35.220.10

La pregunta es:

**¿Cómo hacen 500 computadoras para navegar por Internet usando una sola IP pública?**

La respuesta es:

**Gracias a NAT.**

**2. ¿Por qué existe NAT?**

Recordemos algo que vimos en el módulo de IP públicas y privadas.

Las direcciones IPv4 son limitadas.

Solo existen aproximadamente:

4.294 millones

Parece mucho\...

Pero no alcanza para asignar una IP pública a cada computadora, celular, TV, consola, reloj inteligente, cámara IP, etc.

Por eso se crearon las IP privadas y NAT.

**Sin NAT**

Imaginemos una empresa con:

1000 computadoras

Necesitaría:

1000 IP públicas

Sería extremadamente costoso y prácticamente inviable.

**Con NAT**

Solo necesita:

1 IP pública

o unas pocas.

**3. ¿Cómo funciona NAT?**

Supongamos:

Mi PC

IP Privada

192.168.1.25

Quiere acceder a:

www.google.com

(Una IP pública).

La PC envía el paquete al Gateway.

Recordemos:

PC

↓

Gateway

↓

Internet

Hasta aquí no hay nada nuevo.

Ahora aparece NAT.

El Gateway recibe:

Origen

192.168.1.25

Destino

142.250.xxx.xxx

Pero Internet no conoce esa IP privada.

Entonces el Gateway hace algo muy importante.

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

192.168.1.25

↓

Gateway

↓

NAT

↓

181.35.220.10

↓

Internet

↓

Google

**4. ¿Cómo vuelve la respuesta?**

Aquí aparece la magia de NAT.

Cuando Google responde:

Destino

181.35.220.10

El Gateway recuerda:

Esa conexión en realidad pertenecía a:

192.168.1.25

Entonces realiza la traducción inversa.

Internet

↓

181.35.220.10

↓

Gateway

↓

NAT

↓

192.168.1.25

↓

Mi PC

La computadora nunca sabe que su dirección fue modificada.

**5. ¿Cómo recuerda el Gateway quién hizo cada conexión?**

El Gateway mantiene una **Tabla NAT**.

Ejemplo:

  -------------------------------------------------------------------------
  **IP Privada**         **Puerto**   **IP Pública**           **Puerto**
  ---------------------- ------------ ------------------------ ------------
  192.168.1.25           50231        181.35.220.10            45001

  192.168.1.30           50122        181.35.220.10            45002

  192.168.1.45           51015        181.35.220.10            45003
  -------------------------------------------------------------------------

Observa algo importante.

Todos utilizan la misma IP pública.

Lo que cambia es el puerto.

Gracias a esto el Gateway sabe exactamente a quién devolver cada respuesta.

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

NAT funciona exactamente igual.

**6. Tipos de NAT**

**NAT Estático**

Una IP privada siempre corresponde a la misma IP pública.

Ejemplo:

192.168.10.10

↓

181.35.220.15

Siempre.

Muy utilizado para servidores.

**NAT Dinámico**

Existe un grupo de IP públicas.

Cada equipo recibe una disponible.

Ejemplo:

192.168.10.15

↓

181.35.220.20

Más tarde otro equipo podría utilizar esa misma IP.

**PAT (Port Address Translation)**

Es el más utilizado.

También llamado:

**NAT Overload**

Miles de equipos utilizan:

Una sola IP pública.

Se diferencian mediante los puertos.

Este es el NAT que encontrarás en casi todas las casas y empresas.

**7. NAT y el Firewall**

En muchas organizaciones:

PC

↓

Firewall

↓

Internet

El Firewall realiza simultáneamente:

-   NAT.

-   Filtrado.

-   Registro de logs.

-   IDS/IPS.

-   VPN.

Por eso un Firewall moderno suele ser también el Gateway.

**8. ¿Cómo aparece NAT en un SOC?**

Ejemplo:

IP Interna

192.168.10.25

↓

NAT

↓

181.35.220.10

↓

185.15.20.30

Como analista SOC debes responder:

-   ¿Qué usuario utilizaba la IP 192.168.10.25?

-   ¿Qué proceso inició la conexión?

-   ¿Era una conexión autorizada?

-   ¿Qué puerto utilizó?

-   ¿Fue bloqueada por el firewall?

**Otro ejemplo**

Alerta SIEM

IP Pública

181.35.220.10

↓

Descarga malware

El analista debe investigar:

¿Quién fue?

Gracias a la tabla NAT podrá descubrir:

181.35.220.10

↓

192.168.10.85

↓

Usuario

Juan Pérez

↓

PC-Ventas-03

Aquí se ve claramente por qué la tabla NAT es una pieza clave durante una investigación.

**9. ¿Cómo puede aprovechar NAT un atacante?**

**Caso 1 - Ocultar el origen**

Desde Internet solo se observa:

181.35.220.10

No se sabe inmediatamente cuál equipo interno realizó la conexión.

Por eso el analista debe consultar la tabla NAT.

**Caso 2 - Configuración incorrecta**

Si un administrador publica accidentalmente un servidor interno mediante NAT:

Servidor SQL

↓

Internet

Ese servidor queda expuesto.

Si además tiene una vulnerabilidad, un atacante podría comprometerlo.

**Caso 3 - Reglas de Port Forwarding inseguras**

Supongamos:

Internet

↓

Puerto 3389

↓

Servidor Windows

Si el acceso está expuesto sin controles adecuados:

-   Ataques de fuerza bruta.

-   Robo de credenciales.

-   Ransomware.

Este escenario ha sido responsable de numerosos incidentes reales.

**10. ¿Cómo defender una infraestructura NAT?**

-   Publicar solo los servicios necesarios.

-   Evitar exponer RDP directamente a Internet.

-   Revisar periódicamente las reglas de NAT.

-   Utilizar VPN para el acceso remoto.

-   Aplicar MFA para administradores.

-   Monitorear conexiones salientes y entrantes.

-   Registrar y conservar las tablas NAT cuando sea posible.

**11. Aplicación práctica en un SOC**

**Caso 1**

Firewall

Origen

192.168.20.25

↓

NAT

↓

181.35.220.10

↓

HTTPS

↓

Microsoft

Interpretación:

Tráfico normal de navegación.

**Caso 2**

Firewall

Origen

192.168.30.45

↓

NAT

↓

181.35.220.10

↓

185.220.xxx.xxx

↓

Puerto 4444

Como analista pensarías:

-   ¿Qué aplicación inició la conexión?

-   ¿El puerto es habitual?

-   ¿La IP tiene mala reputación?

-   ¿Existe un proceso malicioso?

-   ¿Se trata de comunicación con un servidor de Comando y Control (C2)?

**Caso 3**

Alerta

181.35.220.10

↓

Miles de conexiones por minuto

No puedes concluir inmediatamente que toda la empresa está comprometida.

Primero debes revisar:

-   La tabla NAT.

-   Qué equipos generaron las conexiones.

-   Qué procesos participaron.

-   Si todas pertenecen al mismo usuario o a distintos equipos.

**12. Cuadro comparativo**

  -------------------------------------------------------------------------------------------
  **Concepto**   **Función**
  -------------- ----------------------------------------------------------------------------
  IP Privada     Se utiliza dentro de la red local.

  IP Pública     Identifica a la organización en Internet.

  Gateway        Conecta la red local con otras redes.

  NAT            Traduce direcciones IP entre redes.

  PAT            Permite que muchos equipos compartan una sola IP pública mediante puertos.

  Tabla NAT      Registra la relación entre conexiones internas y externas.
  -------------------------------------------------------------------------------------------

**13. Lo que esperan de un Analista SOC Nivel 1**

Cuando observes un log como este:

Origen:

192.168.10.45

↓

NAT:

181.35.220.10

↓

Destino:

104.26.xxx.xxx

↓

Puerto:

443

Debes ser capaz de responder:

-   ¿Cuál es la IP privada?

-   ¿Cuál es la IP pública?

-   ¿Quién realizó la conexión?

-   ¿Qué aplicación utilizó el puerto 443?

-   ¿El tráfico parece normal?

-   ¿Qué muestra la tabla NAT?

-   ¿Fue una conexión permitida o bloqueada?

-   ¿Debe investigarse?

**Resumen**

**NAT**

-   Traduce direcciones IP.

-   Permite que IP privadas accedan a Internet.

-   Conserva las direcciones IPv4 públicas.

-   Funciona normalmente en el Gateway o Firewall.

**PAT**

-   Es el tipo de NAT más utilizado.

-   Permite que miles de dispositivos compartan una misma IP pública utilizando distintos puertos.

**Tabla NAT**

-   Relaciona IP privadas con IP públicas y puertos.

-   Es fundamental para las investigaciones de un SOC.

**NAT en un SOC**

Como analista, nunca debes quedarte solo con la IP pública. Tu objetivo es reconstruir el camino completo de la comunicación:

1.  **¿Qué equipo interno originó el tráfico?**

2.  **¿Qué usuario estaba utilizando ese equipo?**

3.  **¿Qué proceso generó la conexión?**

4.  **¿Hacia qué destino se conectó?**

5.  **¿Fue un comportamiento esperado o anómalo?**

**💡 Consejo como tu entrenador para un SOC**

Muchos principiantes creen que **NAT solo sirve para \"tener Internet\"**, pero en realidad es una de las primeras piezas que un analista utiliza para **atribuir una conexión a un equipo específico**.

Imagina que recibes un aviso del proveedor de Internet diciendo:

**\"Su IP pública 181.35.220.10 intentó conectarse a un servidor malicioso a las 14:32.\"**

Eso no identifica al culpable. En una empresa con cientos de equipos, todos comparten esa misma IP pública mediante PAT.

Tu trabajo como analista SOC será seguir el rastro:

-   Revisar los **logs del firewall**.

-   Consultar la **tabla NAT**.

-   Identificar la **IP privada** responsable.

-   Relacionarla con el **usuario**, el **equipo** y el **proceso** que inició la conexión.

Ese razonamiento es exactamente el que utilizan los analistas durante investigaciones reales y es una habilidad muy valorada en un **SOC Nivel 1**.

**📚 Evaluación -- Módulo 6: NAT (Network Address Translation)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Al finalizar encontrarás las respuestas con su justificación. Las preguntas están diseñadas con el estilo de una evaluación para un puesto de **Analista SOC Nivel 1**.

**Pregunta 1**

¿Qué significa la sigla **NAT**?

**A)** Network Access Technology

**B)** Network Address Translation

**C)** Network Authentication Tunnel

**D)** Network Application Transfer

**Pregunta 2**

¿Cuál es el principal objetivo de NAT?

**A)** Encriptar las comunicaciones entre dos equipos.

**B)** Traducir direcciones IP entre redes.

**C)** Asignar direcciones IP automáticamente.

**D)** Aumentar la velocidad de Internet.

**Pregunta 3**

¿Por qué fue necesario crear NAT?

**A)** Porque las direcciones IPv4 públicas son limitadas.

**B)** Porque las direcciones MAC se agotaron.

**C)** Porque los routers no pueden trabajar con IP públicas.

**D)** Porque IPv6 dejó de utilizarse.

**Pregunta 4**

¿Qué ocurre cuando una computadora con IP privada quiere acceder a Internet?

**A)** Cambia automáticamente su dirección IP por una dirección MAC.

**B)** El Gateway o Firewall traduce la IP privada a una IP pública mediante NAT.

**C)** El servidor de destino cambia su dirección IP.

**D)** La computadora recibe una nueva IP pública permanente.

**Pregunta 5**

¿Cuál es el tipo de NAT más utilizado en hogares y empresas?

**A)** NAT Estático.

**B)** NAT Dinámico.

**C)** PAT (Port Address Translation o NAT Overload).

**D)** NAT Inverso.

**Pregunta 6**

¿Qué información utiliza principalmente **PAT** para diferenciar múltiples conexiones que comparten una misma IP pública?

**A)** La dirección MAC.

**B)** El nombre del usuario.

**C)** Los números de puerto.

**D)** El sistema operativo.

**Pregunta 7**

Como analista SOC recibes la siguiente alerta:

IP Pública:

181.35.220.10

↓

Conexión sospechosa

↓

Puerto 4444

¿Cuál debería ser tu siguiente paso?

**A)** Concluir inmediatamente que toda la empresa está comprometida.

**B)** Buscar en la tabla NAT qué IP privada originó esa conexión.

**C)** Reiniciar el firewall.

**D)** Cambiar la IP pública del proveedor de Internet.

**Pregunta 8**

¿Cuál de las siguientes afirmaciones sobre NAT es correcta?

**A)** NAT reemplaza al firewall.

**B)** NAT elimina la necesidad de utilizar direcciones IP privadas.

**C)** NAT permite que varios equipos compartan una misma IP pública.

**D)** NAT bloquea automáticamente todos los ataques.

**Pregunta 9**

¿Qué riesgo representa una regla de **Port Forwarding** mal configurada?

**A)** Que una impresora deje de funcionar.

**B)** Que un servidor interno quede expuesto directamente a Internet.

**C)** Que la dirección MAC cambie automáticamente.

**D)** Que el Gateway deje de realizar NAT.

**Pregunta 10 (Caso práctico SOC)**

El SIEM genera la siguiente alerta:

IP Pública:

181.35.220.10

↓

Descarga detectada desde un dominio malicioso

↓

Hora:

15:42

¿Qué información necesitas para identificar el equipo responsable?

**A)** La dirección MAC del servidor remoto.

**B)** La tabla NAT del firewall para conocer qué IP privada realizó la conexión.

**C)** El modelo del router.

**D)** La versión del navegador del usuario.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

**NAT (Network Address Translation)** significa **Traducción de Direcciones de Red**. Su función principal es modificar direcciones IP cuando el tráfico pasa por un router o firewall.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

NAT traduce direcciones IP entre diferentes redes, generalmente de una IP privada a una IP pública (y viceversa para las respuestas).

**Pregunta 3**

✅ **Respuesta correcta: A**

**Justificación**

Las direcciones **IPv4 públicas son un recurso limitado**. NAT permite que miles de dispositivos compartan una o pocas direcciones IP públicas, reduciendo la necesidad de asignar una IP pública a cada equipo.

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

Cuando un equipo con IP privada accede a Internet, el Gateway o Firewall realiza NAT, sustituyendo la IP privada por una IP pública para que el tráfico pueda ser enrutado en Internet.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

**PAT (Port Address Translation)**, también conocido como **NAT Overload**, es el tipo de NAT más común. Permite que muchos dispositivos compartan una misma IP pública utilizando diferentes números de puerto.

**Pregunta 6**

✅ **Respuesta correcta: C**

**Justificación**

PAT utiliza los **puertos** para distinguir las conexiones de múltiples equipos que comparten una misma dirección IP pública.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

Una IP pública suele representar a toda una organización. Para identificar el equipo responsable es necesario consultar la **tabla NAT** y determinar qué IP privada originó la conexión.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación**

NAT permite que varios dispositivos utilicen una única IP pública para acceder a Internet. Esto no reemplaza al firewall ni bloquea ataques por sí mismo.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

Una regla de **Port Forwarding** puede publicar un servidor interno en Internet. Si está mal configurada o el servicio es vulnerable, un atacante podría explotarlo para acceder a la red.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

La **tabla NAT** relaciona las conexiones entre IP privadas, IP públicas y puertos. Es una fuente fundamental para identificar el equipo responsable de una actividad detectada desde la IP pública de la empresa.

**🏆 Resultado**

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Respuestas Correctas**   **Nivel**
  -------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  **10/10**                  ⭐ **Excelente.** Comprendes NAT no solo desde el punto de vista de redes, sino también desde la perspectiva de un Analista SOC.

  **8--9**                   🟢 **Muy buen nivel.** Ya puedes interpretar registros de NAT y comprender cómo rastrear conexiones desde una IP pública hasta un equipo interno.

  **6--7**                   🟡 **Buen progreso.** Repasa los tipos de NAT (especialmente PAT) y el funcionamiento de la tabla NAT.

  **4--5**                   🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar el flujo de traducción de direcciones y el papel del Gateway/Firewall.

  **0--3**                   🔴 **Es recomendable repasar el módulo completo.** NAT es un concepto esencial para investigar incidentes y atribuir actividad a equipos específicos en un SOC.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
