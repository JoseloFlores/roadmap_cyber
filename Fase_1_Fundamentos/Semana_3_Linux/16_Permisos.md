**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Módulo 16 – Permisos de Archivos y Directorios (rwx)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ Modelo OSI y TCP/IP

- ✅ TCP y UDP

- ✅ Puertos

- ✅ DNS, DHCP, HTTP y HTTPS

- ✅ Introducción a Linux y la Terminal (CLI)

- ✅ Estructura del Sistema de Archivos (FHS)

Ahora llegamos a uno de los temas más importantes de todo Linux: **los permisos**.

Ya sabes que en Linux **todo es un archivo**.

Y cada archivo tiene un **dueño** y unos **permisos**.

Los permisos `rwx` controlan quién puede **leer**, quién puede **escribir** y quién puede **ejecutar** cada archivo o directorio.

¿Por qué esto es tan importante para un SOC?

Porque una mala configuración de permisos es una de las causas más comunes de compromiso en Linux.

Archivos de configuración legibles por todos.

Binarios ejecutables por cualquier usuario.

Directorios **world-writable** donde cualquiera puede dejar archivos.

Cuando termines este módulo, serás capaz de detectar esas fallas con un simple `ls -l`.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué son los permisos en Linux.

- Identificar las tres clases de usuarios: owner, group y others.

- Diferenciar el significado de `rwx` en archivos y en directorios.

- Leer la notación simbólica que muestra `ls -l`.

- Modificar permisos con `chmod` en notación simbólica y octal.

- Cambiar propietario y grupo con `chown` y `chgrp`.

- Entender los permisos por defecto mediante `umask`.

- Reconocer los bits especiales: setuid, setgid y sticky bit.

- Identificar ataques que aprovechan permisos mal configurados.

- Aplicar estos conocimientos en auditorías y casos reales de un SOC.

**1. ¿Qué son los permisos?**

Los permisos son el **mecanismo de control de acceso** de Linux.

Determinan **quién puede hacer qué** con un archivo o directorio.

Piensa en una oficina con diferentes niveles de acceso.

Tienes tarjetas que abren ciertas puertas.

- Algunas personas pueden **leer** los documentos.

- Algunas pueden **modificarlos**.

- Algunas pueden **entrar a la sala** donde se guardan.

Los permisos de Linux funcionan igual.

Definen exactamente qué puede hacer cada persona con cada archivo.

Sin permisos, cualquier usuario podría leer, borrar o modificar cualquier cosa del sistema.

Eso sería un caos total.

Y para un atacante, una mina de oro.

**2. Tres clases de usuarios**

En Linux existen **tres clases** de usuarios para cada archivo.

| **Clase**      | **Letra** | **¿Quién es?**                                    |
|----------------|-----------|---------------------------------------------------|
| Owner          | `u`       | El propietario (quien creó o es dueño del archivo). |
| Group          | `g`       | El grupo al que pertenece el archivo.             |
| Others         | `o`       | Todos los demás usuarios.                         |
| All            | `a`       | Los tres anteriores juntos.                       |

**Analogía de la oficina**

Imagina que existe un documento importante en una empresa.

- **Owner:** el autor del documento. Tiene el control total sobre él.

- **Group:** su equipo de trabajo. Puede colaborar y hacer cambios.

- **Others:** el resto del edificio. Solo lo que se les permita.

Cada archivo tiene un **dueño** y pertenece a un **grupo**.

Para saber quién es el dueño usas:

`ls -l`

Ese comando muestra:

- El propietario.

- El grupo.

- Los permisos.

- El tamaño.

- La fecha.

- El nombre del archivo.

Como Analista SOC lo usarás constantemente para auditar el sistema.

**3. Permisos en archivos**

En Linux cada permiso es una letra.

| **Permiso** | **Letra** | **¿Qué permite en un archivo?**                          |
|-------------|-----------|----------------------------------------------------------|
| Read        | `r`       | Leer el contenido del archivo.                           |
| Write       | `w`       | Modificar, sobrescribir o vaciar el archivo.             |
| Execute     | `x`       | Ejecutar el archivo como un programa o script.           |

**r (read): leer el contenido**

Si tienes permiso `r`, puedes ver lo que hay dentro.

Por ejemplo, leer un archivo de configuración con `cat`.

`cat /etc/ssh/sshd_config`

Si no tienes `r`, el sistema te dirá: *"Permission denied"*.

**w (write): modificar el archivo**

Si tienes `w`, puedes cambiar el contenido.

Puedes editarlo, sobrescribirlo o borrar su contenido.

**Cuidado:** tener `w` sobre un archivo no te permite borrarlo.

Borrar un archivo depende de los permisos del **directorio** que lo contiene.

Eso lo verás en el siguiente punto.

**x (execute): ejecutar el archivo**

Si tienes `x`, puedes ejecutarlo como un programa.

**Ejemplo de un script**

Imagina un script llamado `analisis.sh`.

Sin permiso `x`, al intentar ejecutarlo recibirás:

*"Permission denied"*

Con permiso `x` puedes ejecutarlo:

`./analisis.sh`

**Ejemplo de un archivo de texto**

Un archivo de texto como `notas.txt` no necesita permiso de ejecución.

Nadie ejecuta un archivo de texto.

Solo necesita `r` para leerse y `w` para editarse.

Por eso los archivos de texto normalmente tienen permisos como `644`.

Y los scripts o programas, permisos como `755`.

**4. Permisos en directorios**

Aquí el significado de `rwx` **cambia por completo**.

No es lo mismo tener permisos sobre un archivo que sobre un directorio.

| **Permiso** | **Letra** | **¿Qué permite en un directorio?**                          |
|-------------|-----------|-------------------------------------------------------------|
| Read        | `r`       | Listar los nombres de los archivos que contiene.            |
| Write       | `w`       | Crear o eliminar archivos dentro del directorio.            |
| Execute     | `x`       | Entrar al directorio y acceder a sus archivos.              |

**r: listar el contenido**

Con `r` puedes ejecutar `ls` y ver los nombres de los archivos.

`ls /var/log`

Ves los nombres, pero no necesariamente el contenido de cada archivo.

**w: crear o eliminar archivos**

Con `w` puedes crear archivos nuevos dentro del directorio.

También puedes **eliminar** archivos que están dentro.

Ojo con esto:

Aunque un archivo no sea tuyo, si el directorio es `w` para ti, puedes borrarlo.

**x: entrar al directorio**

Este es el permiso clave de un directorio.

Sin `x` no puedes **entrar** al directorio.

Imagina que tienes `r` pero no `x`.

Puedes ver los nombres de los archivos con `ls`.

Pero no puedes entrar a leer su contenido.

Obtendrás errores como *"Permission denied"* al intentar acceder.

**Por qué un directorio sin `x` es inaccesible**

El permiso `x` es lo que te permite "caminar" a través del directorio.

Sin él, el sistema te bloquea el paso.

Es como una puerta cerrada con llave.

Puedes mirar la placa de la puerta desde afuera (listar con `r`).

Pero no puedes abrir la puerta y entrar (acceder con `x`).

**Regla práctica de seguridad**

Para la mayoría de los directorios del sistema se usan permisos como `755`.

El propietario puede hacer todo.

El resto solo puede entrar y leer.

Un directorio que permite a todos crear archivos es una alerta.

Ese tipo de directorio se llama **world-writable**.

**5. Leer la notación simbólica (`ls -l`)**

Cuando ejecutas:

`ls -l`

Obtienes una línea parecida a esta:

`-rwxr-xr--  1 carlos devs 1234 ago 14 10:30 informe.sh`

Esa cadena de 10 caracteres es la clave de todo.

Se divide así:

| **Posición** | **Significado**                          |
|--------------|------------------------------------------|
| 1            | Tipo de archivo.                         |
| 2-4          | Permisos del **owner** (`u`).            |
| 5-7          | Permisos del **group** (`g`).            |
| 8-10         | Permisos de **others** (`o`).            |

**El primer carácter: tipo de archivo**

| **Carácter** | **Tipo de archivo**                       |
|--------------|-------------------------------------------|
| `-`          | Archivo normal.                           |
| `d`          | Directorio.                               |
| `l`          | Enlace simbólico (acceso directo).        |
| `c`          | Dispositivo de caracteres.                |
| `b`          | Dispositivo de bloques.                   |

**Desglosando el ejemplo**

`-rwxr-xr--`

- Primer carácter: `-` → es un archivo normal.

- `rwx` → el owner puede leer, escribir y ejecutar.

- `r-x` → el grupo puede leer y ejecutar, pero no escribir.

- `r--` → los demás solo pueden leer.

Traducción:

`chmod 754`

Ya verás la notación octal en unos minutos.

**Otro ejemplo**

`drwxr-xr-x`

- Primer carácter: `d` → es un directorio.

- `rwx` → el owner puede listar, crear y entrar.

- `r-x` → el grupo puede listar y entrar, pero no crear.

- `r-x` → los demás pueden listar y entrar, pero no crear.

**¿Qué hace `ls -la`?**

La opción `-a` muestra también los archivos ocultos.

Los archivos ocultos comienzan con un punto.

`.bashrc`

`.ssh`

`ls -la`

Es una combinación muy utilizada para auditar.

**6. Notación simbólica para modificar (`chmod`)**

Puedes cambiar los permisos con `chmod` usando letras.

La estructura es:

`chmod [a quién][operación][permiso] archivo`

| **¿A quién?** | **Letra** |
|---------------|-----------|
| Owner         | `u`       |
| Group         | `g`       |
| Others        | `o`       |
| Todos         | `a`       |

| **Operación** | **Símbolo** |
|---------------|-------------|
| Agregar       | `+`         |
| Quitar        | `-`         |
| Asignar exacto| `=`         |

| **Permiso** | **Letra** |
|-------------|-----------|
| Read        | `r`       |
| Write       | `w`       |
| Execute     | `x`       |

**Ejemplos**

Agregar permiso de ejecución al owner:

`chmod u+x script.sh`

Quitar permiso de escritura al grupo:

`chmod g-w archivo.txt`

Agregar permiso de lectura para todos los demás:

`chmod o+r archivo.txt`

Asignar permisos exactos al owner:

`chmod u=rwx script.sh`

Combinar clases en un solo comando:

`chmod u+x,g-w script.sh`

**Ventajas de la notación simbólica**

Es ideal cuando solo quieres cambiar un permiso específico.

No necesitas conocer el valor octal completo.

**Desventaja**

En auditorías sueles necesitar el valor octal exacto.

Por eso debes dominar las dos notaciones.

**7. Notación octal (r=4, w=2, x=1)**

Cada permiso tiene un valor numérico.

| **Permiso** | **Valor** |
|-------------|-----------|
| `r`         | 4         |
| `w`         | 2         |
| `x`         | 1         |

Para obtener el valor de un grupo, **sumas** los valores de los permisos presentes.

Ejemplo:

- `rwx` = 4 + 2 + 1 = **7**

- `rw-` = 4 + 2 + 0 = **6**

- `r-x` = 4 + 0 + 1 = **5**

- `r--` = 4 + 0 + 0 = **4**

**Tabla de combinaciones del 0 al 7**

| **Valor** | **Simbólico** | **Permisos**                       |
|-----------|---------------|------------------------------------|
| 0         | `---`         | Sin permisos.                      |
| 1         | `--x`         | Solo ejecutar.                     |
| 2         | `-w-`         | Solo escribir.                     |
| 3         | `-wx`         | Escribir y ejecutar.               |
| 4         | `r--`         | Solo leer.                         |
| 5         | `r-x`         | Leer y ejecutar.                   |
| 6         | `rw-`         | Leer y escribir.                   |
| 7         | `rwx`         | Leer, escribir y ejecutar.         |

**El número completo tiene tres dígitos**

`chmod 754 archivo`

El primer dígito es para el owner.

El segundo para el group.

El tercero para others.

| **chmod** | **Owner** | **Group** | **Others**  | **Resultado**   |
|-----------|-----------|-----------|-------------|-----------------|
| `750`     | 7 `rwx`   | 5 `r-x`   | 0 `---`     | `-rwxr-x---`    |
| `644`     | 6 `rw-`   | 4 `r--`   | 4 `r--`     | `-rw-r--r--`    |
| `755`     | 7 `rwx`   | 5 `r-x`   | 5 `r-x`     | `-rwxr-xr-x`    |
| `600`     | 6 `rw-`   | 0 `---`   | 0 `---`     | `-rw-------`    |
| `777`     | 7 `rwx`   | 7 `rwx`   | 7 `rwx`     | `-rwxrwxrwx`    |

**Combinaciones que debes memorizar**

- `644` → archivos normales de lectura para todos.

- `755` → scripts y ejecutables para todos.

- `600` → archivos sensibles, solo para el owner.

- `700` → directorios privados, solo para el owner.

- `640` → archivos de configuración legibles por el grupo.

- `777` → TODO MUNDO puede hacer todo. Bandera roja.

**8. `chmod` en la práctica**

Veamos ejemplos con su explicación.

**Ejemplo 1**

`chmod 644 informe.txt`

Resultado:

`-rw-r--r--`

Explicación:

- Owner: `rw-` (puede leer y editar).

- Group: `r--` (solo puede leer).

- Others: `r--` (solo puede leer).

Es el permiso típico de los archivos normales.

**Ejemplo 2**

`chmod 755 script.sh`

Resultado:

`-rwxr-xr-x`

Explicación:

- Owner: `rwx` (puede hacer todo).

- Group: `r-x` (puede ejecutar, pero no modificar).

- Others: `r-x` (puede ejecutar, pero no modificar).

Es el permiso típico de los scripts y binarios.

**Ejemplo 3**

`chmod 600 credenciales.txt`

Resultado:

`-rw-------`

Explicación:

- Owner: `rw-` (puede leer y editar).

- Group: `---` (nada).

- Others: `---` (nada).

Es el permiso ideal para archivos con secretos.

**Ejemplo 4**

`chmod 750 /home/carlos/proyecto`

Resultado:

`drwxr-x---`

Explicación:

- Owner: `rwx` (puede entrar y crear).

- Group: `r-x` (puede entrar y leer, no crear).

- Others: `---` (nada).

Perfecto para directorios de trabajo compartidos.

**Ejemplo 5**

`chmod 400 clave.pem`

Resultado:

`-r--------`

Explicación:

- Owner: `r--` (solo lectura).

- Group: `---`.

- Others: `---`.

Es el permiso típico para claves privadas SSH.

**9. `chown` y `chgrp`**

Los permisos definen qué puede hacer cada clase.

Pero también necesitas saber **quién es el dueño** y **cuál es el grupo**.

Eso se controla con `chown` y `chgrp`.

**Cambiar el propietario**

`chown carlos archivo.txt`

El nuevo propietario será `carlos`.

**Cambiar propietario y grupo a la vez**

`chown carlos:devs archivo.txt`

El propietario será `carlos`.

El grupo será `devs`.

**Cambiar solo el grupo**

`chgrp devs archivo.txt`

O bien:

`chown :devs archivo.txt`

Ambos cambian únicamente el grupo.

**¿Por qué `chown` requiere privilegios?**

Porque cambiar el dueño de un archivo es una operación muy peligrosa.

Imagina que pudieras regalar archivos de la empresa a cualquier usuario.

Podrías hacer que los secretos pertenezcan a un atacante.

Por eso solo `root` puede cambiar el propietario de un archivo.

Los usuarios normales solo pueden cambiar el **grupo** de los archivos que les pertenecen, y solo a grupos de los que forman parte.

Para realizar cambios necesitas privilegios elevados:

`sudo chown carlos:devs archivo.txt`

**Cómo verificar los cambios**

`ls -l archivo.txt`

Verás el propietario y el grupo en la salida.

**10. `umask` (permisos por defecto)**

Cuando creas un archivo nuevo, ¿qué permisos tiene?

Eso lo decide el **umask**.

`umask` significa **User file creation MASK**.

Es una máscara que determina **qué permisos se quitan** al crear un archivo.

**Los valores base**

- Archivos normales: base `666` (`rw-rw-rw-`).

- Directorios: base `777` (`rwxrwxrwx`).

El `umask` resta permisos a esos valores base.

**Valor típico: 022**

`umask 022`

Explicación:

Se quita el permiso de escritura para group y others.

**Resultados con `umask 022`**

- Archivo: `666 - 022 = 644` → `-rw-r--r--`

- Directorio: `777 - 022 = 755` → `drwxr-xr-x`

Es decir:

- Archivos: solo el dueño puede escribir.

- Directorios: todos pueden entrar y leer, solo el dueño escribe.

**Otro valor típico: 077**

`umask 077`

Resultados:

- Archivo: `666 - 077 = 600` → `-rw-------`

- Directorio: `777 - 077 = 700` → `drwx------`

Solo el dueño tiene acceso.

Ideal para directorios privados.

**Cómo ver tu umask actual**

`umask`

**Cómo cambiarlo temporalmente**

`umask 077`

**Cómo cambiarlo de forma permanente**

Se configura en archivos como:

`/etc/profile`

`~/.bashrc`

**Por qué importa para un SOC**

Un `umask` mal configurado puede dejar archivos legibles o escribibles por todos.

Un `umask` seguro garantiza que los nuevos archivos nazcan protegidos.

Recuerda:

**umask 022** → archivos `644`, directorios `755`.

**umask 077** → archivos `600`, directorios `700`.

**11. Bits especiales**

Además de `rwx`, existen **tres bits especiales**.

| **Bit**   | **Valor octal** | **Símbolo** | **Efecto**                             |
|-----------|-----------------|-------------|----------------------------------------|
| setuid    | 4               | `s` en owner  | Ejecuta con los privilegios del dueño. |
| setgid    | 2               | `s` en group  | Ejecuta con el grupo del archivo.      |
| sticky    | 1               | `t`          | Solo el dueño puede borrar sus archivos. |

**setuid (4)**

Un ejecutable con setuid se ejecuta con los privilegios del **propietario** del archivo.

**Ejemplo real**

`/usr/bin/passwd`

Observa su salida:

`-rwsr-xr-x  1 root root ... /usr/bin/passwd`

- El propietario es `root`.

- En la posición del owner aparece `s` en lugar de `x`.

Eso significa que cualquier usuario puede ejecutarlo.

Y al ejecutarlo, el comando actúa como **root**.

¿Por qué es necesario?

Porque para cambiar la contraseña hay que modificar `/etc/shadow`, que solo root puede tocar.

Sin setuid, los usuarios no podrían cambiar sus contraseñas.

**setgid (2)**

Con setgid, el archivo se ejecuta con el grupo del archivo.

En un directorio con setgid, los archivos nuevos **heredan el grupo** del directorio.

Eso es muy útil en directorios compartidos de equipos.

**sticky bit (1)**

El sticky bit se aplica a directorios.

Solo el **propietario** del archivo (o root) puede borrarlo.

**Ejemplo real: `/tmp`**

`drwxrwxrwt  1 root root ... /tmp`

- Todo el mundo puede entrar y crear archivos (`rwxrwxrwx`).

- La `t` final es el sticky bit.

Con sticky bit, un usuario **no puede borrar** los archivos de otro.

Sin sticky bit, cualquiera podría borrar los archivos temporales de los demás.

**Cómo se ven los bits especiales en `ls -l`**

| **Bit**   | **Con x** | **Sin x** |
|-----------|-----------|-----------|
| setuid    | `s`       | `S`       |
| setgid    | `s`       | `S`       |
| sticky    | `t`       | `T`       |

La letra en mayúscula significa que el bit especial está activo pero no hay `x`.

**Cómo activarlos con `chmod`**

`chmod 4755 programa`

Activa setuid.

`chmod 2755 directorio`

Activa setgid.

`chmod 1777 /tmp`

Activa sticky bit.

También en notación simbólica:

`chmod u+s programa`

`chmod g+s directorio`

`chmod +t /tmp`

**Riesgo de seguridad del setuid**

Un binario setuid que pertenece a **root** es muy peligroso.

Si el binario tiene vulnerabilidades, un atacante puede explotarlo.

Y al explotarlo, obtiene privilegios de **root**.

Esta técnica se llama **escalada de privilegios**.

Un Analista SOC debe buscar binarios setuid sospechosos.

**12. ¿Cómo aprovechan esto los atacantes?**

Los permisos mal configurados son una puerta abierta para los atacantes.

**Ataque 1 – Archivos de configuración legibles por todos**

Muchos servicios guardan contraseñas y secretos en archivos de configuración.

Si esos archivos son legibles por todos, cualquiera puede leerlos.

**Ejemplo real**

`/etc/shadow` almacena los hashes de las contraseñas del sistema.

Sus permisos correctos son `640` o `600`, propiedad de `root`.

Si `/etc/shadow` fuera legible por todos:

`-rw-r--r--  1 root root ... /etc/shadow`

Cualquier usuario podría copiar los hashes.

Y después intentar crackearlos con herramientas de fuerza bruta.

**Ataque 2 – Binarios con setuid mal configurados**

Un binario con setuid de root es una escalada de privilegios en potencia.

Los atacantes buscan binarios setuid con vulnerabilidades conocidas.

O binarios setuid que cualquiera pueda **modificar**.

Si un binario setuid es escribible, el atacante puede reemplazarlo.

El nuevo binario se ejecutará con privilegios de root.

**Ataque 3 – Directorios world-writable como `/tmp`**

Los atacantes usan directorios world-writable para dejar sus herramientas.

- Scripts.

- Binarios maliciosos.

- Cargas útiles.

Y los ejecutan desde ahí.

`/tmp` y `/var/tmp` son lugares favoritos.

**Ataque 4 – Permisos 777 en archivos o scripts**

Un archivo con `777` permite que cualquiera lo modifique.

Si un script del sistema tiene `777`, cualquier usuario puede alterarlo.

Podrían inyectar comandos maliciosos.

La próxima vez que el sistema ejecute ese script, el malware se ejecutará.

**Ataque 5 – Logs no protegidos**

Los logs registran todo lo que ocurre en el sistema.

`/var/log/auth.log`

`/var/log/syslog`

`/var/log/secure`

Si esos archivos son escribibles, el atacante puede:

- Borrar sus huellas.

- Eliminar líneas de sus conexiones.

- Ocultar sus comandos.

Y después de borrar las evidencias, la investigación se complica enormemente.

**Resumen de los ataques**

| **Ataque**            | **Fallo de permisos**                         | **Consecuencia**                     |
|------------------------|-----------------------------------------------|--------------------------------------|
| Ataque 1               | `/etc/shadow` legible                         | Robo de hashes de contraseñas.       |
| Ataque 2               | Binario setuid vulnerable                     | Escalada de privilegios a root.      |
| Ataque 3               | Directorio world-writable                      | Alojamiento de herramientas.         |
| Ataque 4               | Archivos `777`                                | Modificación de scripts del sistema. |
| Ataque 5               | Logs escribibles                              | Borrado de evidencias.               |

**13. ¿Cómo defenderse?**

La defensa se basa en un principio simple:

**Principio de menor privilegio.**

Cada usuario y proceso debe tener solo los permisos mínimos para trabajar.

**Buenas prácticas de permisos**

- Archivos normales: `644`.

- Scripts y ejecutables: `755`.

- Archivos sensibles: `600`.

- Directorios de trabajo: `750` o `755`.

- Directorios privados: `700`.

- Claves privadas SSH: `600` o `400`.

**Proteger `/etc/shadow`**

`/etc/shadow` debe pertenecer a `root`.

Y tener permisos `640` o `600`.

`ls -l /etc/shadow`

El grupo `shadow` puede leerlo porque los servicios necesitan verificar contraseñas.

**No usar `777` nunca**

`chmod 777` es una bandera roja en cualquier auditoría.

Significa que cualquiera puede leer, modificar y ejecutar.

**Revisar los binarios setuid**

Buscar periódicamente binarios con setuid:

`find / -perm -4000 -type f 2>/dev/null`

Analizar si todos son legítimos.

**Revisar los permisos de logs y configuraciones**

- Configuraciones: `640` o `644`.

- Logs: `640` y propiedad de root.

- Ningún archivo importante debe ser escribible por others.

**Configurar un `umask` seguro**

Con `umask 022` los nuevos archivos nacen con `644`.

Con `umask 077` nacen con `600`.

Elige según el nivel de sensibilidad.

**14. Aplicación práctica en un SOC**

Como Analista SOC auditarás permisos constantemente.

Estos son los casos más frecuentes.

**Caso 1 – Verificar la protección de `/etc/shadow`**

Ejecutas:

`ls -l /etc/shadow`

Si ves:

`-rw-r-----  1 root shadow 1245 ago 14 08:15 /etc/shadow`

Interpretación:

- Permisos `640`.

- Propietario `root`.

- Grupo `shadow`.

Protección correcta. Los hashes no están expuestos.

Si en cambio ves:

`-rw-r--r--  1 root root ... /etc/shadow`

Interpretación:

- Permisos `644`.

- Cualquier usuario puede leer los hashes.

**Alerta de seguridad inmediata.**

**Caso 2 – Buscar binarios setuid**

Ejecutas:

`find / -perm -4000 -type f 2>/dev/null`

La salida podría mostrar:

`/usr/bin/passwd`

`/usr/bin/sudo`

`/usr/bin/mount`

Interpretación:

- Estos son binarios setuid legítimos del sistema.

- Debes revisar si aparece algo raro o fuera de lo común.

Un binario setuid sospechoso en `/tmp` o `/home` es motivo de alarma.

**Caso 3 – Comprobar los permisos de los logs**

Ejecutas:

`ls -l /var/log/auth.log`

Si ves:

`-rw-r-----  1 root adm ... /var/log/auth.log`

Interpretación:

- Permisos `640`.

- Solo root y el grupo `adm` pueden leerlo.

- Nadie puede modificarlo salvo root.

Protección correcta.

Si un log fuera escribible por others, el atacante podría borrar sus huellas.

**Caso 4 – Revisar directorios world-writable**

Buscas directorios donde cualquiera pueda escribir:

`find / -type d -perm -0002 2>/dev/null`

La salida normalmente incluye:

`/tmp`

`/var/tmp`

`/dev/shm`

Interpretación:

- Son directorios temporales, por diseño world-writable.

- Deben tener el **sticky bit** activo.

Verifícalo:

`ls -ld /tmp`

Si ves:

`drwxrwxrwt  1 root root ... /tmp`

La `t` final indica sticky bit.

Sin sticky bit, ese directorio sería un problema grave.

**15. Lo que esperan de un Analista SOC Nivel 1**

En una entrevista o en tu primer día en el SOC te harán preguntas como:

- ¿Qué significan `rwx`?

- ¿Cuánto vale `chmod 755`?

- ¿Qué es el setuid?

- ¿Por qué `/tmp` es sospechoso?

- ¿Qué permisos debería tener `/etc/shadow`?

Debes poder responder de inmediato, sin dudar.

**En una auditoría real**

Cuando revises un servidor, observa:

- ¿Quién puede leer los archivos de configuración?

- ¿Quién puede escribir en los scripts del sistema?

- ¿Existen binarios setuid inusuales?

- ¿Hay directorios world-writable sin sticky bit?

- ¿Están protegidos los logs y `/etc/shadow`?

Cada respuesta te dice si el servidor está bien configurado o es una víctima esperando.

**Lo que NO debes hacer nunca**

- Ejecutar `chmod 777` sobre archivos del sistema.

- Ignorar un `/etc/shadow` legible.

- Dejar claves privadas con permisos abiertos.

- Olvidar revisar los binarios setuid.

**16. Resumen**

**Permisos**

- Mecanismo de control de acceso de Linux.

- Definen quién puede leer, escribir o ejecutar.

**Tres clases**

- Owner (`u`).

- Group (`g`).

- Others (`o`).

**En archivos**

- `r` = leer contenido.

- `w` = modificar contenido.

- `x` = ejecutar.

**En directorios**

- `r` = listar contenido.

- `w` = crear o eliminar archivos.

- `x` = entrar al directorio.

**Notación octal**

- `r` = 4.

- `w` = 2.

- `x` = 1.

- Se suman los valores.

**Comandos clave**

- `chmod 750` → cambiar permisos.

- `chown user:group archivo` → cambiar dueño y grupo.

- `chgrp grupo archivo` → cambiar grupo.

- `umask 022` → permisos por defecto.

- `ls -l` → ver permisos.

**Bits especiales**

- setuid = 4.

- setgid = 2.

- sticky bit = 1.

**Riesgos principales**

- `/etc/shadow` legible.

- Binarios setuid mal configurados.

- Directorios world-writable.

- Permisos `777`.

- Logs sin proteger.

**🧠 Conceptos clave para memorizar**

| **Concepto**            | **Debes recordar**                                                |
|-------------------------|-------------------------------------------------------------------|
| `rwx`                   | Leer, escribir y ejecutar.                                        |
| `u` `g` `o` `a`         | Owner, group, others y all.                                       |
| Archivo con `r`         | Puedes leer su contenido.                                         |
| Directorio con `x`      | Puedes entrar y acceder.                                          |
| Octal `4-2-1`           | r = 4, w = 2, x = 1.                                              |
| `chmod 755`             | Owner todo, grupo y otros leen y ejecutan.                        |
| `chmod 600`             | Solo el owner lee y escribe.                                      |
| `chmod 777`             | Todos pueden hacer todo. Bandera roja.                            |
| `chown user:group`      | Cambia propietario y grupo.                                       |
| `umask 022`             | Archivos 644 y directorios 755.                                   |
| setuid                  | Ejecuta con los privilegios del dueño.                            |
| sticky bit              | Solo el dueño borra sus archivos en el directorio.                |
| `/etc/shadow`           | Hashes de contraseñas. Permisos 640 o 600.                        |

**🎓 Consejo como tu instructor de SOC**

Quiero que memorices una asociación mental:

**Permisos correctos = menor riesgo.**

**Permisos abiertos = superficie de ataque.**

Cada vez que veas `777` en una auditoría, sospecha.

Cada vez que veas un archivo de configuración legible por todos, investiga.

Y recuerda que `ls -l` será **tu mejor amigo** para auditar.

Aprende a leerlo con un solo vistazo.

`-rwxr-xr--` ya debe decirte todo en un segundo:

- Archivo normal.

- Owner: todo.

- Grupo: lee y ejecuta.

- Others: solo lee.

Con esa habilidad podrás detectar configuraciones inseguras antes de que los atacantes las aprovechen.

Y eso, en un SOC, marca la diferencia entre prevenir un incidente y responder a uno.

**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Evaluación – Módulo 16: Permisos de Archivos y Directorios (rwx)**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Este cuestionario está diseñado con un nivel similar al de una entrevista técnica para un **Analista SOC Nivel 1**. Encontrarás preguntas teóricas y casos prácticos basados en auditorías reales de sistemas Linux.

**Pregunta 1**

En un archivo normal, ¿qué permite el permiso **`w`**?

**A)** Leer el contenido del archivo.

**B)** Ejecutar el archivo como un programa.

**C)** Modificar, sobrescribir o vaciar el contenido del archivo.

**D)** Cambiar el propietario del archivo.

**Pregunta 2**

En un directorio, ¿qué permite el permiso **`x`**?

**A)** Listar los nombres de los archivos que contiene.

**B)** Entrar al directorio y acceder a sus archivos.

**C)** Crear o eliminar archivos dentro del directorio.

**D)** Borrar el directorio completo.

**Pregunta 3**

¿Cuál es el valor octal de los permisos simbólicos **`rwxr-xr--`**?

**A)** 754

**B)** 744

**C)** 751

**D)** 765

**Pregunta 4**

Si ejecutas `chmod 750 archivo.txt`, ¿qué permisos quedan establecidos?

**A)** `-rwxr-x---`

**B)** `-rwxr--r--`

**C)** `-rw-r-----`

**D)** `-rwx------`

**Pregunta 5**

¿Qué comando cambia el propietario y el grupo de un archivo a la vez?

**A)** `chgrp carlos:devs archivo.txt`

**B)** `chmod carlos:devs archivo.txt`

**C)** `chown carlos:devs archivo.txt`

**D)** `chmod 755 archivo.txt`

**Pregunta 6**

¿Qué significa que un binario tenga activo el bit **setuid**?

**A)** Cualquier usuario puede borrarlo.

**B)** Se ejecuta con los privilegios del propietario del archivo.

**C)** Solo puede ejecutarlo el propietario.

**D)** Los archivos creados heredan el grupo del directorio.

**Pregunta 7**

¿Por qué `/tmp` tiene activo el **sticky bit**?

**A)** Para impedir que se escriba en él.

**B)** Para que solo root pueda entrar.

**C)** Para que cada usuario solo pueda borrar sus propios archivos.

**D)** Para que los archivos se eliminen automáticamente.

**Pregunta 8**

Con `umask 022`, ¿qué permisos por defecto reciben los archivos nuevos?

**A)** 644

**B)** 755

**C)** 600

**D)** 777

**Pregunta 9**

Observas la siguiente salida de `ls -l`:

`drwxr-xr-x  1 carlos devs 4096 ago 14 09:30 informe`

¿Qué indica la primera letra **`d`**?

**A)** Que es un enlace simbólico.

**B)** Que es un archivo normal.

**C)** Que es un directorio.

**D)** Que el archivo tiene permisos de ejecución.

**Pregunta 10 (Caso práctico SOC)**

Durante una auditoría encuentras:

`ls -l /etc/shadow`

Resultado:

`-rw-r--r--  1 root root 1245 ago 14 08:15 /etc/shadow`

¿Qué implica esta configuración?

**A)** Configuración correcta y segura.

**B)** Cualquier usuario puede leer los hashes de las contraseñas del sistema.

**C)** Solo root puede acceder al archivo.

**D)** El archivo está protegido con setuid.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: C**

**Justificación**

En un archivo, el permiso **`w`** (write) permite **modificar, sobrescribir o vaciar** su contenido.

El permiso `r` permite leerlo.

El permiso `x` permite ejecutarlo.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

En un directorio, el permiso **`x`** permite **entrar y acceder** a los archivos que contiene.

Sin `x`, el directorio es inaccesible.

`r` permite listar los nombres y `w` permite crear o eliminar archivos dentro.

**Pregunta 3**

✅ **Respuesta correcta: A**

**Justificación**

- `rwx` = 4 + 2 + 1 = 7.

- `r-x` = 4 + 0 + 1 = 5.

- `r--` = 4 + 0 + 0 = 4.

Resultado: **754**.

**Pregunta 4**

✅ **Respuesta correcta: A**

**Justificación**

`chmod 750` significa:

- Owner: 7 = `rwx`.

- Group: 5 = `r-x`.

- Others: 0 = `---`.

Resultado: `-rwxr-x---`.

**Pregunta 5**

✅ **Respuesta correcta: C**

**Justificación**

El comando **`chown user:group archivo`** cambia propietario y grupo a la vez.

Ejemplo:

`chown carlos:devs archivo.txt`

`chmod` cambia permisos y `chgrp` cambia únicamente el grupo.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

El bit **setuid** hace que un binario se ejecute con los privilegios del **propietario** del archivo.

Ejemplo clásico:

`/usr/bin/passwd`

Pertenece a `root` y cualquiera puede ejecutarlo para cambiar su contraseña.

Por eso un setuid mal configurado permite escalada de privilegios.

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

El **sticky bit** en `/tmp` garantiza que **cada usuario solo pueda borrar sus propios archivos**, aunque el directorio sea world-writable.

Sin sticky bit, cualquiera podría eliminar los archivos temporales de los demás.

**Pregunta 8**

✅ **Respuesta correcta: A**

**Justificación**

Con `umask 022` se quita el permiso de escritura para group y others.

- Archivos: `666 - 022 = 644`.

- Directorios: `777 - 022 = 755`.

**Pregunta 9**

✅ **Respuesta correcta: C**

**Justificación**

La primera letra de `ls -l` indica el tipo de archivo.

- `d` → directorio.

- `-` → archivo normal.

- `l` → enlace simbólico.

En este caso es un **directorio** con permisos `755`.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Permisos `644` en `/etc/shadow` significan que **cualquier usuario puede leerlo**.

Como `/etc/shadow` contiene los **hashes de las contraseñas** del sistema, esta configuración expone los hashes a todos los usuarios.

Los permisos correctos son `640` o `600`, con propietario `root`.

Como analista SOC deberías:

- Reportar la configuración como vulnerabilidad crítica.

- Corregir los permisos de inmediato:

`chmod 640 /etc/shadow`

- Evaluar si algún usuario pudo copiar el archivo.

- Revisar logs de acceso.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Dominas los permisos de Linux y puedes detectar configuraciones inseguras.                                                    |
| **8–9**                  | 🟢 **Muy buen nivel.** Interpretas `ls -l`, `chmod` octal y los riesgos de los permisos.                                                        |
| **6–7**                  | 🟡 **Buen progreso.** Repasa la notación octal (4-2-1) y la diferencia entre permisos de archivos y directorios.                                |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Vuelve a estudiar `chmod`, `chown` y los bits especiales.                                          |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** Los permisos son clave para la seguridad y las auditorías en Linux.                           |
