**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 26: Windows Event Logs**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Detección + Análisis de eventos de seguridad

Este módulo unifica la referencia de Event <a href="../../GLOSARIO.md#event-id" target="_blank">IDs</a> (<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>/<a href="../../GLOSARIO.md#4625" target="_blank">4625</a>/4672/<a href="../../GLOSARIO.md#4688" target="_blank">4688</a>/4720/<a href="../../GLOSARIO.md#7045" target="_blank">7045</a>/<a href="../../GLOSARIO.md#1102" target="_blank">1102</a>, Logon Type) con la guía larga (<a href="../../GLOSARIO.md#event-viewer" target="_blank">Event Viewer</a>, Security/System/Application, correlación, <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a> logging, SIEM) y la profundización 4624/4625/4688 (Logon Type, <a href="../../GLOSARIO.md#source-network-address" target="_blank">Source Network Address</a>, brute force vs <a href="../../GLOSARIO.md#password-spraying" target="_blank">password spraying</a>).

**🎯 Objetivos del módulo**

-   Abrir el **Visor de eventos** (`eventvwr.msc`) y distinguir Security/System/Application/PowerShell.
-   Memorizar los **Event IDs** clave y su significado SOC.
-   Diferenciar 4624 vs 4625 y usar Logon Type (2 interactivo, 3 red, 10 RDP).
-   Correlacionar 4625→4624→4688→red para reconstruir incidentes.


---

## Parte A — Referencia rápida

**1. El Visor de eventos**

`Win + R` → `eventvwr.msc`

Rutas principales:

-   **Registros de Windows → Seguridad**: auditoría de inicios,
    privilegios, cuenta.
-   **Registros de Windows → Sistema**: arranque, controladores,
    errores.
-   **Registros de Windows → Aplicación**: errores de programas.
-   **Registros de aplicaciones y servicios → Microsoft → Windows →
    PowerShell**: scripts ejecutados (si el logging está activado).

**2. Event IDs imprescindibles**

| <a href="../../GLOSARIO.md#event-id" target="_blank">Event ID</a> | Significado | Por qué importa al SOC |
| :--- | :--- | :--- |
| **4624** | Inicio de sesión exitoso | ¿De dónde? ¿A qué hora? |
| **4625** | Inicio de sesión fallido | Fuerza bruta, usuario erróneo |
| **4672** | Privilegios especiales asignados | Posible elevación |
| **4688** | Creación de proceso | ¿Qué se ejecutó y con qué padre? |
| **4689** | Fin de proceso | Cierre de la ejecución |
| **4720** | Creación de cuenta | Persistencia, cuenta falsa |
| **4722** | Cuenta habilitada | Reactivación sospechosa |
| **4728** | Miembro agregado a grupo (global) | Escalada de privilegios |
| **4732** | Miembro agregado a grupo (local) | Escalada local |
| **7045** | Instalación de servicio | Persistencia vía servicio |
| **1102** | Borrado de log de seguridad | Intento de encubrimiento |

**3. 4624 vs 4625**

-   **4625** repetido de una cuenta = posible **fuerza bruta**.
-   **4624** tras muchos 4625 = acceso exitoso tras ataque.
-   El campo **<a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a>** ayuda: `2` (interactivo), `3` (red),
    `10` (RDP/RemoteInteractive). Muchos 4624 tipo `3` desde <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>
    externa pueden ser escaneo.

**4. 4688 (creación de proceso)**

Si está habilitado el **Audit Process Creation**, 4688 muestra:

-   Nombre del proceso.
-   **Process ID** y **Parent Process ID**.
-   Línea de comandos (si se configuró).

Esto permite trazar: `explorer.exe` → `powershell.exe` → conexión.

**5. Borrado de logs (1102)**

Un atacante que borra el log de seguridad (1102) intenta **eliminar
evidencia**. El propio borrado es, por sí mismo, una alerta grave.

**6. Correlación básica**

Un incidente real se reconstruye uniendo IDs:

4625 (varios)

↓

4624 (éxito)

↓

4688 (powershell.exe)

↓

Conexión externa (netstat / Sysmon)

↓

Posible compromiso

Esto es **correlación de eventos**, el corazón del trabajo SOC.

**7. Limitaciones**

Los logs nativos no siempre traen la línea de comandos ni la conexión
de red. Por eso en fases posteriores usaremos **Sysmon** (Semana 8) y
un **<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>** (Semana 6) para enriquecerlos.

**🧪 Laboratorio recomendado**

1.  Abre `eventvwr.msc` → Seguridad.
2.  Filtra por ID `4624` y `4625`: ¿ves tus propios inicios?
3.  Busca el ID `4672` (privilegios especiales).
4.  (Opcional) Habilita la política *Audit Process Creation* y lanza
    un proceso para ver el 4688.
5.  Escribe en papel una cadena: 4625 → 4624 → 4688 → conexión.

**📝 Evaluación — Módulo 26: Windows Event Logs**

**🔹 Pregunta 1**

¿Qué herramienta gráfica abre los logs de Windows?

**A)** `regedit`\
**B)** `eventvwr.msc`\
**C)** `services.msc`\
**D)** `taskschd.msc`

**🔹 Pregunta 2**

El Event ID 4625 indica:

**A)** Inicio exitoso\
**B)** Inicio fallido\
**C)** Creación de proceso\
**D)** Borrado de log

**🔹 Pregunta 3**

Varios 4625 seguidos sugieren:

**A)** Actualización\
**B)** Fuerza bruta\
**C)** Apagado\
**D)** Impresión

**🔹 Pregunta 4**

El Event ID 4688 corresponde a:

**A)** Creación de proceso\
**B)** Borrado de usuario\
**C)** Inicio de sesión\
**D)** Instalación de servicio

**🔹 Pregunta 5**

El Event ID 7045 indica:

**A)** Creación de cuenta\
**B)** Instalación de servicio\
**C)** Inicio de sesión\
**D)** Privilegios especiales

**🔹 Pregunta 6**

El Event ID 1102 indica:

**A)** Inicio exitoso\
**B)** Borrado del log de seguridad\
**C)** Proceso nuevo\
**D)** Error de red

**🔹 Pregunta 7**

¿Qué campo del 4624 ayuda a distinguir un inicio en consola de uno por
RDP?

**A)** Logon Type\
**B)** <a href="../../GLOSARIO.md#rid" target="_blank">RID</a>\
**C)** <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>\
**D)** <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>

**🔹 Pregunta 8**

El Event ID 4720 indica:

**A)** Borrado de log\
**B)** Creación de cuenta\
**C)** Descarga de archivo\
**D)** Reinicio

**🔹 Pregunta 9 — Caso SOC**

Secuencia: 20 eventos 4625 (cuenta `admin`) → 1 evento 4624 → 4688
(`powershell.exe`). Conclusión más razonable:

**A)** Mantenimiento normal.\
**B)** Fuerza bruta seguida de acceso y ejecución sospechosa.\
**C)** Error de impresora.\
**D)** Actualización programada.

**🔹 Pregunta 10**

¿Por qué el SOC valora el Event ID 1102 aunque sea "solo un borrado"?

**A)** Porque mejora el rendimiento.\
**B)** Porque suele ser un intento de encubrir evidencias.\
**C)** Porque crea usuarios.\
**D)** Porque cifra el disco.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B — `eventvwr.msc`**.
2. **B — 4625**: inicio fallido.
3. **B**: fuerza bruta.
4. **A — 4688**: creación de proceso.
5. **B — 7045**: instalación de servicio.
6. **B — 1102**: borrado de log de seguridad.
7. **A — Logon Type** (10 = RDP).
8. **B — 4720**: creación de cuenta.
9. **B**: fuerza bruta + acceso + ejecución.
10. **B**: borrar logs suele ser encubrimiento.



---

## Parte B — Guía completa de Event Logs

Llegamos a un tema **fundamental para trabajar en un SOC**.

Hasta ahora aprendiste a reconocer:

Usuarios

↓

Procesos

↓

Servicios

↓

<a href="../../GLOSARIO.md#cmd" target="_blank">CMD</a> / PowerShell

↓

Conexiones de red

Pero aparece una pregunta fundamental:

**¿De dónde obtiene el SOC la evidencia de lo que ocurrió en una computadora Windows?**

Una de las respuestas principales son los:

**🔥 Windows Event Logs**

**1. ¿Qué son los Event Logs?**

Windows registra muchísimos acontecimientos que ocurren dentro del sistema.

Por ejemplo:

Usuario inició sesión

Usuario cerró sesión

Se creó un proceso

Se inició un servicio

Se produjo un error

Se modificó una configuración

Se utilizó PowerShell

Estos acontecimientos pueden quedar registrados como **eventos**.

Podemos imaginarlo así:

ACTIVIDAD EN WINDOWS

↓

EVENTO

↓

EVENT LOG

↓

SIEM

↓

ANALISTA SOC

**2. ¿Por qué son tan importantes para un SOC?**

Imaginá que una computadora fue comprometida.

El atacante podría:

1\. Obtener credenciales

2\. Iniciar sesión

3\. Ejecutar PowerShell

4\. Crear un proceso

5\. Crear persistencia

6\. Acceder a otros equipos

Si tenemos registros adecuados, podemos intentar reconstruir:

¿Quién?

¿Dónde?

¿Cuándo?

¿Qué hizo?

¿Cómo lo hizo?

¿Qué ocurrió después?

Esto es justamente lo que necesita un analista durante una investigación.

**3. Event Viewer**

Windows incluye una herramienta gráfica llamada:

**Event Viewer**

En español:

**Visor de eventos**

Podés abrirla con:

eventvwr.msc

También podés buscar:

Visor de eventos

en el menú Inicio.

**4. Las categorías principales**

Dentro del Visor de eventos vas a encontrar diferentes logs.

Los tres que quiero que conozcas primero son:

Application

Security

System

Y además vamos a estudiar:

PowerShell / Operational

**5. Application**

El log:

Application

contiene eventos relacionados con aplicaciones.

Por ejemplo:

Aplicación falló

Aplicación generó un error

Aplicación produjo determinado evento

Para un SOC puede ser útil dependiendo del incidente.

**6. System**

El log:

System

registra eventos relacionados con componentes del sistema operativo.

Por ejemplo:

Servicios

Drivers

Componentes de Windows

Errores del sistema

Inicio/parada de determinados componentes

**7. Security — ⭐ MUY IMPORTANTE**

Para un SOC, probablemente uno de los logs más importantes sea:

Security

Porque puede contener eventos relacionados con:

- autenticación,

- logins,

- logoffs,

- cuentas,

- privilegios,

- acceso a determinados recursos,

- cambios de seguridad.

Por ejemplo:

Usuario

↓

Login

↓

Security Log

Esto nos permite investigar actividad relacionada con identidades.

**8. Event ID**

Cada evento puede tener un identificador:

**Event ID**

Por ejemplo, en Windows existen eventos conocidos como:

4624

4625

4688

No quiero que los memorices todos todavía.

Pero sí quiero que entiendas:

Event ID

↓

identifica un tipo de evento

**9. Event ID 4624**

Este es uno de los que tenés que empezar a reconocer.

**4624**

Representa:

**Un inicio de sesión exitoso.**

Conceptualmente:

Usuario

↓

Login exitoso

↓

Event ID 4624

Esto puede ser extremadamente útil en un SOC.

**10. Event ID 4625**

Ahora:

**4625**

Representa:

**Un intento de inicio de sesión que falló.**

Por ejemplo:

22:01 → 4625

22:02 → 4625

22:03 → 4625

22:04 → 4624

Esto podría indicar simplemente que alguien escribió mal la contraseña.

Pero también puede ser:

múltiples intentos

↓

posible ataque de fuerza bruta

Por eso necesitamos contexto.

**11. Un ejemplo SOC**

Supongamos que encontramos:

Usuario: administrador

4625

4625

4625

4625

4625

4624

¿Qué pasó?

Podríamos tener:

múltiples fallos

↓

login exitoso

Esto es interesante.

El SOC debería investigar:

¿Desde qué IP?

¿Desde qué equipo?

¿A qué hora?

¿Era habitual?

¿Quién utilizó la cuenta?

¿Qué ocurrió después?

**12. No confundir evento con ataque**

Esto es importantísimo.

Encontrar:

4625

no significa:

"Ataque confirmado."

Puede ser simplemente:

Usuario olvidó su contraseña.

Pero:

4625

4625

4625

4625

4625

4624

desde una IP desconocida puede aumentar considerablemente la sospecha.

El SOC analiza **patrones**.

**13. Event ID 4688 ⭐**

Otro evento extremadamente importante:

**4688**

Está relacionado con:

**Creación de un nuevo proceso.**

Esto conecta directamente con lo que estudiamos anteriormente.

Recordemos:

Proceso

↓

PID

↓

Parent Process

↓

<a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a>

Ahora agregamos:

EVENT LOG

Tenemos:

Proceso creado

↓

Event ID 4688

↓

Registro

↓

SIEM

↓

SOC

**14. Ejemplo**

Imaginemos:

4688

New Process:

powershell.exe

Parent:

winword.exe

User:

Juan

Ahora tenemos evidencia registrada de que:

WINWORD.EXE

↓

POWERSHELL.EXE

Esto puede ser muy útil durante una investigación.

**15. Command Line**

Dependiendo de la configuración de auditoría, los eventos de creación de procesos pueden proporcionar información adicional, como la línea de comandos.

Por ejemplo:

powershell.exe -File C:\Users\Juan\Downloads\factura.ps1

Esto es mucho más valioso que saber únicamente:

powershell.exe

Porque podemos conocer **cómo fue ejecutado**.

**16. Acá empieza a aparecer el verdadero trabajo SOC**

Anteriormente vimos:

WINWORD

↓

PowerShell

↓

CMD

Ahora podemos tener:

4688

↓

WINWORD

↓

4688

↓

PowerShell

↓

4688

↓

CMD

Estamos empezando a reconstruir una **línea temporal**.

**17. Línea temporal**

Una investigación puede terminar pareciéndose a esto:

22:01

4624

Login exitoso

22:03

4688

WINWORD.EXE

22:04

4688

POWERSHELL.EXE

22:04

4688

CMD.EXE

22:05

Conexión externa

22:07

Nuevo servicio

22:08

Actividad sospechosa

Ahora podemos preguntarnos:

¿Qué ocurrió realmente?

**18. Correlación**

La palabra que quiero que empieces a incorporar es:

**CORRELACIÓN**

Un evento aislado puede no significar mucho.

Pero:

4624

\+

4688

\+

conexión de red

\+

nuevo servicio

puede contar una historia.

El SOC busca precisamente eso:

EVENTO

\+

EVENTO

\+

EVENTO

↓

CONTEXTO

↓

POSIBLE INCIDENTE

**19. PowerShell Logs**

Como acabamos de estudiar PowerShell, ahora conectamos ambos temas.

Windows puede registrar información de PowerShell mediante distintos mecanismos.

Algunos importantes:

PowerShell Operational

<a href="../../GLOSARIO.md#script-block-logging" target="_blank">Script Block Logging</a>

Module Logging

Estos registros pueden aportar información útil sobre actividad de PowerShell.

**20. Script Block Logging**

Este concepto es especialmente importante.

Puede registrar información relacionada con bloques de código que PowerShell procesa.

Para un SOC esto puede ayudar a responder:

**¿Qué estaba intentando ejecutar PowerShell?**

Esto puede ser mucho más valioso que simplemente saber:

powershell.exe

**21. Por qué un atacante puede preocuparse por los logs**

Los registros son evidencia.

Un atacante que quiera permanecer oculto puede intentar:

evitar detección

↓

evitar generar indicadores

↓

borrar/modificar evidencias

Por eso la seguridad de los logs es importante.

En una arquitectura empresarial, los eventos suelen enviarse a sistemas centrales.

Por ejemplo:

PC

↓

Event Logs

↓

Collector / Agent

↓

SIEM

Esto evita depender exclusivamente de la máquina comprometida.

**22. ¿Qué es un SIEM?**

Ya lo mencionamos varias veces.

SIEM significa:

**Security Information and Event Management**

Su función general es recopilar y correlacionar eventos de diferentes fuentes.

Por ejemplo:

Windows

Linux

Firewall

<a href="../../GLOSARIO.md#vpn" target="_blank">VPN</a>

<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

Proxy

Cloud

↓

SIEM

↓

ALERTAS

↓

SOC

Esto es exactamente hacia donde estamos llevando tu formación.

**23. Ejemplo de correlación realista**

Supongamos que el SIEM recibe:

PC-01

4625

IP desconocida

Después:

PC-01

4625

IP desconocida

Después:

PC-01

4624

IP desconocida

Y luego:

PC-01

4688

powershell.exe

Y después:

PC-01

Conexión externa

Una alerta podría correlacionar todo:

Fallos de autenticación

↓

Login exitoso

↓

PowerShell

↓

Conexión externa

Eso es mucho más interesante que cada evento individual.

**24. Event ID no significa severidad**

Otro concepto importante.

No pienses:

4624 = malo

4625 = malo

4688 = malo

Incorrecto.

Los Event ID describen **qué ocurrió**.

La gravedad depende del contexto.

Por ejemplo:

4624

puede ser:

🟢 completamente normal.

Pero:

4624

\+

IP desconocida

\+

horario extraño

\+

cuenta privilegiada

\+

PowerShell

puede ser:

🔴 muy sospechoso.

**25. Event ID + usuario**

Siempre preguntá:

¿Quién?

Ejemplo:

4624

Usuario: Juan

No es igual que:

4624

Usuario: Administrator

Y tampoco:

4624

Usuario: SYSTEM

El contexto de identidad es fundamental.

**26. Event ID + IP**

También:

¿Desde dónde?

Ejemplo:

4624

Usuario: Juan

IP: 192.168.1.25

vs:

4624

Usuario: Juan

IP: 185.x.x.x

El segundo podría requerir investigación dependiendo de la arquitectura de la organización.

**27. Event ID + horario**

También:

¿Cuándo?

Por ejemplo:

4624

Usuario: Juan

03:42 AM

Si Juan trabaja normalmente:

08:00 → 17:00

el evento puede ser anómalo.

Pero nuevamente:

**Anómalo no significa automáticamente malicioso.**

Puede existir una explicación legítima.

**28. Event ID + proceso**

Ahora juntamos todo:

4624

↓

Login exitoso

4688

↓

PowerShell

4688

↓

CMD

Conexión externa

↓

Nuevo servicio

Ya tenemos una posible cadena.

**29. ¿Qué debería hacer el analista?**

No debería saltar inmediatamente a:

"Es un ataque."

Debe realizar un proceso:

1\. Detectar

↓

2\. Validar

↓

3\. Correlacionar

↓

4\. Investigar

↓

5\. Determinar severidad

↓

6\. Contener si corresponde

↓

7\. Documentar

Esto es mucho más cercano al trabajo real de un SOC.

**30. Un ejemplo completo**

Supongamos:

Equipo:

PC-VENTAS-05

Usuario:

juan

Eventos:

23:10

4625

Login fallido

23:11

4625

Login fallido

23:12

4624

Login exitoso

23:13

4688

powershell.exe

23:13

4688

cmd.exe

23:14

Conexión externa

23:16

Nuevo servicio

Como analista, yo no investigaría solamente:

"¿Qué hizo PowerShell?"

Miraría la secuencia completa.

**31. ¿Qué hipótesis podríamos plantear?**

Una posible hipótesis:

Intentos de autenticación

↓

Acceso conseguido

↓

Ejecución

↓

Actividad de red

↓

Persistencia

Podría ser:

compromiso

Pero también podría existir una explicación administrativa legítima.

Por eso necesitamos evidencia adicional.

**32. ¿Qué información buscaríamos?**

Podríamos buscar:

**Identidad**

Usuario

Grupo

Privilegios

**Endpoint**

Hostname

IP

Procesos

Servicios

Archivos

**Red**

IP destino

Puerto

Dominio

DNS

**Autenticación**

4624

4625

**Procesos**

4688

**PowerShell**

logs de PowerShell

**33. Windows Event Logs + todo lo anterior**

Fijate cómo ahora la Semana 4 empieza a convertirse en una sola unidad:

WINDOWS

│

┌─────────────┼─────────────┐

↓ ↓ ↓

USUARIO PROCESOS SERVICIOS

│ │ │

↓ ↓ ↓

AUTENTICACIÓN CMD/PS PERSISTENCIA

│ │

└──────┬──────┘

↓

EVENT LOGS

↓

SIEM

↓

SOC

Este es exactamente el tipo de integración que quiero que tengas en la cabeza.

**34. 🎯 Los Event ID que quiero que empieces a recordar**

Por ahora, solamente estos:

| **Event ID** | **Concepto**             |
|--------------|--------------------------|
| **4624**     | Inicio de sesión exitoso |
| **4625**     | Inicio de sesión fallido |
| **4688**     | Creación de proceso      |

No te preocupes todavía por memorizar decenas de IDs.

Primero quiero que seas capaz de razonar:

4624

↓

¿Quién entró?

4625

↓

¿Quién intentó entrar y falló?

4688

↓

¿Qué proceso apareció?

**35. 🧠 Regla de oro del SOC**

Quiero que agregues esta frase a tus apuntes:

**Un Event ID aislado describe un evento. Una secuencia de eventos puede describir un comportamiento.**

Por ejemplo:

4625

es simplemente:

Login fallido.

Pero:

4625

4625

4625

4624

4688 PowerShell

Conexión externa

Nuevo servicio

ya puede representar:

**Una posible cadena de ataque que requiere investigación.**

**📚 Resumen de la clase**

EVENT LOG

= registro de acontecimientos de Windows.

EVENT VIEWER

= herramienta gráfica para consultar eventos.

SECURITY

= log especialmente importante para autenticación y seguridad.

SYSTEM

= eventos relacionados con componentes del sistema.

APPLICATION

= eventos relacionados con aplicaciones.

4624

= login exitoso.

4625

= login fallido.

4688

= creación de proceso.

SIEM

= recopila y correlaciona eventos de múltiples fuentes.

CORRELACIÓN

= relacionar diferentes eventos para encontrar patrones.

SOC

= analiza eventos + contexto + comportamiento.

**🧩 Y ahora aparece algo muy interesante**

Ya aprendiste:

Redes

↓

IP / puertos / <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> / <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> / DNS

y:

Windows

↓

Usuarios / procesos / servicios / PowerShell

Ahora los Event Logs permiten **unir ambas cosas**:

Usuario

↓

Proceso

↓

Conexión

↓

IP

↓

Puerto

↓

Evento

↓

SIEM

↓

Analista SOC

Ese es el puente entre **administrar Windows** y **investigar incidentes de seguridad**.

**🖥️ Semana 4 — Windows**

**📝 Examen B (ampliado) — Windows Event Logs**

**Nivel:** SOC Nivel 1 → Intermedio  
**Modalidad:** 10 preguntas Multiple Choice

Como venimos trabajando: **primero las 10 preguntas**, después las **respuestas con su justificación**.

**🔹 Pregunta 1**

¿Qué son los **Windows Event Logs**?

**A)** Archivos utilizados exclusivamente para guardar contraseñas.

**B)** Registros de acontecimientos que ocurren en Windows.

**C)** Un sistema antivirus integrado en Windows.

**D)** Un tipo de firewall.

**🔹 Pregunta 2**

¿Qué herramienta gráfica permite consultar los eventos de Windows?

**A)** Task Manager.

**B)** Device Manager.

**C)** Event Viewer / Visor de eventos.

**D)** Registry Editor.

**🔹 Pregunta 3**

¿Qué representa principalmente el **Event ID 4624**?

**A)** Inicio de sesión exitoso.

**B)** Inicio de sesión fallido.

**C)** Creación de un proceso.

**D)** Creación de un servicio.

**🔹 Pregunta 4**

¿Qué representa principalmente el **Event ID 4625**?

**A)** Un proceso finalizado.

**B)** Un inicio de sesión fallido.

**C)** Una conexión TCP.

**D)** Un inicio de sesión exitoso.

**🔹 Pregunta 5**

¿Qué representa principalmente el **Event ID 4688**?

**A)** Creación de un nuevo proceso.

**B)** Eliminación de un usuario.

**C)** Inicio de sesión exitoso.

**D)** Cambio de dirección IP.

**🔹 Pregunta 6**

Un SOC encuentra:

22:01 → 4625

22:02 → 4625

22:03 → 4625

22:04 → 4624

¿Qué interpretación es más adecuada?

**A)** Es malware confirmado.

**B)** Es necesariamente un error del sistema.

**C)** Hay múltiples intentos fallidos seguidos de un inicio de sesión exitoso y merece investigación contextual.

**D)** Significa que se creó un nuevo proceso.

**🔹 Pregunta 7 — Caso SOC**

Se registra:

Event ID: 4688

Parent Process:

WINWORD.EXE

New Process:

POWERSHELL.EXE

User:

Juan

Command Line:

powershell.exe -File C:\Users\Juan\Downloads\factura.ps1

¿Cuál es la mejor respuesta del analista?

**A)** Ignorar el evento porque PowerShell es legítimo.

**B)** Declarar inmediatamente que es malware.

**C)** Investigar el documento, el script, el usuario, la línea de comandos y la actividad posterior.

**D)** Eliminar PowerShell del equipo.

**🔹 Pregunta 8**

¿Por qué un SOC no debería analizar un Event ID de manera aislada?

**A)** Porque los Event ID nunca contienen información útil.

**B)** Porque el significado de un evento depende del contexto y su relación con otros eventos.

**C)** Porque solamente los administradores pueden leer Event Logs.

**D)** Porque todos los eventos de Windows son falsos positivos.

**🔹 Pregunta 9 — Caso SOC ⭐**

El SIEM muestra:

Equipo: PC-VENTAS-05

Usuario: Carlos

4625

4625

4625

4624

4688 → powershell.exe

Conexión externa

Nuevo servicio

¿Qué debería hacer principalmente el analista?

**A)** Concluir automáticamente que es un ataque.

**B)** Ignorar los 4625 porque los intentos fallidos no son importantes.

**C)** Correlacionar los eventos y construir una línea temporal para determinar qué ocurrió.

**D)** Reiniciar el equipo inmediatamente.

**🔹 Pregunta 10 — Caso SOC ⭐⭐⭐**

Observás:

03:10

4624

Usuario administrador

03:12

4688

powershell.exe

03:13

4688

cmd.exe

03:14

Conexión a IP externa

03:16

Nuevo servicio

03:17

El servicio comienza a ejecutarse como SYSTEM

¿Cuál es la interpretación más profesional?

**A)** Todos los eventos son normales porque pertenecen a Windows.

**B)** Es malware confirmado sin necesidad de más información.

**C)** Existe una secuencia potencialmente sospechosa que combina autenticación, ejecución, comunicación y posible persistencia, por lo que requiere investigación.

**D)** El problema corresponde exclusivamente a DNS.

**⛔ PAUSA — RESOLVÉ ANTES DE CONTINUAR**

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

No busques memorizar solamente los números. Intentá pensar:

**¿Qué información necesitaría yo si estuviera investigando este equipo en un SOC?**

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**1. ✅ B — Registros de acontecimientos que ocurren en Windows**

Los Event Logs registran diferentes acontecimientos:

Usuario inicia sesión

↓

Proceso creado

↓

Servicio iniciado

↓

Error

↓

Actividad de PowerShell

Para un SOC son una fuente fundamental de evidencia.

**2. ✅ C — Event Viewer / Visor de eventos**

Windows incluye:

**Event Viewer**

También podés abrirlo mediante:

eventvwr.msc

Desde allí podemos consultar diferentes logs, como:

Application

Security

System

y otros registros especializados.

**3. ✅ A — Inicio de sesión exitoso**

**4624**

Significa:

**Successful Logon**

Es decir, un inicio de sesión exitoso.

Ejemplo:

Usuario: Juan

Event ID: 4624

Pero atención:

**4624 no significa "actividad legítima".**

Hay que investigar el contexto:

¿Quién?

¿Desde dónde?

¿Cuándo?

¿Cómo?

¿Qué hizo después?

**4. ✅ B — Inicio de sesión fallido**

**4625**

Representa:

**Failed Logon**

Por ejemplo:

4625

4625

4625

4625

puede indicar múltiples intentos fallidos.

Pero nuevamente:

4625 ≠ ataque confirmado

Puede ser simplemente un usuario introduciendo mal su contraseña.

El contexto es fundamental.

**5. ✅ A — Creación de un nuevo proceso**

**4688**

Está relacionado con:

**Process Creation**

Esto es muy importante para un SOC porque permite investigar la ejecución de programas.

Por ejemplo:

4688

↓

powershell.exe

Y podemos intentar conocer:

Usuario

Proceso padre

Command Line

Ruta

Hora

**6. ✅ C — Múltiples fallos seguidos de un login exitoso**

Tenemos:

4625

4625

4625

↓

4624

Esto merece investigación.

Podría ser:

**Caso legítimo**

Usuario olvidó su contraseña

↓

varios intentos

↓

finalmente acertó

Pero también podría representar:

Intentos de acceso

↓

credencial válida encontrada

↓

acceso

Por eso el SOC debe buscar información adicional:

IP origen

Equipo origen

Usuario

Horario

Actividad posterior

**7. ✅ C — Investigar el contexto**

Tenemos:

WINWORD.EXE

↓

POWERSHELL.EXE

↓

factura.ps1

Esto es interesante.

Pero no podemos afirmar automáticamente:

"Es malware."

El analista debería investigar:

Documento

↓

Script

↓

Command Line

↓

Usuario

↓

Procesos posteriores

↓

Conexiones de red

Esta es una de las diferencias entre un analista que **detecta indicadores** y uno que realmente **investiga incidentes**.

**8. ✅ B — El contexto determina la importancia**

Un evento aislado puede ser perfectamente normal.

Por ejemplo:

4624

puede ocurrir miles de veces en una organización.

Pero imaginá:

4625

4625

4625

4624

4688 PowerShell

Conexión externa

Ahora tenemos una historia potencial.

Por eso:

**El SOC no busca solamente eventos. Busca relaciones entre eventos.**

**9. ✅ C — Correlacionar los eventos**

Tenemos:

4625

↓

4625

↓

4625

↓

4624

↓

4688 PowerShell

↓

Conexión externa

↓

Nuevo servicio

Lo correcto es construir una línea temporal.

Por ejemplo:

22:01 → Intento fallido

22:02 → Intento fallido

22:03 → Intento fallido

22:04 → Login exitoso

22:05 → PowerShell

22:06 → Conexión externa

22:08 → Nuevo servicio

Ahora podemos investigar una posible cadena de:

AUTENTICACIÓN

↓

ACCESO

↓

EJECUCIÓN

↓

COMUNICACIÓN

↓

PERSISTENCIA

**10. ✅ C — Secuencia potencialmente sospechosa**

Esta es la pregunta más importante.

Tenemos:

4624

↓

4688 PowerShell

↓

4688 CMD

↓

Conexión externa

↓

Nuevo servicio

↓

SYSTEM

Esto combina varios elementos:

**🔐 Autenticación**

4624

**⚙️ Ejecución**

4688

PowerShell

CMD

**🌐 Comunicación**

IP externa

**📌 Persistencia potencial**

Nuevo servicio

**👑 Privilegios elevados**

SYSTEM

Esto **no demuestra por sí solo que haya un ataque**, pero sí constituye una cadena que un analista SOC debería investigar inmediatamente.

**🏆 RESULTADO**

| **Correctas** | **Evaluación**                   |
|---------------|----------------------------------|
| **10/10**     | 🟢 Excelente — dominio muy bueno |
| **8–9/10**    | 🟢 Muy buen nivel                |
| **6–7/10**    | 🟡 Buen progreso                 |
| **4–5/10**    | 🟠 Conviene repasar              |
| **0–3/10**    | 🔴 Volver a estudiar el módulo   |

**🧠 DESAFÍO SOC — SIN NOTA**

Ahora quiero que pienses como analista.

El SIEM genera esta secuencia:

PC-RRHH-03

Usuario: Maria

02:14 → 4625

02:14 → 4625

02:15 → 4624

02:16 → 4688

WINWORD.EXE

02:16 → 4688

POWERSHELL.EXE

02:17 → 4688

CMD.EXE

02:18 → conexión TCP/443

IP externa

02:20 → nuevo servicio

Servicio ejecutándose como SYSTEM

No quiero que pienses inmediatamente:

❌ "Es malware."

Quiero que pienses:

✅ **"Tengo una secuencia de eventos que podría representar un incidente y necesito reconstruir qué ocurrió."**

Y empezás a preguntar:

¿Desde qué IP ocurrió el 4625?

↓

¿Desde qué IP ocurrió el 4624?

↓

¿Quién abrió Word?

↓

¿Qué documento abrió?

↓

¿Qué comando ejecutó PowerShell?

↓

¿Qué hizo CMD?

↓

¿Qué archivo se ejecutó?

↓

¿A qué IP se conectó?

↓

¿Quién creó el servicio?

↓

¿Qué archivo ejecuta?

↓

¿Hay otros equipos afectados?

**Esta es exactamente la mentalidad que quiero que desarrolles para tu objetivo de entrar a un SOC.**

---

## Parte C — Profundización: 4624, 4625 y 4688

**🎯 Objetivo**

Al terminar esta parte quiero que puedas mirar algo como:

4625

4625

4625

4624

4688 → powershell.exe

4688 → cmd.exe

Conexión externa

y no pensar simplemente:

"Son números de eventos."

Quiero que pienses:

**"Necesito reconstruir qué usuario entró, desde dónde, cómo consiguió acceso, qué ejecutó y qué hizo después."**

Eso es mentalidad SOC.

**1. Antes de empezar: ¿qué es realmente un Event ID?**

Un evento de Windows tiene información.

Podemos imaginarlo así:

┌──────────────────────────────────┐

│ WINDOWS EVENT │

├──────────────────────────────────┤

│ Event ID │

│ Fecha / Hora │

│ Usuario │

│ Equipo │

│ IP / origen │

│ Tipo de actividad │

│ Información adicional │

└──────────────────────────────────┘

El **Event ID** nos dice qué tipo de evento ocurrió.

Pero el ID solo es una parte de la información.

Por eso:

4624

no es suficiente.

Necesitamos saber:

4624

\+

usuario

\+

hora

\+

origen

\+

equipo

\+

tipo de inicio de sesión

**🔐 2. EVENT ID 4624 — LOGON EXITOSO**

**¿Qué significa?**

El **4624** indica que se produjo un:

**Successful Logon**

Es decir:

Alguien / algo

↓

intentó autenticarse

↓

autenticación exitosa

↓

4624

**3. ¿Por qué es importante?**

Porque en una investigación necesitamos responder:

**¿Quién obtuvo acceso?**

Pero también:

**¿Desde dónde?**

Y:

**¿Cómo?**

Y:

**¿Qué hizo después?**

Por ejemplo:

4624

Usuario: administrador

Hora: 03:14

Origen: 10.10.20.55

Ya tenemos una pieza.

Pero todavía no sabemos si es malicioso.

**4. El campo Logon Type ⭐⭐⭐⭐⭐**

Este es uno de los conceptos que realmente vale la pena aprender.

El 4624 puede indicar diferentes tipos de inicio de sesión.

Algunos importantes:

| **Logon Type** | **Significado general** |
|----------------|-------------------------|
| **2**          | Interactive             |
| **3**          | Network                 |
| **4**          | Batch                   |
| **5**          | Service                 |
| **7**          | Unlock                  |
| **8**          | NetworkCleartext        |
| **9**          | NewCredentials          |
| **10**         | RemoteInteractive       |
| **11**         | CachedInteractive       |

No hace falta memorizar todos ahora.

Quiero que recuerdes especialmente:

**Type 2**

Inicio de sesión interactivo.

Por ejemplo:

Usuario sentado frente al equipo

↓

introduce credenciales

↓

entra a Windows

**Type 3**

Inicio de sesión relacionado con acceso a través de la red.

Por ejemplo:

PC-A

↓

acceso a recurso de

PC-B

**Type 5**

Relacionado con servicios.

**Type 10 ⭐**

Muy importante para SOC.

Está relacionado con:

**Remote Interactive Logon**

Por ejemplo:

RDP

Conceptualmente:

Atacante / administrador

↓

RDP

↓

Windows

↓

4624 Type 10

**5. Ejemplo de investigación**

Encontramos:

Event ID: 4624

User:

Administrator

Logon Type:

10

Source IP:

185.x.x.x

Time:

03:27

Esto inmediatamente merece nuestra atención.

¿Por qué?

Porque tenemos:

Administrator

\+

RDP

\+

IP externa

\+

03:27

¿Significa automáticamente ataque?

**No.**

Podría ser:

- administrador trabajando remotamente,

- VPN,

- proveedor autorizado,

- mantenimiento.

Pero claramente debemos investigar.

**6. ¿Qué mirar en un 4624?**

Cuando veas uno, empezá a buscar:

┌─────────────────────────┐

│ EVENT 4624 │

├─────────────────────────┤

│ Usuario │

│ Cuenta │

│ Logon Type │

│ Hora │

│ Equipo │

│ IP origen │

│ Puerto origen │

│ Autenticación │

│ <a href="../../GLOSARIO.md#sid" target="_blank">SID</a> │

└─────────────────────────┘

No todos los campos tienen la misma importancia en todas las investigaciones.

**7. Un concepto importante: Source Network Address**

En determinados eventos podemos encontrar información del origen de la conexión.

Por ejemplo:

Source Network Address:

192.168.10.25

Esto permite preguntarnos:

¿Desde qué máquina se produjo el acceso?

Y podemos construir:

PC-CLIENTE

↓

192.168.10.25

↓

SERVIDOR

↓

4624

Esto conecta Windows directamente con **Redes**.

**8. 4624 + Redes**

Acá quiero que empieces a integrar todo.

Ya estudiaste:

- IP pública.

- IP privada.

- <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

- <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

- TCP.

- UDP.

- Puertos.

- DNS.

Ahora eso aparece dentro de una investigación Windows.

Por ejemplo:

4624

Usuario: admin

Logon Type: 10

Source IP: 192.168.1.50

Ahora podés preguntarte:

¿Qué equipo tiene 192.168.1.50?

↓

¿Es un equipo autorizado?

↓

¿Desde dónde obtuvo esa IP?

↓

¿Después realizó conexiones?

**🚨 9. EVENT ID 4625 — LOGON FALLIDO**

Ahora el hermano del 4624.

**4625**

Significa:

**Failed Logon**

Conceptualmente:

Intento de autenticación

↓

❌

4625

**10. Un solo 4625**

Supongamos:

08:32

4625

Usuario: Juan

¿Ataque?

No necesariamente.

Puede ser:

Juan escribió mal su contraseña.

Por eso un SOC profesional no genera una conclusión basada en un único evento.

**11. Muchos 4625**

Ahora:

02:10 → 4625

02:10 → 4625

02:11 → 4625

02:11 → 4625

02:11 → 4625

02:12 → 4625

Desde:

IP: 10.20.30.50

Esto es mucho más interesante.

Podríamos estar frente a:

**Brute Force**

**12. Brute Force**

El atacante intenta muchas contraseñas contra una cuenta.

Conceptualmente:

admin

↓

password1 ❌

password2 ❌

password3 ❌

password4 ❌

password5 ❌

Y Windows registra:

4625

4625

4625

4625

4625

**13. Password Spraying**

Hay otra técnica que quiero que conozcas.

En lugar de atacar muchas contraseñas contra una sola cuenta:

admin

↓

muchas contraseñas

el atacante puede utilizar:

contraseña común

↓

Usuario A ❌

Usuario B ❌

Usuario C ❌

Usuario D ❌

Esto puede producir:

Usuario A → 4625

Usuario B → 4625

Usuario C → 4625

Usuario D → 4625

Por eso mirar solamente una cuenta no siempre alcanza.

**14. La combinación más interesante**

Ahora aparece algo muy importante:

4625

4625

4625

4625

↓

4624

Tenemos:

FALLOS

↓

FALLOS

↓

FALLOS

↓

ÉXITO

Esto es **muy interesante para investigar**.

No significa automáticamente compromiso.

Pero la pregunta cambia:

**¿Qué ocurrió después del 4624?**

**⚙️ 15. EVENT ID 4688 — PROCESS CREATION**

Ahora llegamos a uno de los eventos más útiles para investigación de endpoints.

**4688**

Indica:

**Creación de un proceso.**

Por ejemplo:

4688

New Process:

powershell.exe

Esto conecta directamente con lo que estudiamos antes.

**16. ¿Por qué 4688 es tan importante?**

Porque nos permite observar actividad del sistema.

Por ejemplo:

Usuario

↓

Proceso padre

↓

Nuevo proceso

Supongamos:

4688

Parent:

explorer.exe

New Process:

powershell.exe

Tenemos:

explorer.exe

↓

powershell.exe

**17. Process Tree**

Esto se vuelve extremadamente poderoso cuando tenemos varios eventos.

Por ejemplo:

WINWORD.EXE

│

└── POWERSHELL.EXE

│

└── CMD.EXE

│

└── UPDATE.EXE

Cada creación puede aparecer asociada a eventos de proceso.

Ahora podemos reconstruir:

**Qué proceso lanzó a qué proceso.**

**18. Parent Process**

En una investigación SOC, preguntá siempre:

**¿Quién creó este proceso?**

Porque:

explorer.exe

↓

notepad.exe

puede ser perfectamente normal.

Mientras:

WINWORD.EXE

↓

powershell.exe

puede ser mucho más interesante.

Y:

OUTLOOK.EXE

↓

powershell.exe

↓

cmd.exe

puede requerir todavía más investigación.

**19. Command Line ⭐⭐⭐⭐⭐**

Esta parte es fundamental.

No es suficiente saber:

4688

powershell.exe

Queremos saber:

**¿Cómo fue ejecutado?**

Por ejemplo:

powershell.exe -File C:\Temp\script.ps1

es mucho más informativo.

Podemos investigar:

¿Existe script.ps1?

¿Quién lo creó?

¿Qué contiene?

¿Cuándo apareció?

¿Qué hace?

¿Se conecta a Internet?

**20. Ruta del proceso**

También es importante.

Por ejemplo:

C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

es una ruta esperable.

Pero imaginá:

C:\Users\Juan\AppData\Temp\powershell.exe

El nombre puede ser igual.

Pero la ruta cambia completamente el contexto.

Esto nos lleva a una regla:

**No analices solamente el nombre del proceso. Analizá también su ruta.**

**21. Nombre legítimo ≠ proceso legítimo**

Esto es extremadamente importante.

Un atacante puede intentar utilizar nombres conocidos.

Por ejemplo:

svchost.exe

explorer.exe

powershell.exe

update.exe

Podría intentar colocar un archivo malicioso con un nombre parecido o igual.

Por eso investigamos:

Nombre

\+

Ruta

\+

Firma

\+

Hash

\+

Parent

\+

Command Line

\+

Usuario

\+

Red

**22. 4688 + PowerShell**

Ahora un caso:

4688

User:

Juan

Parent:

WINWORD.EXE

Process:

POWERSHELL.EXE

Command Line:

powershell.exe -File C:\Users\Juan\Downloads\factura.ps1

Yo marcaría esto como:

🟠 **Actividad que requiere investigación**

No diría todavía:

🔴 **Malware confirmado**

**23. ¿Qué buscaría después?**

**Paso 1**

Investigar el documento:

factura.docx

**Paso 2**

Investigar el script:

factura.ps1

**Paso 3**

Investigar el proceso:

powershell.exe

**Paso 4**

Buscar conexiones:

IP

Puerto

Dominio

DNS

**Paso 5**

Buscar procesos hijos.

**Paso 6**

Buscar persistencia.

**🔥 24. Ahora combinemos los tres eventos**

Este es el verdadero objetivo.

Tenemos:

4625

4625

4625

↓

4624

↓

4688

↓

powershell.exe

Esto puede representar:

Intentos de acceso

↓

Acceso conseguido

↓

Ejecución

Ahora preguntamos:

¿Quién?

¿Desde dónde?

¿Con qué cuenta?

¿Qué ejecutó?

¿Con qué privilegios?

**25. Agregamos red**

Supongamos:

4625 × 5

↓

4624

↓

4688 powershell.exe

↓

TCP/443

↓

IP externa

Ahora:

AUTENTICACIÓN

↓

EJECUCIÓN

↓

RED

Esto es mucho más interesante.

**26. Agregamos persistencia**

Y encontramos:

4625

4625

4624

4688 powershell.exe

Conexión externa

Nuevo servicio

Ahora podemos sospechar de una cadena:

ACCESO

↓

EJECUCIÓN

↓

COMUNICACIÓN

↓

PERSISTENCIA

Esto es una investigación realista de SOC.

**27. La línea temporal**

Una de las habilidades que quiero que desarrolles es construir timelines.

Por ejemplo:

02:13:21

4625

Login fallido

02:13:24

4625

Login fallido

02:13:27

4624

Login exitoso

02:14:03

4688

powershell.exe

02:14:10

4688

cmd.exe

02:14:18

Conexión TCP/443

02:15:03

Nuevo servicio

Ahora tenemos una película.

Antes teníamos solamente fotografías.

**28. ¿Qué diferencia hay?**

**Evento aislado:**

4688 powershell.exe

Puede ser:

🟢 normal.

**Secuencia:**

4625

4625

4624

4688 powershell

4688 cmd

conexión externa

servicio nuevo

Puede ser:

🔴 **altamente sospechosa**

La diferencia es:

**CONTEXTO**

**29. Falsos positivos**

Quiero que aprendas esto desde ahora.

Un buen analista no busca solamente ataques.

También debe evitar falsas alarmas.

Por ejemplo:

4625

puede ser:

usuario se equivocó

Y:

4688 powershell.exe

puede ser:

administrador ejecutando un script legítimo

Por eso debemos preguntar:

¿Es habitual?

¿Quién lo hizo?

¿Está autorizado?

¿Coincide con la actividad esperada?

**30. <a href="../../GLOSARIO.md#baseline" target="_blank">Baseline</a>**

Esto nos lleva a otro concepto:

**Baseline**

Es conocer qué comportamiento es normal dentro de un entorno.

Por ejemplo:

Administrador de TI

→ PowerShell diariamente

puede ser normal.

Mientras:

Usuario de contabilidad

→ PowerShell

→ 03:00 AM

→ conexión externa

puede ser anómalo.

La misma actividad puede tener diferente riesgo dependiendo del contexto.

**31. Un caso para que pienses como L1**

Tenemos:

Equipo:

SRV-FILES-01

Usuario:

Administrator

02:31

4625

Source IP: 10.10.20.15

02:31

4625

Source IP: 10.10.20.15

02:32

4624

Logon Type: 10

Source IP: 10.10.20.15

02:33

4688

powershell.exe

02:33

Command Line:

powershell.exe -File C:\Temp\backup.ps1

¿Es necesariamente ataque?

No.

Tenemos una hipótesis:

Puede ser un administrador realizando mantenimiento remoto.

Pero tenemos que investigar:

¿10.10.20.15 pertenece a TI?

¿Administrator debía conectarse?

¿backup.ps1 es legítimo?

¿Existe una tarea de mantenimiento?

¿El horario es normal?

¿Hubo conexiones posteriores?

**32. Ahora un caso más sospechoso**

PC-VENTAS-03

02:11

4625

Source: Internet

02:11

4625

Source: Internet

02:12

4625

Source: Internet

02:12

4624

Logon Type: 10

02:13

4688

powershell.exe

02:13

4688

cmd.exe

02:14

Conexión externa

02:15

Nuevo servicio

Acá el nivel de sospecha sube muchísimo.

Tenemos:

Internet

↓

Fallos

↓

Éxito

↓

RDP

↓

PowerShell

↓

CMD

↓

Red

↓

Persistencia

Esto ya requiere una investigación seria.

**33. ¿Qué haría un SOC L1?**

No necesariamente empieza eliminando cosas.

Primero:

**1. Validar la alerta**

¿Es real?

**2. Identificar el equipo**

¿Quién es el propietario?

¿Qué función cumple?

**3. Identificar al usuario**

¿Es legítimo?

**4. Investigar origen**

¿De qué IP vino?

**5. Reconstruir procesos**

¿Quién lanzó PowerShell?

**6. Investigar red**

¿A dónde se conectó?

**7. Buscar persistencia**

¿Se creó servicio?

¿Tarea programada?

¿Run Key?

**8. Determinar severidad**

Low

Medium

High

Critical

Y según el procedimiento:

Escalar

Contener

Cerrar

**🧠 34. Lo que quiero que realmente aprendas**

No quiero que tu conocimiento sea:

4624 = login

4625 = failed login

4688 = process

Eso es solamente el nivel inicial.

Quiero que llegues a:

4624

↓

¿Quién?

↓

¿Desde dónde?

↓

¿Qué Logon Type?

↓

¿Qué hizo después?

↓

4688

↓

¿Qué proceso?

↓

¿Quién lo creó?

↓

¿Qué Command Line?

↓

¿Con qué privilegios?

↓

¿Se conectó a Internet?

↓

¿Hubo persistencia?

**Eso ya es pensamiento de analista SOC.**

**🎯 35. Los tres eventos como mapa mental**

Guardá esto:

AUTENTICACIÓN

│

┌───────┴───────┐

↓ ↓

4624 4625

Login OK Login FAIL

│ │

└───────┬───────┘

↓

¿Quién accedió?

│

↓

4688

│

Proceso creado

│

┌────────────┼────────────┐

↓ ↓ ↓

Padre Command Usuario

Process Line

│ │

└────────────┼────────────┘

↓

¿Qué hizo?

↓

RED / SERVICIOS

↓

SIEM

↓

SOC

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
