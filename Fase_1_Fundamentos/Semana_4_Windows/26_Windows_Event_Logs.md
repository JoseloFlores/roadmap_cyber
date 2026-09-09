**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 26: Windows Event Logs**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Detección + Análisis de eventos de seguridad

Este es **uno de los módulos más importantes de toda la semana**. Los
logs son la materia prima del SOC. Aquí aprendes a leer lo que Windows
ya registra por defecto y a reconocer los eventos clave de seguridad.

**🎯 Objetivos de este módulo**

-   Abrir el **Visor de eventos** (`eventvwr.msc`).
-   Conocer los logs **Security, System, Application, PowerShell**.
-   Memorizar los **Event <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a>** más relevantes para SOC.
-   Entender la diferencia entre inicio exitoso y fallido.
-   Saber correlacionar eventos para reconstruir incidentes.

**1. El Visor de eventos**

`Win + R` → `eventvwr.msc`

Rutas principales:

-   **Registros de Windows → Seguridad**: auditoría de inicios,
    privilegios, cuenta.
-   **Registros de Windows → Sistema**: arranque, controladores,
    errores.
-   **Registros de Windows → Aplicación**: errores de programas.
-   **Registros de aplicaciones y servicios → Microsoft → Windows →
    PowerShell**: scripts ejecutados (si el logging está activado).

**2. Event IDs imprescindibles**

| Event ID | Significado | Por qué importa al SOC |
| :--- | :--- | :--- |
| **4624** | Inicio de sesión exitoso | ¿De dónde? ¿A qué hora? |
| **4625** | Inicio de sesión fallido | Fuerza bruta, usuario erróneo |
| **4672** | Privilegios especiales asignados | Posible elevación |
| **4688** | Creación de proceso | ¿Qué se ejecutó y con qué padre? |
| **4689** | Fin de proceso | Cierre de la ejecución |
| **4720** | Creación de cuenta | Persistencia, cuenta falsa |
| **4722** | Cuenta habilitada | Reactivación sospechosa |
| **4728** | Miembro agregado a grupo (global) | Escalada de privilegios |
| **4732** | Miembro agregado a grupo (local) | Escalada local |
| **7045** | Instalación de servicio | Persistencia vía servicio |
| **1102** | Borrado de log de seguridad | Intento de encubrimiento |

**3. 4624 vs 4625**

-   **4625** repetido de una cuenta = posible **fuerza bruta**.
-   **4624** tras muchos 4625 = acceso exitoso tras ataque.
-   El campo **<a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a>** ayuda: `2` (interactivo), `3` (red),
    `10` (RDP/RemoteInteractive). Muchos 4624 tipo `3` desde <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>
    externa pueden ser escaneo.

**4. 4688 (creación de proceso)**

Si está habilitado el **Audit Process Creation**, 4688 muestra:

-   Nombre del proceso.
-   **Process ID** y **Parent Process ID**.
-   Línea de comandos (si se configuró).

Esto permite trazar: `explorer.exe` → `powershell.exe` → conexión.

**5. Borrado de logs (1102)**

Un atacante que borra el log de seguridad (1102) intenta **eliminar
evidencia**. El propio borrado es, por sí mismo, una alerta grave.

**6. Correlación básica**

Un incidente real se reconstruye uniendo IDs:

4625 (varios)

↓

4624 (éxito)

↓

4688 (powershell.exe)

↓

Conexión externa (netstat / Sysmon)

↓

Posible compromiso

Esto es **correlación de eventos**, el corazón del trabajo SOC.

**7. Limitaciones**

Los logs nativos no siempre traen la línea de comandos ni la conexión
de red. Por eso en fases posteriores usaremos **Sysmon** (Semana 8) y
un **<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>** (Semana 6) para enriquecerlos.

**🧪 Laboratorio recomendado**

1.  Abre `eventvwr.msc` → Seguridad.
2.  Filtra por ID `4624` y `4625`: ¿ves tus propios inicios?
3.  Busca el ID `4672` (privilegios especiales).
4.  (Opcional) Habilita la política *Audit Process Creation* y lanza
    un proceso para ver el 4688.
5.  Escribe en papel una cadena: 4625 → 4624 → 4688 → conexión.

**📝 Evaluación — Módulo 26: Windows Event Logs**

**🔹 Pregunta 1**

¿Qué herramienta gráfica abre los logs de Windows?

**A)** `regedit`\
**B)** `eventvwr.msc`\
**C)** `services.msc`\
**D)** `taskschd.msc`

**🔹 Pregunta 2**

El Event ID 4625 indica:

**A)** Inicio exitoso\
**B)** Inicio fallido\
**C)** Creación de proceso\
**D)** Borrado de log

**🔹 Pregunta 3**

Varios 4625 seguidos sugieren:

**A)** Actualización\
**B)** Fuerza bruta\
**C)** Apagado\
**D)** Impresión

**🔹 Pregunta 4**

El Event ID 4688 corresponde a:

**A)** Creación de proceso\
**B)** Borrado de usuario\
**C)** Inicio de sesión\
**D)** Instalación de servicio

**🔹 Pregunta 5**

El Event ID 7045 indica:

**A)** Creación de cuenta\
**B)** Instalación de servicio\
**C)** Inicio de sesión\
**D)** Privilegios especiales

**🔹 Pregunta 6**

El Event ID 1102 indica:

**A)** Inicio exitoso\
**B)** Borrado del log de seguridad\
**C)** Proceso nuevo\
**D)** Error de red

**🔹 Pregunta 7**

¿Qué campo del 4624 ayuda a distinguir un inicio en consola de uno por
RDP?

**A)** Logon Type\
**B)** <a href="../../GLOSARIO.md#rid" target="_blank">RID</a>\
**C)** <a href="../../GLOSARIO.md#pid" target="_blank">PID</a>\
**D)** <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>

**🔹 Pregunta 8**

El Event ID 4720 indica:

**A)** Borrado de log\
**B)** Creación de cuenta\
**C)** Descarga de archivo\
**D)** Reinicio

**🔹 Pregunta 9 — Caso SOC**

Secuencia: 20 eventos 4625 (cuenta `admin`) → 1 evento 4624 → 4688
(`powershell.exe`). Conclusión más razonable:

**A)** Mantenimiento normal.\
**B)** Fuerza bruta seguida de acceso y ejecución sospechosa.\
**C)** Error de impresora.\
**D)** Actualización programada.

**🔹 Pregunta 10**

¿Por qué el SOC valora el Event ID 1102 aunque sea "solo un borrado"?

**A)** Porque mejora el rendimiento.\
**B)** Porque suele ser un intento de encubrir evidencias.\
**C)** Porque crea usuarios.\
**D)** Porque cifra el disco.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B — `eventvwr.msc`**.
2. **B — 4625**: inicio fallido.
3. **B**: fuerza bruta.
4. **A — 4688**: creación de proceso.
5. **B — 7045**: instalación de servicio.
6. **B — 1102**: borrado de log de seguridad.
7. **A — Logon Type** (10 = RDP).
8. **B — 4720**: creación de cuenta.
9. **B**: fuerza bruta + acceso + ejecución.
10. **B**: borrar logs suele ser encubrimiento.

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ✅ **Módulo 25 — CMD y PowerShell**
-   ✅ **Módulo 26 — Windows Event Logs**
-   ⚪ Módulo 27 — Seguridad de Windows
-   ⚪ Módulo 28 — Windows desde la perspectiva del atacante
-   ⚪ Módulo 29 — Investigación SOC en Windows
