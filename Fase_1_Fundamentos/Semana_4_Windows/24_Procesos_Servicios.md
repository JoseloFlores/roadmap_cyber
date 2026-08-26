**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 24: Procesos y servicios**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Sistemas + Seguridad + Análisis SOC

En el módulo 21 definimos qué es un proceso y un servicio. Aquí
profundizamos en **cómo observarlos** y, sobre todo, en cómo un analista
SOC detecta procesos y servicios sospechosos.

**🎯 Objetivos de este módulo**

-   Usar el Administrador de tareas y `tasklist` / `taskkill`.
-   Entender la relación **proceso padre → proceso hijo**.
-   Diferenciar procesos legítimos de sospechosos.
-   Conocer `services.msc` y la línea de comandos `sc`.
-   Detectar servicios usados para **persistencia**.

**1. Observar procesos (GUI)**

`Ctrl + Shift + Esc` abre el **Administrador de tareas**. Pestañas
clave:

-   **Procesos**: qué se ejecuta y su consumo.
-   **Detalles**: <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>, nombre de imagen, usuario.
-   **Servicios**: servicios en ejecución.

**2. Observar procesos (línea de comandos)**

```cmd
tasklist
```

Muestra PID, nombre de imagen y usuario. Para buscar uno concreto:

```cmd
tasklist | findstr powershell
```

Para terminar un proceso:

```cmd
taskkill /PID 1234 /F
```

**3. Proceso padre e hijo**

Cuando abres un programa, normalmente otro lo lanzó. Ejemplo:

explorer.exe

↓

notepad.exe

El **proceso padre** es `explorer.exe`; el **hijo** es `notepad.exe`.
Esto es oro para el SOC: un proceso hijo inesperado es una bandera. Por
ejemplo:

-   `powershell.exe` lanzado por `winword.exe` (Word) → posible
    macro maliciosa.
-   `cmd.exe` lanzado por `outlook.exe` → posible ejecución desde
    correo.

**4. Servicios de Windows**

Un servicio se ejecuta en segundo plano. Se gestiona con:

`services.msc` (interfaz gráfica)

O por línea de comandos:

```cmd
sc query
sc start NombreServicio
sc stop NombreServicio
sc delete NombreServicio
```

Muchos servicios legítimos corren bajo `svchost.exe`. Un atacante puede
**crear un servicio propio** para que su malware se inicie solo tras
cada reinicio (persistencia).

**5. Procesos que suelen aparecer (línea base)**

No todo lo raro es malware, pero conviene conocer la línea base:

-   `System` / `System Idle Process`.
-   `csrss.exe`, `winlogon.exe`, `lsass.exe` (maneja credenciales).
-   `svchost.exe` (host de servicios).
-   `explorer.exe` (interfaz de usuario).

`lsass.exe` es especialmente sensible: un atacante puede volcarlo
(**LSASS dumping**) para robar hashes/NTLM.

**6. Indicadores de proceso sospechoso**

-   Nombre similar a uno legítimo: `svch0st.exe`, `taskmgr32.exe`.
-   Ubicación inusual: `C:\Users\X\Downloads\svchost.exe`.
-   Padre inesperado (Word → PowerShell).
-   Se comunica a una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> externa recién al ejecutarse.
-   Se ejecuta como `SYSTEM` sin justificación.

**7. Persistencia mediante servicios**

Un atacante puede registrar un servicio:

```cmd
sc create Actualizador binPath= "C:\ruta\malware.exe"
```

Al reiniciar, el malware vuelve a ejecutarse. Por eso el SOC monitoriza
la **creación de servicios** (Event ID 7045).

**🧪 Laboratorio recomendado**

1.  Abre el Administrador de tareas y ordena por "Usuario".
2.  Ejecuta `tasklist` y localiza `powershell.exe`.
3.  Desde PowerShell, lanza `notepad.exe` y observa el padre con
    `Get-CimInstance Win32_Process` (módulo 25 lo amplía).
4.  En `services.msc`, identifica servicios que inician
    automáticamente.
5.  (Opcional, sin permisos reales) imagina cómo detectarías un servicio
    llamado `WindowsUpdateX` con ruta en `C:\Temp`.

**📝 Evaluación — Módulo 24: Procesos y servicios**

**🔹 Pregunta 1**

¿Qué relación indica que un proceso fue lanzado por otro?

**A)** Hijo → Padre\
**B)** Padre → Hijo\
**C)** Servicio → Puerto\
**D)** <a href="../../GLOSARIO.md#kernel" target="_blank">Kernel</a> → RAM

**🔹 Pregunta 2**

Ver `powershell.exe` como hijo de `winword.exe` (Word) sugiere:

**A)** Mantenimiento normal.\
**B)** Posible ejecución maliciosa desde documento.\
**C)** Error de impresión.\
**D)** Actualización de Windows.

**🔹 Pregunta 3**

El proceso que maneja credenciales y es objetivo de dumping es:

**A)** explorer.exe\
**B)** lsass.exe\
**C)** notepad.exe\
**D)** spoolsv.exe

**🔹 Pregunta 4**

¿Para qué sirve `taskkill /PID 1234 /F`?

**A)** Listar procesos.\
**B)** Forzar la terminación del PID 1234.\
**C)** Crear un servicio.\
**D)** Reiniciar la red.

**🔹 Pregunta 5**

`svchost.exe` normalmente:

**A)** Es siempre malware.\
**B)** Aloja servicios de Windows legítimos.\
**C)** Solo existe en Linux.\
**D)** Es el navegador.

**🔹 Pregunta 6**

Crear un servicio propio es una técnica de:

**A)** Persistencia.\
**B)** Borrado de logs.\
**C)** Cifrado de disco.\
**D)** Escaneo de puertos.

**🔹 Pregunta 7**

Un archivo `notepad.exe` ubicado en `C:\Users\X\AppData\Roaming\`
es:

**A)** Garantía de que es legítimo.\
**B)** Un indicador contextual de posible malware.\
**C)** Un servicio del sistema.\
**D)** El registro de Windows.

**🔹 Pregunta 8**

Para listar servicios por línea de comandos usamos:

**A)** `ipconfig`\
**B)** `sc query`\
**C)** `netstat -a`\
**D)** `ping`

**🔹 Pregunta 9 — Caso SOC**

Se detecta `cmd.exe` hijo de `outlook.exe` que luego ejecuta
`powershell.exe` con una conexión a una IP externa. Lo más razonable
es:

**A)** Ignorarlo, es correo legítimo.\
**B)** Investigar como posible cadena de ejecución maliciosa.\
**C)** Reiniciar el router.\
**D)** Desactivar el antivirus.

**🔹 Pregunta 10**

El Event ID que indica instalación de un nuevo servicio es:

**A)** 4624\
**B)** 7045\
**C)** 4672\
**D)** 4720

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: el padre lanza al hijo.
2. **B**: Word lanzando PowerShell es patrón de macro maliciosa.
3. **B — lsass.exe**: objetivo de volcado de credenciales.
4. **B**: termina el proceso forzosamente.
5. **B**: svchost aloja servicios legítimos.
6. **A**: persistencia tras reinicio.
7. **B**: la ubicación es un indicador de alerta.
8. **B — `sc query`**: lista servicios.
9. **B**: es una cadena de ejecución sospechosa típica.
10. **B — 7045**: instalación de servicio.

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ⚪ Módulo 25 — CMD y PowerShell
-   ⚪ Módulo 26 — Windows Event Logs
-   ⚪ Módulo 27 — Seguridad de Windows
-   ⚪ Módulo 28 — Windows desde la perspectiva del atacante
-   ⚪ Módulo 29 — Investigación SOC en Windows
