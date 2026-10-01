**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 32: Event <a href="../../GLOSARIO.md#log" target="_blank">Log</a> de Windows desde la vista SOC (lectura manual)**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Lectura raw + Filtro manual sin <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>

Este módulo es el puente con la Semana 4. Ya conocés los Event <a href="../../GLOSARIO.md#event-id" target="_blank">IDs</a>. Ahora aprendés a **leerlos en crudo, filtrarlos a mano y no depender del SIEM**, que es la meta de esta semana.

**🎯 Objetivos del módulo**

-   Abrir `eventvwr.msc` y filtrar por ID, fecha y origen.
-   Leer la vista XML para sacar usuario, <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> y <a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a>.
-   Distinguir 4624 vs <a href="../../GLOSARIO.md#4625" target="_blank">4625</a> vs <a href="../../GLOSARIO.md#4688" target="_blank">4688</a> vs 4720 vs <a href="../../GLOSARIO.md#7045" target="_blank">7045</a> vs <a href="../../GLOSARIO.md#1102" target="_blank">1102</a>.
-   Guardar evidencia manual para el reporte.

---

**1. Dónde mirar**

`Win + R` → `eventvwr.msc`

-   Registros de Windows → Seguridad → autenticación y cuentas.
-   Registros de Windows → Sistema → servicios y 7045.
-   Registros de Windows → Aplicación → programas.
-   Registros de aplicaciones y servicios → Microsoft → Windows → <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a> → scripts.

**2. Filtrar como L1**

Click derecho en Seguridad → `Filtrar registro actual`:

-   Por ID: `4624,4625,4688,4720,7045,1102`.
-   Por fecha: última hora / últimas 24 h.
-   Por origen: `Microsoft-Windows-Security-Auditing`.

No exportes todo el log. Filtrá primero, analizá después.

**3. Leer el XML, no solo la tabla**

Doble click → pestaña `Detalles` → `Vista XML`.

Ahí ves lo que el SIEM va a parsear:

`TimeCreated SystemTime` → <a href="../../GLOSARIO.md#timestamp" target="_blank">timestamp</a> real.

`TargetUserName` → quién.

`IpAddress / <a href="../../GLOSARIO.md#source-network-address" target="_blank">Source Network Address</a>` → desde dónde.

`LogonType` → cómo (2 consola, 3 red, 10 RDP).

`ProcessName / ParentProcessName` en 4688 → qué se ejecutó y quién lo lanzó.

La tabla te muestra el resumen. El XML te da la evidencia.

**4. Tabla rápida de <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a> para esta semana**

| **ID** | **Significado** | **Lectura SOC manual** |
| :--- | :--- | :--- |
| 4624 | Login exitoso | Mirá usuario + IP + Logon Type + hora. |
| 4625 | Login fallido | Contá cuántos, de quién y desde qué IP. |
| 4688 | Proceso creado | Mirá padre + ruta + <a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a>. |
| 4720 | Cuenta creada | ¿Quién la creó? ¿Fuera de horario? |
| 4728/4732 | Agregado a grupo | Posible escalada a admin. |
| 7045 | Servicio instalado | Ruta en `C:\Temp` = sospechoso. |
| 1102 | Log borrado | Encubrimiento, alerta grave. |

**5. Laboratorio en tu VM Windows 10**

1.  Generá ruido legítimo: bloqueá y desbloqueá sesión, fallá tu contraseña 2 veces a propósito.
2.  Filtrá Seguridad por `4624,4625`. Ubicá tus propios eventos.
3.  Abrí el XML de un 4625: anotá `TargetUserName`, `WorkstationName`, `IpAddress`.
4.  Creá un usuario de prueba `audit_test` → buscá el 4720. ¿Qué cuenta aparece como creadora?
5.  Instalá un servicio de prueba o mirá System → 7045. Anotá `ServiceName` e `ImagePath`.
6.  Guardá: click derecho → `Guardar eventos filtrados como` → `evidencia_sem5.evtx`. Esa es tu cadena de custodia básica.

**6. Patrones que tenés que ver a ojo**

4625 repetido misma cuenta = posible <a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">fuerza bruta</a>.

4625 muchas cuentas misma IP = posible <a href="../../GLOSARIO.md#password-spraying" target="_blank">password spraying</a>.

4625 → <a href="../../GLOSARIO.md#4624" target="_blank">4624</a> → 4688 `powershell.exe` = cadena a investigar.

4720 + grupo Admin + 7045 de noche = posible persistencia.

1102 en horario raro = alguien borró huellas.

**7. Error L1: quedarse en la descripción**

La pestaña General dice "Se inició sesión correctamente". Eso no alcanza.

Siempre anotá: quién, desde dónde, cómo (Logon Type), cuándo, qué hizo después.

**📚 Resumen**

EVENTVWR

= tu consola manual. FILTRO = por ID + fecha. XML = evidencia real. IDs = 4624/4625/4688/4720/7045/1102.

**🧩 Conceptos clave**

| **Concepto** | **Debes recordar** |
| :--- | :--- |
| Filtrar | Por ID antes de analizar. |
| XML | Contiene IP, usuario, Logon Type. |
| Logon Type 10 | RDP, crítico en SOC. |
| 4720 | Cuenta nueva = revisar creador. |
| EVTX | Formato para guardar evidencia. |

**🎓 Consejo como tu instructor de SOC**

Acostumbrate a leer el XML. Cuando llegues a Splunk vas a ver los mismos campos con otro nombre (`src_ip`, `user`, `LogonType`). Si ya los leíste en crudo, el SIEM no te va a marear.

---

**Evaluación — Módulo 32**

**Pregunta 1**

Para ver logins filtrás Seguridad por:

**A)** `4624,4625`.\
**B)** `7045` solo.\
**C)** `1102` solo.\
**D)** `4689` solo.

**Pregunta 2**

El XML aporta respecto a la vista General:

**A)** Nada.\
**B)** Campos exactos: timestamp, usuario, IP, Logon Type, proceso padre.\
**C)** Solo colores.\
**D)** El antivirus.

**Pregunta 3**

Logon Type 10 indica:

**A)** Interactivo local.\
**B)** Red.\
**C)** RDP / RemoteInteractive.\
**D)** Servicio.

**Pregunta 4**

Creás `audit_test` y buscás:

**A)** 4720 y quién lo creó.\
**B)** 4625.\
**C)** 4688 de Word.\
**D)** 1102.

**Pregunta 5**

Un 7045 con `ImagePath C:\Users\juan\AppData\Temp\upd.exe` es:

**A)** Normal.\
**B)** Sospechoso: servicio desde Temp, posible persistencia.\
**C)** Error <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.\
**D)** Phishing de correo.

**Pregunta 6**

`Guardar eventos filtrados como .evtx` sirve para:

**A)** Decorar.\
**B)** Guardar evidencia con cadena básica.\
**C)** Borrar logs.\
**D)** Crear usuarios.

**Pregunta 7**

4625 a 10 cuentas distintas desde una IP sugiere:

**A)** Fuerza bruta clásica.\
**B)** Password spraying.\
**C)** Apagado.\
**D)** Impresión.

**Pregunta 8**

En un 4688 lo más valioso es:

**A)** Solo el nombre.\
**B)** Padre + ruta + Command Line + usuario.\
**C)** El color.\
**D)** La hora sola.

**Pregunta 9 — Caso SOC**

20×4625 `admin` → 4624 Type 10 IP externa → 4688 powershell. Acción L1:

**A)** Ignorar.\
**B)** Anotar usuario, IP, hora, padre de PowerShell y escalar con timeline.\
**C)** Reinstalar.\
**D)** Cambiar impresora.

**Pregunta 10**

Ver solo "Se inició sesión correctamente" sin mirar XML es error porque:

**A)** Falta contexto: quién, desde dónde, cómo y qué hizo después.\
**B)** Sobran datos.\
**C)** Es ilegal.\
**D)** Borra logs.

**⛔ DETENTE AQUÍ.**

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **A**.
2. **B**: el XML es lo que parsea el SIEM.
3. **C — RDP**.
4. **A — 4720**.
5. **B**: Temp + servicio = investigar.
6. **B**.
7. **B — spraying**.
8. **B**.
9. **B**: documentar y escalar, no concluir solo.
10. **A**: sin contexto no hay veredicto.

**🏆 Resultado**

| **Correctas** | **Nivel** |
| :--- | :--- |
| **10/10** | ⭐ Excelente. |
| **8–9/10** | 🟢 Muy buen nivel. |
| **6–7/10** | 🟡 Buen progreso. |
| **4–5/10** | 🟠 Repasar. |
| **0–3/10** | 🔴 Reestudiar. |

**📍 Progreso — Semana 5**

-   ✅ **Módulo 30 — ¿Qué es un log?**
-   ✅ **Módulo 31 — Tipos de logs**
-   ✅ **Módulo 32 — Event Log de Windows**
-   ⚪ Módulo 33 — <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a> en Linux
-   ⚪ Módulo 34 — Anatomía de un log raw
-   ⚪ Módulo 35 — Fuerza bruta y logins inusuales
-   ⚪ Módulo 36 — Usuarios admin, persistencia e investigación
