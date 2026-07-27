**Módulo de Estudio SOC**

**Módulo 5 - Subredes (Subnetting)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar:** Ya aprendiste sobre **IP públicas y privadas**, **Modelo OSI**, **Modelo TCP/IP** y **Máscaras de Subred**. Este módulo une todos esos conceptos. Comprender las subredes es uno de los conocimientos más importantes para trabajar en redes y en un SOC.

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es una subred.

-   Entender por qué las empresas dividen sus redes.

-   Diferenciar una red de una subred.

-   Interpretar una dirección de red.

-   Comprender el concepto de Broadcast.

-   Identificar el rango de hosts de una subred.

-   Entender cómo un atacante aprovecha una mala segmentación.

-   Aplicar estos conocimientos en investigaciones de un SOC.

**1. ¿Qué es una Subred?**

Una **subred (Subnet)** es una división lógica de una red más grande.

En lugar de tener una única red con cientos o miles de dispositivos, se crean varias redes pequeñas.

Por ejemplo:

Empresa

↓

Administración

↓

Ventas

↓

RRHH

↓

Servidores

↓

Invitados

Cada una funciona como una pequeña red independiente.

**¿Por qué existen las subredes?**

Sin subredes una empresa podría verse así:

192.168.1.0/24

↓

PC Administración

↓

PC Ventas

↓

PC RRHH

↓

Servidor

↓

Impresoras

↓

Cámaras

↓

Wi-Fi invitados

Todos los dispositivos están mezclados.

Problemas:

-   Mucho tráfico.

-   Menor rendimiento.

-   Más difícil de administrar.

-   Menor seguridad.

-   Mayor facilidad para el movimiento lateral de un atacante.

**Con subredes**

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

↓

Invitados

192.168.200.0/24

Cada área queda aislada.

**Ventajas**

✔ Más seguridad.

✔ Menor tráfico.

✔ Mejor rendimiento.

✔ Mejor organización.

✔ Mayor control.

**2. Componentes de una Subred**

Tomemos como ejemplo:

192.168.10.0/24

Aquí aparecen cuatro conceptos fundamentales.

**Dirección de Red**

192.168.10.0

Identifica toda la subred.

No se asigna a ningún equipo.

**Hosts**

Son los dispositivos.

Ejemplo:

192.168.10.1

↓

192.168.10.2

↓

192.168.10.3

↓

\...

↓

192.168.10.254

Todos estos pueden asignarse a computadoras, impresoras, servidores, etc.

**Broadcast**

Es la última dirección de la subred.

192.168.10.255

Sirve para enviar información a todos los dispositivos de esa subred.

No puede asignarse a un equipo.

**Gateway**

Generalmente:

192.168.10.1

Es la dirección del router o firewall.

Permite salir hacia otras redes.

**Resumen visual**

192.168.10.0

↓

Dirección de Red

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.10.1

↓

Gateway

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.10.2

↓

Host

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\...

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.10.254

↓

Host

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.10.255

↓

Broadcast

**3. ¿Cuántos hosts puede tener una subred?**

La cantidad depende de la máscara.

**/24**

255.255.255.0

Total de direcciones:

256

Se restan:

-   Dirección de Red

-   Broadcast

Resultado:

**254 hosts**

**/25**

255.255.255.128

Total:

128 direcciones.

Hosts disponibles:

126

**/26**

255.255.255.192

Hosts:

62

**/27**

Hosts:

30

**/28**

Hosts:

14

**/29**

Hosts:

6

**/30**

Hosts:

2

Muy utilizada para enlaces entre routers.

**Tabla rápida**

  ------------------------------------------------------------------------
  **CIDR**    **Máscara**                        **Hosts útiles**
  ----------- ---------------------------------- -------------------------
  /24         255.255.255.0                      254

  /25         255.255.255.128                    126

  /26         255.255.255.192                    62

  /27         255.255.255.224                    30

  /28         255.255.255.240                    14

  /29         255.255.255.248                    6

  /30         255.255.255.252                    2
  ------------------------------------------------------------------------

**4. Ejemplo práctico**

Empresa:

50 empleados.

Una sola red:

192.168.1.0/24

Puede funcionar.

Pero la empresa crece.

Ahora tiene:

-   RRHH

-   Administración

-   Ventas

-   Sistemas

-   Servidores

-   Wi-Fi invitados

Conviene dividirla.

Resultado:

Administración

192.168.10.0/24

\-\-\-\-\-\-\-\-\-\-\-\-\--

Ventas

192.168.20.0/24

\-\-\-\-\-\-\-\-\-\-\-\-\--

RRHH

192.168.30.0/24

\-\-\-\-\-\-\-\-\-\-\-\-\--

Servidores

192.168.100.0/24

\-\-\-\-\-\-\-\-\-\-\-\-\--

Invitados

192.168.200.0/24

Cada departamento queda aislado.

**5. ¿Cómo puede aprovechar esto un atacante?**

**Caso 1**

Toda la empresa está en:

192.168.1.0/24

El atacante compromete:

192.168.1.25

Ahora puede escanear:

192.168.1.1

↓

192.168.1.254

Descubrir:

-   Servidores.

-   Cámaras.

-   Impresoras.

-   NAS.

-   Controlador de dominio.

**Caso 2**

Empresa segmentada.

192.168.10.0/24

Administración

↓

192.168.20.0/24

Ventas

↓

192.168.30.0/24

RRHH

↓

192.168.100.0/24

Servidores

Aunque comprometa un equipo de Ventas, el atacante no necesariamente podrá llegar a los servidores. Tendrá que superar los controles entre subredes (firewalls, ACL, etc.).

**Movimiento lateral**

Una mala segmentación facilita:

PC

↓

Servidor

↓

Controlador de Dominio

↓

Toda la empresa

Una buena segmentación dificulta ese avance.

**6. ¿Cómo defender una red?**

-   Crear subredes.

-   Utilizar VLAN.

-   Firewalls internos.

-   ACL.

-   Zero Trust.

-   Menor privilegio.

-   Segmentar servidores críticos.

-   Separar la red de invitados de la red corporativa.

**7. Aplicación práctica en un SOC**

Un Analista SOC observa constantemente direcciones de subred.

Debe interpretarlas rápidamente.

**Ejemplo 1**

Firewall

Permitir

192.168.20.0/24

↓

192.168.100.10

Interpretación:

Solo la red de Ventas puede acceder a ese servidor.

**Ejemplo 2**

SIEM

Origen

192.168.20.45

↓

Destino

192.168.20.1-254

Interpretación:

Escaneo de toda la subred.

Puede tratarse de reconocimiento.

**Ejemplo 3**

Logs

192.168.20.15

↓

192.168.30.10

Interpretación:

Comunicación entre subredes.

El analista debe validar:

-   ¿Está permitida?

-   ¿Es normal?

-   ¿Existe una regla de firewall que la autorice?

**Ejemplo 4**

Firewall

Bloqueado

192.168.200.20

↓

192.168.100.10

Interpretación:

Un equipo de la red de invitados intentó acceder a un servidor corporativo.

La política de segmentación funcionó correctamente.

**8. Cuadro comparativo**

  ----------------------------------------------------------------------------------
  **Concepto**       **Descripción**
  ------------------ ---------------------------------------------------------------
  Red                Conjunto de dispositivos que pueden comunicarse.

  Subred             División lógica de una red.

  Dirección de Red   Identifica la subred (ej.: 192.168.10.0).

  Host               Dispositivo dentro de la subred.

  Broadcast          Última dirección de la subred; envía datos a todos los hosts.

  Gateway            Router o firewall que conecta con otras redes.
  ----------------------------------------------------------------------------------

**9. Diferencias entre Red y Subred**

  -------------------------------------------------------------------------
  **Red**                                 **Subred**
  --------------------------------------- ---------------------------------
  Puede ser muy grande.                   Es una parte de una red.

  Contiene varias subredes.               Contiene hosts.

  Menor organización si no se segmenta.   Mejor organización y seguridad.

  Mayor superficie de ataque.             Limita el movimiento lateral.
  -------------------------------------------------------------------------

**10. Lo que esperan de un Analista SOC Nivel 1**

Cuando veas una dirección como:

192.168.30.15/24

deberías responder mentalmente:

-   ¿Cuál es la dirección de red?

-   ¿Cuál es el broadcast?

-   ¿Cuál es el rango de hosts?

-   ¿Pertenece a la misma subred que otro equipo?

-   ¿Necesita pasar por un router?

-   ¿Qué firewall controla esa comunicación?

-   ¿El tráfico entre subredes es esperado?

-   ¿Podría tratarse de movimiento lateral?

**11. Resumen**

**Subred**

Es una división lógica de una red más grande.

**Dirección de Red**

Identifica toda la subred.

No se asigna a dispositivos.

**Host**

Es cualquier dispositivo de la red.

**Broadcast**

Permite enviar un mensaje a todos los dispositivos de la subred.

**Gateway**

Conecta una subred con otras redes.

**Segmentación**

Reduce el riesgo de ataques y facilita la administración.

**12. Conceptos clave para memorizar**

  -----------------------------------------------------------------------
  **Concepto**         **Debes recordar**
  -------------------- --------------------------------------------------
  Subred               División lógica de una red.

  Dirección de Red     Primera dirección; identifica la subred.

  Broadcast            Última dirección; comunica con todos los hosts.

  Gateway              Punto de salida hacia otras redes.

  Host                 Equipo dentro de una subred.

  Segmentación         Mejora seguridad y rendimiento.

  Movimiento lateral   Más difícil cuando la red está bien segmentada.
  -----------------------------------------------------------------------

**💡 Consejo como tu entrenador para un SOC**

Este es uno de los temas donde muchos principiantes se confunden porque mezclan **máscara**, **subred**, **CIDR** y **rango de hosts**.

Piensa en este orden:

1.  **La dirección IP** identifica un equipo.

2.  **La máscara** indica dónde termina la parte de red y dónde empieza la parte de host.

3.  **La subred** es el conjunto de equipos que comparten esa parte de red.

4.  **El gateway** conecta esa subred con otras.

5.  **El firewall** controla qué comunicaciones pueden pasar entre subredes.

Cuando analices un log en un SOC, acostúmbrate a hacer este razonamiento:

-   ¿Origen y destino están en la misma subred?

-   Si no lo están, ¿por qué intentan comunicarse?

-   ¿Existe una regla que lo permita?

-   ¿Es un comportamiento normal o un posible movimiento lateral?

Ese enfoque te permitirá interpretar alertas de red con rapidez y tomar mejores decisiones durante una investigación.

**📚 Evaluación -- Módulo 5: Subredes (Subnetting)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Imagina que estás realizando un examen para ingresar a un puesto de **Analista SOC Nivel 1**. Al finalizar encontrarás las respuestas con su justificación.

**Pregunta 1**

¿Qué es una **subred**?

**A)** Una dirección IP pública.

**B)** Una división lógica de una red más grande.

**C)** Un tipo de firewall.

**D)** Un protocolo de red.

**Pregunta 2**

¿Cuál es el principal objetivo de crear subredes en una empresa?

**A)** Aumentar automáticamente la velocidad de Internet.

**B)** Organizar la red, mejorar la seguridad y reducir el tráfico innecesario.

**C)** Eliminar la necesidad de utilizar routers.

**D)** Evitar el uso de direcciones IP.

**Pregunta 3**

En la subred **192.168.10.0/24**, ¿cuál es la dirección de red?

**A)** 192.168.10.1

**B)** 192.168.10.254

**C)** 192.168.10.0

**D)** 192.168.10.255

**Pregunta 4**

En la misma subred **192.168.10.0/24**, ¿cuál es la dirección de broadcast?

**A)** 192.168.10.0

**B)** 192.168.10.1

**C)** 192.168.10.254

**D)** 192.168.10.255

**Pregunta 5**

¿Cuál de las siguientes direcciones **no puede asignarse a un equipo** dentro de una subred /24?

**A)** 192.168.10.25

**B)** 192.168.10.100

**C)** 192.168.10.0

**D)** 192.168.10.200

**Pregunta 6**

¿Cuántos hosts útiles tiene una subred **/26**?

**A)** 30

**B)** 62

**C)** 126

**D)** 254

**Pregunta 7**

¿Qué dispositivo suele utilizarse como **Gateway** dentro de una subred?

**A)** Una impresora.

**B)** Un router o un firewall.

**C)** Un teclado.

**D)** Un monitor.

**Pregunta 8**

¿Por qué una buena segmentación de la red mejora la seguridad?

**A)** Porque elimina todos los ataques.

**B)** Porque dificulta el movimiento lateral de un atacante entre diferentes áreas de la empresa.

**C)** Porque convierte todas las IP privadas en públicas.

**D)** Porque evita la necesidad de utilizar antivirus.

**Pregunta 9**

Como analista SOC recibes la siguiente alerta:

Origen:

192.168.20.15

Destino:

192.168.30.25

¿Cuál es la conclusión más probable?

**A)** Ambos equipos pertenecen a la misma subred.

**B)** La comunicación requiere pasar por un router o firewall.

**C)** El tráfico no puede existir.

**D)** Se trata obligatoriamente de un ataque.

**Pregunta 10 (Caso práctico SOC)**

El SIEM genera la siguiente alerta:

Host origen:

192.168.50.15

Actividad:

Conexiones hacia:

192.168.50.1

↓

192.168.50.254

Tiempo:

12 segundos

¿Cuál sería tu primera hipótesis?

**A)** El usuario está navegando normalmente por Internet.

**B)** El equipo está realizando un reconocimiento o escaneo de la subred.

**C)** Se está actualizando el sistema operativo.

**D)** El firewall está fallando.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

Una **subred** es una división lógica de una red más grande. Permite organizar mejor los dispositivos y aplicar políticas de seguridad más específicas.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

Las subredes permiten:

-   Reducir el tráfico de broadcast.

-   Mejorar el rendimiento.

-   Organizar los dispositivos.

-   Aumentar la seguridad mediante la segmentación.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

En una red **192.168.10.0/24**, la dirección **192.168.10.0** identifica a toda la subred y no se asigna a ningún dispositivo.

**Pregunta 4**

✅ **Respuesta correcta: D**

**Justificación**

En una red **/24**, la última dirección (**192.168.10.255**) es la dirección de **broadcast**, utilizada para enviar información a todos los equipos de la subred.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

La dirección **192.168.10.0** es la dirección de red y está reservada. No puede asignarse a un host.

**Nota:** En una /24, la dirección **192.168.10.255** tampoco podría asignarse porque es el broadcast.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

Una subred **/26** dispone de:

-   64 direcciones totales.

-   1 dirección de red.

-   1 dirección de broadcast.

Resultado:

**62 hosts útiles.**

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

El **Gateway** suele ser un router, un firewall o un switch de capa 3. Es el dispositivo que conecta la subred con otras redes.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

La segmentación limita el alcance de un atacante. Si compromete un equipo de una subred, tendrá más dificultades para acceder a otras subredes protegidas por firewalls o ACL.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

Las direcciones **192.168.20.X** y **192.168.30.X** pertenecen a subredes distintas. Para comunicarse, el tráfico normalmente debe pasar por un router o firewall.

Como analista SOC, deberías comprobar si esa comunicación está permitida y si es un comportamiento esperado.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Un equipo que intenta conectarse rápidamente a todas las direcciones de una misma subred presenta un patrón típico de **reconocimiento (Network Scanning)**.

Herramientas como **Nmap** o **Masscan** pueden generar este tipo de actividad. En un SOC, esta alerta suele investigarse porque puede ser el primer paso antes de un ataque.

**🏆 Resultado**

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Respuestas Correctas**   **Nivel**
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  **10/10**                  ⭐ **Excelente.** Comprendes cómo funcionan las subredes y cómo aplicarlas en investigaciones de un SOC.

  **8--9**                   🟢 **Muy buen nivel.** Ya puedes interpretar comunicaciones entre subredes y comprender la segmentación de una red empresarial.

  **6--7**                   🟡 **Buen progreso.** Repasa especialmente los conceptos de dirección de red, broadcast y cantidad de hosts.

  **4--5**                   🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar el módulo antes de avanzar.

  **0--3**                   🔴 **Es recomendable repasar el tema completo.** Las subredes son fundamentales para interpretar alertas de firewall, SIEM y análisis de tráfico.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
