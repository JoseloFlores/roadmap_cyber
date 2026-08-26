**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 3 – Linux**

**Módulo 17 – Gestión de Usuarios y Grupos**

**Nivel:** Principiante → Analista SOC Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a> y <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

- ✅ TCP y <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

- ✅ Puertos

- ✅ <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>, <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

- ✅ Introducción a Linux y la Terminal (<a href="../../GLOSARIO.md#cli" target="_blank">CLI</a>)

- ✅ Estructura del Sistema de Archivos (<a href="../../GLOSARIO.md#fhs" target="_blank">FHS</a>)

- ✅ Permisos de Archivos (rwx)

Ahora vamos a responder una pregunta clave:

¿Quién puede entrar al sistema?

¿Y con qué derechos?

Eso lo decide la **gestión de usuarios y grupos**.

Los **usuarios** determinan quién puede iniciar sesión en Linux.

Los **grupos** determinan qué accesos comparten esos usuarios.

En un SOC vas a auditar cuentas, detectar cuentas nuevas creadas por un
atacante y revisar intentos de acceso.

Dominar la gestión de usuarios es esencial para detectar escaladas de
privilegios y compromisos.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es un usuario en Linux.

- Diferenciar usuario normal, usuario de sistema y <a href="../../GLOSARIO.md#root" target="_blank">root</a>.

- Interpretar los archivos `/etc/passwd`, `/etc/shadow` y `/etc/group`.

- Crear, modificar y eliminar usuarios con comandos.

- Gestionar contraseñas y expiración de cuentas.

- Crear y administrar grupos.

- Consultar la identidad de un usuario.

- Diferenciar `sudo` de `su`.

- Reconocer cómo usan los atacantes la gestión de usuarios.

- Aplicar estos conocimientos en investigaciones de un SOC.

**1. ¿Qué es un usuario en Linux?**

Un **usuario** es una identidad dentro del sistema.

Es la identidad que puede iniciar sesión y ejecutar procesos.

Cada usuario tiene un nombre y un número único.

Ese número se llama **UID (User Identifier)**.

El sistema no trabaja con nombres.

El sistema trabaja con números.

El nombre es solo una etiqueta fácil de recordar para las personas.

Ejemplo:

usuario "carlos"

↓

UID 1001

Cada proceso que se ejecuta pertenece a un usuario.

Cada archivo que existe pertenece a un usuario.

Si <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> usuarios tienen el mismo UID, el sistema los considera el mismo
usuario.

Esto será muy importante cuando hables de ataques.

**Analogía**

Piensa en el sistema como un edificio.

Cada usuario es un **empleado del edificio**.

Cada empleado tiene una credencial de acceso.

Esa credencial le permite entrar por ciertas puertas.

La credencial contiene su **identificación (UID)**.

Sin credencial, no puedes entrar.

Con la credencial equivocada, entras a lugares equivocados.

Linux funciona exactamente así.

**2. Tipos de usuarios en Linux**

Existen tres tipos principales:

- Usuarios normales.

- Usuarios de sistema.

- El superusuario `root`.

**Usuarios normales**

Son las personas que usan el sistema.

Ejemplo:

- carlos.

- maria.

- juan.

Suelen tener UID desde **1000 en adelante**.

Tienen permisos limitados.

No pueden modificar archivos del sistema.

**Usuarios de sistema**

No son personas.

Son identidades que usan los servicios y programas.

Ejemplos:

- `www-data` → servicio web Apache o Nginx.

- `mysql` → base de datos MySQL.

- `sshd` → servicio <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>.

Suelen tener UID bajos.

Por ejemplo:

- UID 0–999.

No pueden iniciar sesión normalmente.

Su <a href="../../GLOSARIO.md#shell" target="_blank">shell</a> suele ser `/usr/sbin/nologin` o `/bin/false`.

**root (el superusuario)**

`root` es el usuario más poderoso.

Tiene UID **0**.

Puede hacer todo lo que quiera en el sistema:

- Crear y borrar cuentas.

- Modificar cualquier archivo.

- Instalar o eliminar programas.

- Reiniciar servicios.

- Ver todos los procesos.

Ninguna regla de permisos lo limita.

**Analogía**

`root` es el **administrador general del edificio**.

Puede abrir cualquier puerta.

Puede despedir empleados.

Puede entrar a cualquier oficina.

Puede cambiar la cerradura de todo el edificio.

En un SOC, una cuenta con UID 0 despierta siempre sospechas.

**3. El archivo `/etc/passwd`**

Es uno de los archivos más importantes de Linux.

Contiene la información básica de todos los usuarios.

Su nombre es antiguo: hace décadas guardaba las contraseñas.

Hoy **ya no guarda contraseñas**.

Solo guarda los datos de identidad.

Cada usuario ocupa una línea.

Cada línea tiene **7 campos** separados por dos puntos.

Formato:

usuario:x:UID:GID:comentario:home:shell

| **Campo**      | **Significado**                                          | **Ejemplo**                     |
|----------------|----------------------------------------------------------|---------------------------------|
| usuario        | Nombre de la cuenta.                                     | `root`                          |
| x              | Indica que la contraseña está en `/etc/shadow`.          | `x`                             |
| UID            | Número único de identificación del usuario.              | `0`                             |
| GID            | Número del grupo principal del usuario.                  | `0`                             |
| comentario     | Información opcional (nombre real, teléfono, etc.).      | `root`                          |
| home           | Carpeta personal del usuario.                            | `/root`                         |
| shell          | Programa que se ejecuta al iniciar sesión.               | `/bin/bash`                     |

**Ejemplo real**

root:x:0:0:root:/root:/bin/<a href="../../GLOSARIO.md#bash" target="_blank">bash</a>

Interpretación:

- usuario → `root`.

- x → contraseña protegida en `/etc/shadow`.

- UID → 0.

- GID → 0.

- comentario → root.

- home → `/root`.

- shell → `/bin/bash`.

**Otro ejemplo**

carlos:x:1001:1001:Carlos Perez:/home/carlos:/bin/bash

Interpretación:

- usuario → `carlos`.

- UID → 1001.

- home → `/home/carlos`.

- shell → `/bin/bash` (usuario normal con login).

**¿Por qué la "x"?**

Antes las contraseñas se guardaban aquí.

Esto era peligroso.

Cualquiera podía leer el archivo.

En 1980 se inventó `/etc/shadow`.

Ahora las contraseñas se guardan cifradas en otro archivo.

El campo `x` es solo una marca que dice:

"La contraseña real está en `/etc/shadow`."

Para leer el archivo:

`cat /etc/passwd`

Para buscar un usuario específico:

`grep carlos /etc/passwd`

Para buscar usuarios con shell de login:

`grep -v nologin /etc/passwd`

**Pista para el SOC**

Si aparece un usuario con shell `/bin/bash` que no debería tener login,
algo huele mal.

**4. El archivo `/etc/shadow`**

Contiene las contraseñas de los usuarios.

Guardadas en forma de **hash**.

Un hash es una transformación de la contraseña.

No se puede revertir fácilmente.

Ejemplo de hash:

`$6$sal$hGhs9Kd...`

Los prefijos indican el algoritmo:

| **Prefijo** | **Algoritmo**        |
|-------------|----------------------|
| `$1$`       | MD5 (antiguo)        |
| `$5$`       | SHA-256              |
| `$6$`       | SHA-512 (común)      |
| `$y$`       | Yescrypt (moderno)   |

**Es un archivo protegido.**

Solo `root` puede leerlo.

Solo `root` puede modificarlo.

Por eso el campo en `/etc/passwd` es una "x".

Los usuarios no deben ver los hashes.

Si un atacante obtiene el archivo, puede intentar:

- Romper los hashes con diccionarios.

- Romper los hashes con fuerza bruta.

- Reutilizar hashes en otras máquinas.

**Formato resumido de `/etc/shadow`**

Cada línea tiene 9 campos separados por dos puntos.

usuario:hash:ultimo_cambio:min:max:aviso:inactiva:expiracion:reservado

| **Campo**       | **Significado**                                        |
|-----------------|--------------------------------------------------------|
| usuario         | Nombre de la cuenta.                                   |
| hash            | Contraseña cifrada o `!` / `*` si está bloqueada.      |
| ultimo_cambio   | Días desde 1970 hasta el último cambio de contraseña.  |
| min             | Días mínimos antes de poder cambiar la contraseña.     |
| max             | Días máximos de validez de la contraseña.              |
| aviso           | Días de aviso antes de que expire.                     |
| inactiva        | Días tras la expiración antes de bloquear la cuenta.   |
| expiracion      | Fecha de expiración de la cuenta (días desde 1970).    |
| reservado       | Campo vacío reservado para el futuro.                  |

**Ejemplo real**

carlos:$6$abc123$def456...:18500:0:99999:7:::

Interpretación:

- Contraseña con hash SHA-512.

- Se cambió hace 18500 días desde 1970.

- No hay mínimo de días (0).

- Máximo de validez: 99999 días (casi ilimitado).

- Aviso de expiración: 7 días.

**Señales sospechosas en `/etc/shadow`**

- Un hash en lugar de `!` en una cuenta de servicio.

- Una cuenta que debería estar bloqueada y no lo está.

- Hashes de algoritmos antiguos como `$1$`.

Para consultar información de una contraseña:

`passwd -S carlos`

Para bloquear una cuenta:

`passwd -l carlos`

Para desbloquear:

`passwd -u carlos`

**Pista para el SOC**

Un atacante no puede leer `/etc/shadow` sin ser `root`.

Si el archivo aparece en un log de exfiltración, es una emergencia.

**5. El archivo `/etc/group`**

Los grupos agrupan usuarios.

Permiten compartir permisos y accesos.

Cada grupo tiene un número llamado **GID**.

Formato resumido:

grupo:x:GID:miembros

| **Campo** | **Significado**                                 |
|-----------|-------------------------------------------------|
| grupo     | Nombre del grupo.                               |
| x         | La contraseña de grupo vive en `/etc/gshadow`.  |
| GID       | Número único del grupo.                         |
| miembros  | Lista de usuarios del grupo separados por coma. |

**Ejemplo real**

<a href="../../GLOSARIO.md#sudo" target="_blank">sudo</a>:x:27:carlos,maria

Interpretación:

- Grupo `sudo`.

- GID 27.

- Miembros: `carlos` y `maria`.

Para ver todos los grupos:

`cat /etc/group`

Para ver a qué grupos pertenece un usuario:

`groups carlos`

**Analogía**

Piensa en un edificio con departamentos.

Cada grupo es un **departamento**.

- Contabilidad.

- Ventas.

- Sistemas.

Cada empleado pertenece a uno o más departamentos.

Si el departamento de Contabilidad tiene llave de la caja fuerte,
todos sus miembros pueden entrar.

En Linux pasa lo mismo.

El grupo define **qué puertas compartidas pueden abrir** sus miembros.

**6. Crear y eliminar usuarios**

El comando principal es `useradd`.

**Crear un usuario básico**

`useradd carlos`

Crea la cuenta.

Pero puede que no cree el home ni la contraseña.

**Crear un usuario completo**

`useradd -m -s /bin/bash carlos`

Significado:

- `-m` → crea el home `/home/carlos`.

- `-s` → asigna la shell `/bin/bash`.

**Crear un usuario con comentario**

`useradd -m -s /bin/bash -c "Carlos Perez" carlos`

**Crear un usuario con fecha de expiración**

`useradd -m -s /bin/bash -e 2026-12-31 carlos`

La cuenta se desactiva automáticamente en esa fecha.

**Asignar contraseña**

`passwd carlos`

El sistema pedirá la nueva contraseña dos veces.

**Eliminar un usuario**

`userdel carlos`

Elimina la cuenta.

Pero **no borra** el home ni el correo.

**Eliminar un usuario con todo su contenido**

`userdel -r carlos`

Elimina la cuenta.

También borra su home y su bandeja de correo.

**Pista para el SOC**

`userdel -r` es peligroso.

Borra datos que podrían ser evidencia.

En una investigación, primero copia los archivos del usuario.

Luego decide si borras la cuenta.

**7. Modificar usuarios y contraseñas**

Para cambiar datos de un usuario usamos `usermod`.

**Agregar un usuario a un grupo**

`usermod -aG sudo carlos`

Significado:

- `-a` → append (agregar, no reemplazar).

- `-G` → grupos secundarios.

- `sudo` → el grupo destino.

Sin la `-a`, `usermod -G` reemplaza todos los grupos.

Ese error puede dejar al usuario sin accesos.

**Cambiar la shell de un usuario**

`usermod -s /usr/sbin/nologin carlos`

Así se convierten cuentas normales en cuentas sin login.

**Bloquear una cuenta**

`passwd -l carlos`

**Desbloquear una cuenta**

`passwd -u carlos`

**Forzar el cambio de contraseña al siguiente login**

`chage -d 0 carlos`

El valor 0 obliga a cambiar la contraseña en el próximo inicio de
sesión.

**Configurar la expiración de contraseña**

`chage -M 90 carlos`

La contraseña expirará después de 90 días.

**Configurar la expiración de la cuenta**

`chage -E 2026-12-31 carlos`

La cuenta se desactiva en esa fecha.

**Ver la información de expiración**

`chage -l carlos`

Muestra:

- Último cambio de contraseña.

- Edad máxima.

- Aviso de expiración.

- Cuenta activa o inactiva.

**Analogía**

`chage` es como fijar la **fecha de vencimiento de la credencial**.

El empleado sigue en el edificio.

Pero su credencial deja de funcionar después de la fecha límite.

**8. Grupos**

Para crear grupos usamos `groupadd`.

**Crear un grupo**

`groupadd ventas`

**Crear un grupo con GID específico**

`groupadd -g 1100 ventas`

**Eliminar un grupo**

`groupdel ventas`

Solo funciona si el grupo no es el principal de ningún usuario.

**Agregar un usuario a un grupo**

`gpasswd -a carlos ventas`

**Quitar un usuario de un grupo**

`gpasswd -d carlos ventas`

**Poner un administrador de grupo**

`gpasswd -A maria ventas`

Maria podrá agregar y quitar miembros del grupo.

**Asignar un grupo principal**

`usermod -g ventas carlos`

El grupo principal es el que aparece en el GID de `/etc/passwd`.

**Grupos importantes en Linux**

| **Grupo** | **Función**                                   |
|-----------|-----------------------------------------------|
| `root`    | Grupo del superusuario.                       |
| `sudo`    | Permite ejecutar comandos con privilegios.    |
| `wheel`   | Alternativa al grupo sudo (en algunos sistemas). |
| `adm`     | Permite leer los logs del sistema.            |
| `www-data`| Usuario y grupo de los servicios web.         |
| `shadow`  | Puede leer `/etc/shadow` (usado por servicios).|

**Pista para el SOC**

Un usuario que no debería estar en `sudo` o en `wheel` es una alerta.

Puede ser el inicio de una escalada de privilegios.

**9. Consultar usuarios e identidad**

En un SOC vas a necesitar saber quién es quién.

**Ver la identidad del usuario actual**

`id`

Muestra:

- UID.

- GID.

- Grupos secundarios.

Ejemplo de salida:

uid=1000(carlos) gid=1000(carlos) groups=1000(carlos),27(sudo)

**Ver quién soy**

`whoami`

Responde solo con el nombre del usuario.

**Ver quién está conectado**

`who`

Muestra los usuarios con sesión abierta.

**Ver sesiones con más detalle**

`w`

Muestra:

- Usuario.

- Terminal.

- Origen de la conexión.

- Hora de inicio.

- Qué comando está ejecutando.

**Ver los últimos inicios de sesión**

`last`

Lee el archivo `/var/log/wtmp`.

Muestra los últimos accesos al sistema.

**Ver quién se conectó a la fecha actual**

`last -10`

Muestra los 10 últimos inicios de sesión.

**Consultar usuarios desde el sistema**

`getent passwd`

Lee las fuentes de cuentas configuradas.

Puede incluir LDAP o Active Directory.

**Buscar un usuario específico**

`getent passwd carlos`

**Pista para el SOC**

`who` y `w` te dicen quién está ahora.

`last` te dice quién estuvo antes.

Esa línea de tiempo es oro en una investigación.

**10. `sudo` y `su`**

Son dos comandos parecidos.

Pero significan cosas distintas.

**`su`**

Significa **sustituir usuario**.

Cambia tu identidad a otro usuario.

`su carlos`

Cambia al usuario carlos.

Necesitas la contraseña de carlos.

**`su -`**

`su - root`

Inicia una sesión como `root`.

Carga el entorno de `root`.

Necesitas la contraseña de `root`.

**`sudo`**

Significa **superuser do**.

Ejecuta un solo comando con privilegios de otro usuario.

Normalmente de `root`.

`sudo cat /etc/shadow`

Pide la contraseña del **usuario actual**.

No la de `root`.

**Diferencia clave**

- `su` → cambias de usuario por completo.

- `sudo` → ejecutas un comando puntual como administrador.

**Ejemplo práctico**

Para ver los logs necesitas privilegios:

`sudo tail -f /var/log/auth.log`

Para cambiar a root durante un tiempo:

`sudo -i`

Para ejecutar como otro usuario:

`sudo -u mysql mysql`

**El archivo `/etc/sudoers`**

Define quién puede usar `sudo`.

Es un archivo delicado.

Se debe editar siempre con:

`sudo visudo`

`visudo` valida la sintaxis antes de guardar.

Evita errores que dejarían el sistema sin administrador.

**Líneas típicas de `/etc/sudoers`**

Permitir a un usuario todo:

`carlos ALL=(ALL:ALL) ALL`

Permitir a un grupo todo:

`%sudo ALL=(ALL:ALL) ALL`

Permitir solo comandos específicos:

`carlos ALL=(ALL) /usr/bin/systemctl`

Interpretación de los campos:

| **Campo**            | **Significado**                             |
|----------------------|---------------------------------------------|
| usuario o `%grupo`   | Quién tiene el permiso.                     |
| host                 | En qué máquina aplica (`ALL` = todas).      |
| (ALL:ALL)            | Puede ejecutar como cualquier usuario/grupo.|
| comando              | Qué comandos puede ejecutar.                |

**Pista para el SOC**

Revisar `/etc/sudoers` es parte de una auditoría.

Un usuario con permiso a `ALL` en un comando peligroso puede escalar.

**11. ¿Cómo aprovechan esto los atacantes?**

Los usuarios y grupos son un objetivo principal.

**Ataque 1 – Crear una cuenta nueva con UID 0**

El atacante ya es `root`.

Crea una cuenta que parece inocente:

`useradd -o -u 0 -g 0 backdoor`

Con UID 0, el sistema la trata como `root`.

Si borran el binario del atacante, la cuenta sigue ahí.

Es un mecanismo de **persistencia**.

**Cómo detectarlo**

- Buscar UID duplicados.

- Buscar cuentas con UID 0 que no sean `root`.

- Revisar `/etc/passwd` en busca de cuentas nuevas.

**Ataque 2 – Escalar privilegios vía `sudoers` mal configurado**

El atacante compromete una cuenta normal.

Descubre que la cuenta tiene permisos amplios en `sudo`.

Ejemplo:

`carlos ALL=(ALL:ALL) ALL`

Basta con saber su contraseña.

Ejecuta:

`sudo -i`

Y ya es `root`.

**Cómo detectarlo**

- Auditar quién está en el grupo `sudo`.

- Revisar los permisos de `/etc/sudoers`.

- Buscar cuentas con reglas demasiado amplias.

**Ataque 3 – Fuerza bruta SSH contra usuarios conocidos**

El atacante prueba contraseñas contra cuentas reales.

Primero descubre nombres de usuarios válidos.

Luego intenta:

- Contraseñas comunes.

- Contraseñas reutilizadas.

- Listas de diccionarios.

Si acierta, obtiene una sesión legítima.

**Cómo detectarlo**

En `/var/log/auth.log`:

Failed password for carlos from 203.0.113.9 port 52340 ssh2

Miles de líneas parecidas indican fuerza bruta.

**Ataque 4 – Robo de contraseñas débiles o reutilizadas**

Muchos usuarios usan contraseñas fáciles.

O la misma contraseña en varios sistemas.

Un atacante roba credenciales de otro sitio.

Y las prueba en el sistema Linux.

Esto se llama **credential stuffing**.

**Cómo detectarlo**

- Intentos de login desde <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> inusuales.

- Inicios de sesión en horarios extraños.

- Accesos exitosos seguidos de fallos.

**Ataque 5 – Modificar `/etc/passwd` o `/etc/sudoers` con permisos mal configurados**

Si los archivos tienen permisos incorrectos, es grave.

Por ejemplo:

- `/etc/passwd` escribible por cualquiera.

- `/etc/sudoers` modificable.

El atacante puede:

- Agregar una cuenta nueva.

- Agregarse al grupo `sudo`.

- Cambiar el UID de una cuenta existente.

**Cómo detectarlo**

- Verificar los permisos de los archivos.

- Auditar los cambios con el sistema de archivos.

- Monitorear archivos críticos.

**Pista para el SOC**

`/etc/passwd` y `/etc/shadow` solo deben modificarlos `root`.

Si ves que otro usuario puede escribirlos, es una vulnerabilidad crítica.

**12. ¿Cómo defenderse?**

**Política de contraseñas fuertes**

- Longitud mínima de 12 caracteres.

- Combinar letras, números y símbolos.

- No reutilizar contraseñas.

- Cambiarlas periódicamente.

**Bloquear cuentas innecesarias**

- Cuentas de ex empleados.

- Cuentas de servicios que ya no existen.

- Cuentas de prueba.

Ejemplo:

`passwd -l carlos_retirado`

**Principio de menor privilegio**

- Cada usuario solo tiene lo que necesita.

- Nadie es `root` por defecto.

- El grupo `sudo` tiene pocos miembros.

**Restringir sudo**

- Limitar comandos permitidos.

- Exigir contraseña.

- No dar `ALL=(ALL:ALL) ALL` a todos.

**Monitorear la creación de cuentas**

- Revisar `/etc/passwd` con frecuencia.

- Alertar ante cuentas nuevas.

- Alertar ante UID duplicados.

**Revisar `/etc/sudoers`**

- Auditar reglas periódicamente.

- Eliminar reglas innecesarias.

- Usar siempre `visudo`.

**Configurar expiración de contraseñas**

`chage -M 90 carlos`

`chage -d 0 carlos`

Así las contraseñas viejas pierden validez.

**Restringir SSH**

- Deshabilitar el login de `root` por SSH.

- Usar llaves en lugar de contraseñas.

- Limitar usuarios que pueden conectarse.

- Usar herramientas contra fuerza bruta.

**Mantener el sistema actualizado**

- Aplicar parches de seguridad.

- Mantener actualizados los servicios de autenticación.

**Pista para el SOC**

El menor privilegio es tu mejor amigo.

Cuantas menos cuentas con poder, menor superficie de ataque.

**13. Aplicación práctica en un SOC**

Vamos a resolver casos reales.

**Caso 1 – Revisar `/etc/passwd` buscando cuentas inusuales**

Comando:

`cat /etc/passwd`

Encuentras:

`sysadmin:x:0:0:Sistema:/root:/bin/bash`

¿Qué tiene de raro?

- UID 0.

- No se llama `root`.

Interpretación:

Una cuenta con UID 0 distinta de `root` es **muy sospechosa**.

Puede ser una **puerta trasera** creada por un atacante.

Acciones:

- Bloquear la cuenta.

- Revisar la fecha de creación del archivo.

- Buscar otros cambios.

**Caso 2 – Revisar `/var/log/auth.log` por intentos fallidos**

Comando:

`sudo grep "Failed password" /var/log/auth.log`

Encuentras:

Failed password for root from 203.0.113.9 port 52340 ssh2

Failed password for admin from 203.0.113.9 port 52341 ssh2

Failed password for carlos from 203.0.113.9 port 52342 ssh2

Interpretación:

Múltiples fallos desde la misma IP.

Usuarios probados en secuencia.

Es un patrón de **fuerza bruta**.

Acciones:

- Identificar la IP origen.

- Buscar intentos exitosos desde esa IP.

- Bloquear la IP en el firewall.

**Caso 3 – Auditar miembros del grupo sudo**

Comando:

`getent group sudo`

Salida:

sudo:x:27:carlos,maria

Compara con la lista oficial de administradores.

Preguntas:

- ¿Maria debería estar aquí?

- ¿Hubo cambios recientes?

Interpretación:

Un miembro inesperado puede significar una **escalada de privilegios**.

Acciones:

- Quitar al usuario no autorizado:

`sudo gpasswd -d maria sudo`

- Revisar quién lo agregó.

- Cambiar las contraseñas afectadas.

**Caso 4 – Verificar la shell de las cuentas**

Comando:

`awk -F: '{print $1, $7}' /etc/passwd`

Cuentas de servicio con shell de login:

`webapp:/bin/bash`

Interpretación:

`/bin/bash` indica que puede iniciar sesión.

Una cuenta de servicio debería usar:

- `/usr/sbin/nologin`.

- `/bin/false`.

Acciones:

`sudo usermod -s /usr/sbin/nologin webapp`

**Pista para el SOC**

En una investigación, siempre pregunta:

- ¿Qué cuenta hizo esto?

- ¿Cuándo se creó esa cuenta?

- ¿Qué privilegios tiene?

- ¿Entró alguien con ella?

**14. Lo que esperan de un Analista SOC Nivel 1**

En una entrevista o en el trabajo te harán preguntas como:

**¿Quién tiene acceso al sistema?**

Debes poder responder mirando `/etc/passwd` y `/etc/group`.

**¿Qué permisos tiene?**

Debes revisar grupos, shell y reglas de `sudo`.

**¿Hay cuentas nuevas?**

Debes comparar la lista actual con el histórico.

**¿Quién usa `sudo`?**

Debes revisar `/etc/sudoers` y los logs de `sudo`.

Comando:

`sudo grep "sudo" /var/log/auth.log`

**¿Hay fuerza bruta en curso?**

Debes revisar `/var/log/auth.log`.

Buscar:

- Muchos `Failed password`.

- Misma IP origen.

- Usuarios probados en secuencia.

- Accesos exitosos al final.

**Habilidades esperadas**

- Leer los 7 campos de `/etc/passwd`.

- Saber dónde están los hashes de contraseñas.

- Crear y eliminar cuentas.

- Agregar usuarios a grupos.

- Diferenciar `sudo` de `su`.

- Detectar cuentas sospechosas.

- Explicar por qué una cuenta con UID 0 es peligrosa.

**15. Resumen**

**Usuario**

- Identidad que puede iniciar sesión y ejecutar procesos.

- Se identifica por un UID.

**Tipos de usuarios**

- Normal (UID 1000+).

- De sistema (UID bajo).

- `root` (UID 0, poder total).

**`/etc/passwd`**

- 7 campos por línea.

- No guarda contraseñas.

- Guarda identidad, home y shell.

**`/etc/shadow`**

- Guarda los hashes de contraseñas.

- Solo lo puede leer `root`.

- Controla expiración y bloqueo.

**`/etc/group`**

- Define grupos y sus miembros.

- Usa GID.

**Comandos principales**

- `useradd` → crear usuario.

- `userdel -r` → eliminar usuario y su home.

- `usermod -aG` → agregar a un grupo.

- `passwd` → cambiar o bloquear contraseña.

- `chage` → expiración.

- `groupadd`, `groupdel`, `gpasswd` → grupos.

- `id`, `whoami`, `who`, `w`, `last` → consultas.

**`sudo` vs `su`**

- `su` → cambia de usuario.

- `sudo` → ejecuta un comando como administrador.

- `/etc/sudoers` controla quién puede usar `sudo`.

**Riesgos principales**

- Cuentas nuevas con UID 0.

- `sudoers` mal configurado.

- Fuerza bruta SSH.

- Contraseñas débiles.

- Permisos incorrectos en archivos de cuentas.

**🧠 Conceptos clave para memorizar**

| **Concepto** | **Debes recordar**                                           |
|--------------|--------------------------------------------------------------|
| UID          | Número único que identifica a un usuario.                    |
| root         | Superusuario con UID 0 y poder total.                        |
| `/etc/passwd`| 7 campos: usuario, x, UID, GID, comentario, home, shell.     |
| `/etc/shadow`| Almacena los hashes de contraseñas. Solo accesible por root. |
| `/etc/group` | Grupos y sus miembros. Formato: grupo:x:GID:miembros.        |
| `useradd`    | Crea usuarios. `-m` crea home, `-s` define shell.            |
| `usermod`    | Modifica usuarios. `-aG` agrega a un grupo sin reemplazar.   |
| `passwd`     | Cambia contraseñas. `-l` bloquea, `-u` desbloquea.           |
| `sudo`       | Ejecuta un comando con privilegios de administrador.         |
| `sudoers`    | Define quién puede usar `sudo`. Se edita con `visudo`.       |
| `chage`      | Controla expiración de contraseñas y cuentas.                |
| `id`         | Muestra UID, GID y grupos del usuario.                       |

**🎓 Consejo como tu instructor de SOC**

En un compromiso, los atacantes suelen crear cuentas para persistir.

No necesitan mantener el malware funcionando siempre.

Con una cuenta oculta en el sistema, pueden volver cuando quieran.

Un analista que revisa `/etc/passwd`, el grupo `sudo` y `auth.log`
tiene una gran ventaja.

Esa triple revisión descubre:

- Cuentas nuevas.

- Privilegios elevados.

- Intentos de acceso.

Memoriza esto:

**UID 0 = poder total.**

Cualquier cuenta con UID 0 es `root`, aunque se llame "carlos" o
"sysadmin".

Cuando veas un UID 0 que no es `root`, trata el caso como una
emergencia.

Y una última regla personal:

Nunca ejecutes `rm -rf` sobre la carpeta de un usuario comprometido
sin antes copiar sus archivos.

La evidencia vive en el disco.

La cuenta de un atacante puede ser la prueba de un incidente.

**📘 Carrera de Analista SOC**

**Semana 3 – Linux**

**Evaluación – Módulo 17: Gestión de Usuarios y Grupos**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material. Este examen está diseñado con el nivel de dificultad de una
entrevista para un **Analista SOC Nivel 1**. Encontrarás preguntas
conceptuales y casos prácticos basados en situaciones reales de un SOC.

**Pregunta 1**

¿Cuál es el **UID** del usuario `root` en Linux?

**A)** 1

**B)** 0

**C)** 100

**D)** 1000

**Pregunta 2**

¿En qué archivo se almacenan los **hashes de las contraseñas** de los
usuarios?

**A)** `/etc/passwd`

**B)** `/etc/sudoers`

**C)** `/etc/shadow`

**D)** `/etc/group`

**Pregunta 3**

¿Qué significa el campo `x` en la línea de `/etc/passwd`?

**A)** Que el usuario está bloqueado.

**B)** Que la contraseña está guardada en `/etc/shadow`.

**C)** Que el usuario es administrador.

**D)** Que el usuario no puede iniciar sesión.

**Pregunta 4**

¿Cuántos campos tiene cada línea de `/etc/passwd`?

**A)** 5

**B)** 6

**C)** 7

**D)** 9

**Pregunta 5**

¿Cuál es la función del comando `sudo`?

**A)** Cambiar permanentemente de usuario.

**B)** Ejecutar un comando puntual con privilegios de administrador.

**C)** Crear un nuevo usuario.

**D)** Eliminar la contraseña de un usuario.

**Pregunta 6**

¿Qué hace el comando `useradd -m -s /bin/bash carlos`?

**A)** Elimina al usuario carlos.

**B)** Crea al usuario carlos con home y shell `/bin/bash`.

**C)** Cambia la contraseña de carlos.

**D)** Agrega a carlos al grupo root.

**Pregunta 7**

¿Qué comando agrega al usuario `carlos` al grupo `sudo` sin reemplazar
sus grupos actuales?

**A)** `usermod -G sudo carlos`

**B)** `usermod -aG sudo carlos`

**C)** `groupadd -a sudo carlos`

**D)** `chage -a sudo carlos`

**Pregunta 8**

¿Qué archivo define quién puede usar `sudo` y con qué permisos?

**A)** `/etc/shadow`

**B)** `/etc/sudoers`

**C)** `/etc/passwd`

**D)** `/etc/login.defs`

**Pregunta 9**

Como analista SOC revisas `/var/log/auth.log` y encuentras:

Failed password for carlos from 203.0.113.9 port 52340 ssh2

Failed password for maria from 203.0.113.9 port 52341 ssh2

Failed password for root from 203.0.113.9 port 52342 ssh2

¿Cuál es la hipótesis más probable?

**A)** Un usuario olvidó su contraseña.

**B)** Un posible ataque de fuerza bruta contra SSH desde una misma IP.

**C)** Una actualización automática del sistema.

**D)** Un problema con el servicio DNS.

**Pregunta 10 (Caso práctico SOC)**

Durante una auditoría revisas `/etc/passwd` y encuentras:

sysadmin:x:0:0:Cuenta sistema:/root:/bin/bash

¿Qué implica esto?

**A)** Es una cuenta de servicio normal sin riesgo.

**B)** Es una cuenta legítima creada por el sistema.

**C)** Existe una cuenta con UID 0 distinta de `root`, lo que puede
indicar una puerta trasera creada por un atacante.

**D)** No tiene importancia porque el UID 0 no otorga privilegios.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: B**

**Justificación**

El usuario `root` tiene el **UID 0**.

Con UID 0, `root` tiene poder total sobre el sistema.

Cualquier cuenta con UID 0 se comporta como `root`.

**Pregunta 2**

✅ **Respuesta correcta: C**

**Justificación**

Los hashes de las contraseñas se guardan en **`/etc/shadow`**.

Este archivo solo puede leerlo `root`.

`/etc/passwd` solo guarda la identidad y marca el campo con una "x".

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

El campo `x` indica que la contraseña real está almacenada en
`/etc/shadow`.

Antiguamente las contraseñas vivían en `/etc/passwd`.

Por seguridad, se movieron a un archivo protegido.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

Cada línea de `/etc/passwd` tiene **7 campos**:

usuario:x:UID:GID:comentario:home:shell

Ejemplo:

root:x:0:0:root:/root:/bin/bash

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

`sudo` ejecuta un **comando puntual** con privilegios de administrador.

Pide la contraseña del usuario actual.

`su` sí cambia de usuario por completo.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

`useradd -m -s /bin/bash carlos`:

- Crea la cuenta de carlos.

- `-m` crea el home `/home/carlos`.

- `-s` asigna la shell `/bin/bash`.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

`usermod -aG sudo carlos`:

- `-a` → append (agregar).

- `-G` → grupo secundario.

Sin `-a`, `-G` reemplazaría todos los grupos del usuario.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

**`/etc/sudoers`** define quién puede usar `sudo`.

Se edita siempre con `visudo` para validar la sintaxis.

Ejemplo:

`%sudo ALL=(ALL:ALL) ALL`

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

Varios `Failed password` desde **la misma IP** con usuarios probados en
secuencia indican un posible **ataque de fuerza bruta contra SSH**.

Como analista deberías:

- Identificar la IP origen.

- Buscar intentos exitosos.

- Bloquear la IP si procede.

**Pregunta 10**

✅ **Respuesta correcta: C**

**Justificación**

La cuenta `sysadmin` tiene **UID 0** sin ser `root`.

En Linux, el UID 0 equivale a poder total.

Esta situación puede indicar una **puerta trasera** creada por un
atacante para mantener persistencia.

Acciones recomendadas:

- Bloquear la cuenta de inmediato.

- Revisar cuándo se creó.

- Auditar otros cambios en el sistema.

- Revisar los logs de autenticación.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Dominas la gestión de usuarios y puedes detectar cuentas sospechosas en una investigación.                                     |
| **8–9**                  | 🟢 **Muy buen nivel.** Interpretas `/etc/passwd`, `/etc/shadow` y los permisos `sudo` correctamente.                                            |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los comandos de creación de usuarios y la diferencia entre `sudo` y `su`.                                          |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Revisa los archivos de cuentas y el modelo de grupos.                                              |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** La gestión de usuarios es esencial para detectar persistencia y escalada de privilegios.      |
