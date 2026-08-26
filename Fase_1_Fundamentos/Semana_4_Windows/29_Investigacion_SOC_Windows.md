**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 29: Investigación <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> en Windows**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1\
**Enfoque:** Aplicación práctica + Correlación de eventos

Este es el módulo que une todo lo aprendido. Ya no estudiamos una sola
pieza: aprendemos a **reconstruir la historia de un incidente** uniendo
identidad, procesos, red y logs. Es exactamente el trabajo diario de un
Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**🎯 Objetivos de este módulo**

-   Aplicar el método de investigación basado en preguntas.
-   Correlacionar Event <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a> (4625 → 4624 → 4688 → red).
-   Usar una línea de tiempo para ordenar los hechos.
-   Redactar un veredicto y las siguientes acciones.
-   Conectar lo aprendido con las próximas fases (Sysmon, <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>).

**1. El método de las preguntas**

Ante cualquier alerta, un analista responde siempre lo mismo:

-   **¿Quién?** (usuario, cuenta, RID).
-   **¿Qué?** (proceso, servicio, archivo).
-   **¿Cuándo?** (timestamp).
-   **¿Desde dónde?** (ruta, equipo, <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>).
-   **¿Proceso padre?** (quién lo lanzó).
-   **¿Con qué red se comunicó?** (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, dominio, puerto).
-   **¿Qué ocurrió después?** (persistencia, movimiento lateral).

**2. Construir la línea de tiempo**

Ordena los eventos por hora. Ejemplo:

10:31 — 4625 x15 (cuenta `juan`)

10:33 — 4624 (éxito)

10:33 — 4688 (`powershell.exe`, padre `explorer.exe`)

10:34 — conexión <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443 a 203.0.113.50

10:35 — 7045 (servicio `ActualizadorX`)

La secuencia revela un ataque, no eventos aislados.

**3. Caso práctico A: Fuerza bruta**

Alerta: 40 eventos 4625 en 1 minuto para `admin`.

Preguntas:

-   ¿La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen es interna o externa?
-   ¿Hubo un 4624 tras los fallos?
-   ¿El 4624 fue tipo 3 (red) o 10 (RDP)?
-   ¿Se creó algún proceso después (4688)?

Veredicto probable: ataque de fuerza bruta; investigar si hubo acceso
exitoso.

**4. Caso práctico B: PowerShell sospechoso**

Alerta: 4688 `powershell.exe` con padre `outlook.exe`, parámetro
`-enc`.

Preguntas:

-   ¿Qué decodifica el `-enc`?
-   ¿A qué dominio/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> se conectó?
-   ¿Hubo 4625 previos (phishing con credenciales)?
-   ¿Se creó persistencia (7045 / Registro Run)?

Veredicto: posible ejecución maliciosa desde correo; aislar equipo y
decodificar comando.

**5. Caso práctico C: Persistencia**

Alerta: 4720 (cuenta `svc_bk`) + 4728 (a Administrators) + 7045
(servicio).

Preguntas:

-   ¿Quién creó la cuenta? (¿cuenta admin legítima?)
-   ¿Fuera de horario?
-   ¿El servicio apunta a `C:\Windows` o a `C:\Temp`?

Veredicto: alta probabilidad de persistencia con privilegios; desactivar
servicio y cuenta, y cazar en otros equipos.

**6. Redactar el veredicto**

Un buen informe <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> incluye:

1.  Resumen (qué pasó).
2.  Línea de tiempo.
3.  Evidencia (Event <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a>, <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a>, rutas).
4.  Nivel de confianza.
5.  Acciones recomendadas (aislar, cazar, bloquear <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, rotar
    credenciales).

**7. De Windows al <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> y Sysmon**

Los logs nativos son solo el inicio. En la Fase 2 aprenderás:

-   **Sysmon** (Semana 8): telemetría rica de procesos y red.
-   **Splunk** (Semanas 6-7): búsqueda centralizada (SPL).
-   **<a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**: correlación automática de miles de eventos.

Tu trabajo hoy (correlacionar a mano) es la base de lo que luego hará
la herramienta por ti.

**🧪 Laboratorio recomendado**

1.  Toma la alerta hipotética: equipo PC-VENTAS-04, usuario `juan`,
    20 fallos 4625 seguidos de 4624, luego 4688 `powershell.exe`, luego
    conexión a dominio `update-security.xyz`.
2.  Construye la línea de tiempo.
3.  Escribe un veredicto de 3 líneas.
4.  Indica 3 acciones inmediatas.

**📝 Evaluación — Módulo 29: Investigación <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> en Windows**

**🔹 Pregunta 1**

La primera pregunta ante una alerta suele ser:

**A)** ¿Qué impresora usó?\
**B)** ¿Quién, qué, cuándo, desde dónde?\
**C)** ¿Qué antivirus hay?\
**D)** ¿Qué versión de Windows?

**🔹 Pregunta 2**

Ordenar eventos por hora se llama:

**A)** Cifrado\
**B)** Línea de tiempo\
**C)** Enumeración\
**D)** Spoofing

**🔹 Pregunta 3**

Unir 4625 → 4624 → 4688 → conexión es:

**A)** Resolución <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>\
**B)** Correlación de eventos\
**C)** Formateo\
**D)** Fuerza bruta inversa

**🔹 Pregunta 4**

Ante 40 fallos 4625 para `admin` en 1 minuto, lo primero es:

**A)** Reiniciar el router\
**B)** Verificar si hubo un 4624 exitoso y desde qué <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>\
**C)** Apagar la impresora\
**D)** Borrar logs

**🔹 Pregunta 5**

`powershell.exe` con padre `outlook.exe` y `-enc` sugiere:

**A)** Actualización\
**B)** Ejecución sospechosa desde correo\
**C)** Error de red\
**D)** Mantenimiento

**🔹 Pregunta 6**

4720 + 4728 + 7045 fuera de horario apunta a:

**A)** Persistencia con cuenta y servicio\
**B)** Fuerza bruta\
**C)** Phishing de correo\
**D)** Spam

**🔹 Pregunta 7**

Un buen informe <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> incluye:

**A)** Solo la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>\
**B)** Resumen, línea de tiempo, evidencia y acciones\
**C)** La contraseña del usuario\
**D)** Un dibujo

**🔹 Pregunta 8**

Sysmon (Semana 8) aporta respecto a los logs nativos:

**A)** Menos datos\
**B)** Telemetría rica de procesos y red\
**C)** Solo eventos de impresión\
**D)** Cifrado de discos

**🔹 Pregunta 9 — Caso <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

PC-RRHH-07: 4625 x10 → 4624 → 4688 `powershell.exe` (padre
`winword.exe`) → conexión a <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> externa. Veredicto razonable:

**A)** Mantenimiento normal.\
**B)** Documento malicioso que ejecutó PowerShell y conectó a C2; aislar
y decodificar.\
**C)** Error de impresora.\
**D)** Actualización.

**🔹 Pregunta 10**

La habilidad de correlacionar eventos a mano sirve para:

**A)** Nada, lo hace el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> solo.\
**B)** Entender la base que luego automatiza el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>/Sysmon.\
**C)** Apagar equipos.\
**D)** Crear virus.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: quién, qué, cuándo, dónde.
2. **B — línea de tiempo**.
3. **B — correlación**.
4. **B**: verificar acceso exitoso y origen.
5. **B**: ejecución desde correo.
6. **A**: persistencia.
7. **B**: informe completo.
8. **B**: telemetría rica.
9. **B**: macro/doc malicioso a C2.
10. **B**: base del <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

**🏆 TABLA DE RESULTADOS — Semana 4**

| Resultado | Evaluación |
| :--- | :--- |
| **10/10** | 🟢 Excelente — comprensión y razonamiento <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> muy sólidos. |
| **8–9/10** | 🟢 Muy buen nivel — listo para avanzar. |
| **6–7/10** | 🟡 Buen progreso — reforzar conceptos. |
| **4–5/10** | 🟠 Repasar fundamentos. |
| **0–3/10** | 🔴 Volver a estudiar los módulos. |

**📍 Progreso — Semana 4 (COMPLETADA)**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ✅ **Módulo 25 — CMD y PowerShell**
-   ✅ **Módulo 26 — Windows Event Logs**
-   ✅ **Módulo 27 — Seguridad de Windows**
-   ✅ **Módulo 28 — Windows desde la perspectiva del atacante**
-   ✅ **Módulo 29 — Investigación <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> en Windows**

**🎯 Meta de la Semana 4**

Quiero que al recibir algo como:

> ALERTA: PC-VENTAS-04, usuario `juan`, 20 fallos 4625, luego 4624,
> PowerShell (4688), conexión a dominio sospechoso.

Puedas decir:

**"Esto parece fuerza bruta seguida de acceso exitoso y ejecución
sospechosa. Debo investigar el usuario, el proceso padre, el destino de
la conexión y la actividad posterior."**

Esa es la mentalidad <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>. ¡Siguiente parada: las redes de la Fase 2 y
los <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>!
