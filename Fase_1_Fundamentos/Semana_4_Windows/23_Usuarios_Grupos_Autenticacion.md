**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 23: Usuarios, grupos y autenticación**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Windows + Seguridad + Detección SOC

Este módulo unifica la base (cuentas locales, grupos, UAC, NTLM/Kerberos, Active Directory) con la profundización completa (SID, SAM, mínimo privilegio, ataques a identidades) y el complementario Kerberos + Active Directory (KDC, TGT/TGS, SPN, Kerberoasting, Pass-the-Ticket, Golden Ticket).

**🎯 Objetivos del módulo**

Al finalizar deberías poder explicar qué es una cuenta, la diferencia local/dominio, grupos, SYSTEM, UAC, autenticación vs autorización, NTLM vs Kerberos, Active Directory (dominio, DC, OU, GPO), SID/RID, credenciales/SAM, escalada, movimiento lateral y qué observa un SOC (<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>/<a href="../../GLOSARIO.md#4625" target="_blank">4625</a>/4672/4720/4728).


---

## Parte A — Base: cuentas, grupos y autenticación

**1. Cuentas de usuario locales**

Windows identifica a cada persona o servicio mediante una **cuenta**. En
un equipo aislado existen las **cuentas locales**, almacenadas en la
base de datos **<a href="../../GLOSARIO.md#sam" target="_blank">SAM</a>** (`%SystemRoot%\System32\config\SAM`).

Ejemplos típicos:

-   `Administrador` (cuenta con privilegios totales).
-   `Invitado` (cuenta limitada, normalmente deshabilitada).
-   Cuentas de personas: `juan`, `Gonzalo`, `empleado01`.

Cada cuenta tiene un **<a href="../../GLOSARIO.md#rid" target="_blank">RID</a>** (Relative Identifier). Por ejemplo, el
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

Son los dos protocolos de autenticación principales de Windows.

NTLM (más antiguo):

-   Basado en un **desafío-respuesta** (challenge-response).
-   No requiere un servidor de autoridad central.
-   Más vulnerable a ataques como **<a href="../../GLOSARIO.md#pass-the-hash" target="_blank">Pass-the-Hash</a>** y pruebas de
    fuerza bruta.

Kerberos (dominio/Active Directory):

-   Basado en vales (**tickets**) emitidos por el **<a href="../../GLOSARIO.md#dc" target="_blank">DC</a>** (Domain
    Controller).
-   Usa un **<a href="../../GLOSARIO.md#tgt" target="_blank">TGT</a>** (Ticket Granting Ticket) y luego **service tickets**.
-   Más seguro, pero introduce objetivos como el **DC** y ataques como
    **<a href="../../GLOSARIO.md#kerberoasting" target="_blank">Kerberoasting</a>** o **<a href="../../GLOSARIO.md#golden-ticket" target="_blank">Golden Ticket</a>**.

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

-   **Cuenta nueva creada** → ¿fue legítima? (<a href="../../GLOSARIO.md#event-id" target="_blank">Event ID</a> 4720).
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

---

## Parte B — Profundización: usuarios, privilegios y detección

Ahora entramos en uno de los temas **más importantes de Windows para un
SOC**.

Hasta ahora aprendimos:

Módulo 1 → Cómo funciona Windows

Módulo 2 → Cómo se almacenan y protegen los archivos

Ahora vamos a responder:

**¿Quién está usando el equipo, cómo demuestra quién es, qué permisos
tiene y qué ocurrió cuando inició sesión?**

Esto nos llevará directamente a conceptos fundamentales de seguridad:

**usuarios → grupos → permisos → autenticación → privilegios → eventos →
detección.**

**🎯 Objetivos del módulo**

Al finalizar deberías poder explicar:

-   Qué es una cuenta de usuario.

-   Qué diferencia hay entre usuario local y usuario de dominio.

-   Qué son los grupos.

-   Qué es un administrador.

-   Qué es SYSTEM.

-   Qué es <a href="../../GLOSARIO.md#uac" target="_blank">UAC</a>.

-   Qué significa autenticación.

-   Qué diferencia existe entre autenticación y autorización.

-   Qué son <a href="../../GLOSARIO.md#ntlm" target="_blank">NTLM</a> y <a href="../../GLOSARIO.md#kerberos" target="_blank">Kerberos</a>.

-   Qué es <a href="../../GLOSARIO.md#active-directory" target="_blank">Active Directory</a>.

-   Qué es un <a href="../../GLOSARIO.md#sid" target="_blank">SID</a>.

-   Qué son las credenciales.

-   Cómo puede atacar un atacante las cuentas.

-   Qué debería observar un SOC.

**1. ¿Qué es una cuenta de usuario?**

Una cuenta de usuario representa una **identidad dentro del sistema**.

Por ejemplo:

Gonzalo

Juan

Maria

Administrador

Windows utiliza esa identidad para determinar:

¿Quién sos?

↓

¿Qué podés hacer?

↓

¿A qué recursos podés acceder?

**2. ¿Por qué Windows necesita usuarios?**

Imaginemos una empresa:

PC-CONTABILIDAD

Tenemos:

Juan

María

Pedro

No queremos que los tres tengan acceso a todo.

Por ejemplo:

Juan

↓

Documentos generales

María

↓

Contabilidad

Pedro

↓

Administración

Windows utiliza **cuentas + grupos + permisos** para controlar esto.

**3. Usuario ≠ permiso**

Esta distinción es fundamental.

El usuario es:

**Quién sos.**

El permiso determina:

**Qué podés hacer.**

Podemos representarlo:

USUARIO

↓

PERTENECE A GRUPOS

↓

RECIBE PERMISOS

↓

ACCEDE A RECURSOS

**4. Autenticación vs autorización**

Esta es una de las preguntas clásicas de entrevistas de ciberseguridad.

**🔐 Autenticación**

Responde:

**¿Quién sos?**

Ejemplo:

Usuario: Gonzalo

Contraseña: \*\*\*\*\*\*\*\*

Windows verifica las credenciales.

Si son correctas:

AUTENTICADO ✅

**🔑 Autorización**

Responde:

**¿Qué tenés permitido hacer?**

Ejemplo:

Gonzalo

↓

Autenticado ✅

↓

¿Puede modificar este archivo?

↓

NO ❌

Por lo tanto:

**Autenticación = demostrar identidad.**\
**Autorización = determinar permisos.**

Memorizá esta diferencia.

**5. Cuentas locales**

Una cuenta local existe **en ese equipo específico**.

Ejemplo:

PC-VENTAS-01

│

├── Gonzalo

├── Juan

└── Administrador

La cuenta pertenece a esa computadora.

Si creás:

Gonzalo

en:

PC-VENTAS-01

no significa automáticamente que exista la misma cuenta en:

PC-VENTAS-02

**6. Cuentas de dominio**

En una organización podemos tener muchas computadoras:

PC-VENTAS-01

PC-VENTAS-02

PC-RRHH-01

PC-CONTABILIDAD-01

SERVER-01

Administrar usuarios individualmente sería complicado.

Por eso se utilizan sistemas centralizados como:

**Active Directory**

Los usuarios pueden autenticarse contra un dominio corporativo.

Por ejemplo:

EMPRESA\\Gonzalo

**7. Active Directory**

**Active Directory (AD)** es una tecnología de Microsoft utilizada para
administrar identidades, equipos, grupos, políticas y recursos dentro de
un entorno de dominio.

Podemos imaginar:

ACTIVE DIRECTORY

│

┌───────────┼───────────┐

↓ ↓ ↓

Usuarios Grupos Equipos

│

↓

Políticas

En una empresa grande, esto es fundamental.

**8. Domain Controller**

El **Domain Controller (<a href="../../GLOSARIO.md#dc" target="_blank">DC</a>)** es un servidor que cumple funciones
centrales para el dominio de Active Directory.

Simplificando:

PC-VENTAS

↓

\"Quiero iniciar sesión\"

↓

Domain Controller

↓

¿Credenciales correctas?

↓

Sí

↓

Acceso

Esto es extremadamente importante para un SOC porque los **Domain
Controllers son activos críticos**.

Si un atacante compromete el entorno de Active Directory, puede obtener
un nivel de acceso enorme.

**9. Usuarios y grupos**

En Windows podemos asignar usuarios a grupos.

Ejemplo:

Gonzalo

Juan

Maria

│

↓

Grupo \"Contabilidad\"

El grupo puede tener permisos:

Contabilidad

↓

C:\\Empresa\\Finanzas

↓

Leer + Modificar

Así no tenemos que configurar permisos individualmente para cada
usuario.

**10. Grupos importantes**

En Windows existen grupos integrados.

Uno de los más importantes:

Administrators

Los miembros de este grupo tienen privilegios administrativos elevados.

Otros grupos pueden incluir:

Users

Guests

Backup Operators

Remote Desktop Users

Los nombres y composición exacta pueden variar según la edición y
configuración de Windows.

**11. ¿Por qué los grupos son importantes para un SOC?**

Porque un atacante que consigue agregar su cuenta a un grupo
privilegiado puede conseguir **persistencia o escalada de privilegios**.

Imaginemos:

Usuario comprometido

↓

Atacante

↓

agrega cuenta a Administrators

↓

privilegios elevados

Eso es una señal de seguridad muy importante.

**12. Principio de <a href="../../GLOSARIO.md#minimo-privilegio" target="_blank">mínimo privilegio</a>**

Una de las reglas fundamentales de seguridad:

**Cada usuario debe tener únicamente los privilegios necesarios para
realizar su trabajo.**

Ejemplo:

Un empleado que solamente necesita:

Word

Excel

Correo

no necesariamente necesita:

Administrador local

¿Por qué?

Porque si su cuenta es comprometida:

Usuario estándar comprometido

↓

Impacto limitado

mientras que:

Administrador comprometido

↓

Impacto potencialmente mucho mayor

**13. Cuenta Administrator**

Windows puede tener una cuenta administrativa integrada:

Administrator

Esta cuenta posee privilegios elevados.

Pero debemos entender algo:

**Administrador no significa que todo lo que haga esa cuenta sea
automáticamente seguro.**

Si un atacante obtiene control de una cuenta administrativa:

Administrador

↓

Atacante

↓

Mayor capacidad de modificar el sistema

**14. SYSTEM**

Ahora volvemos a un concepto que vimos en el módulo anterior.

Existe:

NT AUTHORITY\\SYSTEM

Esta identidad es utilizada por componentes y servicios de Windows.

Tiene privilegios extremadamente elevados dentro del sistema.

Ejemplo:

Proceso:

servicio.exe

Usuario:

NT AUTHORITY\\SYSTEM

Eso puede ser completamente normal.

Pero:

malware.exe

↓

SYSTEM

es una situación que requiere investigación inmediata.

**15. ¿Qué es un SID?**

Windows utiliza un identificador único para las cuentas llamado:

**SID --- Security Identifier**

Una cuenta puede verse conceptualmente así:

Usuario: Gonzalo

SID:

S-1-5-21-XXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXX-1001

No necesitás memorizar la estructura completa.

Lo importante es:

**Windows identifica las cuentas mediante SID, no simplemente por el
nombre visible.**

**16. ¿Por qué esto interesa al SOC?**

Imaginá que un atacante crea:

Usuario:

Administrador2

y después lo elimina.

El nombre puede desaparecer.

Pero durante una investigación pueden existir otros registros
relacionados con el SID y los eventos de seguridad.

Los identificadores ayudan a correlacionar actividad.

**17. Credenciales**

Las credenciales son información utilizada para demostrar una identidad.

Pueden incluir:

-   Usuario.

-   Contraseña.

-   Tokens.

-   Certificados.

-   Claves.

-   Otros factores de autenticación.

En Windows empresarial, las credenciales son uno de los objetivos
principales de los atacantes.

¿Por qué?

Porque:

Credencial comprometida

↓

Acceso

↓

Más privilegios

↓

Más sistemas

**18. Contraseñas**

Las contraseñas son un mecanismo de autenticación.

Pero una buena arquitectura de seguridad no debería depender únicamente
de ellas.

Por eso las organizaciones utilizan también:

-   <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>.

-   Smart cards.

-   Certificados.

-   Windows Hello.

-   Políticas de contraseñas.

**19. ¿Cómo almacena Windows las contraseñas?**

Este concepto es muy importante.

Windows **no debería almacenar las contraseñas en texto plano**.

En entornos locales, la información relacionada con las credenciales se
encuentra principalmente asociada a la **<a href="../../GLOSARIO.md#sam" target="_blank">SAM</a> (Security Account
Manager)**.

Simplificando:

Contraseña

↓

Proceso de autenticación

↓

Representación criptográfica

↓

Comparación

**20. ¿Qué es SAM?**

SAM significa:

**Security Account Manager**

Es un componente de Windows que almacena información relacionada con las
cuentas locales y sus credenciales.

En términos simplificados:

Cuentas locales

↓

SAM

↓

Información de autenticación

Por eso los atacantes suelen intentar obtener acceso a material
relacionado con SAM.

**21. ¿Qué es NTLM?**

**NTLM** es un protocolo/mecanismo de autenticación histórico de
Microsoft.

No necesitás todavía conocer todos sus detalles criptográficos.

Por ahora recordá:

Windows

↓

Autenticación

↓

NTLM

NTLM todavía puede aparecer en determinados entornos, aunque **Kerberos
es el protocolo principal para autenticación en dominios modernos de
Active Directory**.

**22. ¿Qué es Kerberos?**

Kerberos es un protocolo de autenticación utilizado ampliamente en
entornos de Active Directory.

Su característica fundamental es que utiliza un sistema basado en
**tickets**.

Simplificando:

Usuario

↓

Domain Controller

↓

Ticket

↓

Acceso a recursos

Esto evita tener que enviar continuamente la contraseña al acceder a
diferentes recursos.

**23. NTLM vs Kerberos**

  ----------------------------------------------------------------------------
  **Característica**   **NTLM**                  **Kerberos**
  -------------------- ------------------------- -----------------------------
  Tecnología de        ✅                        ✅
  Microsoft                                      

  Autenticación        ✅                        ✅

  Basado en tickets    ❌                        ✅

  Uso en AD moderno    Existe en escenarios      Principal
                       específicos               

  Seguridad moderna    Más limitada              Más robusta

  SOC                  Muy importante detectar   Muy importante analizar
                       usos anómalos             tickets y autenticación
  ----------------------------------------------------------------------------

**24. ¿Qué es UAC?**

Ya lo vimos anteriormente, pero ahora podemos relacionarlo con usuarios.

**UAC = User Account Control**

Supongamos que un usuario pertenece al grupo Administrators.

Eso **no significa necesariamente que todas sus aplicaciones se ejecuten
permanentemente con privilegios administrativos completos**.

UAC ayuda a controlar la elevación de privilegios.

Ejemplo:

Aplicación

↓

Necesita privilegios elevados

↓

UAC

↓

Confirmación

↓

Elevación

**25. ¿Qué es una escalada de privilegios?**

Es cuando un atacante consigue obtener privilegios superiores a los que
tenía inicialmente.

Ejemplo:

Usuario estándar

↓

Vulnerabilidad

↓

Administrador

O:

Cuenta comprometida

↓

Membresía en grupo privilegiado

↓

Mayor acceso

La escalada de privilegios es una etapa muy importante de muchos
ataques.

**26. ¿Cómo atacaría un atacante las cuentas?**

Desde la perspectiva defensiva podemos pensar en varias categorías.

**Fuerza bruta**

Intentar muchas contraseñas.

usuario

↓

password1

password2

password3

\...

**<a href="../../GLOSARIO.md#password-spraying" target="_blank">Password spraying</a>**

Intentar una contraseña común contra muchas cuentas.

Password123

↓

Juan

Pedro

Maria

Carlos

Esto puede ser especialmente peligroso porque puede generar menos
intentos por cuenta.

**<a href="../../GLOSARIO.md#credential-stuffing" target="_blank">Credential stuffing</a>**

Utilizar credenciales robadas de otros servicios.

usuario + contraseña filtrada

↓

intentar en otra organización

**Phishing**

Engañar al usuario para obtener sus credenciales.

Correo falso

↓

Página falsa

↓

Usuario introduce credenciales

↓

Atacante las obtiene

**27. Robo de credenciales**

Una vez que el atacante está dentro de un equipo, puede intentar obtener
material de autenticación.

Algunas técnicas conocidas incluyen:

-   Credential dumping.

-   Robo de tokens.

-   Extracción de credenciales almacenadas.

-   Ataques contra procesos que manejan credenciales.

No vamos a practicar estas técnicas ofensivamente sobre sistemas reales;
las estudiaremos desde el punto de vista de **detección y respuesta**.

**28. Movimiento lateral**

Este concepto será fundamental cuando estudiemos Active Directory.

Supongamos:

PC-01

↓

PC-02

↓

SERVER-01

↓

DOMAIN CONTROLLER

El atacante empieza en una máquina y trata de acceder a otras.

Esto se llama:

**Movimiento lateral**

**29. Ejemplo de ataque completo**

Podemos empezar a unir todo lo aprendido:

PHISHING

↓

Usuario entrega credenciales

↓

Atacante obtiene acceso

↓

Accede a PC-01

↓

Roba credenciales

↓

Escala privilegios

↓

Movimiento lateral

↓

Accede a servidor

↓

Intenta comprometer Active Directory

El SOC debe detectar las señales durante las distintas etapas.

**30. ¿Qué ve un SOC?**

Imaginemos que el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> muestra:

Usuario:

Gonzalo

10:01

Login fallido

10:02

Login fallido

10:03

Login fallido

10:04

Login exitoso

10:05

Nuevo proceso

10:07

Acceso a servidor

10:10

Cuenta agregada a grupo privilegiado

Esto es muchísimo más interesante que mirar un único evento.

El analista debe correlacionar:

AUTENTICACIÓN

↓

PROCESOS

↓

PRIVILEGIOS

↓

ACCESO A RECURSOS

↓

MOVIMIENTO LATERAL

**🚨 31. Eventos importantes que conoceremos**

Todavía no vamos a profundizar en <a href="../../GLOSARIO.md#event-viewer" target="_blank">Event Viewer</a> ---eso será nuestro
**Módulo 6**--- pero quiero que conozcas algunos eventos desde ahora.

**4624**

Logon exitoso

**4625**

Logon fallido

**4672**

Privilegios especiales asignados

**4720**

Usuario creado

**4728**

Miembro agregado a un grupo global con seguridad habilitada

Estos eventos serán fundamentales cuando lleguemos a **Windows Event
Logs**.

**🕵️ 32. Caso práctico SOC**

El SIEM genera:

PC-VENTAS-04

10:15

15 intentos fallidos

10:17

Login exitoso

Usuario:

ventas01

10:20

ventas01 agregado a grupo Administrators

10:22

<a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a> ejecutado

10:23

Conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

Como analista, esto debería levantar una alerta importante.

¿Por qué?

Porque vemos:

Intentos fallidos

↓

Login exitoso

↓

Elevación de privilegios

↓

PowerShell

↓

Comunicación de red

No podemos afirmar automáticamente que hubo compromiso.

Pero la **secuencia** es altamente relevante.

**🛡️ 33. ¿Cómo defenderse?**

**MFA**

Reduce el riesgo de que una contraseña robada sea suficiente.

**Mínimo privilegio**

Reduce el impacto de una cuenta comprometida.

**Políticas de contraseñas**

Dificultan ataques de fuerza bruta.

**Bloqueo / limitación de intentos**

Reduce ataques automatizados.

**Monitorización**

Detecta:

-   Login anormal.

-   Nuevos usuarios.

-   Cambios de grupos.

-   Escaladas.

-   Movimiento lateral.

**<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> + SIEM**

Permiten correlacionar identidad, procesos y red.

**🧠 34. Concepto fundamental: Identidad**

Quiero que empieces a ver una computadora de esta forma:

IDENTIDAD

│

┌─────────┴─────────┐

↓ ↓

USUARIO GRUPO

│ │

└─────────┬─────────┘

↓

PERMISOS

↓

ACCESO

↓

EVENTOS

↓

SOC

El SOC no solo vigila computadoras.

También vigila:

**Identidades.**

Porque muchas intrusiones modernas comienzan con una cuenta
comprometida.

**🧠 35. Conceptos que quiero que memorices**

  -----------------------------------------------------------------------
  **Concepto**        **Qué significa**
  ------------------- ---------------------------------------------------
  **Usuario**         Identidad que interactúa con el sistema

  **Grupo**           Conjunto de usuarios/identidades con permisos
                      comunes

  **Autenticación**   Verificar quién sos

  **Autorización**    Determinar qué podés hacer

  **SID**             Identificador de seguridad de una cuenta

  **SAM**             Componente que administra información de cuentas
                      locales

  **UAC**             Control de elevación de privilegios

  **NTLM**            Mecanismo/protocolo de autenticación de Microsoft

  **Kerberos**        Protocolo basado en tickets, principal en AD

  **Active            Servicio de directorio para gestionar identidades y
  Directory**         recursos

  **Domain            Servidor que proporciona funciones centrales del
  Controller**        dominio

  **Escalada de       Obtener privilegios superiores
  privilegios**       

  **Movimiento        Pasar de un sistema comprometido a otros
  lateral**           
  -----------------------------------------------------------------------

**🎯 La idea más importante del módulo**

Si mañana entrás a un SOC y te dicen:

**\"Tenemos una cuenta comprometida.\"**

No pienses solamente:

\"Hay que cambiar la contraseña.\"

Pensá:

¿Quién es el usuario?

↓

¿Dónde inició sesión?

↓

¿Desde qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

↓

¿A qué hora?

↓

¿Los intentos anteriores fallaron?

↓

¿Qué procesos ejecutó?

↓

¿Qué grupos tiene?

↓

¿Cambió sus privilegios?

↓

¿A qué otros equipos accedió?

↓

¿Utilizó esas credenciales para movimiento lateral?

Ahí empieza realmente el **análisis de identidad en un SOC**.


  **Módulo**                                                   **Estado**
  ------------------------------------------------------------ ------------
  1\. Fundamentos de Windows                                   ✅

  2\. NTFS y sistema de archivos                               ✅

  **3. Usuarios, grupos y autenticación**                      **✅**

  4\. Procesos y servicios                                     ⏳

  5\. <a href="../../GLOSARIO.md#cmd" target="_blank">CMD</a> y PowerShell                                         ⏳

  6\. Windows Event Logs                                       ⏳

  7\. Seguridad de Windows                                     ⏳

  8\. Windows desde la perspectiva del atacante                ⏳

  9\. Investigación SOC en Windows                             ⏳
  -------------------------------------------------------------------------

**🖥️ Carrera de Analista SOC**

**Semana 4 — Windows**

**📝 Examen --- Usuarios, Grupos y Autenticación**

**Nivel:** Principiante → Analista SOC Nivel 1

Vamos a mantener el formato que venimos usando: **10 preguntas Multiple
Choice** y, después de todas las preguntas, **respuestas con
justificación**.

Esta vez agrego varias situaciones de SOC para que no sea solamente
memoria.

**🔹 Pregunta 1**

¿Cuál es la diferencia principal entre **autenticación** y
**autorización**?

**A)** Autenticación determina qué permisos tiene un usuario y
autorización verifica su identidad.

**B)** Autenticación verifica la identidad y autorización determina qué
puede hacer.

**C)** Son exactamente lo mismo.

**D)** Autenticación solamente se utiliza en Internet y autorización
solamente en Windows.

**🔹 Pregunta 2**

¿Qué representa principalmente un **SID** en Windows?

**A)** La dirección IP de un equipo.

**B)** El nombre de una computadora.

**C)** Un identificador de seguridad asociado a una cuenta o entidad de
seguridad.

**D)** La contraseña cifrada de un usuario.

**🔹 Pregunta 3**

¿Cuál es la principal ventaja de utilizar grupos para administrar
permisos?

**A)** Permite eliminar la necesidad de autenticación.

**B)** Permite asignar permisos a un conjunto de usuarios de manera
centralizada.

**C)** Hace que todos los usuarios sean administradores.

**D)** Evita que los usuarios puedan iniciar sesión.

**🔹 Pregunta 4**

Una empresa tiene 500 empleados. Todos los empleados del departamento de
Finanzas necesitan acceder a:

C:\\Empresa\\Finanzas\\

¿Cuál sería una buena práctica?

**A)** Dar permisos individualmente a cada usuario y repetirlo cada vez
que ingrese un empleado.

**B)** Crear un grupo de seguridad para Finanzas y asignarle los
permisos necesarios.

**C)** Dar permisos de administrador a todos los empleados.

**D)** Hacer pública la carpeta.

**🔹 Pregunta 5**

¿Qué significa **principio de mínimo privilegio**?

**A)** Todos los usuarios deben tener privilegios de administrador.

**B)** Los usuarios deben tener únicamente los permisos necesarios para
realizar sus tareas.

**C)** Los administradores deben utilizar contraseñas cortas.

**D)** Los usuarios deben compartir una cuenta para facilitar la
administración.

**🔹 Pregunta 6**

¿Cuál de las siguientes afirmaciones sobre **Kerberos** es correcta?

**A)** Es un protocolo de autenticación basado en tickets utilizado
ampliamente en Active Directory.

**B)** Es un sistema de archivos de Windows.

**C)** Es un antivirus incluido en Windows.

**D)** Es un protocolo utilizado exclusivamente para <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**🔹 Pregunta 7 --- Caso SOC**

El SIEM detecta:

Usuario: ventas01

09:01 → Login fallido

09:02 → Login fallido

09:03 → Login fallido

09:04 → Login fallido

09:05 → Login exitoso

¿Qué debería hacer principalmente el analista?

**A)** Ignorar los eventos porque finalmente hubo un login exitoso.

**B)** Investigar la secuencia porque puede indicar un intento de fuerza
bruta o actividad sospechosa.

**C)** Eliminar automáticamente la cuenta.

**D)** Reiniciar el servidor.

**🔹 Pregunta 8 --- Caso SOC**

El SIEM muestra:

Usuario: empleado01

10:15 → Login exitoso

10:17 → Usuario agregado al grupo Administrators

10:18 → PowerShell ejecutado

10:20 → Conexión HTTPS hacia dominio desconocido

¿Cuál es la interpretación más adecuada?

**A)** Es definitivamente una actividad normal.

**B)** El login exitoso demuestra que no existe ningún problema.

**C)** La secuencia contiene múltiples indicadores que justifican una
investigación inmediata.

**D)** HTTPS significa que la actividad es segura.

**🔹 Pregunta 9 --- Concepto de ataque**

Un atacante intenta la siguiente contraseña:

Winter2026!

contra:

juan

maria

pedro

carlos

sofia

¿Qué técnica describe mejor este comportamiento?

**A)** Credential stuffing.

**B)** Password spraying.

**C)** SQL Injection.

**D)** DNS poisoning.

**🔹 Pregunta 10 --- Caso SOC ⭐**

Un atacante consigue comprometer las credenciales de:

usuario01

Luego utiliza esas credenciales para acceder a:

PC-VENTAS-01

↓

PC-CONTABILIDAD-02

↓

SERVER-FILES

¿Cómo se denomina principalmente este comportamiento?

**A)** Persistence.

**B)** Privilege escalation.

**C)** Lateral movement.

**D)** Data encryption.

**⛔ DETENTE AQUÍ**

Antes de mirar las respuestas, anotá tus elecciones:

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

Intentá resolverlas sin volver a mirar la explicación anterior.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**Pregunta 1**

**✅ B --- Autenticación verifica la identidad y autorización determina
qué puede hacer.**

La diferencia fundamental es:

AUTENTICACIÓN

↓

¿Quién sos?

AUTORIZACIÓN

↓

¿Qué podés hacer?

Ejemplo:

Usuario + contraseña

↓

Autenticación ✅

↓

Usuario identificado

↓

Permisos

↓

Autorización

Esta distinción aparece constantemente en seguridad informática.

**Pregunta 2**

**✅ C --- Un identificador de seguridad asociado a una cuenta o entidad
de seguridad.**

Windows utiliza los **Security Identifiers (SID)** para identificar
cuentas y otras entidades de seguridad.

Por ejemplo:

Usuario:

Gonzalo

SID:

S-1-5-21-\...\.....-1001

El nombre puede cambiar, pero el SID es el identificador utilizado por
Windows para distinguir la identidad.

Para un SOC esto es útil porque podemos correlacionar eventos
relacionados con una misma identidad.

**Pregunta 3**

**✅ B --- Permite asignar permisos a un conjunto de usuarios de manera
centralizada.**

Imaginá:

100 usuarios

↓

Grupo Finanzas

↓

Permisos

En lugar de configurar 100 usuarios individualmente, podemos administrar
el acceso mediante el grupo.

Esto facilita:

-   Administración.

-   Auditoría.

-   Cambios de personal.

-   Aplicación del mínimo privilegio.

**Pregunta 4**

**✅ B --- Crear un grupo de seguridad para Finanzas y asignarle los
permisos necesarios.**

Una estructura razonable sería:

Usuarios

↓

Grupo Finanzas

↓

Permisos

↓

C:\\Empresa\\Finanzas\\

Cuando ingresa un nuevo empleado:

Nuevo empleado

↓

Agregar al grupo

↓

Recibe los permisos correspondientes

Esto es mucho más escalable y controlable.

**Pregunta 5**

**✅ B --- Los usuarios deben tener únicamente los permisos
necesarios.**

El principio de mínimo privilegio busca reducir el impacto de una cuenta
comprometida.

Ejemplo:

Usuario estándar comprometido

↓

Impacto potencialmente limitado

Comparado con:

Administrador comprometido

↓

Mayor capacidad de modificar el sistema

↓

Mayor riesgo

Por eso **\"todos administradores\"** es una mala práctica de seguridad.

**Pregunta 6**

**✅ A --- Protocolo de autenticación basado en tickets utilizado
ampliamente en Active Directory.**

Kerberos utiliza tickets para permitir la autenticación y acceso a
recursos.

Simplificándolo:

Usuario

↓

Domain Controller

↓

Ticket

↓

Recurso

Esto es diferente de pensar simplemente:

Usuario → contraseña → cada recurso

Kerberos es fundamental para comprender la seguridad de **Active
Directory**.

**Pregunta 7**

**✅ B --- Investigar la secuencia.**

Tenemos:

Fallido

Fallido

Fallido

Fallido

↓

Exitoso

Esto puede ser compatible con un ataque de fuerza bruta, aunque **no
demuestra por sí solo** que exista un ataque.

Un analista debería investigar:

IP origen

↓

Ubicación

↓

Hora

↓

Usuario

↓

Cantidad de intentos

↓

Otros usuarios afectados

↓

Equipo de destino

La clave está en **correlacionar eventos**, no mirar solamente el login
exitoso.

**Pregunta 8**

**✅ C --- La secuencia contiene múltiples indicadores que justifican
una investigación inmediata.**

Tenemos:

Login

↓

Cambio de privilegios

↓

Administrators

↓

PowerShell

↓

Conexión externa

Cada evento individual podría tener una explicación legítima.

Pero juntos forman una cadena que merece atención.

Y recordá:

**HTTPS no significa que una conexión sea segura.**

HTTPS cifra la comunicación, pero un atacante también puede utilizar
HTTPS para comunicarse con infraestructura maliciosa.

**Pregunta 9**

**✅ B --- Password spraying**

Password spraying consiste, simplificando, en probar una contraseña
contra muchas cuentas:

Winter2026!

↓

Juan

María

Pedro

Carlos

Sofía

Mientras que un ataque de fuerza bruta tradicional suele concentrarse en
intentar muchas contraseñas contra una cuenta:

Juan

↓

Password1

Password2

Password3

Password4

\...

**Diferencia importante**

FUERZA BRUTA

1 cuenta

↓

muchas contraseñas

PASSWORD SPRAYING

muchas cuentas

↓

una o pocas contraseñas

Esto es **muy importante para un analista SOC**.

**Pregunta 10**

**✅ C --- Lateral movement**

El atacante pasa de:

PC-VENTAS-01

↓

PC-CONTABILIDAD-02

↓

SERVER-FILES

Eso es **movimiento lateral**.

La idea general:

El atacante ya consiguió acceso a un sistema y busca utilizarlo para
acceder a otros sistemas.

En una organización:

Equipo comprometido

↓

Credenciales

↓

Otro equipo

↓

Servidor

↓

Sistemas críticos

Por eso detectar movimiento lateral rápidamente es fundamental.

**🏆 TABLA DE RESULTADOS**

  -------------------------------------------------------------------------
  **Correctas**   **Evaluación**
  --------------- ---------------------------------------------------------
  **10/10**       🟢 Excelente --- muy buen dominio

  **8--9/10**     🟢 Muy buen nivel

  **6--7/10**     🟡 Bien, pero conviene reforzar conceptos

  **4--5/10**     🟠 Repasar antes de avanzar

  **0--3/10**     🔴 Recomiendo volver al módulo
  -------------------------------------------------------------------------

**🧠 BONUS --- Pregunta de Analista SOC**

Esta no cuenta para la nota.

El SIEM muestra:

Usuario: admin01

02:13 → 18 intentos fallidos

02:15 → Login exitoso

02:16 → Se agrega usuario nuevo

02:17 → Usuario nuevo agregado a Administrators

02:18 → PowerShell

02:20 → Acceso a SERVER-FILES

02:21 → Acceso a SERVER-DC01

Como futuro Analista SOC, ¿qué te preocupa más de toda la secuencia?

**La respuesta que quiero que empieces a desarrollar es:**

1\. Autenticación

↓

2\. Cambio de identidad/privilegios

↓

3\. Persistencia

↓

4\. Ejecución

↓

5\. Movimiento lateral

↓

6\. Posible objetivo crítico

Este es exactamente el tipo de razonamiento que vamos a profundizar
cuando lleguemos a **Windows Event Logs + SIEM**.


  **Módulo**                                                   **Estado**
  ------------------------------------------------------------ ------------
  1\. Fundamentos de Windows                                   ✅

  2\. NTFS y sistema de archivos                               ✅

  3\. Usuarios, grupos y autenticación                         ✅

  4\. Procesos y servicios                                     ⏳

  5\. CMD y PowerShell                                         ⏳

  6\. Windows Event Logs                                       ⏳

  7\. Seguridad de Windows                                     ⏳

  8\. Windows desde la perspectiva del atacante                ⏳

  9\. Investigación SOC en Windows                             ⏳
  -------------------------------------------------------------------------



---

## Parte C — Complemento: Kerberos + Active Directory

**1. Antes de empezar: el escenario**

Hasta ahora estudiamos una computadora Windows individual:

PC-01

│

├── Usuarios

├── Grupos

├── Archivos

├── Procesos

└── Servicios

Ahora imaginemos una empresa:

EMPRESA

│

┌─────────┴─────────┐

│ │

Usuarios Equipos

│ │

┌──────┼──────┐ ┌─────┼─────┐

↓ ↓ ↓ ↓ ↓ ↓

Juan María Pedro PC01 PC02 PC03

Necesitamos que todos esos usuarios puedan autenticarse y acceder a
recursos de forma **centralizada y controlada**.

Ahí entra:

**🏢 Active Directory**

Y dentro de ese ecosistema, uno de los mecanismos fundamentales de
autenticación es:

**🔐 Kerberos**

**PARTE I --- ACTIVE DIRECTORY**

**2. ¿Qué es Active Directory?**

**Active Directory (AD)** es un servicio de directorio de Microsoft que
permite administrar de forma centralizada identidades, equipos, grupos,
políticas y recursos de una organización.

Simplificándolo:

ACTIVE DIRECTORY

│

┌──────────────────┼──────────────────┐

↓ ↓ ↓

Usuarios Grupos Equipos

│ │ │

└──────────────────┼──────────────────┘

↓

Políticas

Por ejemplo, una empresa podría tener:

Dominio:

empresa.local

Y dentro:

Usuarios:

├── juan

├── maria

├── pedro

└── administrador

Equipos:

├── PC-VENTAS-01

├── PC-RRHH-01

├── PC-CONTABILIDAD-01

└── SERVER-FILES

Grupos:

├── Ventas

├── RRHH

├── Contabilidad

└── Administrators

**3. ¿Qué problema soluciona Active Directory?**

Sin AD, imaginemos que tenemos:

500 empleados

100 computadoras

20 servidores

Administrar individualmente:

-   usuarios,

-   contraseñas,

-   grupos,

-   permisos,

-   políticas,

sería extremadamente complicado.

Con Active Directory podemos centralizar gran parte de esa
administración.

Por ejemplo:

Nuevo empleado

↓

Crear cuenta

↓

Agregar a grupos

↓

Aplicar políticas

↓

Acceso a recursos

**4. ¿Qué es un dominio?**

Un **dominio de Active Directory** es un entorno lógico que contiene
identidades y recursos administrados de forma centralizada.

Ejemplo:

EMPRESA.LOCAL

Dentro del dominio podemos tener:

Usuarios

Computadoras

Servidores

Grupos

Políticas

Un usuario podría identificarse como:

EMPRESA\\juan

o mediante el formato UPN:

juan@empresa.local

**5. ¿Qué es un Domain Controller?**

Uno de los conceptos más importantes:

**Domain Controller (<a href="../../GLOSARIO.md#dc" target="_blank">DC</a>)**

Es un servidor que proporciona funciones centrales del dominio de Active
Directory, incluida la autenticación.

Podemos imaginar:

DOMAIN CONTROLLER

│

┌─────────┴─────────┐

↓ ↓

Autenticación Directorio

│ │

↓ ↓

Usuarios Grupos

Por eso un Domain Controller es un **activo extremadamente crítico**.

Si un atacante consigue comprometerlo, el impacto potencial sobre toda
la organización puede ser enorme.

**6. ¿Qué guarda Active Directory?**

Active Directory contiene información sobre objetos del directorio.

Entre ellos:

Usuarios

Grupos

Computadoras

Servidores

Impresoras

Servicios

Políticas

Podemos representarlo:

AD

│

┌────────────┼────────────┐

↓ ↓ ↓

Usuario Grupo Equipo

│

↓

Permisos

│

↓

Recursos

**7. Organizational Units --- <a href="../../GLOSARIO.md#ou" target="_blank">OU</a>**

Dentro de Active Directory podemos organizar objetos mediante:

**Organizational Units (OU)**

Por ejemplo:

EMPRESA

│

├── OU=Ventas

│ ├── Juan

│ ├── Pedro

│ └── PC-Ventas-01

│

├── OU=RRHH

│ ├── Maria

│ └── PC-RRHH-01

│

└── OU=IT

├── Admin01

└── PC-IT-01

Las OU permiten organizar y administrar objetos.

**8. Group Policy --- <a href="../../GLOSARIO.md#gpo" target="_blank">GPO</a>**

Otra pieza fundamental son las:

**Group Policy Objects (GPO)**

Las GPO permiten aplicar configuraciones y políticas a usuarios y
equipos.

Por ejemplo:

GPO

│

├── Política de contraseñas

├── Configuración de Windows

├── Restricciones

├── Firewall

└── Configuraciones de seguridad

Ejemplo:

OU=Ventas

↓

GPO

↓

Bloquear pantalla después de 10 minutos

Esto permite administrar cientos o miles de equipos de forma
centralizada.

**9. ¿Por qué un SOC se interesa por las GPO?**

Porque las políticas pueden ser modificadas por un atacante.

Imaginemos:

Atacante

↓

Compromete cuenta privilegiada

↓

Modifica GPO

↓

La política se aplica

↓

Muchos equipos afectados

Una modificación sospechosa de una GPO puede convertirse en una alerta
crítica.

**10. Active Directory y confianza**

En organizaciones grandes pueden existir varios dominios y relaciones de
confianza.

Por ejemplo:

DOMINIO-A

│

│ Trust

↓

DOMINIO-B

Las relaciones de confianza permiten determinadas interacciones entre
dominios.

Desde seguridad:

**Una relación de confianza mal configurada o abusada puede ampliar el
impacto de un compromiso.**

**🔐 PARTE II --- KERBEROS**

Ahora que entendemos Active Directory podemos estudiar Kerberos.

**11. ¿Qué es Kerberos?**

Kerberos es un protocolo de autenticación basado en **tickets**.

Su objetivo principal es permitir que un usuario demuestre su identidad
y acceda a servicios de una red sin tener que enviar continuamente su
contraseña a cada servicio.

La idea básica:

Usuario

↓

Autenticación

↓

Ticket

↓

Servicio

**12. ¿Por qué usar tickets?**

Imaginemos que Juan inicia sesión y necesita acceder a:

FILESERVER

MAILSERVER

DATABASE

PRINTSERVER

No queremos que Juan tenga que introducir su contraseña nuevamente para
cada recurso.

Kerberos utiliza tickets para facilitar este proceso.

Conceptualmente:

Juan

↓

Autenticación

↓

Ticket inicial

↓

Solicita tickets de servicios

↓

Accede a recursos

**13. <a href="../../GLOSARIO.md#kdc" target="_blank">KDC</a>**

Ahora aparece una pieza fundamental:

**KDC --- Key Distribution Center**

El KDC es el componente central de Kerberos encargado de participar en
la emisión y gestión de tickets.

Conceptualmente contiene dos servicios:

KDC

│

├── <a href="../../GLOSARIO.md#as" target="_blank">AS</a> --- Authentication Service

│

└── <a href="../../GLOSARIO.md#tgs" target="_blank">TGS</a> --- Ticket Granting Service

No hace falta memorizar todavía todos los detalles criptográficos.

Lo importante es entender el flujo.

**14. Authentication Service --- AS**

El **Authentication Service** participa en la autenticación inicial.

Simplificando:

Usuario

↓

\"Quiero autenticarme\"

↓

AS

↓

Verificación

↓

<a href="../../GLOSARIO.md#tgt" target="_blank">TGT</a>

El resultado importante es obtener un:

**🎟️ TGT**

**15. ¿Qué es un TGT?**

**TGT = Ticket Granting Ticket**

Es un ticket que permite al usuario solicitar posteriormente tickets
para servicios concretos.

Podemos imaginarlo como una especie de:

\"credencial temporal que permite solicitar otras credenciales de
servicio\".

El flujo:

Usuario

↓

AS

↓

TGT

↓

TGS

**16. Ticket Granting Service --- TGS**

El **TGS** recibe una solicitud basada en el TGT y puede emitir un
ticket para un servicio específico.

Por ejemplo:

Juan

↓

TGT

↓

TGS

↓

\"Quiero acceder a FILESERVER\"

↓

<a href="../../GLOSARIO.md#service-ticket" target="_blank">Service Ticket</a>

**17. Service Ticket**

Ahora tenemos un ticket específico para un servicio.

Ejemplo:

Juan

↓

TGS

↓

Ticket para FILESERVER

↓

FILESERVER

↓

Acceso

Esto es una de las ideas más importantes de Kerberos.

**18. El flujo completo**

Ahora juntamos todo:

KERBEROS

Usuario

│

│ 1. Autenticación

↓

AS

│

│

↓

TGT

│

│ 2. Solicita acceso

↓

TGS

│

│ 3. Ticket de servicio

↓

Service Ticket

│

│ 4. Acceso

↓

Servidor

Memorizá esta estructura.

**19. Ejemplo real**

Juan inicia sesión:

EMPRESA\\juan

Quiere acceder a:

\\\\FILESERVER\\FINANZAS

Conceptualmente:

Juan

↓

Kerberos

↓

TGT

↓

Solicita ticket para FILESERVER

↓

TGS

↓

Service Ticket

↓

FILESERVER

↓

Acceso autorizado

**20. ¿Dónde entra Active Directory?**

Acá está la conexión importante:

ACTIVE DIRECTORY

│

↓

DOMAIN CONTROLLER

│

↓

KDC

│

↓

KERBEROS

│

↓

AUTENTICACIÓN

En un dominio Windows moderno, Active Directory y Kerberos trabajan
estrechamente juntos.

**21. ¿Kerberos guarda las contraseñas?**

No debemos pensar:

Kerberos

↓

guarda contraseñas

El protocolo utiliza mecanismos criptográficos y secretos asociados a
las identidades para realizar la autenticación y emitir tickets.

La contraseña se utiliza durante la autenticación inicial, pero Kerberos
está diseñado para que no sea necesario enviarla repetidamente a cada
servicio.

**22. ¿Qué es un <a href="../../GLOSARIO.md#spn" target="_blank">SPN</a>?**

Ahora entramos en un concepto importante para SOC:

**SPN --- Service Principal Name**

Un SPN identifica una instancia de servicio asociada a una cuenta dentro
de Kerberos.

Por ejemplo, conceptualmente:

SERVICIO/servidor

Un servicio podría estar asociado a:

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>/webserver

MSSQLSvc/database

HOST/server01

No necesitás memorizar estos formatos todavía.

Lo importante es entender:

**Kerberos necesita saber para qué servicio se solicita un ticket.**

**23. ¿Por qué SPN importa para seguridad?**

Porque determinadas cuentas de servicio asociadas con SPN pueden
convertirse en objetivos para técnicas de ataque como:

**<a href="../../GLOSARIO.md#kerberoasting" target="_blank">Kerberoasting</a>**

No vamos a ejecutar la técnica ahora.

Primero queremos comprender el concepto.

**24. ¿Qué es Kerberoasting?**

Desde una perspectiva defensiva:

Atacante

↓

Obtiene información de servicios

↓

Solicita determinados tickets

↓

Obtiene material asociado al ticket

↓

Intenta atacarlo offline

↓

Busca recuperar una contraseña

El objetivo suele ser encontrar cuentas de servicio con contraseñas
débiles.

**Para el SOC:**

Podríamos buscar comportamientos anómalos relacionados con:

-   Solicitudes de tickets.

-   Cuentas que normalmente no solicitan determinados servicios.

-   Volúmenes inusuales.

-   Cuentas de servicio.

-   Actividad posterior a la obtención de credenciales.

**25. <a href="../../GLOSARIO.md#pass-the-ticket" target="_blank">Pass-the-Ticket</a>**

Otro concepto que debemos conocer.

Supongamos que un atacante obtiene un ticket Kerberos válido.

Puede intentar utilizar ese ticket para autenticarse ante servicios.

Conceptualmente:

Atacante

↓

Obtiene ticket

↓

Utiliza ticket

↓

Accede a servicio

Esto se conoce como:

**Pass-the-Ticket**

Para un SOC es importante porque puede existir actividad de
autenticación sin que necesariamente veamos el patrón habitual de una
contraseña introducida por el usuario.

**26. <a href="../../GLOSARIO.md#golden-ticket" target="_blank">Golden Ticket</a>**

Ahora llegamos a una técnica mucho más avanzada.

Un **Golden Ticket** está relacionado con la falsificación de TGTs
mediante el compromiso de un secreto extremadamente importante del
dominio: la clave asociada a la cuenta **<a href="../../GLOSARIO.md#krbtgt" target="_blank">KRBTGT</a>**.

Conceptualmente:

Compromiso crítico del dominio

↓

Secreto KRBTGT

↓

Atacante puede intentar

crear TGTs falsificados

↓

Acceso potencialmente amplio

Esto es **nivel avanzado**.

Por ahora solamente quiero que entiendas:

**Golden Ticket = amenaza muy grave relacionada con Kerberos y el
dominio.**

**27. ¿Por qué KRBTGT es tan importante?**

La cuenta:

KRBTGT

es una cuenta especial utilizada por Kerberos en Active Directory.

Su secreto criptográfico tiene un papel fundamental en la
emisión/validación de determinados tickets.

Por eso:

KRBTGT comprometida

↓

RIESGO EXTREMADAMENTE ALTO

**28. ¿Qué es <a href="../../GLOSARIO.md#pass-the-hash" target="_blank">Pass-the-Hash</a>?**

Ahora comparemos con otra técnica.

**Pass-the-Hash** consiste, a grandes rasgos, en utilizar un **hash de
credencial** obtenido de un sistema para intentar autenticarse sin
conocer la contraseña original.

Conceptualmente:

Contraseña

↓

Hash

↓

Atacante obtiene hash

↓

Intenta autenticarse

No debemos confundirlo con Pass-the-Ticket:

  -----------------------------------------------------------------------------
  **Técnica**           **Material utilizado**
  --------------------- -------------------------------------------------------
  **Pass-the-Hash**     Hash/material de autenticación asociado a una
                        contraseña

  **Pass-the-Ticket**   Ticket Kerberos
  -----------------------------------------------------------------------------

**29. Kerberos vs <a href="../../GLOSARIO.md#ntlm" target="_blank">NTLM</a>**

Ahora podemos entender mejor la diferencia.

  ------------------------------------------------------------------------------
  **Característica**                      **NTLM**                **Kerberos**
  --------------------------------------- ----------------------- --------------
  Autenticación                           ✅                      ✅

  Basado en tickets                       ❌                      ✅

  Uso en Active Directory                 Sí, en escenarios       Principal
                                          específicos             

  Diseñado para entornos modernos de      Menos adecuado          Sí
  dominio                                                         

  Importancia para SOC                    Alta                    Muy alta
  ------------------------------------------------------------------------------

No significa que:

\"NTLM = malo\"

y:

\"Kerberos = imposible de atacar\".

Ambos pueden ser objeto de ataques.

**30. ¿Cómo piensa un atacante?**

Supongamos que compromete una PC:

PC-VENTAS-01

↓

Usuario Juan

↓

Atacante

Ahora empieza a buscar:

¿Qué credenciales existen?

¿Qué usuarios tienen privilegios?

¿Qué grupos existen?

¿Qué servidores puedo alcanzar?

¿Qué servicios utilizan Kerberos?

¿Qué cuentas de servicio existen?

¿Puedo moverme lateralmente?

Su objetivo puede ser:

PC

↓

Servidor

↓

Servidor crítico

↓

Domain Controller

↓

Dominio

**31. ¿Cómo piensa el SOC?**

El SOC debe hacer exactamente lo contrario.

Si observa:

PC-VENTAS-01

↓

Juan

↓

Autenticación

↓

Servidor inesperado

↓

Otro servidor

↓

DC

debe preguntarse:

**¿Por qué este usuario está accediendo a esos sistemas?**

No basta con decir:

\"El login fue exitoso.\"

Tenemos que analizar el **contexto**.

**32. El contexto es fundamental**

Un login exitoso puede ser completamente normal:

Juan

↓

PC-Ventas

↓

FILESERVER

Pero:

Juan

↓

PC-Ventas

↓

Domain Controller

↓

Servidor de RRHH

↓

Servidor de Backup

puede ser muy diferente.

El evento aislado:

4624

nos dice que hubo un inicio de sesión exitoso.

Pero el SOC necesita contexto:

Quién

Desde dónde

Cuándo

Hacia dónde

Qué tipo de logon

Qué hizo después

**33. Tipos de Logon**

Este concepto será muy útil cuando lleguemos a Windows Event Logs.

Windows registra diferentes tipos de inicio de sesión.

Por ejemplo:

  -----------------------------------------------------------------------
  **<a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a>**         **Concepto general**
  ---------------------- ------------------------------------------------
  **2**                  Interactivo

  **3**                  Network

  **4**                  Batch

  **5**                  Service

  **7**                  Unlock

  **10**                 Remote Interactive / RDP
  -----------------------------------------------------------------------

No necesitás memorizarlos todos todavía.

Pero quiero que conozcas especialmente:

**Type 2**

Usuario inicia sesión localmente

**Type 3**

Acceso a través de red

**Type 10**

RDP / sesión remota

Esto será muy útil para detectar comportamiento sospechoso.

**34. Ejemplo de análisis SOC**

Tenemos:

Usuario:

juan

Origen:

PC-VENTAS-01

Destino:

SERVER-RRHH

Logon Type:

3

Hora:

03:14

El SOC debería preguntarse:

¿Juan normalmente accede a RRHH?

¿Es normal que ocurra a las 03:14?

¿PC-VENTAS-01 debería acceder a ese servidor?

¿Hubo otros logins?

¿Hubo PowerShell?

¿Se copiaron archivos?

Ese es el razonamiento que queremos desarrollar.

**35. Active Directory como \"mapa\" de la empresa**

Una forma sencilla de entender AD:

DOMINIO

│

┌──────────┼──────────┐

↓ ↓ ↓

Usuarios Grupos Equipos

│ │ │

└──────────┼──────────┘

↓

Permisos

↓

Recursos

Para un atacante, este mapa es extremadamente valioso.

Para el SOC también.

**36. ¿Qué busca un atacante dentro de AD?**

Desde una perspectiva defensiva, podemos agrupar sus objetivos:

**Identidad**

Usuarios

**Privilegios**

Administrators

Domain Admins

**Equipos**

Servidores

Domain Controllers

**Relaciones**

Grupos

Permisos

Trusts

**Servicios**

SPN

Cuentas de servicio

**37. Domain Admins**

Uno de los grupos más sensibles en un dominio tradicional de Active
Directory es:

Domain Admins

Sus miembros poseen privilegios extremadamente elevados dentro del
dominio.

Por eso un evento como:

Usuario normal

↓

Agregado a Domain Admins

debería generar una **investigación inmediata**, salvo que exista una
justificación administrativa clara.

**38. El camino hacia el compromiso del dominio**

Un escenario simplificado podría ser:

Phishing

↓

Credencial robada

↓

Cuenta de usuario

↓

PC comprometida

↓

Robo de credenciales

↓

Escalada

↓

Movimiento lateral

↓

Cuenta privilegiada

↓

Domain Admin

↓

Domain Controller

Este tipo de cadena es exactamente lo que queremos aprender a detectar.

**39. ¿Cómo se defiende Active Directory?**

No existe una única defensa.

Se utiliza una combinación de controles.

**🔐 <a href="../../GLOSARIO.md#mfa" target="_blank">MFA</a>**

Reduce el impacto de credenciales robadas.

**👤 <a href="../../GLOSARIO.md#minimo-privilegio" target="_blank">Mínimo privilegio</a>**

Reduce cuentas con privilegios excesivos.

**🏢 Segmentación**

Limita qué equipos pueden comunicarse con otros.

**🔎 Monitorización**

Permite detectar:

-   Logins anormales.

-   Cambios de grupos.

-   Nuevos usuarios.

-   Actividad administrativa.

-   Movimiento lateral.

**🛡️ <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>**

Permite relacionar:

Usuario

\+

Proceso

\+

Equipo

\+

Red

**📋 SIEM**

Centraliza y correlaciona eventos.

**40. ¿Qué debería observar un SOC?**

Cuando veamos una alerta de autenticación, quiero que empieces a pensar:

┌─────────────────────────────┐

│ IDENTIDAD │

├─────────────────────────────┤

│ Usuario │

│ Grupo │

│ Privilegios │

│ Equipo origen │

│ Equipo destino │

│ Hora │

│ Tipo de logon │

│ Protocolo │

│ Kerberos / NTLM │

│ Procesos posteriores │

│ Accesos posteriores │

└─────────────────────────────┘

**41. Caso práctico completo**

Ahora vamos a hacer un pequeño análisis.

El SIEM muestra:

03:02

Usuario: juan

Login fallido

03:03

Usuario: juan

Login exitoso

03:05

PC-VENTAS-01 → SERVER-FILES

Kerberos

03:07

PC-VENTAS-01 → SERVER-RRHH

Kerberos

03:09

PC-VENTAS-01 → DC01

Kerberos

03:10

PowerShell ejecutado

03:12

Usuario agregado a grupo privilegiado

No podemos decir todavía:

\"Es un ataque confirmado.\"

Pero tenemos suficientes señales para investigar.

**42. ¿Qué investigaríamos?**

**1️⃣ Usuario**

¿Quién es Juan?

**2️⃣ Equipo**

¿PC-VENTAS-01 pertenece realmente a Juan?

**3️⃣ Hora**

¿03:00 es un horario normal?

**4️⃣ Autenticación**

¿Desde dónde se produjo?

**5️⃣ Kerberos**

¿Qué tickets fueron solicitados?

**6️⃣ Acceso**

¿Por qué Juan accedió a RRHH?

**7️⃣ PowerShell**

¿Qué comando ejecutó?

**8️⃣ Privilegios**

¿Quién lo agregó al grupo?

**9️⃣ Alcance**

¿Otros equipos fueron afectados?

**43. Lo que quiero que te quede grabado**

No quiero que memorices 50 términos.

Quiero que entiendas esta cadena:

ACTIVE DIRECTORY

│

↓

USUARIO

│

↓

AUTENTICACIÓN

│

↓

KERBEROS

│

┌──────┴──────┐

↓ ↓

TGT TGS

│

↓

SERVICE TICKET

│

↓

SERVICIO

│

↓

ACCESO

│

↓

EVENT LOG

│

↓

SIEM

│

↓

ANALISTA SOC

Ese último tramo es el que más nos interesa.

**🧠 44. Diccionario rápido**

  --------------------------------------------------------------------------------
  **Término**           **Significado**
  --------------------- ----------------------------------------------------------
  **Active Directory**  Servicio de directorio de Microsoft

  **AD**                Abreviatura de Active Directory

  **Domain**            Entorno lógico del directorio

  **DC**                Domain Controller

  **OU**                Organizational Unit

  **GPO**               Group Policy Object

  **KDC**               Key Distribution Center

  **AS**                Authentication Service

  **TGS**               Ticket Granting Service

  **TGT**               Ticket Granting Ticket

  **SPN**               Service Principal Name

  **Service Ticket**    Ticket para acceder a un servicio

  **Kerberos**          Protocolo de autenticación basado en tickets

  **NTLM**              Mecanismo/protocolo de autenticación de Microsoft

  **Pass-the-Hash**     Abuso de material de autenticación basado en hash

  **Pass-the-Ticket**   Abuso de tickets Kerberos

  **Kerberoasting**     Ataque dirigido a determinadas cuentas de servicio
                        mediante tickets Kerberos

  **Golden Ticket**     Falsificación de TGTs tras comprometer secretos críticos
                        de Kerberos

  **KRBTGT**            Cuenta especial utilizada por Kerberos en AD
  --------------------------------------------------------------------------------

**🎯 45. Lo importante para tu carrera SOC**

Quiero que veas por qué agregamos este módulo adicional.

En el futuro vas a recibir una alerta que diga algo parecido a:

Suspicious Authentication Activity

User: juan

Source: 10.10.20.15

Destination: DC01

Logon Type: 3

Authentication: Kerberos

Y ya no vas a pensar solamente:

\"Ah, hubo una autenticación.\"

Vas a pensar:

¿Quién?

↓

¿Desde qué equipo?

↓

¿Por qué accede al DC?

↓

¿Es normal para ese usuario?

↓

¿Qué tickets solicitó?

↓

¿Qué hizo después?

↓

¿Hubo movimiento lateral?

↓

¿Se modificaron privilegios?

**Ese cambio de mentalidad es exactamente lo que buscamos durante tu
formación como futuro Analista SOC.**

**📚 Cómo encaja en nuestra Semana 4**

No vamos a alterar el plan principal:

SEMANA 4 --- WINDOWS

✅ Fundamentos de Windows

✅ NTFS

✅ Usuarios, grupos y autenticación

📘 ADICIONAL

├── Active Directory

├── Kerberos

├── TGT / TGS

├── SPN

├── NTLM

├── Pass-the-Hash

├── Pass-the-Ticket

└── Kerberoasting / Golden Ticket

⏳ Procesos y servicios

⏳ CMD + PowerShell

⏳ Windows Event Logs

⏳ Seguridad de Windows

⏳ Windows desde perspectiva atacante

⏳ Investigación SOC

**🏢 Semana 4 — Windows**

**📝 EXAMEN ADICIONAL --- Kerberos + Active Directory**

**Nivel:** SOC Nivel 1 → Intermedio\
**Modalidad:** 10 preguntas Multiple Choice\
**Enfoque:** comprensión + situaciones reales de SOC

Como venimos haciendo, **primero las 10 preguntas** y recién después las
**respuestas con justificación**.

**🔹 Pregunta 1**

¿Cuál es la función principal de **Active Directory**?

**A)** Analizar malware automáticamente.

**B)** Administrar de forma centralizada identidades, equipos, grupos,
políticas y recursos.

**C)** Reemplazar al firewall de la organización.

**D)** Cifrar todos los archivos de los usuarios.

**🔹 Pregunta 2**

¿Qué función cumple principalmente un **Domain Controller (DC)**?

**A)** Proporcionar funciones centrales del dominio, incluyendo
autenticación y servicios de Active Directory.

**B)** Asignar direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> mediante <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> exclusivamente.

**C)** Actuar únicamente como servidor web.

**D)** Almacenar exclusivamente archivos personales de los usuarios.

**🔹 Pregunta 3**

¿Cuál de las siguientes secuencias representa mejor el funcionamiento
simplificado de Kerberos?

**A)** Usuario → <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> → Firewall → Servidor.

**B)** Usuario → AS → TGT → TGS → Service Ticket → Servicio.

**C)** Usuario → DHCP → TGT → DNS → Servicio.

**D)** Usuario → NTFS → TGS → Firewall → Servicio.

**🔹 Pregunta 4**

¿Qué es un **TGT**?

**A)** Un grupo de usuarios privilegiados.

**B)** Un ticket que permite solicitar posteriormente tickets para
servicios.

**C)** Una contraseña almacenada en Active Directory.

**D)** Una política de seguridad de Windows.

**🔹 Pregunta 5**

¿Cuál es la función del **TGS** en Kerberos?

**A)** Crear cuentas de usuario.

**B)** Administrar las GPO.

**C)** Proporcionar tickets para acceder a servicios específicos
utilizando la información de autenticación correspondiente.

**D)** Asignar direcciones IP a los equipos.

**🔹 Pregunta 6**

¿Qué es un **SPN (Service Principal Name)**?

**A)** Un identificador asociado a una instancia de servicio utilizada
en el contexto de Kerberos.

**B)** El nombre de una computadora asignado por DHCP.

**C)** Una contraseña administrativa.

**D)** Un registro de Windows Event Log.

**🔹 Pregunta 7 --- Caso SOC**

El SIEM detecta:

Usuario: juan

Equipo: PC-VENTAS-01

03:15 → Login exitoso

03:17 → Acceso Kerberos a SERVER-RRHH

03:18 → Acceso Kerberos a SERVER-BACKUP

03:20 → Acceso Kerberos a DC01

Juan normalmente trabaja en Ventas y nunca accede a esos sistemas.

¿Cuál es la mejor reacción inicial del SOC?

**A)** Ignorar los eventos porque todos utilizan Kerberos.

**B)** Considerar automáticamente que Kerberos fue vulnerado.

**C)** Investigar la secuencia, el contexto del usuario, los equipos y
los accesos realizados.

**D)** Bloquear todos los Domain Controllers de la organización.

**🔹 Pregunta 8 --- Ataques**

¿Cuál de las siguientes asociaciones es correcta?

**A)** Pass-the-Hash → utiliza tickets Kerberos.

**B)** Pass-the-Ticket → utiliza material relacionado con tickets
Kerberos.

**C)** Kerberoasting → ataque contra DHCP.

**D)** Golden Ticket → ataque contra NTFS.

**🔹 Pregunta 9 --- Caso SOC ⭐**

El SOC descubre que una cuenta que normalmente pertenece a:

Usuarios

fue agregada inesperadamente a:

Domain Admins

¿Qué representa esto principalmente?

**A)** Un evento irrelevante porque el usuario ya estaba autenticado.

**B)** Una posible escalada de privilegios que requiere investigación.

**C)** Una actualización normal de DNS.

**D)** Una modificación de NTFS.

**🔹 Pregunta 10 --- Caso SOC ⭐⭐**

Durante una investigación se observa:

01:10 → Usuario recibe correo sospechoso

01:15 → Credenciales comprometidas

01:20 → Login desde PC desconocida

01:22 → Acceso a servidor

01:25 → Solicitudes Kerberos anómalas

01:30 → Movimiento hacia otros equipos

01:35 → Cuenta agregada a grupo privilegiado

¿Cuál es la interpretación más adecuada?

**A)** Es imposible que exista un ataque porque se utilizó Kerberos.

**B)** La secuencia presenta múltiples indicadores compatibles con un
posible compromiso de identidad y movimiento lateral.

**C)** El único problema es el correo recibido; el resto no tiene
relación.

**D)** Como el usuario tenía permisos legítimos, toda la actividad es
legítima.

**⛔ DETENTE AQUÍ**

Anotá tus respuestas antes de bajar:

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

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**Pregunta 1**

**✅ B --- Administrar de forma centralizada identidades, equipos,
grupos, políticas y recursos.**

Active Directory funciona como una infraestructura central de identidad
y administración.

Podemos visualizarlo:

ACTIVE DIRECTORY

│

┌──────────────┼──────────────┐

↓ ↓ ↓

Usuarios Grupos Equipos

│ │ │

└──────────────┼──────────────┘

↓

Políticas

↓

Recursos

Para un SOC es especialmente importante porque una gran parte de la
actividad relacionada con **identidades y privilegios** pasa por esta
infraestructura.

**Pregunta 2**

**✅ A --- Proporcionar funciones centrales del dominio, incluyendo
autenticación y servicios de Active Directory.**

El Domain Controller es uno de los activos más sensibles del entorno.

Simplificando:

Usuario

↓

Domain Controller

↓

Autenticación

↓

Acceso

Si un atacante consigue comprometer un DC, puede tener consecuencias
graves para todo el dominio.

Por eso:

**Actividad sospechosa contra un Domain Controller = alta prioridad de
investigación.**

**Pregunta 3**

**✅ B --- Usuario → AS → TGT → TGS → Service Ticket → Servicio.**

Este es el flujo simplificado que quiero que recuerdes:

Usuario

↓

AS

↓

TGT

↓

TGS

↓

Service Ticket

↓

Servicio

No necesitás memorizar todos los mensajes y detalles criptográficos
todavía.

Lo fundamental es comprender **qué papel cumple cada componente**.

**Pregunta 4**

**✅ B --- Un ticket que permite solicitar posteriormente tickets para
servicios.**

TGT significa:

**Ticket Granting Ticket**

Podemos imaginarlo como un ticket que permite al usuario interactuar
posteriormente con el TGS para obtener tickets destinados a servicios
específicos.

Usuario

↓

TGT

↓

TGS

↓

Ticket para servicio

**Pregunta 5**

**✅ C --- Proporcionar tickets para acceder a servicios específicos.**

El TGS significa:

**Ticket Granting Service**

Supongamos:

Juan

↓

Tiene TGT

↓

Quiere acceder a FILESERVER

↓

TGS

↓

Service Ticket

↓

FILESERVER

El concepto clave es:

**TGT → solicitar → Service Ticket → servicio**

**Pregunta 6**

**✅ A --- Un identificador asociado a una instancia de servicio
utilizada en el contexto de Kerberos.**

Un SPN permite identificar un servicio para que Kerberos pueda trabajar
con él.

Por ejemplo, conceptualmente:

SERVICIO/servidor

Los SPN son particularmente importantes para seguridad porque aparecen
en técnicas como **Kerberoasting**.

**Pregunta 7**

**✅ C --- Investigar la secuencia, el contexto del usuario, los equipos
y los accesos realizados.**

Esta pregunta busca evaluar algo fundamental:

**No debemos considerar malicioso un evento únicamente por utilizar
Kerberos.**

Kerberos es un mecanismo legítimo.

Lo sospechoso es el **contexto**:

Usuario de Ventas

↓

RRHH

↓

Backup

↓

Domain Controller

El analista debería investigar:

-   ¿Es normal que Juan acceda a esos servidores?

-   ¿Desde qué IP?

-   ¿A qué hora?

-   ¿Hubo otros eventos?

-   ¿Qué procesos ejecutó?

-   ¿Se produjeron cambios de privilegios?

-   ¿Hubo otros equipos involucrados?

**Pregunta 8**

**✅ B --- Pass-the-Ticket → utiliza material relacionado con tickets
Kerberos.**

Recordá esta diferencia:

PASS-THE-HASH

↓

Hash/material de autenticación

Mientras:

PASS-THE-TICKET

↓

Ticket Kerberos

Y:

KERBEROASTING

↓

Cuentas de servicio / tickets Kerberos

Finalmente:

GOLDEN TICKET

↓

Falsificación de determinados TGT

↓

Compromiso de secretos críticos de Kerberos

**Pregunta 9**

**✅ B --- Posible escalada de privilegios.**

Tenemos:

Usuario normal

↓

Domain Admins

Esto representa un cambio de privilegios extremadamente importante.

Un SOC debería investigar:

¿Quién hizo el cambio?

↓

¿Por qué?

↓

¿Quién autorizó?

↓

¿Desde qué equipo?

↓

¿Qué ocurrió después?

Una cuenta agregada inesperadamente a un grupo privilegiado puede ser
una señal de compromiso.

**Pregunta 10**

**✅ B --- Posible compromiso de identidad y movimiento lateral.**

La secuencia completa es mucho más importante que un evento aislado:

Correo sospechoso

↓

Credenciales comprometidas

↓

Login desde equipo desconocido

↓

Acceso a servidor

↓

Actividad Kerberos anómala

↓

Movimiento lateral

↓

Escalada de privilegios

Este es precisamente el tipo de **cadena de ataque** que un SOC debe
intentar detectar y reconstruir.

**🏆 RESULTADO**

  -------------------------------------------------------------------------
  **Correctas**   **Nivel**
  --------------- ---------------------------------------------------------
  **10/10**       🟢 Excelente --- dominio muy sólido

  **8--9/10**     🟢 Muy buen nivel

  **6--7/10**     🟡 Buen progreso; reforzar conceptos

  **4--5/10**     🟠 Conviene repasar Kerberos + AD

  **0--3/10**     🔴 Recomiendo volver a estudiar el módulo
  -------------------------------------------------------------------------

**🧠 DESAFÍO FINAL --- Nivel SOC**

Este **no cuenta para la nota**.

El SIEM muestra:

Equipo: PC-VENTAS-04

Usuario: juan

22:10 → Login exitoso

22:12 → Solicitud de ticket Kerberos

22:13 → Acceso a FILESERVER

22:15 → Acceso a SERVER-RRHH

22:17 → PowerShell

22:18 → Nuevo usuario creado

22:19 → Nuevo usuario agregado a Administrators

22:20 → Acceso a DC01

Como futuro analista, intentá separar la situación en:

1\. Autenticación

2\. Acceso

3\. Ejecución

4\. Persistencia

5\. Escalada de privilegios

6\. Movimiento lateral

7\. Activo crítico

Ese ejercicio ya se parece bastante más a una **investigación real de
SOC** que a una pregunta de examen.

**📊 Semana 4 --- Progreso actualizado**

✅ Fundamentos de Windows

✅ NTFS

✅ Usuarios, grupos y autenticación

📘 MÓDULO ADICIONAL

✅ Active Directory

✅ Kerberos

✅ TGT / TGS

✅ SPN

✅ NTLM

✅ Pass-the-Hash

✅ Pass-the-Ticket

✅ Kerberoasting

✅ Golden Ticket

⏳ Procesos y servicios

⏳ CMD + PowerShell

⏳ Windows Event Logs

⏳ Seguridad de Windows

⏳ Windows desde perspectiva atacante

⏳ Investigación SOC

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
