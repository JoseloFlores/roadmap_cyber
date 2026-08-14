**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Módulo 14 – Introducción a Linux y la Terminal (CLI)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ IP Públicas y Privadas

- ✅ Modelo OSI

- ✅ Modelo TCP/IP

- ✅ Máscaras y Subredes

- ✅ Gateway y NAT

- ✅ TCP y UDP

- ✅ Puertos

- ✅ DNS

- ✅ DHCP

- ✅ HTTP y HTTPS

Con esto terminamos la etapa de **redes** de tu formación.

Ahora comienza una nueva etapa: la de **administración de sistemas**.

Y para un Analista SOC, esa etapa tiene un nombre propio: **Linux**.

¿Por qué Linux?

Porque casi todos los servidores del mundo corren sobre Linux.

Porque las herramientas de seguridad que usarás todos los días (Wireshark, Suricata, Wazuh, Splunk) se ejecutan nativamente sobre Linux.

Porque los logs que revisarás en tu trabajo diario se generan, se almacenan y se analizan en servidores Linux.

El objetivo de esta semana es simple pero fundamental:

**Moverte con soltura en la terminal (CLI) sin depender de la interfaz gráfica.**

Bienvenido a la semana que cambiará la forma en que trabajas.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es Linux y qué es una distribución.

- Explicar por qué un Analista SOC trabaja con Linux todos los días.

- Diferenciar entre terminal, shell y CLI.

- Entender la estructura de un comando de Linux.

- Utilizar `man` y `--help` para obtener ayuda.

- Navegar por el sistema de archivos con `pwd`, `ls` y `cd`.

- Crear, copiar, mover y eliminar archivos y carpetas.

- Ver el contenido de archivos con `cat`, `head`, `tail` y `less`.

- Reconocer la diferencia entre usuario normal y `root`.

- Conocer los atajos de terminal que ahorran tiempo.

**1. ¿Qué es Linux?**

Linux es un **sistema operativo**.

Pero no es cualquier sistema operativo.

Linux es, técnicamente, un **kernel**.

Un kernel es el núcleo del sistema operativo.

Es la parte que conecta el hardware con el software.

Imagina un edificio.

El kernel serían los cimientos y la estructura interna.

Sin ellos, el edificio no se sostiene.

**GNU/Linux**

Cuando hablamos de "Linux" en la práctica, casi siempre nos referimos a **GNU/Linux**.

¿Por qué?

Porque el kernel de Linux se combina con herramientas desarrolladas por el proyecto **GNU**.

Ese conjunto completo es lo que usamos a diario.

Por eso verás escritas ambas cosas:

- Linux (el kernel).

- GNU/Linux (el sistema operativo completo).

**Sistemas operativos libres**

Linux es **software libre** y de **código abierto**.

Esto significa:

- El código fuente es público.

- Cualquiera puede estudiarlo.

- Cualquiera puede modificarlo.

- Cualquiera puede distribuirlo.

Esta característica lo hace muy atractivo para la seguridad.

Porque puedes auditar exactamente qué hace tu sistema.

**¿Dónde se usa Linux?**

Linux está en todas partes, aunque no lo veas.

Algunos ejemplos:

- **Servidores web:** la mayoría de los sitios de Internet corren sobre Linux.

- **Bases de datos:** la mayoría se ejecutan en servidores Linux.

- **Cloud:** los servicios en la nube como AWS y Azure usan Linux masivamente.

- **Smartphones:** el sistema operativo Android está basado en Linux.

- **Dispositivos IoT:** routers, televisores y dispositivos inteligentes.

- **Supercomputadoras:** las más potentes del mundo usan Linux.

- **Herramientas de seguridad:** Wireshark, Suricata, Nmap, Metasploit y más.

**Dato que te servirá como analista**

Si aprendes a manejar Linux, podrás trabajar en cualquier tipo de infraestructura.

Porque Linux es el "idioma común" de los servidores modernos.

**2. ¿Por qué un Analista SOC necesita Linux?**

Un Analista SOC Nivel 1 debe vivir en Linux.

No es un "extra" de la carrera.

Es una **herramienta principal de trabajo**.

Estas son las razones más importantes:

**Razón 1 – Los servidores corporativos corren sobre Linux**

Casi todos los servidores web, de correo, de bases de datos y de aplicaciones usan Linux.

Si la empresa sufre un incidente, el análisis se hará sobre servidores Linux.

**Razón 2 – Los logs son archivos de texto plano**

En Linux, los logs son simplemente archivos de texto.

Y los analistas trabajan con texto todo el día.

Verás archivos en `/var/log/` que puedes abrir y leer con comandos como `cat`, `tail` o `less`.

**Razón 3 – Las herramientas de seguridad corren sobre Linux**

La mayoría de las herramientas de un SOC funcionan mejor en Linux.

Ejemplos:

- **Wireshark:** análisis de tráfico.

- **Suricata:** detección de intrusos (IDS/IPS).

- **Wazuh:** monitoreo y SIEM open source.

- **Splunk:** la plataforma de análisis de logs más usada en SOCs.

- **Zeek:** análisis de red.

**Razón 4 – Kali Linux para el laboratorio**

Kali Linux es una distribución enfocada en seguridad ofensiva.

Trae instaladas herramientas como Nmap, Metasploit y Wireshark.

Es ideal para practicar en un laboratorio controlado.

**Razón 5 – La mayoría de los SIEM y EDR corren sobre Linux**

Las plataformas de seguridad que recopilan eventos se despliegan casi siempre en servidores Linux.

El analista debe poder:

- Revisar procesos con `ps`.

- Leer logs con `tail` y `grep`.

- Comprobar el estado del sistema con `free` y `df`.

- Moverse por el sistema con `ls` y `cd`.

Todo eso se hace desde la terminal.

**Analogía rápida**

Linux es como el taller donde se hace la mecánica del SOC.

La terminal es el banco de trabajo.

Y los comandos son las herramientas del taller.

Sin saber usar esas herramientas, no puedes reparar nada.

**3. Distribuciones principales**

Linux no es un único sistema operativo.

Existen muchas versiones llamadas **distribuciones** (o "distros").

**Analogía del motor**

Imagina que Linux es el **motor** de un auto.

La distribución es el **auto completo** con sus accesorios.

Con el mismo motor puedes tener:

- Un auto familiar.

- Un auto deportivo.

- Una camioneta de trabajo.

Todos usan el mismo motor, pero cada uno está armado para un propósito.

Las principales distribuciones para un Analista SOC:

| **Distribución**        | **Uso principal**                              | **Por qué importa**                              |
|-------------------------|------------------------------------------------|--------------------------------------------------|
| Ubuntu                  | Servidores y uso general                        | La más usada; gran comunidad y documentación.    |
| Debian                  | Servidores estables                            | Base de Ubuntu; muy estable y confiable.         |
| Kali Linux              | Seguridad ofensiva y pentesting                 | Trae herramientas de seguridad preinstaladas.    |
| Parrot OS               | Seguridad y privacidad                         | Alternativa a Kali con buenas herramientas.      |
| CentOS / RHEL           | Empresas y servidores corporativos             | Estandar en muchas empresas grandes.             |
| AlmaLinux               | Sucesor de CentOS para empresas                | Compatible con RHEL sin costo de licencia.       |
| Alpine                  | Contenedores (Docker)                          | Muy liviana; se usa en casi todos los contenedores. |

**Ubuntu y Debian**

Son las más amigables para empezar.

Las recomiendo para practicar desde cero.

**Kali y Parrot**

Enfocadas en seguridad.

Perfectas para tu laboratorio de práctica.

**CentOS, RHEL y AlmaLinux**

Son las que encontrarás en el mundo corporativo.

Si trabajas en un SOC empresarial, es muy probable que veas alguna de estas.

**Alpine**

Extremadamente pequeña.

Se usa casi exclusivamente para contenedores Docker.

**Regla práctica**

Elige una distribución para aprender, por ejemplo Ubuntu.

Los comandos básicos son los mismos en casi todas.

Si sabes navegar en Ubuntu, te adaptarás rápido a las demás.

**4. Terminal, shell y CLI**

Estos tres términos se usan mucho.

Y es importante diferenciarlos.

**La terminal**

La **terminal** es el programa que te permite interactuar con el sistema escribiendo texto.

Es como la "ventana" donde escribes.

**La shell**

La **shell** es el intérprete de comandos.

Es el programa que lee lo que escribes y lo ejecuta.

La shell más común en Linux es **bash** (Bourne Again Shell).

**El CLI**

CLI significa **Command Line Interface** (Interfaz de Línea de Comandos).

Es la forma de trabajar escribiendo comandos, en lugar de hacer clic.

**GUI vs CLI**

GUI significa **Graphical User Interface** (Interfaz Gráfica).

Son las ventanas, botones y menús que todos conocemos.

| **Característica** | **GUI**                  | **CLI**                       |
|--------------------|--------------------------|-------------------------------|
| Interacción        | Clics y ventanas         | Escribir comandos             |
| Velocidad          | Más lenta para tareas    | Más rápida                    |
| Automatización     | Difícil                  | Fácil (scripts)               |
| Recursos           | Consume más              | Consume muy poco              |
| Uso en servidores  | Casi nulo                | El estándar                   |
| Aprendizaje        | Intuitiva                | Requiere práctica             |

**¿Por qué el SOC usa CLI?**

Porque los servidores no tienen pantalla ni mouse.

Se administran solo por terminal, muchas veces de forma remota vía SSH.

Y porque automatizar con scripts solo es posible desde la línea de comandos.

**El prompt**

Cuando abres la terminal, ves algo como:

`usuario@hostname:~$`

Eso se llama **prompt**.

Te está indicando:

- Qué usuario eres.

- En qué equipo estás.

- En qué carpeta te encuentras.

El símbolo final es muy importante:

- `$` → Eres un **usuario normal**.

- `#` → Eres **root** (administrador).

Verás esto con más detalle en la sección de privilegios.

**5. Estructura de un comando**

Un comando de Linux tiene una estructura muy ordenada.

Normalmente se compone de tres partes:

1. El **comando** en sí.

2. Las **opciones** (también llamadas flags).

3. Los **argumentos**.

**Ejemplo:**

`ls -l /home`

- `ls` → el comando (listar archivos).

- `-l` → la opción (formato largo, con detalles).

- `/home` → el argumento (qué carpeta listar).

**Otro ejemplo:**

`cd /etc`

- `cd` → el comando (cambiar de directorio).

- `/etc` → el argumento (a dónde ir).

**Opciones cortas y largas**

Las opciones pueden escribirse de dos formas:

- Cortas: `-l`

- Largas: `--long`

Ejemplo:

`ls --all`

Es lo mismo que:

`ls -a`

Ambas muestran archivos ocultos.

**Puedes combinar opciones**

`ls -la`

Combina `-l` (formato largo) y `-a` (todo, incluidos ocultos).

Es uno de los comandos que más usarás.

**Espacios importantes**

Los comandos se separan con espacios.

`cd /etc` es diferente de `cd/etc`.

Siempre respeta los espacios.

**No todo es un comando**

Si escribes algo que no existe como comando, verás un error:

`command not found`

No es grave.

Es la forma del sistema de decir "eso no existe".

**6. Obtener ayuda**

No necesitas memorizar todas las opciones de todos los comandos.

Nadie lo hace.

Lo importante es saber **cómo buscar ayuda**.

**Comando 1 – man**

`man` muestra el manual del comando.

Ejemplo:

`man ls`

Verás la documentación completa de `ls`.

Para salir del manual, presiona:

`q`

**Comando 2 – --help**

La mayoría de los comandos aceptan:

`comando --help`

Ejemplo:

`ls --help`

Muestra un resumen de opciones, más corto que `man`.

**Comando 3 – info**

También existe:

`info comando`

Es otro formato de documentación.

Lo usarás menos, pero es bueno saber que existe.

**Analogía**

`man` es como leer el manual completo del electrodoméstico.

`--help` es como la tarjeta rápida que viene en la caja.

Para el trabajo diario, casi siempre alcanza con `--help`.

**Consejo de instructor**

Antes de preguntar "¿cómo se hace X?":

- Prueba `man comando`.

- Prueba `comando --help`.

El 90% de las respuestas están ahí.

**7. Navegar por el sistema de archivos**

En Linux, todo es un archivo.

Carpetas, textos, configuraciones, incluso dispositivos.

El sistema de archivos es una estructura de carpetas que empieza en `/`.

**pwd**

`pwd` significa **print working directory**.

Te dice en qué carpeta estás.

Ejemplo:

`pwd`

Salida:

`/home/usuario`

Lo usarás decenas de veces al día.

Es el "¿dónde estoy?" de la terminal.

**ls**

`ls` significa **list**.

Muestra los archivos y carpetas del directorio actual.

Ejemplo:

`ls`

**ls con opciones**

`ls -l` → formato largo, con permisos, dueño, tamaño y fecha.

`ls -a` → muestra también archivos ocultos (los que empiezan con punto).

`ls -la` → la combinación más usada.

Ejemplo:

`ls -la`

Verás entradas como:

`.`

`..`

`archivo.txt`

`.config`

Las carpetas `.` y `..` son especiales:

- `.` → el directorio actual.

- `..` → el directorio padre.

**cd**

`cd` significa **change directory**.

Cambia de carpeta.

Ejemplo:

`cd /etc`

Te mueves a la carpeta `/etc`.

**cd con argumentos especiales**

`cd ..` → sube una carpeta (al directorio padre).

`cd ~` → va a la carpeta personal del usuario (home).

`cd /` → va a la raíz del sistema.

`cd -` → vuelve a la carpeta anterior.

**Ejemplo de navegación**

Estás en:

`/home/usuario`

Escribes:

`cd /etc`

Ahora estás en:

`/etc`

Escribes:

`cd ..`

Ahora estás en:

`/`

**Analogía**

Piensa en la terminal como un explorador de archivos sin clics.

`pwd` te dice en qué sala estás.

`ls` te muestra qué hay en la sala.

`cd` te lleva a otra sala.

**Carpetas importantes que debes conocer**

| **Carpeta** | **Qué contiene**                                          |
|-------------|-----------------------------------------------------------|
| `/`         | La raíz del sistema de archivos.                          |
| `/home`     | Las carpetas personales de los usuarios.                  |
| `/etc`      | Los archivos de configuración del sistema.                |
| `/var`      | Datos variables, incluidos los logs.                      |
| `/var/log`  | Los logs del sistema (oro para un SOC).                   |
| `/tmp`      | Archivos temporales.                                      |
| `/bin`      | Comandos esenciales del sistema.                          |
| `/usr`      | Programas y aplicaciones del usuario.                     |
| `/root`     | La carpeta personal del usuario root.                     |

Como analista, vivirás mucho en `/var/log` y `/etc`.

**8. Crear y eliminar archivos y carpetas**

**mkdir**

`mkdir` significa **make directory**.

Crea una carpeta.

Ejemplo:

`mkdir proyectos`

**Crear varias carpetas**

`mkdir proyectos informes respaldos`

Crea las tres carpetas.

**mkdir con estructura**

`mkdir -p proyecto/subcarpeta`

Crea la carpeta y su subcarpeta aunque la intermedia no exista.

**touch**

`touch` crea un archivo vacío.

Ejemplo:

`touch notas.txt`

Si el archivo ya existe, actualiza su fecha de modificación.

**¿Para qué usar touch?**

- Crear archivos de prueba.

- Crear archivos de logs vacíos.

- Forzar la actualización de fechas.

**cp**

`cp` significa **copy**.

Copia archivos.

Ejemplo:

`cp notas.txt copia.txt`

Copia `notas.txt` a `copia.txt`.

**Copiar una carpeta**

`cp -r carpeta carpeta_copia`

La opción `-r` copia de forma recursiva (todo el contenido).

**mv**

`mv` significa **move**.

Mueve o renombra.

**Mover**

`mv notas.txt /home/usuario/Documentos`

Mueve el archivo a otra carpeta.

**Renombrar**

`mv notas.txt apuntes.txt`

Cambia el nombre del archivo.

**Analogía de mv**

`mv` es como agarrar un archivo y llevarlo a otro lugar.

O como cambiarle la etiqueta.

**rm**

`rm` significa **remove**.

Elimina archivos.

Ejemplo:

`rm notas.txt`

**Cuidado**

`rm` elimina de forma **permanente**.

No va a la papelera de reciclaje.

No hay "deshacer".

Sé siempre muy cuidadoso con `rm`.

**Eliminar una carpeta**

`rm -r carpeta`

Elimina la carpeta con todo su contenido.

**rmdir**

`rmdir` elimina carpetas **vacías**.

Ejemplo:

`rmdir carpeta_vacia`

Si la carpeta tiene contenido, fallará.

Ahí es cuando necesitas `rm -r`.

**Regla de seguridad en el SOC**

Antes de eliminar cualquier archivo:

- Verifica que es el correcto.

- Asegúrate de que no es un log que necesites para una investigación.

- Confirma que no es evidencia de un incidente.

En un SOC, borrar evidencia puede arruinar toda una investigación.

**9. Ver contenido de archivos**

Los logs son archivos de texto.

Por eso, saber leer archivos es la habilidad más importante del analista.

**cat**

`cat` muestra el contenido completo de un archivo.

Ejemplo:

`cat /etc/hostname`

**Cuándo usar cat**

Cuando el archivo es corto.

**Problema de cat**

Si el archivo es muy largo, la información pasa rápido por la pantalla.

No es ideal para logs grandes.

**head**

`head` muestra las **primeras** líneas del archivo.

Ejemplo:

`head /var/log/syslog`

Por defecto muestra las 10 primeras líneas.

**Con número de líneas**

`head -n 20 /var/log/syslog`

Muestra las primeras 20 líneas.

**tail**

`tail` muestra las **últimas** líneas del archivo.

Ejemplo:

`tail /var/log/syslog`

Es el comando más importante para un SOC.

**¿Por qué tail es tan importante?**

Porque los logs nuevos se escriben al final del archivo.

`tail` te muestra lo más reciente.

**tail con número de líneas**

`tail -n 20 /var/log/syslog`

Muestra las últimas 20 líneas.

**tail -f (seguir)**

`tail -f /var/log/syslog`

Muestra las últimas líneas y se queda "siguiendo" el archivo.

A medida que llegan líneas nuevas, se muestran en tiempo real.

Es como ver "en vivo" lo que está pasando en el sistema.

Para salir de `tail -f`:

`Ctrl+C`

**less**

`less` muestra el archivo de forma paginada.

Ejemplo:

`less /var/log/syslog`

Puedes navegar:

- Flecha arriba / abajo → moverte.

- `Espacio` → bajar una página.

- `/texto` → buscar una palabra.

- `q` → salir.

**¿Cuál usar?**

| **Comando** | **Cuándo usarlo**                                       |
|-------------|---------------------------------------------------------|
| `cat`       | Archivo corto, leerlo completo.                         |
| `head`      | Ver solo el inicio de un archivo.                       |
| `tail`      | Ver el final (lo más reciente).                         |
| `tail -f`   | Seguir un log en tiempo real.                           |
| `less`      | Archivos largos, con navegación y búsqueda.             |

**Analogía**

`cat` es abrir el cuaderno y leerlo todo de corrido.

`tail` es leer solo la última página, la que se escribió recién.

`less` es leer con calma, poder volver atrás y buscar información.

**10. Usuario y privilegios**

Linux es un sistema multiusuario.

Varios usuarios pueden existir en el mismo equipo.

Cada usuario tiene permisos distintos.

**whoami**

`whoami` te dice qué usuario eres.

Ejemplo:

`whoami`

Salida:

`usuario`

**id**

`id` muestra información detallada de tu usuario.

Ejemplo:

`id`

Muestra:

- Tu usuario.

- Tu grupo.

- Tus identificadores numéricos.

**root**

El usuario `root` es el **administrador del sistema**.

Tiene control total:

- Puede modificar cualquier archivo.

- Puede instalar programas.

- Puede gestionar usuarios.

- Puede ver todos los logs.

Por eso, el prompt de root termina en `#`.

**Usuario normal**

El usuario normal tiene limitaciones.

No puede modificar archivos del sistema.

Su prompt termina en `$`.

**¿Por qué esta separación?**

Por seguridad.

Si cometes un error como usuario normal, el daño es limitado.

Si cometes un error como root, puedes romper todo el sistema.

**sudo**

`sudo` significa **superuser do**.

Permite ejecutar un comando con privilegios de administrador.

Ejemplo:

`sudo apt update`

Ejecuta `apt update` con permisos de root.

**Analogía del sudo**

`sudo` es como la **tarjeta de administrador** de un edificio.

Todos los empleados tienen su credencial normal.

Solo quien tiene la tarjeta de administrador puede entrar a las salas restringidas.

Y la usa solo cuando es necesario.

No camina con la tarjeta pegada a la frente todo el día.

**Reglas de sudo**

- Usa `sudo` solo cuando el comando lo necesite.

- No uses `sudo` para todo.

- Cuando uses `sudo`, verifica bien lo que vas a ejecutar.

**Ejemplos con sudo**

`sudo systemctl restart ssh`

`sudo apt install wireshark`

`sudo cat /var/log/auth.log`

**Ojo con root**

Muchas guías te dicen "trabaja como root".

En tu laboratorio de práctica está bien.

En un entorno real de trabajo, es una mala práctica.

Trabaja como usuario normal.

Usa `sudo` solo para lo necesario.

**11. Información del sistema**

Como analista, necesitarás conocer el estado del sistema.

Estos comandos te dan información valiosa.

**uname**

`uname` muestra información del sistema.

Ejemplo:

`uname -a`

Muestra:

- El nombre del sistema.

- La versión del kernel.

- La arquitectura.

- La fecha.

**hostname**

`hostname` muestra el nombre del equipo.

Ejemplo:

`hostname`

Salida:

`servidor-web-01`

Es muy útil para identificar en qué máquina estás.

**date**

`date` muestra la fecha y hora actuales.

Ejemplo:

`date`

**uptime**

`uptime` muestra cuánto tiempo lleva encendido el sistema.

También muestra la carga del sistema.

Ejemplo:

`uptime`

Si un servidor se reinició sin permiso, `uptime` lo delata.

**who**

`who` muestra qué usuarios están conectados.

Ejemplo:

`who`

En un SOC, es útil para ver quién tiene sesión activa en el servidor.

**free**

`free` muestra el uso de memoria.

Ejemplo:

`free -h`

La opción `-h` muestra los valores en formato legible (human).

Verás:

- Memoria total.

- Memoria usada.

- Memoria disponible.

**df**

`df` muestra el uso del espacio en disco.

Ejemplo:

`df -h`

Verás cada partición y cuánto espacio libre tiene.

**¿Por qué importa esto en un SOC?**

Porque los logs se guardan en disco.

Si el disco se llena, el sistema puede dejar de registrar eventos.

Y sin logs, un SOC queda "ciego".

Por eso:

- `free -h` → memoria.

- `df -h` → disco.

- `uptime` → reinicios o caídas.

Son tus primeras comprobaciones de diagnóstico.

**12. Atajos de terminal que ahorran tiempo**

La terminal tiene atajos que te harán trabajar más rápido.

Aprenderlos desde el inicio marca la diferencia.

**Tab – Autocompletar**

Presiona `Tab` para autocompletar comandos y nombres de archivos.

Ejemplo:

`cd /e[TAB]`

Se convierte en:

`cd /etc`

Si hay varias opciones, presiona `Tab` dos veces para verlas.

**Las flechas del teclado**

- Flecha arriba → comando anterior.

- Flecha abajo → siguiente comando.

No necesitas reescribir comandos largos.

La terminal recuerda el historial.

**Ctrl+C – Cancelar**

Cancela el comando que se está ejecutando.

Ejemplo:

`tail -f /var/log/syslog`

Para salir:

`Ctrl+C`

**Ctrl+L – Limpiar pantalla**

Limpia la pantalla de la terminal.

Es equivalente al comando `clear`.

**Ctrl+A – Inicio de línea**

Mueve el cursor al principio de la línea.

**Ctrl+E – Fin de línea**

Mueve el cursor al final de la línea.

**Ctrl+D – Salir de la terminal**

Cierra la sesión de la terminal.

Equivale al comando `exit`.

**Ctrl+W – Borrar palabra**

Borra la palabra anterior al cursor.

**Ctrl+U – Borrar toda la línea**

Borra todo lo que hay escrito en la línea.

**Tabla de atajos**

| **Atajo**  | **Función**                                     |
|------------|-------------------------------------------------|
| `Tab`      | Autocompletar comandos y rutas.                 |
| Flecha ↑   | Comando anterior del historial.                 |
| Flecha ↓   | Comando siguiente del historial.                |
| `Ctrl+C`   | Cancelar el comando actual.                     |
| `Ctrl+L`   | Limpiar la pantalla.                            |
| `Ctrl+A`   | Ir al inicio de la línea.                       |
| `Ctrl+E`   | Ir al final de la línea.                        |
| `Ctrl+D`   | Cerrar la sesión de terminal.                   |
| `Ctrl+W`   | Borrar la palabra anterior.                     |
| `Ctrl+U`   | Borrar toda la línea.                           |

**El más importante para el SOC**

`Ctrl+C`.

Porque `tail -f` y otras herramientas se quedan en ejecución.

Y necesitas saber detenerlas con seguridad.

**13. Mini recorrido guiado**

Vamos a practicar.

Enciende tu máquina virtual con Linux.

Abre la terminal.

**Paso 1 – ¿Dónde estoy?**

`pwd`

Verás algo como:

`/home/tuusuario`

**Paso 2 – ¿Qué hay aquí?**

`ls`

Verás las carpetas de tu usuario.

**Paso 3 – Veamos todo, incluso lo oculto**

`ls -la`

**Paso 4 – Vamos a la carpeta de configuración**

`cd /etc`

**Paso 5 – ¿Qué hay en /etc?**

`ls`

Verás archivos y carpetas de configuración.

**Paso 6 – ¿Cómo se llama este equipo?**

`cat /etc/hostname`

Verás el nombre de tu máquina.

**Paso 7 – Volvamos a casa**

`cd ~`

**Paso 8 – Primer acercamiento a los logs**

`cd /var/log`

**Paso 9 – ¿Qué hay en los logs?**

`ls`

Verás archivos como `syslog`, `auth.log` o `kern.log`.

**Paso 10 – Lee las últimas líneas**

`tail /var/log/syslog`

Verás eventos recientes del sistema.

**Paso 11 – Sigue el log en vivo**

`tail -f /var/log/syslog`

El archivo se mostrará en tiempo real.

Para salir:

`Ctrl+C`

**Paso 12 – Ahora como analista**

`grep` no es parte de este módulo en detalle, pero pruébalo:

`grep -i error /var/log/syslog`

Verás solo las líneas que contienen "error".

Es tu primer vistazo a cómo se filtra información de los logs.

**¿Qué acabas de hacer?**

Navegaste por el sistema de archivos.

Viste configuración.

Leíste logs.

Y filtramos errores.

Eso es, literalmente, el trabajo básico de un Analista SOC.

**14. Aplicación práctica en un SOC**

¿Por qué el analista debe "vivir" en la terminal?

Porque cada tarea diaria se resuelve con comandos.

**Tarea 1 – Revisar logs**

El analista revisa eventos con:

`tail -f /var/log/auth.log`

Es como estar observando en vivo los intentos de acceso.

**Tarea 2 – Comprobar el estado del sistema**

Antes de investigar un incidente, revisa el estado:

`uptime`

`free -h`

`df -h`

Si el servidor está saturado o sin espacio, eso afecta la interpretación de los eventos.

**Tarea 3 – Identificar procesos sospechosos**

Con `ps` puedes listar procesos.

Ejemplo:

`ps aux`

Verás todos los procesos en ejecución.

Como analista, aprenderás a buscar procesos anómalos.

**Tarea 4 – Responder un incidente rápido**

Imagina una alerta de fuerza bruta SSH.

El analista:

1. Abre el log: `tail /var/log/auth.log`.

2. Filtra los intentos fallidos.

3. Identifica la IP origen.

4. Verifica si algún acceso fue exitoso.

5. Toma medidas de contención.

Todo eso desde la terminal.

**Tarea 5 – Comunicarse con servidores remotos**

Cuando necesites entrar a otro servidor:

`ssh usuario@servidor`

Este comando aparecerá en módulos futuros de Linux.

**La terminal como extensión de ti**

Un analista que domina la terminal:

- Revisa logs en segundos.

- Ejecuta diagnósticos sin esperar ayuda.

- Responde incidentes con velocidad.

Un analista que depende de la interfaz gráfica:

- Pierde tiempo haciendo clic.

- Depende de herramientas visuales.

- No puede trabajar en servidores sin escritorio.

**La regla del SOC**

En un SOC, el tiempo de respuesta importa.

Y la terminal es la forma más rápida de trabajar.

**15. Lo que esperan de un Analista SOC Nivel 1**

Como analista Nivel 1, deberías poder responder estas preguntas:

- ¿Qué es Linux y qué es un kernel?

- ¿Por qué se dice GNU/Linux?

- ¿Qué distribución usarías para un laboratorio de seguridad?

- ¿Cuál es la diferencia entre CLI y GUI?

- ¿Qué significa el `$` y el `#` en el prompt?

- ¿Cómo obtengo ayuda sobre un comando?

- ¿Qué hace `pwd` y por qué se usa tanto?

- ¿Cómo cambio de directorio con `cd`?

- ¿Qué muestra `ls -la`?

- ¿Cuál es la diferencia entre `cat` y `tail`?

- ¿Cómo sigo un log en tiempo real?

- ¿Qué hace `sudo` y cuándo usarlo?

- ¿Cuál es la diferencia entre usuario normal y `root`?

- ¿Cómo cancelo un comando en ejecución?

- ¿Cuál es el directorio de logs del sistema?

Ese es el nivel de base que se espera al terminar esta semana.

No necesitas ser un experto.

Necesitas moverte sin miedo por la terminal.

**Lo que NO se espera todavía**

No se espera que domines:

- Permisos avanzados.

- Configuración de red en Linux.

- Servicios y procesos en profundidad.

- Scripts avanzados.

Eso llegará en módulos futuros.

Hoy el objetivo es la base.

**16. Resumen**

**Linux**

- Es un sistema operativo.

- Su núcleo se llama **kernel**.

- La combinación con las herramientas GNU se llama **GNU/Linux**.

- Es libre y de código abierto.

- Se usa en servidores, IoT, supercomputadoras y Android.

**Por qué es importante para un SOC**

- Los servidores corporativos corren Linux.

- Los logs son archivos de texto.

- Las herramientas de seguridad corren Linux.

- La mayoría de los SIEM y EDR corren Linux.

**Terminal, shell y CLI**

- La terminal es la ventana de texto.

- La shell interpreta los comandos (la más común es bash).

- CLI es la forma de trabajar con comandos.

**Comandos clave**

| **Comando** | **Función**                                   |
|-------------|-----------------------------------------------|
| `pwd`       | Muestra la carpeta actual.                    |
| `ls`        | Lista archivos y carpetas.                    |
| `ls -la`    | Lista todo en formato detallado.              |
| `cd`        | Cambia de carpeta.                            |
| `mkdir`     | Crea una carpeta.                             |
| `touch`     | Crea un archivo vacío.                        |
| `cp`        | Copia archivos.                               |
| `mv`        | Mueve o renombra.                             |
| `rm`        | Elimina archivos (¡con cuidado!).             |
| `cat`       | Muestra el contenido completo de un archivo.  |
| `head`      | Muestra las primeras líneas.                  |
| `tail`      | Muestra las últimas líneas.                   |
| `tail -f`   | Sigue el archivo en tiempo real.              |
| `less`      | Lee archivos largos con navegación.           |
| `whoami`    | Muestra tu usuario.                           |
| `id`        | Muestra información de tu usuario.            |
| `sudo`      | Ejecuta un comando como administrador.        |
| `uname -a`  | Muestra información del sistema.              |
| `hostname`  | Muestra el nombre del equipo.                 |
| `date`      | Muestra fecha y hora.                         |
| `uptime`    | Muestra tiempo encendido y carga.             |
| `who`       | Muestra usuarios conectados.                  |
| `free -h`   | Muestra el uso de memoria.                    |
| `df -h`     | Muestra el uso del disco.                     |

**Usuario y privilegios**

- Usuario normal: prompt `$`.

- Root: prompt `#`.

- `sudo` permite ejecutar comandos como administrador.

- Usa `sudo` solo cuando sea necesario.

**Atajos clave**

- `Tab` → autocompletar.

- `Ctrl+C` → cancelar.

- `Ctrl+L` → limpiar pantalla.

- Flechas → historial.

**Directorio de logs**

- `/var/log` → los logs del sistema.

- `tail` y `tail -f` → tus mejores amigos en el SOC.

**🧠 Conceptos clave para memorizar**

| **Concepto**    | **Debes recordar**                                              |
|-----------------|-----------------------------------------------------------------|
| Kernel          | El núcleo del sistema operativo; conecta hardware y software.   |
| Distribución    | Una versión de Linux armada para un propósito (Ubuntu, Kali...).|
| GNU/Linux       | El kernel Linux + las herramientas GNU.                         |
| Shell           | El intérprete de comandos.                                      |
| bash            | La shell más común en Linux.                                    |
| CLI             | Interfaz de línea de comandos.                                  |
| GUI             | Interfaz gráfica (ventanas y clics).                            |
| Prompt `$`      | Indica usuario normal.                                          |
| Prompt `#`      | Indica usuario root.                                            |
| sudo            | Ejecutar un comando con privilegios de administrador.           |
| man             | Muestra el manual de un comando.                                |
| pwd             | Muestra el directorio actual ("¿dónde estoy?").                 |
| ls              | Lista archivos y carpetas.                                      |
| cd              | Cambia de directorio.                                           |
| cat             | Muestra el contenido completo de un archivo.                    |
| tail            | Muestra las últimas líneas (lo más reciente).                   |
| tail -f         | Sigue el log en tiempo real.                                    |
| /var/log        | Directorio de logs del sistema.                                 |
| Ctrl+C          | Cancela el comando en ejecución.                                |
| Tab             | Autocompleta comandos y rutas.                                  |

**🎓 Consejo como tu instructor de SOC**

No memorices los comandos de memoria.

Entiéndelos.

Si entiendes que `ls` lista contenido y `cd` cambia de carpeta, no necesitas memorizar nada.

El comando se convierte en una herramienta natural.

**El secreto del Tab**

El `Tab` y el historial con flechas son tus mejores aliados.

Ningún analista escribe comandos larguísimos a mano.

Todos autocompletan.

Todos usan el historial.

Todos se equivocan.

**Equivocarse es parte del aprendizaje**

Vas a escribir mal comandos.

Vas a ver mensajes de error.

Vas a borrar archivos que no querías borrar.

Y está bien.

Así se aprende.

Lo importante es que entiendas por qué falló y no repetir el error.

**La terminal es tu herramienta principal**

No es una moda.

No es un capricho de los administradores.

Es la herramienta principal del analista.

Cada día de tu carrera en un SOC vas a:

- Abrir una terminal.

- Leer un log con `tail`.

- Buscar información con `less`.

- Ejecutar diagnósticos.

Si dominas esta base, todo lo demás (permisos, redes, servicios, scripts) será más fácil.

Si no dominas esta base, cada módulo futuro será una batalla.

**Una frase para llevar**

"El Analista SOC no usa Linux porque quiere.

Lo usa porque es donde ocurre el trabajo real."

Practica esta semana.

Abre la terminal todos los días.

Crea carpetas.

Borra archivos.

Lee logs.

Comete errores.

Y en una semana verás la diferencia.

Bienvenido al mundo de la línea de comandos.

---

**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Evaluación – Módulo 14: Introducción a Linux y la Terminal (CLI)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Este examen está diseñado con el nivel de dificultad de una entrevista técnica para un **Analista SOC Nivel 1**. Encontrarás preguntas teóricas y casos prácticos similares a los que enfrentarás trabajando desde la terminal de un servidor Linux.

**Pregunta 1**

¿Qué es exactamente **Linux** desde un punto de vista técnico?

**A)** Un navegador web.

**B)** Un kernel (núcleo) de sistema operativo.

**C)** Una base de datos.

**D)** Un protocolo de red.

**Pregunta 2**

¿Cuál es la principal razón por la que un **Analista SOC** necesita Linux?

**A)** Porque las interfaces gráficas son más rápidas.

**B)** Porque los servidores, los logs y las herramientas de seguridad que se analizan en un SOC corren mayoritariamente sobre Linux.

**C)** Porque Linux es el único sistema que se conecta a Internet.

**D)** Porque es obligatorio para jugar videojuegos.

**Pregunta 3**

¿Cuál es la diferencia fundamental entre **CLI** y **GUI**?

**A)** CLI usa el mouse y GUI usa el teclado.

**B)** CLI se controla escribiendo comandos de texto, mientras que GUI se controla con elementos gráficos como ventanas y botones.

**C)** No existe diferencia.

**D)** CLI solo funciona en Windows.

**Pregunta 4**

Ejecutas el comando `pwd` en la terminal. ¿Qué obtendrás?

**A)** El nombre del usuario actual.

**B)** La contraseña del usuario.

**C)** El directorio de trabajo actual (en qué carpeta estás).

**D)** La versión del kernel.

**Pregunta 5**

Quieres ver todos los archivos de la carpeta actual, incluidos los ocultos, en formato detallado. ¿Qué comando usarías?

**A)** `cd -a`

**B)** `ls -la`

**C)** `cat -a`

**D)** `pwd -la`

**Pregunta 6**

Estás en `/etc` y quieres ir a la carpeta personal de tu usuario. ¿Qué comando usarías?

**A)** `cd /var`

**B)** `cd ..`

**C)** `cd ~`

**D)** `cat /home`

**Pregunta 7**

¿Para qué sirve el comando `man`?

**A)** Para eliminar archivos.

**B)** Para mostrar el manual de ayuda de un comando.

**C)** Para cambiar el nombre del usuario.

**D)** Para comprimir archivos.

**Pregunta 8**

Quieres ejecutar `apt update`, pero necesitas privilegios de administrador. ¿Qué comando escribirías?

**A)** `sudo apt update`

**B)** `root apt update`

**C)** `admin apt update`

**D)** `user apt update`

**Pregunta 9**

¿Cuál es la diferencia entre `cat /var/log/syslog` y `tail /var/log/syslog`?

**A)** `cat` muestra las últimas líneas y `tail` muestra el archivo completo.

**B)** `cat` muestra el contenido completo y `tail` muestra las últimas líneas (lo más reciente).

**C)** Ambos hacen exactamente lo mismo.

**D)** `cat` solo funciona en Windows y `tail` solo en Linux.

**Pregunta 10 (Caso práctico SOC)**

Eres el Analista SOC de turno.

Te piden revisar si un servidor está sufriendo intentos de acceso no autorizados por SSH.

En el servidor existen los logs del sistema en `/var/log`.

¿Cuál es la secuencia de comandos más razonable para empezar a investigar?

**A)** `pwd` y `date`.

**B)** `cd /var/log` → `ls` → `tail -f /var/log/auth.log`.

**C)** `cat /etc/hostname` y `whoami`.

**D)** `rm -r /var/log` para limpiar los logs.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

Linux es, técnicamente, un **kernel**.

Es el núcleo del sistema operativo que conecta el hardware con el software.

En la práctica, cuando hablamos de "Linux" nos referimos a **GNU/Linux**, que combina el kernel con las herramientas GNU.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

Un Analista SOC trabaja con Linux porque:

- Los servidores corporativos corren sobre Linux.

- Los logs son archivos de texto plano.

- Herramientas como Wireshark, Suricata, Wazuh y Splunk corren sobre Linux.

- La mayoría de los SIEM y EDR se despliegan en servidores Linux.

Es la plataforma donde ocurre el trabajo real del SOC.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

- **CLI (Command Line Interface):** se controla escribiendo comandos de texto.

- **GUI (Graphical User Interface):** se controla con elementos gráficos como ventanas, botones y menús.

Los servidores se administran casi siempre por CLI, porque no tienen escritorio gráfico y porque la CLI permite automatizar tareas.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

`pwd` significa **print working directory**.

Muestra el directorio de trabajo actual, es decir, en qué carpeta estás parado dentro del sistema de archivos.

Ejemplo de salida:

`/home/usuario`

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

`ls -la` combina:

- `-l` → formato largo, con permisos, dueño, tamaño y fecha.

- `-a` → muestra todos los archivos, incluidos los ocultos (los que empiezan con punto).

Es una de las combinaciones más usadas en el trabajo diario.

**Pregunta 6**

✅ **Respuesta correcta: C**

**Justificación**

`cd ~` te lleva siempre a la carpeta personal de tu usuario (home).

Otros valores útiles:

- `cd ..` → sube al directorio padre.

- `cd /` → va a la raíz del sistema.

- `cd -` → vuelve al directorio anterior.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

`man` muestra el **manual** de un comando.

Ejemplo:

`man ls`

Para salir del manual se presiona `q`.

También existe `comando --help`, que muestra un resumen más corto y rápido.

**Pregunta 8**

✅ **Respuesta correcta: A**

**Justificación**

`sudo` significa **superuser do**.

Permite ejecutar un comando con privilegios de administrador.

Ejemplo:

`sudo apt update`

Usa `sudo` solo cuando el comando lo necesite, no para todo.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

- `cat` muestra el contenido **completo** del archivo de corrido.

- `tail` muestra solo las **últimas líneas**, que es donde se escriben los eventos más recientes.

Por eso `tail` es tan importante en un SOC:

los logs nuevos se agregan al final del archivo.

Y `tail -f` permite seguir el log en tiempo real.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

La secuencia más razonable es:

1. `cd /var/log` → ir al directorio de logs.

2. `ls` → ver qué logs existen.

3. `tail -f /var/log/auth.log` → leer en vivo los intentos de autenticación.

`auth.log` es el log donde se registran los accesos y fallos de autenticación.

Es el primer lugar donde se observan intentos de fuerza bruta por SSH.

Como analista, después deberías:

- Verificar si hubo accesos exitosos.

- Identificar las IPs origen.

- Revisar el patrón de intentos fallidos.

La opción **D** es peligrosa: **nunca** borres los logs con `rm`, porque son evidencia fundamental de la investigación.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                         |
|--------------------------|------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Ya estás en camino de dominar la terminal de Linux como un Analista SOC L1.                    |
| **8–9**                  | 🟢 **Muy buen nivel.** Te manejas bien con los comandos básicos de navegación y archivos.                       |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los comandos de navegación y la diferencia entre shell y GUI.                      |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a practicar `ls`, `cd`, `pwd`, `cat` y `tail` en tu máquina virtual. |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** La terminal de Linux será tu herramienta principal durante toda tu carrera como analista. |
