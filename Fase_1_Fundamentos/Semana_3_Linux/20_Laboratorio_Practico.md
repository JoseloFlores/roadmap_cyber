**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 3 – Linux**

**Módulo 20 – Laboratorio Práctico de Linux**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ Introducción a Linux y la Terminal (<a href="../../GLOSARIO.md#cli" target="_blank">CLI</a>)

- ✅ Estructura del Sistema de Archivos (<a href="../../GLOSARIO.md#fhs" target="_blank">FHS</a>)

- ✅ Permisos de Archivos (rwx)

- ✅ Gestión de Usuarios y Grupos

- ✅ Gestión de Procesos

- ✅ <a href="../../GLOSARIO.md#grep" target="_blank">grep</a>, Pipes y Análisis de Logs

Hasta ahora has visto la teoría de cada tema por separado.

Este es el **módulo de laboratorio** de la semana.

Aquí no hay teoría nueva.

Aquí vas a **poner las manos sobre el teclado** y ejecutar todo lo aprendido.

El objetivo es integrar en un solo escenario práctico:

- La creación de usuarios y grupos.

- La configuración de permisos restrictivos.

- El análisis de logs con `grep`.

- El monitoreo en tiempo real con `tail -f`.

- La gestión de procesos.

Vas a simular una pequeña situación de oficina:

una empresa con <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> equipos de trabajo (ventas y sistemas), una carpeta compartida con información secreta y un servidor que registra intentos de acceso fallidos.

Ese escenario te obligará a usar las herramientas de Linux exactamente como las usarás el día de mañana dentro de un SOC.

La meta de esta semana es simple y exigente a la vez:

**moverte con total soltura en la terminal sin depender de la interfaz gráfica.**

**🎯 Objetivos del laboratorio**

Al finalizar este laboratorio podrás:

- Aplicar comandos reales de Linux en un entorno de prueba.

- Crear usuarios y grupos con `groupadd` y `useradd`.

- Asignar contraseñas con `passwd`.

- Configurar permisos restrictivos con `chmod` y `chown`.

- Verificar quién puede acceder a qué con `su` y `id`.

- Analizar logs de autenticación con `grep`.

- Contar intentos fallidos de acceso con `grep -c`.

- Monitorear logs en tiempo real con `tail -f`.

- Gestionar procesos con `ps`, `top` y `kill`.

- Detectar patrones de fuerza bruta en los logs.

**Requisitos**

Para realizar este laboratorio necesitas:

- Una máquina virtual con **Ubuntu** o **Debian** (o la <a href="../../GLOSARIO.md#distribucion" target="_blank">distribución</a> que uses).

- Un usuario con permisos de administrador (`sudo`).

- Una terminal abierta.

- Ganas de equivocarte y probar de nuevo.

Si todavía no tienes una máquina virtual creada, revisa el PDF **"Creando maquina virtual.pdf"** que se encuentra en la carpeta **Recursos** de tu formación.

Importante sobre la responsabilidad:

Todo lo que haremos en este laboratorio se realiza en un **entorno de prueba local**.

Nunca ejecutes estos pasos en un servidor de producción.

Los comandos que modifican usuarios, permisos y archivos están diseñados para una máquina que puedes romper y volver a crear sin consecuencias.

Esa es la gran ventaja de practicar con una VM.

**1. Preparación del entorno**

Antes de empezar a crear usuarios y revisar logs, vamos a verificar que todo funciona.

**Paso 1: Abrir la terminal**

Abre la terminal de tu máquina virtual.

En Ubuntu puedes abrirla con el atajo de teclado:

`Ctrl + Alt + T`

También puedes buscarla en el menú de aplicaciones.

Verás una ventana negra con un texto similar a:

`usuario@ubuntu:~$`

Ese texto se llama **prompt** y te dice:

- Qué usuario eres (`usuario`).

- En qué máquina estás (`ubuntu`).

- En qué carpeta estás (`~`, que significa tu directorio personal).

**Paso 2: Ver quién eres**

Escribe:

`whoami`

Deberías ver tu nombre de usuario.

Este comando responde la pregunta: ¿quién soy en este sistema?

Es la primera verificación que hace cualquier analista antes de tocar un sistema.

**Paso 3: Ver dónde estás**

Escribe:

`pwd`

`pwd` significa **print working directory**.

Te muestra la ruta absoluta de la carpeta donde te encuentras.

Deberías ver algo como:

`/home/usuario`

Es decir, estás dentro de tu directorio personal.

**Paso 4: Verificar que tienes permisos de administrador**

Escribe:

`sudo -v`

Este comando valida tu contraseña de administrador.

La primera vez te pedirá tu contraseña.

Escríbela y presiona Enter.

Nota importante:

Cuando escribas la contraseña, **no verás caracteres en la pantalla**.

Ni puntos, ni asteriscos.

Eso es normal y seguro.

Linux lo hace a propósito para que nadie mire cuántos caracteres tiene tu contraseña.

Si el comando termina sin mostrar errores, significa que tienes acceso `sudo` correcto.

Si ves un mensaje de error como *"usuario is not in the sudoers file"*, necesitas agregar tu usuario al grupo `sudo` antes de continuar.

**Paso 5: Verificar la red**

Escribe:

`ping -c 4 8.8.8.8`

Esto envía 4 paquetes a la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> 8.8.8.8 (un servidor de Google).

Deberías ver respuestas como:

`64 bytes from 8.8.8.8: icmp_seq=1 ttl=... time=...`

Este comando no es obligatorio para el laboratorio, pero confirma que tu máquina virtual tiene acceso a Internet.

Si tu VM no tiene red, no pasa nada: los laboratorios funcionan igual.

**Paso 6: Ver la fecha del sistema**

Escribe:

`date`

Verás la fecha y hora actuales.

Esto es más útil de lo que parece:

cuando analices logs, necesitarás saber en qué hora está el sistema para compararla con la hora de los eventos.

**🧠 Concepto importante**

Todos los comandos que empiezan con `sudo` se ejecutan como **administrador**.

Los comandos que no llevan `sudo` se ejecutan con tus permisos de usuario normal.

Un analista SOC siempre sabe **con qué permisos está ejecutando cada comando**.

**2. Laboratorio 1: Crear usuarios y grupos**

En una empresa real, cada empleado tiene su propio usuario.

Y cada usuario pertenece a un grupo según su área.

Nosotros vamos a simular una pequeña oficina con dos departamentos:

- **ventas**

- **sistemas**

Y dos empleados:

- **ana**, que trabaja en ventas.

- **carlos**, que trabaja en sistemas.

**Paso 1: Crear los grupos**

Ejecuta:

`sudo groupadd ventas`

Este comando crea el grupo **ventas**.

`groupadd` significa "agregar grupo".

Ahora ejecuta:

`sudo groupadd sistemas`

Este comando crea el grupo **sistemas**.

Nota: si tu distribución usa los grupos **ventas** y **sistemas** en mayúscula o con otro nombre, no importa. Lo que importa es el procedimiento.

**Paso 2: Verificar que los grupos existen**

Ejecuta:

`grep ventas /etc/group`

Deberías ver una línea como:

`ventas:x:1001:`

Eso significa que el grupo **ventas** existe y tiene un ID de grupo (GID).

Ejecuta también:

`grep sistemas /etc/group`

Deberías ver una línea similar para **sistemas**.

El archivo `/etc/group` es el catálogo de grupos del sistema.

Cada línea tiene este formato:

`nombre_grupo:contrasena:gid:miembros`

**Paso 3: Crear el usuario ana**

Ejecuta:

`sudo useradd -m -g ventas ana`

Vamos a desglosar este comando:

- `useradd` → crea un usuario.

- `-m` → crea el directorio personal (`/home/ana`).

- `-g ventas` → asigna a ana el grupo principal **ventas**.

- `ana` → nombre del usuario.

Sin la opción `-m`, Linux no crea el directorio personal del usuario.

Eso causaría problemas al usuario cuando quiera guardar archivos.

**Paso 4: Crear el usuario carlos**

Ejecuta:

`sudo useradd -m -g sistemas carlos`

Este comando hace lo mismo, pero con el usuario **carlos** y el grupo **sistemas**.

**Paso 5: Asignar contraseñas**

Los usuarios existen, pero todavía no tienen contraseña.

Sin contraseña no pueden iniciar sesión.

Ejecuta:

`sudo passwd ana`

El sistema te pedirá que escribas una contraseña dos veces.

Esto es lo que vas a ver:

`New password:`

`Retype new password:`

`passwd: password updated successfully`

La frase final confirma que la contraseña se guardó correctamente.

Ahora ejecuta:

`sudo passwd carlos`

Repite el mismo proceso.

Usa contraseñas fáciles de recordar para el laboratorio, por ejemplo:

- ana → `ana123`

- carlos → `carlos123`

En una empresa real las contraseñas deben ser fuertes.

Pero en tu VM de práctica puedes usar contraseñas simples.

**Paso 6: Verificar los usuarios**

Ejecuta:

`id ana`

Deberías ver algo como:

`uid=1001(ana) gid=1001(ventas) groups=1001(ventas)`

Interpretación:

- `uid=1001(ana)` → el ID de usuario de ana es 1001.

- `gid=1001(ventas)` → su grupo principal es ventas.

- `groups=1001(ventas)` → pertenece al grupo ventas.

Ahora ejecuta:

`id carlos`

Deberías ver algo como:

`uid=1002(carlos) gid=1002(sistemas) groups=1002(sistemas)`

Nota que cada usuario tiene su propio UID.

Linux identifica a las personas por números, no por nombres.

**Paso 7: Verificar en el catálogo de usuarios**

Ejecuta:

`tail -5 /etc/passwd`

Deberías ver las últimas 5 líneas del archivo `/etc/passwd`, donde aparecen ana y carlos.

Cada línea se ve similar a:

`ana:x:1001:1001::/home/ana:/bin/sh`

Los campos, separados por dos puntos, son:

- Nombre de usuario: `ana`.

- `x` → la contraseña está guardada en otro archivo protegido.

- UID: `1001`.

- GID: `1001`.

- Directorio personal: `/home/ana`.

- <a href="../../GLOSARIO.md#shell" target="_blank">Shell</a>: `/bin/sh`.

**Paso 8: Verificar los directorios personales**

Ejecuta:

`ls -l /home`

Deberías ver los directorios `/home/ana` y `/home/carlos`.

Cada uno pertenece a su usuario.

**🎓 Dato de SOC**

En una investigación real, los archivos `/etc/passwd` y `/etc/group` te dicen **qué usuarios y grupos existen** en un sistema comprometido.

Un analista revisa si hay usuarios creados en fechas sospechosas o con nombres extraños.

Eso puede indicar que un atacante dejó una "puerta trasera" con una cuenta oculta.

**3. Laboratorio 2: Configurar permisos restrictivos**

Ahora viene la parte interesante.

Vamos a crear una carpeta compartida para el departamento de sistemas.

Solo los miembros de **sistemas** podrán entrar y trabajar.

El resto del sistema no podrá ni ver su contenido.

**Paso 1: Crear la carpeta del proyecto**

Ejecuta:

`sudo mkdir /opt/proyecto`

Esto crea la carpeta `/opt/proyecto`.

`mkdir` significa **make directory**.

La carpeta `/opt` está pensada para software y proyectos opcionales, así que es un buen lugar.

Verifica que se creó:

`ls -ld /opt/proyecto`

Deberías ver algo como:

`drwxr-xr-x 2 root root 4096 fecha /opt/proyecto`

Interpretación del principio:

- `d` → es un directorio.

- `rwxr-xr-x` → permisos del dueño (<a href="../../GLOSARIO.md#root" target="_blank">root</a>), del grupo (root) y del resto.

En este momento, el dueño es `root` y el grupo es `root`.

Tenemos que cambiar el grupo.

**Paso 2: Cambiar el grupo de la carpeta**

Ejecuta:

`sudo chown :sistemas /opt/proyecto`

`chown` cambia el dueño.

Al escribir `:sistemas`, cambiamos **solo el grupo** (el campo vacío significa "no cambiar al dueño").

Verifica:

`ls -ld /opt/proyecto`

Ahora deberías ver:

`drwxr-xr-x 2 root sistemas 4096 fecha /opt/proyecto`

La carpeta pertenece a `root:sistemas`.

**Paso 3: Configurar permisos restrictivos**

Ejecuta:

`sudo chmod 770 /opt/proyecto`

El número `770` es la notación octal de permisos.

Significa:

- **7** para el dueño (root) → lectura, escritura y ejecución.

- **7** para el grupo (sistemas) → lectura, escritura y ejecución.

- **0** para el resto del mundo → ningún permiso.

Desglose del 7:

- 4 = lectura (r)

- 2 = escritura (w)

- 1 = ejecución (x)

- 7 = 4 + 2 + 1 → rwx completo

Verifica con:

`ls -ld /opt/proyecto`

Ahora deberías ver:

`drwxrwx--- 2 root sistemas 4096 fecha /opt/proyecto`

Fíjate en el final:

`rwxrwx---`

- El dueño (root): `rwx`.

- El grupo (sistemas): `rwx`.

- El resto: `---` (nada).

**Analogía**

Piensa en una sala de reuniones con cerradura.

- `root` es el jefe: tiene llave maestra.

- `sistemas` es el equipo: cada miembro tiene llave.

- El resto del edificio: no tiene llave ni puede ver la puerta.

**Paso 4: Crear un archivo secreto**

Ejecuta:

`sudo touch /opt/proyecto/secretos.txt`

`touch` crea un archivo vacío.

Verifica que existe:

`ls -l /opt/proyecto`

Ahora dale permisos muy restrictivos:

`sudo chmod 600 /opt/proyecto/secretos.txt`

El `600` significa:

- **6** para el dueño (root) → lectura y escritura (4 + 2).

- **0** para el grupo.

- **0** para el resto.

Nadie más que root puede tocar ese archivo.

Verifica:

`ls -l /opt/proyecto/secretos.txt`

Deberías ver:

`-rw------- 1 root root 0 fecha /opt/proyecto/secretos.txt`

El patrón `rw-------` confirma el permiso 600.

**Paso 5: Probar el acceso como ana (debe fallar)**

Ejecuta:

`su - ana`

El comando `su -` inicia una sesión como otro usuario.

Te pedirá la contraseña de ana.

Escribe la contraseña que le asignaste.

Ahora, ya como ana, intenta entrar a la carpeta:

`ls /opt/proyecto`

Deberías ver un error:

`ls: cannot open directory '/opt/proyecto': Permission denied`

Ese error es exactamente lo que queremos.

Ana pertenece a **ventas**, no a **sistemas**.

Como la carpeta tiene permisos `770`, y ana no es ni dueña ni del grupo, no puede ni listarla.

Escribe:

`cat /opt/proyecto/secretos.txt`

Deberías ver:

`cat: /opt/proyecto/secretos.txt: Permission denied`

Ana no puede leer el archivo secreto.

Eso es correcto.

**Paso 6: Salir de la sesión de ana**

Ejecuta:

`exit`

Volverás a tu sesión normal de usuario.

**Paso 7: Probar el acceso como carlos (debe funcionar)**

Ejecuta:

`su - carlos`

Te pedirá la contraseña de carlos.

Ya como carlos, intenta entrar:

`ls /opt/proyecto`

Ahora deberías poder listar la carpeta sin errores.

Verás:

`secretos.txt`

Carlos pertenece al grupo **sistemas**.

Como la carpeta tiene permisos `770` y el grupo es **sistemas**, carlos puede entrar.

Ahora intenta leer el archivo secreto:

`cat /opt/proyecto/secretos.txt`

Nota lo que pasa:

Carlos **puede entrar a la carpeta**, pero no puede leer el archivo.

¿Por qué?

Porque el archivo tiene permisos `600`.

Solo el dueño (root) puede leerlo.

El grupo y el resto tienen `0`.

El acceso a una carpeta **no garantiza** acceso a lo que hay dentro.

Cada archivo tiene sus propios permisos.

Esa es una distinción muy importante para un analista.

Ejecuta:

`exit`

Vuelve a tu sesión normal.

**Paso 8: Crear una carpeta pública**

Para comparar, vamos a crear una carpeta de acceso público.

Ejecuta:

`sudo mkdir /opt/publica`

`sudo chmod 755 /opt/publica`

El `755` significa:

- **7** para el dueño → rwx.

- **5** para el grupo → lectura y ejecución (4 + 1).

- **5** para el resto → lectura y ejecución (4 + 1).

Todos pueden entrar y leer, pero solo el dueño puede modificar.

Verifica:

`ls -ld /opt/publica`

Deberías ver:

`drwxr-xr-x 2 root root 4096 fecha /opt/publica`

Pruébalo como ana:

`su - ana`

`ls /opt/publica`

Ahora sí, ana puede entrar sin problemas.

Ejecuta:

`exit`

**🧠 Concepto importante**

| **Permiso** | **Dueño** | **Grupo** | **Resto** | **¿Quién entra?**                    |
|-------------|-----------|-----------|-----------|--------------------------------------|
| `770`       | rwx       | rwx       | `---`     | Solo dueño y miembros del grupo.     |
| `755`       | rwx       | r-x       | `r-x`     | Todo el mundo puede entrar y leer.   |
| `600`       | rw-       | `---`     | `---`     | Solo el dueño puede leer/escribir.   |

**🎓 Dato de SOC**

Los permisos `770` y `600` son ejemplos del **principio de menor privilegio**.

Cada usuario tiene acceso únicamente a lo que necesita para trabajar.

En un SOC verás que las malas configuraciones de permisos aparecen en los rankings de vulnerabilidades más explotadas.

Un archivo de configuración con permisos demasiado abiertos puede filtrar contraseñas o claves privadas.

**4. Laboratorio 3: Búsquedas avanzadas de logs con grep**

Ahora vas a ponerte el sombrero de analista.

Los logs de autenticación registran todos los intentos de acceso al sistema.

En Debian y Ubuntu, esos logs viven en:

`/var/log/auth.log`

En distribuciones basadas en Red Hat (como CentOS, Fedora o Rocky), el archivo equivalente se llama:

`/var/log/secure`

Para este laboratorio asumimos que usas Ubuntu o Debian.

**Paso 1: Verificar que el log existe**

Ejecuta:

`ls -l /var/log/auth.log`

Deberías ver una entrada como:

`-rw-r--r-- 1 syslog adm 123456 fecha /var/log/auth.log`

Si no existe el archivo, es posible que necesites ejecutar:

`sudo grep "Failed password" /var/log/secure`

o revisar dónde está el log de autenticación en tu distribución.

**Paso 2: Leer un fragmento del log**

Ejecuta:

`tail -20 /var/log/auth.log`

Verás las últimas 20 líneas del log.

Cada línea es un evento de autenticación con:

- Fecha y hora.

- Máquina.

- Proceso (por ejemplo `sshd`).

- Descripción del evento.

Este es el formato de los logs que analizarás todos los días.

**Paso 3: Buscar intentos de acceso fallidos**

Ejecuta:

`grep "Failed password" /var/log/auth.log`

Este comando busca todas las líneas que contienen el texto **"Failed password"**.

Si tu sistema recibió intentos de conexión <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> fallidos, verás líneas como:

`Aug 14 10:22:01 ubuntu sshd[...]: Failed password for invalid user admin from 203.0.113.45 port 50000 ssh2`

Interpretación:

- Hubo un intento fallido.

- El usuario intentado era `admin`.

- El origen era la IP `203.0.113.45`.

Si no ves resultados, no te preocupes.

Los logs de una máquina nueva suelen estar vacíos de intentos fallidos.

Más adelante en este laboratorio vamos a generar nuestros propios intentos.

**Paso 4: Contar los intentos fallidos**

Ejecuta:

`grep -c "Failed password" /var/log/auth.log`

El `-c` significa **count** (contar).

En lugar de mostrar las líneas, muestra el número de coincidencias.

Deberías ver un número.

Si no hay intentos fallidos, verás:

`0`

**Paso 5: Buscar accesos exitosos**

Ejecuta:

`grep "Accepted password" /var/log/auth.log`

Este comando busca los accesos que sí fueron exitosos.

Las líneas se ven así:

`Aug 14 09:00:12 ubuntu sshd[...]: Accepted password for ana from 192.168.1.50 port 50001 ssh2`

Un analista que ve:

- Muchos `Failed password`.

- Y luego un `Accepted password`.

Debe preguntarse inmediatamente: ¿el atacante logró entrar?

**Paso 6: Búsqueda sin distinguir mayúsculas**

Ejecuta:

`grep -i "failed" /var/log/auth.log`

La opción `-i` ignora las mayúsculas y minúsculas.

Esto encontrará:

- `Failed`

- `failed`

- `FAILED`

Es útil porque los logs de distintos sistemas escriben las palabras de forma diferente.

**Paso 7: Excluir líneas con la opción -v**

Ejecuta:

`grep -v "session" /var/log/auth.log`

La opción `-v` invierte la búsqueda.

Muestra **todas las líneas que NO contienen** la palabra `session`.

Útil para limpiar el ruido:

`grep "Accepted" /var/log/auth.log | grep -v "password"`

Ese pipeline muestra los accesos aceptados, pero excluye las líneas que contienen `password`.

**Paso 8: Combinar grep con otros comandos**

Ejecuta:

`grep "Failed password" /var/log/auth.log | tail -5`

Verás los últimos 5 intentos fallidos.

Ejecuta:

`grep "Failed password" /var/log/auth.log | wc -l`

Verás el mismo resultado que con `grep -c`, pero usando un <a href="../../GLOSARIO.md#pipe" target="_blank">pipe</a>.

Ambas formas son válidas.

**Paso 9: Ver los últimos intentos con más detalle**

Ejecuta:

`sudo lastb | head -10`

`lastb` muestra los **últimos intentos de conexión fallidos** registrados por el sistema.

En muchas distribuciones necesita `sudo` porque contiene información sensible.

Si ves líneas como:

`ana     ssh:notty    203.0.113.45     Thu Aug 14 10:30 - 10:30 (00:00)`

Significa que alguien intentó conectarse como ana y falló.

**🎓 Dato de SOC**

El patrón más clásico de fuerza bruta en Linux se ve así en los logs:

- Muchos `Failed password` desde una misma IP.

- Con usuarios variados (`root`, `admin`, `oracle`, `test`).

- En un período corto de tiempo.

- A veces seguido de un `Accepted password`.

Esa secuencia es la firma de un ataque automatizado.

**5. Laboratorio 4: Monitoreo en tiempo real con tail -f**

Hasta ahora hemos buscado eventos que ya ocurrieron.

Pero un analista SOC también vigila los logs **mientras ocurren los eventos**.

Para eso existe `tail -f`.

La opción `-f` significa **follow** (seguir).

El comando se queda "mirando" el archivo y muestra cada línea nueva que se agrega.

**Paso 1: Abrir el log en modo seguimiento**

Ejecuta:

`sudo tail -f /var/log/auth.log`

Nota el `sudo`:

el log de autenticación suele ser legible solo por el grupo `adm`, así que necesitamos permisos elevados.

El comando no va a terminar.

Quedará "colgado" esperando líneas nuevas.

Eso es correcto.

Deja esta terminal abierta.

**Paso 2: Abrir una segunda terminal**

Abre otra terminal (puedes usar `Ctrl + Alt + T` para abrir una ventana nueva).

**Paso 3: Generar eventos en la segunda terminal**

Vamos a simular intentos de acceso.

Ejecuta:

`su - ana`

Te pedirá la contraseña de ana.

Escribe **una contraseña incorrecta** a propósito.

Verás el error:

`su: Authentication failure`

Ahora vuelve a intentarlo con una contraseña incorrecta de nuevo.

Ejecuta:

`su - ana`

Y escribe otra contraseña incorrecta.

Repite una vez más:

`su - carlos`

Escribe una contraseña incorrecta para carlos.

**Paso 4: Observar la primera terminal**

Vuelve a la primera terminal (la del `tail -f`).

Deberías ver aparecer, en tiempo real, líneas nuevas como:

`Aug 14 10:35:20 ubuntu su[...]: FAILED su (to ana) usuario on pts/1`

`Aug 14 10:35:22 ubuntu su[...]: FAILED su (to carlos) usuario on pts/1`

Cada intento fallido que hiciste en la segunda terminal aparece **al instante** en la primera.

Eso es `tail -f` en acción.

**Paso 5: Simular un acceso correcto**

En la segunda terminal, inicia sesión correctamente como carlos:

`su - carlos`

Escribe la contraseña correcta de carlos.

En la primera terminal deberías ver una línea nueva con el acceso correcto, similar a:

`Aug 14 10:36:00 ubuntu su[...]: Successful su for carlos by usuario`

Ahora en la segunda terminal ejecuta:

`exit`

**Paso 6: Buscar las <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> de origen**

Si quieres ver de dónde vienen los intentos con más detalle, en la primera terminal (después de `Ctrl + C`) ejecuta:

`grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c`

Este pipeline:

- Filtra las líneas fallidas.

- Extrae el campo número 11 (la IP en la línea de sshd).

- Las ordena.

- Cuenta cuántas veces aparece cada IP.

Si tus intentos fueron con `su` y no con SSH, puede que no veas IPs.

Pero la técnica es oro puro para un SOC:

`grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c`

Es una de las primeras consultas que hace un analista cuando sospecha fuerza bruta.

**Paso 7: Detener el monitoreo**

En la primera terminal, presiona:

`Ctrl + C`

Esto interrumpe el comando `tail -f` y te devuelve el prompt.

**🧠 Concepto importante**

| **Comando** | **¿Qué hace?**                                  |
|-------------|--------------------------------------------------|
| `tail -20`  | Muestra las últimas 20 líneas y termina.        |
| `tail -f`   | Se queda en vivo mostrando las líneas nuevas.    |
| `Ctrl + C`  | Detiene el comando que está en primer plano.     |

**🎓 Dato de SOC**

En un SOC, `tail -f` (o herramientas equivalentes) se usa para:

- Verificar en vivo si un ataque continúa.

- Confirmar que una regla de bloqueo está funcionando.

- Seguir la actividad de un usuario sospechoso.

- Ver si los intentos de acceso cesan después de bloquear una IP.

**6. Laboratorio 5 (extra): Gestión de procesos**

Los procesos son los programas en ejecución.

Un servidor Linux tiene cientos de procesos activos.

Un analista necesita saber cuáles son normales y cuáles no.

**Paso 1: Ver los procesos del sistema**

Ejecuta:

`ps aux`

Verás una lista enorme de procesos.

Columnas principales:

- `USER` → quién ejecuta el proceso.

- `PID` → identificador numérico del proceso.

- `%CPU` → porcentaje de CPU usado.

- `%MEM` → porcentaje de memoria usada.

- `COMMAND` → el comando que lo lanzó.

**Paso 2: Buscar un proceso específico**

Ejecuta:

`ps aux | grep sshd`

Este pipeline muestra solo los procesos que contienen `sshd` (el servicio de SSH).

`grep` busca dentro de la salida de `ps`.

Deberías ver uno o dos procesos de `sshd` si el servicio está activo.

Nota: la propia línea de `grep` aparece en el resultado.

Eso es normal y no significa nada raro.

**Paso 3: Observar los procesos en vivo con top**

Ejecuta:

`top`

Verás una pantalla que se actualiza cada pocos segundos.

En la parte superior está el resumen del sistema (CPU, memoria, carga).

Debajo, la lista de procesos ordenada por uso de CPU.

Esto te muestra **en tiempo real** qué proceso está consumiendo más recursos.

Para salir, presiona:

`q`

**Paso 4: Crear un proceso de prueba**

Vamos a lanzar un proceso en segundo plano.

Ejecuta:

`sleep 300 &`

Qué hace este comando:

- `sleep 300` → un programa que no hace nada durante 300 segundos.

- `&` → lo lanza en segundo plano (background).

Linux te responderá con una línea como:

`[1] 12345`

Interpretación:

- `[1]` → número de job en tu sesión.

- `12345` → el **<a href="../../GLOSARIO.md#pid" target="_blank">PID</a>** del proceso.

**Paso 5: Encontrar el proceso**

Ejecuta:

`ps aux | grep sleep`

Deberías ver una línea con tu proceso `sleep 300`.

Fíjate en el número del PID.

**Paso 6: Matar el proceso**

Ejecuta:

`kill 12345`

Usa el PID real que apareció en tu sistema.

`kill` envía una señal al proceso para que termine.

Verifica que ya no existe:

`ps aux | grep sleep`

Ahora el proceso ya no debería aparecer.

**Paso 7: Probar top de nuevo**

Ejecuta:

`top`

Presiona `q` para salir.

**🎓 Dato de SOC**

En una investigación, los analistas buscan procesos sospechosos como:

- `nc` (netcat) corriendo desde un directorio extraño.

- `cron` ejecutando scripts no conocidos.

- Procesos con nombres genéricos que consumen mucha CPU.

- Procesos con permisos de root pero lanzados desde carpetas temporales.

`ps aux` y `top` son las dos primeras herramientas que un analista usa para detectar actividad maliciosa en Linux.

**7. Resumen de lo logrado**

Haz un recorrido mental por lo que acabas de hacer.

Verifica con estas comprobaciones:

- [ ] ¿Creaste los usuarios ana y carlos?

  Puedes confirmarlo con:

  `grep -E "ana|carlos" /etc/passwd`

- [ ] ¿Creaste los grupos ventas y sistemas?

  Puedes confirmarlo con:

  `grep -E "ventas|sistemas" /etc/group`

- [ ] ¿Asignaste contraseñas a ambos usuarios?

  Puedes confirmarlo intentando:

  `su - ana`

- [ ] ¿La carpeta /opt/proyecto tiene permisos 770 y pertenece al grupo sistemas?

  Puedes confirmarlo con:

  `ls -ld /opt/proyecto`

- [ ] ¿El archivo secretos.txt tiene permisos 600?

  Puedes confirmarlo con:

  `ls -l /opt/proyecto/secretos.txt`

- [ ] ¿Comprobaste que ana no puede entrar y carlos sí?

- [ ] ¿Buscaste "Failed password" en el log?

  Con:

  `grep "Failed password" /var/log/auth.log`

- [ ] ¿Contaste los intentos fallidos?

  Con:

  `grep -c "Failed password" /var/log/auth.log`

- [ ] ¿Viste el log aparecer en vivo con tail -f?

- [ ] ¿Detectaste y mataste un proceso con ps y kill?

Si marcaste todos los casilleros, completaste la semana.

**8. Preguntas de reflexión**

Responde estas preguntas con tus propias palabras.

Te ayudan a consolidar lo que practicaste.

1. ¿Qué permiso le darías a una carpeta para que **solo el grupo sistemas** pueda entrar y trabajar en ella?

2. ¿Cómo sabrías si alguien está intentando forzar el acceso SSH a tu servidor?

3. ¿Por qué no se deben usar permisos `777` en archivos de configuración o scripts?

4. ¿Qué diferencia hay entre `tail -20` y `tail -f`?

5. Si ves muchos `Failed password` seguidos de un `Accepted password`, ¿qué hipótesis formularías?

6. ¿Por qué es importante saber con qué usuario ejecutas cada comando (`sudo` o sin `sudo`)?

**Respuestas de referencia (para autoevaluarte)**

1. `sudo chmod 770 carpeta` y asegurarte de que el grupo de la carpeta sea el correcto con `sudo chown :sistemas carpeta`.

2. Ejecutar `grep "Failed password" /var/log/auth.log` y contar coincidencias con `grep -c "Failed password" /var/log/auth.log`. También `tail -f /var/log/auth.log` en vivo.

3. Porque `777` da permisos de lectura, escritura y ejecución a **todos** los usuarios del sistema. Cualquier usuario podría modificar o ejecutar el archivo, incluido un atacante que ya tenga acceso limitado al equipo.

4. `tail -20` muestra las últimas 20 líneas y termina. `tail -f` se queda en vivo mostrando las líneas nuevas a medida que se escriben.

5. Que el atacante logró entrar después de probar credenciales. Hay que revisar inmediatamente el origen, el usuario comprometido, el horario y cualquier actividad posterior.

6. Porque muchos comandos solo funcionan con privilegios de root, y ejecutar como root algo innecesario aumenta el riesgo de romper el sistema o de dar a un atacante más poder si ejecutas algo malicioso.

**9. 🎯 Meta de la semana**

La meta de esta semana es:

**moverte con total soltura en la terminal sin depender de la interfaz gráfica.**

No se trata de memorizar comandos.

Se trata de que tus manos los escriban sin pensar.

La forma de lograrlo es la repetición.

**Autoevaluación**

Repite los laboratorios **sin mirar las notas**:

1. Crea dos usuarios y dos grupos desde cero.

2. Configura una carpeta con acceso solo para un grupo.

3. Crea un archivo que solo root pueda leer.

4. Genera intentos fallidos y encuéntralos con grep.

5. Cuenta los intentos fallidos.

6. Observa el log en vivo con tail -f.

7. Lanza un proceso, encuéntralo con ps y mátalo con kill.

Si puedes hacer los siete puntos sin consultar el material, estás listo para avanzar.

Si te trabas en algún paso, vuelve a leer el módulo correspondiente y repite.

La práctica es la clave.

**🎓 Consejo como tu instructor de SOC**

Cuando entres a un SOC real, el primer día te van a dar acceso a una terminal.

Los equipos Windows se administran con herramientas gráficas.

Los equipos Linux se administran con comandos.

Un analista que sabe moverse en la terminal:

- Investiga incidentes mucho más rápido.

- Entiende los logs con más profundidad.

- Puede trabajar en servidores que no tienen interfaz gráfica.

- Inspira confianza en su equipo.

Lo que practicaste hoy, con usuarios de prueba y una carpeta de práctica, es exactamente la misma lógica que usarás en un incidente real.

Solo cambia la gravedad.

Por eso practicar ahora es tan importante.

---

**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Evaluación – Módulo 20: Laboratorio Práctico de Linux**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Evalúa lo que practicaste en el laboratorio: creación de usuarios y grupos, permisos, análisis de logs con grep y monitoreo con tail -f. Algunas preguntas presentan escenarios similares a los que verás en tu trabajo diario como Analista SOC.

**Pregunta 1**

¿Qué comando se utiliza para crear un **usuario** nuevo en Linux?

**A)** `groupadd usuario`

**B)** `useradd -m usuario`

**C)** `passwd usuario`

**D)** `mkdir usuario`

**Pregunta 2**

Ejecutaste `sudo chmod 770 /opt/proyecto`. ¿Qué significa el número **770**?

**A)** Solo el dueño tiene todos los permisos.

**B)** El dueño y el grupo tienen permisos de lectura, escritura y ejecución, y el resto no tiene ninguno.

**C)** Todos los usuarios del sistema tienen todos los permisos.

**D)** Solo el grupo tiene permisos de lectura.

**Pregunta 3**

¿Qué comando te permite **contar** cuántas veces aparece el texto "Failed password" en el archivo `/var/log/auth.log`?

**A)** `grep -c "Failed password" /var/log/auth.log`

**B)** `grep -v "Failed password" /var/log/auth.log`

**C)** `tail -f "Failed password" /var/log/auth.log`

**D)** `cat "Failed password" /var/log/auth.log`

**Pregunta 4**

¿Para qué sirve el comando `tail -f /var/log/auth.log`?

**A)** Para ver las primeras líneas del archivo una sola vez.

**B)** Para quedarse monitoreando el archivo y mostrar las líneas nuevas en tiempo real.

**C)** Para borrar el archivo de logs.

**D)** Para contar las líneas del archivo.

**Pregunta 5**

Ejecutaste `id ana` y el sistema respondió:

`uid=1001(ana) gid=1001(ventas) groups=1001(ventas)`

¿Qué significa `gid=1001(ventas)`?

**A)** Que ana es la dueña del sistema.

**B)** Que el grupo principal de ana es ventas.

**C)** Que ana tiene la contraseña 1001.

**D)** Que ana puede usar el comando <a href="../../GLOSARIO.md#sudo" target="_blank">sudo</a>.

**Pregunta 6**

¿Qué comando muestra los procesos en ejecución?

**A)** `ps aux`

**B)** `ls -l`

**C)** `grep procesos`

**D)** `pwd`

**Pregunta 7**

Creaste un archivo con `sudo chmod 600 /opt/proyecto/secretos.txt`. ¿Quién puede leerlo?

**A)** Cualquier usuario del sistema.

**B)** Todos los miembros del grupo sistemas.

**C)** Solo el usuario root (el dueño del archivo).

**D)** Solo los usuarios que pertenezcan al grupo ventas.

**Pregunta 8**

¿Cuál es la ruta del log de autenticación en Ubuntu y Debian?

**A)** `/var/log/syslog`

**B)** `/var/log/auth.log`

**C)** `/var/log/secure`

**D)** `/etc/passwd`

**Pregunta 9**

Quieres saber qué procesos relacionados con SSH se están ejecutando. ¿Qué pipeline usarías?

**A)** `ps aux | grep sshd`

**B)** `grep sshd /etc/passwd`

**C)** `tail -f sshd`

**D)** `kill sshd`

**Pregunta 10 (Caso práctico SOC)**

Como analista SOC revisas el log `/var/log/auth.log` y encuentras esta secuencia:

`grep -c "Failed password" /var/log/auth.log` → **1.247**

Todos los intentos vienen de la misma IP `203.0.113.77` en los últimos 15 minutos, probando usuarios como `root`, `admin`, `oracle` y `test`. Al final aparece una línea `Accepted password for root from 203.0.113.77`.

¿Cuál sería la interpretación más razonable?

**A)** Tráfico normal de mantenimiento programado.

**B)** Un posible ataque de fuerza bruta contra SSH que terminó en un acceso exitoso.

**C)** Un error de sincronización del reloj del servidor.

**D)** El usuario root cambió su contraseña manualmente.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

`useradd -m usuario` crea un usuario nuevo y, con la opción `-m`, también crea su directorio personal en `/home/usuario`.

`groupadd` crea grupos, `passwd` asigna contraseñas y `mkdir` crea carpetas.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

El `770` en octal significa:

- 7 para el dueño → lectura, escritura y ejecución.

- 7 para el grupo → lectura, escritura y ejecución.

- 0 para el resto → ningún permiso.

Solo el dueño y los miembros del grupo pueden entrar y trabajar.

**Pregunta 3**

✅ **Respuesta correcta: A**

**Justificación**

`grep -c` cuenta las líneas que coinciden con el patrón y muestra el número total.

Si hay 1.247 intentos fallidos, el comando mostrará `1247`.

La opción `-v` invierte la búsqueda y `tail -f` monitorea en vivo.

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

`tail -f` se queda "siguiendo" el archivo.

Cada línea nueva que se agrega aparece en pantalla al instante.

Se detiene con `Ctrl + C`.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

`gid` significa **group ID**.

`gid=1001(ventas)` indica que el grupo principal de ana es `ventas`.

El comando `id` muestra identidad y pertenencia a grupos.

**Pregunta 6**

✅ **Respuesta correcta: A**

**Justificación**

`ps aux` muestra todos los procesos del sistema con su PID, usuario y consumo de recursos.

`ls -l` lista archivos, `grep` busca texto y `pwd` muestra la carpeta actual.

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

El `600` significa lectura y escritura solo para el dueño.

El grupo y el resto tienen `0` (ningún permiso).

Como el archivo fue creado por root, solo root puede leerlo.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

En Debian y Ubuntu, el log de autenticación es `/var/log/auth.log`.

En distribuciones Red Hat, el equivalente es `/var/log/secure`.

`/var/log/syslog` contiene eventos generales y `/etc/passwd` es el catálogo de usuarios.

**Pregunta 9**

✅ **Respuesta correcta: A**

**Justificación**

`ps aux | grep sshd` toma la salida de `ps aux` y la filtra para mostrar solo las líneas que contienen `sshd`.

Es la combinación clásica de pipes que usa un analista para buscar procesos.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

1.247 intentos fallidos desde una misma IP en 15 minutos, probando usuarios comunes, es la firma clásica de un **ataque de fuerza bruta** contra SSH.

Lo más grave es el `Accepted password for root` final:

el atacante logró acceder al sistema.

Como analista SOC deberías:

- Bloquear la IP origen.

- Cambiar la contraseña de root y revocar la sesión activa.

- Verificar qué hizo el atacante después del acceso.

- Revisar los logs de sesión y los procesos sospechosos.

- Escalar el incidente según el procedimiento de tu organización.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Completaste el laboratorio y ya te mueves en la terminal con confianza. |
| **8–9**                  | 🟢 **Muy buen nivel.** Solo necesitas practicar un poco más los permisos y grep. |
| **6–7**                  | 🟡 **Buen progreso.** Repite los laboratorios 2 y 3 hasta dominarlos.      |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a repasar los módulos de usuarios, permisos y logs. |
| **0–3**                  | 🔴 **Es recomendable repetir el laboratorio completo.** La práctica es la clave para dominar Linux. |
