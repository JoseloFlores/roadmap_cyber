**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 27: Seguridad de Windows**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Defensas nativas + Evasión del atacante

Este módulo unifica la referencia de defensas (Defender, Firewall, <a href="../../GLOSARIO.md#uac" target="_blank">UAC</a>, Update, <a href="../../GLOSARIO.md#bitlocker" target="_blank">BitLocker</a>, <a href="../../GLOSARIO.md#credential-guard" target="_blank">Credential Guard</a>, <a href="../../GLOSARIO.md#smartscreen" target="_blank">SmartScreen</a>, <a href="../../GLOSARIO.md#applocker" target="_blank">AppLocker</a>/WDAC, defensa en profundidad) con la guía larga (firmas vs comportamiento, Defender + Event Logs, Defender + <a href="../../GLOSARIO.md#powershell" target="_blank">PowerShell</a>/procesos, alerta ≠ fin, protección ≠ investigación).

**🎯 Objetivos del módulo**

-   Conocer qué protege cada defensa nativa y cómo se evade.
-   Distinguir detección por firmas vs comportamiento.
-   Relacionar alertas de Defender con Event Logs, procesos y red.
-   Aplicar defensa en profundidad (EDR + Firewall + SIEM + SOC).


---

## Parte A — Referencia de defensas

**1. <a href="../../GLOSARIO.md#windows-defender" target="_blank">Windows Defender</a> (Antivirus / Antimalware)**

Protección en tiempo real contra malware. Genera eventos cuando detecta
o **bloquea** una amenaza. Un SOC revisa:

-   Detecciones de Defender (log de *Microsoft-Windows-Windows
    Defender/Operational*).
-   Intentos de **desactivar** Defender (cambios en registro o
    política).

Evasión típica: el atacante usa malware "fileless" (en memoria) o
firmas desconocidas para esquivar el antivirus.

**2. <a href="../../GLOSARIO.md#firewall-de-windows" target="_blank">Firewall de Windows</a>**

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

Aísla secretos (como los hashes de <a href="../../GLOSARIO.md#lsass" target="_blank">LSASS</a>) en una zona protegida por
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



---

## Parte B — Guía completa: Defender y seguridad del sistema (visión general 1-9 + profundización)

> Nota: la numeración original 36-44 se corrigió a 1-9 para mantener la coherencia del módulo.

Hasta ahora estudiamos cómo **investigar lo que ocurrió**.

Ahora vamos a estudiar cómo Windows intenta **prevenir y detectar amenazas**.

**1. ¿Qué es Windows Defender?**

Actualmente forma parte de:

**Microsoft Defender**

Es el conjunto de capacidades de seguridad de Microsoft para proteger Windows y otros componentes del entorno.

En un equipo Windows podemos encontrar capacidades relacionadas con:

Antivirus

Antimalware

Firewall

Protección de aplicaciones

Protección de cuentas

Protección del dispositivo

**2. Defender Antivirus**

Una de sus funciones principales es detectar y bloquear malware.

Conceptualmente:

Archivo

↓

Defender

↓

Análisis

↓

¿Malicioso?

┌───────┴───────┐

↓ ↓

NO SÍ

↓ ↓

Permitir Bloquear

Pero la seguridad moderna no depende únicamente de firmas.

También existen mecanismos de análisis de comportamiento.

**3. Firma vs comportamiento**

**Detección basada en firmas**

Busca características conocidas.

Conceptualmente:

Archivo

↓

Hash / patrón

↓

Base de amenazas

↓

Coincidencia

**Detección basada en comportamiento**

Busca acciones sospechosas.

Por ejemplo:

Word

↓

PowerShell

↓

script

↓

descarga

↓

ejecución

Aunque el archivo no sea reconocido exactamente por una firma, la cadena puede resultar sospechosa.

**4. ¿Por qué esto importa para SOC?**

Porque un EDR/antivirus puede generar una alerta.

Por ejemplo:

Threat Detected

Host:

PC-VENTAS-03

Process:

powershell.exe

File:

C:\Users\Juan\AppData\Temp\update.exe

El SOC recibe esa alerta.

Pero ahora tenemos que combinar:

Defender

\+

Event Logs

\+

Procesos

\+

Red

\+

Usuario

Y volvemos a la correlación.

**5. Defender no es lo mismo que un SIEM**

Esto es importante.

**Defender / EDR**

Está más enfocado en:

Endpoint

↓

Detectar

↓

Prevenir

↓

Responder

**SIEM**

Está más enfocado en:

Múltiples fuentes

↓

Recopilar

↓

Correlacionar

↓

Generar alertas

Conceptualmente:

┌── Windows

├── Firewall

├── DNS

├── <a href="../../GLOSARIO.md#vpn" target="_blank">VPN</a>

└── Defender

↓

SIEM

↓

SOC

**6. Defender Firewall**

Windows también incluye firewall.

Su función básica es controlar tráfico de red según reglas.

Conceptualmente:

Conexión

↓

Firewall

↓

¿Existe regla?

┌───────┴───────┐

↓ ↓

Permitir Bloquear

Y esto conecta directamente con:

IP

Puerto

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

<a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

que estudiamos durante Redes.

**7. Un ejemplo**

Supongamos:

Proceso:

malware.exe

Destino:

203.x.x.x

Puerto:

443

El SOC podría observar:

Proceso

↓

Conexión TCP

↓

Firewall

↓

Defender

↓

SIEM

Cada componente aporta una pieza diferente.

**8. Windows Security**

En Windows también encontramos distintas capas de seguridad.

Pensalo como:

WINDOWS

│

┌──────────────┼──────────────┐

↓ ↓ ↓

Defender Firewall Seguridad

↓ ↓ ↓

Malware Red Cuentas

│ │ │

└──────────────┼──────────────┘

↓

LOGS

↓

SIEM

↓

SOC

**9. ¿Qué quiero que aprendas de este módulo?**

No quiero que te conviertas todavía en administrador de Defender.

Quiero que comprendas:

- qué protege,

- qué puede detectar,

- qué es una alerta,

- qué diferencia existe entre antivirus, EDR y SIEM,

- cómo se relaciona Defender con Event Logs,

- cómo se relaciona con procesos,

- cómo se relaciona con red.

**🧠 Conexión con todo lo anterior**

Mirá el recorrido que estamos construyendo:

REDES

↓

IP

↓

TCP

↓

PUERTOS

↓

DNS

↓

WINDOWS

↓

Usuarios

↓

Autenticación

↓

<a href="../../GLOSARIO.md#4624" target="_blank">4624</a>/<a href="../../GLOSARIO.md#4625" target="_blank">4625</a>

↓

Procesos

↓

<a href="../../GLOSARIO.md#4688" target="_blank">4688</a>

↓

<a href="../../GLOSARIO.md#cmd" target="_blank">CMD</a> / PowerShell

↓

Conexiones

↓

Defender

↓

SIEM

↓

SOC

Esto ya no son temas separados.

**Estamos construyendo una cadena completa de investigación.**

Y ese es el objetivo de esta formación.

**🛡️ SEMANA 4 — WINDOWS**

**Profundización: Microsoft Defender y seguridad de Windows**

**1. La idea fundamental**

Pensá en un equipo Windows como una casa:

WINDOWS

│

┌────────┼────────┐

↓ ↓ ↓

Antivirus Firewall Identidad

│ │ │

└────────┼────────┘

↓

Telemetría

↓

SIEM

↓

SOC

Cada mecanismo protege una parte diferente.

**Defender no reemplaza al firewall, al SIEM ni al analista SOC.**

**2. Microsoft Defender Antivirus**

La función principal es detectar y bloquear amenazas en el endpoint.

Puede analizar:

- archivos,

- procesos,

- memoria y comportamiento según las capacidades habilitadas,

- descargas,

- scripts,

- actividad asociada a malware.

Un flujo simplificado:

Archivo / proceso

↓

Defender

↓

análisis

↓

¿Sospechoso?

↓ ↓

NO SÍ

↓ ↓

Permitir Bloquear / alertar

Pero acá aparece algo importante:

**Detectar un archivo malicioso y detectar un comportamiento malicioso no son exactamente lo mismo.**

**3. Firmas vs comportamiento**

**Detección tradicional**

Un antivirus puede utilizar información conocida sobre amenazas.

Por ejemplo:

Archivo

↓

Características

↓

Comparación

↓

Coincide con amenaza conocida

↓

Detección

Esto es muy útil contra amenazas conocidas.

Pero un atacante puede modificar un malware para intentar evadir una firma.

Por eso entran otras técnicas.

**4. Detección basada en comportamiento**

Supongamos que aparece:

WINWORD.EXE

↓

POWERSHELL.EXE

↓

script

↓

descarga

↓

ejecución

Ninguno de esos elementos, considerado aisladamente, necesariamente significa malware.

Pero la **cadena de comportamiento** puede resultar sospechosa.

Esto conecta directamente con lo que acabamos de estudiar:

4688

↓

Proceso creado

↓

Parent Process

↓

<a href="../../GLOSARIO.md#command-line" target="_blank">Command Line</a>

↓

Comportamiento

**5. Defender + Event Logs**

Esta conexión es importantísima para tu futuro trabajo.

Imaginá que Defender genera:

Threat detected

Y simultáneamente tenemos:

4624

↓

4688 PowerShell

↓

Conexión externa

↓

Defender detecta amenaza

Ahora no tenemos una sola fuente.

Tenemos varias evidencias.

Event Logs

\+

Defender

\+

Red

↓

Correlación

↓

SOC

**6. Microsoft Defender Firewall**

El firewall controla tráfico según reglas.

Conceptualmente:

TRÁFICO

↓

FIREWALL

↓

┌───────┴───────┐

↓ ↓

PERMITIR BLOQUEAR

Las reglas pueden considerar diferentes características, como:

IP origen

IP destino

Puerto

Protocolo

Programa

Perfil de red

Dirección del tráfico

Por eso todo lo que estudiaste en Redes vuelve a aparecer.

**7. Ejemplo SOC**

Supongamos que un proceso sospechoso intenta:

malware.exe

↓

TCP

↓

203.x.x.x

↓

443

Podemos tener:

Proceso

↓

4688

Red

↓

TCP/443

Defender

↓

detección

Firewall

↓

bloqueo

SIEM

↓

correlación

SOC

↓

investigación

Esto es exactamente el tipo de información que puede terminar en una investigación.

**8. Defender y PowerShell**

Esto es particularmente importante para vos.

PowerShell es una herramienta legítima:

Administradores

↓

PowerShell

↓

Automatización

Pero también puede ser utilizada abusivamente.

Por eso un SOC puede interesarse por:

Quién ejecutó PowerShell

↓

Desde qué proceso

↓

Qué command line utilizó

↓

Qué script ejecutó

↓

Qué archivos tocó

↓

Qué conexiones realizó

Por eso estudiamos PowerShell **antes** de Event Logs.

Ahora todo empieza a tener sentido.

**9. Defender y procesos**

Imaginemos:

WINWORD.EXE

↓

POWERSHELL.EXE

↓

CMD.EXE

↓

UNKNOWN.EXE

Defender podría generar una alerta relacionada con alguna actividad.

El analista no debería mirar únicamente:

"Defender detectó algo."

Tiene que mirar:

¿Quién?

¿Dónde?

¿Cuándo?

¿Qué proceso?

¿Quién lo creó?

¿Qué comando?

¿Qué archivo?

¿Qué conexión?

**10. Defender no es un SIEM**

Esto quiero que quede muy claro.

**Defender**

Protege principalmente el endpoint.

ENDPOINT

↓

DEFENDER

↓

Detectar / prevenir

**SIEM**

Centraliza y correlaciona información.

Windows ──┐

Linux ────┤

Firewall ─┤

DNS ──────┤

VPN ──────┤

Defender ─┘

↓

SIEM

↓

SOC

**EDR**

Está orientado a proporcionar mayor visibilidad y capacidades de detección/respuesta sobre endpoints.

Conceptualmente:

Endpoint

↓

EDR

↓

Telemetría

↓

Detección

↓

Investigación / respuesta

En entornos empresariales, estas tecnologías suelen complementarse.

**11. ¿Qué puede interesarle al SOC de Defender?**

Muchísimas cosas, pero para tu nivel inicial quiero que pienses en:

**Detecciones**

Malware

PUA

Comportamiento sospechoso

Script sospechoso

**Equipo**

Hostname

Usuario

IP

**Proceso**

Nombre

Ruta

Parent

Command Line

**Archivo**

Ruta

Nombre

Hash

Detección

**Red**

IP destino

Dominio

Puerto

Protocolo

**12. Una alerta no es el final**

Esto es una de las cosas más importantes de tu formación.

Un principiante puede pensar:

"Defender detectó malware → caso terminado."

Un analista piensa:

"Defender detectó una amenaza. Ahora necesito determinar el alcance."

Por ejemplo:

¿Está solamente en este equipo?

↓

¿Se ejecutó?

↓

¿Quién lo ejecutó?

↓

¿Se comunicó con Internet?

↓

¿Hay otros equipos afectados?

↓

¿Hubo robo de credenciales?

↓

¿Hubo persistencia?

Eso es **Incident Response**.

**13. Protección ≠ investigación**

Una herramienta puede:

BLOQUEAR

algo.

Pero el SOC todavía puede necesitar investigar:

¿Quién lo descargó?

¿Desde dónde?

¿Por qué llegó al equipo?

¿Se ejecutó?

¿Intentó comunicarse?

¿Hay otros indicadores?

Por eso el SOC necesita **telemetría**, no solamente antivirus.

---

**📍 Progreso — Semana 4**

-   ✅ **Módulo 21 — Fundamentos de Windows**
-   ✅ **Módulo 22 — NTFS y sistema de archivos**
-   ✅ **Módulo 23 — Usuarios, grupos y autenticación**
-   ✅ **Módulo 24 — Procesos y servicios**
-   ✅ **Módulo 25 — CMD y PowerShell**
-   ✅ **Módulo 26 — Windows Event Logs**
-   ✅ **Módulo 27 — Seguridad de Windows**
-   ✅ **Módulo 28 — Windows desde la perspectiva del atacante**
-   ⚪ Módulo 29 — Investigación SOC en Windows
