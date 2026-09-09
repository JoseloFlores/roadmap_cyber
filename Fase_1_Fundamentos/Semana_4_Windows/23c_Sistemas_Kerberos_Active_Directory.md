**🏢 Semana 3 --- Sistemas Windows**

**🔐 Módulo Adicional: <a href="../../GLOSARIO.md#kerberos" target="_blank">Kerberos</a> + <a href="../../GLOSARIO.md#active-directory" target="_blank">Active Directory</a>**

**Enfoque:** Ciberseguridad / <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1\
**Objetivo:** comprender cómo funciona la autenticación en un entorno
Windows empresarial y aprender a reconocer comportamientos que podrían
indicar un ataque.

📌 **Importante:** este módulo es complementario. No reemplaza el
recorrido principal de Semana 3; lo vamos a utilizar como base cuando
lleguemos a **Windows Event Logs, <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>, detección y respuesta**.

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

Conceptualmente contiene <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> servicios:

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

**📚 Cómo encaja en nuestra Semana 3**

No vamos a alterar el plan principal:

SEMANA 3 --- WINDOWS

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

**🏢 Semana 3 --- Sistemas Windows**

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

**📊 Semana 3 --- Progreso actualizado**

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
