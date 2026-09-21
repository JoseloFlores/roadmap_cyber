**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 25: <a href="../../GLOSARIO.md#cmd" target="_blank">CMD</a> y <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a>**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Línea de comandos + Detección SOC

Este módulo unifica la referencia rápida (comandos clave, cmdlets, LOLBins, `-enc`) con la guía larga (CMD comando por comando, objetos PowerShell, `CommandLine`, ofuscación, logging, correlación con procesos/servicios).

**🎯 Objetivos del módulo**

-   Diferenciar `cmd.exe` de `powershell.exe`.
-   Usar comandos clave de reconocimiento y red (`whoami`, `ipconfig`, `ping`, `tracert`, `netstat -ano`, `tasklist`, `sc`).
-   Entender por qué **PowerShell es legítimo y peligroso a la vez** (objetos, `|`, `IEX`, `-EncodedCommand`).
-   Detectar comandos sospechosos, ofuscación y LOLBins, y correlacionar con proceso padre, red y servicios.


---

## Parte A — Referencia rápida SOC

**1. CMD (Símbolo del sistema)**

`cmd.exe` es el intérprete clásico. Comandos esenciales:

```cmd
ipconfig            # configuración de red
ipconfig /all       # incluye MAC y DNS
ipconfig /flushdns  # limpia caché DNS
ping 8.8.8.8        # conectividad básica
tracert google.com  # ruta hasta el destino
netstat -ano        # conexiones y puertos (a=all, n=numérico, o=PID)
systeminfo          # resumen del sistema
whoami              # usuario actual y privilegios
net user            # usuarios locales
net localgroup      # grupos locales
```

`netstat -ano` es clave: muestra <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, puerto y **<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>**, permitiendo
cruzar con `tasklist` para saber qué proceso abrió la conexión.

**2. PowerShell**

`powershell.exe` es mucho más potente: accede a .NET, WMI y la API de
Windows. Cmdlets comunes:

```powershell
Get-Process
Get-Service
Get-EventLog -LogName Security
Get-WinEvent -LogName System
Get-ChildItem C:\Users
Get-NetTCPConnection        # alternativa moderna a netstat
Get-CimInstance Win32_Process | Select Name, ParentProcessId, CommandLine
```

Obtener la **línea de comandos completa** de un proceso es vital en
investigación, porque revela qué argumentos usó (por ejemplo, una
descarga oculta).

**3. ¿Por qué PowerShell asusta a los defensores?**

PowerShell puede:

-   Descargar y ejecutar código desde internet.
-   Codificar comandos en Base64 para ocultarlos.
-   Usar `Invoke-WebRequest` o `IEX` para traer scripts.

Ejemplo sospechoso (no lo ejecutes):

```powershell
powershell -enc <cadena_base64>
```

`--enc` (`-EncodedCommand`) oculta la intención real. Un SOC debe
revisar **qué comando decodificado** se ejecutó.

**4. LOLBins**

Algunas herramientas legítimas de Windows pueden ser abusadas:

-   `certutil`: puede descargar archivos.
-   `bitsadmin`: transferencia en segundo plano.
-   `powershell` / `cmd`: ejecución.
-   `wmic`: consultas y ejecución remota.

No son malware, pero un analista las mira con sospecha cuando aparecen
en una cadena de ataque.

**5. Detección de comandos sospechosos**

Señales en un evento de PowerShell:

-   Parámetro `-enc` o `-EncodedCommand`.
-   `IEX (New-Object Net.WebClient)...` (descarga y ejecuta).
-   Nombres ofuscados o sin espacios (`Inv0ke-WebRequest`).
-   Ejecución desde `C:\Users\...\AppData` o `%TEMP%`.

**6. Conexión con el SOC**

Un evento de PowerShell (<a href="../../GLOSARIO.md#event-id" target="_blank">Event ID</a> 4104 en el log de PowerShell, cuando
el logging está habilitado) puede mostrar el script exacto ejecutado.
Combinado con `netstat` y el proceso padre, reconstruyes la historia.

**🧪 Laboratorio recomendado**

1.  Abre CMD y ejecuta `ipconfig /all`, `systeminfo`, `whoami`.
2.  Ejecuta `netstat -ano` y anota una conexión ESTABLISHED con su PID.
3.  Abre PowerShell y ejecuta `Get-NetTCPConnection`.
4.  Ejecuta `Get-Process | Select-Object Name, Id, Path` y observa
    rutas.
5.  (Sin ejecutar) Analiza mentalmente por qué `powershell -enc ...`
    merece investigación.

**📝 Evaluación — Módulo 25: CMD y PowerShell**

**🔹 Pregunta 1**

¿Qué combinación de `netstat` muestra conexiones, puertos numéricos y
PID?

**A)** `netstat -e`\
**B)** `netstat -ano`\
**C)** `netstat /?`\
**D)** `netstat -r`

**🔹 Pregunta 2**

Para ver la línea de comandos completa de un proceso en PowerShell
usamos:

**A)** `Get-Service`\
**B)** `Get-CimInstance Win32_Process | Select CommandLine`\
**C)** `ipconfig`\
**D)** `ping`

**🔹 Pregunta 3**

`powershell -enc <base64>` es peligroso porque:

**A)** Actualiza Windows.\
**B)** Oculta el comando real mediante codificación.\
**C)** Solo sirve para imprimir.\
**D)** Es un firewall.

**🔹 Pregunta 4**

`certutil` es considerado <a href="../../GLOSARIO.md#lolbin" target="_blank">LOLBin</a> porque puede:

**A)** Apagar el equipo.\
**B)** Descargar archivos desde la red.\
**C)** Crear usuarios.\
**D)** Cifrar discos.

**🔹 Pregunta 5**

El cmdlet para listar eventos del log de Seguridad es:

**A)** `Get-EventLog -LogName Security`\
**B)** `Get-Service`\
**C)** `Test-NetConnection`\
**D)** `Set-ExecutionPolicy`

**🔹 Pregunta 6**

`whoami` nos indica:

**A)** La IP pública.\
**B)** El usuario actual y sus privilegios.\
**C)** El sistema de archivos.\
**D)** El registro de Windows.

**🔹 Pregunta 7**

¿Por qué un analista desconfía de PowerShell lanzado desde `%TEMP%`?

**A)** Porque PowerShell nunca debe usarse.\
**B)** Porque es una ubicación típica de ejecución de malware.\
**C)** Porque requiere administrador siempre.\
**D)** Porque borra logs.

**🔹 Pregunta 8**

`Get-NetTCPConnection` es útil para:

**A)** Listar conexiones de red activas.\
**B)** Crear usuarios.\
**C)** Formatear discos.\
**D)** Editar el registro.

**🔹 Pregunta 9 — Caso SOC**

Se observa: `cmd.exe` → `powershell.exe -enc <cadena>`. El SOC debe:

**A)** Ignorarlo, PowerShell es legítimo.\
**B)** Decodificar el comando y analizarlo junto con red y proceso
padre.\
**C)** Reiniciar el equipo de inmediato.\
**D)** Desactivar la red doméstica.

**🔹 Pregunta 10**

Un LOLBin es:

**A)** Un binario legítimo de Windows abusado con fines maliciosos.\
**B)** Un controlador de impresora.\
**C)** Un tipo de firewall.\
**D)** Un virus conocido.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B — `netstat -ano`**: all, numérico, PID.
2. **B**: `CommandLine` revela argumentos.
3. **B**: `-enc` oculta la intención.
4. **B**: puede descargar archivos.
5. **A**: `Get-EventLog -LogName Security`.
6. **B**: usuario y privilegios.
7. **B**: `%TEMP%` es ubicación típica de malware.
8. **A**: lista conexiones.
9. **B**: decodificar y correlacionar.
10. **A**: binario legítimo abusado.



---

## Parte B — Guía completa CMD + PowerShell

Vamos a mantener exactamente la metodología que venimos usando: **primero entender el concepto**, después relacionarlo con **ciberseguridad y SOC**, y finalmente hacer un examen.

Hasta ahora:

Windows

↓

NTFS

↓

Usuarios y grupos

↓

Autenticación

↓

<a href="../../GLOSARIO.md#active-directory" target="_blank">Active Directory</a> + <a href="../../GLOSARIO.md#kerberos" target="_blank">Kerberos</a>

↓

Procesos y servicios

↓

CMD + PowerShell ← ESTAMOS ACÁ

Este tema es **muy importante para SOC**, porque muchas investigaciones de Windows terminan necesitando interpretar comandos ejecutados en el equipo.

**1. ¿Qué es CMD?**

CMD significa:

**Command Prompt**

Es la consola de comandos tradicional de Windows.

Permite interactuar con el sistema mediante comandos de texto.

En lugar de hacer:

Abrir carpeta

→ buscar archivo

→ hacer clic

→ propiedades

podemos utilizar comandos.

Por ejemplo:

dir

para listar archivos y carpetas.

**2. ¿Por qué debería importarle CMD a un SOC?**

Porque un atacante puede utilizarlo para ejecutar comandos.

Por ejemplo, conceptualmente:

Atacante

↓

obtiene acceso

↓

abre CMD

↓

ejecuta comandos

↓

reconoce el sistema

Puede intentar averiguar:

- usuario actual,

- equipo,

- configuración de red,

- procesos,

- servicios,

- archivos,

- conexiones,

- otros equipos.

Por eso un SOC puede encontrar eventos relacionados con:

cmd.exe

**3. Comandos básicos de CMD**

Vamos a conocer algunos.

**whoami**

Muestra el usuario con el que se está ejecutando la sesión.

whoami

Podríamos obtener:

empresa\juan

Esto es importantísimo para seguridad porque nos dice:

**¿Con qué identidad se está ejecutando este comando?**

**4. hostname**

Muestra el nombre del equipo.

hostname

Ejemplo:

PC-CONTABILIDAD-01

Un atacante podría utilizarlo durante una fase de reconocimiento.

**5. ipconfig**

Muestra información de configuración de red.

ipconfig

Por ejemplo:

IPv4 Address: 192.168.1.25

Default <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>: 192.168.1.1

Recordá lo que aprendimos en Redes:

IP

↓

Máscara

↓

Gateway

↓

Red

Ahora estamos viendo cómo obtener esa información desde Windows.

**6. ipconfig /all**

Para obtener información más completa:

ipconfig /all

Puede mostrar:

- dirección IP,

- máscara,

- gateway,

- <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>,

- <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>,

- <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>,

- adaptadores de red.

Para un analista SOC puede ser útil durante una investigación.

**7. ping**

Permite comprobar conectividad mediante <a href="../../GLOSARIO.md#icmp" target="_blank">ICMP</a>.

Por ejemplo:

ping 192.168.1.1

Podemos utilizarlo para comprobar:

PC

↓

Gateway

↓

¿Responde?

Pero recordá:

Que un host no responda a ping no significa necesariamente que esté apagado.

Puede existir un firewall bloqueando ICMP.

**8. tracert**

Permite observar el camino hacia un destino.

tracert 8.8.8.8

Conceptualmente:

PC

↓

Router

↓

Router

↓

Router

↓

Destino

Esto puede ayudar a comprender problemas de conectividad.

**9. netstat**

Este es especialmente interesante para SOC.

netstat

Puede mostrar conexiones de red.

Una opción útil:

netstat -ano

Permite relacionar:

IP

\+

Puerto

\+

Estado

\+

PID

Por ejemplo:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

192.168.1.25:49152

→

203.0.113.50:443

PID 4520

Entonces podemos preguntar:

¿Qué proceso es el PID 4520?

Y relacionarlo con procesos.

Esto es **muy importante**.

**10. La conexión entre netstat y procesos**

Imaginemos:

netstat -ano

PID 4520

Luego investigamos:

Proceso

PID 4520

↓

powershell.exe

Ahora tenemos:

powershell.exe

↓

conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

↓

IP externa

Ya tenemos una pieza mucho más interesante para una investigación SOC.

**11. tasklist**

Permite listar procesos.

tasklist

Ejemplo:

Image Name PID

--------------------

explorer.exe 3520

powershell.exe 4520

chrome.exe 7812

Ahora podemos combinar:

tasklist

\+

netstat -ano

y relacionar procesos con conexiones.

**12. taskkill**

Permite finalizar procesos.

Por ejemplo:

taskkill /PID 4520

⚠️ **Importante para tu formación SOC:** conocer este comando no significa que debamos utilizarlo automáticamente frente a una alerta.

En una empresa real, el SOC normalmente debe seguir procedimientos establecidos.

Podríamos necesitar:

Alerta

↓

Validación

↓

Investigación

↓

Contención autorizada

No simplemente:

Alerta

↓

Matar proceso

**13. dir**

Lista archivos y carpetas:

dir

Ejemplo:

C:\Users\Juan\> dir

Podemos investigar:

¿Qué archivos existen?

¿Qué carpetas existen?

¿Cuándo fueron modificados?

**14. cd**

Permite cambiar de directorio.

cd C:\Windows

También:

cd ..

para subir un nivel.

Esto parece básico, pero necesitamos dominarlo antes de pasar a PowerShell.

**15. type**

Puede mostrar el contenido de un archivo de texto:

type archivo.txt

En una investigación puede servir para inspeccionar archivos de texto simples.

**16. findstr**

Permite buscar texto.

Por ejemplo:

findstr "error" archivo.log

Esto puede ser útil para buscar determinados patrones dentro de archivos de texto.

**17. Ahora aparece PowerShell**

PowerShell es mucho más que un CMD moderno.

Es:

**Una <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> y plataforma de automatización/administración de Windows.**

Tiene acceso a objetos y a muchas funciones del sistema.

Esto hace que sea extremadamente potente.

**18. CMD vs PowerShell**

La diferencia conceptual:

| **CMD**                                   | **PowerShell**                  |
|-------------------------------------------|---------------------------------|
| Consola tradicional                       | Shell moderna de Windows        |
| Comandos clásicos                         | Cmdlets                         |
| Trabaja principalmente con texto          | Trabaja con objetos             |
| Menos potente para automatización moderna | Muy potente para administración |
| Muy utilizada históricamente              | Muy utilizada actualmente       |

Pero atención:

**PowerShell es una herramienta legítima.**

No debemos asociar:

PowerShell = malware

**19. ¿Por qué PowerShell es importante para un SOC?**

Porque tiene acceso a muchas capacidades del sistema.

Puede interactuar con:

- procesos,

- servicios,

- archivos,

- usuarios,

- red,

- registro,

- administración,

- Active Directory,

- APIs,

- otros componentes.

Por eso un atacante puede abusar de ella.

**20. Cmdlets**

PowerShell utiliza comandos llamados:

**Cmdlets**

Normalmente tienen una estructura:

Verbo-Sustantivo

Por ejemplo:

Get-Process

Get-Service

Get-ComputerInfo

Esto es mucho más fácil de recordar que memorizar cientos de comandos.

**21. Get-Process**

Para consultar procesos:

Get-Process

Podemos obtener información como:

Name

Id

CPU

Memory

Es similar conceptualmente a:

tasklist

Pero PowerShell trabaja con objetos.

**22. Get-Service**

Para consultar servicios:

Get-Service

Podemos observar:

Status

Name

DisplayName

Por ejemplo:

Running

Stopped

Esto conecta directamente con lo que acabamos de estudiar.

**23. Get-NetTCPConnection**

PowerShell también puede consultar conexiones TCP.

Conceptualmente:

Get-NetTCPConnection

Esto puede permitir investigar conexiones activas.

Y nuevamente podemos relacionarlo con procesos.

**24. El gran poder de PowerShell: objetos**

En CMD normalmente pensamos:

comando

↓

texto

En PowerShell:

comando

↓

OBJETOS

↓

propiedades

↓

filtrado

↓

automatización

Esto es una diferencia fundamental.

**25. Ejemplo conceptual**

Supongamos:

Get-Process

Devuelve procesos.

Podemos filtrar:

Get-Process \| Where-Object {\$\_.CPU -gt 100}

La idea es:

Get-Process

↓

procesos

↓

Where-Object

↓

filtrar

↓

CPU \> 100

No hace falta que memorices todavía la sintaxis.

Lo importante es comprender el concepto.

**26. El operador \|**

Este símbolo:

\|

se llama:

**<a href="../../GLOSARIO.md#pipe" target="_blank">Pipe</a>**

Y es uno de los conceptos más importantes de PowerShell.

Permite pasar la salida de un comando al siguiente.

Por ejemplo:

Get-Process \| Where-Object ...

Podemos imaginar:

Get-Process

↓

salida

↓

\|

↓

Where-Object

↓

filtrado

**27. ¿Por qué esto es importante para un SOC?**

Porque permite investigar rápidamente.

Por ejemplo:

Todos los procesos

↓

filtrar procesos

↓

buscar uno concreto

↓

obtener información

En lugar de revisar manualmente cientos de procesos.

**28. PowerShell y reconocimiento**

Imaginemos que un atacante consigue acceso a una máquina.

Puede intentar obtener información sobre:

Usuario

Equipo

Red

Procesos

Servicios

Sistema

Conceptualmente:

whoami

hostname

ipconfig

Get-Process

Get-Service

Esto es:

**Reconocimiento local**

El atacante intenta comprender dónde está.

**29. PowerShell y ejecución**

PowerShell también permite ejecutar comandos y scripts.

Por eso aparece frecuentemente en investigaciones de incidentes.

Una alerta puede indicar:

powershell.exe

Pero nuevamente:

El hecho de que PowerShell se ejecute no demuestra un ataque.

Debemos analizar:

Usuario

\+

Parent Process

\+

<a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a>

\+

Script

\+

Destino de red

\+

Archivos

**30. Command Line — MUY IMPORTANTE**

En SOC vas a escuchar mucho:

**Command Line**

Es la línea de comandos utilizada para iniciar un proceso.

Por ejemplo:

powershell.exe -File script.ps1

No es lo mismo investigar:

powershell.exe

que:

powershell.exe -File C:\Users\Juan\Downloads\script.ps1

La segunda información nos da mucho más contexto.

**31. Un ejemplo de alerta**

Imaginemos que el <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> muestra:

Process:

powershell.exe

User:

Juan

Parent:

WINWORD.EXE

Command Line:

powershell.exe -File C:\Users\Juan\Downloads\factura.ps1

Como analista:

🚨 **Esto merece investigación.**

Preguntas:

¿Juan esperaba ejecutar ese script?

¿De dónde salió factura.ps1?

¿Quién creó el archivo?

¿Qué contiene?

¿Con qué IP se comunicó?

¿Qué procesos creó?

**32. Ofuscación**

Otro concepto importante.

Un atacante puede intentar ocultar lo que está haciendo utilizando comandos difíciles de leer.

Por ejemplo:

Código

↓

codificación

↓

ejecución

En PowerShell puede aparecer actividad codificada u ofuscada.

Esto dificulta la detección.

Por eso el SOC analiza:

- command line,

- scripts,

- logs,

- comportamiento,

- procesos hijos,

- conexiones.

**33. PowerShell Logging**

Windows puede registrar actividad de PowerShell mediante distintos mecanismos de logging.

Algunos importantes que vas a estudiar más adelante:

<a href="../../GLOSARIO.md#script-block-logging" target="_blank">Script Block Logging</a>

PowerShell Operational Logs

Module Logging

Esto es muy importante para un SOC porque permite obtener evidencia sobre qué ocurrió.

Más adelante vamos a entrar profundamente en:

**Windows Event Logs**

y ahí esto va a empezar a tomar forma.

**34. CMD + PowerShell + Procesos**

Ahora juntamos la clase anterior con esta.

Tenemos:

WINWORD.EXE

↓

POWERSHELL.EXE

↓

CMD.EXE

↓

otro.exe

Y además:

otro.exe

↓

conexión externa

El SOC puede reconstruir:

Proceso padre

↓

Proceso hijo

↓

Command Line

↓

Red

↓

Archivo

Esto es muchísimo más poderoso que simplemente mirar "hay PowerShell".

**35. CMD + PowerShell + servicios**

Podríamos encontrar:

powershell.exe

↓

creación/modificación de servicio

↓

servicio ejecuta archivo

↓

persistencia

Entonces tenemos:

Ejecución

↓

Persistencia

Y ahora empieza a conectarse con conceptos de **MITRE ATT&CK** que veremos más adelante.

**36. ¿Cómo se defiende una organización?**

No se trata simplemente de:

"Bloquear CMD y PowerShell."

Porque son herramientas necesarias para administración.

La defensa puede incluir:

**🔐 Control de privilegios**

Aplicar <a href="../../GLOSARIO.md#minimo-privilegio" target="_blank">mínimo privilegio</a>.

**📋 Logging**

Registrar actividad.

**🛡️ EDR**

Detectar comportamientos sospechosos.

**🔎 <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**

Correlacionar eventos.

**📜 Políticas de PowerShell**

Controlar su utilización según el entorno.

**👤 Control de cuentas**

Evitar que usuarios comunes tengan privilegios innecesarios.

**37. Pensamiento SOC**

Quiero que empieces a pensar de esta manera.

Encontramos:

powershell.exe

❌ Pensamiento incorrecto:

"PowerShell = ataque."

❌ También incorrecto:

"PowerShell es de Microsoft, entonces es seguro."

✅ Pensamiento SOC:

"PowerShell es una herramienta legítima. Necesito analizar quién la ejecutó, desde qué proceso, con qué argumentos, qué hizo y qué ocurrió después."

**38. La matriz mental del analista**

Cuando encuentres un proceso o comando sospechoso:

┌─────────────────────────────┐

│ PROCESO │

├─────────────────────────────┤

│ ¿Quién? │

│ ¿Qué proceso? │

│ ¿PID? │

│ ¿Proceso padre? │

│ ¿Command Line? │

│ ¿Ruta? │

│ ¿Privilegios? │

│ ¿Archivos? │

│ ¿Conexiones? │

│ ¿Qué ocurrió después? │

└─────────────────────────────┘

Esta forma de pensar te va a servir muchísimo cuando lleguemos a análisis de alertas reales.

**🧠 39. Lo que quiero que memorices**

No hace falta memorizar 100 comandos.

Por ahora quedate con estos:

**CMD**

whoami

hostname

ipconfig

ipconfig /all

ping

tracert

netstat -ano

tasklist

dir

cd

**PowerShell**

Get-Process

Get-Service

Get-NetTCPConnection

Y estos conceptos:

PID

Process Tree

Parent Process

Child Process

Command Line

Pipe \|

PowerShell

<a href="../../GLOSARIO.md#living-off-the-land" target="_blank">Living off the Land</a>

**🎯 40. Conexión con todo lo aprendido**

Mirá dónde llegamos:

WINDOWS

│

┌───────────────┼────────────────┐

↓ ↓ ↓

USUARIO PROCESOS SERVICIOS

│ │ │

↓ ↓ ↓

AUTENTICACIÓN PID / TREE PERSISTENCIA

│ │

↓ ↓

Kerberos CMD / PS

│ │

└───────┬───────┘

↓

RED

↓

CONEXIONES

↓

SIEM

↓

ANALISTA SOC

Esto es exactamente lo que buscamos: **dejar de estudiar conceptos aislados y empezar a conectarlos como lo haría un analista SOC.**

**🖥️ Semana 4 — Windows**

**📝 Examen B (ampliado) — CMD + PowerShell**

**Nivel:** SOC Nivel 1 → Intermedio  
**Modalidad:** 10 preguntas Multiple Choice

Como venimos trabajando: **primero resolvé las 10 preguntas sin mirar las respuestas**. Después tenés las soluciones y la justificación de cada una.

**🔹 Pregunta 1**

¿Qué comando de CMD permite conocer el usuario con el que se está ejecutando la sesión?

**A)** hostname  
**B)** whoami  
**C)** ipconfig  
**D)** tasklist

**🔹 Pregunta 2**

¿Qué información proporciona principalmente ipconfig /all?

**A)** Procesos y PID.

**B)** Usuarios y grupos de Active Directory.

**C)** Configuración detallada de red, incluyendo IP, máscara, gateway, DNS y DHCP.

**D)** Servicios ejecutándose en Windows.

**🔹 Pregunta 3**

Un analista ejecuta:

netstat -ano

¿Qué combinación de información puede relacionar especialmente con este comando?

**A)** Usuario + contraseña + grupo.

**B)** Conexiones de red + puertos + estado + PID.

**C)** Archivos + permisos NTFS.

**D)** Servicios + <a href="../../GLOSARIO.md#gpo" target="_blank">GPO</a> + usuarios.

**🔹 Pregunta 4**

El SOC encuentra:

PID: 4520

¿Cómo podría determinar qué proceso corresponde a ese PID?

**A)** Utilizando tasklist.

**B)** Utilizando hostname.

**C)** Utilizando ipconfig.

**D)** Utilizando cd.

**🔹 Pregunta 5**

¿Cuál es la diferencia conceptual más importante entre CMD y PowerShell?

**A)** CMD solamente funciona con Internet y PowerShell sin Internet.

**B)** PowerShell trabaja con objetos y ofrece capacidades avanzadas de administración y automatización.

**C)** CMD es exclusivo para servidores y PowerShell para clientes.

**D)** PowerShell no puede ejecutar comandos del sistema.

**🔹 Pregunta 6**

¿Qué significa esta estructura en PowerShell?

Get-Process \| Where-Object ...

**A)** Ejecuta <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> procesos simultáneamente.

**B)** Envía la salida de Get-Process hacia Where-Object para procesarla o filtrarla.

**C)** Elimina todos los procesos.

**D)** Convierte PowerShell en CMD.

**🔹 Pregunta 7 — Caso SOC**

El EDR registra:

Parent:

WINWORD.EXE

Child:

POWERSHELL.EXE

Command Line:

powershell.exe -File C:\Users\Juan\Downloads\factura.ps1

¿Cuál es la reacción más adecuada del analista?

**A)** Bloquear inmediatamente todos los documentos de Word.

**B)** Declarar malware confirmado solamente por la presencia de PowerShell.

**C)** Investigar el documento, el script, el usuario, la línea de comandos y la actividad posterior.

**D)** Ignorar el evento porque PowerShell es una herramienta legítima.

**🔹 Pregunta 8**

¿Qué concepto describe mejor el abuso de herramientas legítimas de Windows por parte de un atacante?

**A)** NTFS.

**B)** Living off the Land.

**C)** DHCP.

**D)** DNS poisoning.

**🔹 Pregunta 9 — Caso SOC**

Se observa:

powershell.exe

↓

Get-NetTCPConnection

↓

conexión externa sospechosa

¿Qué debería intentar determinar el analista?

**A)** Únicamente la versión de Windows.

**B)** Qué usuario ejecutó PowerShell, desde qué proceso padre, qué comandos utilizó y qué proceso realizó la conexión.

**C)** Solamente si PowerShell está instalado.

**D)** Eliminar PowerShell del equipo.

**🔹 Pregunta 10 — Caso SOC ⭐**

El SIEM muestra:

Usuario: Carlos

WINWORD.EXE

↓

POWERSHELL.EXE

↓

CMD.EXE

↓

archivo.exe

↓

conexión externa

↓

nuevo servicio

¿Cuál es la interpretación más apropiada?

**A)** Es una secuencia normal porque todos los programas son de Windows.

**B)** Es malware confirmado sin necesidad de investigar más.

**C)** Es una cadena potencialmente sospechosa que debe investigarse correlacionando procesos, usuario, comandos, archivo, red y persistencia.

**D)** Es exclusivamente un problema de DNS.

**⛔ PAUSA**

Antes de bajar a las respuestas, anotá tus opciones:

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

Intentá resolverlas como si estuvieras frente a una alerta de un SOC.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**1. ✅ B — whoami**

whoami

muestra la identidad con la que se está ejecutando la sesión.

Ejemplo:

empresa\juan

Para SOC es importante porque permite relacionar una actividad con una identidad.

**2. ✅ C — Configuración detallada de red**

ipconfig /all

puede mostrar:

- IPv4

- IPv6

- máscara

- gateway

- DNS

- DHCP

- MAC

- adaptadores

Esto conecta directamente con todo lo que estudiamos en **Redes 1 y Redes 2**.

**3. ✅ B — Conexiones de red + puertos + estado + PID**

Este comando:

netstat -ano

es especialmente útil para investigación.

Podemos encontrar algo como:

IP local:puerto

↓

IP remota:puerto

↓

Estado

↓

PID

Y luego:

PID

↓

Proceso

Por ejemplo:

PID 4520

↓

powershell.exe

↓

conexión externa

Ahí empieza a aparecer información muy valiosa para un SOC.

**4. ✅ A — tasklist**

tasklist

permite listar procesos y sus identificadores.

Por ejemplo:

Image Name PID

---------------------

explorer.exe 3520

powershell.exe 4520

Entonces podemos correlacionar el PID encontrado mediante netstat.

**5. ✅ B — PowerShell trabaja con objetos**

Esta es una diferencia fundamental.

CMD tradicionalmente trabaja mucho con **texto**.

PowerShell trabaja con **objetos**, lo que permite consultar propiedades, filtrarlas y automatizar tareas de manera mucho más potente.

Por ejemplo:

Get-Process

devuelve objetos que representan procesos.

**6. ✅ B — Pipe \|**

El símbolo:

\|

es el **pipe**.

Permite pasar la salida de un comando al siguiente.

Conceptualmente:

Get-Process

↓

\|

↓

Where-Object

↓

filtrar

Es una de las herramientas fundamentales de PowerShell.

**7. ✅ C — Investigar el contexto**

Tenemos:

WINWORD.EXE

↓

POWERSHELL.EXE

↓

factura.ps1

Esto **no confirma automáticamente malware**.

Pero sí genera una alerta interesante.

El analista debería investigar:

¿Quién abrió Word?

↓

¿Qué documento abrió?

↓

¿De dónde salió?

↓

¿Qué contiene factura.ps1?

↓

¿Qué comandos ejecutó?

↓

¿Se conectó a Internet?

↓

¿Creó archivos/procesos?

Esta es exactamente la forma de pensar que queremos desarrollar.

**8. ✅ B — Living off the Land**

**Living off the Land (LotL)** describe el uso de herramientas legítimas disponibles en el sistema para realizar actividades maliciosas.

Por ejemplo:

PowerShell

CMD

WMI

El problema para el SOC es que:

**Una herramienta legítima puede utilizarse para una actividad ilegítima.**

Por eso no alcanza con mirar solamente el nombre del proceso.

**9. ✅ B — Investigar usuario, proceso, comandos y conexión**

Tenemos:

PowerShell

↓

consulta conexiones

↓

conexión sospechosa

Hay que reconstruir el contexto.

Preguntas importantes:

¿Quién ejecutó PowerShell?

↓

¿Cuál era el proceso padre?

↓

¿Qué comandos ejecutó?

↓

¿Qué proceso realizó la conexión?

↓

¿A qué IP/dominio?

↓

¿Qué ocurrió después?

Esto convierte un evento aislado en una investigación.

**10. ✅ C — Cadena potencialmente sospechosa**

Tenemos:

WINWORD

↓

PowerShell

↓

CMD

↓

archivo

↓

Internet

↓

servicio

Esto podría representar:

Ejecución

↓

Actividad

↓

Comunicación

↓

Persistencia

Pero todavía debemos investigar antes de afirmar que es malware.

Ese matiz es **muy importante para un SOC profesional**.

**🏆 EVALUACIÓN**

| **Resultado** | **Nivel**           |
|---------------|---------------------|
| **10/10**     | 🟢 Excelente        |
| **8–9/10**    | 🟢 Muy buen nivel   |
| **6–7/10**    | 🟡 Buen progreso    |
| **4–5/10**    | 🟠 Conviene repasar |
| **0–3/10**    | 🔴 Reforzar el tema |

**🧠 DESAFÍO EXTRA — SOC**

Este no cuenta para la nota.

El SIEM detecta:

Usuario: Gonzalo

22:31

WINWORD.EXE

22:32

└── POWERSHELL.EXE

PID: 4812

22:33

└── CMD.EXE

22:34

└── update.exe

22:34

netstat:

PID 4812 → conexión externa

22:36

Nuevo servicio:

WindowsUpdateHelper

Como analista, tu primera tarea sería **construir la línea temporal**:

1\. ¿Qué ocurrió primero?

2\. ¿Qué proceso creó a cuál?

3\. ¿Qué usuario inició la actividad?

4\. ¿Qué conexión realizó el proceso?

5\. ¿Qué archivo apareció?

6\. ¿Qué servicio fue creado?

7\. ¿Podría existir persistencia?

Esto ya combina prácticamente todo lo que aprendimos hasta ahora:

**usuarios + procesos + servicios + CMD + PowerShell + red + persistencia.**

Y justamente esa capacidad de **correlacionar piezas** es la que vamos a seguir entrenando para tu objetivo de trabajar en un SOC.

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
