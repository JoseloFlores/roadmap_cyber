**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 21: Fundamentos de Windows**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Administración + Seguridad + Detección SOC

Perfecto. A partir de ahora cerramos formalmente **Redes** y comenzamos
**Sistemas**, empezando por Windows.

La idea en esta etapa cambia ligeramente: ya no vamos a estudiar
solamente \"qué hace Windows\", sino **qué ocurre dentro de un equipo
Windows y cómo puede observarlo un Analista SOC**.

**🎯 Objetivos de este módulo**

Al terminar esta clase deberías poder explicar:

-   Qué es un sistema operativo.

-   Qué es Windows.

-   Qué es el <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a>.

-   Qué diferencia existe entre **User Mode** y **Kernel Mode**.

-   Qué son los procesos.

-   Qué son los servicios.

-   Qué son los usuarios y grupos.

-   Qué es el sistema de archivos.

-   Qué es el Registro de Windows.

-   Qué relación tienen todos estos elementos con un SOC.

**1. ¿Qué es un sistema operativo?**

Antes de hablar de Windows tenemos que entender qué es un **Sistema
Operativo (OS)**.

Un sistema operativo es el software que administra los recursos de una
computadora y permite que las aplicaciones interactúen con el hardware.

Podemos imaginarlo así:

USUARIO

↓

APLICACIONES

↓

SISTEMA OPERATIVO

↓

┌─────────┴─────────┐

↓ ↓

HARDWARE RECURSOS

↓

CPU / RAM / DISCO / RED

Sin un sistema operativo, utilizar una computadora moderna sería
extremadamente complicado.

**2. ¿Qué administra un sistema operativo?**

Principalmente:

**🧠 CPU**

Decide qué procesos utilizan el procesador.

**💾 Memoria RAM**

Administra qué programas pueden utilizar memoria y cuánto.

**💽 Almacenamiento**

Administra archivos, carpetas y permisos.

**🌐 Red**

Permite que los programas se comuniquen mediante la red.

**👤 Usuarios**

Controla quién puede acceder a determinados recursos.

**⚙️ Procesos**

Administra los programas que están ejecutándose.

**🔐 Seguridad**

Controla permisos, autenticación y diferentes mecanismos de protección.

**3. ¿Qué es Windows?**

**Windows** es una familia de sistemas operativos desarrollada por
Microsoft.

Algunos ejemplos:

Windows 10

Windows 11

Windows Server 2019

Windows Server 2022

Windows Server 2025

Para nosotros hay una distinción importante:

**Windows cliente**

Ejemplo:

Windows 11

Normalmente utilizado en computadoras de usuarios.

**Windows Server**

Ejemplo:

Windows Server

Utilizado para servidores y servicios empresariales.

En un SOC podemos encontrar ambos.

**4. ¿Por qué Windows es importante para un SOC?**

Porque es uno de los sistemas operativos más utilizados en entornos
corporativos.

Un SOC puede monitorear:

PC-VENTAS-01

PC-RRHH-02

PC-FINANZAS-03

SERVER-AD-01

SERVER-FILES-01

Todos ellos pueden generar enormes cantidades de eventos.

Por ejemplo:

Usuario inició sesión

Proceso ejecutado

Archivo creado

Servicio iniciado

Conexión de red

PowerShell ejecutado

Antivirus detectó malware

El trabajo del SOC consiste, entre otras cosas, en distinguir:

ACTIVIDAD NORMAL

↓

ACTIVIDAD SOSPECHOSA

↓

POSIBLE INCIDENTE

**5. Arquitectura básica de Windows**

Ahora llegamos a uno de los conceptos más importantes.

Windows separa la ejecución del sistema en diferentes niveles de
privilegios.

Los <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> principales son:

USER MODE

↓

KERNEL MODE

**6. User Mode**

En **User Mode** se ejecutan normalmente las aplicaciones.

Por ejemplo:

Chrome

Edge

Word

Outlook

PowerShell

Notepad

Estas aplicaciones tienen restricciones.

¿Por qué?

Porque si cualquier programa pudiera modificar directamente la memoria
del sistema o controlar el hardware, un simple error podría destruir el
sistema completo.

**7. Kernel Mode**

El **Kernel Mode** tiene privilegios mucho mayores.

Aquí funciona el núcleo del sistema operativo y componentes que
necesitan acceso privilegiado.

El kernel administra cosas como:

-   CPU.

-   Memoria.

-   Dispositivos.

-   Controladores.

-   Procesos.

-   Recursos del sistema.

Podemos representarlo:

┌─────────────────────────────┐

│ USER MODE │

│ │

│ Chrome Word PowerShell │

│ Outlook Apps │

└──────────────┬──────────────┘

│

API / System Calls

│

┌──────────────▼──────────────┐

│ KERNEL MODE │

│ │

│ Kernel │

│ Drivers │

│ Gestión de memoria │

│ Gestión de procesos │

│ Hardware │

└──────────────┬──────────────┘

│

▼

HARDWARE

**8. ¿Por qué esto importa para un SOC?**

Porque una aplicación ejecutándose en User Mode normalmente tiene menos
privilegios que un componente del Kernel.

Un atacante que consigue pasar de:

User Mode

a ejecutar código con privilegios elevados puede obtener un control
mucho mayor sobre el equipo.

Por eso una de las preguntas fundamentales durante una investigación es:

**¿Con qué privilegios se ejecutó este proceso?**

**9. ¿Qué es un proceso?**

Un **proceso** es una instancia de un programa que está ejecutándose.

Por ejemplo:

chrome.exe

Cuando abres Chrome, Windows crea uno o varios procesos.

Otros ejemplos:

notepad.exe

explorer.exe

powershell.exe

cmd.exe

svchost.exe

**10. Programa vs proceso**

Esta diferencia es importante.

**Programa**

Es el archivo almacenado en disco.

Ejemplo:

C:\\Windows\\System32\\notepad.exe

**Proceso**

Es ese programa **ejecutándose en memoria**.

notepad.exe

↓

PROCESO

↓

RAM

Una forma sencilla de recordarlo:

**Programa = archivo.**\
**Proceso = programa ejecutándose.**

**11. ¿Qué es un servicio?**

Un **servicio de Windows** es un programa diseñado para ejecutarse en
segundo plano y proporcionar una función al sistema o a otros programas.

Ejemplos:

-   Windows Update.

-   Windows Defender.

-   <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a> Client.

-   <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Client.

-   Print Spooler.

Muchos servicios pueden ejecutarse incluso aunque ningún usuario tenga
abierta una aplicación relacionada.

**12. Procesos vs servicios**

  ------------------------------------------------------------------------------
  **Característica**                          **Proceso**         **Servicio**
  ------------------------------------------- ------------------- --------------
  Es código ejecutándose                      ✅                  ✅

  Puede ejecutarse en segundo plano           ✅                  ✅

  Puede ser iniciado por un usuario           ✅                  A veces

  Puede iniciarse automáticamente             ✅                  ✅

  Está diseñado para una función permanente   No necesariamente   ✅
  ------------------------------------------------------------------------------

Un servicio puede generar uno o varios procesos.

Por ejemplo:

Servicio

↓

svchost.exe

↓

Proceso

**13. ¿Qué es un usuario?**

Windows utiliza cuentas de usuario para identificar quién está
utilizando el sistema.

Ejemplo:

Gonzalo

Administrador

Invitado

SYSTEM

Cada cuenta puede tener diferentes permisos.

**14. Usuarios y privilegios**

Podemos simplificarlo así:

Usuario estándar

↓

Menos privilegios

Administrador

↓

Más privilegios

Pero existe un usuario especialmente importante:

NT AUTHORITY\\SYSTEM

La cuenta **SYSTEM** posee privilegios extremadamente elevados dentro
del sistema Windows.

Para un SOC, esto es muy importante.

Si observamos:

malware.exe

ejecutándose como:

SYSTEM

merece una investigación inmediata.

**15. ¿Qué son los grupos?**

Los grupos permiten asignar permisos a múltiples usuarios.

Ejemplo:

Administrators

Users

Remote Desktop Users

Backup Operators

En lugar de configurar permisos individualmente:

Juan → permiso

Pedro → permiso

María → permiso

podemos utilizar:

Grupo Finanzas

↓

Permisos

↓

Juan

Pedro

María

**16. ¿Qué es el sistema de archivos?**

Windows necesita organizar la información almacenada en el disco.

La estructura típica es:

C:\\

│

├── Windows

├── Users

├── Program Files

├── Program Files (x86)

└── ProgramData

Estas carpetas son extremadamente importantes para un analista.

**17. C:\\Windows**

Aquí se encuentran muchos componentes fundamentales del sistema.

Ejemplo:

C:\\Windows\\System32

Contiene herramientas y componentes esenciales.

Algunos ejecutables conocidos:

cmd.exe

powershell.exe

taskmgr.exe

**18. C:\\Users**

Contiene los perfiles de los usuarios.

Ejemplo:

C:\\Users\\Gonzalo

Dentro pueden existir:

Desktop

Documents

Downloads

Pictures

AppData

**19. C:\\Program Files**

Normalmente contiene aplicaciones instaladas.

Ejemplo:

C:\\Program Files\\Google\\

C:\\Program Files\\Microsoft\\

Un analista SOC puede investigar desde qué ubicación se ejecutó un
programa.

Por ejemplo:

C:\\Program Files\\Aplicacion\\app.exe

podría ser normal.

Mientras que:

C:\\Users\\Gonzalo\\Downloads\\factura.exe

puede requerir mayor investigación.

**La ubicación por sí sola no demuestra que sea malware**, pero es un
indicador contextual importante.

**20. AppData**

Dentro del perfil de usuario existe:

C:\\Users\\\<usuario\>\\AppData

Es una ubicación muy importante en seguridad.

Allí muchas aplicaciones almacenan:

-   Configuraciones.

-   Cachés.

-   Datos temporales.

-   Información de aplicaciones.

También puede ser abusada por malware.

Por ejemplo:

C:\\Users\\Gonzalo\\AppData\\Roaming\\

puede aparecer en investigaciones relacionadas con persistencia o
ejecución de malware.

**21. ¿Qué es el Registro de Windows?**

El **Windows Registry** es una base de datos jerárquica que almacena
configuraciones importantes del sistema y de aplicaciones.

Podemos imaginarlo como:

REGISTRO

│

├── Configuración del sistema

├── Usuarios

├── Aplicaciones

├── Servicios

└── Configuraciones

La herramienta gráfica para explorarlo es:

regedit.exe

**22. ¿Por qué el Registry importa en seguridad?**

Porque algunos mecanismos de persistencia pueden utilizar determinadas
claves del Registro.

Por ejemplo, un atacante podría intentar configurar un programa para que
se ejecute automáticamente cuando un usuario inicia sesión.

Esto convierte al Registro en una fuente importante de evidencia durante
una investigación.

**23. ¿Qué es el <a href="../../GLOSARIO.md#uac" target="_blank">UAC</a>?**

UAC significa:

**User Account Control**

Es el mecanismo que solicita confirmación cuando una acción requiere
privilegios elevados.

Por ejemplo:

Aplicación quiere realizar cambios

↓

UAC

↓

¿Permitir?

Su objetivo es evitar que cualquier aplicación obtenga privilegios
administrativos silenciosamente.

**24. Windows y la seguridad**

Windows incluye diferentes mecanismos defensivos:

Windows Defender

\+

Windows Firewall

\+

UAC

\+

Windows Update

\+

Event Logs

\+

Microsoft Security

Pero ningún mecanismo es perfecto.

Por eso las organizaciones utilizan otras capas:

Windows

↓

<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a>

↓

Firewall

↓

<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>

↓

SOC

**25. ¿Qué información puede utilizar un SOC?**

Aquí comienza la conexión con todo lo que estudiamos anteriormente.

Imagina:

PC-FINANZAS-03

El SOC puede recibir:

**Evento de autenticación**

Usuario: Gonzalo

Resultado: Fallido

**Evento de proceso**

powershell.exe

**Evento de red**

192.168.1.25

↓

203.0.113.50:443

**Evento DNS**

consulta:

dominio-sospechoso.xyz

Ahora podemos unir todo:

LOGIN

↓

POWERSHELL

↓

DNS

↓

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

Esto es **correlación de eventos**.

Y es precisamente una de las habilidades que vamos a desarrollar durante
esta etapa.

**🕵️ 26. ¿Cómo podría aprovechar Windows un atacante?**

Supongamos que un atacante consigue ejecutar un archivo:

factura.exe

Podría intentar:

1\. Ejecutar malware

↓

2\. Obtener información del equipo

↓

3\. Buscar usuarios

↓

4\. Buscar privilegios

↓

5\. Crear persistencia

↓

6\. Comunicarse con C2

↓

7\. Intentar escalar privilegios

Cada etapa puede dejar evidencia.

**🔍 27. Ejemplo de investigación SOC**

Supongamos que aparece:

factura.exe

El SOC podría preguntar:

**¿Dónde estaba?**

Downloads

**¿Quién lo ejecutó?**

Gonzalo

**¿Cuándo?**

10:32

**¿Qué proceso creó?**

powershell.exe

**¿Qué hizo PowerShell?**

Comandos sospechosos

**¿A qué dominio se conectó?**

update-security.xyz

**¿Qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> resolvió?**

203.0.113.50

**¿Qué protocolo utilizó?**

HTTPS / <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443

De esta forma podemos reconstruir una historia.

**🧠 28. Lo más importante del módulo**

Quiero que te quedes con este modelo mental:

WINDOWS

│

┌───────────────┼────────────────┐

↓ ↓ ↓

USUARIOS PROCESOS SERVICIOS

│ │ │

└───────────────┼────────────────┘

↓

SISTEMA OPERATIVO

│

┌────────┴────────┐

↓ ↓

ARCHIVOS REGISTRO

│ │

└────────┬────────┘

↓

EVENTOS

↓

SOC

El SOC observa **qué hacen los usuarios, procesos, servicios y
componentes del sistema** para determinar si existe actividad maliciosa.

**🎯 Resumen del Módulo 21**

**Sistema operativo**

Administra:

-   CPU.

-   RAM.

-   Disco.

-   Red.

-   Usuarios.

-   Procesos.

-   Seguridad.

**Windows**

Es un sistema operativo ampliamente utilizado en organizaciones.

**Kernel**

Es el núcleo del sistema operativo.

**User Mode**

Ejecutan normalmente las aplicaciones.

**Kernel Mode**

Tiene acceso privilegiado al sistema y hardware.

**Proceso**

Programa actualmente ejecutándose.

**Servicio**

Programa que funciona normalmente en segundo plano para proporcionar una
función.

**Usuario**

Identidad que utiliza el sistema.

**Grupo**

Conjunto de usuarios al que pueden asignarse permisos.

**Registro**

Base de datos de configuración de Windows.

**UAC**

Controla determinadas acciones que requieren elevación de privilegios.

**🧠 Conceptos que quiero que memorices**

  -----------------------------------------------------------------------
  **Concepto**   **Definición**
  -------------- --------------------------------------------------------
  **OS**         Sistema operativo

  **Kernel**     Núcleo del sistema

  **User Mode**  Entorno con privilegios limitados

  **Kernel       Entorno con privilegios elevados
  Mode**         

  **Proceso**    Programa en ejecución

  **Servicio**   Programa diseñado para funcionar en segundo plano

  **SYSTEM**     Cuenta con privilegios muy elevados

  **Registry**   Base de datos de configuración de Windows

  **UAC**        Control de cuentas de usuario

  **NTFS**       Sistema de archivos habitual de Windows
  -----------------------------------------------------------------------

**🛡️ Conexión con tu futura profesión**

Hay una diferencia importante entre aprender Windows como usuario y
aprenderlo como **Analista SOC**.

Un usuario pregunta:

\"¿Cómo hago para abrir el Administrador de tareas?\"

Un Analista SOC pregunta:

**\"¿Por qué este proceso apareció, quién lo inició, con qué
privilegios, desde qué ruta, qué proceso padre lo creó y con qué IP se
comunicó después?\"**

Ese cambio de mentalidad es justamente lo que vamos a trabajar durante
toda esta etapa.

**🧪 Laboratorio recomendado**

Para este primer módulo, no hace falta instalar herramientas
adicionales.

En tu Windows podés empezar a explorar:

**Administrador de tareas**

Ctrl + Shift + Esc

Observá:

-   Procesos.

-   CPU.

-   Memoria.

-   Disco.

-   Red.

-   Usuarios.

**Información del sistema**

Abrí:

Win + R

y ejecutá:

msinfo32

**Registro**

Win + R

y:

regedit

⚠️ **Por ahora solo explorá. No modifiques ni elimines claves del
Registro.**

**Servicios**

Win + R

y:

services.msc

No cambies configuraciones todavía. El objetivo es simplemente reconocer
qué estamos observando.

**📝 Próximo paso: evaluación**

Como venimos haciendo desde Redes, después de este módulo corresponde
nuestro:

**Examen --- 10 preguntas Multiple Choice**

Pero esta vez voy a empezar a introducir **situaciones de SOC**.

No solamente:

\"¿Qué es un proceso?\"

También:

\"El SOC detecta que powershell.exe fue iniciado desde una carpeta de
usuario. ¿Qué información debería investigar el analista?\"

Así empezamos progresivamente a pasar de **memorizar conceptos → razonar
como Analista SOC**.

**📍 Progreso**

**Semana 4 — Windows**

-   🔵 Módulo 21: Fundamentos de Windows ← **COMPLETADO**

-   ⚪ Módulo 22: Sistema de archivos NTFS

-   ⚪ Módulo 23: Usuarios, grupos y autenticación

-   ⚪ Módulo 24: Procesos y servicios

-   ⚪ Módulo 25: CMD y PowerShell

-   ⚪ Módulo 26: Windows Event Logs

-   ⚪ Módulo 27: Seguridad de Windows

-   ⚪ Módulo 28: Windows desde la perspectiva del atacante

-   ⚪ Módulo 29: Investigación SOC en Windows

**🖥️ Carrera de Analista SOC**

**Semana 4 — Windows**

**📝 Evaluación --- Módulo 21: Fundamentos de Windows**

**Nivel:** Principiante → Analista SOC Nivel 1

Vamos a mantener el formato que venimos utilizando. Esta vez agrego
algunas preguntas de **razonamiento SOC**, para empezar a entrenarte
como analista y no solamente como estudiante.

**Instrucciones:** elegí una sola respuesta por pregunta.\
**No mires las soluciones hasta terminar.**

**🔹 Pregunta 1**

¿Cuál es la función principal de un sistema operativo?

**A)** Proporcionar únicamente una interfaz gráfica.

**B)** Administrar los recursos de hardware y software de la
computadora.

**C)** Servir exclusivamente para conectarse a Internet.

**D)** Ejecutar solamente aplicaciones de seguridad.

**🔹 Pregunta 2**

¿Qué componente de Windows funciona como núcleo del sistema operativo y
administra recursos como memoria, procesos y hardware?

**A)** Registry.

**B)** Explorer.exe.

**C)** Kernel.

**D)** Task Manager.

**🔹 Pregunta 3**

¿Cuál es una característica de **User Mode**?

**A)** Las aplicaciones tienen acceso directo e ilimitado al hardware.

**B)** Las aplicaciones funcionan con privilegios limitados para
proteger el sistema.

**C)** Solo pueden ejecutarse servicios de Windows.

**D)** Es el modo utilizado exclusivamente por administradores.

**🔹 Pregunta 4**

¿Cuál es la diferencia correcta entre un **programa** y un **proceso**?

**A)** Un programa está en RAM y un proceso está únicamente en disco.

**B)** Un programa es un archivo/código almacenado; un proceso es una
instancia de ese programa ejecutándose.

**C)** Un proceso siempre es un servicio.

**D)** No existe ninguna diferencia.

**🔹 Pregunta 5**

¿Qué es un servicio de Windows?

**A)** Una cuenta especial utilizada por administradores.

**B)** Un programa diseñado normalmente para ejecutarse en segundo plano
y proporcionar una función al sistema o a otros programas.

**C)** Un archivo almacenado dentro de C:\\Users.

**D)** Una conexión de red.

**🔹 Pregunta 6**

Un Analista SOC observa:

Proceso:

malware.exe

Usuario:

SYSTEM

¿Por qué debería considerarse un evento de alta importancia?

**A)** Porque SYSTEM es una cuenta utilizada exclusivamente para navegar
por Internet.

**B)** Porque SYSTEM tiene privilegios muy elevados dentro de Windows.

**C)** Porque todos los procesos ejecutados como SYSTEM son
automáticamente malware.

**D)** Porque SYSTEM significa que el equipo está apagado.

**🔹 Pregunta 7**

¿Cuál de las siguientes rutas corresponde normalmente al perfil de un
usuario de Windows?

**A)** C:\\Users\\NombreUsuario

**B)** C:\\Kernel\\Users

**C)** C:\\System\\Accounts

**D)** C:\\Windows\\ProfilesOnly

**🔹 Pregunta 8**

¿Qué es el **Windows Registry**?

**A)** Un servidor DNS local.

**B)** Una base de datos jerárquica que almacena configuraciones del
sistema y aplicaciones.

**C)** Un antivirus incluido en Windows.

**D)** Un sistema de archivos utilizado exclusivamente para discos
externos.

**🔹 Pregunta 9 --- Caso SOC**

El SIEM genera la siguiente alerta:

Equipo: PC-FINANZAS-03

Usuario: Gonzalo

Proceso:

powershell.exe

Ubicación del proceso:

C:\\Users\\Gonzalo\\Downloads\\

Proceso padre:

factura.exe

Conexión posterior:

TCP 443

¿Cuál sería la mejor reacción inicial del Analista SOC?

**A)** Ignorar la alerta porque PowerShell es una herramienta legítima
de Windows.

**B)** Bloquear inmediatamente toda la red corporativa.

**C)** Investigar la cadena de procesos, el archivo factura.exe, el
destino de la conexión y la actividad realizada por PowerShell.

**D)** Concluir inmediatamente que se trata de ransomware.

**🔹 Pregunta 10 --- Caso SOC ⭐**

Durante una investigación se observa la siguiente secuencia:

Usuario

↓

factura.exe

↓

powershell.exe

↓

modificación del Registry

↓

conexión HTTPS

¿Qué concepto describe mejor lo que está haciendo el analista al
estudiar esta secuencia completa?

**A)** Resolución DNS.

**B)** Correlación y análisis de eventos para reconstruir la actividad.

**C)** Fragmentación IP.

**D)** Administración de memoria.

**⛔ DETENTE AQUÍ**

Antes de mirar las respuestas, intenta resolver las 10.

Podés anotar simplemente:

1-B

2-C

3-\...

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**Pregunta 1**

**✅ Respuesta: B**

Un sistema operativo administra los recursos de la computadora:

-   CPU.

-   RAM.

-   Disco.

-   Red.

-   Procesos.

-   Usuarios.

-   Permisos.

Es la capa que permite que las aplicaciones utilicen el hardware de
forma controlada.

**Pregunta 2**

**✅ Respuesta: C --- Kernel**

El **kernel** es el núcleo del sistema operativo.

Se encarga de tareas fundamentales como:

-   Administración de memoria.

-   Procesos.

-   Hardware.

-   Controladores.

-   Recursos del sistema.

Por eso comprometer componentes con privilegios de kernel puede tener
consecuencias extremadamente graves.

**Pregunta 3**

**✅ Respuesta: B**

En **User Mode**, las aplicaciones tienen restricciones.

Por ejemplo:

Chrome

Word

PowerShell

Notepad

No deberían poder modificar libremente recursos críticos del sistema.

Esta separación ayuda a evitar que un fallo en una aplicación comprometa
automáticamente todo el sistema.

**Pregunta 4**

**✅ Respuesta: B**

La diferencia fundamental es:

PROGRAMA

↓

Archivo/código almacenado

mientras que:

PROCESO

↓

Programa ejecutándose

↓

Memoria RAM

Por ejemplo:

C:\\Windows\\System32\\notepad.exe

es un archivo.

Cuando lo ejecutamos:

notepad.exe

aparece como proceso.

**Pregunta 5**

**✅ Respuesta: B**

Un servicio está diseñado normalmente para ejecutarse en segundo plano.

Ejemplos:

-   Windows Update.

-   Windows Defender.

-   DHCP Client.

-   DNS Client.

Desde un SOC, los servicios son importantes porque un atacante puede
intentar **crear o modificar servicios para conseguir persistencia**.

**Pregunta 6**

**✅ Respuesta: B**

SYSTEM es una identidad con privilegios muy elevados dentro de Windows.

Por eso:

malware.exe

↓

SYSTEM

es especialmente preocupante.

⚠️ Importante:

Que un proceso se ejecute como SYSTEM **no significa automáticamente que
sea malware**.

Windows tiene muchos procesos legítimos que utilizan esa cuenta.

El analista debe investigar **qué proceso es, dónde está ubicado, quién
lo inició, qué proceso padre tiene y qué actividad realizó**.

**Pregunta 7**

**✅ Respuesta: A**

Los perfiles de usuario normalmente se encuentran en:

C:\\Users\\

Por ejemplo:

C:\\Users\\Gonzalo\\

Dentro pueden encontrarse:

Desktop

Documents

Downloads

Pictures

AppData

Estas ubicaciones son importantes durante investigaciones forenses y de
malware.

**Pregunta 8**

**✅ Respuesta: B**

El **Windows Registry** es una base de datos jerárquica utilizada para
almacenar configuraciones.

Puede contener información relacionada con:

-   Sistema.

-   Usuarios.

-   Aplicaciones.

-   Servicios.

-   Configuraciones.

También puede ser utilizado por atacantes para mecanismos de
**persistencia** u otras modificaciones del sistema.

**Pregunta 9**

**✅ Respuesta: C**

Esta es una pregunta importante para tu futura profesión.

No debemos pensar:

\"PowerShell = malware.\"

PowerShell es una herramienta legítima y muy utilizada por
administradores.

Lo sospechoso es el **contexto**:

factura.exe

↓

PowerShell

↓

HTTPS

Además:

C:\\Users\\Gonzalo\\Downloads\\

es una ubicación que merece investigación.

El analista debería buscar:

-   Hash de factura.exe.

-   Proceso padre.

-   Línea de comandos.

-   Usuario.

-   Destino de red.

-   Consultas DNS relacionadas.

-   Eventos de PowerShell.

-   Eventos del EDR.

-   Actividad posterior.

Esto es pensamiento SOC.

**Pregunta 10**

**✅ Respuesta: B**

El analista está realizando **correlación de eventos**.

No está observando un evento aislado:

factura.exe

Está construyendo una secuencia:

Usuario

↓

Ejecución

↓

PowerShell

↓

Modificación

↓

Comunicación

Esto permite reconstruir potencialmente la cadena de ataque.

**🏆 TABLA DE RESULTADOS**

  ------------------------------------------------------------------------------
  **Resultado**   **Evaluación**
  --------------- --------------------------------------------------------------
  **10/10**       🟢 Excelente --- comprensión muy sólida y buen razonamiento
                  SOC.

  **8--9/10**     🟢 Muy buen nivel --- estás listo para avanzar.

  **6--7/10**     🟡 Buen progreso --- conviene reforzar algunos conceptos antes
                  de avanzar.

  **4--5/10**     🟠 Necesitamos repasar fundamentos.

  **0--3/10**     🔴 Conviene volver a estudiar el módulo antes de continuar.
  ------------------------------------------------------------------------------

**🎯 DESAFÍO EXTRA --- NIVEL ENTREVISTA SOC**

Este no cuenta para la nota, pero quiero que empieces a desarrollar el
razonamiento que vas a necesitar en una entrevista.

Recibes esta alerta:

Equipo: PC-RRHH-07

Usuario: empleado01

09:42

└── Outlook.exe

└── factura.exe

└── powershell.exe

└── conexión TCP 443

El EDR además informa:

factura.exe

ubicación:

C:\\Users\\empleado01\\AppData\\Roaming\\

**Como Analista SOC, ¿qué te llama la atención?**

Hay **varias cosas**:

**1. Cadena de procesos**

Outlook

↓

factura.exe

↓

PowerShell

Un correo electrónico podría haber provocado la ejecución de un archivo.

**2. Ubicación**

AppData\\Roaming

No significa automáticamente malware, pero es una ubicación que puede
aparecer en investigaciones de persistencia o ejecución maliciosa.

**3. PowerShell**

PowerShell es legítimo, pero debemos investigar:

¿Quién lo ejecutó?

¿Qué comando ejecutó?

¿Con qué argumentos?

¿Qué proceso lo inició?

**4. Comunicación posterior**

PowerShell

↓

TCP 443

Debemos investigar:

¿A qué IP?

¿A qué dominio?

¿Hubo una consulta DNS?

¿Es un dominio conocido?

¿Se enviaron datos?

**5. Correlación**

Finalmente podemos construir:

EMAIL

↓

ARCHIVO

↓

EJECUCIÓN

↓

POWERSHELL

↓

RED

↓

POSIBLE C2

**Eso ya empieza a parecer una investigación SOC real.**

**📊 Progreso --- Semana 4**

**Sistemas Windows**

-   ✅ Módulo 21 --- Fundamentos de Windows

-   ⚪ Módulo 22 --- Sistema de archivos NTFS

-   ⚪ Módulo 3 --- Usuarios, grupos y autenticación

-   ⚪ Módulo 4 --- Procesos y servicios

-   ⚪ Módulo 5 --- CMD y PowerShell

-   ⚪ Módulo 6 --- Windows Event Logs

-   ⚪ Módulo 7 --- Seguridad de Windows

-   ⚪ Módulo 8 --- Windows desde la perspectiva del atacante

-   ⚪ Módulo 9 --- Investigación SOC en Windows

**Siguiente módulo recomendado:** **Sistema de archivos NTFS**, donde
vamos a profundizar en C:\\Windows, C:\\Users, Program Files, AppData,
permisos, ACL, archivos ocultos y qué evidencias puede buscar un
analista SOC en el sistema de archivos.
