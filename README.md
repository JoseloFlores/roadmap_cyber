# 🛡️ SOC Analyst Journey: Ruta de Aprendizaje de Cero a L1

<p align="center">
  <img src="https://img.shields.io/badge/Curso-Ciberseguridad%20Defensiva-blue?style=for-the-badge&logo=shield" alt="Curso Badge">
  <img src="https://img.shields.io/badge/Fase-1%20Fundamentos-green?style=for-the-badge&logo=read-the-docs" alt="Fase Badge">
  <img src="https://img.shields.io/badge/Contribuciones-Abiertas-orange?style=for-the-badge&logo=git" alt="Contribuciones Badge">
</p>

---

## 📖 Sobre el Proyecto

Este repositorio contiene una **hoja de ruta estructurada y metódica de 24 semanas (6 meses)** diseñada específicamente para cualquier persona que desee ingresar al mundo de la ciberseguridad defensiva y convertirse en un **Analista SOC (Security Operations Center) Nivel 1** altamente empleable. 

Aquí encontrarás apuntes limpios, recursos teóricos, laboratorios paso a paso, glosarios técnicos y guías prácticas basadas en estándares de documentación reales de la industria.

---

## 🗺️ Estructura del Road Map (24 Semanas)

El camino está dividido en **6 fases de aprendizaje progresivo**:

```mermaid
graph TD
    F1[Fase 1: Fundamentos <br> Semanas 1-4] --> F2[Fase 2: Analista SOC <br> Semanas 5-8]
    F2 --> F3[Fase 3: Threat Detection <br> Semanas 9-12]
    F3 --> F4[Fase 4: Blue Team <br> Semanas 13-16]
    F4 --> F5[Fase 5: Experiencia Real <br> Semanas 17-20]
    F5 --> F6[Fase 6: Empleabilidad <br> Semanas 21-24]
```

### 🗓️ Resumen de las Fases

| Fase | Semanas | Enfoque Principal | Documentación Principal |
| :--- | :--- | :--- | :--- |
| **Fase 1: Fundamentos** | 1 - 4 | Redes, Protocolos, Administración de Linux y Windows | [Ver Hoja de Ruta](file:///home/jo/Documentos/road_map_cyber/SOC_Hoja_De_Ruta.md#fase-1-fundamentos-semanas-1-a-4) |
| **Fase 2: Analista SOC** | 5 - 8 | Gestión de Logs, SIEM (Splunk) y Sysmon | [Ver Hoja de Ruta](file:///home/jo/Documentos/road_map_cyber/SOC_Hoja_De_Ruta.md#fase-2-analista-soc-semanas-5-a-8) |
| **Fase 3: Threat Detection** | 9 - 12 | MITRE ATT&CK, Malware, Phishing y OSINT | [Ver Hoja de Ruta](file:///home/jo/Documentos/road_map_cyber/SOC_Hoja_De_Ruta.md#fase-3-threat-detection-semanas-9-a-12) |
| **Fase 4: Blue Team** | 13 - 16 | Security Onion, IDS/IPS (Suricata) y Zeek | [Ver Hoja de Ruta](file:///home/jo/Documentos/road_map_cyber/SOC_Hoja_De_Ruta.md#fase-4-blue-team-semanas-13-a-16) |
| **Fase 5: Experiencia Real** | 17 - 20 | TryHackMe, CyberDefenders y Hack The Box | [Ver Hoja de Ruta](file:///home/jo/Documentos/road_map_cyber/SOC_Hoja_De_Ruta.md#fase-5-experiencia-practica-y-plataformas-semanas-17-a-20) |
| **Fase 6: Empleabilidad** | 21 - 24 | LinkedIn, Portafolio en GitHub y Preparación Técnica | [Ver Hoja de Ruta](file:///home/jo/Documentos/road_map_cyber/SOC_Hoja_De_Ruta.md#fase-6-marca-personal-y-empleabilidad-semanas-21-a-24) |

---

## 🗂️ Contenido de la Semana 1: Redes I

Los módulos teóricos y prácticos correspondientes a la **Semana 1** se encuentran organizados y limpios para su fácil lectura:

1. **[01. Modelo OSI](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/01_Modelo_OSI.md)**: El modelo teórico de interconexión de sistemas abiertos y su aplicación de seguridad.
2. **[02. Modelo TCP/IP](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/02_Modelo_TCP_IP.md)**: El modelo práctico sobre el que funciona Internet.
3. **[03. IP Pública y Privada](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/03_IP_Publica_Privada.md)**: Tipos de direccionamiento e implicaciones en el análisis SOC.
4. **[04. Máscaras de Subred](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/04_Mascaras.md)**: Identificación de Redes y Hosts.
5. **[05. Subredes](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/05_Subredes.md)**: Fundamentos de subnetting y segmentación de red.
6. **[06. Puerta de Enlace (Gateway)](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/06_Gateway.md)**: El punto de salida de la red local.
7. **[07. NAT](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_1_Redes_I/07_NAT.md)**: Traducción de Direcciones de Red.

* **[📖 Glosario de Términos y Siglas Críticas del SOC](file:///home/jo/Documentos/road_map_cyber/GLOSARIO.md)**: Cheat-sheet rápido de siglas esenciales de redes, herramientas y amenazas.

---

## 🗂️ Contenido de la Semana 2: Redes II

Los módulos teóricos correspondientes a la **Semana 2** se encuentran organizados y limpios para su fácil lectura:

1. **[Módulo 8. UDP](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_2_Redes_II/9%20_Semana_2_Redes_2_UDP.md)**: El protocolo de transporte rápido, sin conexión y sin garantías.
2. **[Módulo 9. Puertos](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_2_Redes_II/10%20-%20Semana%202%20Redes%202%20-%20Puertos.%20By%20gpt.md)**: Identificación de servicios y aplicaciones dentro de un dispositivo.
3. **[Módulo 10. TCP](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_2_Redes_II/11%20-%20Semana%202%20Redes%202%20-%20TCP.%20By%20gpt.md)**: El protocolo confiable y orientado a conexión (Three-Way Handshake).
4. **[Módulo 11. DHCP](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_2_Redes_II/12%20-%20Semana%202%20Redes%202%20-%20DHCP.%20By%20gpt.md)**: Asignación automática de IP, máscara, gateway y DNS (proceso DORA).
5. **[Módulo 12. HTTP y HTTPS](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_2_Redes_II/13%20-%20Semana%202%20Redes%202%20-%20HTTP_HTTPS.%20By%20gpt.md)**: Métodos, códigos de estado y la web cifrada.
6. **[Módulo 13. DNS](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_2_Redes_II/10%20-%20Semana%202%20Redes%202%20-%20DNS.%20By%20gpt.md)**: La agenda telefónica de Internet y sus ataques (DGA, tunneling, spoofing).

---

## 🗂️ Contenido de la Semana 3: Linux

Los módulos teóricos y el laboratorio correspondientes a la **Semana 3** se encuentran organizados y listos para practicar:

1. **[Módulo 14. Introducción a Linux y la Terminal (CLI)](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/01%20-%20Semana%203%20Linux%20-%20Introduccion%20CLI.%20By%20gpt.md)**: Kernel, distribuciones, shell y primeros comandos (`ls`, `cd`, `pwd`, `cat`, `tail`).
2. **[Módulo 15. Estructura del Sistema de Archivos (FHS)](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/02%20-%20Semana%203%20Linux%20-%20Estructura%20de%20Archivos%20FHS.%20By%20gpt.md)**: El árbol de directorios y dónde vive la evidencia (`/etc`, `/var/log`, `/tmp`).
3. **[Módulo 16. Permisos de Archivos (rwx)](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/03%20-%20Semana%203%20Linux%20-%20Permisos.%20By%20gpt.md)**: `chmod`, `chown`, notación octal y bits especiales.
4. **[Módulo 17. Gestión de Usuarios y Grupos](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/04%20-%20Semana%203%20Linux%20-%20Usuarios%20y%20Grupos.%20By%20gpt.md)**: `/etc/passwd`, `/etc/shadow`, `sudo` y detección de cuentas sospechosas.
5. **[Módulo 18. Gestión de Procesos](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/05%20-%20Semana%203%20Linux%20-%20Procesos.%20By%20gpt.md)**: `ps`, `top`, `kill`, señales y detección de procesos maliciosos.
6. **[Módulo 19. grep, Pipes y Análisis de Logs](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/06%20-%20Semana%203%20Linux%20-%20grep%20y%20Analisis%20de%20Logs.%20By%20gpt.md)**: Filtros avanzados y detección de fuerza bruta en `/var/log/auth.log`.
7. **[Módulo 20. Laboratorio Práctico de Linux](file:///home/jo/Documentos/road_map_cyber/Fase_1_Fundamentos/Semana_3_Linux/07%20-%20Semana%203%20Linux%20-%20Laboratorio%20Practico.%20By%20gpt.md)**: Guía paso a paso: usuarios, permisos restrictivos y monitoreo de logs con `tail -f`.

---

## 📚 Recursos PDF Incluidos

En la carpeta **[Recursos/](file:///home/jo/Documentos/road_map_cyber/Recursos/)** encontrarás documentación complementaria en formato PDF:
* **[Guía para principiantes de Wazuh](file:///home/jo/Documentos/road_map_cyber/Recursos/Guia-Wazuh-Principiantes.pdf)**: Guía práctica para comprender y configurar el agente EDR/SIEM de Wazuh.
* **[Creando máquina virtual](file:///home/jo/Documentos/road_map_cyber/Recursos/Creando_maquina_virtual.pdf)**: Guía paso a paso para el aprovisionamiento de tu hipervisor y laboratorios de pruebas.
* **[Manual de Auditoría](file:///home/jo/Documentos/road_map_cyber/Recursos/auditoria.pdf)**: Conceptos y directrices de auditoría de sistemas.

---

## 👥 Colaboradores y Créditos

Este proyecto es posible gracias al valioso aporte de los siguientes colaboradores:

| Colaborador | Rol / Contribución | GitHub |
| :--- | :--- | :--- |
| <img src="https://github.com/identicons/user.png" width="40" height="40" style="border-radius:50%"/> <br> **[Nombre Colaborador 1]** | Liderazgo del Roadmap / Redacción de Apuntes | [@colaborador1](https://github.com/github_username_1) |
| <img src="https://github.com/identicons/user2.png" width="40" height="40" style="border-radius:50%"/> <br> **[Nombre Colaborador 2]** | Diseño del Repositorio / Laboratorios Prácticos | [@colaborador2](https://github.com/github_username_2) |
| <img src="https://avatars.githubusercontent.com/u/70613354?v=4" width="40" height="40" style="border-radius:50%"/> <br> **[Jo!]** | Documentacion/ Revisión Técnica | [@Jo!](https://github.com/JoseloFlores) |

> 💡 *Si deseas aparecer en esta sección, lee las instrucciones de contribución a continuación.*

---

## 🤝 ¿Cómo Contribuir?

1. Haz un **Fork** del repositorio.
2. Crea una rama para tu característica: `git checkout -b feature/NuevaSeccion`.
3. Haz tus cambios respetando los estándares de formato y documentación.
4. Envía tu **Pull Request** detallando tus adiciones o correcciones.
