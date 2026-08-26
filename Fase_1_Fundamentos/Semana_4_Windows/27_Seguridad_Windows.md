**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 27: Seguridad de Windows**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Defensas nativas + Evasión del atacante

Windows incluye varias capas de defensa. Entender **qué protege cada
una** y **cómo un atacante intenta evadirla** te permite valorar qué
alarmas son reales y qué controles reforzar.

**🎯 Objetivos de este módulo**

-   Conocer Windows Defender, Firewall, UAC, Windows Update.
-   Entender BitLocker, SmartScreen y Credential Guard.
-   Relacionar cada defensa con su posible evasión.
-   Ver cómo el SOC detecta intentos de evasión.

**1. Windows Defender (Antivirus / Antimalware)**

Protección en tiempo real contra malware. Genera eventos cuando detecta
o **bloquea** una amenaza. Un SOC revisa:

-   Detecciones de Defender (log de *Microsoft-Windows-Windows
    Defender/Operational*).
-   Intentos de **desactivar** Defender (cambios en registro o
    política).

Evasión típica: el atacante usa malware "fileless" (en memoria) o
firmas desconocidas para esquivar el antivirus.

**2. Firewall de Windows**

Controla qué tráfico entra/sale. Reglas por perfil (Dominio,
Privado, Público). El SOC investiga conexiones que salen hacia <a href="../../GLOSARIO.md#ips" target="_blank">IPs</a>
externas sin justificación.

**3. UAC**

Ya visto en el módulo 23. Un atacante intenta **bypass UAC** para
elevarse sin aviso.

**4. Windows Update**

Parchea vulnerabilidades. Un equipo sin actualizar es presa fácil de
**exploits conocidos**. El SOC debe identificar equipos desactualizados.

**5. BitLocker**

Cifra el disco. Protege los datos en reposo si alguien roba el equipo.
No detiene un atacante que ya inició sesión, pero dificulta el análisis
forense desde fuera.

**6. Credential Guard**

Aísla secretos (como los hashes de LSASS) en una zona protegida por
virtualización (VBS). Dificulta el **LSASS dumping**. Si está
desactivado, el riesgo aumenta.

**7. SmartScreen**

Filtra descargas y ejecutables desde internet. Un atacante intenta
engañarlo o desactivarlo para ejecutar su payload.

**8. Control de aplicaciones (AppLocker / WDAC)**

Permite o bloquea la ejecución de ciertas aplicaciones por política.
Si está activo, un binario no autorizado no corre. El atacante busca
LOLBins ya permitidos.

**9. Mapa de defensa vs evasión**

Defensa

↓

Intento de evasión

Windows Defender → malware fileless / sin firma

Firewall → túneles por <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> o <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> (puerto 443)

UAC → bypass UAC

BitLocker → no ayuda si ya hay sesión

Credential Guard → técnicas sin volcado de LSASS

SmartScreen → ejecutables firmados o desactivación

**10. El SOC y las capas**

Ninguna capa es perfecta. Por eso las organizaciones suman **<a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> +
Firewall + <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> + SOC**. El analista busca la **falla en la cadena**:
por ejemplo, Defender bloquea pero el atacante ya había ejecutado
PowerShell.

**🧪 Laboratorio recomendado**

1.  Abre *Seguridad de Windows* (icono de escudo) y revisa las secciones
    (Protección contra virus, Firewall, Antirransumo/BitLocker).
2.  `Win + R` → `wf.msc` para ver el Firewall avanzado.
3.  Investiga qué ocurre si un equipo tiene Defender desactivado (en
    entorno de prueba, sin riesgo).
4.  Reflexiona: ¿qué evento del log de Defender te alertaría?

**📝 Evaluación — Módulo 27: Seguridad de Windows**

**🔹 Pregunta 1**

¿Qué defensa cifra el disco para proteger datos en reposo?

**A)** UAC\
**B)** BitLocker\
**C)** SmartScreen\
**D)** Firewall

**🔹 Pregunta 2**

Credential Guard protege principalmente contra:

**A)** Spam\
**B)** Volcado de credenciales (LSASS)\
**C)** Impresión\
**D)** Errores de red

**🔹 Pregunta 3**

El atacante intenta "bypass UAC" para:

**A)** Imprimir\
**B)** Elevar privilegios sin aviso\
**C)** Cifrar disco\
**D)** Crear usuarios

**🔹 Pregunta 4**

Un equipo sin Windows Update es vulnerable a:

**A)** Phishing de correo\
**B)** Exploits conocidos ya parcheados\
**C)** Borrado de logs\
**D)** Fuerza bruta de red

**🔹 Pregunta 5**

SmartScreen filtra principalmente:

**A)** Descargas y ejecutables desde internet\
**B)** Memoria RAM\
**C)** Registros del sistema\
**D)** Usuarios locales

**🔹 Pregunta 6**

El malware "fileless" intenta evadir:

**A)** El firewall físico\
**B)** El antivirus (ejecuta en memoria)\
**C)** BitLocker\
**D)** UAC

**🔹 Pregunta 7**

AppLocker/WDAC sirven para:

**A)** Cifrar discos\
**B)** Permitir o bloquear ejecución de aplicaciones\
**C)** Crear usuarios\
**D)** Reiniciar servicios

**🔹 Pregunta 8**

¿Por qué el SOCrevisa si Defender fue desactivado?

**A)** Porque mejora el rendimiento.\
**B)** Porque puede ser un paso del atacante para ejecutar malware.\
**C)** Porque crea logs.\
**D)** Porque cifra la red.

**🔹 Pregunta 9 — Caso SOC**

Se detecta que un binario se comunicó por HTTPS (443) hacia una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>
externa y que Defender luego lo bloqueó. Conclusión razonable:

**A)** Es tráfico normal de actualización.\
**B)** Posible malware que intentó C2 y fue detenido; debe
investigarse el origen.\
**C)** El firewall falló.\
**D)** No pasa nada.

**🔹 Pregunta 10**

El concepto de "defensa en profundidad" significa:

**A)** Usar un solo antivirus muy potente.\
**B)** Sumar varias capas (EDR, Firewall, SIEM, SOC) porque ninguna es
perfecta.\
**C)** Apagar UAC.\
**D)** Cifrar solo el correo.

**⛔ DETENTE AQUÍ** e intenta resolver las 10.

**✅ RESPUESTAS Y JUSTIFICACIÓN**

1. **B — BitLocker**.
2. **B**: protege LSASS/credenciales.
3. **B**: elevar sin aviso.
4. **B**: exploits conocidos.
5. **A**: descargas/ejecutables.
6. **B**: malware en memoria evade AV.
7. **B**: control de ejecución.
8. **B**: desactivar Defender es táctica de atacante.
9. **B**: C2 intentado y bloqueado merece investigación.
10. **B**: capas múltiples porque ninguna es perfecta.

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ✅ **Módulo 25 — CMD y PowerShell**
-   ✅ **Módulo 26 — Windows Event Logs**
-   ✅ **Módulo 27 — Seguridad de Windows**
-   ⚪ Módulo 28 — Windows desde la perspectiva del atacante
-   ⚪ Módulo 29 — Investigación SOC en Windows
