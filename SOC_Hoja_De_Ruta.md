# 🗺️ Hoja de Ruta: De Cero a Analista SOC L1
> **Objetivo primordial:** Convertirte en un candidato SOC L1 técnico, autónomo y altamente empleable en un periodo de **24 semanas (6 meses)**.  
> **Dedicación sugerida:** ~2 horas por día de lunes a viernes, y ~4 horas diarias los fines de semana.

---

## 🚀 FASE 1: Fundamentos (Semanas 1 a 4)

### 📂 Semana 1 - Redes I
* **Teoría:**
  * Modelo OSI (Capas 1-7)
  * TCP/IP
  * Direccionamiento IP (Público y Privado)
  * Máscaras de red
  * Subredes
  * Puerta de enlace (Gateway)
  * NAT (Network Address Translation)
* **Laboratorio Práctico:**
  * Instalar **VirtualBox** o **VMware**
  * Crear y configurar una VM con **Windows 10**
  * Crear y configurar una VM con **Ubuntu**
* **Preguntas a Responder (Meta Semanal):**
  * ¿Qué ocurre detalladamente cuando escribo `google.com` en mi navegador?
  * ¿Qué es una dirección IP y cómo se diferencia de una MAC?
  * ¿Cuál es la función exacta de un router en la red?
* **🎯 Meta:** Explicar con tus propias palabras el recorrido completo de un paquete de datos desde tu PC hasta un servidor web externo.

---

### 📂 Semana 2 - Redes II
* **Teoría:**
  * Protocolos de transporte (TCP vs UDP)
  * Puertos de red comunes (22, 53, 80, 443, etc.)
  * Funcionamiento de DNS (Domain Name System)
  * Funcionamiento de DHCP (Dynamic Host Configuration Protocol)
  * Protocolos HTTP y HTTPS
* **Laboratorio Práctico:**
  * Instalar **Wireshark** en tu máquina virtual
  * Capturar tráfico web básico
  * Capturar y analizar resoluciones DNS
* **🎯 Meta (Identificar en Capturas):**
  * Una consulta (Query) y respuesta DNS
  * El saludo de tres vías (TCP Three-Way Handshake)
  * Una petición HTTP GET
  * Entender la diferencia visual entre tráfico HTTP y HTTPS cifrado

---

### 📂 Semana 3 - Linux
* **Teoría:**
  * Estructura del sistema de archivos Linux (FHS)
  * Permisos de archivos y directorios (`rwx`)
  * Gestión de usuarios y grupos
  * Gestión de procesos
* **Comandos Clave a Dominar:**
  * `ls`, `cd`, `pwd`, `mkdir`, `rm`
  * `chmod`, `chown`
  * `grep`, `cat`, `tail`, `head`
  * `ps`, `top`
* **Laboratorio Práctico:**
  * Crear múltiples usuarios y grupos
  * Configurar permisos restrictivos en carpetas del sistema
  * Realizar búsquedas avanzadas de logs usando filtros con `grep` y `tail -f`
* **🎯 Meta:** Moverte con total soltura a través de la terminal (CLI) de Linux sin depender de una interfaz gráfica.

---

### 📂 Semana 4 - Windows
* **Teoría:**
  * Registro de eventos de Windows (Event Viewer)
  * Servicios y procesos del sistema
  * Gestión de usuarios y grupos locales
  * Introducción a PowerShell
* **Laboratorio Práctico:**
  * Auditar e interpretar logs en el Event Viewer:
    * Inicios de sesión exitosos y fallidos (Event ID 4624 y 4625)
    * Logouts
    * Errores críticos del sistema
* **🎯 Meta:** Entender e interpretar los principales eventos de seguridad del ecosistema Windows.

---

## 🔍 FASE 2: Analista SOC (Semanas 5 a 8)

### 📂 Semana 5 - Gestión de Logs
* **Teoría:**
  * ¿Qué es un log y por qué es la materia prima del SOC?
  * Tipos de logs (Seguridad, Aplicación, Sistema, Auditoría)
  * Eventos en Windows (Event Log)
  * Protocolo Syslog en Linux
* **Laboratorio Práctico:**
  * Analizar de forma manual logs de autenticación
  * Detectar patrones de:
    * Inicios de sesión inusuales
    * Fallas de login repetitivas (fuerza bruta)
    * Creación y modificación de usuarios administradores
* **🎯 Meta:** Interpretar logs nativos directamente en formato raw (texto plano) sin asistencia de herramientas automatizadas.

---

### 📂 Semana 6 - Introducción a Splunk
* **Teoría:**
  * Conceptos básicos de Splunk: Indexes, Source, SourceType, Host
  * Búsquedas básicas usando Splunk Search Processing Language (SPL)
  * Creación de visualizaciones y paneles básicos
* **Laboratorio Práctico:**
  * Instalar **Splunk Free** en tu máquina virtual
  * Importar logs de ejemplo (logs de Windows o Syslog)
  * Realizar búsquedas básicas:
    * `index=*`
    * `host=*`
    * `source=*`
* **🎯 Meta:** Localizar y filtrar eventos específicos rápidamente utilizando SPL.

---

### 📂 Semana 7 - Splunk Avanzado
* **Teoría:**
  * Comandos de agregación: `stats`, `chart`, `timechart`
  * Creación y configuración de alertas automáticas basadas en umbrales
* **Laboratorio Práctico:**
  * Diseñar y estructurar dos Dashboards clave:
    1. **Dashboard de Accesos:** Intentos exitosos vs fallidos, geolocalización de IPs.
    2. **Dashboard de Errores/Alertas:** Errores del sistema, picos de tráfico inusual.
* **🎯 Meta:** Construir visualizaciones complejas y útiles para el monitoreo en tiempo real.

---

### 📂 Semana 8 - Sysmon (System Monitor)
* **Teoría:**
  * ¿Qué es Sysmon y por qué complementa a los logs nativos de Windows?
  * Estructura de eventos críticos de Sysmon:
    * `Event ID 1`: Creación de Procesos (Process Creation)
    * `Event ID 3`: Conexión de Red (Network Connection)
    * `Event ID 7`: Carga de Módulo (Image Loaded)
    * `Event ID 11`: Creación de Archivos (File Created)
    * `Event ID 22`: Consulta DNS (DNS Query)
* **Laboratorio Práctico:**
  * Instalar Sysmon en Windows Server o Windows 10
  * Aplicar la plantilla de configuración de **SwiftOnSecurity**
  * Simular ejecuciones sospechosas y ver cómo las registra Sysmon
* **🎯 Meta:** Detectar actividad anómala o sospechosa analizando la telemetría detallada de procesos y red.

---

## 🎯 FASE 3: Threat Detection (Semanas 9 a 12)

### 📂 Semana 9 - MITRE ATT&CK
* **Teoría:**
  * Entender la matriz MITRE ATT&CK
  * Diferencia e importancia de:
    * **Tactics (Tácticas):** El objetivo del atacante (por qué lo hace)
    * **Techniques (Técnicas):** El método empleado (cómo lo hace)
    * **Procedures (Procedimientos):** La implementación específica del software/actor de amenaza (APT)
* **🎯 Meta:** Correlacionar un log de evento sospechoso (como la ejecución de PowerShell con comandos codificados) con una técnica y táctica específica de la matriz MITRE ATT&CK.

---

### 📂 Semana 10 - Fundamentos de Malware
* **Teoría:**
  * Tipos de software malicioso: Troyanos, RATs, Gusanos, Ransomware, Spyware
  * Indicadores de Compromiso básicos (Hashes MD5/SHA256, IPs, Dominios)
* **Herramientas a Utilizar:**
  * **VirusTotal**
  * Sandboxes de análisis dinámico (Any.run, Hybrid Analysis)
* **🎯 Meta:** Analizar y diagnosticar una muestra potencial de malware utilizando recursos de OSINT.

---

### 📂 Semana 11 - Phishing y Seguridad en Correo
* **Teoría:**
  * Anatomía de un correo de phishing
  * Cabeceras de correo electrónico (Email Headers)
  * Protocolos de autenticación de correo:
    * **SPF (Sender Policy Framework)**
    * **DKIM (DomainKeys Identified Mail)**
    * **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**
* **Laboratorio Práctico:**
  * Analizar las cabeceras de un correo sospechoso
  * Verificar si los registros SPF, DKIM y DMARC son válidos para el dominio remitente
* **🎯 Meta:** Determinar la legitimidad de un correo y rastrear su servidor de origen.

---

### 📂 Semana 12 - IOC Hunting & OSINT
* **Teoría:**
  * Concepto de Indicador de Compromiso (IOC)
  * La Pirámide del Dolor (Pyramid of Pain) de David Bianco
  * Uso de herramientas OSINT
* **Herramientas de Investigación:**
  * **VirusTotal**
  * **AbuseIPDB**
  * AlienVault OTX (Open Threat Exchange)
* **🎯 Meta:** Investigar una alerta de seguridad de extremo a extremo, determinando la reputación de los artefactos involucrados (Hashes, IPs, Dominios).

---

## 🛡️ FASE 4: Blue Team & Mini-SOC (Semanas 13 a 16)

### 📂 Semana 13 - Security Onion
* **Teoría:**
  * Arquitectura de Security Onion
  * Componentes incluidos: Elastic Stack (ELK), Suricata, Zeek, Wazuh
* **Laboratorio Práctico:**
  * Instalar **Security Onion** en modo de evaluación/monitoreo en tu entorno de red
* **🎯 Meta:** Configurar y poner en marcha tu propio mini-SOC para capturar tráfico de red local.

---

### 📂 Semana 14 - IDS/IPS con Suricata
* **Teoría:**
  * Detección basada en firmas
  * Sintaxis y estructura de las reglas de **Suricata**
  * Gestión de alertas y falsos positivos
* **Laboratorio Práctico:**
  * Crear y cargar una regla personalizada en Suricata para detectar tráfico sospechoso
  * Lanzar la prueba y verificar que dispare la alerta en Security Onion
* **🎯 Meta:** Escribir reglas básicas de detección e interpretar logs de alertas IDS.

---

### 📂 Semana 15 - Análisis de Tráfico con Zeek
* **Teoría:**
  * Análisis de tráfico basado en metadatos y comportamiento
  * Registro estructurado de Zeek (conn.log, dns.log, http.log, ssl.log)
* **Laboratorio Práctico:**
  * Investigar una captura de red (PCAP) utilizando exclusivamente los logs generados por Zeek
* **🎯 Meta:** Reconstruir la actividad de red de un equipo comprometido sin abrir el PCAP en Wireshark.

---

### 📂 Semana 16 - Análisis de Casos de Estudio Reales
* **Práctica:**
  * Resolver laboratorios que integren múltiples disciplinas:
    * Infección por Malware y su rastro en logs de red (Zeek/Suricata)
    * Campañas de Phishing que descargan cargadores de malware (Loaders)
    * Intentos de fuerza bruta exitosos seguidos de movimiento lateral
* **🎯 Meta:** Desarrollar el pensamiento crítico e investigativo necesario para un Analista SOC en el día a día.

---

## 🏆 FASE 5: Experiencia Práctica y Plataformas (Semanas 17 a 20)

### 📂 Semana 17 y 18 - TryHackMe
* **Plataforma:** [TryHackMe](https://tryhackme.com/)
* **Ruta de Aprendizaje (Path):**
  * **SOC Level 1** (Completar módulos de redes, SIEM, análisis de endpoints y phishing)

### 📂 Semana 19 - CyberDefenders
* **Plataforma:** [CyberDefenders](https://cyberdefenders.org/)
* **Laboratorios Clave a Resolver:**
  * **BlueYard** (Investigación SIEM/Splunk)
  * **PsExec Hunt** (Detección de movimientos laterales con herramientas de Sysinternals)

### 📂 Semana 20 - Hack The Box
* **Plataforma:** [Hack The Box](https://www.hackthebox.com/)
* **Ruta de Aprendizaje:**
  * **SOC Analyst Path** (Prácticas avanzadas y resolución de desafíos de defensa)

---

## 💼 FASE 6: Marca Personal y Empleabilidad (Semanas 21 a 24)

### 📂 Semana 21 - LinkedIn Profesional
* **Acciones:**
  * Configurar tu perfil enfocado en ciberseguridad defensiva.
  * **Título sugerido:** `Junior SOC Analyst | Splunk | SIEM | Incident Response | Blue Team`
  * Redactar una sección "Acerca de" que destaque tus laboratorios prácticos y tu pasión por la investigación.

### 📂 Semana 22 - GitHub como Portafolio
* **Acciones:**
  * Crear un repositorio dedicado para documentar tu trayectoria.
  * Subir:
    * Dashboards de Splunk que hayas diseñado.
    * Writeups detallados de salas de TryHackMe/CyberDefenders (respetando las políticas de writeups).
    * Tu documentación de laboratorios personales.

### 📂 Semana 23 - Simulación de Entrevistas Técnicas
* **Preguntas Clave a Preparar:**
  * Diferencias detalladas entre TCP y UDP.
  * ¿Cómo funciona DNS y qué registros existen (A, AAAA, MX, TXT)?
  * ¿Qué Event IDs de Windows/Sysmon monitorearías para detectar malware?
  * Explica qué es un IOC y da 3 ejemplos.
  * ¿Cómo investigarías una alerta de phishing?

### 📂 Semana 24 - Postulaciones Activas
* **Perfiles Objetivo:**
  * `SOC Analyst L1`
  * `Junior Security Analyst`
  * `Cybersecurity Analyst (Blue Team) Jr`
* **Métrica:** Enviar un mínimo de **10 postulaciones enfocadas** por semana.

---

## 🛡️ Proyecto Final (El mayor diferenciador de tu CV)
> Al finalizar las 24 semanas, debes construir y documentar un **Laboratorio de Detección de Ataques Doméstico**.

### Componentes del Laboratorio:
- **Endpoints:** Windows 10 (con Sysmon configurado) y Ubuntu.
- **Atacante:** Kali Linux.
- **SIEM / Analizador:** Splunk Enterprise (Free) o Security Onion.
- **Herramientas de Red:** Wireshark y Suricata.

### Entregable del Proyecto en GitHub:
1. **Instalación:** Documentar paso a paso la configuración de la topología de red.
2. **Recolección:** Explicar cómo centralizaste los logs (Windows Event Logs + Sysmon -> Splunk).
3. **Simulación:** Ejecutar ataques controlados (por ejemplo, escaneo Nmap, fuerza bruta SSH, ejecución de PowerShell malicioso).
4. **Investigación:** Mostrar capturas de pantalla de los logs que registraron el ataque en Splunk.
5. **Evidencias:** Compartir las consultas SPL utilizadas para hallar al atacante.
6. **Mitigación:** Documentar las acciones defensivas (reglas de firewall, desactivación de servicios, etc.) tomadas para contener la amenaza.

---

## 🤖 Cómo utilizar la Inteligencia Artificial a tu favor
Para cada semana de estudio, puedes interactuar con una IA utilizando los siguientes prompts:

1. **Clase y Explicación:**
   > *"Actúa como un instructor senior de SOC Analyst. Explícame el tema [Tema de la Semana] desde cero con analogías claras, ejemplos reales de la industria, preguntas típicas de entrevista y laboratorios prácticos paso a paso."*
2. **Simulación de Entrevista:**
   > *"Hazme una entrevista técnica estricta para un puesto SOC L1 enfocada en [Tema de la Semana]. Hazme una pregunta a la vez, espera a que responda y luego evalúa mi respuesta dándome feedback detallado."*
3. **Laboratorio Personalizado:**
   > *"Dame un ejercicio o laboratorio práctico que pueda montar en mi entorno virtual local para aplicar los conocimientos sobre [Tema de la Semana]."*
