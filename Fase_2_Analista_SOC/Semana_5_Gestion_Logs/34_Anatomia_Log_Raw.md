**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 34: Anatomía de un <a href="../../GLOSARIO.md#log" target="_blank">log</a> raw (timestamp, host, proceso, mensaje)**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Parseo manual + <a href="../../GLOSARIO.md#normalizacion" target="_blank">Normalización</a>

La meta de la semana es **interpretar logs nativos en raw sin herramientas**. Este módulo te enseña a desarmar cualquier línea aunque nunca la hayas visto.

**🎯 Objetivos del módulo**

-   Desarmar una línea en timestamp + hostname + proceso + <a href="../../GLOSARIO.md#pid" target="_blank">PID</a> + mensaje.
-   Entender <a href="../../GLOSARIO.md#timestamp" target="_blank">timestamp</a>, <a href="../../GLOSARIO.md#retencion" target="_blank">retención</a> y <a href="../../GLOSARIO.md#log-rotation" target="_blank">log rotation</a>.
-   Comprender normalización: por qué el <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> convierte todo a campos comunes.
-   Detectar logs incompletos o manipulados.

---

**1. La receta de toda línea**

Casi todo <a href="../../GLOSARIO.md#raw-log" target="_blank">raw log</a> tiene:

CUÁNDO

↓

DÓNDE

↓

QUIÉN LO DICE

↓

QUÉ PASÓ

Ejemplo Linux:

`May 14 09:12:33 server sshd[1245]: Failed password for invalid user admin from 203.0.113.5 port 52270 ssh2`

-   `May 14 09:12:33` → timestamp.
-   `server` → hostname.
-   `sshd[1245]` → proceso + PID.
-   Resto → mensaje con usuario, <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, puerto.

Ejemplo Windows XML (mismo idioma):

`TimeCreated=02:13:27, Computer=PC-VENTAS-05, EventID=4625, TargetUserName=admin, IpAddress=10.10.20.15`

**2. Timestamp: tu columna vertebral**

Sin hora confiable no hay línea de tiempo.

Preguntá siempre:

¿El equipo usa NTP? ¿Zona horaria? ¿El timestamp es local o UTC?

Un desfase de 1 hora rompe la <a href="../../GLOSARIO.md#correlacion" target="_blank">correlación</a> <a href="../../GLOSARIO.md#4625" target="_blank">4625</a>→<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>→<a href="../../GLOSARIO.md#4688" target="_blank">4688</a>.

En Linux: `timedatectl status`. En Windows: `w32tm /query /status`.

**3. Hostname + IP: dónde pasó**

Hostname te dice qué equipo. IP origen te dice desde dónde.

`Failed` sin IP = historia incompleta.

`4624` sin <a href="../../GLOSARIO.md#source-network-address" target="_blank">Source Network Address</a> = no sabés si fue local o RDP externo.

Siempre anotá ambos.

**4. Proceso + PID + padre**

`sshd[1245]` no es igual que `sshd[1299]`: son conexiones distintas.

En Windows, 4688 agrega `ParentProcess`: `winword.exe → powershell.exe` cambia todo.

Regla: **nombre solo no alcanza; necesitás ruta + padre + <a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a>.**

**5. El mensaje: el verbo**

`Failed password` vs `Accepted password`.

`useradd` vs `userdel`.

`Service installed` vs `Service stopped`.

Subrayá el verbo primero, después los detalles.

**6. Normalización: lo que hará el SIEM por vos**

El SIEM convierte:

`May 14 09:12:33 server sshd: Failed... from 203.0.113.5`

y

`EventID=4625 IpAddress=10.10.20.15`

en campos comunes:

`_time, src_ip, user, action=failed_login, app=ssh/windows`

Por eso hoy parseás a mano: para entender qué campo buscar mañana en SPL.

**7. Retención y log rotation**

Los logs no son infinitos.

Linux rota: `auth.log → auth.log.1 → auth.log.2.gz`. Config: `/etc/logrotate.conf`.

Windows sobrescribe cuando el log se llena si así está configurado.

Si investigás algo de hace 60 días y la <a href="../../GLOSARIO.md#retencion" target="_blank">retención</a> es 30, ya no está en local: pedilo al SIEM.

Siempre preguntá: **¿desde cuándo tengo cobertura?**

**8. Laboratorio raw**

1.  `grep "Failed password" /var/log/auth.log | head -5` → desarmá cada campo en papel.
2.  `grep "Accepted" /var/log/auth.log | head -5` → compará verbo y puerto.
3.  `ls -lh /var/log/auth.log*` → identificá rotados y comprimidos. `zgrep "Failed" /var/log/auth.log.2.gz | head`.
4.  En Windows, abrí un 4624 y copiá a papel: hora, usuario, LogonType, IP. Sin mirar la pestaña General.
5.  Escribí en una línea: `cuándo + dónde + quién + qué`. Esa es tu normalización manual.

**📚 Resumen**

RAW

= cuándo + dónde + quién lo dice + qué pasó. TIMESTAMP = orden. HOST+IP = lugar. PROCESO+PADRE = actor. NORMALIZACIÓN = traducir a campos comunes. ROTACIÓN = los logs viejos se comprimen o pierden.

**🧩 Conceptos clave**

| **Concepto** | **Debes recordar** |
| :--- | :--- |
| timestamp | Sin hora no hay timeline. |
| hostname | Qué equipo. |
| PID / PPID | Qué instancia y quién la lanzó. |
| normalización | Campos comunes para correlacionar. |
| log rotation | `.1`, `.gz`, retención limitada. |

**🎓 Consejo como tu instructor de SOC**

Cuando veas una línea rara, tapá todo menos el verbo y el timestamp. Si con eso no podés decir qué pasó y cuándo, te falta contexto. Pedí el campo que falta antes de concluir.

---

**Evaluación — Módulo 34**

**Pregunta 1**

En `May 14 09:12:33 server sshd[1245]: Failed...`, el timestamp es:

**A)** `server`.\
**B)** `May 14 09:12:33`.\
**C)** `sshd`.\
**D)** `Failed`.

**Pregunta 2**

`sshd[1245]` indica:

**A)** IP.\
**B)** Proceso + PID.\
**C)** Usuario.\
**D)** Puerto.

**Pregunta 3**

Sin NTP confiable:

**A)** No pasa nada.\
**B)** La línea de tiempo y correlación se rompen.\
**C)** Mejora la seguridad.\
**D)** Se cifra el log.

**Pregunta 4**

Normalización es:

**A)** Borrar logs.\
**B)** Convertir formatos distintos a campos comunes (`src_ip`, `user`, `_time`).\
**C)** Comprimir.\
**D)** Crear usuarios.

**Pregunta 5**

`auth.log.2.gz` es:

**A)** Un virus.\
**B)** Un log rotado y comprimido.\
**C)** Un backup de <a href="../../GLOSARIO.md#sam" target="_blank">SAM</a>.\
**D)** Un ejecutable.

**Pregunta 6**

Para buscar en rotados usás:

**A)** `zgrep`.\
**B)** `ping`.\
**C)** `ipconfig`.\
**D)** `tasklist`.

**Pregunta 7**

En un 4624, si falta Source Network Address:

**A)** Igual sabés si fue RDP externo.\
**B)** No podés distinguir local vs remoto.\
**C)** Es phishing.\
**D)** Es malware.

**Pregunta 8**

`Failed` vs `Accepted` es diferencia de:

**A)** Verbo / resultado.\
**B)** Hora.\
**C)** Hostname.\
**D)** PID.

**Pregunta 9 — Caso SOC**

Línea sin año ni zona, equipo con hora atrasada 1 h. Lo primero:

**A)** Concluir ataque.\
**B)** Validar timestamp/NTP antes de correlacionar.\
**C)** Borrar.\
**D)** Reiniciar.

**Pregunta 10**

Retención de 30 días implica:

**A)** Todo lo viejo sigue en local.\
**B)** Lo de hace 60 días solo estará en SIEM si se centralizó.\
**C)** No hay logs.\
**D)** Es ilimitada.

**⛔ DETENTE AQUÍ.**

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**.
2. **B**.
3. **B**: hora rota = timeline roto.
4. **B**.
5. **B — rotation**.
6. **A — zgrep**.
7. **B**.
8. **A — verbo**.
9. **B — validar hora**.
10. **B**.

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
-   ✅ **Módulo 33 — <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a> en Linux**
-   ✅ **Módulo 34 — Anatomía raw**
-   ⚪ Módulo 35 — <a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">Fuerza bruta</a> y logins inusuales
-   ⚪ Módulo 36 — Usuarios admin, persistencia e investigación
