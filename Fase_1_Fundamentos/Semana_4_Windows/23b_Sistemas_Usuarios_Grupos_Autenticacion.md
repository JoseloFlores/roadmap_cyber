**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 3 --- Sistemas Windows**

**Módulo 3: Usuarios, Grupos y Autenticación**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Windows + Seguridad + Detección SOC

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

Todavía no vamos a profundizar en Event Viewer ---eso será nuestro
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

PowerShell ejecutado

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

**📍 Progreso --- Semana 3**

  -------------------------------------------------------------------------
  **Módulo**                                                   **Estado**
  ------------------------------------------------------------ ------------
  1\. Fundamentos de Windows                                   ✅

  2\. NTFS y sistema de archivos                               ✅

  **3. Usuarios, grupos y autenticación**                      **✅**

  4\. Procesos y servicios                                     ⏳

  5\. CMD y PowerShell                                         ⏳

  6\. Windows Event Logs                                       ⏳

  7\. Seguridad de Windows                                     ⏳

  8\. Windows desde la perspectiva del atacante                ⏳

  9\. Investigación SOC en Windows                             ⏳
  -------------------------------------------------------------------------

**🖥️ Carrera de Analista SOC**

**Semana 3 --- Sistemas Windows**

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

**📊 Semana 3 --- Progreso**

  -------------------------------------------------------------------------
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
