**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 23: Usuarios, grupos y autenticación**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Administración + Seguridad + Detección SOC

En el módulo anterior vimos el sistema de archivos NTFS. Ahora nos
centramos en **quién** puede acceder a ese sistema: las cuentas, los
grupos y los mecanismos de autenticación. Para un SOC, entender la
identidad es tan importante como entender la red.

**🎯 Objetivos de este módulo**

Al terminar deberías poder explicar:

-   Qué es una cuenta de usuario local.
-   Diferencia entre usuario estándar y administrador.
-   Qué son los grupos y por qué se usan.
-   Qué es el UAC y cómo protege el sistema.
-   Qué es una contraseña, el bloqueo de cuenta y la política de bloqueo.
-   Diferencia entre los protocolos de autenticación **NTLM** y
    **Kerberos**.
-   Qué es **Active Directory** y por qué cambia la escala del análisis.

**1. Cuentas de usuario locales**

Windows identifica a cada persona o servicio mediante una **cuenta**. En
un equipo aislado existen las **cuentas locales**, almacenadas en la
base de datos **SAM** (`%SystemRoot%\System32\config\SAM`).

Ejemplos típicos:

-   `Administrador` (cuenta con privilegios totales).
-   `Invitado` (cuenta limitada, normalmente deshabilitada).
-   Cuentas de personas: `juan`, `Gonzalo`, `empleado01`.

Cada cuenta tiene un **RID** (Relative Identifier). Por ejemplo, el
administrador local siempre termina en `-500`. Esto es útil en
investigaciones: ver un RID `-500` significa que se usó la cuenta
administrador integrada.

**2. Usuario estándar vs Administrador**

Usuario estándar

↓

Menos privilegios

Administrador

↓

Control total sobre el equipo

Un Analista SOC debe preguntarse: **¿el proceso sospechoso se ejecutó
como administrador o como usuario estándar?** Un malware como usuario
estándar ya es grave, pero como administrador tiene libertad para
modificar el sistema, desactivar defensas y crear persistencia.

**3. Grupos**

En lugar de asignar permisos usuario por usuario:

Juan → permiso

Pedro → permiso

María → permiso

Se usa:

Grupo Finanzas

↓

Permisos

↓

Juan / Pedro / María

Grupos importantes en Windows:

-   **Administrators**: control total.
-   **Users**: usuarios estándar.
-   **Remote Desktop Users**: pueden iniciar sesión por Escritorio
    Remoto.
-   **Backup Operators**: pueden leer cualquier archivo (incluso los
    protegidos) para respaldos.
-   **Event Log Readers**: pueden leer logs (a veces abusado por
    atacantes para leer credenciales en logs).

**4. UAC (User Account Control)**

El UAC solicita confirmación cuando una acción requiere privilegios
elevados:

Aplicación quiere realizar cambios

↓

UAC

↓

¿Permitir?

Su objetivo es evitar que cualquier aplicación obtenga privilegios
administrativos en silencio. Un atacante intentará **eludir el UAC**
(con técnicas de escalada) para no mostrar ese aviso.

**5. Contraseñas y bloqueo de cuenta**

Una contraseña demuestra que quien intenta autenticarse es el dueño de
la cuenta. Windows puede aplicar:

-   Longitud y complejidad mínimas.
-   Caducidad.
-   **Política de bloqueo**: tras N intentos fallidos, la cuenta se
    bloquea durante un tiempo.

Para un SOC, muchos bloqueos seguidos de una misma cuenta pueden indicar
un **ataque de fuerza bruta** o un usuario que simplemente olvidó la
contraseña.

**6. NTLM vs Kerberos**

Son los <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> protocolos de autenticación principales de Windows.

NTLM (más antiguo):

-   Basado en un **desafío-respuesta** (challenge-response).
-   No requiere un servidor de autoridad central.
-   Más vulnerable a ataques como **Pass-the-Hash** y **brujula de
    fuerza bruta**.

Kerberos (dominio/Active Directory):

-   Basado en vales (**tickets**) emitidos por el **DC** (Domain
    Controller).
-   Usa un **TGT** (Ticket Granting Ticket) y luego **service tickets**.
-   Más seguro, pero introduce objetivos como el **DC** y ataques como
    **Kerberoasting** o **Golden Ticket**.

**7. Active Directory (introducción)**

Hasta ahora hablamos de un equipo solo. En empresas existen cientos de
equipos unidos a un **dominio** gestionado por **Active Directory
(AD)**.

En AD:

-   Las cuentas y grupos son **centralizados**.
-   Un usuario puede iniciar sesión en cualquier equipo del dominio.
-   Existen grupos poderosos como **Domain Admins**.

Para un SOC esto cambia la escala: un solo evento de un DC puede
afectar a toda la organización.

**8. ¿Por qué importa esto al SOC?**

-   **Cuenta nueva creada** → ¿fue legítima? (Event ID 4720).
-   **Usuario agregado a grupo privilegiado** → ¿aprobado? (Event ID
    4728).
-   **Muchos inicios fallidos** → ¿fuerza bruta? (Event ID 4625).
-   **Uso de la cuenta Administrador (-500)** → ¿debería usarse?
-   **Kerberoasting** → solicitudes masivas de service tickets.

**🧪 Laboratorio recomendado**

En tu Windows (o VM):

1.  `Win + R` → `lusrmgr.msc` para ver usuarios y grupos locales.
2.  Crea un usuario estándar y uno administrador.
3.  Agrega el usuario estándar al grupo `Remote Desktop Users`.
4.  `secpol.msc` → Directivas de bloqueo de cuenta: revisa el umbral de
    intentos fallidos.
5.  Observa en el Visor de eventos (`eventvwr.msc`) → Windows Logs →
    Security las entradas cuando creas usuarios.

**📝 Evaluación — Módulo 23: Usuarios, grupos y autenticación**

**Instrucciones:** elige una sola respuesta. No mires las soluciones
hasta terminar.

**🔹 Pregunta 1**

¿Qué base de datos local almacena las cuentas de usuario en un equipo
Windows independiente?

**A)** Registry\
**B)** SAM\
**C)** NTFS\
**D)** Active Directory

**🔹 Pregunta 2**

¿Cuál es la ventaja de asignar permisos a un grupo en lugar de a cada
usuario?

**A)** Las contraseñas caducan más rápido.\
**B)** Se administran muchos usuarios de forma centralizada.\
**C)** Windows deja de pedir UAC.\
**D)** Los archivos se cifran automáticamente.

**🔹 Pregunta 3**

El RID `-500` normalmente corresponde a:

**A)** Un usuario invitado.\
**B)** La cuenta Administrador integrada.\
**C)** El grupo Users.\
**D)** Una cuenta de servicio de red.

**🔹 Pregunta 4**

¿Cuál es la función principal del UAC?

**A)** Acelerar el inicio de sesión.\
**B)** Pedir confirmación antes de acciones con privilegios elevados.\
**C)** Bloquear la red.\
**D)** Cifrar el disco.

**🔹 Pregunta 5**

¿Qué protocolo de autenticación usa vales (tickets) emitidos por un
Controlador de Dominio?

**A)** NTLM\
**B)** Kerberos\
**C)** <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>\
**D)** <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

**🔹 Pregunta 6 — Caso SOC**

El SOC observa 50 eventos 4625 en 2 minutos para la cuenta `admin`. Lo
más probable es:

**A)** Una actualización de Windows.\
**B)** Un ataque de fuerza bruta.\
**C)** Un escaneo de antivirus.\
**D)** Un reinicio del equipo.

**🔹 Pregunta 7**

Un atacante con acceso de lectura al grupo **Event Log Readers** podría:

**A)** Apagar el servidor.\
**B)** Leer registros que quizá contienen credenciales.\
**C)** Crear usuarios nuevos.\
**D)** Desactivar el firewall.

**🔹 Pregunta 8**

¿Qué ataque aprovecha vales de servicio en Active Directory para
obtener hashes?

**A)** Kerberoasting\
**B)** Phishing\
**C)** Spoofing de <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>\
**D)** Ransomware

**🔹 Pregunta 9**

El grupo **Backup Operators** es peligroso porque:

**A)** No puede leer archivos.\
**B)** Puede leer cualquier archivo, incluso los protegidos, y abusarse
para extraer datos.\
**C)** Solo sirve para imprimir.\
**D)** Es igual que el grupo Users.

**🔹 Pregunta 10 — Caso SOC ⭐**

Un analista ve la creación de la cuenta `svc_backup` (Event ID 4720) y
su posterior agregación al grupo `Administrators` (Event ID 4728) fuera
del horario laboral. ¿Qué conclusión es más razonable?

**A)** Es mantenimiento rutinario normal.\
**B)** Debe investigarse como posible creación de persistencia con
privilegios altos.\
**C)** No tiene importancia.\
**D)** Significa que el equipo se apagó.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B — SAM**: almacena las cuentas y hashes locales.
2. **B**: los grupos permiten administrar permisos de forma centralizada.
3. **B**: el RID `-500` es la cuenta Administrador integrada.
4. **B**: el UAC pide confirmación para elevar privilegios.
5. **B — Kerberos**: usa TGT y service tickets desde el DC.
6. **B**: múltiples 4625 repetidos sugieren fuerza bruta.
7. **B**: puede leer logs que a veces contienen credenciales.
8. **A — Kerberoasting**: solicita service tickets para extraer hashes.
9. **B**: puede leer archivos protegidos y usarse para exfiltración.
10. **B**: crear cuenta y subirla a Administradores fuera de horario es
   bandera roja de persistencia.

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ⚪ Módulo 24 — Procesos y servicios
-   ⚪ Módulo 25 — CMD y PowerShell
-   ⚪ Módulo 26 — Windows Event Logs
-   ⚪ Módulo 27 — Seguridad de Windows
-   ⚪ Módulo 28 — Windows desde la perspectiva del atacante
-   ⚪ Módulo 29 — Investigación SOC en Windows
