**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Módulo 19 – grep, Pipes y Análisis de Logs**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ Modelo OSI y TCP/IP

- ✅ TCP y UDP

- ✅ Puertos

- ✅ DNS, DHCP, HTTP y HTTPS

- ✅ Introducción a Linux y la Terminal (CLI)

- ✅ Estructura del Sistema de Archivos (FHS)

- ✅ Permisos de Archivos (rwx)

- ✅ Gestión de Usuarios y Grupos

- ✅ Gestión de Procesos

Hoy llegamos a uno de los módulos más importantes de toda tu formación como Analista SOC.

Los logs son la materia prima del trabajo en un centro de operaciones de seguridad.

Todo lo que ocurre en un sistema queda registrado en algún archivo de log.

Y en Linux, `grep` es la herramienta más poderosa para buscar y filtrar dentro de esos archivos.

Dominar `grep`, los pipes y `tail -f` te permitirá detectar fuerza bruta, accesos sospechosos y actividad anómala directamente en los logs.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es `grep` y para qué se usa en un SOC.

- Buscar patrones de texto dentro de archivos de log.

- Utilizar las opciones esenciales de `grep`: `-i`, `-v`, `-n`, `-c`, `-r`, `-l` y `-E`.

- Encadenar comandos con el pipe `|`.

- Redirigir la salida de un comando hacia un archivo con `>` y `>>`.

- Monitorear logs en tiempo real con `tail -f`.

- Combinar `grep` con `sort`, `uniq -c` y `awk` para contar eventos.

- Buscar archivos por nombre, tipo y permisos con `find`.

- Conocer los logs más importantes del sistema Linux.

- Detectar fuerza bruta SSH y accesos sospechosos analizando `auth.log`.

**1. ¿Qué es `grep`?**

`grep` significa **Global Regular Expression Print**.

Es un comando que busca patrones de texto dentro de archivos.

También puede filtrar la salida de otros comandos.

Es el "buscador" de la terminal.

**Analogía del detector de metales**

Imagina que estás en la playa con un detector de metales.

Pasas el detector por la arena y este solo emite una señal cuando encuentra metal.

No te muestra toda la arena.

Solo te indica dónde está lo que buscas.

`grep` funciona igual.

No te muestra todo el archivo.

Solo te muestra las líneas que coinciden con el patrón que buscas.

**Analogía del filtro de café**

Piensa también en un filtro de café.

Echas la mezcla, pero el filtro solo deja pasar el líquido que quieres tomar.

`grep` deja pasar únicamente las líneas que contienen lo que buscas.

Para un Analista SOC, `grep` es el filtro universal de los logs.

**2. Uso básico de `grep`**

La estructura más simple es:

`grep "patrón" archivo`

`grep` recorre el archivo línea por línea.

Si una línea contiene el patrón, la muestra.

Si no lo contiene, la descarta.

**Ejemplo clásico**

`grep "Failed" /var/log/auth.log`

Este comando muestra todas las líneas de `/var/log/auth.log` que contienen la palabra "Failed".

Verás líneas como:

`May 14 09:12:33 server sshd[1245]: Failed password for invalid user admin from 203.0.113.5 port 52270 ssh2`

Esa línea cuenta una historia.

Un intento de conexión SSH falló.

**El patrón puede ser una frase**

`grep "Failed password" /var/log/auth.log`

Busca exactamente la frase "Failed password".

Es más preciso que buscar solo "Failed".

**Los patrones distinguen mayúsculas y minúsculas**

`grep "failed"` es diferente de `grep "Failed"`.

Por defecto, `grep` distingue mayúsculas de minúsculas.

Si no encuentras resultados, revisa primero las mayúsculas.

**Siempre entre comillas**

Coloca el patrón entre comillas dobles.

`grep "error" /var/log/syslog`

Esto evita problemas con espacios y caracteres especiales.

**Resultado vacío = no hay coincidencias**

Si `grep` no muestra nada, significa que ninguna línea coincide.

Eso también es información útil.

**3. Opciones esenciales de `grep`**

`grep` tiene muchas opciones.

Estas son las que usarás todos los días en un SOC.

| **Opción** | **Función**                                  | **Ejemplo**                              |
|------------|----------------------------------------------|------------------------------------------|
| `-i`       | Ignora mayúsculas y minúsculas.              | `grep -i "error" /var/log/syslog`        |
| `-v`       | Invierte: muestra todo menos el patrón.      | `grep -v "Accepted" /var/log/auth.log`   |
| `-n`       | Muestra el número de línea.                  | `grep -n "Failed" /var/log/auth.log`     |
| `-c`       | Cuenta cuántas líneas coinciden.             | `grep -c "Failed password" /var/log/auth.log` |
| `-r`       | Busca de forma recursiva en carpetas.        | `grep -r "password" /etc/`               |
| `-l`       | Lista solo los archivos que coinciden.       | `grep -l "error" /var/log/*.log`         |
| `-E`       | Expresiones regulares extendidas.            | `grep -E "Failed|Accepted" /var/log/auth.log` |

**`-i`: ignorar mayúsculas**

`grep -i "error" /var/log/syslog`

Coincide con "error", "Error", "ERROR" y cualquier combinación.

Ideal cuando no estás seguro de cómo está escrito el texto.

**`-v`: invertir la búsqueda**

`grep -v "Accepted" /var/log/auth.log`

Muestra todas las líneas que NO contienen "Accepted".

Es el comando "todo menos esto".

Útil para filtrar ruido.

**`-n`: número de línea**

`grep -n "Failed" /var/log/auth.log`

Muestra el número de línea junto al resultado.

`3452:May 14 09:12:33 server sshd[1245]: Failed password ...`

Muy útil cuando quieres ubicar un evento exacto dentro del archivo.

**`-c`: contar coincidencias**

`grep -c "Failed password" /var/log/auth.log`

No muestra las líneas.

Solo muestra el número total de coincidencias.

Es la forma más rápida de medir el volumen de un ataque.

**`-r`: recursivo**

`grep -r "Listen" /etc/apache2/`

Busca el patrón dentro de todos los archivos de la carpeta y subcarpetas.

Ideal para revisar configuraciones completas.

**`-l`: listar archivos**

`grep -l "error" /var/log/*.log`

No muestra las líneas.

Solo muestra los nombres de los archivos que contienen el patrón.

Útil cuando no sabes en qué log está el evento.

**`-E`: expresiones regulares extendidas**

`grep -E "Failed|Accepted" /var/log/auth.log`

El `|` dentro del patrón significa "o".

Muestra líneas que contengan "Failed" O "Accepted".

Un solo comando para ver todos los intentos de autenticación.

**4. Pipes `|`: encadenar comandos**

El pipe se representa con el carácter vertical.

`|`

Es uno de los caracteres más importantes de la terminal.

**¿Qué hace el pipe?**

Toma la salida de un comando.

Y la pasa como entrada del siguiente.

Es como una tubería de agua.

El agua sale de un lugar y fluye hacia otro.

**Ejemplo básico**

`cat archivo | grep patrón`

Primero `cat` muestra el archivo completo.

El pipe pasa esa salida a `grep`.

`grep` la filtra y solo muestra las líneas que coinciden.

Resultado:

Solo las líneas que te interesan.

**Ver procesos que ejecutas**

`ps aux | grep python`

`ps aux` lista todos los procesos.

El pipe filtra solo los que contienen "python".

En un SOC lo usarás para verificar si un proceso sospechoso está corriendo.

**Buscar archivos de configuración**

`ls -la /etc | grep ".conf"`

Lista el contenido de `/etc`.

El pipe filtra solo los archivos que terminan en `.conf`.

**`grep` como filtro universal**

Casi cualquier comando puede pasar por un filtro `grep`.

`history | grep "sudo"`

`dmesg | grep "error"`

`journalctl | grep "sshd"`

Esta combinación es la base del análisis de logs en la terminal.

**Encadenar más de dos comandos**

`cat /var/log/auth.log | grep "Failed" | grep "203.0.113.5"`

Primero muestra el log.

Luego filtra los intentos fallidos.

Finalmente filtra solo los de una IP específica.

Tres comandos trabajando juntos en una sola línea.

**5. Redirecciones: `>`, `>>` y `2>`**

A veces no quieres ver la salida en pantalla.

Quieres guardarla en un archivo.

Para eso existen las redirecciones.

**`>` : crear o sobrescribir**

`grep "Failed password" /var/log/auth.log > intentos.txt`

La salida se guarda en `intentos.txt`.

Si el archivo ya existe, se sobrescribe.

Cuidado: `>` borra el contenido anterior sin preguntar.

**`>>` : añadir al final**

`grep "Accepted password" /var/log/auth.log >> intentos.txt`

La salida se añade al final del archivo.

No se borra lo que ya había.

Perfecto para ir acumulando evidencias.

**`2>` : redirigir errores**

`grep "patrón" /var/log/auth.log 2> errores.txt`

Los errores van a `errores.txt`.

La salida normal sigue en pantalla.

Algo muy común es descartar los errores:

`find / -name "*.sh" 2>/dev/null`

`2>/dev/null` envía los errores a la "nada".

Así solo ves resultados limpios.

**Guardar evidencias para el reporte**

Imagina que estás investigando fuerza bruta.

Guardas los intentos fallidos:

`grep "Failed password" /var/log/auth.log > evidencias_fuerza_bruta.txt`

Ese archivo se convierte en parte de tu reporte.

**Diferencia clave**

`>` crea o sobrescribe.

`>>` añade sin borrar.

`2>` redirige los errores.

**6. `tail -f`: monitorear logs en tiempo real**

`tail` muestra las últimas líneas de un archivo.

`tail -n 20 /var/log/auth.log`

Muestra las últimas 20 líneas.

**La opción `-f` es la estrella**

`tail -f /var/log/auth.log`

La `f` significa **follow** (seguir).

`tail -f` muestra las últimas líneas.

Y después sigue mostrando las líneas nuevas a medida que aparecen.

Es monitoreo en vivo.

**Analogía de la ventana**

Imagina que miras por una ventana hacia la calle.

Ves pasar a la gente en tiempo real.

Cada nueva persona que pasa, la ves.

`tail -f` es esa ventana hacia el log.

**¿Cuándo se usa?**

Durante un incidente en curso.

Mientras un atacante intenta entrar.

Mientras pruebas la configuración de un servicio.

Ves aparecer cada intento en el momento en que ocurre.

**Salir del monitoreo**

Cuando quieras detener el monitoreo, presiona:

`Ctrl + C`

**Ejemplo real**

Ejecutas:

`tail -f /var/log/auth.log`

Y comienzan a aparecer líneas:

`Failed password for invalid user root from 203.0.113.7`

`Failed password for invalid user admin from 203.0.113.7`

`Failed password for invalid user ubuntu from 203.0.113.7`

Estás viendo un ataque de fuerza bruta en vivo.

**7. Combinaciones poderosas**

`grep` solo ya es útil.

Pero combinado con otros comandos se vuelve demoledor.

**Contar el total de intentos**

`grep -c "Failed password" /var/log/auth.log`

Te dice cuántos intentos fallidos hubo.

**Contar líneas de otro comando**

`grep "Failed password" /var/log/auth.log | wc -l`

`wc -l` cuenta las líneas.

El resultado es el mismo que con `-c`.

**Ver las primeras líneas**

`grep "Failed" /var/log/auth.log | head -20`

Muestra solo los primeros 20 resultados.

**Ver las últimas líneas**

`grep "Failed" /var/log/auth.log | tail -20`

Muestra solo los últimos 20 resultados.

**Navegar en un archivo grande**

`grep "Failed" /var/log/auth.log | less`

`less` te permite navegar con flechas.

Presiona `q` para salir.

**Listar las IPs que más atacan**

Este es un comando esencial para un SOC:

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

Paso a paso:

- `grep "Failed password"` filtra los intentos fallidos.

- `awk '{print $(NF-3)}'` extrae la IP de cada línea.

- `sort` ordena las IPs.

- `uniq -c` las agrupa y cuenta cuántas veces aparece cada una.

- `sort -nr` las ordena de mayor a menor.

Resultado:

La IP con más intentos fallidos aparece primero.

Es decir, el atacante más activo.

**Explicación breve de los comandos auxiliares**

`awk` → extrae campos (columnas) de cada línea.

`sort` → ordena las líneas.

`uniq -c` → cuenta líneas consecutivas iguales.

`head` → primeras líneas.

`tail` → últimas líneas.

`wc -l` → cuenta líneas.

No necesitas dominarlos a fondo todavía.

Solo reconócelos como herramientas para procesar texto.

**8. `find`: buscar archivos en el sistema**

`find` busca archivos en el sistema de archivos.

No es lo mismo que `grep`.

`grep` busca **dentro** del contenido de los archivos.

`find` busca **archivos** por nombre, tipo o permisos.

**Buscar por nombre**

`find / -name "*.sh"`

Busca todos los archivos que terminan en `.sh` desde la raíz.

El `/` indica que empieza desde la raíz.

**Buscar en un directorio específico**

`find /home -name "*.conf"`

Busca archivos de configuración en `/home`.

**Buscar por tipo**

`find / -type d -name "tmp"`

`-type d` busca directorios.

`find / -type f -name "backup*"`

`-type f` busca archivos normales.

**Buscar por permisos**

`find / -perm -4000 -type f 2>/dev/null`

Busca archivos con el bit **setuid** activo.

Los binarios setuid son una forma de escalada de privilegios.

Este comando aparece en auditorías de seguridad.

**Evitar el ruido de errores**

`find / -name "*.sh" 2>/dev/null`

Descarta los errores de "Permission denied".

Hace que la salida sea mucho más limpia.

**¿Por qué importa en un SOC?**

Buscar scripts sospechosos.

`find /tmp -name "*.sh" 2>/dev/null`

Buscar binarios setuid.

`find / -perm -4000 -type f 2>/dev/null`

Buscar archivos modificados recientemente.

`find / -mtime -1 2>/dev/null`

Encuentra archivos modificados en las últimas 24 horas.

Eso puede revelar herramientas dejadas por un atacante.

**9. Logs importantes de Linux**

Cada log cuenta una parte de la historia del sistema.

| **Log**                  | **Contenido**                                           | **Sistema**                 |
|--------------------------|---------------------------------------------------------|-----------------------------|
| `/var/log/auth.log`      | Autenticación: logins, SSH, sudo.                       | Debian / Ubuntu             |
| `/var/log/secure`        | Autenticación: logins, SSH, sudo.                       | Red Hat / CentOS / Fedora   |
| `/var/log/syslog`        | Eventos generales del sistema y servicios.              | Debian / Ubuntu             |
| `/var/log/messages`      | Eventos generales del sistema y servicios.              | Red Hat / CentOS            |
| `/var/log/kern.log`      | Mensajes del kernel.                                    | Debian / Ubuntu             |
| `/var/log/dpkg.log`      | Instalación de paquetes con `dpkg`/`apt`.               | Debian / Ubuntu             |
| `/var/log/apache2/`      | Logs del servidor web Apache.                           | Debian / Ubuntu             |
| `/var/log/nginx/`        | Logs del servidor web Nginx.                            | Multiplataforma             |

**`/var/log/auth.log` – el favorito del SOC**

Registra los intentos de autenticación.

Ahí aparecen los intentos de SSH.

También los eventos de `sudo`.

En sistemas Debian y Ubuntu es el archivo que más analizarás.

**`/var/log/secure` – el equivalente en Red Hat**

Cumple la misma función que `auth.log`.

Pero en sistemas Red Hat, CentOS y Fedora.

Recuerda: analista SOC ve ambos mundos.

**`/var/log/syslog` – el evento general**

Todos los servicios pueden escribir aquí.

`grep -i "error" /var/log/syslog`

Busca errores generales del sistema.

**`/var/log/kern.log` – el kernel**

`grep -i "error" /var/log/kern.log`

Revisa problemas del kernel.

Útil en fallos de hardware o cargas de módulos.

**`/var/log/dpkg.log` – paquetes**

`grep "install" /var/log/dpkg.log`

Muestra qué paquetes se instalaron.

Puede revelar la instalación de herramientas no autorizadas.

**Logs web**

`/var/log/apache2/access.log`

`/var/log/apache2/error.log`

`/var/log/nginx/access.log`

`/var/log/nginx/error.log`

Los logs de acceso web registran cada petición.

Ahí se ven ataques a aplicaciones web.

`grep "404" /var/log/apache2/access.log`

Puede mostrar intentos de encontrar archivos inexistentes.

Un escaneo de vulnerabilidades deja miles de 404.

**10. Análisis real: detectar fuerza bruta SSH**

La fuerza bruta SSH es uno de los ataques más comunes en Internet.

El atacante prueba miles de usuarios y contraseñas.

Todo intento fallido queda registrado en el log.

Este es el análisis paso a paso.

**Paso 1: buscar los intentos fallidos**

`grep "Failed password" /var/log/auth.log`

Muestra todas las líneas de intentos fallidos.

Cada línea incluye:

- Fecha y hora.

- Usuario intentado.

- IP de origen.

- Puerto.

**Paso 2: contar cuántos intentos hubo**

`grep -c "Failed password" /var/log/auth.log`

El número resultante te da el volumen total.

Cientos o miles de intentos = posible ataque.

**Paso 3: identificar la IP de origen**

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

La primera línea del resultado es la IP con más intentos.

Esa es la IP del atacante más activo.

**Paso 4: distinguir fallidos de exitosos**

Los intentos fallidos dicen:

`Failed password`

Los accesos exitosos dicen:

`Accepted password`

Un log de línea para cada caso:

`grep "Failed password" /var/log/auth.log | wc -l`

`grep "Accepted password" /var/log/auth.log | wc -l`

Compara los dos números.

**Paso 5: detectar un compromiso probable**

Busca si la IP atacante logró acceder:

`grep "203.0.113.5" /var/log/auth.log | grep "Accepted"`

Si hay líneas de "Accepted password" desde esa IP, algo grave ocurrió.

Secuencia típica de un compromiso:

Miles de fallidos desde una IP.

↓

Un acceso exitoso desde esa misma IP.

= **Compromiso probable.**

Como analista debes:

- Confirmar el acceso exitoso.

- Identificar el usuario comprometido.

- Verificar qué comandos ejecutó.

- Contener la cuenta afectada.

**Ver todos los usuarios que se intentaron**

`grep "Failed password" /var/log/auth.log | grep "invalid user"`

Muestra los intentos con usuarios inexistentes.

**Monitoreo en vivo durante el ataque**

`tail -f /var/log/auth.log`

Ves los intentos aparecer en tiempo real.

**11. Analizar otros eventos**

La fuerza bruta no es lo único que se analiza.

Con `grep` puedes revisar casi cualquier evento.

**Eventos de `sudo`**

`grep "sudo" /var/log/auth.log`

Muestra los usos de `sudo`.

`grep "sudo" /var/log/auth.log | grep -i "COMMAND"`

Muestra los comandos ejecutados con `sudo`.

Esto puede revelar comandos sospechosos.

**Creación de usuarios**

`grep "useradd" /var/log/auth.log`

Muestra cuándo se crearon usuarios.

Un usuario nuevo sin explicación es sospechoso.

**Cambios de contraseña**

`grep "passwd" /var/log/auth.log`

`grep "password changed" /var/log/auth.log`

**Errores generales del sistema**

`grep -i "error" /var/log/syslog`

Busca errores en cualquier servicio.

**Reinicios del sistema**

`grep -i "shutdown" /var/log/syslog`

`grep -i "reboot" /var/log/syslog`

Un reinicio inesperado puede ser indicio de manipulación.

**Instalación de paquetes**

`grep "install" /var/log/dpkg.log`

`grep -i "error" /var/log/dpkg.log`

**Servicios caídos**

`grep -i "fail" /var/log/syslog`

Muestra fallos de servicios.

Un servicio crítico caído es una alerta inmediata.

**12. Aplicación práctica en un SOC**

Veamos cómo se aplica todo esto en casos reales.

**Caso 1 – Fuerza bruta SSH desde una IP externa**

El equipo de operaciones reporta lentitud en un servidor.

Revisas el log:

`grep "Failed password" /var/log/auth.log`

Encuentras miles de intentos.

Cuentas:

`grep -c "Failed password" /var/log/auth.log`

Resultado: 12.450 intentos en 24 horas.

Identificas la IP origen:

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

La IP 203.0.113.99 tiene 9.800 intentos.

Verificas si hubo acceso exitoso:

`grep "203.0.113.99" /var/log/auth.log | grep "Accepted"`

Resultado: no hay accesos exitosos.

Conclusión:

Ataque de fuerza bruta sin éxito.

Acciones:

- Bloquear la IP en el firewall.

- Reforzar la política de contraseñas.

- Considerar fail2ban para bloqueos automáticos.

**Caso 2 – Monitoreo en vivo durante una prueba**

El equipo va a probar la autenticación de un servicio.

Necesitas ver los eventos en tiempo real.

Ejecutas:

`tail -f /var/log/auth.log`

Ves cada intento aparecer al instante.

Confirmas que los logs registran correctamente los eventos.

Después de la prueba, guardas la evidencia:

`grep "Failed password" /var/log/auth.log > prueba_auth_$(date +%F).txt`

**Caso 3 – Búsqueda de eventos `sudo` sospechosos**

Un usuario reporta actividad extraña en su cuenta.

Revisas el uso de `sudo`:

`grep "sudo" /var/log/auth.log`

`grep "sudo" /var/log/auth.log | grep -i "COMMAND"`

Encuentras que alguien ejecutó comandos de administración a las 03:00 AM.

Nadie debería administrar el sistema a esa hora.

Investigas:

- ¿Qué comando exacto se ejecutó?

- ¿Desde qué IP?

- ¿Con qué usuario?

- ¿Coincide con la jornada laboral?

Ese evento merece una investigación completa.

**Caso 4 – Guardar evidencias para el reporte**

Terminas la investigación de fuerza bruta.

Necesitas guardar todas las evidencias.

Creas la carpeta de evidencias:

`mkdir ~/evidencias_incidente`

Guardas los intentos fallidos:

`grep "Failed password" /var/log/auth.log > ~/evidencias_incidente/fuerza_bruta.txt`

Guardas los accesos exitosos:

`grep "Accepted password" /var/log/auth.log > ~/evidencias_incidente/accesos_exitosos.txt`

Guardas la lista de IPs atacantes:

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr > ~/evidencias_incidente/top_ips.txt`

Esas evidencias acompañarán tu reporte de incidente.

**13. Lo que esperan de un Analista SOC Nivel 1**

En una entrevista o en tu primer día te harán preguntas como:

- ¿Qué comando buscaría los intentos fallidos de login?

- ¿Cómo cuento cuántas veces apareció un evento?

- ¿Qué IP está atacando más?

- ¿Hubo acceso exitoso después de los intentos fallidos?

Debes responder con comandos concretos.

**¿Qué comando busca intentos fallidos?**

`grep "Failed password" /var/log/auth.log`

**¿Cómo cuento cuántas veces?**

`grep -c "Failed password" /var/log/auth.log`

**¿Qué IP ataca más?**

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

**¿Hubo acceso exitoso después?**

`grep "Accepted password" /var/log/auth.log`

`grep "203.0.113.99" /var/log/auth.log | grep "Accepted"`

**Pensar como analista**

No basta con ejecutar comandos.

Debes interpretar el contexto:

- ¿El volumen de intentos es normal?

- ¿La IP de origen es interna o externa?

- ¿El horario es habitual?

- ¿Hubo accesos exitosos después?

- ¿Qué usuarios se intentaron usar?

Ese razonamiento es el que distingue a un buen analista.

**14. Resumen**

**`grep`**

- Busca patrones de texto dentro de archivos.

- Muestra solo las líneas que coinciden.

- Es el filtro universal de los logs.

**Uso básico**

`grep "patrón" archivo`

**Opciones esenciales**

- `-i`: ignora mayúsculas.

- `-v`: invierte, muestra todo menos el patrón.

- `-n`: número de línea.

- `-c`: cuenta coincidencias.

- `-r`: recursivo en carpetas.

- `-l`: lista archivos que coinciden.

- `-E`: expresiones regulares extendidas.

**Pipe `|`**

- Pasa la salida de un comando al siguiente.

- Ejemplo: `cat archivo | grep patrón`.

**Redirecciones**

- `>` crea o sobrescribe.

- `>>` añade al final.

- `2>` redirige errores.

**`tail -f`**

- Muestra los logs en tiempo real.

- Esencial durante un incidente.

**Fuerza bruta SSH**

- Fallidos: "Failed password".

- Exitosos: "Accepted password".

- Fallidos + exitosos desde la misma IP = compromiso probable.

**`find`**

- Busca archivos por nombre, tipo y permisos.

- Ejemplo: `find / -perm -4000 -type f`.

**Logs clave**

- `/var/log/auth.log` → autenticación (Debian/Ubuntu).

- `/var/log/secure` → autenticación (Red Hat).

- `/var/log/syslog` → sistema.

- `/var/log/kern.log` → kernel.

**🧠 Conceptos clave para memorizar**

| **Concepto**              | **Debes recordar**                                              |
|---------------------------|-----------------------------------------------------------------|
| grep                      | Global Regular Expression Print.                                |
| `grep "patrón" archivo`   | Busca el patrón en el archivo.                                  |
| `-i`                      | Ignora mayúsculas y minúsculas.                                 |
| `-v`                      | Muestra todo menos el patrón.                                   |
| `-c`                      | Cuenta cuántas líneas coinciden.                                |
| `-r`                      | Busca de forma recursiva en carpetas.                           |
| Pipe `|`                  | Pasa la salida de un comando como entrada del siguiente.        |
| `>`                       | Crea o sobrescribe un archivo.                                  |
| `>>`                      | Añade al final del archivo.                                     |
| `tail -f`                 | Monitorea el log en tiempo real.                                |
| `/var/log/auth.log`       | Log de autenticación en Debian/Ubuntu.                          |
| `/var/log/secure`         | Log de autenticación en Red Hat.                                |
| "Failed password"         | Intento de inicio de sesión fallido.                            |
| "Accepted password"       | Inicio de sesión exitoso.                                       |
| `find`                    | Busca archivos por nombre, tipo y permisos.                     |

**🎓 Consejo como tu instructor de SOC**

`grep` es tu detector de anomalías en los logs.

En el SOC real, cada día revisarás miles de líneas de logs.

Sin `grep` sería imposible.

Con `grep`, encuentras la aguja en el pajar en segundos.

**Memoriza el patrón "Failed password"**

Es el patrón de fuerza bruta por excelencia.

Aparecerá en tus logs constantemente.

También memoriza su contraparte:

"Accepted password"

Un acceso exitoso es el momento más importante de toda la investigación.

**Memoriza la combinación con pipes**

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

Este comando te da al instante las IPs que más atacan.

Es una de las consultas más usadas en cualquier SOC Linux.

**El futuro: los SIEM**

En el SOC real los logs llegarán a un SIEM.

Herramientas como Splunk, Elastic o Sentinel.

Ahí tendrás buscadores más avanzados.

Pero saber leer los logs en crudo te da la base.

**Comprenderás qué hay detrás de cada alerta.**

Sabrás de dónde salen los datos que ves en el SIEM.

Y cuando el SIEM falle, podrás ir directo al servidor y analizar con `grep`.

Esa combinación te convierte en un analista completo.

---

**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Evaluación – Módulo 19: grep, Pipes y Análisis de Logs**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el material de estudio. Este cuestionario está diseñado con el nivel de una entrevista técnica para un **Analista SOC Nivel 1**. Encontrarás preguntas teóricas y casos prácticos basados en el análisis real de logs de Linux.

**Pregunta 1**

¿Qué significa la sigla **grep**?

**A)** Global Regular Expression Print

**B)** General Report Error Program

**C)** Global Read Execute Print

**D)** Group Regular Expression Path

**Pregunta 2**

Quieres ver solo las líneas del archivo `/var/log/auth.log` que contienen la frase "Failed password".

¿Qué comando ejecutas?

**A)** `cat /var/log/auth.log`

**B)** `grep "Failed password" /var/log/auth.log`

**C)** `tail -f /var/log/auth.log`

**D)** `ls /var/log/auth.log`

**Pregunta 3**

¿Qué hace la opción **`-i`** en `grep`?

**A)** Muestra solo las primeras líneas.

**B)** Ignora mayúsculas y minúsculas en la búsqueda.

**C)** Invierte el resultado y muestra todo menos el patrón.

**D)** Cuenta cuántas coincidencias hay.

**Pregunta 4**

¿Qué hace la opción **`-v`** en `grep`?

**A)** Muestra el número de línea de cada coincidencia.

**B)** Busca de forma recursiva en carpetas.

**C)** Muestra todo excepto las líneas que coinciden con el patrón.

**D)** Ignora las mayúsculas.

**Pregunta 5**

¿Qué hace la opción **`-c`** en `grep`?

**A)** Muestra las coincidencias a color.

**B)** Cuenta cuántas líneas coinciden con el patrón.

**C)** Copia el resultado a un archivo.

**D)** Compara dos archivos.

**Pregunta 6**

¿Para qué sirve el pipe **`|`** en Linux?

**A)** Para ejecutar un comando en segundo plano.

**B)** Para pasar la salida de un comando como entrada del siguiente.

**C)** Para crear un archivo nuevo.

**D)** Para eliminar un archivo.

**Pregunta 7**

Estás monitoreando un ataque de fuerza bruta SSH en tiempo real.

¿Qué comando te muestra las nuevas líneas de `/var/log/auth.log` a medida que aparecen?

**A)** `cat /var/log/auth.log`

**B)** `grep -c "Failed password" /var/log/auth.log`

**C)** `tail -f /var/log/auth.log`

**D)** `head -20 /var/log/auth.log`

**Pregunta 8**

¿Cuál es la diferencia entre **`>`** y **`>>`**?

**A)** `>` añade al final y `>>` sobrescribe.

**B)** Ambos hacen exactamente lo mismo.

**C)** `>` crea o sobrescribe el archivo y `>>` añade al final.

**D)** `>>` sirve solo para errores.

**Pregunta 9**

¿Qué comando busca todos los archivos que terminan en **`.sh`** desde la raíz del sistema?

**A)** `grep -r "*.sh" /`

**B)** `find / -name "*.sh"`

**C)** `ls -la *.sh`

**D)** `tail -f *.sh`

**Pregunta 10 (Caso práctico SOC)**

El SIEM generó una alerta de posible fuerza bruta SSH.

Necesitas saber cuántos intentos fallidos hubo en el servidor.

¿Qué comando utilizas?

**A)** `grep "Accepted password" /var/log/auth.log`

**B)** `grep -c "Failed password" /var/log/auth.log`

**C)** `tail -f /var/log/auth.log`

**D)** `find / -name "auth.log"`

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: A**

**Justificación**

`grep` significa **Global Regular Expression Print**.

Es un comando que busca patrones de texto dentro de archivos y muestra las líneas que coinciden.

Es la herramienta principal para filtrar logs en Linux.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

El comando correcto es:

`grep "Failed password" /var/log/auth.log`

Busca la frase dentro del archivo y muestra solo las líneas que la contienen.

`cat` muestra el archivo completo sin filtrar.

`tail -f` monitorea en tiempo real.

`ls` lista archivos y carpetas.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

La opción **`-i`** (ignore case) hace que la búsqueda no distinga entre mayúsculas y minúsculas.

Ejemplo:

`grep -i "error" /var/log/syslog`

Coincide con "error", "Error" y "ERROR".

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

La opción **`-v`** (invert) muestra todo **excepto** las líneas que coinciden con el patrón.

Ejemplo:

`grep -v "Accepted" /var/log/auth.log`

Muestra todas las líneas del log que NO contienen "Accepted".

Es muy útil para filtrar ruido.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

La opción **`-c`** (count) cuenta cuántas líneas coinciden con el patrón.

No muestra las líneas.

Solo muestra el número total.

Ejemplo:

`grep -c "Failed password" /var/log/auth.log`

Devuelve un número como 12.450.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

El pipe **`|`** toma la salida de un comando y la pasa como entrada del siguiente.

Ejemplo:

`cat /var/log/auth.log | grep "Failed"`

Primero `cat` muestra el log.

El pipe envía esa salida a `grep`.

`grep` filtra solo las líneas que contienen "Failed".

**Pregunta 7**

✅ **Respuesta correcta: C**

**Justificación**

`tail -f /var/log/auth.log` muestra las últimas líneas y sigue mostrando las líneas nuevas a medida que se escriben.

La opción **`-f`** significa follow (seguir).

Es el monitoreo en tiempo real.

Se detiene con `Ctrl + C`.

**Pregunta 8**

✅ **Respuesta correcta: C**

**Justificación**

`>` crea un archivo nuevo o sobrescribe el existente.

`>>` añade el contenido al final sin borrar lo anterior.

`2>` se usa para redirigir los errores.

Ejemplo:

`grep "Failed password" /var/log/auth.log > evidencias.txt`

Crea o sobrescribe el archivo.

`grep "Accepted password" /var/log/auth.log >> evidencias.txt`

Añade al final.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

`find / -name "*.sh"` busca archivos por nombre desde la raíz del sistema.

`find` busca archivos.

`grep` busca dentro del contenido.

`-perm -4000` permite buscar por permisos, como los binarios setuid:

`find / -perm -4000 -type f 2>/dev/null`

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Para contar los intentos fallidos de SSH:

`grep -c "Failed password" /var/log/auth.log`

El resultado es el número total de intentos fallidos.

Si quieres ir más allá, puedes identificar la IP más atacante:

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

Y verificar si hubo accesos exitosos:

`grep "Accepted password" /var/log/auth.log`

Si una misma IP tuvo muchos fallidos y luego un acceso exitoso:

**Compromiso probable.**

Como analista SOC debes:

- Confirmar el acceso exitoso.

- Identificar el usuario afectado.

- Verificar qué se hizo con esa cuenta.

- Bloquear la IP en el firewall.

- Documentar todo en el reporte de incidente.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Ya analizas logs en Linux como un Analista SOC: filtras, cuentas y detectas fuerza bruta.     |
| **8–9**                  | 🟢 **Muy buen nivel.** Dominas grep y los pipes para encontrar información rápidamente.                        |
| **6–7**                  | 🟡 **Buen progreso.** Repasa las opciones de grep y la diferencia entre `>` y `>>`.                            |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Practica más con grep y tail -f en tu máquina virtual.            |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** grep es una de las herramientas más usadas por los analistas todos los días. |
