**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Módulo 11 – <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> (Dynamic Host Configuration Protocol)**

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

- ✅ <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

- ✅ Puertos

Hasta ahora sabes que cada equipo necesita una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> para comunicarse.

Pero, ¿quién le asigna esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

¿Imaginas configurar manualmente la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de cada computadora de una empresa con 500 empleados?

Ahí entra en juego **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>**.

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> asigna configuraciones de red automáticamente.

Entrega <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> sin intervención manual.

Es "invisible" para el usuario, pero fundamental en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

Una configuración maliciosa puede redirigir tráfico o suplantar servidores.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

- Entender por qué existe.

- Explicar el proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a> paso a paso.

- Conocer los puertos <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67 y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68.

- Entender el concepto de concesión (<a href="../../GLOSARIO.md#lease" target="_blank">lease</a>) y su renovación.

- Diferenciar <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> estática e <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> dinámica.

- Conocer los componentes de un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

- Identificar ataques como <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a> y <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a>.

- Interpretar eventos <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

- Aplicar estos conocimientos en investigaciones de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>?**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> significa:

**Dynamic Host Configuration Protocol**

**Protocolo de Configuración Dinámica de Host**

Es un protocolo de la **Capa de Aplicación** del modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

Un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> reparte <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> y otros datos de configuración a los equipos.

Todo ocurre sin que el usuario haga nada.

Enciende su computadora y ya tiene Internet.

**2. ¿Por qué existe <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>?**

Configurar a mano <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> en cada equipo sería un caos.

Un solo error de tipeo deja un equipo sin funcionar.

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> resuelve este problema.

Entrega <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, además del dominio y el tiempo de concesión.

**3. ¿Cómo funciona? El proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> funciona con un proceso de **4 pasos**.

Se conoce como **<a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>**.

<a href="../../GLOSARIO.md#dora" target="_blank">DORA</a> significa:

**D**iscover

**O**ffer

**R**equest

**A**cknowledge

**Paso 1 – Discover (Descubrimiento)**

El cliente no tiene <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> todavía.

Envía un mensaje a todos (<a href="../../GLOSARIO.md#broadcast" target="_blank">broadcast</a>):

¿Hay algún servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> aquí?

**Paso 2 – Offer (Oferta)**

Los servidores <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> responden.

Cada uno ofrece una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> disponible.

**Paso 3 – Request (Petición)**

El cliente elige una oferta.

Acepto la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> 192.168.1.50.

**Paso 4 – Acknowledge (Confirmación)**

El servidor confirma.

Entrega <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

El cliente ya puede comunicarse.

**Diagrama del proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>**

Cliente                  Servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

    |                        |

    |----- Discover -------->|

    |<----- Offer -----------|

    |----- Request --------->|

    |<----- Acknowledge -----|

    |                        |

    |  ✅ <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> asignada        |

**El proceso en una línea:**

Discover → Offer → Request → Acknowledge

**Analogía del hotel**

Llegas a un hotel sin reserva.

**Discover**

¿Tienen una habitación libre?

**Offer**

Sí, tengo la habitación 204.

**Request**

Quiero la habitación 204.

**Acknowledge**

Confirmado. Aquí tienes la llave.

**4. Puertos**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> utiliza <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> puertos:

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67** → Servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68** → Cliente <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**¿Por qué <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> y no <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>?**

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> necesita una conexión previa (<a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>).

Pero el cliente <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> todavía no tiene <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> permite enviar mensajes sin conexión previa.

Además es rápido y ligero.

**Dato importante:**

Los mensajes Discover y Request viajan en <a href="../../GLOSARIO.md#broadcast" target="_blank">broadcast</a>.

**5. Información que entrega**

Cuando el servidor confirma, entrega la configuración completa.

**Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>**

La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> que el equipo usará en la red.

**Máscara de subred**

Define el tamaño de la red local.

**<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>**

La puerta de salida hacia otras redes.

**Servidores <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>**

Los servidores para resolver nombres.

Por ejemplo: 8.8.8.8 o 1.1.1.1

**Dominio**

El dominio de la organización.

Por ejemplo:

empresa.local

**Duración de la concesión (<a href="../../GLOSARIO.md#lease" target="_blank">lease</a>)**

El tiempo que el equipo puede usar la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> (por ejemplo, 24 horas).

**6. Concesión (<a href="../../GLOSARIO.md#lease" target="_blank">lease</a>) y renovación**

El <a href="../../GLOSARIO.md#lease" target="_blank">lease</a> es el tiempo que la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> está "alquilada".

Ejemplos típicos: 8, 12 o 24 horas.

El cliente no espera a que expire.

Intenta renovar antes.

**Renovación (T1)**

Se intenta a la **mitad** del tiempo de concesión.

Con un <a href="../../GLOSARIO.md#lease" target="_blank">lease</a> de 24 horas, a las 12 horas.

Si el servidor responde, se renueva.

**Reintento (T2)**

Si el servidor no respondió.

Se intenta al **87,5%** del tiempo.

Con un <a href="../../GLOSARIO.md#lease" target="_blank">lease</a> de 24 horas, a las 21 horas.

**Si la concesión expira**

El cliente vuelve a <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>.

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> estática vs dinámica**

| **Característica** | **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Estática**        | **<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Dinámica**            |
|--------------------|------------------------|----------------------------|
| Asignación         | Manual                 | Automática (<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>)          |
| Cambio de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>       | No cambia              | Puede cambiar              |
| Configuración      | Se escribe a mano      | La entrega el servidor     |
| Uso típico         | Servidores, impresoras | Computadoras de usuarios   |
| Riesgo             | Errores de configuración | <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>, cambio de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> |

**Reservas**

Un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> puede reservar una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> para un equipo.

La reserva se hace según la **dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>**.

Ideal para servidores e impresoras.

**7. Componentes de un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>**

**<a href="../../GLOSARIO.md#scope" target="_blank">Scope</a> (Ámbito)**

El rango de <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> disponibles para repartir.

Ejemplo:

192.168.1.100

↓

192.168.1.200

**Exclusiones**

<a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> del rango que NO se reparten.

La impresora usa la 192.168.1.100 asignada a mano.

Esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> se excluye del <a href="../../GLOSARIO.md#scope" target="_blank">scope</a>.

**Reservas**

Asignaciones fijas por <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>.

**Opciones**

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, dominio y otras.

**Analogía de la portería**

El **<a href="../../GLOSARIO.md#scope" target="_blank">scope</a>** son los apartamentos disponibles.

Las **exclusiones** son los que nadie puede alquilar.

Las **reservas** son los asignados de forma fija a un inquilino.

La **concesión** es el contrato con fecha de vencimiento.

**8. <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>**

<a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a> captura los mensajes <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

Verás los 4 mensajes del proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>:

- **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> Discover:** el cliente busca un servidor.

- **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> Offer:** un servidor ofrece una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

- **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> Request:** el cliente acepta la oferta.

- **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> ACK:** el servidor confirma la asignación.

En la columna Info verás los 4 mensajes del proceso.

Todos comparten el mismo **<a href="../../GLOSARIO.md#transaction-id" target="_blank">Transaction ID</a>** (por ejemplo, 0x3f2a1b).

Ese ID relaciona los 4 mensajes entre sí.

**Filtro útil en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>**

bootp or <a href="../../GLOSARIO.md#dhcp" target="_blank">dhcp</a>

**9. <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> en un Firewall y en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**

**En un Firewall**

El firewall debe permitir tráfico <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

Normalmente solo en la red local.

Cliente

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68

↓

Servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

↓

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67

↓

Permitido (solo red local)

Permitir <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> hacia Internet es sospechoso.

**En un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**

El <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> recoge eventos de asignación.

Un evento típico podría mostrar:

Equipo:

PC-VENTAS-042

↓

<a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>:

00:1A:2B:3C:4D:5E

↓

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>:

192.168.1.150

↓

Servidor:

192.168.1.1

Como analista deberías preguntarte:

- ¿Ese equipo es nuevo?

- ¿Es esperado que reciba <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>?

- ¿El servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> es el oficial?

**10. ¿Cómo aprovechan <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> los atacantes?**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> es un servicio de confianza.

Los equipos aceptan lo que les entregue.

Esa confianza es lo que explotan los atacantes.

**Ataque 1 – <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a> (Servidor no autorizado)**

Un atacante monta su propio servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> en la red.

Con una laptop o un dispositivo pequeño.

Los clientes que piden <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pueden recibir respuesta de él.

Si responde primero, "gana" la oferta.

**Ataque 2 – <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a> (Agotamiento de direcciones)**

El atacante envía miles de solicitudes con <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> falsas.

El servidor legítimo reparte <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> hasta agotar el pool.

Los equipos legítimos se quedan sin <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

Es una forma de **denegación de servicio**.

**Ataque 3 – <a href="../../GLOSARIO.md#dhcp-spoofing" target="_blank">DHCP Spoofing</a> para <a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a>**

Un atacante monta un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> falso.

Entrega un **<a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> falso** o un **<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> falso**.

El tráfico del usuario pasa por el atacante.

Atacante

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>/<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> maliciosos

↓

Tráfico redirigido

↓

Intercepta, lee o modifica (<a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a>)

**Ataque 4 – Configuración como vector de phishing**

El <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> malicioso entrega un <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> falso.

El usuario escribe:

www.banco.com

El <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> falso responde con la página falsa del atacante.

El usuario ve una página idéntica al banco.

Escribe sus credenciales.

El atacante las captura.

**11. ¿Cómo defenderse?**

Existen controles específicos contra estos ataques.

**<a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>**

Es una función del **switch**.

Separa puertos de confianza (hacia el servidor) y de no confianza (usuarios).

El switch **descarta** mensajes <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> que no vienen del servidor oficial.

Bloquea mensajes Offer y ACK de puertos no confiables.

También limita los mensajes por segundo.

Ayuda a frenar <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a>.

**<a href="../../GLOSARIO.md#802-1x" target="_blank">802.1X</a>**

Autenticación por puerto.

**<a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>**

Limita las <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> por puerto.

**Segmentación de red**

Separar la red en segmentos (VLANs).

**Monitoreo**

Detectar servidores <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> no autorizados.

Alertar ante configuraciones inusuales.

**12. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Caso 1**

Log del <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>:

Equipo:

PC-CONTABILIDAD

↓

Recibió <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>:

192.168.1.150

Interpretación:

Comportamiento normal de <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**Caso 2**

Log del <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>:

Equipo:

PC-VENTAS-015

↓

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>:

192.168.1.90

↓

15 min después:

192.168.1.140

↓

20 min después:

192.168.1.60

Interpretación:

El equipo cambia de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> constantemente.

Puede indicar un <a href="../../GLOSARIO.md#lease" target="_blank">lease</a> corto, un problema de conectividad o algo sospechoso.

Hay que investigar.

**Caso 3**

Log del <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>:

Respuesta <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> Offer

↓

Origen:

172.16.10.77

Interpretación:

Esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> no corresponde al servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> oficial.

Posible **<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>**.

Alerta de máxima prioridad.

**Caso 4**

Log del <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>:

Equipo:

PC-GERENCIA

↓

Recibió por <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>:

Servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>: 203.0.113.50

Interpretación:

El servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> oficial es otro.

Posible **<a href="../../GLOSARIO.md#dhcp-spoofing" target="_blank">DHCP Spoofing</a>** o configuración comprometida.

El equipo podría resolver dominios hacia sitios falsos.

Investigación inmediata.

**13. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando veas un evento <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>, debes hacerte preguntas:

- ¿Quién asignó esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

- ¿El servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> es el oficial?

- ¿Qué <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> recibe el equipo?

- ¿Hubo cambios de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> en el equipo?

- ¿El cambio es esperado?

- ¿La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> entregada está dentro del <a href="../../GLOSARIO.md#scope" target="_blank">scope</a> correcto?

Ese análisis contextual distingue lo normal de lo sospechoso.

El registro <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> te dice **qué equipo tenía qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>** en un momento dado.

Permite rastrear el origen de un incidente.

**14. Resumen**

**<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>**

- Protocolo de la **Capa de Aplicación**.

- Asigna configuración de red automáticamente.

- Entrega <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

- Usa **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67** (servidor) y **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68** (cliente).

**Proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>**

- Discover.

- Offer.

- Request.

- Acknowledge.

**Concesión (<a href="../../GLOSARIO.md#lease" target="_blank">lease</a>)**

- Tiempo de uso de la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

- Renovación a la mitad del tiempo (T1).

- Reintento al 87,5% (T2).

- Si expira, se reinicia <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>.

**<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> estática vs dinámica**

- Estática: manual y fija.

- Dinámica: automática y puede cambiar.

**Ataques relacionados**

- <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>.

- <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a>.

- <a href="../../GLOSARIO.md#dhcp-spoofing" target="_blank">DHCP Spoofing</a> (<a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a>).

- Configuración maliciosa (phishing).

**Defensa**

- <a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>.

- <a href="../../GLOSARIO.md#802-1x" target="_blank">802.1X</a>.

- <a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>.

- Segmentación.

- Monitoreo.

**🧠 Conceptos clave para memorizar**

| **Concepto**        | **Debes recordar**                                        |
|---------------------|-----------------------------------------------------------|
| <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>                | Dynamic Host Configuration Protocol.                      |
| Función             | Asignar configuración de red automáticamente.             |
| Puerto servidor     | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67.                                                   |
| Puerto cliente      | <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68.                                                   |
| <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>                | Discover, Offer, Request, Acknowledge.                    |
| <a href="../../GLOSARIO.md#lease" target="_blank">Lease</a>               | Tiempo de uso de una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> asignada.                         |
| T1                  | Renovación a la mitad del <a href="../../GLOSARIO.md#lease" target="_blank">lease</a>.                          |
| T2                  | Reintento al 87,5% del <a href="../../GLOSARIO.md#lease" target="_blank">lease</a>.                             |
| <a href="../../GLOSARIO.md#scope" target="_blank">Scope</a>               | Rango de <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> disponibles para repartir.                   |
| Exclusión           | <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> del rango que no se reparten.                         |
| Reserva             | <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> fija ligada a una <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>.                                 |
| <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>          | Servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> no autorizado.                              |
| <a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>       | Función del switch que filtra <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.                       |
| <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> estática         | Configurada manualmente, no cambia.                       |
| <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> dinámica         | Entregada por <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>, puede cambiar.                        |

**🎓 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> parece aburrido.

Pero es oro puro para un analista.

¿Quieres saber qué equipo usó una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> ayer a las 15:00?

Revisa los logs <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

En muchas investigaciones, la primera pista está en <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

Te dice qué <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> obtuvo qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y en qué momento.

Los atacantes a veces montan un <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> falso.

Lo hacen para interceptar tráfico.

Si los equipos dejan de recibir <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

O si reciben <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> de un servidor desconocido.

Algo está pasando.

No veas un evento <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> como "ruido".

Velo como una pista.

La asignación de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> es el comienzo de toda comunicación.

---

**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Evaluación – Módulo 11: <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> (Dynamic Host Configuration Protocol)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Este cuestionario está diseñado con el nivel de dificultad de una evaluación para ingresar a un **<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**. Algunas preguntas son conceptuales y otras presentan casos similares a los que encontrarás en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> o en los logs de red. Al finalizar encontrarás las respuestas con su justificación.

**Pregunta 1**

¿Qué significa la sigla **<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>**?

**A)** Dynamic Host Configuration Protocol

**B)** Digital Host Control Protocol

**C)** Dynamic Home Connection Protocol

**D)** Domain Host Configuration Process

**Pregunta 2**

¿Cuál es la función principal de <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>?

**A)** Traducir nombres de dominio a direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**B)** Asignar automáticamente configuración de red (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>).

**C)** Cifrar las comunicaciones de la red.

**D)** Bloquear puertos no autorizados.

**Pregunta 3**

¿Qué puertos utiliza <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>?

**A)** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53 y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 123

**B)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80 y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443

**C)** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67 (servidor) y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68 (cliente)

**D)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 67 (cliente) y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68 (servidor)

**Pregunta 4**

¿Qué significa el proceso **<a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>**?

**A)** Discover, Offer, Request, Acknowledge

**B)** Data, Offer, Route, Accept

**C)** Discover, Open, Request, Accept

**D)** Domain, Offer, Renew, Acknowledge

**Pregunta 5**

Durante el proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a>, ¿qué hace el cliente en el paso **Discover**?

**A)** Entrega su configuración al servidor.

**B)** Busca servidores <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> disponibles en la red.

**C)** Confirma la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> recibida.

**D)** Renueva su concesión antes de que expire.

**Pregunta 6**

Una concesión (<a href="../../GLOSARIO.md#lease" target="_blank">lease</a>) de 24 horas se renueva normalmente:

**A)** A las 24 horas exactas.

**B)** A la mitad del tiempo, es decir, a las 12 horas.

**C)** Solo si el equipo se reinicia.

**D)** Nunca se renueva.

**Pregunta 7**

¿Qué dato **NO** entrega normalmente un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>?

**A)** Dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**B)** Máscara de subred.

**C)** <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**D)** La contraseña del usuario.

**Pregunta 8**

¿Qué es un **<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>**?

**A)** Un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> configurado con un <a href="../../GLOSARIO.md#lease" target="_blank">lease</a> muy largo.

**B)** Un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> no autorizado montado en la red.

**C)** Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> estática mal configurada.

**D)** Un cliente <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> con la <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a> bloqueada.

**Pregunta 9**

¿Qué función de un switch ayuda a prevenir ataques como el **<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>**?

**A)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**B)** <a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>.

**C)** Firewall de aplicación.

**D)** Encriptación de la red Wi-Fi.

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

El <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> genera la siguiente alerta:

<a href="../../GLOSARIO.md#dos" target="_blank">Dos</a> servidores responden

↓

peticiones <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

↓

Uno de ellos es:

172.16.10.77

↓

El servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> oficial es:

172.16.10.2

¿Cuál sería tu primera hipótesis?

**A)** El servidor 172.16.10.77 está realizando una actualización de Windows.

**B)** Existe un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> no autorizado (<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>) intentando repartir configuración.

**C)** El servidor oficial cambió de <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> sin avisar.

**D)** Es un error menor que no requiere atención.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: A**

**Justificación**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> significa **Dynamic Host Configuration Protocol**.

Es el protocolo encargado de asignar configuración de red de forma automática.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

La función principal de <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> es **asignar automáticamente** la configuración de red:

- <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

- Máscara.

- <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

Sin intervención manual del usuario.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> utiliza **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 67** para el servidor y **<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 68** para el cliente.

Usa <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> porque el cliente aún no tiene <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y no puede establecer una conexión <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>.

**Pregunta 4**

✅ **Respuesta correcta: A**

**Justificación**

<a href="../../GLOSARIO.md#dora" target="_blank">DORA</a> es el proceso de 4 pasos de <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>:

- **D**iscover.

- **O**ffer.

- **R**equest.

- **A**cknowledge.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

En el paso **Discover**, el cliente no tiene <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y busca servidores <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

Envía un mensaje de <a href="../../GLOSARIO.md#broadcast" target="_blank">broadcast</a> preguntando quién puede ofrecerle una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

La concesión se renueva a la **mitad** del tiempo (T1).

Con un <a href="../../GLOSARIO.md#lease" target="_blank">lease</a> de 24 horas, la renovación ocurre a las 12 horas.

Si el servidor no responde, se intenta de nuevo al 87,5% (T2).

**Pregunta 7**

✅ **Respuesta correcta: D**

**Justificación**

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> entrega datos de configuración de red.

Entrega <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, máscara, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

Nunca entrega contraseñas de usuarios.

Si un mensaje <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> incluyera credenciales, sería un grave indicador de compromiso.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

Un **<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>** es un servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> no autorizado dentro de la red.

Puede repartir configuraciones maliciosas:

- Gateways falsos.

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> falsos.

Para interceptar el tráfico o redirigir al usuario a sitios falsos.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

**<a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>** es una función del switch que distingue puertos de confianza y no confianza.

Descarta mensajes <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> que no provienen del servidor oficial.

Es uno de los controles más efectivos contra <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a> y <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a>.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#dos" target="_blank">Dos</a> servidores respondiendo peticiones <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> es un fuerte indicador de un **<a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a>**.

El servidor 172.16.10.77 no es el oficial.

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> deberías:

- Confirmar si ese servidor existe en el inventario.

- Revisar qué configuración entregó.

- Verificar si los equipos recibieron <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> o <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a> maliciosos.

- Contener el dispositivo desconocido.

- Coordinar con el equipo de red para activar <a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Comprendes <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> y puedes detectar servidores y configuraciones anómalas en la red.                                                                     |
| **8–9**                  | 🟢 **Muy buen nivel.** Dominas el proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a> y los riesgos asociados.                                                                                                  |
| **6–7**                  | 🟡 **Buen progreso.** Repasa el proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a> y los ataques de <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a> y <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a>.                                                                               |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Revisa los puertos 67/68 y el ciclo de concesión de direcciones.                                                            |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> es clave para entender la asignación de <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> y rastrear equipos en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.                                        |
