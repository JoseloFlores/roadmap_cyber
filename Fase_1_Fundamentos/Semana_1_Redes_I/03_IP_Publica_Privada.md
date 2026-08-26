**Ciberseguridad para <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Módulo 1 - Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

-   Diferenciar una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública de una privada.

-   Entender cuándo se utiliza cada una.

-   Saber cómo un atacante puede aprovecharlas.

-   Aprender las medidas de defensa.

-   Relacionar este conocimiento con el trabajo diario de un analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?**

Una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> (Internet Protocol Address) es un identificador único que recibe cada dispositivo conectado a una red.

Es equivalente a la dirección de una casa.

Así como el correo necesita una dirección para entregar una carta, Internet necesita una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> para enviar y recibir información.

Ejemplos:

192.168.1.15
10.0.0.50
172.16.5.22
8.8.8.8
181.45.221.33

Sin direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, ningún dispositivo podría comunicarse.

**2. Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública**

**Definición**

Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública es la dirección con la que una red aparece en Internet.

Es visible para cualquier servidor del mundo.

Cuando ingresas a una página web, esa página puede ver tu <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

Ejemplo:

181.45.25.120

**¿Quién la asigna?**

Generalmente:

-   ISP (Proveedor de Internet)

Ejemplos:

-   Fibertel

-   Movistar

-   Claro

-   Personal

**Características**

✔ Es única en Internet.

✔ Puede verse desde cualquier parte del mundo.

✔ Permite la comunicación con Internet.

✔ Puede cambiar (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> dinámica).

✔ Puede ser fija (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> estática).

**Analogía**

Imagina un edificio.

La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública sería:

Av. Corrientes 1234

Todo el mundo conoce esa dirección.

Dentro del edificio hay departamentos.

Esos departamentos serían las <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas.

**Ejemplo real**

Casa:

Router

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública

181.45.25.120

Dentro de la casa:

Notebook
Celular
Smart TV
PlayStation

Todos usan la misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública para salir a Internet.

**Ventajas**

-   Acceso a Internet

-   Permite servidores

-   Acceso remoto

-   <a href="../../GLOSARIO.md#vpn" target="_blank">VPN</a>

**Desventajas**

Al ser visible también puede ser atacada.

**¿Qué puede ver Internet?**

Internet puede ver:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública

Puertos abiertos

Servicios expuestos

Ubicación aproximada

Proveedor de Internet

**3. Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada**

**Definición**

Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada solo existe dentro de una red local.

No puede utilizarse directamente en Internet.

**Rangos reservados**

**Clase A**

10.0.0.0
hasta

10.255.255.255

**Clase B**

172.16.0.0

hasta

172.31.255.255

**Clase C**

192.168.0.0

hasta

192.168.255.255

**Ejemplos**

192.168.1.5

192.168.1.20

10.0.0.15

172.20.5.6

**¿Quién las asigna?**

Generalmente el router mediante <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**Características**

✔ Solo funcionan dentro de la red.

✔ No son visibles en Internet.

✔ Pueden repetirse en millones de hogares.

Por ejemplo:

Tu PC:

192.168.1.100

Y la PC de otra persona:

192.168.1.100

No existe conflicto porque pertenecen a redes distintas.

**Analogía**

Si la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública es la dirección del edificio,

la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada sería:

Departamento 4B

Solo tiene sentido dentro del edificio.

**Ventajas**

-   Mayor seguridad

-   No consumen <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas

-   Organización interna

-   Facilitan el uso de <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>

**¿Cómo salen a Internet?**

Aquí aparece un concepto muy importante.

**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (Network Address Translation)**

El router traduce todas las <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas hacia una única <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

Ejemplo:

PC

192.168.1.10

↓

Router

↓

181.45.25.120

↓

Internet

Miles de dispositivos pueden compartir una sola <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

**4. Cuadro comparativo**

  ------------------------------------------------------------------------------------------
  **Característica**                  **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública**   **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada**
  ----------------------------------- ---------------- -------------------------------------
  Visible desde Internet              Sí               No

  Puede repetirse                     No               Sí

  Acceso mundial                      Sí               No

  Asignada por ISP                    Sí               No

  Asignada por Router                 No               Sí

  Se utiliza para navegar             Sí               Indirectamente

  Puede recibir conexiones externas   Sí               No (salvo configuración específica)

  Seguridad                           Menor            Mayor

  Necesita <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>                        No               Sí
  ------------------------------------------------------------------------------------------

**Similitudes**

Las <a href="../../GLOSARIO.md#dos" target="_blank">dos</a>:

-   Son direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

-   Identifican dispositivos.

-   Permiten comunicación.

-   Utilizan IPv4 o IPv6.

-   Forman parte del protocolo <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**5. ¿Cómo puede aprovecharlas un atacante?**

**Ataques contra <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública**

**Escaneo de puertos**

El atacante identifica:

Puertos abiertos

Servicios

Versiones

Sistema operativo

Herramientas comunes:

-   Nmap

-   Masscan

-   RustScan

**Fuerza bruta**

Si encuentra abiertos:

22 <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

3389 RDP

21 <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

23 Telnet

Intentará miles de contraseñas.

**Explotación de vulnerabilidades**

Ejemplo:

Servidor web desactualizado.

El atacante aprovecha un fallo conocido para obtener acceso.

**Ataques <a href="../../GLOSARIO.md#ddos" target="_blank">DDoS</a>**

Miles de equipos atacan una misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

Resultado:

El servicio deja de responder.

**Enumeración**

Obtiene información:

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

-   Certificados

-   Versiones

-   Servicios

-   Software instalado

**Ataques contra <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada**

Generalmente ocurren después de comprometer la red.

Ejemplos:

**Movimiento lateral**

Compromete:

PC 1

↓

PC 2

↓

Servidor

↓

Controlador de dominio

**Escaneo interno**

Busca:

Impresoras

Servidores

NAS

Cámaras <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

Switches

**Robo de información**

Una vez dentro:

-   Bases de datos

-   Documentos

-   Credenciales

**Ataques <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing**

El atacante intercepta el tráfico interno para espiar o modificar comunicaciones.

**6. ¿Cómo defenderse?**

**Contra ataques a <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública**

-   Firewall bien configurado.

-   Cerrar puertos innecesarios.

-   Actualizar servicios.

-   Utilizar <a href="../../GLOSARIO.md#vpn" target="_blank">VPN</a> para accesos remotos.

-   <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a> (autenticación multifactor).

-   <a href="../../GLOSARIO.md#ids" target="_blank">IDS</a>/<a href="../../GLOSARIO.md#ips" target="_blank">IPS</a>.

-   Monitoreo continuo.

-   Segmentación de servicios.

**Contra ataques internos**

-   <a href="../../GLOSARIO.md#vlan" target="_blank">VLAN</a>.

-   Segmentación de red.

-   Control de accesos.

-   Antivirus/<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>.

-   Detección de movimiento lateral.

-   Menor privilegio.

-   Monitoreo de tráfico interno.

-   Inventario actualizado.

**7. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Un analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> trabaja diariamente con direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

Debe distinguir rápidamente:

-   ¿Es pública?

-   ¿Es privada?

-   ¿Es interna?

-   ¿Es externa?

-   ¿Es legítima?

-   ¿Es sospechosa?

**Ejemplo 1**

Alerta:

181.45.25.120

Intentos <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

Puerto 22

Interpretación:

La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública de la empresa está siendo atacada.

Acciones:

-   Revisar firewall.

-   Revisar intentos fallidos.

-   Buscar fuerza bruta.

-   Bloquear <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> si corresponde.

**Ejemplo 2**

Logs:

192.168.1.50

↓

192.168.1.200

500 conexiones

Interpretación:

Puede tratarse de movimiento lateral.

**Ejemplo 3**

Logs:

10.10.20.30

↓

8.8.8.8

Interpretación:

Equipo interno realizando consultas <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> hacia un servidor externo.

Puede ser normal o indicar un comportamiento anómalo, según el contexto.

**Ejemplo 4**

Logs:

192.168.1.15

↓

185.x.x.x

Puerto 4444

Interpretación:

Podría indicar comunicación con un servidor de Comando y Control (C2) o un servicio remoto no autorizado. Se debe investigar el proceso que originó la conexión y validar si el destino es legítimo.

**8. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Debes poder responder preguntas como:

-   ¿La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> es pública o privada?

-   ¿De qué dispositivo proviene?

-   ¿Qué servicio está utilizando?

-   ¿Es tráfico esperado?

-   ¿Qué puerto utiliza?

-   ¿Qué protocolo utiliza?

-   ¿Hay intentos repetitivos?

-   ¿Existe movimiento lateral?

-   ¿Debe escalarse el incidente?

**Resumen**

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública**

-   Visible en Internet.

-   Única.

-   Asignada por el ISP.

-   Puede ser atacada desde cualquier lugar.

-   Requiere protección mediante firewalls, actualizaciones y monitoreo.

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada**

-   Solo funciona dentro de la red local.

-   No es accesible directamente desde Internet.

-   Asignada normalmente por el router mediante <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

-   Facilita la organización y seguridad de la red.

-   Utiliza <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> para comunicarse con Internet.

**Conceptos clave para memorizar**

  ------------------------------------------------------------------------
  **Concepto**         **Debes recordar**
  -------------------- ---------------------------------------------------
  <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública           Identifica la red en Internet.

  <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Privada           Identifica un dispositivo dentro de la red local.

  <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>                  Traduce <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas a una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

  <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>                 Asigna automáticamente <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas.

  Firewall             Filtra el tráfico de red.

  Puerto               Punto de entrada o salida de un servicio.

  Escaneo              Búsqueda de puertos y servicios.

  Movimiento lateral   Propagación del atacante entre equipos internos.
  ------------------------------------------------------------------------

**💡 Consejo como si estuviera formando a un futuro analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

No memorices solo las definiciones. Cuando veas una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> en un log, acostúmbrate a preguntarte automáticamente:

1.  ¿Es pública o privada?

2.  ¿Quién inició la comunicación?

3.  ¿Hacia dónde se dirige?

4.  ¿Qué puerto y protocolo utiliza?

5.  ¿Ese comportamiento es normal para ese equipo?

6.  Si no es normal, ¿qué evidencia necesito para confirmar si es un incidente?

Ese hábito mental es el que diferencia a alguien que conoce teoría de un analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> capaz de investigar y responder incidentes con criterio.

**Evaluación -- Módulo 1: Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Selecciona una única respuesta correcta para cada pregunta. Al finalizar, compara tus respuestas con la sección de soluciones y lee la justificación.

**Pregunta 1**

¿Cuál de las siguientes afirmaciones describe mejor una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública?

**A)** Solo puede utilizarse dentro de una red local.

**B)** Es visible desde Internet y permite identificar una red o dispositivo hacia el exterior.

**C)** Es asignada únicamente por un switch.

**D)** Solo funciona cuando existe un servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**Pregunta 2**

¿Cuál de las siguientes direcciones pertenece a un rango de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas?

**A)** 8.8.8.8

**B)** 181.45.22.10

**C)** 192.168.1.15

**D)** 200.25.10.1

**Pregunta 3**

¿Qué dispositivo suele asignar automáticamente las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas dentro de una vivienda?

**A)** Firewall

**B)** Router mediante <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

**C)** Servidor Web

**D)** Switch

**Pregunta 4**

¿Qué tecnología permite que varios dispositivos con <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada compartan una única <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública para acceder a Internet?

**A)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

**B)** <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

**C)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>

**D)** <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>

**Pregunta 5**

Un atacante realiza un escaneo sobre la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública de una empresa. ¿Qué busca principalmente?

**A)** El fondo de pantalla de los usuarios.

**B)** Puertos abiertos y servicios disponibles.

**C)** Archivos personales del administrador.

**D)** La velocidad del disco duro.

**Pregunta 6**

¿Cuál de las siguientes direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> es pública?

**A)** 10.20.30.40

**B)** 172.18.5.10

**C)** 192.168.10.25

**D)** 45.33.120.8

**Pregunta 7**

En un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> se observa el siguiente registro:

192.168.1.25
↓

192.168.1.180

con cientos de conexiones en pocos segundos.

¿Qué podría indicar este comportamiento?

**A)** Movimiento lateral dentro de la red.

**B)** Un cambio de contraseña.

**C)** Una actualización de Windows obligatoriamente.

**D)** Un problema con el monitor.

**Pregunta 8**

¿Cuál de las siguientes medidas ayuda a proteger una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública expuesta a Internet?

**A)** Desactivar el firewall.

**B)** Abrir todos los puertos.

**C)** Mantener los servicios actualizados y limitar los puertos abiertos.

**D)** Compartir las credenciales con todos los usuarios.

**Pregunta 9**

¿Cuál de los siguientes rangos corresponde completamente a direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas?

**A)** 8.0.0.0 -- 8.255.255.255

**B)** 10.0.0.0 -- 10.255.255.255

**C)** 150.0.0.0 -- 150.255.255.255

**D)** 200.0.0.0 -- 200.255.255.255

**Pregunta 10**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> recibes una alerta indicando múltiples intentos de conexión <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> contra la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública de la empresa.

¿Cuál sería tu primera acción?

**A)** Ignorar la alerta.

**B)** Revisar los logs, verificar si existe un ataque de fuerza bruta y validar si el firewall está bloqueando los intentos.

**C)** Apagar todos los servidores inmediatamente.

**D)** Cambiar todas las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de la empresa.

**Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación:**
Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública es visible desde Internet y permite que otros equipos se comuniquen con la red o el dispositivo que la posee. Es la \"cara visible\" de una organización o de un hogar en Internet.

**Pregunta 2**

✅ **Respuesta correcta: C**

**Justificación:**
La dirección **192.168.1.15** pertenece al rango privado **192.168.0.0/16**.

Las demás son direcciones públicas.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación:**
En la mayoría de los hogares y pequeñas empresas, el **router** ejecuta un servicio **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>**, que asigna automáticamente las <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas a los dispositivos conectados.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación:**
**<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> (Network Address Translation)** traduce las direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas en una dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública, permitiendo que múltiples dispositivos compartan una única conexión a Internet.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación:**
El primer paso de muchos atacantes es identificar **puertos abiertos, servicios expuestos y versiones de software**, para luego buscar vulnerabilidades o intentar acceder al sistema.

**Pregunta 6**

✅ **Respuesta correcta: D**

**Justificación:**
La dirección **45.33.120.8** no pertenece a ninguno de los rangos privados.

Los rangos privados son:

-   10.0.0.0/8

-   172.16.0.0 -- 172.31.255.255

-   192.168.0.0/16

**Pregunta 7**

✅ **Respuesta correcta: A**

**Justificación:**
Cuando un equipo realiza numerosas conexiones hacia otros equipos internos en poco tiempo, puede tratarse de un **movimiento lateral**, una técnica utilizada por atacantes para expandirse dentro de la red después de comprometer un equipo.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación:**
Reducir la superficie de ataque es una buena práctica: mantener los servicios actualizados y exponer únicamente los puertos necesarios disminuye el riesgo de explotación.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación:**
El rango **10.0.0.0 -- 10.255.255.255** es uno de los tres bloques reservados para redes privadas según el estándar IPv4.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación:**
Un analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> debe **investigar antes de actuar**. Revisar los registros, confirmar si se trata de un ataque de fuerza bruta y verificar la efectividad de los controles (como el firewall) son pasos iniciales adecuados. Apagar servidores o cambiar <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> sin evidencia suele generar más problemas que soluciones.

**Autoevaluación**

**9--10 respuestas correctas:** ⭐ Excelente. Tienes una buena comprensión de los conceptos básicos y estás listo para avanzar a temas como puertos, protocolos <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y análisis de tráfico.

**7--8 respuestas correctas:** 👍 Buen trabajo. Repasa especialmente <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>, los rangos de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas y el rol de las <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas en un entorno <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**5--6 respuestas correctas:** 📚 Vas por buen camino, pero conviene reforzar los fundamentos antes de continuar con conceptos más avanzados.

**0--4 respuestas correctas:** 🔄 Te recomiendo volver a leer el módulo y repetir el cuestionario. Una base sólida sobre direccionamiento <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> será clave para interpretar logs, alertas y tráfico de red en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.
