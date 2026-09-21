**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 24: Procesos y servicios**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Sistemas + Seguridad + Análisis SOC

Este módulo unifica la base operativa (Task Manager, `tasklist`/`taskkill`, padre→hijo, `services.msc`/`sc`, persistencia) con la profundización completa (PID, process tree, svchost, LSASS, Masquerading, Process Injection, Living off the Land).

**🎯 Objetivos del módulo**

Al terminar deberías poder explicar qué es un proceso/PID, padre→hijo y process tree, ruta y parent como evidencia, servicios y svchost, persistencia vía servicios, LSASS como objetivo sensible y cómo investiga un SOC (quién, cómo, cuándo, red, antes/después).


---

## Parte A — Base operativa

**1. Observar procesos (GUI)**

`Ctrl + Shift + Esc` abre el **Administrador de tareas**. Pestañas
clave:

-   **Procesos**: qué se ejecuta y su consumo.
-   **Detalles**: <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>, nombre de imagen, usuario.
-   **Servicios**: servicios en ejecución.

**2. Observar procesos (línea de comandos)**

```cmd
tasklist
```

Muestra PID, nombre de imagen y usuario. Para buscar uno concreto:

```cmd
tasklist | findstr powershell
```

Para terminar un proceso:

```cmd
taskkill /PID 1234 /F
```

**3. Proceso padre e hijo**

Cuando abres un programa, normalmente otro lo lanzó. Ejemplo:

explorer.exe

↓

notepad.exe

El **proceso padre** es `explorer.exe`; el **hijo** es `notepad.exe`.
Esto es oro para el SOC: un proceso hijo inesperado es una bandera. Por
ejemplo:

-   `powershell.exe` lanzado por `winword.exe` (Word) → posible
    macro maliciosa.
-   `cmd.exe` lanzado por `outlook.exe` → posible ejecución desde
    correo.

**4. Servicios de Windows**

Un servicio se ejecuta en segundo plano. Se gestiona con:

`services.msc` (interfaz gráfica)

O por línea de comandos:

```cmd
sc query
sc start NombreServicio
sc stop NombreServicio
sc delete NombreServicio
```

Muchos servicios legítimos corren bajo `svchost.exe`. Un atacante puede
**crear un servicio propio** para que su malware se inicie solo tras
cada reinicio (persistencia).

**5. Procesos que suelen aparecer (línea base)**

No todo lo raro es malware, pero conviene conocer la línea base:

-   `System` / `System Idle Process`.
-   `csrss.exe`, `winlogon.exe`, `lsass.exe` (maneja credenciales).
-   `svchost.exe` (host de servicios).
-   `explorer.exe` (interfaz de usuario).

`lsass.exe` es especialmente sensible: un atacante puede volcarlo
(**<a href="../../GLOSARIO.md#lsass" target="_blank">LSASS</a> dumping**) para robar hashes/<a href="../../GLOSARIO.md#ntlm" target="_blank">NTLM</a>.

**6. Indicadores de proceso sospechoso**

-   Nombre similar a uno legítimo: `svch0st.exe`, `taskmgr32.exe`.
-   Ubicación inusual: `C:\Users\X\Downloads\svchost.exe`.
-   Padre inesperado (Word → <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a>).
-   Se comunica a una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> externa recién al ejecutarse.
-   Se ejecuta como `SYSTEM` sin justificación.

**7. Persistencia mediante servicios**

Un atacante puede registrar un servicio:

```cmd
sc create Actualizador binPath= "C:\ruta\malware.exe"
```

Al reiniciar, el malware vuelve a ejecutarse. Por eso el SOC monitoriza
la **creación de servicios** (<a href="../../GLOSARIO.md#event-id" target="_blank">Event ID</a> <a href="../../GLOSARIO.md#7045" target="_blank">7045</a>).

**🧪 Laboratorio recomendado**

1.  Abre el Administrador de tareas y ordena por "Usuario".
2.  Ejecuta `tasklist` y localiza `powershell.exe`.
3.  Desde PowerShell, lanza `notepad.exe` y observa el padre con
    `Get-CimInstance Win32_Process` (módulo 25 lo amplía).
4.  En `services.msc`, identifica servicios que inician
    automáticamente.
5.  (Opcional, sin permisos reales) imagina cómo detectarías un servicio
    llamado `WindowsUpdateX` con ruta en `C:\Temp`.

**📝 Evaluación — Módulo 24: Procesos y servicios**

**🔹 Pregunta 1**

¿Qué relación indica que un proceso fue lanzado por otro?

**A)** Hijo → Padre\
**B)** Padre → Hijo\
**C)** Servicio → Puerto\
**D)** <a href="../../GLOSARIO.md#kernel" target="_blank">Kernel</a> → RAM

**🔹 Pregunta 2**

Ver `powershell.exe` como hijo de `winword.exe` (Word) sugiere:

**A)** Mantenimiento normal.\
**B)** Posible ejecución maliciosa desde documento.\
**C)** Error de impresión.\
**D)** Actualización de Windows.

**🔹 Pregunta 3**

El proceso que maneja credenciales y es objetivo de dumping es:

**A)** explorer.exe\
**B)** lsass.exe\
**C)** notepad.exe\
**D)** spoolsv.exe

**🔹 Pregunta 4**

¿Para qué sirve `taskkill /PID 1234 /F`?

**A)** Listar procesos.\
**B)** Forzar la terminación del PID 1234.\
**C)** Crear un servicio.\
**D)** Reiniciar la red.

**🔹 Pregunta 5**

`svchost.exe` normalmente:

**A)** Es siempre malware.\
**B)** Aloja servicios de Windows legítimos.\
**C)** Solo existe en Linux.\
**D)** Es el navegador.

**🔹 Pregunta 6**

Crear un servicio propio es una técnica de:

**A)** Persistencia.\
**B)** Borrado de logs.\
**C)** Cifrado de disco.\
**D)** Escaneo de puertos.

**🔹 Pregunta 7**

Un archivo `notepad.exe` ubicado en `C:\Users\X\AppData\Roaming\`
es:

**A)** Garantía de que es legítimo.\
**B)** Un indicador contextual de posible malware.\
**C)** Un servicio del sistema.\
**D)** El registro de Windows.

**🔹 Pregunta 8**

Para listar servicios por línea de comandos usamos:

**A)** `ipconfig`\
**B)** `sc query`\
**C)** `netstat -a`\
**D)** `ping`

**🔹 Pregunta 9 — Caso SOC**

Se detecta `cmd.exe` hijo de `outlook.exe` que luego ejecuta
`powershell.exe` con una conexión a una IP externa. Lo más razonable
es:

**A)** Ignorarlo, es correo legítimo.\
**B)** Investigar como posible cadena de ejecución maliciosa.\
**C)** Reiniciar el router.\
**D)** Desactivar el antivirus.

**🔹 Pregunta 10**

El Event ID que indica instalación de un nuevo servicio es:

**A)** <a href="../../GLOSARIO.md#4624" target="_blank">4624</a>\
**B)** 7045\
**C)** 4672\
**D)** 4720

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: el padre lanza al hijo.
2. **B**: Word lanzando PowerShell es patrón de macro maliciosa.
3. **B — lsass.exe**: objetivo de volcado de credenciales.
4. **B**: termina el proceso forzosamente.
5. **B**: svchost aloja servicios legítimos.
6. **A**: persistencia tras reinicio.
7. **B**: la ubicación es un indicador de alerta.
8. **B — `sc query`**: lista servicios.
9. **B**: es una cadena de ejecución sospechosa típica.
10. **B — 7045**: instalación de servicio.



---

## Parte B — Profundización: procesos, servicios y detección SOC

Hasta ahora vimos:

Windows

↓

NTFS

↓

Usuarios y grupos

↓

Autenticación

↓

<a href="../../GLOSARIO.md#active-directory" target="_blank">Active Directory</a> + <a href="../../GLOSARIO.md#kerberos" target="_blank">Kerberos</a>

Ahora agregamos una pieza fundamental:

USUARIO

↓

PROCESO

↓

SERVICIO

↓

RECURSO

Y esto es importantísimo porque **un atacante puede utilizar procesos y
servicios legítimos de Windows para ejecutar acciones maliciosas**.

**1. ¿Qué es un proceso?**

Un **proceso** es, simplificando, una instancia de un programa que está
siendo ejecutado por Windows.

Por ejemplo, cuando abrís el Bloc de notas:

notepad.exe

Windows crea un proceso.

Podemos verlo:

Programa en disco

↓

ejecución

↓

PROCESO

Otro ejemplo:

chrome.exe

explorer.exe

powershell.exe

notepad.exe

Cada uno puede tener uno o varios procesos en ejecución.

**2. Programa ≠ proceso**

Esta diferencia es importante.

Un **programa** es código almacenado en el disco.

Un **proceso** es una instancia de ese programa que está ejecutándose.

Por ejemplo:

C:\\Windows\\System32\\notepad.exe

es un archivo.

Cuando lo ejecutás:

notepad.exe

↓

PROCESO

↓

<a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 4520

**3. ¿Qué es un PID?**

PID significa:

**Process Identifier**

Es un identificador que Windows asigna a un proceso.

Por ejemplo:

Proceso PID

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

explorer.exe 3520

notepad.exe 4520

powershell.exe 8912

El PID es extremadamente útil para un analista SOC.

Si una alerta dice:

powershell.exe

PID: 8912

podemos investigar ese proceso concreto.

**4. ¿Dónde vemos los procesos?**

La herramienta más conocida es:

**Task Manager**

En español:

Administrador de tareas

Podés abrirlo con:

CTRL + SHIFT + ESC

Ahí podés observar información como:

-   Procesos.

-   CPU.

-   Memoria.

-   Disco.

-   Red.

-   Usuarios.

-   Servicios.

**5. Procesos padre e hijo**

Este concepto es **fundamental para SOC**.

Los procesos pueden crear otros procesos.

Por ejemplo:

explorer.exe

↓

<a href="../../GLOSARIO.md#cmd" target="_blank">cmd.exe</a>

↓

powershell.exe

↓

otro_proceso.exe

Esto genera una relación:

**Parent Process → Child Process**

Es decir:

Proceso padre

↓

Proceso hijo

**6. ¿Por qué importa esto para seguridad?**

Porque el **proceso padre puede revelar cómo se inició un proceso**.

Imaginemos:

explorer.exe

↓

notepad.exe

Eso puede ser perfectamente normal.

Pero imaginemos:

winword.exe

↓

powershell.exe

↓

cmd.exe

Eso merece atención.

No significa automáticamente que sea malware.

Pero un documento de Word normalmente no necesita iniciar PowerShell.

El SOC debería investigar el contexto.

**7. Árbol de procesos**

Podemos representar la relación:

explorer.exe

│

├── chrome.exe

│

├── notepad.exe

│

└── powershell.exe

│

└── cmd.exe

Esto se llama:

**Process Tree**

Para un SOC, un árbol de procesos puede ser muchísimo más útil que mirar
solamente el nombre del proceso.

**8. Ejemplo de una alerta SOC**

Imaginemos:

Usuario:

juan

Proceso:

powershell.exe

Parent:

winword.exe

Destino:

Internet

El analista debería preguntarse:

¿Juan abrió un documento?

↓

¿Word inició PowerShell?

↓

¿Por qué?

↓

¿Qué comando ejecutó PowerShell?

↓

¿Se conectó a Internet?

↓

¿Descargó algo?

Esto puede ser indicativo de una cadena de ataque.

**9. Procesos legítimos que pueden ser utilizados por atacantes**

Esto es muy importante.

Un atacante no necesariamente necesita instalar un programa llamado:

virus.exe

Puede utilizar herramientas legítimas de Windows.

Por ejemplo:

PowerShell

cmd

WMI

rundll32

regsvr32

mshta

Por eso en seguridad:

**El nombre de un proceso por sí solo no determina si es malicioso.**

Tenemos que analizar:

Nombre

\+

Ruta

\+

Usuario

\+

Proceso padre

\+

Argumentos

\+

Conexiones

\+

Comportamiento

**10. Un ejemplo muy importante**

Supongamos que encontramos:

powershell.exe

No podemos decir:

\"Es malware.\"

PowerShell es una herramienta legítima de Windows.

Pero:

powershell.exe

↓

Usuario: Juan

↓

Parent: winword.exe

↓

Conexión externa

↓

Descarga de archivo

es muchísimo más interesante para un SOC.

**11. Ruta del ejecutable**

Otro elemento fundamental:

¿Dónde está el archivo?

Por ejemplo, un proceso legítimo puede encontrarse en una ruta esperada
del sistema.

Pero imaginemos:

C:\\Windows\\System32\\svchost.exe

versus:

C:\\Users\\Juan\\Downloads\\svchost.exe

Ambos se llaman:

svchost.exe

pero el segundo debería generar sospechas.

Esto se relaciona con una técnica conocida como:

**<a href="../../GLOSARIO.md#masquerading" target="_blank">Masquerading</a>**

El atacante intenta hacer que un archivo parezca legítimo.

**12. El problema de los nombres**

Un atacante podría crear:

svch0st.exe

en lugar de:

svchost.exe

Observá la diferencia:

svchost

svch0st

↑

cero

A simple vista puede pasar desapercibido.

Por eso un SOC no debería confiar únicamente en el nombre.

**13. Procesos y privilegios**

Un proceso se ejecuta dentro de un contexto de seguridad.

Por ejemplo:

Usuario estándar

↓

Proceso

↓

Permisos limitados

o:

Administrador

↓

Proceso

↓

Mayores privilegios

Esto es fundamental.

Si un atacante consigue ejecutar código con privilegios elevados, puede
realizar acciones mucho más peligrosas.

**14. Principio de <a href="../../GLOSARIO.md#minimo-privilegio" target="_blank">mínimo privilegio</a> aplicado a procesos**

Recordemos:

**Mínimo privilegio = solamente los permisos necesarios.**

Aplicado a procesos:

Proceso

↓

Permisos necesarios

↓

Menor superficie de ataque

Si todo se ejecutara como administrador:

Proceso comprometido

↓

ADMINISTRADOR

↓

Mayor impacto

**15. ¿Qué es un servicio de Windows?**

Ahora pasamos a la segunda parte.

Un **servicio** es un componente diseñado para ejecutarse en segundo
plano y proporcionar una función al sistema o a otras aplicaciones.

Ejemplos conceptuales:

Servicio

↓

se ejecuta en segundo plano

↓

proporciona una función

No necesariamente requiere que un usuario esté interactuando con él.

**16. Ejemplos de servicios**

Windows tiene muchísimos.

Podemos encontrar servicios relacionados con:

-   Red.

-   Actualizaciones.

-   Seguridad.

-   Registro.

-   Impresión.

-   Eventos.

-   Administración remota.

Una herramienta para administrarlos es:

services.msc

Podés abrir:

Win + R

y escribir:

services.msc

**17. Servicio ≠ proceso**

Aunque están relacionados, no son exactamente lo mismo.

Podemos pensarlo así:

SERVICIO

↓

necesita ejecutarse

↓

PROCESO

Pero la relación puede ser más compleja.

Un servicio puede ejecutarse mediante un proceso específico o compartir
un proceso con otros servicios.

Por ejemplo, varios servicios pueden ejecutarse bajo:

svchost.exe

**18. ¿Qué es svchost.exe?**

Este proceso aparece muchísimo en Windows.

svchost.exe

Significa:

**Service Host**

Windows utiliza svchost.exe para alojar determinados servicios.

Por eso podés encontrar:

svchost.exe

svchost.exe

svchost.exe

svchost.exe

varias veces simultáneamente.

Esto **no significa automáticamente que haya malware**.

**19. ¿Por qué aparecen tantos svchost?**

Porque Windows puede separar distintos grupos de servicios en diferentes
procesos.

Conceptualmente:

svchost.exe

├── Servicio A

├── Servicio B

└── Servicio C

svchost.exe

├── Servicio D

└── Servicio E

Esto ayuda a aislar servicios y administrar recursos.

**20. Servicios y privilegios**

Los servicios pueden ejecutarse con cuentas especiales.

Por ejemplo:

LocalSystem

LocalService

NetworkService

**LocalSystem** tiene privilegios muy elevados en el sistema local.

Por eso:

Servicio comprometido

↓

cuenta con privilegios elevados

↓

alto impacto

es una situación de riesgo.

**21. ¿Cómo puede atacar un atacante los servicios?**

Una posibilidad es crear o modificar un servicio para conseguir
**persistencia**.

Conceptualmente:

Atacante

↓

Compromete equipo

↓

Crea/modifica servicio

↓

Servicio se ejecuta

↓

Código malicioso

Esto puede permitir que el atacante mantenga acceso incluso después de
reiniciar el equipo.

**22. Persistencia**

Recordemos este concepto:

**Persistencia = capacidad del atacante de mantener acceso o ejecución
después de determinados eventos, como un reinicio o cierre de sesión.**

Ejemplo:

Equipo

↓

Atacante consigue acceso

↓

Crea mecanismo de persistencia

↓

Reinicio

↓

Mecanismo vuelve a ejecutarse

Los servicios pueden utilizarse para esto.

**23. ¿Qué debería vigilar un SOC?**

Un SOC puede prestar atención a:

**🔎 Nuevos servicios**

Servicio nuevo creado

↓

Investigar

**🔎 Modificación de servicios**

Servicio existente

↓

Cambio inesperado

↓

Investigar

**🔎 Ruta sospechosa**

Servicio

↓

C:\\Users\\\...\\Temp\\archivo.exe

Puede ser sospechoso.

**🔎 Cuenta utilizada**

Servicio

↓

LocalSystem

Requiere contexto.

**🔎 Momento**

Servicio creado

↓

03:00 AM

Puede aumentar la sospecha si no existe una explicación.

**24. Proceso sospechoso vs proceso malicioso**

Esta distinción es muy importante para tu futuro trabajo.

No debemos pensar:

Proceso extraño

=

Malware

Debemos pensar:

Proceso extraño

↓

INDICADOR

↓

INVESTIGACIÓN

El SOC trabaja con **evidencias y contexto**.

**25. Ejemplo de análisis**

Tenemos:

Proceso:

powershell.exe

Usuario:

juan

Parent:

winword.exe

Ruta:

C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe

Hora:

03:30

Conexión:

Internet

Tenemos varios elementos.

**Ruta**

Parece legítima.

**Usuario**

Hay que identificarlo.

**Parent**

winword.exe

↓

powershell.exe

Es interesante.

**Hora**

03:30 puede ser inusual dependiendo de la organización.

**Red**

Existe una conexión externa.

Resultado:

**No podemos declarar malware solamente con estos datos, pero tenemos
suficiente información para abrir una investigación.**

**26. Ahora agregamos comandos**

Supongamos que PowerShell ejecutó algo equivalente a:

powershell.exe -enc \...

El parámetro:

-enc

es una abreviatura relacionada con la ejecución de comandos codificados.

Esto puede ser un indicador importante.

Pero nuevamente:

**Indicador ≠ confirmación automática de ataque.**

Hay que investigar.

**27. Process Tree sospechoso**

Un ejemplo más interesante:

WINWORD.EXE

│

└── POWERSHELL.EXE

│

└── CMD.EXE

│

└── CERTUTIL.EXE

Como SOC, deberíamos preguntarnos:

¿Por qué Word inició PowerShell?

¿Por qué PowerShell inició CMD?

¿Por qué CMD inició certutil?

¿Qué archivo se manipuló?

¿Hubo conexión de red?

La **cadena completa** es mucho más importante que un proceso
individual.

**28. Proceso + usuario + red**

Ahora juntamos todo lo aprendido.

Usuario

↓

Proceso

↓

Proceso hijo

↓

Conexión de red

↓

Archivo

Por ejemplo:

juan

↓

WINWORD.EXE

↓

POWERSHELL.EXE

↓

Internet

↓

archivo.exe

Esto permite al SOC reconstruir una posible cadena de ataque.

**29. <a href="../../GLOSARIO.md#process-injection" target="_blank">Process Injection</a>**

Ahora un concepto que vas a encontrar en seguridad:

**Process Injection**

Es una categoría de técnicas donde código malicioso intenta ejecutarse
dentro del contexto de otro proceso.

Conceptualmente:

Proceso legítimo

↑

Código malicioso

↓

Ejecución dentro / mediante otro proceso

¿Por qué hacerlo?

Porque puede ayudar al atacante a:

-   ocultar actividad,

-   evadir controles,

-   utilizar procesos legítimos.

No vamos a profundizar en la ejecución de estas técnicas ahora; lo
importante es reconocer el concepto.

**30. ¿Por qué un atacante quiere utilizar procesos legítimos?**

Porque puede ser más difícil distinguir:

malware.exe

de:

powershell.exe

o:

rundll32.exe

o:

wmi

El atacante intenta aprovechar herramientas que ya existen en el
sistema.

Esto suele relacionarse con:

**<a href="../../GLOSARIO.md#living-off-the-land" target="_blank">Living off the Land</a> (LotL)**

**31. Living off the Land**

Concepto:

Utilizar herramientas legítimas ya presentes en el sistema para realizar
actividades maliciosas.

Por ejemplo, un atacante podría abusar de herramientas administrativas
legítimas.

La idea:

Herramienta legítima

↓

Uso legítimo

\+

Uso malicioso

Por eso el SOC necesita analizar **comportamiento**, no simplemente
bloquear todo lo que sea PowerShell.

**32. Procesos importantes que deberías reconocer**

No hace falta memorizarlos todos todavía, pero empezá a familiarizarte
con:

explorer.exe

svchost.exe

services.exe

<a href="../../GLOSARIO.md#lsass" target="_blank">lsass</a>.exe

winlogon.exe

csrss.exe

smss.exe

powershell.exe

cmd.exe

conhost.exe

Algunos son procesos centrales del sistema.

**33. LSASS --- muy importante para SOC**

Uno especialmente importante:

lsass.exe

Está relacionado con funciones de seguridad y autenticación de Windows.

Por eso:

lsass.exe

es un proceso de **alta sensibilidad**.

Los atacantes pueden intentar obtener material de autenticación desde
procesos o mecanismos relacionados con LSASS.

Por eso un SOC presta mucha atención a comportamientos anómalos
relacionados con él.

**34. ¿Qué pasa si LSASS es comprometido?**

Simplificando:

LSASS

↓

información sensible de autenticación

↓

posible robo de credenciales

↓

movimiento lateral

Por eso una alerta relacionada con acceso sospechoso a LSASS puede tener
una prioridad elevada.

**35. Servicios + procesos + usuarios**

Ahora tenemos tres conceptos:

USUARIO

↓

ejecuta

↓

PROCESO

↓

puede estar asociado a

↓

SERVICIO

Y además:

PROCESO

↓

tiene

↓

PID

Esto nos permite construir una investigación.

**36. Ejemplo SOC completo**

Supongamos:

Usuario:

juan

Equipo:

PC-VENTAS-01

Proceso:

powershell.exe

PID:

4520

Parent:

winword.exe

Servicio:

ninguno

Conexión:

Internet

El SOC puede investigar:

¿Quién es Juan?

↓

¿Abrió Word?

↓

¿Qué documento abrió?

↓

¿Por qué Word ejecutó PowerShell?

↓

¿Qué comando ejecutó?

↓

¿Qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>/dominio contactó?

↓

¿Descargó algún archivo?

↓

¿Se ejecutaron otros procesos?

Esto ya es una investigación realista de endpoint.

**37. Herramientas que vas a conocer**

En Windows existen varias herramientas para investigar procesos y
servicios.

**Administrador de tareas**

taskmgr

**Servicios**

services.msc

**Process Explorer**

Herramienta avanzada de Microsoft Sysinternals.

**PowerShell**

Permite consultar procesos y servicios.

Por ejemplo, conceptualmente:

Get-Process

y:

Get-Service

Más adelante vamos a aprender estos comandos correctamente.

**38. ¿Qué debería aprender un futuro SOC Analyst?**

No alcanza con saber:

\"Esto es un proceso.\"

Necesitás poder responder:

¿Qué proceso es?

↓

¿Quién lo ejecutó?

↓

¿Con qué privilegios?

↓

¿Quién lo creó?

↓

¿Cuál es su proceso padre?

↓

¿Dónde está ubicado?

↓

¿Qué argumentos utilizó?

↓

¿Qué archivos modificó?

↓

¿Con qué <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> se comunicó?

↓

¿Qué ocurrió antes y después?

Ese razonamiento es mucho más importante que memorizar nombres.

**🧠 39. La regla de oro**

Quiero que te quede esta idea:

**En un SOC, un proceso legítimo puede formar parte de una actividad
maliciosa.**

Por ejemplo:

PowerShell

es legítimo.

Pero:

Word

↓

PowerShell

↓

descarga

↓

ejecución

↓

conexión externa

puede ser una cadena sospechosa.

Por eso:

**No investigamos solamente QUÉ se ejecutó. Investigamos QUIÉN, CÓMO,
CUÁNDO, DESDE DÓNDE y QUÉ HIZO DESPUÉS.**

**📌 Resumen para tus apuntes**

PROCESO

= programa en ejecución.

PID

= identificador del proceso.

PROCESO PADRE

= proceso que inició otro proceso.

PROCESO HIJO

= proceso iniciado por otro proceso.

PROCESS TREE

= representación de las relaciones entre procesos.

SERVICIO

= componente que funciona normalmente en segundo plano.

svchost.exe

= proceso utilizado por Windows para alojar determinados servicios.

LSASS.exe

= proceso sensible relacionado con funciones de seguridad/autenticación.

PERSISTENCIA

= mecanismo que permite mantener ejecución/acceso.

LIVING OFF THE LAND

= abuso de herramientas legítimas del sistema.

SOC

= analiza procesos + usuarios + privilegios + rutas + argumentos

\+ red + archivos + contexto.

**🎯 Conexión con lo que ya aprendiste**

Mirá cómo empieza a unirse todo:

WINDOWS

│

┌─────────┴─────────┐

↓ ↓

USUARIO SISTEMA

│ │

↓ ↓

AUTENTICACIÓN PROCESOS

│ │

┌─────┴─────┐ ↓

↓ ↓ SERVICIOS

Kerberos <a href="../../GLOSARIO.md#ntlm" target="_blank">NTLM</a> │

│ ↓

└──────────┬──────────────┘

↓

EVENTOS

↓

<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>

↓

ANALISTA SOC

El siguiente salto importante será **CMD + PowerShell**, porque ahí
vamos a empezar a ver cómo un analista puede utilizar la propia consola
de Windows para **investigar procesos, servicios, usuarios, conexiones y
actividad sospechosa**.

**🖥️ Semana 4 — Windows**

**📝 EXAMEN --- Procesos y Servicios**

**Nivel:** SOC Nivel 1 → Intermedio\
**Modalidad:** 10 preguntas Multiple Choice

Como venimos trabajando: **primero las 10 preguntas**, y después de
todas, las **respuestas con su justificación**.

**🔹 Pregunta 1**

¿Qué es un **proceso** en Windows?

**A)** Un archivo comprimido almacenado en NTFS.

**B)** Una instancia de un programa que está siendo ejecutada.

**C)** Una cuenta de usuario.

**D)** Una regla del Firewall.

**🔹 Pregunta 2**

¿Qué representa un **PID**?

**A)** El identificador asignado a un proceso.

**B)** La dirección IP del equipo.

**C)** El identificador de un usuario de Active Directory.

**D)** El nombre de un servicio.

**🔹 Pregunta 3**

Observá este árbol:

explorer.exe

│

└── powershell.exe

│

└── cmd.exe

¿Qué representa explorer.exe respecto de powershell.exe?

**A)** Proceso hijo.

**B)** Servicio.

**C)** Proceso padre.

**D)** Controlador de dominio.

**🔹 Pregunta 4**

Un SOC encuentra:

C:\\Windows\\System32\\svchost.exe

¿Cuál es la interpretación más correcta?

**A)** Es necesariamente malware porque svchost.exe es sospechoso.

**B)** Es necesariamente seguro porque está en Windows.

**C)** Es un proceso legítimo de Windows que puede alojar determinados
servicios, pero igualmente debe analizarse en contexto.

**D)** Es un archivo utilizado exclusivamente por Active Directory.

**🔹 Pregunta 5**

¿Cuál de las siguientes situaciones debería generar mayor interés para
un analista SOC?

**A)** explorer.exe → notepad.exe

**B)** explorer.exe → chrome.exe

**C)** winword.exe → powershell.exe → cmd.exe → conexión externa

**D)** services.exe → svchost.exe

**🔹 Pregunta 6**

¿Qué es un **servicio de Windows**?

**A)** Un programa que obligatoriamente requiere interacción constante
del usuario.

**B)** Un componente que normalmente funciona en segundo plano para
proporcionar determinadas funciones.

**C)** Un tipo de cuenta de Active Directory.

**D)** Un proceso que solamente existe durante el inicio de sesión.

**🔹 Pregunta 7 --- Caso SOC**

Un analista observa:

Usuario: juan

Proceso:

powershell.exe

Parent:

winword.exe

Hora:

03:30

Conexión:

Internet

¿Cuál es la mejor conclusión inicial?

**A)** Es malware confirmado.

**B)** Es completamente normal porque PowerShell es legítimo.

**C)** Hay varios indicadores que justifican una investigación
contextual.

**D)** Debe bloquearse inmediatamente todo PowerShell de la
organización.

**🔹 Pregunta 8**

¿Por qué un atacante podría utilizar una herramienta legítima como
PowerShell?

**A)** Porque las herramientas legítimas no pueden ser detectadas.

**B)** Porque puede aprovechar herramientas ya presentes en el sistema
para realizar acciones maliciosas.

**C)** Porque PowerShell solamente funciona con privilegios de
administrador.

**D)** Porque PowerShell reemplaza al antivirus.

**🔹 Pregunta 9 --- Caso SOC**

El SOC detecta:

Nuevo servicio creado

Nombre:

WindowsUpdateHelper

Ruta:

C:\\Users\\Juan\\AppData\\Temp\\update.exe

Cuenta:

LocalSystem

Hora:

02:47

¿Qué debería hacer el analista?

**A)** Ignorarlo porque el nombre contiene \"WindowsUpdate\".

**B)** Considerarlo automáticamente legítimo porque utiliza LocalSystem.

**C)** Investigar el servicio, su ruta, origen, proceso asociado,
usuario que lo creó y actividad posterior.

**D)** Eliminar inmediatamente todos los servicios relacionados con
Windows Update.

**🔹 Pregunta 10 --- Caso SOC ⭐**

Observás la siguiente cadena:

Usuario: juan

↓

WINWORD.EXE

↓

POWERSHELL.EXE

↓

CMD.EXE

↓

archivo.exe

↓

Conexión externa

↓

Nuevo servicio

↓

Persistencia

¿Qué describe mejor esta situación?

**A)** Una secuencia necesariamente normal de Windows.

**B)** Una posible cadena de ataque que combina ejecución, comunicación
externa y persistencia.

**C)** Un problema exclusivo de NTFS.

**D)** Una autenticación Kerberos normal.

**⛔ DETENTE AQUÍ**

Antes de mirar las respuestas, anotá:

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

Intentá resolverlas sin consultar nuevamente la explicación.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**Pregunta 1**

**✅ B --- Una instancia de un programa que está siendo ejecutada.**

La diferencia fundamental:

Programa

↓

archivo almacenado

Proceso

↓

programa ejecutándose

Por ejemplo:

C:\\Windows\\System32\\notepad.exe

es el archivo.

Cuando se ejecuta:

notepad.exe

↓

PROCESO

↓

PID

**Pregunta 2**

**✅ A --- El identificador asignado a un proceso.**

PID significa:

**Process Identifier**

Ejemplo:

powershell.exe

PID: 4520

El PID permite diferenciar ese proceso de otros procesos similares.

Para un SOC es útil porque una alerta puede referirse específicamente a
un proceso determinado.

**Pregunta 3**

**✅ C --- Proceso padre.**

Tenemos:

explorer.exe

↓

powershell.exe

explorer.exe creó/inició a powershell.exe en esa relación.

Por lo tanto:

explorer.exe = padre

powershell.exe = hijo

Esto es fundamental para analizar **Process Trees**.

**Pregunta 4**

**✅ C --- Es un proceso legítimo de Windows que puede alojar
determinados servicios, pero igualmente debe analizarse en contexto.**

svchost.exe es legítimo y se utiliza para alojar determinados servicios
de Windows.

Pero atención:

**Que un proceso tenga un nombre legítimo no significa que cualquier
instancia sea legítima.**

Un SOC debería analizar:

Ruta

↓

PID

↓

Servicios asociados

↓

Usuario

↓

Argumentos

↓

Conexiones de red

Por eso:

svchost.exe

por sí solo no confirma ni malware ni legitimidad.

**Pregunta 5**

**✅ C --- winword.exe → powershell.exe → cmd.exe → conexión externa**

Esta cadena merece especial atención:

Word

↓

PowerShell

↓

CMD

↓

Internet

No significa automáticamente que haya un ataque, pero combina varios
indicadores interesantes.

El analista debería investigar:

-   Documento abierto.

-   Usuario.

-   Comandos ejecutados.

-   Dominio/IP contactado.

-   Archivos creados.

-   Procesos posteriores.

**Pregunta 6**

**✅ B --- Un componente que normalmente funciona en segundo plano para
proporcionar determinadas funciones.**

Un servicio está diseñado para realizar funciones sin requerir que un
usuario interactúe continuamente con él.

Conceptualmente:

Windows

↓

Servicio

↓

Proceso en segundo plano

↓

Función

Ejemplos pueden estar relacionados con:

-   Actualizaciones.

-   Red.

-   Seguridad.

-   Eventos.

-   Administración.

**Pregunta 7**

**✅ C --- Hay varios indicadores que justifican una investigación
contextual.**

Tenemos:

winword.exe

↓

powershell.exe

↓

Internet

Además:

03:30

podría ser un horario inusual, dependiendo de la organización.

Pero no debemos cometer el error de decir:

\"PowerShell = malware.\"

PowerShell es una herramienta legítima.

El análisis correcto es:

Indicadores

↓

Contexto

↓

Correlación

↓

Investigación

**Pregunta 8**

**✅ B --- Porque puede aprovechar herramientas ya presentes en el
sistema para realizar acciones maliciosas.**

Esto se relaciona con:

**Living off the Land (LotL)**

El atacante utiliza herramientas legítimas disponibles en el sistema.

Por ejemplo:

PowerShell

CMD

WMI

La ventaja para el atacante es que esas herramientas pueden parecer
normales dentro de una organización.

Por eso el SOC debe analizar **cómo se utilizaron**, no simplemente si
existen.

**Pregunta 9**

**✅ C --- Investigar el servicio, su ruta, origen, proceso asociado,
usuario que lo creó y actividad posterior.**

Tenemos varios elementos interesantes:

Nuevo servicio

↓

Nombre que intenta parecer legítimo

↓

Ruta en AppData\\Temp

↓

archivo.exe

↓

LocalSystem

↓

02:47

Ninguno de estos datos por separado demuestra un ataque.

Pero juntos justifican una investigación.

Especialmente:

C:\\Users\\Juan\\AppData\\Temp\\update.exe

merece atención porque intenta utilizar un nombre relacionado con
actualización y está ubicado en una ruta poco habitual para un
componente central del sistema.

**Pregunta 10**

**✅ B --- Una posible cadena de ataque que combina ejecución,
comunicación externa y persistencia.**

La cadena:

Usuario

↓

Word

↓

PowerShell

↓

CMD

↓

archivo

↓

Internet

↓

Servicio

↓

Persistencia

es exactamente el tipo de secuencia que un SOC debería intentar
reconstruir.

Podríamos dividirla en fases:

EJECUCIÓN

↓

COMUNICACIÓN

↓

DESCARGA / ACTIVIDAD

↓

PERSISTENCIA

Y posteriormente investigar si hubo:

Escalada de privilegios

↓

Robo de credenciales

↓

Movimiento lateral

↓

Acceso a servidores

**🏆 RESULTADO**

  -----------------------------------------------------------------------
  **Correctas**   **Evaluación**
  --------------- -------------------------------------------------------
  **10/10**       🟢 Excelente

  **8--9/10**     🟢 Muy buen dominio

  **6--7/10**     🟡 Bien, reforzar algunos conceptos

  **4--5/10**     🟠 Conviene repasar

  **0--3/10**     🔴 Recomiendo volver al módulo
  -----------------------------------------------------------------------

**🧠 DESAFÍO SOC --- No cuenta para la nota**

Quiero que empieces a pensar como analista.

El <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> muestra:

Equipo: PC-CONTABILIDAD-02

Usuario: maria

22:41

WINWORD.EXE

22:42

└── POWERSHELL.EXE

22:42

└── CMD.EXE

22:43

└── archivo.exe

22:44

└── conexión a Internet

22:46

Nuevo servicio:

WindowsSecurityUpdate

22:46

Ruta:

C:\\Users\\Maria\\AppData\\Temp\\security.exe

22:47

Servicio ejecutándose como:

LocalSystem

Tu primera hipótesis **no debería ser automáticamente \"es malware\"**.

Debería ser:

**\"Tengo una cadena de eventos altamente sospechosa que necesito
investigar y correlacionar.\"**

Y ahí vas a buscar:

¿Quién inició WINWORD?

↓

¿Qué documento abrió?

↓

¿Qué comando ejecutó PowerShell?

↓

¿Qué hizo CMD?

↓

¿Qué es archivo.exe?

↓

¿Qué IP/dominio contactó?

↓

¿Quién creó el servicio?

↓

¿Desde qué proceso?

↓

¿Qué privilegios tenía?

↓

¿Hubo otros equipos afectados?

Ese cambio de pensamiento es una de las cosas que más quiero que
desarrolles durante esta carrera.

**📊 Semana 4 --- Estado**

✅ Fundamentos Windows

✅ NTFS

✅ Usuarios y grupos

✅ Autenticación

✅ Active Directory

✅ Kerberos

✅ Procesos y servicios

⏳ CMD + PowerShell

⏳ Windows Event Logs

⏳ Seguridad de Windows

⏳ Windows desde perspectiva atacante

⏳ Investigación SOC

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
