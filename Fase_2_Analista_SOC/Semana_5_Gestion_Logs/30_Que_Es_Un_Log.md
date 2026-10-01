**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 5 — Gestión de Logs**

**Módulo 30: ¿Qué es un log y por qué es la materia prima del SOC?**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Fundamento + Mentalidad SOC

Este módulo abre la Fase 2. Hasta ahora aprendiste redes, Linux y Windows. Ahora respondemos la pregunta que une todo: **¿de dónde saca el SOC la evidencia?** La respuesta es el <a href="../../GLOSARIO.md#log" target="_blank">log</a>.

**🎯 Objetivos del módulo**

-   Definir qué es un log y qué partes tiene.
-   Entender por qué el log es la materia prima del SOC.
-   Distinguir evento, registro y alerta.
-   Comprender el ciclo: `Evento → Log → Colector → <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> → Analista`.
-   Asumir la regla de oro: sin logs no hay investigación.

---

**1. ¿Qué es un log?**

Un log es un **registro escrito de algo que ocurrió en un sistema**.

Por ejemplo:

Usuario inició sesión

↓

Proceso creado

↓

Servicio falló

↓

Conexión a una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

Cada uno de esos hechos puede quedar guardado como una línea de texto, una entrada estructurada o un evento Windows.

Podés imaginarlo así:

ACTIVIDAD

↓

EVENTO

↓

LOG

↓

EVIDENCIA

Sin log, la actividad **pasó y se perdió**. Con log, la actividad **pasó y quedó registrada**.

**2. Analogía de la caja negra**

Pensá en la caja negra de un avión.

El avión vuela.

↓

La caja negra graba.

↓

Si hay un accidente, los investigadores escuchan la grabación.

↓

Reconstruyen qué pasó.

El log es la caja negra de cada servidor, PC, firewall y aplicación.

El SOC es el equipo que escucha esas grabaciones todos los días.

**3. Analogía del libro de guardia**

En un edificio, el guardia anota en un cuaderno:

08:00 → entró Juan

08:05 → entró proveedora

09:12 → alarma puerta trasera

Nadie lee el cuaderno a cada minuto. Pero cuando falta algo, lo primero que se revisa es ese cuaderno.

El log funciona igual. La mayoría de las líneas son rutina. El valor aparece cuando investigás.

**4. Evento, registro y alerta: no los confundas**

**Evento:** algo ocurrió. Ejemplo: `login fallido`.

**Registro (log):** el evento quedó guardado. Ejemplo: línea en `/var/log/auth.log` o <a href="../../GLOSARIO.md#event-id" target="_blank">Event ID</a> <a href="../../GLOSARIO.md#4625" target="_blank">4625</a>.

**Alerta:** una herramienta o regla decidió que ese evento merece atención. Ejemplo: `40 fallos en 1 minuto → alerta de fuerza bruta`.

Podés tener:

Evento

↓

sin log = invisible para el SOC.

Evento

↓

con log = visible.

Log

↓

sin regla = nadie lo mira.

Log + regla

↓

alerta = alguien lo investiga.

**5. ¿Por qué el log es la materia prima del SOC?**

Porque todo lo que el SOC hace depende de logs:

Detección

↓

logs.

Investigación

↓

logs.

<a href="../../GLOSARIO.md#correlacion" target="_blank">Correlación</a>

↓

logs.

Reporte

↓

logs con timestamps.

Si los logs están incompletos, el SOC investiga a ciegas. Si están manipulados, investiga engañado. Si no existen, no puede investigar.

Por eso en la Semana 4 insistimos tanto en <a href="../../GLOSARIO.md#4624" target="_blank">4624</a>/4625/<a href="../../GLOSARIO.md#4688" target="_blank">4688</a>: ya estabas leyendo logs sin llamarlos así.

**6. El ciclo completo del dato**

PC / Servidor / Firewall

↓

genera evento

↓

escribe log local

↓

agente/colector lo reenvía

↓

SIEM lo recibe y normaliza

↓

regla genera alerta

↓

analista investiga

En esta Semana 5 trabajás en el primer eslabón: **leer el log local en crudo**. En las Semanas 6-7 verás cómo el SIEM automatiza el resto.

**7. ¿Qué pasa si no hay logs o se borran?**

Recordá el Event ID <a href="../../GLOSARIO.md#1102" target="_blank">1102</a> (borrado del log de seguridad).

Un atacante que borra logs intenta:

evitar detección

↓

eliminar evidencia

↓

romper la línea de tiempo

Por eso en empresas los logs se **centralizan**: aunque borre el log local, la copia ya viajó al SIEM.

Regla práctica:

> **Log local = evidencia frágil. Log centralizado = evidencia defendible.**

**8. Caso SOC introductorio**

Servidor lento. Abrís el log y ves:

`Failed password for invalid user admin from 203.0.113.5`

repetido 500 veces.

Sin log, dirías: "está lento".

Con log, decís: "está bajo <a href="../../GLOSARIO.md#fuerza-bruta" target="_blank">fuerza bruta</a> <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a> desde 203.0.113.5, debo verificar si hubo un `Accepted password` posterior".

Esa diferencia es la que te convierte en analista.

**9. Lo que NO es un log**

No es un antivirus. No bloquea nada.

No es un firewall. No filtra nada.

No es una conclusión. Solo cuenta hechos.

Tu trabajo es convertir hechos en contexto y contexto en veredicto.

**📚 Resumen**

LOG

= registro de lo que ocurrió.

EVENTO

= el hecho. LOG = el hecho guardado. ALERTA = el hecho que alguien marcó para investigar.

MATERIA PRIMA

= sin logs no hay detección ni investigación.

CICLO

= evento → log → colector → SIEM → analista.

REGLA

= centralizar, proteger y leer en crudo antes de automatizar.

**🧩 Conceptos clave para memorizar**

| **Concepto** | **Debes recordar** |
| :--- | :--- |
| Log | Registro de acontecimientos del sistema. |
| Evento | Algo que ocurrió. |
| Alerta | Evento que una regla marcó para investigar. |
| Caja negra | El log guarda la historia para reconstruirla. |
| Centralización | Evita depender solo de la máquina comprometida. |
| 1102 | Borrar el log también es evidencia. |

**🎓 Consejo como tu instructor de SOC**

No empieces por el SIEM. Empezá por el archivo de texto.

Si sabés leer un <a href="../../GLOSARIO.md#raw-log" target="_blank">raw log</a> con `cat` y `grep`, después vas a entender qué hace Splunk por vos. Si empezás al revés, solo vas a apretar botones.

Acordate: **un Event ID aislado describe un evento. Una secuencia de eventos puede describir un comportamiento.**

---

**📘 Carrera de Analista SOC**

**Semana 5 — Gestión de Logs**

**Evaluación — Módulo 30: ¿Qué es un log?**

**Nivel:** Principiante → Analista SOC Nivel 1

**Instrucciones:** Respondé sin consultar el material. Nivel entrevista SOC L1.

**Pregunta 1**

¿Qué es un log?

**A)** Un antivirus.\
**B)** Un registro de algo que ocurrió en un sistema.\
**C)** Un tipo de firewall.\
**D)** Una contraseña.

**Pregunta 2**

¿Qué diferencia hay entre evento y alerta?

**A)** Son lo mismo.\
**B)** Evento es lo que ocurrió; alerta es lo que una regla marcó para investigar.\
**C)** Alerta es lo que ocurrió; evento es la regla.\
**D)** Ninguna.

**Pregunta 3**

¿Por qué el log es la materia prima del SOC?

**A)** Porque reemplaza al firewall.\
**B)** Porque de él salen la detección, investigación y reporte.\
**C)** Porque cifra el disco.\
**D)** Porque crea usuarios.

**Pregunta 4**

Orden correcto del ciclo del dato:

**A)** Analista → SIEM → Log → Evento.\
**B)** Evento → Log → Colector → SIEM → Analista.\
**C)** SIEM → Evento → Log → Analista.\
**D)** Log → Evento → Alerta → Firewall.

**Pregunta 5**

Si un evento no queda registrado en ningún log:

**A)** Igual lo ve el SOC.\
**B)** Es invisible para la investigación posterior.\
**C)** Genera alerta solo.\
**D)** Se guarda en el SIEM.

**Pregunta 6**

¿Qué indica un Event ID 1102?

**A)** Login exitoso.\
**B)** Borrado del log de seguridad, posible encubrimiento.\
**C)** Creación de proceso.\
**D)** Error de impresora.

**Pregunta 7**

¿Por qué se centralizan los logs en un SIEM?

**A)** Para borrarlos más rápido.\
**B)** Para no depender solo de la máquina que pudo ser comprometida.\
**C)** Para ahorrar disco.\
**D)** Para cifrarlos.

**Pregunta 8**

Ves 500 líneas `Failed password` desde una IP. Lo correcto es:

**A)** Decir "está lento" y cerrar.\
**B)** Verificar volumen, IP origen y si hubo un acceso exitoso posterior.\
**C)** Reiniciar sin mirar más.\
**D)** Borrar el log.

**Pregunta 9 — Caso SOC**

Secuencia: evento → log local → ¿qué sigue en empresa?

**A)** Nada.\
**B)** Colector lo envía al SIEM, el SIEM correlaciona y el analista investiga.\
**C)** El log se borra solo.\
**D)** El firewall lo cifra.

**Pregunta 10**

¿Qué NO es un log?

**A)** Evidencia de hechos.\
**B)** Una conclusión o veredicto por sí solo.\
**C)** Fuente de investigación.\
**D)** Registro de eventos.

**⛔ DETENTE AQUÍ** e intentá resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B**: registro de lo ocurrido.
2. **B**: evento = hecho; alerta = hecho marcado por regla.
3. **B**: todo el trabajo SOC sale de logs.
4. **B**: evento → log → colector → SIEM → analista.
5. **B**: sin registro no hay historia.
6. **B — 1102**: borrado del log, alerta grave.
7. **B**: la copia central sobrevive aunque borren lo local.
8. **B**: volumen + origen + éxito posterior.
9. **B**: centralizar y correlacionar.
10. **B**: el log cuenta hechos; el analista concluye.

**🏆 Resultado**

| **Correctas** | **Nivel** |
| :--- | :--- |
| **10/10** | ⭐ Excelente — base SOC sólida. |
| **8–9/10** | 🟢 Muy buen nivel. |
| **6–7/10** | 🟡 Buen progreso. |
| **4–5/10** | 🟠 Repasar conceptos. |
| **0–3/10** | 🔴 Volver a estudiar el módulo. |

**📍 Progreso — Semana 5**

-   ✅ **Módulo 30 — ¿Qué es un log?**
-   ⚪ Módulo 31 — Tipos de logs
-   ⚪ Módulo 32 — Event Log de Windows (vista SOC)
-   ⚪ Módulo 33 — <a href="../../GLOSARIO.md#syslog" target="_blank">Syslog</a> en Linux
-   ⚪ Módulo 34 — Anatomía de un log raw
-   ⚪ Módulo 35 — Fuerza bruta y logins inusuales
-   ⚪ Módulo 36 — Usuarios admin, persistencia e investigación
