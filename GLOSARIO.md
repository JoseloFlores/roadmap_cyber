# 📖 Glosario de Términos y Siglas Críticas del SOC

> **De:** Analista Senior / Líder de SOC  
> **Para:** Futuro Analista SOC Nivel 1  
> **Clasificación:** Uso Interno / Formación Técnica / Material de Estudio

Este glosario contiene los términos, siglas y acrónimos más críticos e importantes que debes dominar para superar entrevistas técnicas y desempeñarte con éxito en tu día a día dentro de un Centro de Operaciones de Seguridad (SOC).

---

## 🌐 1. Conceptos Base, Redes y Modelos

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="osi"></a>**OSI** | *Open Systems Interconnection* | Modelo de referencia de 7 capas que estandariza las funciones de comunicación de red. |
| <a id="tcp"></a>**TCP** | *Transmission Control Protocol* | Protocolo de transporte orientado a conexión, confiable y con control de flujo y errores. |
| <a id="ip"></a>**IP** | *Internet Protocol* | Protocolo de red encargado de direccionar y enrutar paquetes a través de internet. |
| <a id="udp"></a>**UDP** | *User Datagram Protocol* | Protocolo de transporte no orientado a conexión, rápido pero sin garantías de entrega. |
| <a id="pdu"></a>**PDU** | *Protocol Data Unit* | Unidad de datos formateada para una capa específica del modelo OSI (ej. Trama, Paquete, Segmento). |
| <a id="mac"></a>**MAC** | *Media Access Control* | Dirección física única asignada de fábrica a cada tarjeta de red (NIC). |
| <a id="arp"></a>**ARP** | *Address Resolution Protocol* | Protocolo que traduce direcciones IP (Capa 3) a direcciones MAC (Capa 2). |
| <a id="icmp"></a>**ICMP** | *Internet Control Message Protocol* | Protocolo utilizado para enviar mensajes de control y diagnóstico (ej. comandos `ping` y `traceroute`). |
| <a id="lan"></a>**LAN** | *Local Area Network* | Red de computadoras que abarca un área geográfica limitada, como una oficina u hogar. |
| <a id="wan"></a>**WAN** | *Wide Area Network* | Red que interconecta múltiples redes locales (LAN) a gran distancia geográfica. |
| <a id="dmz"></a>**DMZ** | *Demilitarized Zone* | Zona desmilitarizada; segmento de red aislado que contiene los servidores expuestos a Internet (ej. web, correo). |
| <a id="gateway"></a>**Gateway** | *Puerta de Enlace* | Dispositivo o ruta que conecta la red local con otras redes (Internet); punto de salida del tráfico. |
| <a id="nat"></a>**NAT** | *Network Address Translation* | Traducción de direcciones de red; permite que varios equipos salgan a Internet compartiendo una sola IP pública. |
| <a id="broadcast"></a>**broadcast** | *Difusión* | Envío de un mensaje a todos los equipos de una subred a la vez (ej. el DHCP Discover). |
| <a id="vlan"></a>**VLAN** | *Virtual LAN* | Red de área local virtual; segmenta una red física en varias redes lógicas separadas. |
| <a id="three-way-handshake"></a>**Three-Way Handshake** | *Conexión de tres pasos* | Proceso de TCP para establecer una conexión fiable: SYN, SYN-ACK y ACK. |

---

## 🔐 2. Aplicaciones y Protocolos de Capa Superior

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="dns"></a>**DNS** | *Domain Name System* | Servicio de resolución de nombres que traduce nombres de dominio (ej. `google.com`) a direcciones IP. |
| <a id="http"></a>**HTTP** | *Hypertext Transfer Protocol* | Protocolo de transferencia de hipertexto utilizado para la navegación web (sin cifrar). |
| <a id="https"></a>**HTTPS** | *Hypertext Transfer Protocol Secure* | Versión segura de HTTP que cifra el tráfico mediante SSL/TLS por el puerto 443. |
| <a id="ftp"></a>**FTP** | *File Transfer Protocol* | Protocolo tradicional para la transferencia de archivos en una red. |
| <a id="smtp"></a>**SMTP** | *Simple Mail Transfer Protocol* | Protocolo estándar utilizado para el envío de correos electrónicos entre servidores. |
| <a id="ssh"></a>**SSH** | *Secure Shell* | Protocolo que permite el acceso y control remoto seguro de servidores por consola (puerto 22). |
| <a id="ssl"></a>**SSL** | *Secure Sockets Layer* | Protocolo criptográfico antiguo para asegurar comunicaciones web (reemplazado por TLS). |
| <a id="tls"></a>**TLS** | *Transport Layer Security* | Sucesor moderno y seguro de SSL, utilizado para cifrar conexiones de red (ej. HTTPS, SMTPS). |
| <a id="wireshark"></a>**Wireshark** | *Wireshark* | Analizador de protocolos (sniffer) que captura y muestra el tráfico de red en detalle. |
| <a id="transaction-id"></a>**Transaction ID** | *ID de Transacción* | Identificador que relaciona entre sí los 4 mensajes DHCP (Discover, Offer, Request y ACK). |
| <a id="dhcp"></a>**DHCP** | *Dynamic Host Configuration Protocol* | Protocolo de la capa de aplicación que asigna automáticamente IP, máscara, gateway y DNS a los equipos (proceso DORA). |

---

## 🛡️ 3. Arquitectura y Tecnologías del SOC

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="soc"></a>**SOC** | *Security Operations Center* | Centro de Operaciones de Seguridad; equipo y facilidad física encargada del monitoreo y respuesta a incidentes. |
| <a id="siem"></a>**SIEM** | *Security Information and Event Management* | Plataforma centralizada que recopila, correlaciona y analiza logs de seguridad de toda la infraestructura. |
| <a id="soar"></a>**SOAR** | *Security Orchestration, Automation, and Response* | Herramienta que automatiza la respuesta a incidentes de seguridad mediante flujos de trabajo (playbooks). |
| <a id="waf"></a>**WAF** | *Web Application Firewall* | Firewall especializado en proteger aplicaciones web filtrando el tráfico HTTP/HTTPS (Capa 7). |
| <a id="ids"></a>**IDS** | *Intrusion Detection System* | Sistema de detección de intrusos; monitorea el tráfico de red o endpoints para alertar sobre actividad maliciosa. |
| <a id="ips"></a>**IPS** | *Intrusion Prevention System* | Sistema de prevención de intrusos; además de detectar, tiene la capacidad de bloquear activamente el tráfico malicioso. |
| <a id="edr"></a>**EDR** | *Endpoint Detection and Response* | Solución avanzada de seguridad para hosts que monitorea, registra y responde ante amenazas en endpoints (PCs, servidores). |
| <a id="xdr"></a>**XDR** | *Extended Detection and Response* | Evolución del EDR que integra la detección y respuesta a través de múltiples capas (red, nube, endpoints, correo). |
| <a id="ndr"></a>**NDR** | *Network Detection and Response* | Solución enfocada en el análisis continuo del tráfico de red para identificar comportamientos anómalos. |
| <a id="mdr"></a>**MDR** | *Managed Detection and Response* | Servicio de ciberseguridad tercerizado que provee monitoreo y respuesta a amenazas las 24/7. |
| <a id="vpn"></a>**VPN** | *Virtual Private Network* | Red privada virtual; crea un túnel seguro y cifrado sobre una red pública como Internet. |
| <a id="iam"></a>**IAM** | *Identity and Access Management* | Marco de políticas y tecnologías para asegurar que los usuarios correctos tengan el acceso adecuado a los recursos. |
| <a id="mfa"></a>**MFA** | *Multi-Factor Authentication* | Autenticación multifactor; requiere dos o más pruebas de identidad independientes para conceder acceso. |
| <a id="wazuh"></a>**Wazuh** | *Wazuh* | Plataforma open-source de SIEM/EDR para detección, respuesta y cumplimiento de seguridad. |

---

## ☣️ 4. Ciberamenazas e Investigación de Incidentes

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="cve"></a>**CVE** | *Common Vulnerabilities and Exposures* | Diccionario público de vulnerabilidades de seguridad conocidas en software y hardware. |
| <a id="ioc"></a>**IOC** | *Indicator of Compromise* | Indicador de Compromiso; evidencia forense (hash, IP, dominio) que sugiere que un sistema fue comprometido. |
| <a id="ioa"></a>**IOA** | *Indicator of Attack* | Indicador de Ataque; señales en tiempo real que se enfocan en la intención y el comportamiento activo del atacante. |
| <a id="dos"></a>**DoS** | *Denial of Service* | Ataque de denegación de servicio que busca inhabilitar un recurso saturándolo con peticiones. |
| <a id="ddos"></a>**DDoS** | *Distributed Denial of Service* | Ataque DoS realizado de manera distribuida desde múltiples fuentes comprometidas (botnets). |
| <a id="apt"></a>**APT** | *Advanced Persistent Threat* | Amenaza Persistente Avanzada; grupo de atacantes altamente capacitado y financiado (generalmente estados-nación). |

---

## 🐧 5. Administración de Linux y Línea de Comandos

| Término | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="cli"></a>**CLI** | *Command Line Interface* | Interfaz de línea de comandos; forma de interactuar con el sistema operativo escribiendo comandos en la terminal. |
| <a id="shell"></a>**Shell** | *Shell* | Intérprete de comandos que recibe lo que escribes y lo ejecuta (ej. `bash`, `sh`, `zsh`). |
| <a id="bash"></a>**Bash** | *Bourne Again Shell* | La shell más utilizada en Linux y macOS; es el intérprete por defecto en la mayoría de distribuciones. |
| <a id="kernel"></a>**Kernel** | *Kernel* | Núcleo del sistema operativo; gestiona hardware, memoria y procesos. Linux es un kernel. |
| <a id="distribucion"></a>**Distribución** | *Linux Distribution* | Conjunto de Linux + software empaquetado (Ubuntu, Debian, Kali, CentOS, etc.). El kernel es el motor; la distribución es el auto. |
| <a id="fhs"></a>**FHS** | *Filesystem Hierarchy Standard* | Estándar que define la estructura de directorios de Linux (`/etc`, `/home`, `/var/log`, `/tmp`, etc.). |
| <a id="root"></a>**root** | *Root / Superusuario* | Usuario administrador con control total del sistema (UID 0). |
| <a id="sudo"></a>**sudo** | *Super User DO* | Comando que permite ejecutar acciones con privilegios de administrador de forma temporal y controlada. |
| <a id="grep"></a>**grep** | *Global Regular Expression Print* | Herramienta para buscar patrones de texto dentro de archivos o salidas de otros comandos; esencial para analizar logs. |
| <a id="pipe"></a>**pipe** | *Pipe (\|)* | Operador que conecta la salida de un comando con la entrada de otro (ej. `cat log \| grep "Failed"`). |
| <a id="pid"></a>**PID** | *Process Identifier* | Identificador numérico único de cada proceso en ejecución. |
| <a id="daemon"></a>**Daemon** | *Daemon* | Proceso que corre en segundo plano prestando un servicio (ej. `sshd`, `nginx`, `systemd`). |
| <a id="chmod"></a>**chmod** | *Change Mode* | Comando para cambiar los permisos (`rwx`) de archivos y directorios. |
| <a id="chown"></a>**chown** | *Change Owner* | Comando para cambiar el propietario (y grupo) de un archivo o directorio. |
| <a id="setuid"></a>**setuid** | *Set User ID* | Bit especial de permisos que hace que un ejecutable corra con los privilegios de su propietario (potencial riesgo de escalada). |
| <a id="umask"></a>**umask** | *User file creation mask* | Define los permisos por defecto que reciben los archivos y directorios recién creados. |
| <a id="syslog"></a>**Syslog** | *System Logging Protocol* | Protocolo estándar (UDP 514) para enviar y centralizar logs de sistemas y dispositivos; clave para SIEM. |

---

## 🧩 6. Términos prácticos de los módulos

| Término | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="dora"></a>**DORA** | *Discover, Offer, Request, Acknowledge* | Proceso de 4 pasos con el que DHCP asigna una configuración IP al cliente. |
| <a id="rogue-dhcp"></a>**Rogue DHCP** | *Servidor DHCP no autorizado* | Servidor DHCP malicioso montado en la red para entregar configuración falsa (gateway/DNS). |
| <a id="dhcp-starvation"></a>**DHCP Starvation** | *Agotamiento de DHCP* | Ataque que consume todas las IPs del pool para dejar a equipos legítimos sin dirección (DoS). |
| <a id="dhcp-spoofing"></a>**DHCP Spoofing** | *Suplantación DHCP* | Servidor DHCP falso que entrega gateway/DNS maliciosos para interceptar el tráfico (MITM). |
| <a id="dhcp-snooping"></a>**DHCP Snooping** | *Filtrado DHCP del switch* | Función del switch que descarta mensajes DHCP de puertos no confiables. |
| <a id="mitm"></a>**MITM** | *Man-In-The-Middle* | Ataque donde el atacante se sitúa entre dos partes para interceptar o modificar el tráfico. |
| <a id="802-1x"></a>**802.1X** | *IEEE 802.1X* | Estándar de autenticación por puerto de red para controlar el acceso a la red. |
| <a id="port-security"></a>**Port Security** | *Seguridad de Puertos* | Función del switch que limita las direcciones MAC por puerto para frenar ataques. |
| <a id="lease"></a>**lease** | *Concesión* | Tiempo durante el cual una IP asignada por DHCP puede ser usada antes de renovarse. |
| <a id="scope"></a>**scope** | *Ámbito* | Rango de direcciones IP que un servidor DHCP reparte a los clientes. |

---

## 🪟 7. Windows, Usuarios y Autenticación

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="sam"></a>**SAM** | *Security Account Manager* | Base de datos local de Windows que almacena la información de las cuentas locales y representaciones criptográficas de sus contraseñas; objetivo frecuente de *credential dumping*. |
| <a id="sid"></a>**SID** | *Security Identifier* | Identificador de seguridad único con el que Windows identifica cuentas y otras entidades de seguridad (usuario, grupo, equipo). |
| <a id="rid"></a>**RID** | *Relative Identifier* | Última parte del SID que distingue una cuenta dentro de un equipo o dominio (ej. la cuenta Administrador integrada termina en `-500`). |
| <a id="uac"></a>**UAC** | *User Account Control* | Control de cuentas de usuario; solicita confirmación antes de ejecutar acciones con privilegios elevados para frenar elevaciones silenciosas. |
| <a id="ntlm"></a>**NTLM** | *NT LAN Manager* | Mecanismo/protocolo de autenticación histórico de Microsoft basado en desafío-respuesta (challenge-response); todavía presente en escenarios específicos. |
| <a id="kerberos"></a>**Kerberos** | *Kerberos* | Protocolo de autenticación basado en tickets, principal en dominios modernos de Active Directory (KDC → TGT → service tickets). |
| <a id="active-directory"></a>**Active Directory** | *Active Directory (AD)* | Servicio de directorio de Microsoft que administra de forma centralizada identidades, equipos, grupos, políticas y recursos de un dominio. |
| <a id="dc"></a>**DC** | *Domain Controller* | Servidor que proporciona las funciones centrales del dominio de Active Directory, incluida la autenticación; activo crítico. |
| <a id="kdc"></a>**KDC** | *Key Distribution Center* | Componente central de Kerberos encargado de emitir y gestionar tickets (contiene los servicios AS y TGS). |
| <a id="as"></a>**AS** | *Authentication Service* | Servicio del KDC que participa en la autenticación inicial y entrega el TGT. |
| <a id="tgt"></a>**TGT** | *Ticket Granting Ticket* | Ticket inicial de Kerberos que permite al usuario solicitar posteriormente tickets para servicios concretos. |
| <a id="tgs"></a>**TGS** | *Ticket Granting Service* | Servicio del KDC que, a partir del TGT, emite los tickets de servicio (service tickets). |
| <a id="service-ticket"></a>**Service Ticket** | *Ticket de Servicio* | Ticket de Kerberos que permite al usuario acceder a un servicio específico (ej. FILESERVER). |
| <a id="spn"></a>**SPN** | *Service Principal Name* | Identificador de una instancia de servicio dentro de Kerberos; las cuentas con SPN son objetivo de Kerberoasting. |
| <a id="ou"></a>**OU** | *Organizational Unit* | Unidad organizativa; contenedor de Active Directory que agrupa objetos (usuarios, equipos) para administrarlos mediante políticas. |
| <a id="gpo"></a>**GPO** | *Group Policy Object* | Objeto de directiva de grupo; aplica configuraciones y políticas (contraseñas, firewall, restricciones) a usuarios y equipos del dominio. |
| <a id="krbtgt"></a>**KRBTGT** | *KRBTGT Account* | Cuenta especial de Active Directory cuyo secreto criptográfico es clave en la emisión/validación de tickets Kerberos; su compromiso habilita un Golden Ticket. |
| <a id="logon-type"></a>**Logon Type** | *Tipo de inicio de sesión* | Clasificación que registra cómo ocurrió un logon: 2 (interactivo), 3 (red), 4 (batch), 5 (servicio), 10 (RDP). |
| <a id="lsass"></a>**LSASS** | *Local Security Authority Subsystem Service* | Proceso de Windows (`lsass.exe`) que gestiona seguridad y autenticación; objetivo de volcado de credenciales (LSASS dumping). |
| <a id="minimo-privilegio"></a>**Mínimo Privilegio** | *Principle of Least Privilege* | Regla de seguridad: cada usuario, grupo o proceso debe tener únicamente los permisos necesarios para realizar su función. |

---

## ⚔️ 8. Ataques a Credenciales y Técnicas de Evasión

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| <a id="password-spraying"></a>**Password Spraying** | *Rociado de contraseñas* | Ataque que prueba una o pocas contraseñas comunes contra muchas cuentas para evadir los bloqueos por intentos fallidos. |
| <a id="credential-stuffing"></a>**Credential Stuffing** | *Relleno de credenciales* | Ataque que reutiliza credenciales robadas de otros servicios para intentar acceder a una organización. |
| <a id="pass-the-hash"></a>**Pass-the-Hash** | *Pass-the-Hash* | Técnica que usa el hash de una credencial obtenido de un sistema para autenticarse sin conocer la contraseña original. |
| <a id="pass-the-ticket"></a>**Pass-the-Ticket** | *Pass-the-Ticket* | Técnica que reutiliza un ticket Kerberos válido para autenticarse ante servicios sin conocer la contraseña. |
| <a id="kerberoasting"></a>**Kerberoasting** | *Kerberoasting* | Ataque que solicita tickets de servicio de cuentas con SPN para atacar sus contraseñas de forma offline. |
| <a id="golden-ticket"></a>**Golden Ticket** | *Golden Ticket* | Falsificación de TGTs de Kerberos tras comprometer el secreto KRBTGT, otorgando acceso amplio y persistente al dominio. |
| <a id="masquerading"></a>**Masquerading** | *Suplantación de nombre* | Técnica de evasión donde el atacante nombra o ubica un archivo para que parezca legítimo (ej. `svch0st.exe`). |
| <a id="living-off-the-land"></a>**Living off the Land** | *Living off the Land (LotL)* | Abuso de herramientas legítimas ya presentes en el sistema (PowerShell, WMI, `rundll32`) para realizar acciones maliciosas. |
| <a id="process-injection"></a>**Process Injection** | *Inyección de procesos* | Familia de técnicas donde código malicioso intenta ejecutarse dentro del contexto de otro proceso legítimo. |
