**🖥️ Carrera de Analista SOC**

**Semana 4 — Windows**

**Módulo 25: CMD y PowerShell**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Línea de comandos + Detección SOC

Esta es **una de las partes más importantes de la semana** para un
Analista SOC. Tanto el atacante como el defensor usan la línea de
comandos: dominarla te permite investigar y entender qué hizo un
adversario.

**🎯 Objetivos de este módulo**

-   Diferenciar `cmd.exe` de `powershell.exe`.
-   Usar comandos clave de reconocimiento y red.
-   Entender por qué **PowerShell es peligroso y legítimo a la vez**.
-   Conocer cmdlets básicos de PowerShell para análisis.
-   Detectar comandos sospechosos (codificados, descargas, etc.).

**1. CMD (Símbolo del sistema)**

`cmd.exe` es el intérprete clásico. Comandos esenciales:

```cmd
ipconfig            # configuración de red
ipconfig /all       # incluye MAC y DNS
ipconfig /flushdns  # limpia caché DNS
ping 8.8.8.8        # conectividad básica
tracert google.com  # ruta hasta el destino
netstat -ano        # conexiones y puertos (a=all, n=numérico, o=PID)
systeminfo          # resumen del sistema
whoami              # usuario actual y privilegios
net user            # usuarios locales
net localgroup      # grupos locales
```

`netstat -ano` es clave: muestra IP, puerto y **PID**, permitiendo
cruzar con `tasklist` para saber qué proceso abrió la conexión.

**2. PowerShell**

`powershell.exe` es mucho más potente: accede a .NET, WMI y la API de
Windows. Cmdlets comunes:

```powershell
Get-Process
Get-Service
Get-EventLog -LogName Security
Get-WinEvent -LogName System
Get-ChildItem C:\Users
Get-NetTCPConnection        # alternativa moderna a netstat
Get-CimInstance Win32_Process | Select Name, ParentProcessId, CommandLine
```

Obtener la **línea de comandos completa** de un proceso es vital en
investigación, porque revela qué argumentos usó (por ejemplo, una
descarga oculta).

**3. ¿Por qué PowerShell asusta a los defensores?**

PowerShell puede:

-   Descargar y ejecutar código desde internet.
-   Codificar comandos en Base64 para ocultarlos.
-   Usar `Invoke-WebRequest` o `IEX` para traer scripts.

Ejemplo sospechoso (no lo ejecutes):

```powershell
powershell -enc <cadena_base64>
```

`--enc` (`-EncodedCommand`) oculta la intención real. Un SOC debe
revisar **qué comando decodificado** se ejecutó.

**4. LOLBins**

Algunas herramientas legítimas de Windows pueden ser abusadas:

-   `certutil`: puede descargar archivos.
-   `bitsadmin`: transferencia en segundo plano.
-   `powershell` / `cmd`: ejecución.
-   `wmic`: consultas y ejecución remota.

No son malware, pero un analista las mira con sospecha cuando aparecen
en una cadena de ataque.

**5. Detección de comandos sospechosos**

Señales en un evento de PowerShell:

-   Parámetro `-enc` o `-EncodedCommand`.
-   `IEX (New-Object Net.WebClient)...` (descarga y ejecuta).
-   Nombres ofuscados o sin espacios (`Inv0ke-WebRequest`).
-   Ejecución desde `C:\Users\...\AppData` o `%TEMP%`.

**6. Conexión con el SOC**

Un evento de PowerShell (Event ID 4104 en el log de PowerShell, cuando
el logging está habilitado) puede mostrar el script exacto ejecutado.
Combinado con `netstat` y el proceso padre, reconstruyes la historia.

**🧪 Laboratorio recomendado**

1.  Abre CMD y ejecuta `ipconfig /all`, `systeminfo`, `whoami`.
2.  Ejecuta `netstat -ano` y anota una conexión ESTABLISHED con su PID.
3.  Abre PowerShell y ejecuta `Get-NetTCPConnection`.
4.  Ejecuta `Get-Process | Select-Object Name, Id, Path` y observa
    rutas.
5.  (Sin ejecutar) Analiza mentalmente por qué `powershell -enc ...`
    merece investigación.

**📝 Evaluación — Módulo 25: CMD y PowerShell**

**🔹 Pregunta 1**

¿Qué combinación de `netstat` muestra conexiones, puertos numéricos y
PID?

**A)** `netstat -e`\
**B)** `netstat -ano`\
**C)** `netstat /?`\
**D)** `netstat -r`

**🔹 Pregunta 2**

Para ver la línea de comandos completa de un proceso en PowerShell
usamos:

**A)** `Get-Service`\
**B)** `Get-CimInstance Win32_Process | Select CommandLine`\
**C)** `ipconfig`\
**D)** `ping`

**🔹 Pregunta 3**

`powershell -enc <base64>` es peligroso porque:

**A)** Actualiza Windows.\
**B)** Oculta el comando real mediante codificación.\
**C)** Solo sirve para imprimir.\
**D)** Es un firewall.

**🔹 Pregunta 4**

`certutil` es considerado LOLBin porque puede:

**A)** Apagar el equipo.\
**B)** Descargar archivos desde la red.\
**C)** Crear usuarios.\
**D)** Cifrar discos.

**🔹 Pregunta 5**

El cmdlet para listar eventos del log de Seguridad es:

**A)** `Get-EventLog -LogName Security`\
**B)** `Get-Service`\
**C)** `Test-NetConnection`\
**D)** `Set-ExecutionPolicy`

**🔹 Pregunta 6**

`whoami` nos indica:

**A)** La IP pública.\
**B)** El usuario actual y sus privilegios.\
**C)** El sistema de archivos.\
**D)** El registro de Windows.

**🔹 Pregunta 7**

¿Por qué un analista desconfía de PowerShell lanzado desde `%TEMP%`?

**A)** Porque PowerShell nunca debe usarse.\
**B)** Porque es una ubicación típica de ejecución de malware.\
**C)** Porque requiere administrador siempre.\
**D)** Porque borra logs.

**🔹 Pregunta 8**

`Get-NetTCPConnection` es útil para:

**A)** Listar conexiones de red activas.\
**B)** Crear usuarios.\
**C)** Formatear discos.\
**D)** Editar el registro.

**🔹 Pregunta 9 — Caso SOC**

Se observa: `cmd.exe` → `powershell.exe -enc <cadena>`. El SOC debe:

**A)** Ignorarlo, PowerShell es legítimo.\
**B)** Decodificar el comando y analizarlo junto con red y proceso
padre.\
**C)** Reiniciar el equipo de inmediato.\
**D)** Desactivar la red doméstica.

**🔹 Pregunta 10**

Un LOLBin es:

**A)** Un binario legítimo de Windows abusado con fines maliciosos.\
**B)** Un controlador de impresora.\
**C)** Un tipo de firewall.\
**D)** Un virus conocido.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B — `netstat -ano`**: all, numérico, PID.
2. **B**: `CommandLine` revela argumentos.
3. **B**: `-enc` oculta la intención.
4. **B**: puede descargar archivos.
5. **A**: `Get-EventLog -LogName Security`.
6. **B**: usuario y privilegios.
7. **B**: `%TEMP%` es ubicación típica de malware.
8. **A**: lista conexiones.
9. **B**: decodificar y correlacionar.
10. **A**: binario legítimo abusado.

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ✅ **Módulo 25 — CMD y PowerShell**
-   ⚪ Módulo 26 — Windows Event Logs
-   ⚪ Módulo 27 — Seguridad de Windows
-   ⚪ Módulo 28 — Windows desde la perspectiva del atacante
-   ⚪ Módulo 29 — Investigación SOC en Windows
