**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 31: Tipos de logs (Seguridad, Aplicación, Sistema, Auditoría)**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Clasificación + Dónde buscar

Ya sabés qué es un <a href="../../GLOSARIO.md#log" target="_blank">log</a>. Ahora aprendé a clasificarlo. Cuando te digan "revisá los logs", tenés que saber **qué tipo de log buscar y qué pregunta responde**.

**🎯 Objetivos del módulo**

-   Distinguir logs de Seguridad, Aplicación, Sistema y <a href="../../GLOSARIO.md#auditoria" target="_blank">Auditoría</a>.
-   Ubicar cada tipo en Windows y en Linux.
-   Saber qué buscar en cada uno durante una investigación.
-   Evitar el error L1: buscar autenticación en el log equivocado.

---

**1. Los 4 tipos que te van a pedir**

SEGURIDAD

= quién entró, quién falló, qué permiso usó.

SISTEMA

= qué le pasó al equipo (servicios, drivers, arranque).

APLICACIÓN

= qué le pasó a un programa (web, base, antivirus).

AUDITORÍA

= registro inmutable para probar qué pasó y quién lo hizo.

**2. Analogía del hospital**

Imaginá un hospital:

Seguridad → registro de visitas en puerta.

Sistema → estado del edificio (luz, ascensores).

Aplicación → historia clínica de cada paciente.

Auditoría → libro firmado que nadie puede arrancar hojas.

En un incidente necesitás los cuatro, pero cada uno responde algo distinto.

**3. Tabla maestra**

| **Tipo** | **Pregunta que responde** | **Windows** | **Linux** |
| :--- | :--- | :--- | :--- |
| Seguridad | ¿Quién se autenticó? | Security (<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>/<a href="../../GLOSARIO.md#4625" target="_blank">4625</a>/4720) | `/var/log/auth.log`, `/var/log/secure` |
| Sistema | ¿El equipo está sano? | System (<a href="../../GLOSARIO.md#7045" target="_blank">7045</a>, errores) | `/var/log/syslog`, `/var/log/messages`, `journalctl` |
| Aplicación | ¿Qué hizo el programa? | Application, IIS, Defender | `/var/log/apache2/`, `/var/log/nginx/`, `/var/log/dpkg.log` |
| Auditoría | ¿Puedo probarlo? | Security + <a href="../../GLOSARIO.md#1102" target="_blank">1102</a>, <a href="../../GLOSARIO.md#gpo" target="_blank">GPO</a> de auditoría | `auditd`, `sudo` en auth.log |

**4. Seguridad en detalle**

Windows:

`eventvwr.msc` → Registros de Windows → Seguridad.

Event <a href="../../GLOSARIO.md#ids" target="_blank">IDs</a>: 4624 éxito, 4625 fallo, 4720 cuenta creada, <a href="../../GLOSARIO.md#4688" target="_blank">4688</a> proceso.

Linux:

`grep "Failed password" /var/log/auth.log`

`grep "Accepted password" /var/log/auth.log`

`grep "sudo" /var/log/auth.log | grep COMMAND`

Si buscás logins, **empezá siempre acá**.

**5. Sistema en detalle**

Windows → System: servicios que no arrancan, 7045 (servicio instalado), pantallazos, drivers.

Linux:

`grep -i "error" /var/log/syslog`

`journalctl -p err -b`

`grep -i "shutdown\|reboot" /var/log/syslog`

Te dice si el equipo se reinició solo, si un servicio crítico cayó o si hubo manipulación para persistencia.

**6. Aplicación en detalle**

Windows → Application: errores de programas, IIS, <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a> Operational.

Linux:

`/var/log/apache2/access.log` → cada petición web.

`grep "404" /var/log/apache2/access.log` → posible escaneo.

`/var/log/dpkg.log` → `grep "install"` muestra herramientas instaladas sin permiso.

Un ataque web deja rastro acá aunque no deje rastro en auth.

**7. Auditoría en detalle**

Auditoría no es un archivo distinto. Es una **propiedad**: el log debe ser completo, con <a href="../../GLOSARIO.md#timestamp" target="_blank">timestamp</a> confiable, y difícil de borrar.

Windows: si no activás `Audit Logon Events` y `Audit Process Creation`, el 4688 no aparece. Auditar es decidir qué guardar.

Linux: `auditd` registra syscalls, acceso a `/etc/shadow`, ejecución de binarios. `sudo` queda en auth.log con usuario + comando.

Y el 1102 (log borrado) es evento de auditoría por excelencia: el hueco también es evidencia.

**8. Error típico L1**

Buscar <a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">fuerza bruta</a> <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> en `/var/log/syslog` y decir "no hay ataque".

El ataque estaba en `/var/log/auth.log`.

O buscar creación de usuarios en Application cuando está en Security (4720) o en auth.log (`useradd`).

Regla:

> **Autenticación → Seguridad. Salud del equipo → Sistema. Ataque web → Aplicación. Prueba forense → Auditoría.**

**9. Mini-casos para ubicarte**

Caso A: 40 fallos para `admin` → Seguridad.

Caso B: servicio nuevo `ActualizadorX` a las 03:00 → Sistema (7045) + Seguridad (quién lo creó).

Caso C: miles de 404 a `/admin.php` → Aplicación (access.log).

Caso D: hueco de 2 horas en logs + 1102 → Auditoría (encubrimiento).

**📚 Resumen**

SEGURIDAD

= quién. SISTEMA = cómo está el equipo. APLICACIÓN = qué hizo el programa. AUDITORÍA = puedo probarlo.

WINDOWS

= Security / System / Application. LINUX = auth.log-secure / <a href="../../GLOSARIO.md#syslog" target="_blank">syslog</a>-messages / apache-nginx-dpkg + <a href="../../GLOSARIO.md#journalctl" target="_blank">journalctl</a>.

**🧩 Conceptos clave para memorizar**

| **Concepto** | **Debes recordar** |
| :--- | :--- |
| Seguridad | Autenticación y permisos. |
| Sistema | Servicios, arranque, errores. |
| Aplicación | Peticiones y errores de programas. |
| Auditoría | Completitud + timestamp + no repudio. |
| auth.log / secure | Según Debian o Red Hat. |
| 4720 / useradd | Creación de cuenta = persistencia posible. |

**🎓 Consejo como tu instructor de SOC**

Ante cada alerta preguntate primero: **¿qué tipo de log necesito?** Eso te ahorra horas. El buen analista no hace `grep` en todos lados: va directo al log que responde su pregunta.

---

**📘 Carrera de Analista SOC**

**Semana 5 — Gestión de Logs**

**Evaluación — Módulo 31: Tipos de logs**

**Pregunta 1**

Log de Seguridad responde a:

**A)** ¿Qué programa falló?\
**B)** ¿Quién se autenticó y con qué resultado?\
**C)** ¿Cuánto disco hay?\
**D)** ¿Qué temperatura tiene la CPU?

**Pregunta 2**

En Windows, los logins 4624/4625 están en:

**A)** Application.\
**B)** System.\
**C)** Security.\
**D)** Setup.

**Pregunta 3**

En Ubuntu, los intentos SSH están en:

**A)** `/var/log/auth.log`.\
**B)** `/var/log/kern.log`.\
**C)** `/var/log/dpkg.log`.\
**D)** `/tmp`.

**Pregunta 4**

En Red Hat, el equivalente a auth.log es:

**A)** `/var/log/secure`.\
**B)** `/var/log/syslog`.\
**C)** `/var/log/apache2/access.log`.\
**D)** `/etc/passwd`.

**Pregunta 5**

Un 7045 (servicio instalado) lo buscás primero en:

**A)** Log de Sistema.\
**B)** Log de Aplicación.\
**C)** Historial del navegador.\
**D)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**Pregunta 6**

Miles de 404 a `/wp-admin` se investigan en:

**A)** Log de Aplicación / access.log.\
**B)** Log de Seguridad.\
**C)** Tabla <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a>.\
**D)** <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**Pregunta 7**

¿Qué es auditoría en este contexto?

**A)** Un antivirus.\
**B)** La propiedad de que el log sea completo, con timestamp confiable y difícil de borrar.\
**C)** Un firewall.\
**D)** Un backup.

**Pregunta 8**

Si el 4688 no aparece, probablemente:

**A)** No hay disco.\
**B)** No está activado Audit Process Creation.\
**C)** No hay red.\
**D)** Es Linux.

**Pregunta 9 — Caso SOC**

Buscás fuerza bruta en syslog y no ves nada, pero en auth.log hay 2000 `Failed password`. Conclusión:

**A)** No hay ataque.\
**B)** Buscaste en el log equivocado; el ataque sí existe.\
**C)** Es phishing.\
**D)** Es malware confirmado.

**Pregunta 10**

Hueco de 2 horas + Event 1102 sugiere:

**A)** Actualización normal.\
**B)** Posible borrado intencional / encubrimiento.\
**C)** Error de impresora.\
**D)** DNS caído.

**⛔ DETENTE AQUÍ** e intentá resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: seguridad = identidad.
2. **C — Security**.
3. **A — auth.log**.
4. **A — secure**.
5. **A — Sistema**.
6. **A — Aplicación/access.log**.
7. **B**: completitud + timestamp + no repudio.
8. **B**: hay que habilitar la auditoría.
9. **B**: cada pregunta tiene su log.
10. **B**: el hueco también es evidencia.

**🏆 Resultado**

| **Correctas** | **Nivel** |
| :--- | :--- |
| **10/10** | ⭐ Excelente. |
| **8–9/10** | 🟢 Muy buen nivel. |
| **6–7/10** | 🟡 Buen progreso. |
| **4–5/10** | 🟠 Repasar tipos. |
| **0–3/10** | 🔴 Volver a estudiar. |

**📍 Progreso — Semana 5**

-   ✅ **Módulo 30 — ¿Qué es un log?**
-   ✅ **Módulo 31 — Tipos de logs**
-   ⚪ Módulo 32 — Event Log de Windows (vista SOC)
-   ⚪ Módulo 33 — Syslog en Linux
-   ⚪ Módulo 34 — Anatomía de un log raw
-   ⚪ Módulo 35 — Fuerza bruta y logins inusuales
-   ⚪ Módulo 36 — Usuarios admin, persistencia e investigación
