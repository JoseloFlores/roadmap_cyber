**🖥️ Semana 3 --- SISTEMAS**

**Windows para Analistas SOC**

Vamos a mantener exactamente la metodología que venimos utilizando:

**Teoría → profundización → seguridad → atacante → defensa → aplicación
SOC → ejercicios → cuestionario de 10 preguntas.**

Y esta etapa la vamos a hacer **desde cero pero con profundidad**, sin
asumir que ya sos administrador de Windows.

**📚 Roadmap --- Semana 3: Windows**

Te propongo este recorrido:

**1. Fundamentos de Windows ⭐**

-   ¿Qué es un sistema operativo?

-   Windows y su arquitectura.

-   Kernel.

-   User Mode / Kernel Mode.

-   Procesos y servicios.

-   Sistema de archivos.

-   Registro de Windows.

-   Usuarios y grupos.

**2. Sistema de archivos NTFS**

-   Discos y particiones.

-   NTFS.

-   Carpetas importantes.

-   Permisos.

-   ACL.

-   Herencia de permisos.

-   Archivos ocultos.

-   Archivos temporales.

**3. Usuarios, grupos y autenticación**

-   Usuarios locales.

-   Administradores.

-   Grupos.

-   UAC.

-   Contraseñas.

-   Windows Logon.

-   NTLM.

-   Kerberos.

-   Active Directory --- introducción.

**4. Procesos y servicios**

-   Task Manager.

-   tasklist.

-   taskkill.

-   Procesos padre/hijo.

-   Servicios Windows.

-   services.msc.

-   sc.

-   Procesos sospechosos.

**5. CMD y PowerShell**

Esta parte será **muy importante para SOC**.

Aprenderemos:

cmd.exe

powershell.exe

Y comandos como:

ipconfig

netstat

tasklist

whoami

systeminfo

nslookup

ping

tracert

net user

net localgroup

Y posteriormente PowerShell:

Get-Process

Get-Service

Get-EventLog

Get-WinEvent

Get-ChildItem

Get-NetTCPConnection

**🔥 6. Windows Event Logs**

Este será uno de los módulos más importantes de toda la Semana 3.

Aprenderás:

Event Viewer

y especialmente:

-   Security

-   System

-   Application

-   PowerShell

-   Windows Defender

Y eventos como:

4624 → inicio de sesión exitoso

4625 → inicio de sesión fallido

4688 → creación de proceso

4672 → privilegios especiales

4720 → creación de usuario

4728 → usuario agregado a grupo

7045 → instalación de servicio

Esto empieza a ser **trabajo real de SOC**.

**🛡️ 7. Seguridad de Windows**

Vamos a estudiar:

-   Windows Defender.

-   Firewall de Windows.

-   UAC.

-   Windows Update.

-   BitLocker.

-   Credential Guard.

-   SmartScreen.

-   Control de aplicaciones.

Y veremos **qué protege cada mecanismo y qué intenta hacer un atacante
para evadirlo**.

**🕵️ 8. Windows desde la perspectiva del atacante**

No vamos a estudiar Windows solamente como usuario.

Vamos a preguntarnos:

**\"Si yo fuera un atacante y consiguiera acceso a esta máquina, ¿qué
intentaría hacer?\"**

Estudiaremos conceptos como:

-   Reconocimiento.

-   Enumeración.

-   Escalada de privilegios.

-   Persistencia.

-   Movimiento lateral.

-   Credential dumping.

-   PowerShell malicioso.

-   LOLBins.

-   Ejecución de comandos.

-   Manipulación de servicios.

Todo desde una perspectiva **defensiva y de detección**.

**🔍 9. Windows desde la perspectiva del SOC**

Finalmente vamos a unir todo.

Por ejemplo:

Usuario

↓

Login sospechoso

↓

4624 / 4625

↓

PowerShell

↓

4688

↓

Conexión externa

↓

Firewall / DNS

↓

Posible incidente

Y aprenderás a reconstruir la historia de un ataque a partir de los
registros.

**🧪 10. Laboratorios**

Quiero que esta etapa tenga mucho más trabajo práctico que la etapa de
redes.

Por ejemplo:

**Laboratorio 1**

Crear usuarios y grupos.

**Laboratorio 2**

Investigar procesos.

**Laboratorio 3**

Analizar conexiones:

netstat

**Laboratorio 4**

Investigar eventos:

Event Viewer

**Laboratorio 5**

Buscar intentos de login fallidos.

**Laboratorio 6**

Detectar creación de usuarios.

**Laboratorio 7**

Analizar PowerShell.

**Laboratorio 8**

Investigar un incidente simulado.

**🎯 Objetivo al terminar Windows**

Quiero que puedas recibir algo como:

ALERTA SOC

Equipo: PC-VENTAS-04

Usuario: juan

Evento: 4625

20 intentos fallidos

↓

Evento 4624

Login exitoso

↓

PowerShell ejecutado

↓

Evento 4688

↓

Conexión externa

↓

Dominio sospechoso

Y que seas capaz de decir:

**\"Esto podría ser un ataque de fuerza bruta seguido de acceso exitoso
y ejecución sospechosa. Necesito investigar el usuario, el proceso que
inició PowerShell, el origen de la conexión y la actividad
posterior.\"**

Eso es exactamente el tipo de razonamiento que quiero desarrollar
contigo.

**🧭 Y después de Windows\...**

Una vez terminemos esta etapa, seguimos con:

**🐧 Semana 4 --- Linux**

Y ahí vamos a profundizar todavía más en:

-   Bash.

-   Procesos.

-   Usuarios.

-   Permisos.

-   SSH.

-   Logs.

-   grep.

-   awk.

-   sed.

-   journalctl.

-   systemctl.

-   Investigación de incidentes.

Después podremos entrar en herramientas específicas de SOC:

**Wireshark → SIEM → EDR → IDS/IPS → análisis de logs → detección →
respuesta a incidentes.**
