**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Módulo 11 – <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> (Dynamic Host Configuration Protocol)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>

- ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/IP

- ✅ Máscaras

- ✅ Subredes

- ✅ <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

- ✅ <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>

- ✅ TCP

- ✅ <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

- ✅ Puertos

Hasta ahora sabes que cada equipo necesita una IP para comunicarse.

Pero, ¿quién le asigna esa IP?

¿Imaginas configurar manualmente la IP de cada computadora de una empresa con 500 empleados?

Ahí entra en juego **DHCP**.

DHCP asigna configuraciones de red automáticamente.

Entrega IP, máscara, gateway y <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> sin intervención manual.

Es "invisible" para el usuario, pero fundamental en un SOC.

Una configuración maliciosa puede redirigir tráfico o suplantar servidores.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es DHCP.

- Entender por qué existe.

- Explicar el proceso <a href="../../GLOSARIO.md#dora" target="_blank">DORA</a> paso a paso.

- Conocer los puertos UDP 67 y UDP 68.

- Entender el concepto de concesión (<a href="../../GLOSARIO.md#lease" target="_blank">lease</a>) y su renovación.

- Diferenciar IP estática e IP dinámica.

- Conocer los componentes de un servidor DHCP.

- Identificar ataques como <a href="../../GLOSARIO.md#rogue-dhcp" target="_blank">Rogue DHCP</a> y <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP Starvation</a>.

- Interpretar eventos DHCP en un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

- Aplicar estos conocimientos en investigaciones de un SOC.

**1. ¿Qué es DHCP?**

DHCP significa:

**Dynamic Host Configuration Protocol**

**Protocolo de Configuración Dinámica de Host**

Es un protocolo de la **Capa de Aplicación** del modelo OSI.

Un servidor DHCP reparte <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> y otros datos de configuración a los equipos.

Todo ocurre sin que el usuario haga nada.

Enciende su computadora y ya tiene Internet.

**2. ¿Por qué existe DHCP?**

Configurar a mano IP, máscara, gateway y DNS en cada equipo sería un caos.

Un solo error de tipeo deja un equipo sin funcionar.

DHCP resuelve este problema.

Entrega IP, máscara, gateway y DNS, además del dominio y el tiempo de concesión.

**3. ¿Cómo funciona? El proceso DORA**

DHCP funciona con un proceso de **4 pasos**.

Se conoce como **DORA**.

DORA significa:

**D**iscover

**O**ffer

**R**equest

**A**cknowledge

**Paso 1 – Discover (Descubrimiento)**

El cliente no tiene IP todavía.

Envía un mensaje a todos (<a href="../../GLOSARIO.md#broadcast" target="_blank">broadcast</a>):

¿Hay algún servidor DHCP aquí?

**Paso 2 – Offer (Oferta)**

Los servidores DHCP responden.

Cada uno ofrece una IP disponible.

**Paso 3 – Request (Petición)**

El cliente elige una oferta.

Acepto la IP 192.168.1.50.

**Paso 4 – Acknowledge (Confirmación)**

El servidor confirma.

Entrega IP, máscara, gateway y DNS.

El cliente ya puede comunicarse.

**Diagrama del proceso DORA**

Cliente                  Servidor DHCP

    |                        |

    |----- Discover -------->|

    |<----- Offer -----------|

    |----- Request --------->|

    |<----- Acknowledge -----|

    |                        |

    |  ✅ IP asignada        |

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

DHCP utiliza <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> puertos:

**UDP 67** → Servidor DHCP.

**UDP 68** → Cliente DHCP.

**¿Por qué UDP y no TCP?**

TCP necesita una conexión previa (<a href="../../GLOSARIO.md#three-way-handshake" target="_blank">Three-Way Handshake</a>).

Pero el cliente DHCP todavía no tiene IP.

UDP permite enviar mensajes sin conexión previa.

Además es rápido y ligero.

**Dato importante:**

Los mensajes Discover y Request viajan en broadcast.

**5. Información que entrega**

Cuando el servidor confirma, entrega la configuración completa.

**Dirección IP**

La IP que el equipo usará en la red.

**Máscara de subred**

Define el tamaño de la red local.

**Gateway**

La puerta de salida hacia otras redes.

**Servidores DNS**

Los servidores para resolver nombres.

Por ejemplo: 8.8.8.8 o 1.1.1.1

**Dominio**

El dominio de la organización.

Por ejemplo:

empresa.local

**Duración de la concesión (lease)**

El tiempo que el equipo puede usar la IP (por ejemplo, 24 horas).

**6. Concesión (lease) y renovación**

El lease es el tiempo que la IP está "alquilada".

Ejemplos típicos: 8, 12 o 24 horas.

El cliente no espera a que expire.

Intenta renovar antes.

**Renovación (T1)**

Se intenta a la **mitad** del tiempo de concesión.

Con un lease de 24 horas, a las 12 horas.

Si el servidor responde, se renueva.

**Reintento (T2)**

Si el servidor no respondió.

Se intenta al **87,5%** del tiempo.

Con un lease de 24 horas, a las 21 horas.

**Si la concesión expira**

El cliente vuelve a DORA.

**IP estática vs dinámica**

| **Característica** | **IP Estática**        | **IP Dinámica**            |
|--------------------|------------------------|----------------------------|
| Asignación         | Manual                 | Automática (DHCP)          |
| Cambio de IP       | No cambia              | Puede cambiar              |
| Configuración      | Se escribe a mano      | La entrega el servidor     |
| Uso típico         | Servidores, impresoras | Computadoras de usuarios   |
| Riesgo             | Errores de configuración | Rogue DHCP, cambio de IP |

**Reservas**

Un servidor DHCP puede reservar una IP para un equipo.

La reserva se hace según la **dirección <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>**.

Ideal para servidores e impresoras.

**7. Componentes de un servidor DHCP**

**<a href="../../GLOSARIO.md#scope" target="_blank">Scope</a> (Ámbito)**

El rango de IPs disponibles para repartir.

Ejemplo:

192.168.1.100

↓

192.168.1.200

**Exclusiones**

IPs del rango que NO se reparten.

La impresora usa la 192.168.1.100 asignada a mano.

Esa IP se excluye del scope.

**Reservas**

Asignaciones fijas por MAC.

**Opciones**

Gateway, DNS, dominio y otras.

**Analogía de la portería**

El **scope** son los apartamentos disponibles.

Las **exclusiones** son los que nadie puede alquilar.

Las **reservas** son los asignados de forma fija a un inquilino.

La **concesión** es el contrato con fecha de vencimiento.

**8. DHCP en <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a>**

Wireshark captura los mensajes DHCP.

Verás los 4 mensajes del proceso DORA:

- **DHCP Discover:** el cliente busca un servidor.

- **DHCP Offer:** un servidor ofrece una IP.

- **DHCP Request:** el cliente acepta la oferta.

- **DHCP ACK:** el servidor confirma la asignación.

En la columna Info verás los 4 mensajes del proceso.

Todos comparten el mismo **<a href="../../GLOSARIO.md#transaction-id" target="_blank">Transaction ID</a>** (por ejemplo, 0x3f2a1b).

Ese ID relaciona los 4 mensajes entre sí.

**Filtro útil en Wireshark**

bootp or dhcp

**9. DHCP en un Firewall y en un SIEM**

**En un Firewall**

El firewall debe permitir tráfico DHCP.

Normalmente solo en la red local.

Cliente

↓

UDP 68

↓

Servidor DHCP

↓

UDP 67

↓

Permitido (solo red local)

Permitir DHCP hacia Internet es sospechoso.

**En un SIEM**

El SIEM recoge eventos de asignación.

Un evento típico podría mostrar:

Equipo:

PC-VENTAS-042

↓

MAC:

00:1A:2B:3C:4D:5E

↓

IP:

192.168.1.150

↓

Servidor:

192.168.1.1

Como analista deberías preguntarte:

- ¿Ese equipo es nuevo?

- ¿Es esperado que reciba DHCP?

- ¿El servidor DHCP es el oficial?

**10. ¿Cómo aprovechan DHCP los atacantes?**

DHCP es un servicio de confianza.

Los equipos aceptan lo que les entregue.

Esa confianza es lo que explotan los atacantes.

**Ataque 1 – Rogue DHCP (Servidor no autorizado)**

Un atacante monta su propio servidor DHCP en la red.

Con una laptop o un dispositivo pequeño.

Los clientes que piden IP pueden recibir respuesta de él.

Si responde primero, "gana" la oferta.

**Ataque 2 – DHCP Starvation (Agotamiento de direcciones)**

El atacante envía miles de solicitudes con MAC falsas.

El servidor legítimo reparte IPs hasta agotar el pool.

Los equipos legítimos se quedan sin IP.

Es una forma de **denegación de servicio**.

**Ataque 3 – <a href="../../GLOSARIO.md#dhcp-spoofing" target="_blank">DHCP Spoofing</a> para <a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a>**

Un atacante monta un servidor DHCP falso.

Entrega un **gateway falso** o un **DNS falso**.

El tráfico del usuario pasa por el atacante.

Atacante

↓

Gateway/DNS maliciosos

↓

Tráfico redirigido

↓

Intercepta, lee o modifica (MITM)

**Ataque 4 – Configuración como vector de phishing**

El DHCP malicioso entrega un DNS falso.

El usuario escribe:

www.banco.com

El DNS falso responde con la página falsa del atacante.

El usuario ve una página idéntica al banco.

Escribe sus credenciales.

El atacante las captura.

**11. ¿Cómo defenderse?**

Existen controles específicos contra estos ataques.

**<a href="../../GLOSARIO.md#dhcp-snooping" target="_blank">DHCP Snooping</a>**

Es una función del **switch**.

Separa puertos de confianza (hacia el servidor) y de no confianza (usuarios).

El switch **descarta** mensajes DHCP que no vienen del servidor oficial.

Bloquea mensajes Offer y ACK de puertos no confiables.

También limita los mensajes por segundo.

Ayuda a frenar DHCP Starvation.

**<a href="../../GLOSARIO.md#802-1x" target="_blank">802.1X</a>**

Autenticación por puerto.

**<a href="../../GLOSARIO.md#port-security" target="_blank">Port Security</a>**

Limita las MAC por puerto.

**Segmentación de red**

Separar la red en segmentos (VLANs).

**Monitoreo**

Detectar servidores DHCP no autorizados.

Alertar ante configuraciones inusuales.

**12. Aplicación práctica en un SOC**

**Caso 1**

Log del SIEM:

Equipo:

PC-CONTABILIDAD

↓

Recibió IP:

192.168.1.150

Interpretación:

Comportamiento normal de DHCP.

**Caso 2**

Log del SIEM:

Equipo:

PC-VENTAS-015

↓

IP:

192.168.1.90

↓

15 min después:

192.168.1.140

↓

20 min después:

192.168.1.60

Interpretación:

El equipo cambia de IP constantemente.

Puede indicar un lease corto, un problema de conectividad o algo sospechoso.

Hay que investigar.

**Caso 3**

Log del SIEM:

Respuesta DHCP Offer

↓

Origen:

172.16.10.77

Interpretación:

Esa IP no corresponde al servidor DHCP oficial.

Posible **Rogue DHCP**.

Alerta de máxima prioridad.

**Caso 4**

Log del SIEM:

Equipo:

PC-GERENCIA

↓

Recibió por DHCP:

Servidor DNS: 203.0.113.50

Interpretación:

El servidor DNS oficial es otro.

Posible **DHCP Spoofing** o configuración comprometida.

El equipo podría resolver dominios hacia sitios falsos.

Investigación inmediata.

**13. Lo que esperan de un Analista SOC Nivel 1**

Cuando veas un evento DHCP, debes hacerte preguntas:

- ¿Quién asignó esa IP?

- ¿El servidor DHCP es el oficial?

- ¿Qué DNS recibe el equipo?

- ¿Hubo cambios de IP en el equipo?

- ¿El cambio es esperado?

- ¿La IP entregada está dentro del scope correcto?

Ese análisis contextual distingue lo normal de lo sospechoso.

El registro DHCP te dice **qué equipo tenía qué IP** en un momento dado.

Permite rastrear el origen de un incidente.

**14. Resumen**

**DHCP**

- Protocolo de la **Capa de Aplicación**.

- Asigna configuración de red automáticamente.

- Entrega IP, máscara, gateway y DNS.

- Usa **UDP 67** (servidor) y **UDP 68** (cliente).

**Proceso DORA**

- Discover.

- Offer.

- Request.

- Acknowledge.

**Concesión (lease)**

- Tiempo de uso de la IP.

- Renovación a la mitad del tiempo (T1).

- Reintento al 87,5% (T2).

- Si expira, se reinicia DORA.

**IP estática vs dinámica**

- Estática: manual y fija.

- Dinámica: automática y puede cambiar.

**Ataques relacionados**

- Rogue DHCP.

- DHCP Starvation.

- DHCP Spoofing (MITM).

- Configuración maliciosa (phishing).

**Defensa**

- DHCP Snooping.

- 802.1X.

- Port Security.

- Segmentación.

- Monitoreo.

**🧠 Conceptos clave para memorizar**

| **Concepto**        | **Debes recordar**                                        |
|---------------------|-----------------------------------------------------------|
| DHCP                | Dynamic Host Configuration Protocol.                      |
| Función             | Asignar configuración de red automáticamente.             |
| Puerto servidor     | UDP 67.                                                   |
| Puerto cliente      | UDP 68.                                                   |
| DORA                | Discover, Offer, Request, Acknowledge.                    |
| Lease               | Tiempo de uso de una IP asignada.                         |
| T1                  | Renovación a la mitad del lease.                          |
| T2                  | Reintento al 87,5% del lease.                             |
| Scope               | Rango de IPs disponibles para repartir.                   |
| Exclusión           | IPs del rango que no se reparten.                         |
| Reserva             | IP fija ligada a una MAC.                                 |
| Rogue DHCP          | Servidor DHCP no autorizado.                              |
| DHCP Snooping       | Función del switch que filtra DHCP.                       |
| IP estática         | Configurada manualmente, no cambia.                       |
| IP dinámica         | Entregada por DHCP, puede cambiar.                        |

**🎓 Consejo como tu instructor de SOC**

DHCP parece aburrido.

Pero es oro puro para un analista.

¿Quieres saber qué equipo usó una IP ayer a las 15:00?

Revisa los logs DHCP.

En muchas investigaciones, la primera pista está en DHCP.

Te dice qué MAC obtuvo qué IP y en qué momento.

Los atacantes a veces montan un DHCP falso.

Lo hacen para interceptar tráfico.

Si los equipos dejan de recibir IP.

O si reciben IPs de un servidor desconocido.

Algo está pasando.

No veas un evento DHCP como "ruido".

Velo como una pista.

La asignación de IP es el comienzo de toda comunicación.

---

**📘 Carrera de Analista SOC**

**Semana 2 – Redes II**

**Evaluación – Módulo 11: DHCP (Dynamic Host Configuration Protocol)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Este cuestionario está diseñado con el nivel de dificultad de una evaluación para ingresar a un **SOC Nivel 1**. Algunas preguntas son conceptuales y otras presentan casos similares a los que encontrarás en un SIEM o en los logs de red. Al finalizar encontrarás las respuestas con su justificación.

**Pregunta 1**

¿Qué significa la sigla **DHCP**?

**A)** Dynamic Host Configuration Protocol

**B)** Digital Host Control Protocol

**C)** Dynamic Home Connection Protocol

**D)** Domain Host Configuration Process

**Pregunta 2**

¿Cuál es la función principal de DHCP?

**A)** Traducir nombres de dominio a direcciones IP.

**B)** Asignar automáticamente configuración de red (IP, máscara, gateway y DNS).

**C)** Cifrar las comunicaciones de la red.

**D)** Bloquear puertos no autorizados.

**Pregunta 3**

¿Qué puertos utiliza DHCP?

**A)** UDP 53 y UDP 123

**B)** TCP 80 y TCP 443

**C)** UDP 67 (servidor) y UDP 68 (cliente)

**D)** TCP 67 (cliente) y UDP 68 (servidor)

**Pregunta 4**

¿Qué significa el proceso **DORA**?

**A)** Discover, Offer, Request, Acknowledge

**B)** Data, Offer, Route, Accept

**C)** Discover, Open, Request, Accept

**D)** Domain, Offer, Renew, Acknowledge

**Pregunta 5**

Durante el proceso DORA, ¿qué hace el cliente en el paso **Discover**?

**A)** Entrega su configuración al servidor.

**B)** Busca servidores DHCP disponibles en la red.

**C)** Confirma la IP recibida.

**D)** Renueva su concesión antes de que expire.

**Pregunta 6**

Una concesión (lease) de 24 horas se renueva normalmente:

**A)** A las 24 horas exactas.

**B)** A la mitad del tiempo, es decir, a las 12 horas.

**C)** Solo si el equipo se reinicia.

**D)** Nunca se renueva.

**Pregunta 7**

¿Qué dato **NO** entrega normalmente un servidor DHCP?

**A)** Dirección IP.

**B)** Máscara de subred.

**C)** Gateway.

**D)** La contraseña del usuario.

**Pregunta 8**

¿Qué es un **Rogue DHCP**?

**A)** Un servidor DHCP configurado con un lease muy largo.

**B)** Un servidor DHCP no autorizado montado en la red.

**C)** Una IP estática mal configurada.

**D)** Un cliente DHCP con la MAC bloqueada.

**Pregunta 9**

¿Qué función de un switch ayuda a prevenir ataques como el **Rogue DHCP**?

**A)** NAT.

**B)** DHCP Snooping.

**C)** Firewall de aplicación.

**D)** Encriptación de la red Wi-Fi.

**Pregunta 10 (Caso práctico SOC)**

El SIEM genera la siguiente alerta:

Dos servidores responden

↓

peticiones DHCP

↓

Uno de ellos es:

172.16.10.77

↓

El servidor DHCP oficial es:

172.16.10.2

¿Cuál sería tu primera hipótesis?

**A)** El servidor 172.16.10.77 está realizando una actualización de Windows.

**B)** Existe un servidor DHCP no autorizado (Rogue DHCP) intentando repartir configuración.

**C)** El servidor oficial cambió de IP sin avisar.

**D)** Es un error menor que no requiere atención.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: A**

**Justificación**

DHCP significa **Dynamic Host Configuration Protocol**.

Es el protocolo encargado de asignar configuración de red de forma automática.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

La función principal de DHCP es **asignar automáticamente** la configuración de red:

- IP.

- Máscara.

- Gateway.

- DNS.

Sin intervención manual del usuario.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

DHCP utiliza **UDP 67** para el servidor y **UDP 68** para el cliente.

Usa UDP porque el cliente aún no tiene IP y no puede establecer una conexión TCP.

**Pregunta 4**

✅ **Respuesta correcta: A**

**Justificación**

DORA es el proceso de 4 pasos de DHCP:

- **D**iscover.

- **O**ffer.

- **R**equest.

- **A**cknowledge.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

En el paso **Discover**, el cliente no tiene IP y busca servidores DHCP.

Envía un mensaje de broadcast preguntando quién puede ofrecerle una IP.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

La concesión se renueva a la **mitad** del tiempo (T1).

Con un lease de 24 horas, la renovación ocurre a las 12 horas.

Si el servidor no responde, se intenta de nuevo al 87,5% (T2).

**Pregunta 7**

✅ **Respuesta correcta: D**

**Justificación**

DHCP entrega datos de configuración de red.

Entrega IP, máscara, gateway y DNS.

Nunca entrega contraseñas de usuarios.

Si un mensaje DHCP incluyera credenciales, sería un grave indicador de compromiso.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

Un **Rogue DHCP** es un servidor DHCP no autorizado dentro de la red.

Puede repartir configuraciones maliciosas:

- Gateways falsos.

- DNS falsos.

Para interceptar el tráfico o redirigir al usuario a sitios falsos.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

**DHCP Snooping** es una función del switch que distingue puertos de confianza y no confianza.

Descarta mensajes DHCP que no provienen del servidor oficial.

Es uno de los controles más efectivos contra Rogue DHCP y DHCP Starvation.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Dos servidores respondiendo peticiones DHCP es un fuerte indicador de un **Rogue DHCP**.

El servidor 172.16.10.77 no es el oficial.

Como analista SOC deberías:

- Confirmar si ese servidor existe en el inventario.

- Revisar qué configuración entregó.

- Verificar si los equipos recibieron DNS o gateway maliciosos.

- Contener el dispositivo desconocido.

- Coordinar con el equipo de red para activar DHCP Snooping.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Comprendes DHCP y puedes detectar servidores y configuraciones anómalas en la red.                                                                     |
| **8–9**                  | 🟢 **Muy buen nivel.** Dominas el proceso DORA y los riesgos asociados.                                                                                                  |
| **6–7**                  | 🟡 **Buen progreso.** Repasa el proceso DORA y los ataques de Rogue DHCP y DHCP Starvation.                                                                               |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Revisa los puertos 67/68 y el ciclo de concesión de direcciones.                                                            |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** DHCP es clave para entender la asignación de IPs y rastrear equipos en un SOC.                                        |
