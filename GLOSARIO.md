# 📖 Glosario de Términos y Siglas Críticas del SOC

> **De:** Analista Senior / Líder de SOC  
> **Para:** Futuro Analista SOC Nivel 1  
> **Clasificación:** Uso Interno / Formación Técnica / Material de Estudio

Este glosario contiene los términos, siglas y acrónimos más críticos e importantes que debes dominar para superar entrevistas técnicas y desempeñarte con éxito en tu día a día dentro de un Centro de Operaciones de Seguridad (SOC).

---

## 🌐 1. Conceptos Base, Redes y Modelos

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| **OSI** | *Open Systems Interconnection* | Modelo de referencia de 7 capas que estandariza las funciones de comunicación de red. |
| **TCP** | *Transmission Control Protocol* | Protocolo de transporte orientado a conexión, confiable y con control de flujo y errores. |
| **IP** | *Internet Protocol* | Protocolo de red encargado de direccionar y enrutar paquetes a través de internet. |
| **UDP** | *User Datagram Protocol* | Protocolo de transporte no orientado a conexión, rápido pero sin garantías de entrega. |
| **PDU** | *Protocol Data Unit* | Unidad de datos formateada para una capa específica del modelo OSI (ej. Trama, Paquete, Segmento). |
| **MAC** | *Media Access Control* | Dirección física única asignada de fábrica a cada tarjeta de red (NIC). |
| **ARP** | *Address Resolution Protocol* | Protocolo que traduce direcciones IP (Capa 3) a direcciones MAC (Capa 2). |
| **ICMP** | *Internet Control Message Protocol* | Protocolo utilizado para enviar mensajes de control y diagnóstico (ej. comandos `ping` y `traceroute`). |
| **LAN** | *Local Area Network* | Red de computadoras que abarca un área geográfica limitada, como una oficina u hogar. |
| **WAN** | *Wide Area Network* | Red que interconecta múltiples redes locales (LAN) a gran distancia geográfica. |
| **DMZ** | *Demilitarized Zone* | Zona desmilitarizada; segmento de red aislado que contiene los servidores expuestos a Internet (ej. web, correo). |

---

## 🔐 2. Aplicaciones y Protocolos de Capa Superior

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| **DNS** | *Domain Name System* | Servicio de resolución de nombres que traduce nombres de dominio (ej. `google.com`) a direcciones IP. |
| **HTTP** | *Hypertext Transfer Protocol* | Protocolo de transferencia de hipertexto utilizado para la navegación web (sin cifrar). |
| **HTTPS** | *Hypertext Transfer Protocol Secure* | Versión segura de HTTP que cifra el tráfico mediante SSL/TLS por el puerto 443. |
| **FTP** | *File Transfer Protocol* | Protocolo tradicional para la transferencia de archivos en una red. |
| **SMTP** | *Simple Mail Transfer Protocol* | Protocolo estándar utilizado para el envío de correos electrónicos entre servidores. |
| **SSH** | *Secure Shell* | Protocolo que permite el acceso y control remoto seguro de servidores por consola (puerto 22). |
| **SSL** | *Secure Sockets Layer* | Protocolo criptográfico antiguo para asegurar comunicaciones web (reemplazado por TLS). |
| **TLS** | *Transport Layer Security* | Sucesor moderno y seguro de SSL, utilizado para cifrar conexiones de red (ej. HTTPS, SMTPS). |

---

## 🛡️ 3. Arquitectura y Tecnologías del SOC

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| **SOC** | *Security Operations Center* | Centro de Operaciones de Seguridad; equipo y facilidad física encargada del monitoreo y respuesta a incidentes. |
| **SIEM** | *Security Information and Event Management* | Plataforma centralizada que recopila, correlaciona y analiza logs de seguridad de toda la infraestructura. |
| **SOAR** | *Security Orchestration, Automation, and Response* | Herramienta que automatiza la respuesta a incidentes de seguridad mediante flujos de trabajo (playbooks). |
| **WAF** | *Web Application Firewall* | Firewall especializado en proteger aplicaciones web filtrando el tráfico HTTP/HTTPS (Capa 7). |
| **IDS** | *Intrusion Detection System* | Sistema de detección de intrusos; monitorea el tráfico de red o endpoints para alertar sobre actividad maliciosa. |
| **IPS** | *Intrusion Prevention System* | Sistema de prevención de intrusos; además de detectar, tiene la capacidad de bloquear activamente el tráfico malicioso. |
| **EDR** | *Endpoint Detection and Response* | Solución avanzada de seguridad para hosts que monitorea, registra y responde ante amenazas en endpoints (PCs, servidores). |
| **XDR** | *Extended Detection and Response* | Evolución del EDR que integra la detección y respuesta a través de múltiples capas (red, nube, endpoints, correo). |
| **NDR** | *Network Detection and Response* | Solución enfocada en el análisis continuo del tráfico de red para identificar comportamientos anómalos. |
| **MDR** | *Managed Detection and Response* | Servicio de ciberseguridad tercerizado que provee monitoreo y respuesta a amenazas las 24/7. |
| **VPN** | *Virtual Private Network* | Red privada virtual; crea un túnel seguro y cifrado sobre una red pública como Internet. |
| **IAM** | *Identity and Access Management* | Marco de políticas y tecnologías para asegurar que los usuarios correctos tengan el acceso adecuado a los recursos. |
| **MFA** | *Multi-Factor Authentication* | Autenticación multifactor; requiere dos o más pruebas de identidad independientes para conceder acceso. |

---

## ☣️ 4. Ciberamenazas e Investigación de Incidentes

| Sigla | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| **CVE** | *Common Vulnerabilities and Exposures* | Diccionario público de vulnerabilidades de seguridad conocidas en software y hardware. |
| **IOC** | *Indicator of Compromise* | Indicador de Compromiso; evidencia forense (hash, IP, dominio) que sugiere que un sistema fue comprometido. |
| **IOA** | *Indicator of Attack* | Indicador de Ataque; señales en tiempo real que se enfocan en la intención y el comportamiento activo del atacante. |
| **DoS** | *Denial of Service* | Ataque de denegación de servicio que busca inhabilitar un recurso saturándolo con peticiones. |
| **DDoS** | *Distributed Denial of Service* | Ataque DoS realizado de manera distribuida desde múltiples fuentes comprometidas (botnets). |
| **APT** | *Advanced Persistent Threat* | Amenaza Persistente Avanzada; grupo de atacantes altamente capacitado y financiado (generalmente estados-nación). |

---

## 🐧 5. Administración de Linux y Línea de Comandos

| Término | Nombre Completo | Descripción |
| :--- | :--- | :--- |
| **CLI** | *Command Line Interface* | Interfaz de línea de comandos; forma de interactuar con el sistema operativo escribiendo comandos en la terminal. |
| **Shell** | *Shell* | Intérprete de comandos que recibe lo que escribes y lo ejecuta (ej. `bash`, `sh`, `zsh`). |
| **Bash** | *Bourne Again Shell* | La shell más utilizada en Linux y macOS; es el intérprete por defecto en la mayoría de distribuciones. |
| **Kernel** | *Kernel* | Núcleo del sistema operativo; gestiona hardware, memoria y procesos. Linux es un kernel. |
| **Distribución** | *Linux Distribution* | Conjunto de Linux + software empaquetado (Ubuntu, Debian, Kali, CentOS, etc.). El kernel es el motor; la distribución es el auto. |
| **FHS** | *Filesystem Hierarchy Standard* | Estándar que define la estructura de directorios de Linux (`/etc`, `/home`, `/var/log`, `/tmp`, etc.). |
| **root** | *Root / Superusuario* | Usuario administrador con control total del sistema (UID 0). |
| **sudo** | *Super User DO* | Comando que permite ejecutar acciones con privilegios de administrador de forma temporal y controlada. |
| **grep** | *Global Regular Expression Print* | Herramienta para buscar patrones de texto dentro de archivos o salidas de otros comandos; esencial para analizar logs. |
| **pipe** | *Pipe (|)* | Operador que conecta la salida de un comando con la entrada de otro (ej. `cat log \| grep "Failed"`). |
| **PID** | *Process Identifier* | Identificador numérico único de cada proceso en ejecución. |
| **Daemon** | *Daemon* | Proceso que corre en segundo plano prestando un servicio (ej. `sshd`, `nginx`, `systemd`). |
| **chmod** | *Change Mode* | Comando para cambiar los permisos (`rwx`) de archivos y directorios. |
| **chown** | *Change Owner* | Comando para cambiar el propietario (y grupo) de un archivo o directorio. |
| **setuid** | *Set User ID* | Bit especial de permisos que hace que un ejecutable corra con los privilegios de su propietario (potencial riesgo de escalada). |
| **umask** | *User file creation mask* | Define los permisos por defecto que reciben los archivos y directorios recién creados. |
| **Syslog** | *System Logging Protocol* | Protocolo estándar (UDP 514) para enviar y centralizar logs de sistemas y dispositivos; clave para SIEM. |
