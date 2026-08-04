
# Modelo OSI (Open Systems Interconnection)

El modelo de interconexión de sistemas abiertos (OSI) es un marco conceptual que divide las funciones de comunicaciones de red en siete capas. Proporciona un lenguaje universal para las redes informáticas, de modo que diversas tecnologías pueden comunicarse mediante protocolos o reglas de comunicación estándar.

## ¿Por qué es importante el modelo OSI?

*   **Comprensión compartida de sistemas complejos:** Los ingenieros pueden usar el modelo para organizar y modelar arquitecturas de sistemas en red complejas, separando la capa operativa de cada componente según su funcionalidad principal.
*   **Investigación y desarrollo más rápidos:** Permite a los ingenieros entender mejor su trabajo y desarrollar sistemas en red aprovechando una serie de procesos y protocolos repetibles.
*   **Estandarización flexible:** Estandariza el desarrollo de las comunicaciones de red sin especificar los protocolos exactos, sino las tareas que deben realizar. Abstrae los detalles para simplificar el diseño y el desarrollo.

## Las 7 Capas del Modelo OSI

El modelo fue desarrollado por la Organización Internacional de Normalización (ISO) y publicado en 1984.

### 1. Capa Física
Se refiere al medio de comunicación físico y a las tecnologías para transmitir datos a través de ese medio (señales digitales y electrónicas).
*   **Ejemplos de canales físicos:** Cables de fibra óptica, cableado de cobre, aire.
*   **Ejemplos de estándares:** Bluetooth, NFC, velocidades de transmisión de datos.

### 2. Capa de Enlace de Datos
Conecta dos máquinas a través de una red donde la capa física ya existe. Gestiona los marcos de datos (señales digitales encapsuladas en paquetes de datos), el control de flujo y el control de errores.
*   **Ejemplo de estándar:** Ethernet.
*   **Subcapas:** Capa de control de acceso a los medios (MAC) y Capa de control de enlace lógico (LLC).

### 3. Capa de Red
Se ocupa del enrutamiento, el reenvío y el direccionamiento a través de una red dispersa o múltiples redes conectadas. También puede gestionar el control de flujo.
*   **Protocolos principales (en Internet):** IPv4 e IPv6.

### 4. Capa de Transporte
Garantiza que los paquetes de datos lleguen en el orden correcto, sin pérdidas ni errores (o que se puedan recuperar). Se encarga del control de flujo y control de errores.
*   **Protocolos principales:**
    *   **TCP (Protocolo de Control de Transmisión):** Basado en conexiones, casi sin pérdidas (ideal para compartir archivos).
    *   **UDP (Protocolo de datagramas de usuario):** Sin conexiones, con pérdidas (ideal para streaming de vídeo).

### 5. Capa de Sesión
Responsable de la coordinación de la red entre dos aplicaciones independientes. Gestiona el inicio y el final de los conflictos de sincronización y conexión de una aplicación uno a uno.
*   **Protocolos comunes:** NFS (Sistema de archivos de red) y SMB (Bloque de mensajes del servidor).

### 6. Capa de Presentación
Se ocupa de la sintaxis de los datos para que las aplicaciones los envíen y consuman.
*   **Lenguajes de modelado comunes:** HTML, JSON, CSV.

### 7. Capa de Aplicación
Se refiere a la aplicación en sí y a sus métodos de comunicación estandarizados.
*   **Protocolos comunes:** HTTPS (navegadores), POP3 y SMTP (correo electrónico).

## ¿Cómo se produce la comunicación en el modelo OSI?

Las capas son independientes y solo conocen las interfaces para comunicarse con la capa superior e inferior. El proceso de envío de datos (de una aplicación a otra) es el siguiente:

1.  La capa de aplicación del remitente transfiere los datos a la capa inferior.
2.  Cada capa añade sus propios encabezados y direccionamientos antes de transmitir a la siguiente.
3.  Los datos descienden por las capas hasta transmitirse por el medio físico.
4.  En el extremo receptor, cada capa procesa los datos según los encabezados de su nivel.
5.  Los datos suben por las capas y se desempaquetan hasta llegar a la aplicación receptora.

## Alternativas al modelo OSI: El Modelo TCP/IP

Hoy en día, la alternativa principal (y más utilizada en la práctica para la estructura de Internet) es el modelo TCP/IP, que tiene cinco capas:

1.  Capa física
2.  Capa de enlace de datos
3.  Capa de red
4.  Capa de transporte
5.  Capa de aplicación

*Nota: El modelo OSI sigue siendo popular con fines educativos para describir las redes de forma holística.*
