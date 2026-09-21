**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 28: Windows desde la perspectiva del atacante**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Mentalidad ofensiva (defensiva) + Detección

Este módulo unifica la cadena de ataque (recon → ejecución → escalada → credenciales → persistencia → movimiento lateral → evasión) con la guía larga (attack lifecycle, descubrimiento con <a href="../../GLOSARIO.md#cmd" target="_blank">CMD</a>/<a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a>, <a href="../../GLOSARIO.md#living-off-the-land" target="_blank">Living off the Land</a>, anomalía/<a href="../../GLOSARIO.md#baseline" target="_blank">baseline</a>, <a href="../../GLOSARIO.md#ioc" target="_blank">IOC</a>/<a href="../../GLOSARIO.md#ioa" target="_blank">IOA</a>, defensa en profundidad) y el examen general de Windows de 20 preguntas.

**🎯 Objetivos del módulo**

-   Recorrer la cadena: acceso inicial → ejecución → descubrimiento → escalada → credenciales → persistencia → movimiento lateral → evasión.
-   Relacionar cada técnica con sus Event <a href="../../GLOSARIO.md#event-id" target="_blank">IDs</a> (<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>/<a href="../../GLOSARIO.md#4625" target="_blank">4625</a>/<a href="../../GLOSARIO.md#4688" target="_blank">4688</a>/4720/4728/<a href="../../GLOSARIO.md#7045" target="_blank">7045</a>/<a href="../../GLOSARIO.md#1102" target="_blank">1102</a>).
-   Entender credential dumping, Kerberoasting, Pass-the-Hash/Ticket, LOLBins y PowerShell malicioso desde la detección.


---

## Parte A — Referencia de la cadena de ataque

**1. Reconocimiento y enumeración**

El atacante recopila información:

-   Usuarios y grupos (`net user`, `net localgroup`).
-   Sistema y parches (`systeminfo`).
-   Procesos y servicios (`tasklist`, `sc query`).
-   Red (`ipconfig`, `netstat`).

Detección: comandos de enumeración masiva, especialmente fuera de
horario o desde cuentas no administrativas.

**2. Escalada de privilegios**

Busca pasar de usuario estándar a SYSTEM/Administrador. Técnicas:

-   Bypass <a href="../../GLOSARIO.md#uac" target="_blank">UAC</a>.
-   Explotar servicio mal configurado.
-   Abusar de tareas programadas.

Detección: 4672 (privilegios especiales), creación de servicios (7045),
modificación de tareas.

**3. Persistencia**

Quiere seguir dentro tras reiniciar:

-   Servicio propio (7045).
-   Clave de Registro de autoarranque (Run / RunOnce).
-   Tarea programada.
-   Cuenta nueva con privilegios (4720 + 4728).

Detección: revisar 7045, 4720, 4728 y claves de autoarranque.

**4. Credential dumping**

Roba credenciales en memoria:

-   Volcado de **<a href="../../GLOSARIO.md#lsass" target="_blank">LSASS</a>** para obtener hashes/<a href="../../GLOSARIO.md#ntlm" target="_blank">NTLM</a>.
-   **<a href="../../GLOSARIO.md#kerberoasting" target="_blank">Kerberoasting</a>**: pide service tickets para crackearlos.

Detección: herramientas como `mimikatz`, accesos anómalos a LSASS,
muchas solicitudes de service tickets.

**5. Movimiento lateral**

Una vez dentro de un equipo, salta a otros:

-   **PsExec**: ejecución remota vía SMB.
-   **WMI** / **WinRM**.
-   Uso de credenciales robadas (<a href="../../GLOSARIO.md#pass-the-hash" target="_blank">Pass-the-Hash</a>).

Detección: inicios de sesión tipo 3 (red) hacia múltiples equipos,
creación de procesos remotamente.

**6. LOLBins y PowerShell malicioso**

Como vimos en el módulo 25, abusa de binarios legítimos:

-   `powershell -enc` para ocultar comandos.
-   `certutil` / `bitsadmin` para descargas.
-   `wmic` para ejecución remota.

Detección: 4688 con línea de comandos sospechosa, scripts codificados.

**7. Ejecución de comandos y manipulación de servicios**

El atacante puede:

-   Crear/modificar servicios para ejecutar su payload.
-   Manipular el Registro para autoarranque.
-   Desactivar defensas (Defender, logs).

Detección: 7045, cambios en claves de Run, eventos 1102 (borrado de
logs).

**8. Cadena de ataque típica**

Phishing

↓

Ejecución (factura.exe)

↓

PowerShell

↓

Recon / enumeración

↓

Escalada / dumping

↓

Persistencia

↓

Movimiento lateral

↓

Exfiltración / C2

Cada flecha deja **evidencia** en logs, procesos o red. El SOC las une.

**🧪 Laboratorio recomendado (defensivo)**

1.  Enumera tu propia máquina con `net user`, `systeminfo`,
    `tasklist` y anota qué vería un atacante.
2.  Revisa en `eventvwr` los eventos 4720, 4728 y 7045.
3.  Piensa: ¿dónde colocarías una alerta para cada fase anterior?
4.  (Sin herramientas ofensivas) describe cómo detectarías una tarea
    programada creada por un atacante.

**📝 Evaluación — Módulo 28: Windows desde la perspectiva del atacante**

**🔹 Pregunta 1**

El "reconocimiento" busca principalmente:

**A)** Apagar el equipo\
**B)** Reunir información (usuarios, servicios, red)\
**C)** Cifrar discos\
**D)** Borrar logs

**🔹 Pregunta 2**

Crear una cuenta nueva y subirla a Administradores es una técnica de:

**A)** Persistencia\
**B)** Impresión\
**C)** Actualización\
**D)** Spam

**🔹 Pregunta 3**

Volcar LSASS para robar hashes es:

**A)** Credential dumping\
**B)** Movimiento lateral\
**C)** Cifrado\
**D)** Phishing

**🔹 Pregunta 4**

Kerberoasting ataca:

**A)** El firewall\
**B)** Service tickets de <a href="../../GLOSARIO.md#active-directory" target="_blank">Active Directory</a>\
**C)** El registro\
**D)** <a href="../../GLOSARIO.md#bitlocker" target="_blank">BitLocker</a>

**🔹 Pregunta 5**

Una clave de Registro Run usada para autoarrancar malware es:

**A)** Persistencia\
**B)** Reconocimiento\
**C)** Exfiltración\
**D)** Spoofing

**🔹 Pregunta 6**

`powershell -enc` se usa para:

**A)** Actualizar Windows\
**B)** Ocultar el comando real\
**C)** Imprimir\
**D)** Crear usuarios

**🔹 Pregunta 7**

PsExec suele asociarse a:

**A)** Movimiento lateral remoto\
**B)** Cifrado de disco\
**C)** Antivirus\
**D)** Firewall

**🔹 Pregunta 8**

El borrado del log de seguridad (1102) suele ser:

**A)** Mantenimiento\
**B)** Intento de encubrir evidencias\
**C)** Actualización\
**D)** Error de red

**🔹 Pregunta 9 — Caso SOC**

Varios equipos muestran inicios de sesión tipo 3 (red) desde una misma
cuenta hacia muchos servidores en minutos. Sugiere:

**A)** Actualización central\
**B)** Movimiento lateral automatizado\
**C)** Impresión\
**D)** Reinicio

**🔹 Pregunta 10**

Relaciona: 4720 + 4728 + 7045 en poco tiempo apunta a:

**A)** Fuerza bruta\
**B)** Persistencia con cuenta y servicio privilegiados\
**C)** Phishing de correo\
**D)** Spam

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: reune información.
2. **A**: persistencia (y escalada).
3. **A — Credential dumping**.
4. **B — Kerberoasting** sobre service tickets.
5. **A**: persistencia vía autoarranque.
6. **B**: oculta el comando.
7. **A**: movimiento lateral.
8. **B**: encubrimiento.
9. **B**: movimiento lateral.
10. **B**: persistencia con cuenta y servicio.



---

## Parte B — Guía completa del atacante al defensor (numeración original 14-26 corregida a secuencia continua)

Hasta ahora vimos:

**Perspectiva del administrador**

¿Cómo funciona Windows?

¿Cómo creo usuarios?

¿Cómo funcionan procesos?

¿Cómo funcionan servicios?

¿Cómo utilizo PowerShell?

¿Cómo veo logs?

¿Cómo protejo el sistema?

Ahora:

**Perspectiva del atacante**

¿Cómo obtiene acceso?

¿Cómo descubre el sistema?

¿Cómo obtiene privilegios?

¿Cómo roba credenciales?

¿Cómo mantiene acceso?

¿Cómo se mueve?

¿Cómo intenta evitar detección?

Y finalmente volvemos al SOC:

ATAQUE

↓

EVIDENCIA

↓

LOG

↓

DETECCIÓN

↓

SOC

**15. La cadena que vamos a estudiar**

Quiero que tengas este mapa:

WINDOWS ATTACK LIFECYCLE

ACCESO INICIAL

↓

EJECUCIÓN

↓

DESCUBRIMIENTO

↓

ESCALADA DE PRIVILEGIOS

↓

CREDENCIALES

↓

PERSISTENCIA

↓

MOVIMIENTO LATERAL

↓

OBJETIVO

↓

EVASIÓN / OCULTACIÓN

No necesariamente todos los ataques siguen exactamente esta secuencia, pero es un excelente modelo mental para estudiar.

**16. ① Acceso inicial**

Primera pregunta:

**¿Cómo consiguió el atacante entrar?**

Puede existir, entre otras posibilidades:

Credenciales robadas

Vulnerabilidad

Phishing

Servicio expuesto

Acceso remoto comprometido

Para el SOC:

4625

↓

4624

↓

¿Cómo ocurrió?

Acá ya utilizamos lo aprendido.

**17. ② Ejecución**

Una vez dentro:

**¿Cómo ejecuta código?**

Podría utilizar herramientas legítimas del sistema.

Por ejemplo:

PowerShell

CMD

WMI

Scripts

Esto es importante porque muchos ataques no necesitan necesariamente instalar un programa extraño inmediatamente.

Pueden abusar de herramientas legítimas.

Conceptualmente:

Herramienta legítima

↓

Uso legítimo

o

Uso malicioso

**18. ③ Descubrimiento**

Una vez dentro, el atacante necesita conocer el entorno.

Puede intentar descubrir:

Usuario actual

Equipo

Sistema operativo

Interfaces de red

Otros equipos

Dominios

Usuarios

Grupos

Servicios

Procesos

¿Por qué?

Porque un atacante que no conoce el entorno está prácticamente a ciegas.

**19. Y acá volvemos a CMD + PowerShell**

¿Recordás que estudiamos comandos?

Ahora cambia la perspectiva.

Antes:

"¿Cómo uso ipconfig?"

Ahora:

**"¿Qué podría aprender un atacante ejecutando ipconfig?"**

Por ejemplo:

ipconfig

puede proporcionar información sobre:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

Máscara

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

Y eso ayuda al atacante a comprender la red.

**20. Otro ejemplo conceptual**

Un atacante puede intentar consultar información sobre:

whoami

hostname

¿Qué obtiene?

whoami

↓

usuario actual

hostname

↓

nombre del equipo

Para un SOC:

4688

↓

cmd.exe

↓

whoami

↓

hostname

↓

ipconfig

puede ser una secuencia interesante dependiendo del contexto.

**21. ④ Escalada de privilegios**

Supongamos que el atacante consiguió acceso como:

Usuario estándar

Pero necesita:

Administrador

SYSTEM

Entonces aparece otra etapa:

**Privilege Escalation**

Conceptualmente:

Usuario

↓

Privilegios limitados

↓

Escalada

↓

Administrador / SYSTEM

Esto es importantísimo para Windows.

**22. ¿Por qué es tan importante?**

Porque controlar un usuario normal no equivale necesariamente a controlar el equipo.

Compará:

Usuario estándar

con:

Administrator

y:

SYSTEM

El impacto potencial aumenta muchísimo.

**23. ⑤ Credenciales**

Después tenemos:

**Credential Access**

Un atacante puede intentar obtener credenciales para:

Acceder a otros sistemas

Escalar privilegios

Mantener acceso

Moverse lateralmente

Acá vamos a estudiar posteriormente conceptos como:

Windows credentials

LSASS

NTLM

<a href="../../GLOSARIO.md#kerberos" target="_blank">Kerberos</a>

Tokens

Hashes

Y acá vuelve a aparecer lo que ya estudiamos sobre:

**Kerberos + Active Directory.**

Por eso estuvo bien que hayas pedido profundizarlo anteriormente.

**24. ⑥ Persistencia**

Ahora imaginemos:

Atacante

↓

entra

↓

hace algo

↓

se desconecta

Si no tiene persistencia:

puede perder el acceso.

Por eso puede intentar establecer un mecanismo que le permita volver.

Algunos conceptos que estudiaremos:

Servicios

Tareas programadas

Registry Run Keys

Cuentas

Startup

Y acá volvemos a:

Procesos

Servicios

Event Logs

**25. ⑦ Movimiento lateral**

Este concepto es fundamental para un SOC.

El atacante no necesariamente quiere quedarse en:

PC-01

Puede intentar pasar a:

PC-01

↓

SERVER-01

↓

SERVER-02

↓

<a href="../../GLOSARIO.md#dc" target="_blank">DC</a>-01

Esto se llama:

**Lateral Movement**

Y es una de las razones por las que aprender:

IP

DNS

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

Puertos

Windows

Active Directory

Kerberos

es tan importante.

Todo empieza a converger.

**26. ⑧ Evasión**

Finalmente:

**¿Cómo intenta evitar ser detectado?**

Puede intentar reducir su visibilidad o aprovechar herramientas legítimas para mezclarse con actividad normal.

Para el SOC esto significa buscar:

Comportamientos anómalos

Procesos extraños

Cambios inesperados

Logs

Conexiones

Persistencia

Por eso los Event Logs que acabamos de estudiar son tan importantes.

**🎯 La gran conexión**

Mirá lo que acabamos de construir:

ATAQUE WINDOWS

│

┌───────────┼────────────┐

↓ ↓ ↓

AUTENTICACIÓN PROCESOS RED

│ │ │

4624/4625 4688 TCP/IP

│ │ │

└───────────┼────────────┘

↓

PERSISTENCIA

↓

MOVIMIENTO LATERAL

↓

LOGS

↓

DEFENDER

↓

<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>

↓

SOC

**Esto es exactamente por lo que estamos estudiando estos temas en este orden.**

No son temas aislados.

**📚 Lo que sigue en nuestro programa**

Después de esta introducción a la perspectiva atacante, la progresión que te recomiendo es:

**Windows desde perspectiva atacante**

**1. Reconocimiento y enumeración**

- whoami

- hostname

- ipconfig

- systeminfo

- usuarios

- grupos

- procesos

- servicios

- red

**2. Ejecución**

- CMD

- PowerShell

- WMI

- scripts

**3. Privilegios**

- usuario vs administrador

- SYSTEM

- UAC

- conceptos de escalada

**4. Credenciales**

- LSASS

- NTLM

- Kerberos

- tokens

- hashes

**5. Persistencia**

- servicios

- tareas programadas

- Registry

- cuentas

**6. Movimiento lateral**

- SMB

- RDP

- WinRM

- administración remota

- Active Directory

**7. Evasión y detección**

- logs

- Defender

- PowerShell logging

- indicadores

- correlación SIEM

**8. Caso práctico SOC**

- investigar una máquina Windows comprometida de principio a fin.

**🖥️ SEMANA 4 — SISTEMAS WINDOWS**

**🕵️ Windows desde la perspectiva del atacante — Evasión y detección**

**1. ¿Qué significa "evasión"?**

Desde la perspectiva de un atacante:

**Evasión consiste en intentar evitar ser detectado o dificultar la investigación.**

Pero desde nuestra perspectiva de SOC, lo importante es:

**¿Qué intenta ocultar el atacante y qué evidencia podemos encontrar igualmente?**

**2. El atacante no quiere solamente entrar**

Imaginemos:

ATACANTE

↓

Obtiene acceso

↓

Ejecuta código

↓

Obtiene privilegios

↓

Mantiene acceso

Ahora tiene un problema:

🚨 Windows registra eventos

🚨 Defender puede detectar actividad

🚨 Firewall puede registrar conexiones

🚨 SIEM puede correlacionar eventos

Por eso intentará reducir su visibilidad.

**3. ¿Qué puede intentar ocultar?**

Un atacante podría intentar ocultar:

┌───────────────────────────┐

│ Actividad │

│ Procesos │

│ Archivos │

│ Persistencia │

│ Comunicaciones │

│ Identidad │

│ Herramientas utilizadas │

└───────────────────────────┘

Pero esto genera una idea fundamental:

**⚠️ Ocultar una evidencia no significa necesariamente eliminar todas las evidencias.**

Por ejemplo:

Proceso sospechoso

↓

Intenta ocultarse

↓

Pero...

↓

Event Log

Defender

<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>

DNS

Firewall

SIEM

pueden contener otras pistas.

**4. Living off the Land**

Este concepto es **muy importante para SOC**.

Se conoce como:

**Living off the Land (LotL)**

La idea general es utilizar herramientas legítimas que ya existen en Windows.

Por ejemplo:

PowerShell

CMD

WMI

Windows services

Task Scheduler

¿Por qué?

Porque un proceso llamado:

malware123.exe

puede llamar inmediatamente la atención.

Mientras que:

powershell.exe

es un componente legítimo de Windows.

Pero:

**Herramienta legítima ≠ uso legítimo.**

**5. Ejemplo**

Imaginemos:

Usuario

↓

WINWORD.EXE

↓

POWERSHELL.EXE

↓

script

PowerShell no es malware.

Pero la cadena puede ser sospechosa.

Por eso un SOC analiza:

¿Quién?

↓

¿Desde qué proceso?

↓

¿Qué <a href="../../GLOSARIO.md#command-line" target="_blank">command line</a>?

↓

¿Qué archivo?

↓

¿Qué hizo después?

Esto conecta directamente con nuestro **<a href="../../GLOSARIO.md#event-id" target="_blank">Event ID</a> 4688**.

**6. Evasión y Event Logs**

Un atacante puede intentar reducir o manipular evidencias.

Desde el punto de vista defensivo, eso es interesante.

Por ejemplo:

Actividad sospechosa

↓

Cambios inesperados

↓

Eventos de seguridad

↓

SOC

Si de repente observamos cambios anómalos en la configuración de logging, eso mismo puede convertirse en un indicador.

**7. ¿Por qué no debemos depender de una sola fuente?**

Este concepto es fundamental.

Supongamos que tenemos:

Windows Event Logs

↓

información

Pero una investigación seria puede incorporar:

Windows Logs

\+

Defender / EDR

\+

Firewall

\+

DNS

\+

<a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

\+

Proxy

\+

SIEM

Entonces:

INCIDENTE

↓

┌────────┼────────┐

↓ ↓ ↓

<a href="../../GLOSARIO.md#windows-defender" target="_blank">Windows Defender</a> Red

│ │ │

└────────┼────────┘

↓

SIEM

↓

SOC

Si una fuente no tiene información suficiente, otra puede proporcionar la pieza que falta.

**8. Detección basada en comportamiento**

Este es uno de los conceptos que quiero que te quede grabado.

No siempre buscamos:

"¿Existe un archivo conocido como malware?"

También buscamos:

**"¿Este comportamiento tiene sentido?"**

Ejemplo:

03:12

Usuario de contabilidad inicia sesión

03:13

PowerShell

03:14

CMD

03:15

Conexión externa

03:16

Creación de servicio

03:17

SYSTEM

Aunque no tengamos todavía un archivo identificado como malware:

**la secuencia es sospechosa.**

**9. Anomalía**

Otra palabra que vas a escuchar muchísimo en SOC:

**Anomalía**

Significa, simplificando:

Algo que se aparta del comportamiento esperado.

Ejemplo:

**Normal**

Administrador

09:00

PowerShell

Servidor de administración

**Anómalo**

Usuario de RRHH

03:00

PowerShell

Servidor crítico

El comando puede ser exactamente el mismo.

Lo que cambia es el **contexto**.

**10. Baseline + anomalía**

Recordá este concepto:

BASELINE

↓

¿Qué es normal?

↓

COMPARAR

↓

¿Qué cambió?

↓

ANOMALÍA

Esto es muy importante para detección.

**11. Indicadores de compromiso — IOC**

Otro concepto fundamental para SOC:

**IOC — Indicator of Compromise**

Son elementos que pueden indicar que un sistema fue comprometido.

Ejemplos:

Hash de archivo

IP maliciosa

Dominio sospechoso

Archivo sospechoso

Cuenta comprometida

Proceso anómalo

Por ejemplo:

PowerShell

↓

archivo sospechoso

↓

hash conocido

↓

conexión a IP maliciosa

Ahora tenemos varios indicadores.

**12. IOC vs comportamiento**

Esto también es importante.

**IOC**

Busca una evidencia concreta:

IP X

Hash Y

Dominio Z

**Comportamiento**

Busca una actividad sospechosa:

Word

↓

PowerShell

↓

script

↓

conexión externa

Un SOC moderno utiliza **ambos enfoques**.

**13. IOA — Indicator of Attack**

También vas a encontrarte con:

**IOA — Indicator of Attack**

Mientras que un IOC puede representar una evidencia de compromiso, un IOA se centra más en el **comportamiento o acción asociada a un ataque**.

Ejemplo conceptual:

IOC:

Archivo sospechoso

IOA:

Proceso de Office

↓

PowerShell

↓

actividad anómala

Para un SOC esto es muy útil porque permite detectar comportamientos incluso cuando todavía no conocemos exactamente el malware.

**14. Defensa en profundidad**

Ahora juntamos todo.

No queremos:

❌ Una única defensa

Queremos:

WINDOWS

│

┌──────────────┼──────────────┐

↓ ↓ ↓

Defender Firewall Logs

│ │ │

└──────────────┼──────────────┘

↓

EDR

↓

SIEM

↓

SOC

Si una defensa falla, otra puede detectar la actividad.

Eso se llama:

**Defense in Depth**

**15. ¿Qué busca realmente un SOC?**

No busca únicamente:

"Encontré malware."

Busca responder:

¿QUÉ ocurrió?

↓

¿CUÁNDO?

↓

¿DÓNDE?

↓

¿QUIÉN?

↓

¿CÓMO?

↓

¿QUÉ HIZO?

↓

¿HASTA DÓNDE LLEGÓ?

↓

¿SIGUE ACTIVO?

Eso es investigación.

**16. Ejemplo final**

Imaginemos esta alerta:

PC-VENTAS-03

02:10

4625

02:11

4625

02:12

4624

<a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a> 10

02:13

4688

powershell.exe

02:13

Command Line sospechosa

02:14

Conexión externa

02:15

Nuevo servicio

02:16

Defender genera alerta

Un principiante puede pensar:

"Defender detectó malware."

Un analista SOC piensa:

4625

↓

¿Intentos de acceso?

4624

↓

¿Quién entró?

Type 10

↓

¿RDP?

4688

↓

¿Qué proceso?

PowerShell

↓

¿Qué command line?

Conexión

↓

¿A dónde?

Servicio

↓

¿Persistencia?

Defender

↓

¿Qué detectó?

Todo

↓

¿Hay otros equipos?

Ese cambio de pensamiento es **exactamente lo que estamos buscando en tu formación**.

**🧠 RESUMEN DE SEMANA 4 — WINDOWS**

Hasta ahora trabajamos:

**Windows básico**

- usuarios

- grupos

- autenticación

- procesos

- servicios

- CMD

- PowerShell

**Windows avanzado**

- Kerberos

- Active Directory

- <a href="../../GLOSARIO.md#event-viewer" target="_blank">Event Viewer</a>

- Event ID 4624

- Event ID 4625

- Event ID 4688

- Defender

- Firewall

- logs

- correlación

- IOC

- IOA

- baseline

- anomalías

**Windows desde perspectiva atacante**

Acceso

↓

Ejecución

↓

Descubrimiento

↓

Escalada

↓

Credenciales

↓

Persistencia

↓

Movimiento lateral

↓

Evasión

**Windows desde perspectiva SOC**

EVENTO

↓

EVIDENCIA

↓

CORRELACIÓN

↓

DETECCIÓN

↓

INVESTIGACIÓN

↓

RESPUESTA

**🎓 ¿Y qué viene después?**

Con esto **cerramos conceptualmente el bloque de Windows desde atacante/defensor**. Lo siguiente es que hagamos el examen de esta etapa, pero hay algo que te recomiendo antes:

**un examen general de Windows de 20 preguntas**, mezclando los temas que vimos, en lugar de seguir haciendo exámenes aislados. Eso te va a mostrar si realmente podés conectar los conocimientos como un futuro SOC L1.

**🖥️ SEMANA 4 — WINDOWS**

**📝 EXAMEN GENERAL — 20 PREGUNTAS**

**Nivel:** Básico → Intermedio  
**Objetivo:** evaluar toda la etapa Windows.

**Pregunta 1**

¿Cuál es la función principal del sistema de archivos **NTFS**?

**A)** Gestionar conexiones TCP.

**B)** Administrar cómo se almacenan y protegen archivos y directorios.

**C)** Resolver nombres DNS.

**D)** Asignar direcciones IP.

**Pregunta 2**

¿Qué diferencia existe entre un **usuario** y un **grupo** en Windows?

**A)** Un usuario representa una identidad; un grupo permite organizar identidades y asignar permisos de forma colectiva.

**B)** Un grupo siempre tiene más privilegios que un administrador.

**C)** Un usuario solamente sirve para iniciar sesión y un grupo solamente para conectarse a Internet.

**D)** No existe diferencia.

**Pregunta 3**

¿Qué protocolo es especialmente importante en entornos **Active Directory** para autenticación?

**A)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

**B)** <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>.

**C)** Kerberos.

**D)** DHCP.

**Pregunta 4**

¿Cuál es el propósito principal de **Active Directory**?

**A)** Administrar exclusivamente conexiones Wi-Fi.

**B)** Gestionar identidades, equipos, recursos y políticas dentro de un entorno de dominio.

**C)** Reemplazar el antivirus.

**D)** Resolver todas las consultas DNS de Internet.

**Pregunta 5**

¿Qué representa principalmente el **Event ID 4624**?

**A)** Inicio de sesión exitoso.

**B)** Inicio de sesión fallido.

**C)** Creación de proceso.

**D)** Creación de usuario.

**Pregunta 6**

¿Qué representa principalmente el **Event ID 4625**?

**A)** Servicio iniciado.

**B)** Inicio de sesión fallido.

**C)** Inicio de sesión exitoso.

**D)** Proceso terminado.

**Pregunta 7**

¿Qué representa principalmente el **Event ID 4688**?

**A)** Creación de un proceso.

**B)** Cambio de contraseña.

**C)** Conexión DNS.

**D)** Inicio de sesión remoto.

**Pregunta 8**

¿Por qué el **Parent Process** es importante durante una investigación?

**A)** Porque indica la dirección IP del equipo.

**B)** Porque permite saber qué proceso creó/lanzó otro proceso.

**C)** Porque muestra la contraseña del usuario.

**D)** Porque reemplaza al Event ID.

**Pregunta 9**

Observás:

WINWORD.EXE

↓

POWERSHELL.EXE

↓

CMD.EXE

¿Qué debería hacer un analista SOC?

**A)** Declarar automáticamente que es malware.

**B)** Ignorarlo porque todos son procesos legítimos.

**C)** Investigar la cadena de procesos, usuario, command line y actividad posterior.

**D)** Eliminar inmediatamente Microsoft Office.

**Pregunta 10**

¿Cuál es la principal ventaja de **PowerShell** para un administrador?

**A)** Solamente permite navegar por Internet.

**B)** Permite automatizar y administrar Windows mediante comandos y scripts.

**C)** Reemplaza físicamente al procesador.

**D)** Es exclusivamente un antivirus.

**Pregunta 11**

¿Por qué PowerShell también es relevante para un SOC?

**A)** Porque nunca puede utilizarse con fines maliciosos.

**B)** Porque puede ser utilizado tanto legítimamente como abusivamente y deja información útil para investigar.

**C)** Porque solamente funciona cuando no existe Internet.

**D)** Porque sustituye al SIEM.

**Pregunta 12**

¿Qué función cumple principalmente **Microsoft Defender Antivirus**?

**A)** Asignar direcciones IP.

**B)** Detectar y proteger frente a malware y otras amenazas.

**C)** Administrar usuarios de Active Directory exclusivamente.

**D)** Resolver nombres DNS.

**Pregunta 13**

¿Cuál es la función principal de un **firewall**?

**A)** Controlar tráfico de red según reglas.

**B)** Crear usuarios.

**C)** Crear procesos.

**D)** Administrar archivos NTFS.

**Pregunta 14**

¿Qué es un **SIEM**?

**A)** Un sistema operativo.

**B)** Una herramienta destinada exclusivamente a eliminar virus.

**C)** Una plataforma que centraliza y correlaciona eventos y registros de múltiples fuentes.

**D)** Un protocolo de autenticación.

**Pregunta 15**

¿Por qué un SOC debería correlacionar eventos?

**A)** Porque un evento aislado puede no tener suficiente contexto para determinar si existe una amenaza.

**B)** Porque los Event ID no tienen significado.

**C)** Porque Defender no funciona sin SIEM.

**D)** Porque Windows genera solamente eventos falsos.

**Pregunta 16**

¿Qué significa **Privilege Escalation**?

**A)** Cambiar una dirección IP.

**B)** Obtener privilegios superiores a los que inicialmente posee una cuenta o proceso.

**C)** Crear una conexión DNS.

**D)** Cambiar un archivo de NTFS a FAT32.

**Pregunta 17**

¿Qué es **persistencia** desde la perspectiva de un atacante?

**A)** Intentar mantener acceso a un sistema después de que la sesión inicial termine.

**B)** Crear una contraseña más segura.

**C)** Actualizar Windows.

**D)** Eliminar todos los usuarios.

**Pregunta 18**

¿Qué significa **Lateral Movement**?

**A)** Mover archivos entre carpetas.

**B)** Desplazarse desde un sistema comprometido hacia otros sistemas de la organización.

**C)** Cambiar de TCP a <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

**D)** Cambiar el nombre del equipo.

**Pregunta 19**

¿Qué es un **IOC**?

**A)** Un indicador que puede proporcionar evidencia de compromiso, como un hash, IP o dominio asociado a una amenaza.

**B)** Un tipo de usuario Windows.

**C)** Un protocolo de red.

**D)** Un tipo de firewall.

**Pregunta 20 ⭐**

Un SOC observa:

4625

4625

4625

4624

4688 → powershell.exe

Conexión externa

Nuevo servicio

¿Cuál es la mejor interpretación?

**A)** Es malware confirmado.

**B)** Todos los eventos son normales porque pertenecen a Windows.

**C)** Existe una secuencia potencialmente sospechosa que debe investigarse y correlacionarse.

**D)** El problema necesariamente es DNS.

**⛔ PAUSA**

Anotá tus respuestas:

1-

2-

3-

4-

5-

6-

7-

8-

9-

10-

11-

12-

13-

14-

15-

16-

17-

18-

19-

20-

**✅ RESPUESTAS — EXAMEN GENERAL**

**1. B**

NTFS administra archivos y directorios y proporciona características como permisos, ACL, journaling y otras capacidades del sistema de archivos.

**2. A**

El usuario representa una identidad. Los grupos permiten agrupar usuarios y asignar permisos de manera colectiva.

**3. C**

Kerberos es un protocolo fundamental de autenticación en Active Directory.

**4. B**

Active Directory permite administrar identidades, equipos, recursos y políticas dentro de un entorno de dominio.

**5. A**

4624 = **Successful Logon**.

**6. B**

4625 = **Failed Logon**.

**7. A**

4688 = **Process Creation**.

**8. B**

El Parent Process permite reconstruir la relación entre procesos.

**9. C**

Una cadena de procesos sospechosa debe investigarse considerando contexto, usuario, command line, archivos y red.

**10. B**

PowerShell permite administrar y automatizar Windows mediante comandos y scripts.

**11. B**

PowerShell es legítimo, pero puede ser abusado. Para el SOC, su command line, proceso padre y contexto son muy importantes.

**12. B**

Microsoft Defender proporciona capacidades de protección y detección frente a malware y otras amenazas.

**13. A**

El firewall controla tráfico según reglas.

**14. C**

Un SIEM centraliza y correlaciona información de múltiples fuentes.

**15. A**

La correlación permite convertir eventos aislados en una secuencia con contexto.

**16. B**

Privilege Escalation significa obtener mayores privilegios.

**17. A**

Persistencia busca mantener acceso al sistema.

**18. B**

Lateral Movement consiste en desplazarse hacia otros sistemas de la organización.

**19. A**

Un IOC puede ser un hash, IP, dominio, archivo u otro elemento asociado con un compromiso.

**20. C**

La secuencia es potencialmente sospechosa, pero un SOC no debería afirmar compromiso únicamente con esos datos. Primero debe investigar y correlacionar.

**🏆 ESCALA DE RESULTADOS**

| **Resultado** | **Nivel**                    |
|---------------|------------------------------|
| **19–20**     | 🟢 Excelente                 |
| **17–18**     | 🟢 Muy bueno                 |
| **14–16**     | 🟡 Buen nivel                |
| **11–13**     | 🟠 Necesita repaso           |
| **0–10**      | 🔴 Conviene reforzar Windows |

**🛡️ EXAMEN 2**

**SOC L1 — NIVEL DIFÍCIL**

Este es **otro examen completamente separado**.

Acá cambia la modalidad.

Ya no te voy a preguntar:

"¿Qué significa 4624?"

Ahora te voy a dar situaciones y quiero que pienses como **analista SOC**.

**🚨 Pregunta 1**

El SIEM genera:

02:14 → 4625

02:14 → 4625

02:15 → 4625

02:15 → 4624

Usuario:

Administrator

Logon Type:

10

¿Cuál debería ser tu primera interpretación?

**A)** Ataque confirmado.

**B)** Existe una secuencia de intentos fallidos seguida de un acceso exitoso remoto que merece investigación.

**C)** Es necesariamente un problema de Kerberos.

**D)** El Event ID 4624 demuestra que la cuenta fue robada.

**🚨 Pregunta 2**

Encontrás:

4688

Parent:

WINWORD.EXE

Child:

POWERSHELL.EXE

User:

Empleado-RRHH

Command Line:

powershell.exe -File C:\Users\Empleado\Downloads\documento.ps1

¿Qué evidencia adicional sería más útil investigar primero?

**A)** El fondo de pantalla del usuario.

**B)** El contenido y origen del documento/script y la actividad posterior de PowerShell.

**C)** La versión de Microsoft Word únicamente.

**D)** El nombre del equipo únicamente.

**🚨 Pregunta 3**

Un usuario estándar aparece ejecutando:

powershell.exe

y posteriormente observás:

Nuevo proceso

SYSTEM

¿Qué concepto podría estar relacionado?

**A)** DHCP.

**B)** Privilege Escalation.

**C)** DNS.

**D)** <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**🚨 Pregunta 4**

Un equipo muestra:

4624

↓

4688 powershell.exe

↓

4688 cmd.exe

↓

TCP/443

↓

IP externa

¿Qué enfoque es más apropiado?

**A)** Investigar únicamente PowerShell.

**B)** Investigar únicamente la IP.

**C)** Correlacionar autenticación, procesos y actividad de red.

**D)** Reiniciar inmediatamente el equipo sin recopilar evidencia.

**🚨 Pregunta 5**

Observás:

PC-01

↓

Usuario comprometido

↓

Acceso a SERVER-01

↓

Acceso a SERVER-02

↓

Intento de acceso a DC-01

¿Qué comportamiento representa potencialmente?

**A)** Lateral Movement.

**B)** DHCP.

**C)** NAT.

**D)** Fragmentación IP.

**🚨 Pregunta 6**

Defender detecta un archivo sospechoso.

El analista encuentra:

Archivo:

update.exe

Ruta:

C:\Users\Juan\AppData\Temp\update.exe

Parent:

powershell.exe

Conexión:

IP externa

¿Cuál es la mejor conclusión?

**A)** Es malware confirmado únicamente por llamarse update.exe.

**B)** No es sospechoso porque update.exe es un nombre legítimo.

**C)** Hay múltiples elementos que justifican investigación: ruta, proceso padre y comunicación externa.

**D)** El archivo es necesariamente parte de Windows.

**🚨 Pregunta 7**

Un atacante utiliza una herramienta legítima de Windows para ejecutar acciones maliciosas.

¿Qué concepto describe mejor este comportamiento?

**A)** Living off the Land.

**B)** <a href="../../GLOSARIO.md#dhcp-starvation" target="_blank">DHCP starvation</a>.

**C)** NAT traversal.

**D)** DNS caching.

**🚨 Pregunta 8 ⭐**

Un SOC observa:

Usuario:

contabilidad01

Hora:

03:17

Proceso:

powershell.exe

Parent:

excel.exe

Conexión:

IP externa

Actividad:

Creación de servicio

El mismo usuario normalmente trabaja:

08:00 — 17:00

¿Cuál es el factor que más aumenta la sospecha?

**A)** Que PowerShell exista en Windows.

**B)** Que Excel exista en Windows.

**C)** La combinación de contexto temporal, cadena de procesos, red y persistencia potencial.

**D)** Que el equipo tenga NTFS.

**🚨 Pregunta 9 ⭐⭐**

Un atacante consigue acceso mediante credenciales comprometidas.

Después:

4624

↓

Discovery

↓

Privilege Escalation

↓

Credential Access

↓

Lateral Movement

¿Cuál es la mejor estrategia defensiva?

**A)** Buscar solamente el malware.

**B)** Analizar únicamente el primer 4624.

**C)** Reconstruir la cadena completa y buscar evidencia en endpoints, autenticación y red.

**D)** Bloquear todos los usuarios.

**🚨 Pregunta 10 ⭐⭐⭐**

Tenés esta situación:

Equipo: PC-FINANZAS-02

02:03

4625 × 8

02:05

4624

Logon Type 10

02:06

4688

WINWORD.EXE

02:06

4688

POWERSHELL.EXE

02:07

4688

CMD.EXE

02:08

Conexión TCP/443

IP externa

02:09

Defender:

Threat Detected

02:10

Nuevo servicio

02:11

Servicio ejecutándose como SYSTEM

¿Cuál sería la mejor descripción del incidente en una primera etapa?

**A)** "Malware confirmado."

**B)** "Actividad normal de Windows."

**C)** "Posible compromiso del endpoint con evidencia de autenticación sospechosa, ejecución de procesos, comunicación externa y posible persistencia; requiere investigación y respuesta."

**D)** "Problema de firewall."

**⛔ FIN DEL EXAMEN SOC L1**

Anotá:

1-

2-

3-

4-

5-

6-

7-

8-

9-

10-

**🧠 RESPUESTAS Y JUSTIFICACIÓN**

**1. ✅ B**

Tenemos:

4625

4625

4625

↓

4624

↓

Type 10

Type 10 está asociado a **Remote Interactive Logon**, por ejemplo RDP.

No podemos decir automáticamente que sea un ataque.

Pero:

fallos

↓

éxito

↓

acceso remoto

es suficiente para investigar.

**2. ✅ B**

La relación:

WINWORD

↓

PowerShell

↓

script

merece investigación.

Hay que conocer:

- origen del documento,

- contenido del script,

- command line,

- procesos posteriores,

- archivos creados,

- conexiones de red.

**3. ✅ B**

Pasar de un contexto de usuario estándar a ejecutar algo como **SYSTEM** puede indicar una posible **escalada de privilegios**.

No significa automáticamente explotación, pero es una señal importante.

**4. ✅ C**

La fuerza está en la correlación:

Autenticación

\+

Procesos

\+

Red

Esto permite construir una línea temporal.

**5. ✅ A**

El movimiento:

PC-01

↓

SERVER-01

↓

SERVER-02

↓

DC-01

es potencialmente **Lateral Movement**.

Y si el objetivo final es un Domain Controller, el riesgo puede ser especialmente elevado.

**6. ✅ C**

Nunca debemos decidir únicamente por el nombre.

Tenemos:

update.exe

\+

AppData\Temp

\+

PowerShell parent

\+

IP externa

La combinación aumenta significativamente la sospecha.

**7. ✅ A**

**Living off the Land** consiste, en términos generales, en abusar de herramientas legítimas disponibles en el sistema para realizar acciones.

Esto puede dificultar la detección basada únicamente en nombres de malware.

**8. ✅ C**

La anomalía no está simplemente en PowerShell.

Está en la combinación:

Usuario

\+

03:17

\+

Excel → PowerShell

\+

IP externa

\+

servicio

Esto demuestra nuevamente el valor del **contexto**.

**9. ✅ C**

Un SOC debe pensar en términos de cadena:

Acceso

↓

Descubrimiento

↓

Escalada

↓

Credenciales

↓

Movimiento

La investigación debe abarcar múltiples fuentes.

**🏆 10. ✅ C**

Esta es la respuesta que quiero que aprendas a formular como analista.

No decimos:

❌ "Es malware."

Decimos:

**"Tenemos evidencia que indica un posible compromiso y necesitamos investigar y responder."**

Porque tenemos:

4625 × 8

↓

4624 Type 10

↓

WINWORD

↓

PowerShell

↓

CMD

↓

TCP/443

↓

Defender

↓

Nuevo servicio

↓

SYSTEM

Eso es una **cadena de comportamiento altamente relevante**.

---

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ✅ **Módulo 25 — CMD y PowerShell**
-   ✅ **Módulo 26 — Windows Event Logs**
-   ✅ **Módulo 27 — Seguridad de Windows**
-   ✅ **Módulo 28 — Windows desde la perspectiva del atacante**
-   ⚪ Módulo 29 — Investigación SOC en Windows
