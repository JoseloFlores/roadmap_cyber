Nmap es la herramienta estándar para exploración de red y auditorías de seguridad. Para entenderla sin abrumarte con el menú de ayuda, lo ideal es estructurar sus opciones según las **fases típicas de un escaneo** y aprender los **combos de comandos** más usados en el mundo real.

---

**Las Secciones Clave de Nmap**

* **Objetivo (Target Specification):** Define a *quién* vas a escanear (IPs, rangos, dominios o desde un archivo con `-iL`).
* **Descubrimiento (Host Discovery):** Determina *si el equipo está vivo*. Por defecto usa Pings, pero si hay un firewall bloqueándolos, usas **`-Pn`** para obligar a Nmap a escanear los puertos de todos modos.
* **Técnicas de Escaneo (Scan Techniques):** Define *cómo* se envían los paquetes.
* `-sS` (SYN Scan): El predeterminado (requiere root/sudo). Rápido y discreto porque no completa la conexión TCP (conexión a medias).
* `-sT` (Connect Scan): Completa la conexión TCP. Se usa si no tienes permisos de administrador.
* `-sU` (UDP Scan): Para servicios como DNS, DHCP o SNMP.


* **Puertos (Port Specification):** Por defecto evalúa los 1,000 puertos más comunes. Con `-p 1-65535` escaneas todo el rango, o con `-p 80,443,22` escaneas puertos específicos.
* **Detección de Servicios y SO:** **`-sV`** conecta a los puertos abiertos para identificar la versión exacta del programa (ej. Apache 2.4.41), y **`-O`** deduce el Sistema Operativo analizando la respuesta de los paquetes.
* **Scripts (NSE - `-sC` / `--script`):** Automatiza tareas con scripts en Lua (detectar vulnerabilidades, enumerar usuarios, etc.).
* **Rendimiento (Timing `-T0` a `-T5`):** Controla la velocidad. `-T4` es el estándar agresivo pero seguro para redes locales/laboratorios; `-T2` o menor se usa para no saturar enlaces o evitar alertas.
* **Evasión (Firewall/IDS):** Técnicas como fragmentar paquetes (`-f`), usar IPs falsas de señuelo (`-D`) o cambiar el puerto de origen (`-g 53`).
* **Salida (Output):** **`-oA nombre`** guarda los resultados en tres formatos simultáneamente (texto, XML y grepable).

---

**Combinaciones de Comandos Esenciales (Combos Reales)**

| Objetivo del Escaneo | Comando Recomendado | Explicación del Combo |
| --- | --- | --- |
| **1. Reconocimiento Rápido** | `nmap -sn 192.168.1.0/24` | Descubre qué equipos están encendidos en la red sin escanear sus puertos (*Ping sweep*). |
| **2. Escaneo Básico Rápido** | `nmap -T4 -F 192.168.1.50` | Escanea rápidamente (`-T4`) solo los 100 puertos más comunes (`-F`). |
| **3. Completo de Auditoría (El "All-in-One")** | `nmap -A -p- -T4 192.168.1.50` | **`-A`** activa detección de SO, versiones, scripts básicos y traceroute. **`-p-`** analiza los 65,535 puertos. |
| **4. Evasión de Bloqueo ICMP** | `nmap -Pn -sV -sC 192.168.1.50` | **`-Pn`** asume que el host está vivo aunque no responda pings. Agrega versiones (`-sV`) y scripts por defecto (`-sC`). |
| **5. Escaneo de Servicios UDP** | `nmap -sU --top-ports 20 192.168.1.50` | Mide los 20 puertos UDP más comunes (el escaneo UDP completo suele ser muy lento). |
| **6. Reporte Profesional** | `nmap -sV -sC -oA resultado_escaneo 192.168.1.50` | Extrae versiones y scripts, guardando la evidencia en todos los formatos de archivo (`-oA`). |

---

**Consejo Pro para Principiantes**

En lugar de memorizar opciones individuales, acostúmbrate a usar esta estructura mental:
`nmap [CÓMO ESCANEAR] [QUÉ PUERTOS] [QUÉ INFORMACIÓN EXTRAER] [DÓNDE GUARDAR] [OBJETIVO]`

*Ejemplo:* `sudo nmap -sS -p 80,443 -sV -oN web_scan.txt 10.10.10.10`