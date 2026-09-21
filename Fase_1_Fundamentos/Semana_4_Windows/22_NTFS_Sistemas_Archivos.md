**🖥️ Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 4 — Windows**

**Módulo 22: NTFS y Sistema de Archivos de Windows**

**Nivel:** Principiante → Analista SOC Nivel 1\
**Enfoque:** Sistemas + Seguridad + Análisis SOC

Muy bien. Ahora entramos en un tema fundamental porque, cuando un equipo
Windows es comprometido, **el sistema de archivos suele contener
evidencias de lo que ocurrió**.

Hasta ahora aprendimos qué es un proceso, un servicio, un usuario y el
Registro. Ahora vamos a aprender **dónde viven los archivos y qué
información de seguridad podemos obtener de ellos**.

**🎯 Objetivos**

Al finalizar este módulo deberías poder:

-   Entender qué es un sistema de archivos.

-   Comprender qué es NTFS.

-   Diferenciar archivo, carpeta, volumen y partición.

-   Conocer la estructura de C:\\.

-   Entender permisos y ACL.

-   Comprender la herencia de permisos.

-   Entender archivos ocultos.

-   Conocer \$MFT, \$LogFile y otros componentes importantes.

-   Identificar ubicaciones interesantes para un Analista SOC.

-   Reconocer cómo un atacante puede abusar del sistema de archivos.

-   Saber qué evidencias buscar durante una investigación.

**1. ¿Qué es un sistema de archivos?**

Un sistema de archivos es el mecanismo que utiliza el sistema operativo
para **organizar y administrar la información almacenada**.

Imaginá un depósito:

DEPÓSITO

│

├── Documentos

├── Herramientas

├── Equipos

└── Archivos

Windows necesita hacer algo similar con el disco:

DISCO

│

├── Windows

├── Users

├── Program Files

└── ProgramData

El sistema de archivos determina, entre otras cosas:

-   Cómo se almacenan los archivos.

-   Cómo se organizan.

-   Cómo se identifican.

-   Qué permisos tienen.

-   Qué usuario puede acceder.

-   Qué información adicional se almacena.

**2. ¿Qué es NTFS?**

**NTFS** significa:

**New Technology File System**

Es el sistema de archivos utilizado habitualmente por Windows para sus
volúmenes.

Por ejemplo:

C:\\

puede estar utilizando NTFS.

**3. ¿Por qué NTFS es importante para un SOC?**

Porque NTFS no solamente almacena:

archivo.exe

También mantiene información relacionada con ese archivo.

Por ejemplo:

-   Nombre.

-   Tamaño.

-   Ubicación.

-   Permisos.

-   Fechas.

-   Propietario.

-   Metadatos.

-   Información utilizada por el sistema para administrar el archivo.

Durante una investigación esto puede ayudar a responder:

**¿Qué archivo existía? ¿Dónde estaba? ¿Quién podía acceder? ¿Cuándo fue
creado o modificado?**

**4. Disco, partición y volumen**

Antes de continuar tenemos que separar tres conceptos.

**Disco**

Es el dispositivo físico.

Ejemplo:

SSD de 1 TB

**Partición**

Es una división lógica del disco.

DISCO

│

├── Partición 1

└── Partición 2

**Volumen**

Es una estructura de almacenamiento que Windows puede montar y utilizar.

Por ejemplo:

C:\\

D:\\

E:\\

Una forma simplificada de recordarlo:

DISCO FÍSICO

↓

PARTICIONES

↓

VOLÚMENES

↓

SISTEMA DE ARCHIVOS

↓

ARCHIVOS Y CARPETAS

**5. La raíz C:\\**

Cuando abrís:

C:\\

estás en la raíz del volumen.

Podemos encontrar:

C:\\

│

├── Windows

├── Users

├── Program Files

├── Program Files (x86)

└── ProgramData

No todos los equipos tienen exactamente las mismas carpetas, pero estas
son muy comunes.

**6. C:\\Windows**

Esta carpeta contiene componentes del sistema operativo.

Ejemplo:

C:\\Windows\\

Dentro encontramos muchas subcarpetas.

Una de las más importantes:

C:\\Windows\\System32\\

**7. System32**

A pesar de su nombre, en Windows de 64 bits System32 contiene muchos
componentes de 64 bits del sistema.

Aquí podemos encontrar ejecutables legítimos como:

<a href="../../GLOSARIO.md#cmd" target="_blank">cmd.exe</a>

<a href="../../GLOSARIO.md#powershell" target="_blank">powershell</a>.exe

taskmgr.exe

services.exe

Esto nos lleva a una idea de seguridad muy importante:

**Que un archivo tenga un nombre legítimo no significa que cualquier
archivo con ese nombre sea legítimo.**

Por ejemplo:

C:\\Windows\\System32\\powershell.exe

es una ubicación esperable.

Pero:

C:\\Users\\Public\\powershell.exe

merece una investigación adicional si aparece inesperadamente.

**La ruta importa.**

**8. C:\\Users**

Aquí encontramos los perfiles de los usuarios.

Ejemplo:

C:\\Users\\

│

├── Public

├── Administrator

└── Gonzalo

Dentro del perfil:

C:\\Users\\Gonzalo\\

podemos encontrar:

Desktop

Documents

Downloads

Pictures

Videos

AppData

**9. Downloads**

Esta ubicación es especialmente interesante:

C:\\Users\\\<usuario\>\\Downloads\\

¿Por qué?

Porque muchos archivos descargados de Internet terminan allí.

Por ejemplo:

factura.pdf

documento.docx

programa.exe

actualizacion.exe

Imaginemos:

Downloads

↓

factura.exe

↓

PowerShell

↓

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

Para un SOC, esto podría ser una cadena de investigación importante.

**10. AppData**

Otra ubicación muy importante:

C:\\Users\\\<usuario\>\\AppData\\

Contiene datos utilizados por aplicaciones.

Tiene subdirectorios como:

Local

LocalLow

Roaming

**11. ¿Por qué AppData interesa a un SOC?**

Porque es una ubicación utilizada legítimamente por muchas aplicaciones,
pero también puede ser utilizada por malware.

Por ejemplo:

C:\\Users\\Gonzalo\\AppData\\Roaming\\

podría contener archivos de una aplicación legítima.

Pero imaginemos:

C:\\Users\\Gonzalo\\AppData\\Roaming\\update.exe

y descubrimos que:

update.exe

↓

se ejecuta al iniciar sesión

↓

crea PowerShell

↓

se conecta a Internet

Ahora tenemos una situación que merece una investigación seria.

**12. Program Files**

Normalmente las aplicaciones instaladas se encuentran aquí:

C:\\Program Files\\

y:

C:\\Program Files (x86)\\

Por ejemplo:

C:\\Program Files\\Google\\

C:\\Program Files\\Microsoft\\

Una aplicación ejecutándose desde su ubicación habitual suele ser menos
sospechosa que una copia inesperada en una carpeta temporal.

Pero nuevamente:

**La ubicación es un indicador, no una prueba definitiva.**

**13. ProgramData**

Otra carpeta importante:

C:\\ProgramData\\

Es utilizada para almacenar datos de aplicaciones que pueden ser
compartidos entre usuarios.

También puede aparecer en investigaciones de malware y persistencia.

Por eso, si un <a href="../../GLOSARIO.md#edr" target="_blank">EDR</a> informa:

C:\\ProgramData\\update.exe

no debemos asumir automáticamente que es malicioso.

Debemos investigar:

-   Firma digital.

-   Hash.

-   Propietario.

-   Fecha.

-   Proceso padre.

-   Persistencia.

-   Conexiones de red.

**14. Permisos NTFS**

Ahora entramos en una parte muy importante.

NTFS permite establecer permisos sobre archivos y carpetas.

Por ejemplo:

Archivo:

informe.pdf

Podríamos tener:

Gonzalo → Leer

Juan → Leer / Modificar

Admin → Control total

Esto permite controlar quién puede hacer qué.

**15. Principales permisos**

Simplificando:

**Read**

Leer.

**Write**

Escribir/modificar.

**Execute**

Ejecutar.

**Delete**

Eliminar.

**Full Control**

Control total.

**16. ACL**

ACL significa:

**Access Control List**

Una ACL contiene las reglas que determinan quién puede acceder a un
recurso y qué puede hacer.

Podemos imaginar:

ARCHIVO

↓

ACL

│

├── Usuario A → Leer

├── Usuario B → Modificar

└── Administrador → Control total

**17. ACE**

Dentro de una ACL existen entradas individuales llamadas **ACE**:

Access Control Entry

Por ejemplo:

ACL

│

├── ACE → Gonzalo → Read

├── ACE → Juan → Write

└── ACE → Administrators → Full Control

Entonces:

ACL = conjunto de reglas

ACE = una regla individual

**18. Herencia de permisos**

Los permisos pueden heredarse desde una carpeta superior.

Ejemplo:

C:\\Empresa\\

↓

Documentos\\

↓

Finanzas\\

↓

informe.xlsx

Si Documentos tiene determinados permisos, Finanzas y sus archivos
pueden heredarlos.

Esto facilita la administración.

**19. ¿Por qué la herencia importa para seguridad?**

Imaginá que:

C:\\Empresa\\

tiene permisos demasiado amplios.

Esos permisos podrían heredarse hacia:

C:\\Empresa\\Finanzas\\

y terminar permitiendo que usuarios que no deberían acceder a
información financiera tengan acceso.

Por eso una mala configuración de permisos puede convertirse en un
problema de seguridad.

**20. NTFS y un atacante**

Supongamos que un atacante obtiene acceso como:

usuario estándar

Intentará descubrir:

¿Qué archivos puedo leer?

¿Qué puedo modificar?

¿Qué carpetas puedo escribir?

¿Qué usuarios existen?

¿Qué recursos están protegidos?

Si encuentra una carpeta donde puede escribir:

C:\\ProgramData\\

podría intentar utilizarla para almacenar archivos maliciosos.

**21. Privilegios y permisos no son exactamente lo mismo**

Esta distinción es importante.

**Privilegios**

Son capacidades asignadas a una cuenta o contexto de seguridad.

**Permisos**

Controlan el acceso a recursos concretos.

Por ejemplo:

Usuario

↓

Privilegios

Archivo

↓

Permisos

Un usuario podría tener ciertos privilegios administrativos pero
encontrarse con restricciones específicas sobre determinados recursos,
dependiendo de la configuración.

**22. Archivos ocultos**

Windows permite ocultar archivos.

Por ejemplo:

archivo.txt

puede tener el atributo:

Hidden

Pero:

**Oculto no significa seguro ni malicioso.**

Muchos archivos legítimos están ocultos porque forman parte de la
configuración del sistema.

**23. Atributos de archivos**

Un archivo puede tener diferentes atributos.

Entre ellos:

-   Hidden.

-   Read-only.

-   System.

-   Archive.

Podemos observarlos mediante herramientas de Windows.

Por ejemplo:

attrib

**24. ¿Cómo podría abusar un atacante de los atributos?**

Podría intentar ocultar archivos para dificultar una investigación.

Por ejemplo:

malware.exe

podría configurarse con atributos que dificulten su visualización
normal.

Pero un analista SOC o investigador puede buscar específicamente esos
atributos.

**25. \$MFT**

Ahora entramos en una parte más avanzada.

NTFS utiliza una estructura llamada:

**Master File Table (MFT)**

Podemos pensar en ella como un índice central de los archivos y
directorios del volumen.

Simplificando:

NTFS

│

└── \$MFT

│

├── archivo1

├── archivo2

├── archivo3

└── carpeta1

La MFT contiene metadatos importantes.

**26. ¿Por qué la MFT interesa a un investigador?**

Porque puede proporcionar información relacionada con:

-   Archivos existentes.

-   Archivos eliminados que aún tengan rastros recuperables.

-   Metadatos.

-   Fechas.

-   Estructura de directorios.

En análisis forense, la MFT puede ser una fuente de evidencia muy
importante.

**27. \$LogFile**

NTFS también utiliza:

\$LogFile

Está relacionado con el registro de operaciones del sistema de archivos
y ayuda a mantener la consistencia de NTFS.

Para un analista forense puede aportar información sobre operaciones
realizadas sobre archivos.

**28. \$UsnJrnl**

Otro componente interesante es:

\$UsnJrnl

El **USN Journal** registra cambios realizados sobre archivos y
directorios.

Por ejemplo, puede registrar eventos relacionados con:

-   Creación.

-   Modificación.

-   Eliminación.

-   Renombrado.

Esto puede resultar muy útil para reconstruir actividad.

**29. Ejemplo de investigación**

Imaginemos:

10:00

usuario recibe correo

10:02

descarga factura.exe

10:03

factura.exe ejecutado

10:03

se crea archivo en AppData

10:04

se modifica Registry

10:04

se inicia PowerShell

10:05

conexión HTTPS

El sistema de archivos podría ayudarnos a investigar:

¿Qué archivo apareció?

¿Dónde?

¿Cuándo?

¿Fue modificado?

¿Fue eliminado?

¿Qué otros archivos aparecieron?

Y otras fuentes nos permiten complementar:

Event Logs

EDR

Registry

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

Firewall

**🕵️ 30. Un atacante elimina el archivo. ¿Terminó la evidencia?**

**No necesariamente.**

Este concepto es importantísimo.

Supongamos:

malware.exe

↓

ejecutado

↓

eliminado

Eso no significa necesariamente que toda evidencia desapareció.

Podrían quedar rastros en:

-   Event Logs.

-   EDR.

-   MFT.

-   USN Journal.

-   Prefetch.

-   Registro.

-   Memoria.

-   DNS.

-   Firewall.

-   Proxy.

Por eso una investigación SOC no debe depender de un único artefacto.

**31. Prefetch**

En determinados sistemas Windows, **Prefetch** puede proporcionar
información sobre la ejecución de aplicaciones.

Podemos encontrar archivos relacionados en:

C:\\Windows\\Prefetch\\

Por ejemplo:

NOTEPAD.EXE-XXXX.pf

Estos artefactos pueden ayudar en análisis forense a determinar que
determinadas aplicaciones fueron ejecutadas y obtener contexto temporal.

**32. ¿Cómo piensa un SOC?**

Supongamos que encontramos:

C:\\Users\\Empleado\\AppData\\Roaming\\update.exe

No debemos decir:

\"Es malware.\"

Debemos construir hipótesis.

**Pregunta 1**

¿Está firmado digitalmente?

**Pregunta 2**

¿Cuál es su hash?

**Pregunta 3**

¿Cuándo apareció?

**Pregunta 4**

¿Quién lo creó?

**Pregunta 5**

¿Se ejecutó?

**Pregunta 6**

¿Qué proceso lo inició?

**Pregunta 7**

¿Tiene persistencia?

**Pregunta 8**

¿Se comunicó con Internet?

**Pregunta 9**

¿Otros equipos tienen el mismo archivo?

Eso es **investigación basada en evidencia**.

**🛡️ 33. Defensa**

¿Cómo podemos defender un sistema Windows?

**Principio de <a href="../../GLOSARIO.md#minimo-privilegio" target="_blank">mínimo privilegio</a>**

Los usuarios deben tener solamente los permisos necesarios.

Necesita leer

↓

Read

No necesita modificar

↓

No Write

**Control de aplicaciones**

Permitir únicamente software autorizado.

**EDR**

Detectar comportamientos sospechosos.

**Antivirus**

Detectar archivos maliciosos conocidos y determinados comportamientos.

**Auditoría**

Registrar actividades relevantes.

**Control de permisos**

Revisar ACL y evitar permisos excesivos.

**🚨 34. Indicadores que deberían llamar nuestra atención**

No significan automáticamente malware, pero merecen investigación:

.exe en Downloads

.exe en AppData

.exe en Temp

PowerShell ejecutado desde ubicación inusual

Archivo con nombre parecido a un proceso legítimo

Ejemplo:

svchost.exe

versus:

svch0st.exe

La segunda utiliza 0 en lugar de o.

Esto puede ser un intento de **<a href="../../GLOSARIO.md#masquerading" target="_blank">masquerading</a>**.

**🧠 35. Concepto clave: Masquerading**

Un atacante puede intentar hacer que un archivo malicioso parezca
legítimo.

Ejemplo:

Nombre legítimo:

svchost.exe

Archivo sospechoso:

svch0st.exe

Otro ejemplo:

C:\\Windows\\System32\\legitimo.exe

versus:

C:\\Users\\Public\\legitimo.exe

El nombre puede ser idéntico.

La **ruta**, firma, hash y comportamiento pueden revelar la diferencia.

**🔬 36. Comandos que vamos a utilizar**

Más adelante vas a trabajar bastante con comandos como:

dir

Para listar archivos.

cd

Para cambiar de directorio.

type

Para visualizar contenido de archivos de texto.

attrib

Para observar/modificar atributos.

Y PowerShell:

Get-ChildItem

equivalente moderno de listar elementos.

También:

Get-Acl

para consultar permisos.

Por ejemplo:

Get-Acl C:\\Users

Esto será especialmente importante cuando lleguemos a **PowerShell para
SOC**.

**🧩 37. Caso práctico SOC**

Tenemos:

ALERTA

Equipo:

PC-CONTABILIDAD-04

Archivo:

update.exe

Ruta:

C:\\Users\\Usuario\\AppData\\Roaming\\

Fecha:

10:32

Usuario:

Usuario

Proceso padre:

winword.exe

Conexión:

HTTPS → dominio desconocido

**¿Qué observamos?**

Tenemos varios indicadores:

Word

↓

update.exe

↓

AppData\\Roaming

↓

HTTPS

No podemos afirmar todavía que sea malware.

Pero la combinación merece investigación.

**🔎 38. ¿Qué investigarías?**

Como SOC Nivel 1:

**Archivo**

Hash

Firma digital

Tamaño

Fecha

**Proceso**

Proceso padre

Línea de comandos

Usuario

Privilegios

**Red**

Dominio

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

Puerto

DNS

Reputación

**Persistencia**

Registry

Servicios

Tareas programadas

Startup

**Alcance**

¿Hay otros equipos afectados?

Esto es muy importante:

**Un archivo sospechoso aislado puede ser un incidente. El mismo archivo
en 300 equipos puede indicar una campaña.**

**🧠 Resumen del módulo**

  --------------------------------------------------------------------------
  **Concepto**       **Qué significa**
  ------------------ -------------------------------------------------------
  **NTFS**           Sistema de archivos de Windows

  **Volumen**        Espacio de almacenamiento utilizado por Windows

  **ACL**            Lista de control de acceso

  **ACE**            Entrada individual dentro de una ACL

  **MFT**            Tabla maestra de archivos de NTFS

  **\$LogFile**      Registro utilizado por NTFS

  **\$UsnJrnl**      Registra cambios en archivos/directorios

  **AppData**        Datos de aplicaciones por usuario

  **Program Files**  Ubicación habitual de aplicaciones

  **ProgramData**    Datos compartidos de aplicaciones

  **Prefetch**       Artefacto útil para investigar ejecución de
                     aplicaciones

  **Masquerading**   Intentar aparentar ser un archivo legítimo
  --------------------------------------------------------------------------

**🎯 Lo que quiero que recuerdes**

No quiero que memorices simplemente:

\"AppData puede ser peligroso.\"

Quiero que aprendas a pensar:

ARCHIVO

↓

¿Dónde está?

↓

¿Quién lo creó?

↓

¿Cuándo apareció?

↓

¿Quién lo ejecutó?

↓

¿Con qué privilegios?

↓

¿Qué proceso lo inició?

↓

¿Modificó algo?

↓

¿Tiene persistencia?

↓

¿Se comunicó con Internet?

↓

¿Hay otros equipos afectados?

Ese razonamiento es muchísimo más importante que memorizar rutas.

**📍 Progreso --- Semana 4**

-   ✅ **Módulo 21 --- Fundamentos de Windows**

-   ✅ **Módulo 22 --- NTFS y sistema de archivos**

-   ⚪ Módulo 23 --- Usuarios, grupos y autenticación

-   ⚪ Módulo 24 --- Procesos y servicios

-   ⚪ Módulo 25 --- CMD y PowerShell

-   ⚪ Módulo 26 --- Windows Event Logs

-   ⚪ Módulo 27 --- Seguridad de Windows

-   ⚪ Módulo 28 --- Windows desde la perspectiva del atacante

-   ⚪ Módulo 29 --- Investigación SOC en Windows

Como venimos haciendo, **el siguiente paso natural es el examen de 10
preguntas sobre NTFS**, incluyendo algunas situaciones donde tendrás que
pensar como Analista SOC.

**🖥️ Carrera de Analista SOC**

**Semana 4 — Windows**

**📝 Examen --- Módulo 22: NTFS y Sistema de Archivos**

**Nivel:** Principiante → Analista SOC Nivel 1

Vamos a mantener el mismo formato. Esta evaluación combina **conceptos
de NTFS + análisis de situaciones reales de SOC**.

**Instrucciones:** una sola respuesta correcta por pregunta.\
Intentá responder las 10 antes de bajar a las soluciones.

**🔹 Pregunta 1**

¿Qué significa **NTFS**?

**A)** Network Transfer File System

**B)** New Technology File System

**C)** Network Technology Firewall System

**D)** New Transfer Security

**🔹 Pregunta 2**

¿Cuál es la función principal de un sistema de archivos?

**A)** Controlar exclusivamente las conexiones de red.

**B)** Administrar y organizar la información almacenada en un
dispositivo.

**C)** Detectar automáticamente malware.

**D)** Administrar únicamente usuarios.

**🔹 Pregunta 3**

¿Cuál de las siguientes rutas es una ubicación habitual para los
perfiles de usuario de Windows?

**A)** C:\\Accounts\\

**B)** C:\\Windows\\Profiles\\

**C)** C:\\Users\\

**D)** C:\\System\\Users\\

**🔹 Pregunta 4**

Un Analista SOC encuentra el siguiente archivo:

C:\\Users\\Empleado\\Downloads\\factura.exe

¿Cuál es la interpretación más correcta?

**A)** Es definitivamente malware.

**B)** Es definitivamente un archivo legítimo.

**C)** La ubicación puede ser un indicador de interés, pero es necesario
investigar el archivo y su comportamiento.

**D)** Windows no permite ejecutar archivos desde Downloads.

**🔹 Pregunta 5**

¿Qué es una **ACL**?

**A)** Una lista que define qué usuarios o grupos pueden acceder a un
recurso y qué acciones pueden realizar.

**B)** Un registro de eventos de Windows.

**C)** Un tipo de malware.

**D)** Una tabla que almacena direcciones IP.

**🔹 Pregunta 6**

¿Cuál es la relación correcta entre **ACL y ACE**?

**A)** ACL y ACE son exactamente lo mismo.

**B)** ACE es un conjunto de ACL.

**C)** ACL es un conjunto de entradas ACE.

**D)** ACL pertenece al Registro y ACE pertenece a DNS.

**🔹 Pregunta 7**

¿Qué componente de NTFS mantiene información relacionada con los
archivos y directorios del volumen?

**A)** \$MFT

**B)** \$DNS

**C)** \$Registry

**D)** \$Network

**🔹 Pregunta 8**

Durante una investigación, un analista observa:

C:\\Users\\Empleado\\AppData\\Roaming\\update.exe

¿Qué debería concluir inicialmente?

**A)** Es malware confirmado.

**B)** Es un archivo legítimo porque se llama update.exe.

**C)** La ubicación y el nombre justifican una investigación adicional,
pero no demuestran por sí solos que sea malware.

**D)** Windows solo permite ejecutar archivos legítimos desde AppData.

**🔹 Pregunta 9 --- Caso SOC**

Un EDR informa:

Archivo:

svch0st.exe

Ruta:

C:\\Users\\Public\\

Proceso:

svch0st.exe

Conexión:

<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443

El analista observa que el nombre se parece a:

svchost.exe

¿Qué técnica podría estar intentando utilizar el atacante?

**A)** DNS Tunneling.

**B)** Masquerading.

**C)** <a href="../../GLOSARIO.md#dhcp-spoofing" target="_blank">DHCP Spoofing</a>.

**D)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Poisoning.

**🔹 Pregunta 10 --- Caso SOC ⭐**

Durante una investigación se descubre:

09:00 → Documento recibido por correo

09:02 → factura.exe aparece en Downloads

09:03 → factura.exe es ejecutado

09:03 → aparece nuevo archivo en AppData

09:04 → se modifica el Registry

09:05 → comienza conexión HTTPS

09:10 → factura.exe es eliminado

El atacante eliminó el archivo. ¿Qué afirmación es más correcta?

**A)** La investigación terminó porque el archivo ya no existe.

**B)** No queda ninguna evidencia.

**C)** Pueden existir otros artefactos y registros que permitan
reconstruir la actividad.

**D)** Al eliminar el archivo, Windows elimina automáticamente todos los
logs relacionados.

**⛔ DETENTE AQUÍ**

Antes de mirar las respuestas, anotá tus elecciones:

1-

2-

3-

4-

5-

6-

7-

8-

9-

10-

**✅ RESPUESTAS Y JUSTIFICACIÓN**

**Pregunta 1**

**✅ B --- New Technology File System**

NTFS significa **New Technology File System** y es el sistema de
archivos utilizado habitualmente por Windows.

Además de almacenar archivos, NTFS administra información como:

-   Metadatos.

-   Permisos.

-   Estructura de directorios.

-   Información necesaria para administrar el volumen.

**Pregunta 2**

**✅ B --- Administrar y organizar la información almacenada**

Un sistema de archivos permite organizar y administrar:

Archivos

Carpetas

Metadatos

Permisos

En nuestro caso:

Windows

↓

NTFS

↓

Archivos y carpetas

**Pregunta 3**

**✅ C --- C:\\Users\\**

Los perfiles de usuario normalmente se encuentran allí:

C:\\Users\\

├── Usuario1

├── Usuario2

└── Public

Dentro del perfil podemos encontrar:

Desktop

Documents

Downloads

Pictures

AppData

Para un SOC, estas ubicaciones son importantes porque pueden contener
archivos descargados, datos de aplicaciones y posibles artefactos de
actividad maliciosa.

**Pregunta 4**

**✅ C**

Esta es una de las reglas más importantes de nuestro entrenamiento:

**Un indicador sospechoso no es automáticamente una prueba de malware.**

Un .exe en Downloads puede ser:

Programa legítimo

o

Malware

Por eso investigaríamos:

-   Hash.

-   Firma digital.

-   Origen.

-   Fecha de creación.

-   Proceso padre.

-   Línea de comandos.

-   Conexiones de red.

-   EDR/antivirus.

-   Comportamiento.

**Pregunta 5**

**✅ A --- Access Control List**

Una ACL determina quién puede acceder a un recurso y qué puede hacer.

Por ejemplo:

archivo.txt

Juan → Read

Pedro → Modify

Administrators → Full Control

Esto es fundamental para aplicar el **principio de mínimo privilegio**.

**Pregunta 6**

**✅ C --- ACL es un conjunto de entradas ACE**

Recordalo así:

ACL

│

├── ACE → Usuario A → Read

├── ACE → Usuario B → Write

└── ACE → Admin → Full Control

Por lo tanto:

**ACL = conjunto de reglas.**\
**ACE = una regla individual.**

**Pregunta 7**

**✅ A --- \$MFT**

La **Master File Table** es una estructura fundamental de NTFS.

Contiene información relacionada con los archivos y directorios del
volumen.

En análisis forense puede ayudar a estudiar:

-   Archivos.

-   Directorios.

-   Metadatos.

-   Fechas.

-   Estructura del sistema de archivos.

**Pregunta 8**

**✅ C**

Esta es otra pregunta de pensamiento SOC.

No debemos caer en:

AppData + update.exe = malware

La conclusión correcta es:

Ubicación interesante

\+

Nombre genérico

↓

INVESTIGAR

Después buscaríamos:

Hash

Firma

Proceso padre

Fecha

Persistencia

Conexiones

Otros equipos afectados

**Pregunta 9**

**✅ B --- Masquerading**

El archivo:

svch0st.exe

intenta parecerse a:

svchost.exe

La sustitución de:

o

por:

0

es un ejemplo clásico de engaño mediante nombres similares.

Esto puede intentar engañar a:

-   Usuarios.

-   Administradores.

-   Analistas.

-   Herramientas o procesos de revisión manual.

Además, la ruta:

C:\\Users\\Public\\

y la conexión de red hacen que el archivo merezca una investigación
adicional.

**Pregunta 10**

**✅ C --- Pueden existir otros artefactos y registros**

Esta pregunta es especialmente importante para un futuro analista.

Aunque:

factura.exe

sea eliminado, pueden quedar evidencias en:

Event Logs

EDR

MFT

USN Journal

Prefetch

Registry

DNS

Firewall

Proxy

Memoria

Por eso una investigación no debe depender de encontrar **el archivo
original**.

El objetivo es reconstruir:

¿Qué ocurrió?

↓

¿Cuándo?

↓

¿Quién?

↓

¿Cómo?

↓

¿Qué ejecutó?

↓

¿A dónde se conectó?

↓

¿Qué hizo después?

**🏆 TABLA DE RESULTADOS**

  -----------------------------------------------------------------------------
  **Correctas**   **Nivel**
  --------------- -------------------------------------------------------------
  **10/10**       🟢 Excelente --- dominio sólido de NTFS y buen razonamiento
                  SOC.

  **8--9/10**     🟢 Muy buen nivel --- podés avanzar.

  **6--7/10**     🟡 Buen progreso --- conviene reforzar algunos conceptos.

  **4--5/10**     🟠 Necesitamos repasar NTFS y permisos.

  **0--3/10**     🔴 Recomiendo volver al módulo antes de avanzar.
  -----------------------------------------------------------------------------

**🧠 DESAFÍO SOC --- Sin opciones**

Este ejercicio es diferente. No tiene respuestas A/B/C/D.

El <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> informa:

Equipo: PC-CONTABILIDAD-05

Usuario: empleado01

Archivo detectado:

update.exe

Ruta:

C:\\Users\\empleado01\\AppData\\Roaming\\

Proceso padre:

winword.exe

Después:

powershell.exe

Conexión:

TCP 443

Dominio:

update-security\[.\]xyz

Como Analista SOC, quiero que pienses en **qué investigarías primero**.

Tu respuesta podría tener esta estructura:

1\. Archivo:

\...

2\. Proceso:

\...

3\. Usuario:

\...

4\. Persistencia:

\...

5\. Red:

\...

6\. Alcance:

\...

No busco todavía una respuesta perfecta. Lo importante es empezar a
desarrollar el **método de investigación** que vamos a utilizar durante
los próximos módulos.

**📊 Progreso de Semana 4**

  -------------------------------------------------------------------------
  **Módulo**                                                   **Estado**
  ------------------------------------------------------------ ------------
  1\. Fundamentos de Windows                                   ✅

  2\. NTFS y sistema de archivos                               ✅

  3\. Usuarios, grupos y autenticación                         ⏳

  4\. Procesos y servicios                                     ⏳

  5\. CMD y PowerShell                                         ⏳

  6\. Windows Event Logs                                       ⏳

  7\. Seguridad de Windows                                     ⏳

  8\. Windows desde la perspectiva del atacante                ⏳

  9\. Investigación SOC en Windows                             ⏳
  -------------------------------------------------------------------------
