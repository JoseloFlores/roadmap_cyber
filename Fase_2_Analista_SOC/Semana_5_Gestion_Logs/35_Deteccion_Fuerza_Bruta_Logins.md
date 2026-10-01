**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 35: Detección de patrones — fuerza bruta y logins inusuales**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Detección manual + <a href="../../GLOSARIO.md#grep" target="_blank">grep</a> + Criterio SOC

Este es el laboratorio corazón de la semana. La Hoja de Ruta pide: **detectar inicios inusuales, fallas repetitivas y distinguir fuerza bruta de ruido**. Lo vas a hacer sin <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>, como pide la meta.

**🎯 Objetivos del módulo**

-   Contar fallos y ubicar la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> más atacante.
-   Distinguir <a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">fuerza bruta</a> vs <a href="../../GLOSARIO.md#password-spraying" target="_blank">password spraying</a> vs error de usuario.
-   Detectar logins inusuales por hora, IP y cuenta.
-   Decidir cuándo es <a href="../../GLOSARIO.md#falso-positivo" target="_blank">falso positivo</a> y cuándo escalar.

---

**1. El patrón que buscás**

Fuerza bruta clásica:

`Failed` × N misma cuenta misma IP

↓

`Accepted` misma IP (a veces)

Password spraying:

`Failed` 1 vez × N cuentas misma IP.

Error de usuario:

`Failed` × 2-3 + `Accepted` mismo usuario IP interna horario laboral.

**2. Comandos que tenés que dominar**

Total fallidos:

`grep -c "Failed password" /var/log/auth.log`

Total exitosos:

`grep -c "Accepted password" /var/log/auth.log`

Top <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a> atacantes:

`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -20`

¿Esa IP logró entrar?

`grep "203.0.113.5" /var/log/auth.log | grep "Accepted"`

En vivo:

`tail -f /var/log/auth.log`

En Windows (filtro manual):

Seguridad → `4625` contar por IP origen → ¿hubo `4624` posterior? → ¿<a href="../../GLOSARIO.md#logon-type" target="_blank">Logon Type</a> 3 o 10?

**3. Paso a paso en tu Ubuntu**

1.  `grep "Failed password" /var/log/auth.log | tail -20` → leé usuarios e IPs.
2.  Contá: `grep -c`. Si son cientos en 1 h, es ataque o escaneo.
3.  Sacá el top 10 de IPs. La primera es tu sospechosa principal.
4.  `grep "IP_SOSPECHOSA" /var/log/auth.log | grep -E "Failed|Accepted|session opened"` → timeline de esa IP.
5.  `grep "Failed password" /var/log/auth.log | grep "invalid user"` → ¿prueba usuarios inexistentes? Típico de diccionario.
6.  Guardá: `grep "IP_SOSPECHOSA" /var/log/auth.log > ~/evidencia_fuerza_bruta.txt`.

**4. Logins inusuales: las 3 preguntas**

¿HORA RARA?

`admin` a las 03:42 cuando trabaja 08-17 = anómalo.

¿IP RARA?

`juan` desde `192.168.1.25` siempre, hoy desde externa = investigar.

¿CUENTA RARA?

`Administrator` en PC-VENTAS cuando nadie lo usa, o `SYSTEM` haciendo RDP = sospechoso.

Anómalo ≠ malicioso. Pero anómalo + fallos previos + proceso raro = escalar.

**5. Falsos positivos que tenés que evitar**

Usuario que vuelve de vacaciones y falla 3 veces = ruido.

Servicio con contraseña vieja que reintenta solo = muchos <a href="../../GLOSARIO.md#4625" target="_blank">4625</a> legítimos.

Admin que automatizó script con `Accepted` cada 5 min = baseline, no ataque.

Siempre contrastá con <a href="../../GLOSARIO.md#baseline" target="_blank">baseline</a>: quién, horario, IP habitual.

**6. Caso A: fuerza bruta sin éxito**

`12.450 Failed` en 24 h, IP `203.0.113.99` con 9800, cero `Accepted` desde ella.

Veredicto: ataque sin éxito.

Acciones: bloquear IP en firewall, fail2ban, reforzar password, monitorear si vuelve con otra IP.

**7. Caso B: compromiso probable**

`Failed ×40` → `Accepted admin desde misma IP` → `sudo COMMAND` de noche.

Veredicto: compromiso probable.

Acciones L1: no apagar sin orden, aislar de red si el playbook lo permite, rotar credencial, cazar misma IP en otros equipos, escalar a L2 con timeline.

**8. Caso C Windows**

`4625 ×20 admin` 23:10-23:12 → `4624 Type 10 IP externa` 23:12 → `4688 powershell.exe` 23:13 → conexión externa.

No digas "es malware". Decí: "fuerza bruta seguida de RDP exitoso y ejecución; necesito padre de <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a>, <a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a> y destino de red".

**📚 Resumen**

FALLOS

= contar + agrupar por IP. ÉXITO POSTERIOR = compromiso probable. HORA/IP/CUENTA = anomalía. BASELINE = evita falsos positivos.

**🧩 Conceptos clave**

| **Concepto** | **Debes recordar** |
| :--- | :--- |
| fuerza bruta | Muchos passwords, una cuenta. |
| password spraying | Un password, muchas cuentas. |
| `uniq -c` | Agrupa y cuenta por IP. |
| Accepted tras Failed | Señal crítica. |
| falso positivo | Anomalía con explicación legítima. |
| <a href="../../GLOSARIO.md#falso-negativo" target="_blank">falso negativo</a> | Ataque que no marcaste. |

**🎓 Consejo como tu instructor de SOC**

Memorizá el pipeline top-IP. Te va a salvar en entrevistas y en guardias. Y nunca declares "ataque confirmado" solo por volumen: mostrá el `Accepted` o la ejecución posterior.

---

**Evaluación — Módulo 35**

**Pregunta 1**

Para contar fallidos <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> usás:

**A)** `grep -c "Failed password" /var/log/auth.log`.\
**B)** `ls /var/log`.\
**C)** `tail -f` solo.\
**D)** `ping`.

**Pregunta 2**

Top IP atacante:

**A)** `grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`.\
**B)** `cat /etc/passwd`.\
**C)** `ipconfig`.\
**D)** `tasklist`.

**Pregunta 3**

Fuerza bruta vs spraying:

**A)** Iguales.\
**B)** Bruta = muchas passwords una cuenta; spraying = una password muchas cuentas.\
**C)** Spraying es impresora.\
**D)** Bruta es <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**Pregunta 4**

3 fallos de Juan 08:00 IP interna + éxito = probablemente:

**A)** <a href="../../GLOSARIO.md#apt" target="_blank">APT</a>.\
**B)** Error humano / ruido.\
**C)** Ransomware.\
**D)** <a href="../../GLOSARIO.md#golden-ticket" target="_blank">Golden Ticket</a>.

**Pregunta 5**

Para saber si la IP atacante entró:

**A)** `grep "IP" /var/log/auth.log | grep "Accepted"`.\
**B)** `grep "install" /var/log/dpkg.log`.\
**C)** `ls -la`.\
**D)** `whoami`.

**Pregunta 6**

Login `admin` 03:42 IP externa cuando trabaja 08-17 es:

**A)** Normal.\
**B)** Inusual por hora + IP + cuenta; investigar.\
**C)** Error DNS.\
**D)** Phishing confirmado.

**Pregunta 7**

Servicio con password vieja que genera 4625 cada minuto es:

**A)** Ataque seguro.\
**B)** Posible falso positivo / baseline roto.\
**C)** <a href="../../GLOSARIO.md#kerberoasting" target="_blank">Kerberoasting</a>.\
**D)** <a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a>.

**Pregunta 8**

`Failed ×500` sin ningún `Accepted`:

**A)** Compromiso confirmado.\
**B)** Ataque sin éxito (por ahora); bloquear y monitorear.\
**C)** Nada.\
**D)** Malware.

**Pregunta 9 — Caso SOC**

40 fallos → 1 éxito misma IP + <a href="../../GLOSARIO.md#sudo" target="_blank">sudo</a> nocturno. Lo correcto:

**A)** Ignorar.\
**B)** Escalar como compromiso probable con timeline y pedir rotación + caza lateral.\
**C)** Borrar logs.\
**D)** Cambiar <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a>.

**Pregunta 10**

En Windows, tras muchos 4625 lo primero es:

**A)** Ver si hubo <a href="../../GLOSARIO.md#4624" target="_blank">4624</a>, qué Logon Type y qué IP.\
**B)** Reiniciar.\
**C)** Apagar switch.\
**D)** Reinstalar.

**⛔ DETENTE AQUÍ.**

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **A**.
2. **A — pipeline top IP**.
3. **B**.
4. **B — ruido**.
5. **A**.
6. **B**.
7. **B — baseline**.
8. **B**.
9. **B**.
10. **A**.

**🏆 Resultado**

| **Correctas** | **Nivel** |
| :--- | :--- |
| **10/10** | ⭐ Excelente — detectás como L1. |
| **8–9/10** | 🟢 Muy buen nivel. |
| **6–7/10** | 🟡 Buen progreso. |
| **4–5/10** | 🟠 Repasar. |
| **0–3/10** | 🔴 Reestudiar. |

**📍 Progreso — Semana 5**

-   ✅ **Módulo 30 — ¿Qué es un <a href="../../GLOSARIO.md#log" target="_blank">log</a>?**
-   ✅ **Módulo 31 — Tipos de logs**
-   ✅ **Módulo 32 — Event Log de Windows**
-   ✅ **Módulo 33 — <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a> en Linux**
-   ✅ **Módulo 34 — Anatomía raw**
-   ✅ **Módulo 35 — Fuerza bruta y logins**
-   ⚪ Módulo 36 — Usuarios admin, persistencia e investigación
