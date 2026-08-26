**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 28: Windows desde la perspectiva del atacante**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Mentalidad ofensiva (defensiva) + Detección

Para defender Windows bien, debes pensar como quien quiere vulnerarlo.
Estudiaremos las fases del atacante **desde una perspectiva defensiva y
de detección**: conocer el "qué haría" te permite colocar las alarmas
correctas.

**🎯 Objetivos de este módulo**

-   Recorrer la cadena de ataque: recon → explotación → persistencia →
    movimiento lateral → exfiltración.
-   Conocer técnicas clave: escalada, LOLBins, PowerShell malicioso.
-   Entender **credential dumping**, **persistencia** y **movimiento
    lateral**.
-   Relacionar cada técnica con los Event <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a> que la delatan.

**1. Reconocimiento y enumeración**

El atacante recopila información:

-   Usuarios y grupos (`net user`, `net localgroup`).
-   Sistema y parches (`systeminfo`).
-   Procesos y servicios (`tasklist`, `sc query`).
-   Red (`ipconfig`, `netstat`).

Detección: comandos de enumeración masiva, especialmente fuera de
horario o desde cuentas no administrativas.

**2. Escalada de privilegios**

Busca pasar de usuario estándar a SYSTEM/Administrador. Técnicas:

-   Bypass UAC.
-   Explotar servicio mal configurado.
-   Abusar de tareas programadas.

Detección: 4672 (privilegios especiales), creación de servicios (7045),
modificación de tareas.

**3. Persistencia**

Quiere seguir dentro tras reiniciar:

-   Servicio propio (7045).
-   Clave de Registro de autoarranque (Run / RunOnce).
-   Tarea programada.
-   Cuenta nueva con privilegios (4720 + 4728).

Detección: revisar 7045, 4720, 4728 y claves de autoarranque.

**4. Credential dumping**

Roba credenciales en memoria:

-   Volcado de **LSASS** para obtener hashes/NTLM.
-   **Kerberoasting**: pide service tickets para crackearlos.

Detección: herramientas como `mimikatz`, accesos anómalos a LSASS,
muchas solicitudes de service tickets.

**5. Movimiento lateral**

Una vez dentro de un equipo, salta a otros:

-   **PsExec**: ejecución remota vía SMB.
-   **WMI** / **WinRM**.
-   Uso de credenciales robadas (Pass-the-Hash).

Detección: inicios de sesión tipo 3 (red) hacia múltiples equipos,
creación de procesos remotamente.

**6. LOLBins y PowerShell malicioso**

Como vimos en el módulo 25, abusa de binarios legítimos:

-   `powershell -enc` para ocultar comandos.
-   `certutil` / `bitsadmin` para descargas.
-   `wmic` para ejecución remota.

Detección: 4688 con línea de comandos sospechosa, scripts codificados.

**7. Ejecución de comandos y manipulación de servicios**

El atacante puede:

-   Crear/modificar servicios para ejecutar su payload.
-   Manipular el Registro para autoarranque.
-   Desactivar defensas (Defender, logs).

Detección: 7045, cambios en claves de Run, eventos 1102 (borrado de
logs).

**8. Cadena de ataque típica**

Phishing

↓

Ejecución (factura.exe)

↓

PowerShell

↓

Recon / enumeración

↓

Escalada / dumping

↓

Persistencia

↓

Movimiento lateral

↓

Exfiltración / C2

Cada flecha deja **evidencia** en logs, procesos o red. El SOC las une.

**🧪 Laboratorio recomendado (defensivo)**

1.  Enumera tu propia máquina con `net user`, `systeminfo`,
    `tasklist` y anota qué vería un atacante.
2.  Revisa en `eventvwr` los eventos 4720, 4728 y 7045.
3.  Piensa: ¿dónde colocarías una alerta para cada fase anterior?
4.  (Sin herramientas ofensivas) describe cómo detectarías una tarea
    programada creada por un atacante.

**📝 Evaluación — Módulo 28: Windows desde la perspectiva del atacante**

**🔹 Pregunta 1**

El "reconocimiento" busca principalmente:

**A)** Apagar el equipo\
**B)** Reunir información (usuarios, servicios, red)\
**C)** Cifrar discos\
**D)** Borrar logs

**🔹 Pregunta 2**

Crear una cuenta nueva y subirla a Administradores es una técnica de:

**A)** Persistencia\
**B)** Impresión\
**C)** Actualización\
**D)** Spam

**🔹 Pregunta 3**

Volcar LSASS para robar hashes es:

**A)** Credential dumping\
**B)** Movimiento lateral\
**C)** Cifrado\
**D)** Phishing

**🔹 Pregunta 4**

Kerberoasting ataca:

**A)** El firewall\
**B)** Service tickets de Active Directory\
**C)** El registro\
**D)** BitLocker

**🔹 Pregunta 5**

Una clave de Registro Run usada para autoarrancar malware es:

**A)** Persistencia\
**B)** Reconocimiento\
**C)** Exfiltración\
**D)** Spoofing

**🔹 Pregunta 6**

`powershell -enc` se usa para:

**A)** Actualizar Windows\
**B)** Ocultar el comando real\
**C)** Imprimir\
**D)** Crear usuarios

**🔹 Pregunta 7**

PsExec suele asociarse a:

**A)** Movimiento lateral remoto\
**B)** Cifrado de disco\
**C)** Antivirus\
**D)** Firewall

**🔹 Pregunta 8**

El borrado del log de seguridad (1102) suele ser:

**A)** Mantenimiento\
**B)** Intento de encubrir evidencias\
**C)** Actualización\
**D)** Error de red

**🔹 Pregunta 9 — Caso SOC**

Varios equipos muestran inicios de sesión tipo 3 (red) desde una misma
cuenta hacia muchos servidores en minutos. Sugiere:

**A)** Actualización central\
**B)** Movimiento lateral automatizado\
**C)** Impresión\
**D)** Reinicio

**🔹 Pregunta 10**

Relaciona: 4720 + 4728 + 7045 en poco tiempo apunta a:

**A)** Fuerza bruta\
**B)** Persistencia con cuenta y servicio privilegiados\
**C)** Phishing de correo\
**D)** Spam

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: reune información.
2. **A**: persistencia (y escalada).
3. **A — Credential dumping**.
4. **B — Kerberoasting** sobre service tickets.
5. **A**: persistencia vía autoarranque.
6. **B**: oculta el comando.
7. **A**: movimiento lateral.
8. **B**: encubrimiento.
9. **B**: movimiento lateral.
10. **B**: persistencia con cuenta y servicio.

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
