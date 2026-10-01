**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 33: Syslog en Linux (facilities, severities, <a href="../../GLOSARIO.md#rsyslog" target="_blank">rsyslog</a>, <a href="../../GLOSARIO.md#journalctl" target="_blank">journalctl</a>)**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Lectura raw en Ubuntu + Centralización

Si Windows tiene Event <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a>, Linux tiene <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a>. Es el protocolo que lleva 40 años guardando lo que pasa. Tenés que leerlo sin miedo.

**🎯 Objetivos del módulo**

-   Entender formato Syslog: <a href="../../GLOSARIO.md#facility" target="_blank">facility</a> + <a href="../../GLOSARIO.md#severity" target="_blank">severity</a> + mensaje.
-   Ubicar `auth.log`, `syslog`, `kern.log`, `secure`.
-   Usar `rsyslog`, `journalctl` y `logger` en tu VM Ubuntu.
-   Generar tus propios eventos para practicar.

---

**1. ¿Qué es Syslog?**

Syslog es un estándar para escribir y enviar logs.

Cada mensaje dice:

quién lo manda (facility)

↓

qué tan grave es (severity)

↓

qué pasó (mensaje)

Puerto clásico: <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 514. Hoy también <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 514 + <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> para no perder ni exponer logs.

**2. Analogía del correo interno**

Facility = departamento que envía (auth, kern, mail, cron).

Severity = prioridad del sobre (emergencia, error, aviso, info, debug).

El SOC es la mesa de entradas que clasifica por prioridad.

**3. Facilities que tenés que reconocer**

`auth / authpriv` → autenticación (tu foco SOC).

`kern` → <a href="../../GLOSARIO.md#kernel" target="_blank">kernel</a>.

`daemon` → servicios en segundo plano.

`cron` → tareas programadas.

`mail`, `user`, `local0-7` → aplicaciones y custom.

**4. Severities de memoria**

| **Nº** | **Nombre** | **Idea SOC** |
| :--- | :--- | :--- |
| 0 | emerg | Sistema inutilizable. |
| 1 | alert | Actuar ya. |
| 2 | crit | Crítico. |
| 3 | err | Error. |
| 4 | warning | Aviso. |
| 5 | notice | Normal pero relevante. |
| 6 | info | Informativo. |
| 7 | debug | Solo desarrollo. |

Un `authpriv err Failed password` te interesa más que un `daemon info`.

**5. Dónde vive en tu VM**

Debian/Ubuntu:

`/var/log/auth.log` → <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>, <a href="../../GLOSARIO.md#sudo" target="_blank">sudo</a>, logins.

`/var/log/syslog` → sistema general.

`/var/log/kern.log` → kernel.

`/var/log/dpkg.log` → paquetes.

Red Hat:

`/var/log/secure` = auth.<a href="../../GLOSARIO.md#log" target="_blank">log</a>.

`/var/log/messages` = syslog.

Comandos base:

`ls -lh /var/log/auth.log /var/log/syslog`

`cat /var/log/auth.log | head -20`

`sudo grep "Failed password" /var/log/auth.log | tail -20`

**6. rsyslog: el que escribe y reenvía**

`rsyslog` es el servicio que recibe mensajes y los escribe o reenvía al <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

Config: `/etc/rsyslog.conf` + `/etc/rsyslog.d/`.

Verificá:

`systemctl status rsyslog`

`cat /etc/rsyslog.conf | grep -v "^#" | grep -v "^$"`

Idea clave: si el atacante para rsyslog, dejan de llegar logs al SIEM. Por eso se monitorea que el flujo no se corte.

**7. journalctl: el visor moderno**

`systemd-journald` guarda en binario. Lo leés con `journalctl`:

`journalctl -p err -b` → errores de este arranque.

`journalctl -u ssh --since "1 hour ago"` → solo SSH última hora.

`journalctl -f` → en vivo (como `tail -f`).

`journalctl --since "2026-09-30 02:00" --until "2026-09-30 03:00"` → ventana de incidente.

**8. Laboratorio: generá tus propios logs**

En tu Ubuntu:

1.  `logger -p authpriv.info "PRUEBA SOC sem5 usuario juan login test"` → buscá en syslog.
2.  Fallá tu SSH 3 veces a propósito → `grep "Failed password" /var/log/auth.log`.
3.  `sudo -i` y salí → `grep "sudo" /var/log/auth.log | tail`.
4.  `sudo useradd auditor5 && sudo passwd auditor5` → `grep "useradd" /var/log/auth.log`.
5.  Borrá `auditor5`: `sudo userdel -r auditor5` → documentá qué quedó.
6.  `journalctl -u ssh --since "30 min ago" > ~/evidencia_ssh.txt` → tu primera evidencia Linux.

**9. Caso SOC**

`auth.log`:

`Failed password for invalid user admin from 203.0.113.5` ×40

↓

`Accepted password for admin from 203.0.113.5`

↓

`session opened for user admin`

↓

`COMMAND=/bin/bash` vía sudo a las 03:12.

Eso es <a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">fuerza bruta</a> + éxito + escalada. Mismo patrón que <a href="../../GLOSARIO.md#4625" target="_blank">4625</a>→<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>→<a href="../../GLOSARIO.md#4688" target="_blank">4688</a> en Windows, pero en idioma Syslog.

**📚 Resumen**

SYSLOG

= facility + severity + mensaje. AUTH = logins. RSYSLOG = escribe y reenvía. JOURNALCTL = filtra por servicio y tiempo. LOGGER = genera pruebas.

**🧩 Conceptos clave**

| **Concepto** | **Debes recordar** |
| :--- | :--- |
| facility | Quién manda (auth, kern, cron). |
| severity | Gravedad 0-7. |
| auth.log / secure | Según distro. |
| rsyslog | UDP/TCP 514, centraliza. |
| journalctl | `-u`, `-p`, `--since`, `-f`. |
| logger | Genera eventos de prueba. |

**🎓 Consejo como tu instructor de SOC**

Practicá `journalctl -u ssh --since "1 hour ago"` todos los días. Cuando llegues a Splunk vas a hacer lo mismo con `index=linux sourcetype=auth`. El campo cambia, la pregunta es la misma: **¿quién intentó entrar y lo logró?**

---

**Evaluación — Módulo 33**

**Pregunta 1**

Syslog transporta por defecto en:

**A)** UDP 514 (y TCP 514 moderno).\
**B)** TCP 443.\
**C)** UDP 53.\
**D)** TCP 22.

**Pregunta 2**

Facility indica:

**A)** Gravedad.\
**B)** Quién genera el mensaje (auth, kern, cron).\
**C)** La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.\
**D)** El hash.

**Pregunta 3**

Severity `err` es:

**A)** Debug.\
**B)** Error.\
**C)** Info.\
**D)** Emergencia.

**Pregunta 4**

En Ubuntu, SSH fallido se busca en:

**A)** `/var/log/auth.log`.\
**B)** `/var/log/kern.log`.\
**C)** `/var/log/dpkg.log`.\
**D)** `/etc/hosts`.

**Pregunta 5**

`journalctl -u ssh --since "1 hour ago"` muestra:

**A)** Todo el disco.\
**B)** Solo SSH de la última hora.\
**C)** Solo kernel.\
**D)** Usuarios creados.

**Pregunta 6**

`logger -p authpriv.info "test"` sirve para:

**A)** Borrar logs.\
**B)** Generar un evento de prueba.\
**C)** Crear usuarios.\
**D)** Escanear puertos.

**Pregunta 7**

Si rsyslog se detiene:

**A)** Nada pasa.\
**B)** Se corta el flujo hacia archivos y SIEM: punto ciego.\
**C)** Mejora la seguridad.\
**D)** Cifra logs.

**Pregunta 8**

`Failed password` + luego `Accepted password` misma IP es:

**A)** Normal.\
**B)** Posible fuerza bruta exitosa, compromiso probable.\
**C)** Error <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.\
**D)** Phishing.

**Pregunta 9 — Caso SOC**

40 fallos + 1 éxito `admin` 03:12 + `COMMAND=/bin/bash` vía sudo. Prioridad:

**A)** Baja.\
**B)** Alta: acceso + horario anómalo + escalada; aislar y rotar credencial.\
**C)** Ignorar.\
**D)** Reinstalar impresora.

**Pregunta 10**

Equivalente Red Hat de `/var/log/auth.log`:

**A)** `/var/log/secure`.\
**B)** `/var/log/syslog`.\
**C)** `/var/log/kern.log`.\
**D)** `/var/log/nginx/access.log`.

**⛔ DETENTE AQUÍ.**

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **A — 514**.
2. **B — facility**.
3. **B — err**.
4. **A**.
5. **B**.
6. **B — prueba**.
7. **B — punto ciego**.
8. **B**.
9. **B**.
10. **A — secure**.

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
-   ✅ **Módulo 33 — Syslog en Linux**
-   ⚪ Módulo 34 — Anatomía de un log raw
-   ⚪ Módulo 35 — Fuerza bruta y logins inusuales
-   ⚪ Módulo 36 — Usuarios admin, persistencia e investigación
