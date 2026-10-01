**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 36: Creación de usuarios admin, persistencia e investigación SOC**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** <a href="../../GLOSARIO.md#correlacion" target="_blank">Correlación</a> manual + Veredicto + Cierre de semana

Este módulo cierra la semana. Unís autenticación + cuentas + procesos + red y redactás como un L1. Es el mismo método del Módulo 29, ahora con logs de los <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> sistemas.

**🎯 Objetivos del módulo**

-   Detectar creación y elevación de usuarios administradores.
-   Detectar persistencia por servicio y tarea.
-   Construir línea de tiempo mixta Linux + Windows.
-   Redactar veredicto con nivel de confianza y acciones.

---

**1. Qué buscar: cuentas**

Windows:

4720 cuenta creada → 4728/4732 a Admin → 4672 privilegios.

Preguntá: ¿quién la creó? ¿fuera de horario? ¿nombre parecido a legítimo (`adm1n`, `svc_bk`)?

Linux:

`grep -E "useradd|adduser|usermod" /var/log/auth.log`

`grep "sudo" /var/log/auth.log | grep COMMAND`

`cat /etc/passwd | grep -E "0:0|/bin/bash"` → ¿nuevo UID 0?

Cuenta nueva + <a href="../../GLOSARIO.md#sudo" target="_blank">sudo</a> nocturno = investigar ya.

**2. Qué buscar: persistencia**

Windows: <a href="../../GLOSARIO.md#7045" target="_blank">7045</a> servicio nuevo. Mirá `ImagePath`: `C:\Windows` esperable, `C:\Temp` o `AppData` sospechoso.

Linux: `crontab -l`, `/etc/cron*`, `systemctl list-timers`, `grep "install" /var/log/dpkg.log`.

Cadena típica:

cuenta creada

↓

elevada a admin

↓

servicio/tarea creada

↓

conexión externa

**3. Laboratorio en tus VMs**

Windows (como admin de prueba):

1.  Creá `svc_backup`: mirá 4720 + creador.
2.  Agregalo a Administradores: mirá 4728.
3.  Creá tarea o servicio de prueba que ejecute `calc.exe`: mirá 7045 / Task Scheduler.
4.  Anotá timeline con horas exactas.

Linux:

1.  `sudo useradd svc_backup && sudo usermod -aG sudo svc_backup`.
2.  `grep "useradd\|usermod" /var/log/auth.log | tail`.
3.  `(crontab -l; echo "* * * * * echo test") | crontab -` solo prueba → `grep CRON /var/log/syslog | tail` → luego borrala con `crontab -r`.
4.  Guardá: `grep "svc_backup" /var/log/auth.log > ~/evidencia_persistencia.txt`.

**4. Método de investigación (repaso M29)**

¿QUIÉN? usuario, <a href="../../GLOSARIO.md#rid" target="_blank">RID</a>, grupo.

¿QUÉ? proceso, servicio, archivo.

¿CUÁNDO? <a href="../../GLOSARIO.md#timestamp" target="_blank">timestamp</a> ordenado.

¿DESDE DÓNDE? <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> origen, ruta, equipo.

¿PADRE? quién lanzó el proceso.

¿RED? IP/dominio/puerto destino.

¿DESPUÉS? persistencia, lateral, borrado (<a href="../../GLOSARIO.md#1102" target="_blank">1102</a> / hueco).

**5. Línea de tiempo ejemplo**

10:31 — <a href="../../GLOSARIO.md#4625" target="_blank">4625</a> ×15 `juan` IP 10.10.20.15

10:33 — <a href="../../GLOSARIO.md#4624" target="_blank">4624</a> éxito Type 10 misma IP

10:33 — <a href="../../GLOSARIO.md#4688" target="_blank">4688</a> `powershell.exe` padre `explorer.exe`

10:34 — <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443 a 203.0.113.50

10:35 — 7045 `ActualizadorX` desde Temp

En Linux sería: `Failed ×15` → `Accepted` → `sudo COMMAND` → conexión → `cron` nuevo.

La historia es la misma, cambia el idioma del <a href="../../GLOSARIO.md#log" target="_blank">log</a>.

**6. Cómo redactar el veredicto**

1.  Resumen (2 líneas).
2.  Timeline.
3.  Evidencia (<a href="../../GLOSARIO.md#ids" target="_blank">IDs</a>, <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a>, rutas, comandos).
4.  Confianza: baja/media/alta.
5.  Acciones: aislar, bloquear IP, deshabilitar cuenta/servicio, rotar credencial, cazar en otros hosts.

Ejemplo:

> "<a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">Fuerza bruta</a> contra `juan` desde 10.10.20.15 con éxito RDP y ejecución <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a> + persistencia. Confianza alta. Aislar PC-VENTAS-04, deshabilitar cuenta, bloquear IP, decodificar <a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a>."

**7. De lo manual al <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> (puente a Semana 6)**

Lo que hiciste a mano (`grep`, filtro <a href="../../GLOSARIO.md#event-viewer" target="_blank">Event Viewer</a>, timeline en papel) es lo que Splunk hará con SPL:

`index=* user=juan (4625 OR 4624 OR 4688)` en vez de 3 filtros.

`stats count by src_ip` en vez de `uniq -c`.

Pero si no sabés hacerlo en raw, el SPL te va a mentir y no te vas a dar cuenta.

**🧪 Laboratorio final**

Alerta: PC-VENTAS-04, `juan`, 20×4625 → 4624 → 4688 powershell → `update-security.xyz`.

1.  Timeline con horas ficticias pero ordenadas.
2.  Veredicto 3 líneas.
3.  3 acciones inmediatas.
4.  Repetilo con `auth.log` ficticio: `Failed ×20` → `Accepted` → `sudo`.

**📚 Resumen semana**

LOG

= evidencia. TIPOS = dónde buscar. WINDOWS = filtrar + XML. <a href="../../GLOSARIO.md#syslog" target="_blank">SYSLOG</a> = <a href="../../GLOSARIO.md#facility" target="_blank">facility</a> + <a href="../../GLOSARIO.md#severity" target="_blank">severity</a>. RAW = cuándo+dónde+quién+qué. PATRONES = fallos, hora/IP/cuenta. CUENTAS = persistencia. INVESTIGACIÓN = timeline + veredicto.

---

**📘 Carrera de Analista SOC**

**Semana 5 — Gestión de Logs**

**Evaluación — Módulo 36: Persistencia e investigación**

**Pregunta 1**

4720 + 4728 a Administradores fuera de horario sugiere:

**A)** Mantenimiento normal.\
**B)** Posible persistencia con cuenta privilegiada.\
**C)** Error <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.\
**D)** Spam.

**Pregunta 2**

En Linux, creación de usuario se rastrea con:

**A)** `grep -E "useradd|usermod" /var/log/auth.log` + `/etc/passwd`.\
**B)** `ping`.\
**C)** `nslookup`.\
**D)** `ipconfig`.

**Pregunta 3**

7045 con ruta `C:\Temp\upd.exe` indica:

**A)** Servicio legítimo.\
**B)** Persistencia sospechosa.\
**C)** Impresora.\
**D)** <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**Pregunta 4**

En Linux, persistencia por tarea se revisa en:

**A)** `crontab -l`, `/etc/cron*`, `systemctl list-timers`.\
**B)** `/etc/hosts`.\
**C)** Historial <a href="../../GLOSARIO.md#bash" target="_blank">bash</a> solo.\
**D)** `/tmp` solo.

**Pregunta 5**

Ordenar por hora para contar la historia se llama:

**A)** Cifrado.\
**B)** Línea de tiempo.\
**C)** Spoofing.\
**D)** Enumeración.

**Pregunta 6**

Un buen informe incluye:

**A)** Solo IP.\
**B)** Resumen, timeline, evidencia y acciones.\
**C)** Contraseñas.\
**D)** Dibujo.

**Pregunta 7**

`powershell.exe` padre `outlook.exe` con `-enc` sugiere:

**A)** Update.\
**B)** Ejecución desde correo, decodificar y aislar.\
**C)** Error red.\
**D)** Mantenimiento.

**Pregunta 8**

Tras 4625→4624→4688→red, lo profesional es:

**A)** Decir "malware confirmado".\
**B)** Correlacionar y pedir padre, Command Line, destino y persistencia.\
**C)** Reiniciar.\
**D)** Ignorar.

**Pregunta 9 — Caso SOC**

PC-RRHH-07: 4625×10 → 4624 → 4688 powershell padre winword → IP externa. Veredicto:

**A)** Normal.\
**B)** Doc malicioso con macro → C2; aislar y decodificar.\
**C)** Impresora.\
**D)** Update.

**Pregunta 10**

Saber leer en raw sirve para:

**A)** Nada.\
**B)** Entender lo que luego automatiza el SIEM/Sysmon.\
**C)** Crear virus.\
**D)** Apagar equipos.

**⛔ DETENTE AQUÍ.**

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**.
2. **A**.
3. **B**.
4. **A**.
5. **B**.
6. **B**.
7. **B**.
8. **B**.
9. **B**.
10. **B**.

**🏆 TABLA DE RESULTADOS — Semana 5**

| Resultado | Evaluación |
| :--- | :--- |
| **10/10** | 🟢 Excelente — listo para Splunk. |
| **8–9/10** | 🟢 Muy buen nivel. |
| **6–7/10** | 🟡 Buen progreso. |
| **4–5/10** | 🟠 Repasar patrones. |
| **0–3/10** | 🔴 Volver a estudiar. |

**📍 Progreso — Semana 5 (COMPLETADA)**

-   ✅ **Módulo 30 — ¿Qué es un log?**
-   ✅ **Módulo 31 — Tipos de logs**
-   ✅ **Módulo 32 — Event Log de Windows**
-   ✅ **Módulo 33 — Syslog en Linux**
-   ✅ **Módulo 34 — Anatomía raw**
-   ✅ **Módulo 35 — Fuerza bruta y logins**
-   ✅ **Módulo 36 — Usuarios admin, persistencia e investigación**

**🎯 Meta de la Semana 5**

Ante `auth.log` o Security con fallos + éxito + proceso + red, podés decir:

**"Esto parece fuerza bruta seguida de acceso y ejecución. Debo verificar usuario, IP origen, <a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a>, padre y Command Line, destino de red y persistencia, y redactar timeline con veredicto."**

Siguiente parada: Semana 6 — Splunk.
