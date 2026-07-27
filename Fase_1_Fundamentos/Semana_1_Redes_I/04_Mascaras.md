**Módulo de Estudio SOC**

**Módulo 4 - Máscaras de Subred (Subnet Mask)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es una máscara de subred.

-   Entender por qué existe.

-   Saber cómo identificar una red y un host.

-   Interpretar la notación CIDR (/24, /16, /8, etc.).

-   Comprender cómo se utiliza en una red empresarial.

-   Identificar cómo un atacante puede aprovechar una mala segmentación.

-   Saber cómo un Analista SOC utiliza las máscaras de subred en una investigación.

**1. ¿Qué es una máscara de subred?**

Una **máscara de subred (Subnet Mask)** es un número que le indica a un dispositivo:

-   Qué parte de una dirección IP identifica la **red**.

-   Qué parte identifica al **equipo (host)**.

En otras palabras:

**La máscara le dice a una computadora quién pertenece a su misma red y quién no.**

**Analogía**

Imagina una ciudad.

La dirección completa es:

Av. San Martín 2500

Departamento 8

Podemos dividirla así:

Av. San Martín 2500

↓

La calle (RED)

Departamento 8

↓

El HOST

La máscara hace exactamente eso.

Divide una IP en dos partes:

RED \| HOST

**¿Por qué existe?**

Sin máscara de subred, una computadora no sabría:

-   Si el destino está dentro de su red.

-   Si debe enviar los datos directamente.

-   Si debe enviarlos al router.

Es una información esencial para que el tráfico llegue al destino correcto.

**2. Estructura de una dirección IPv4**

Recordemos que una IP tiene **32 bits**.

Ejemplo:

192.168.1.20

En binario:

11000000.10101000.00000001.00010100

No hace falta memorizar el binario, pero es importante saber que la máscara también está formada por 32 bits.

**3. ¿Qué hace realmente una máscara?**

Supongamos:

IP:

192.168.1.35

Máscara:

255.255.255.0

La máscara indica que:

192.168.1 \| 35

RED HOST

Todos los equipos que comiencen con:

192.168.1.X

pertenecen a la misma red.

**Ejemplo**

PC 1

192.168.1.20

PC 2

192.168.1.45

Máscara

255.255.255.0

Resultado:

Ambas están en la misma red.

Pueden comunicarse directamente.

Ahora:

PC 3

192.168.2.15

Con la misma máscara:

255.255.255.0

Ya pertenece a otra red.

Necesita pasar por un router.

**4. Las máscaras más comunes**

**/8**

Máscara:

255.0.0.0

Ejemplo

10.25.18.40

La red es:

10

Todo lo demás corresponde a los hosts.

**/16**

Máscara

255.255.0.0

Ejemplo

172.20.15.30

Red

172.20

Host

15.30

**/24 (La más utilizada)**

Máscara

255.255.255.0

Ejemplo

192.168.1.80

Red

192.168.1

Host

80

**/32**

Máscara

255.255.255.255

Representa un único equipo.

Muy utilizada en:

-   Firewalls

-   ACL

-   VPN

-   Reglas de seguridad

**5. ¿Qué significa la notación CIDR?**

En lugar de escribir:

255.255.255.0

se escribe:

/24

¿Por qué?

Porque existen **24 bits** destinados a la red.

Ejemplos

  -----------------------------------------------------------------------
  **CIDR**          **Máscara**
  ----------------- -----------------------------------------------------
  /8                255.0.0.0

  /16               255.255.0.0

  /24               255.255.255.0

  /25               255.255.255.128

  /26               255.255.255.192

  /27               255.255.255.224

  /28               255.255.255.240

  /29               255.255.255.248

  /30               255.255.255.252

  /32               255.255.255.255
  -----------------------------------------------------------------------

**6. ¿Para qué sirven las subredes?**

Una empresa no suele tener una sola red.

Puede dividirla así:

Administración

192.168.10.0/24

↓

Ventas

192.168.20.0/24

↓

RRHH

192.168.30.0/24

↓

Servidores

192.168.100.0/24

Cada departamento trabaja en su propia subred.

Esto mejora:

-   Organización.

-   Rendimiento.

-   Seguridad.

-   Control del tráfico.

**7. ¿Cómo puede aprovechar esto un atacante?**

**Mala segmentación**

Si toda la empresa utiliza:

192.168.1.0/24

un atacante que comprometa una PC puede:

-   Escanear toda la red.

-   Buscar servidores.

-   Buscar impresoras.

-   Buscar cámaras IP.

-   Buscar controladores de dominio.

**Movimiento lateral**

Supongamos:

192.168.10.15

↓

192.168.10.40

↓

192.168.10.80

↓

Servidor

Si todos pertenecen a la misma subred y no existen controles, el atacante puede desplazarse con mayor facilidad.

**Descubrimiento de red**

Mediante herramientas como:

-   Nmap

-   Angry IP Scanner

-   Masscan

el atacante puede identificar rápidamente los equipos activos de una subred.

**8. ¿Cómo defender una red?**

-   Crear subredes por función.

-   Utilizar VLAN.

-   Limitar la comunicación entre redes.

-   Aplicar ACL.

-   Configurar firewalls internos.

-   Implementar el principio de menor privilegio.

-   Monitorear el tráfico entre subredes.

**9. Aplicación práctica en un SOC**

Las máscaras aparecen constantemente en:

-   Firewalls.

-   SIEM.

-   IDS/IPS.

-   Logs.

-   VPN.

-   Reglas de acceso.

Un analista SOC debe interpretarlas rápidamente.

**Ejemplo 1**

Alerta

192.168.20.45

↓

192.168.20.200

Máscara

/24

Interpretación:

Ambos equipos pertenecen a la misma red.

No necesitan pasar por el router para comunicarse.

**Ejemplo 2**

Alerta

192.168.20.45

↓

192.168.30.15

Interpretación:

El tráfico debe pasar por un router o firewall.

Como analista SOC deberías verificar:

-   ¿Está permitido ese tráfico?

-   ¿Existe una regla que lo autorice?

-   ¿Es un comportamiento esperado?

**Ejemplo 3**

Firewall

Permitir

192.168.10.0/24

↓

192.168.100.10

Interpretación:

Solo los equipos de la red **192.168.10.0/24** pueden acceder a ese servidor.

**Ejemplo 4**

SIEM

Escaneo detectado

Origen

192.168.1.50

Destino

192.168.1.1-254

Interpretación:

Un equipo está intentando descubrir todos los dispositivos de la subred.

Puede tratarse de un reconocimiento previo a un ataque.

**10. Cuadro comparativo de máscaras comunes**

  -----------------------------------------------------------------------------------
  **Máscara**       **CIDR**   **Hosts aproximados**   **Uso común**
  ----------------- ---------- ----------------------- ------------------------------
  255.0.0.0         /8         16.777.214              Redes muy grandes

  255.255.0.0       /16        65.534                  Empresas grandes

  255.255.255.0     /24        254                     Oficinas y LAN

  255.255.255.128   /25        126                     Dividir una LAN

  255.255.255.192   /26        62                      Redes pequeñas

  255.255.255.224   /27        30                      Segmentación específica

  255.255.255.240   /28        14                      Pequeños grupos de equipos

  255.255.255.248   /29        6                       Enlaces o pocos dispositivos

  255.255.255.252   /30        2                       Enlaces punto a punto

  255.255.255.255   /32        1                       Un único host
  -----------------------------------------------------------------------------------

**Nota:** Los valores de \"hosts aproximados\" se refieren a IPv4 y consideran las direcciones reservadas de red y broadcast cuando aplican.

**11. Lo que esperan de un Analista SOC Nivel 1**

Cuando veas una dirección como:

192.168.50.25/24

deberías poder responder rápidamente:

-   ¿Cuál es la red?

-   ¿Qué máscara utiliza?

-   ¿Pertenece a la misma subred que otro equipo?

-   ¿Debe pasar por un router?

-   ¿Ese tráfico es normal?

-   ¿Hay un escaneo de la subred?

-   ¿Existe movimiento lateral?

-   ¿Qué firewall controla esa comunicación?

**12. Resumen**

**Máscara de Subred**

-   Divide una IP en **Red** y **Host**.

-   Determina quién puede comunicarse directamente.

-   Permite crear subredes.

-   Mejora el rendimiento y la seguridad.

-   Es esencial para el enrutamiento.

**CIDR**

-   Es una forma abreviada de escribir la máscara.

-   **/24** equivale a **255.255.255.0**.

-   Cuanto mayor es el número, **más pequeña** suele ser la red y **menos hosts** puede contener.

**Subredes**

Permiten:

-   Organizar redes.

-   Aumentar la seguridad.

-   Limitar el movimiento lateral.

-   Facilitar el monitoreo.

-   Aplicar controles de acceso.

**13. Conceptos clave para memorizar**

  -----------------------------------------------------------------------------------------------
  **Concepto**         **Debes recordar**
  -------------------- --------------------------------------------------------------------------
  Máscara de Subred    Divide una IP en Red y Host.

  CIDR                 Notación abreviada de la máscara (/24, /16, etc.).

  Subred               Grupo de dispositivos que comparten la misma parte de red.

  Router               Comunica distintas subredes.

  VLAN                 Segmenta una red lógica para mejorar seguridad y administración.

  Movimiento lateral   Un atacante se desplaza entre equipos de una misma o distintas subredes.
  -----------------------------------------------------------------------------------------------

**💡 Consejo como tu entrenador para un SOC**

Este tema suele intimidar porque aparecen números como **/24**, **/27** o **255.255.255.192**. Sin embargo, en un **SOC Nivel 1** no se espera que calcules subredes complejas de memoria.

Lo que sí se espera es que puedas responder rápidamente preguntas como:

-   **¿Estos dos equipos están en la misma subred?**

-   **¿Ese tráfico debería pasar por un router o firewall?**

-   **¿El atacante está escaneando solo una subred o toda la red corporativa?**

-   **¿Qué segmento de la empresa está siendo afectado?**

Con esa capacidad podrás interpretar mejor los logs, las reglas de firewall y las alertas del SIEM. Más adelante aprenderemos a calcular subredes manualmente, pero primero es importante dominar el concepto y saber aplicarlo durante una investigación de seguridad.

**Evaluación -- Módulo 4: Máscaras de Subred (Subnet Mask)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Al finalizar, revisa las respuestas y sus justificaciones.

**Pregunta 1**

¿Cuál es la función principal de una máscara de subred?

**A)** Aumentar la velocidad de Internet.

**B)** Dividir una dirección IP en una parte de red y una parte de host.

**C)** Encriptar las direcciones IP.

**D)** Asignar automáticamente direcciones IP.

**Pregunta 2**

¿Cuál de las siguientes máscaras corresponde a una red **/24**?

**A)** 255.0.0.0

**B)** 255.255.0.0

**C)** 255.255.255.0

**D)** 255.255.255.255

**Pregunta 3**

¿Qué representa la notación **/16**?

**A)** Que existen 16 computadoras en la red.

**B)** Que los primeros 16 bits corresponden a la parte de red.

**C)** Que la red tiene 16 routers.

**D)** Que solo existen 16 direcciones IP disponibles.

**Pregunta 4**

Dos computadoras tienen las siguientes configuraciones:

PC 1

192.168.1.25

Máscara

255.255.255.0

PC 2

192.168.1.200

Máscara

255.255.255.0

¿Qué afirmación es correcta?

**A)** Están en redes diferentes.

**B)** No pueden comunicarse.

**C)** Pertenecen a la misma subred.

**D)** Necesitan obligatoriamente un router para comunicarse.

**Pregunta 5**

¿Cuál de las siguientes direcciones pertenece a una red distinta si todas utilizan la máscara **255.255.255.0**?

**A)** 192.168.1.15

**B)** 192.168.1.40

**C)** 192.168.1.250

**D)** 192.168.2.15

**Pregunta 6**

¿Qué dispositivo permite comunicar dos subredes diferentes?

**A)** Hub

**B)** Switch

**C)** Router

**D)** Tarjeta de red

**Pregunta 7**

¿Cuál es una ventaja de dividir una empresa en varias subredes?

**A)** Eliminar la necesidad de usar direcciones IP.

**B)** Mejorar la organización y limitar el movimiento lateral de un atacante.

**C)** Hacer que todos los equipos sean visibles desde Internet.

**D)** Evitar el uso de firewalls.

**Pregunta 8**

Como analista SOC recibes la siguiente alerta:

Origen:

192.168.10.25

Destino:

192.168.10.150

Máscara:

/24

¿Qué puedes concluir inmediatamente?

**A)** Los equipos pertenecen a la misma subred.

**B)** Los equipos están en países diferentes.

**C)** El tráfico debe pasar por Internet.

**D)** Es obligatorio utilizar una VPN.

**Pregunta 9**

¿Qué tipo de actividad podría indicar el siguiente registro?

Origen:

192.168.1.45

Destino:

192.168.1.1

↓

192.168.1.254

**A)** Un usuario está imprimiendo un documento.

**B)** Un escaneo de red o reconocimiento.

**C)** Una actualización automática del sistema operativo.

**D)** Un cambio de contraseña.

**Pregunta 10 (Caso práctico SOC)**

Un firewall tiene la siguiente regla:

Permitir

192.168.20.0/24

↓

Servidor

192.168.100.10

¿Qué significa esta regla?

**A)** Solo los equipos pertenecientes a la red 192.168.20.0/24 pueden acceder al servidor.

**B)** Cualquier equipo de Internet puede acceder al servidor.

**C)** El servidor solo puede acceder a Internet.

**D)** El firewall está bloqueando todo el tráfico.

**Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

La máscara de subred divide una dirección IP en dos partes:

-   **Red**

-   **Host**

Gracias a esta división, un dispositivo puede determinar si el destino pertenece a su misma red o si debe enviar el tráfico a un router.

**Pregunta 2**

✅ **Respuesta correcta: C**

**Justificación**

La máscara correspondiente a **/24** es:

255.255.255.0

Es la máscara más utilizada en redes domésticas y muchas redes empresariales.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

La notación **/16** indica que **los primeros 16 bits** identifican la red y los **16 bits restantes** identifican a los hosts.

No indica la cantidad de computadoras ni de routers.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

Con una máscara **255.255.255.0 (/24)**, las direcciones:

-   192.168.1.25

-   192.168.1.200

comparten la misma parte de red (**192.168.1**), por lo que pertenecen a la misma subred y pueden comunicarse directamente.

**Pregunta 5**

✅ **Respuesta correcta: D**

**Justificación**

Con una máscara **/24**, la parte de red corresponde a los tres primeros octetos.

Por lo tanto:

-   **192.168.1.X** → misma red.

-   **192.168.2.X** → red diferente.

**Pregunta 6**

✅ **Respuesta correcta: C**

**Justificación**

El **router** es el dispositivo encargado de comunicar diferentes redes o subredes.

Recuerda:

-   **Switch** → misma red.

-   **Router** → distintas redes.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

La segmentación mediante subredes mejora:

-   La organización.

-   El rendimiento.

-   La seguridad.

-   La contención de ataques y del movimiento lateral.

**Pregunta 8**

✅ **Respuesta correcta: A**

**Justificación**

Con una máscara **/24**, ambas direcciones pertenecen a la red **192.168.10.0/24**.

Esto significa que están en la misma subred.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

Cuando un equipo intenta conectarse a una gran cantidad de direcciones IP dentro de la misma subred, es un comportamiento típico de un **escaneo de red** o actividad de reconocimiento.

Como analista SOC, esta alerta merece investigación.

**Pregunta 10**

✅ **Respuesta correcta: A**

**Justificación**

La regla permite que **únicamente los equipos pertenecientes a la subred 192.168.20.0/24** accedan al servidor ubicado en **192.168.100.10**.

Este tipo de reglas es habitual para limitar el acceso a recursos críticos.

**Resultado**

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Respuestas Correctas**   **Nivel**
  -------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **10/10**                  ⭐ Excelente. Comprendes el propósito de las máscaras de subred y cómo aplicarlas en investigaciones de un SOC.

  **8--9**                   🟢 Muy buen nivel. Ya puedes interpretar la mayoría de las reglas de red y de firewall relacionadas con subredes.

  **6--7**                   🟡 Buen progreso. Repasa la relación entre la máscara, la parte de red y la parte de host.

  **4--5**                   🟠 Necesitas reforzar los conceptos de CIDR y segmentación antes de avanzar a temas más complejos.

  **0--3**                   🔴 Te recomiendo volver a estudiar el módulo. Entender las máscaras de subred es fundamental para analizar tráfico, interpretar reglas de firewall y comprender la segmentación en un SOC.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
