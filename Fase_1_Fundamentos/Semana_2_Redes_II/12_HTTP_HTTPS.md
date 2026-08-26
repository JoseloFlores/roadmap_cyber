**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Módulo 12 – <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Antes de comenzar**

Ya dominas:

- ✅ <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Públicas y Privadas

- ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>

- ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

- ✅ Máscaras

- ✅ Subredes

- ✅ <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

- ✅ <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>

- ✅ <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

- ✅ <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>

- ✅ Puertos

- ✅ <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

- ✅ <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>

Ahora llega el momento de estudiar los protocolos que más tráfico generan
en cualquier red: **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>** y **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**.

Casi todo lo que haces en Internet pasa por ellos.

- Ver un video.

- Enviar un correo.

- Comprar en línea.

- Iniciar sesión en una aplicación.

- Descargar un archivo.

Todo es tráfico web.

Como Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>, interpretar los métodos <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, los códigos de estado y
las cabeceras te permitirá leer los logs de proxy y firewall como si
fueran un libro abierto.

También es la base para detectar ataques a aplicaciones web como:

- SQL Injection (SQLi).

- Cross-Site Scripting (XSS).

- Phishing.

- Exfiltración de datos.

Sin esta base, no podrás entender gran parte de lo que verás en tu
primer día de trabajo en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**🎯 Objetivos de aprendizaje**

Al finalizar este módulo podrás:

- Comprender qué es <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y dónde trabaja en el modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

- Explicar cómo funciona una petición <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

- Conocer los métodos <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y su utilidad.

- Interpretar los códigos de estado más importantes.

- Reconocer las cabeceras clave en una investigación.

- Comprender qué es <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> y qué aporta <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>.

- Diferenciar <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> de <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> en una tabla.

- Saber qué información queda visible en el tráfico <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- Identificar ataques que aprovechan <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y las aplicaciones web.

- Aplicar estos conocimientos en casos reales de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**1. ¿Qué es <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>?**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> significa:

**HyperText Transfer Protocol**

**Protocolo de Transferencia de Hipertexto**

Es el protocolo encargado de transferir las páginas web.

- Texto.

- Imágenes.

- Videos.

- Archivos.

- Datos de formularios.

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> trabaja en la **Capa 7 (Aplicación)** del modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>:

7 Aplicación ← <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>

6 Presentación

5 Sesión

4 Transporte ← <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>

3 Red ← <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

2 Enlace

1 Física

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> se transmite normalmente sobre **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>**, porque necesita que los
datos lleguen completos y en orden.

Utiliza el puerto:

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80**

¿Recuerdas el puerto de <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>?

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443**

**Una característica clave:**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> viaja en **texto plano**.

Todo lo que se envía puede leerse si se intercepta.

- La URL.

- Las contraseñas.

- Los formularios.

- Las cookies.

Por eso <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> por sí solo no es seguro.

**2. ¿Cómo funciona una petición <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>?**

El funcionamiento es simple.

El cliente pide.

El servidor responde.

Visualmente:

Cliente

↓

Petición (request)

↓

Servidor

↓

Respuesta (response)

↓

Cliente

Cada petición tiene una estructura definida.

**1. Método**

Indica qué acción se quiere realizar.

Ejemplo:

GET

**2. Ruta (URL o recurso)**

Indica qué recurso se pide.

Ejemplo:

/index.html

**3. Versión del protocolo**

Ejemplo:

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>/1.1

**4. Cabeceras (headers)**

Información adicional sobre la petición.

Ejemplo:

Host: www.ejemplo.com

**5. Cuerpo (body)**

Datos que se envían en la petición.

No siempre está presente.

Ejemplo:

En un login, el cuerpo contiene el usuario y la contraseña.

**Analogía**

Piensa en un pedido en un restaurante.

El **método** es la acción que realizas:

¿Vas a pedir el menú?

¿Vas a devolver un plato?

El **código de estado** es la respuesta del cocinero y la administración:

¿Lo prepararon?

¿No existe ese plato?

¿No tienes permiso para entrar a la cocina?

¿Hubo un error en la cocina?

Las **cabeceras** son la orden con todos los detalles:

Nombre del cliente.

Mesa.

Alergias.

Tipo de entrega.

Todo junto forma una comunicación completa y entendible.

**3. Métodos <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**

Los métodos <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> indican la acción que el cliente quiere realizar.

| **Método** | **¿Qué hace?**                 | **Uso típico**              |
|------------|--------------------------------|-----------------------------|
| GET        | Solicita información.          | Abrir una página, buscar.   |
| POST       | Envía datos para procesar.     | Login, formularios, cargas. |
| PUT        | Crea o reemplaza un recurso.   | Actualizar un perfil.       |
| DELETE     | Elimina un recurso.            | Borrar un registro.         |
| HEAD       | Como GET, pero sin contenido.  | Verificar si existe un recurso. |
| OPTIONS    | Pregunta qué métodos permite.  | Consultas de API.           |

**GET**

Es el más común.

Se utiliza para leer o solicitar información.

Ejemplo:

GET /index.html

En logs verás:

GET

↓

www.ejemplo.com

↓

200

Interpretación:

Un cliente solicitó la página y el servidor respondió correctamente.

**POST**

Se utiliza para enviar datos.

Ejemplo:

POST /login

El cuerpo contiene:

usuario=ana

contraseña=xxxxxx

**¿Por qué un POST de login es interesante en logs?**

Porque indica un intento de autenticación.

Muchos ataques envían cientos o miles de POST a la misma ruta.

- Fuerza bruta contra un portal.

- Relleno de credenciales (credential stuffing).

- Intentos de acceso de cuentas robadas.

Si un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> ve muchos POST a /login desde la misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, hay que investigar.

**4. Respuesta <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y códigos de estado**

El servidor responde con un código de tres dígitos.

Ese código indica el resultado de la petición.

| **Código** | **Nombre**                    | **¿Qué significa?**                          |
|------------|-------------------------------|----------------------------------------------|
| 200        | OK                            | Éxito. La petición se completó.              |
| 201        | Created                       | Se creó un recurso nuevo.                    |
| 301        | Moved Permanently             | El recurso se movió a otra URL.              |
| 400        | Bad Request                   | La petición está mal formada.                |
| 401        | Unauthorized                  | Falta autenticación. ¿Quién eres?            |
| 403        | Forbidden                     | Autenticado, pero sin permiso. Acceso negado.|
| 404        | Not Found                     | El recurso no existe.                        |
| 500        | Internal Server Error         | Error interno del servidor.                  |
| 502        | Bad <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>                   | Un servidor intermedio recibió respuesta mala. |

**¿Qué indican en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

**200**

Actividad normal... o respuesta de éxito a un ataque.

**401**

El cliente no está autenticado.

**403**

El cliente está autenticado, pero no tiene permiso.

Puede ser un usuario bloqueado.

Puede ser un atacante probando áreas restringidas.

**404**

El recurso no existe.

Muchos atacantes hacen barridos buscando rutas como:

/admin

/backup.zip

/.env

Cada intento genera 404.

**500**

Error del servidor.

Puede ser un fallo técnico.

También puede ser el resultado de una **SQL Injection** que rompió la
consulta.

**502**

Error en un servidor intermedio (proxy, <a href="../../GLOSARIO.md#gateway" target="_blank">gateway</a>, balanceador).

**La combinación que debes vigilar:**

Muchos 200 después de muchos 401.

Interpretación posible:

Un atacante probó credenciales.

Falló varias veces (401).

Luego acertó (200).

Eso puede significar credenciales robadas en uso.

**5. Cabeceras importantes**

Las cabeceras (headers) son campos que acompañan a la petición o a la
respuesta.

Aportan contexto valioso en una investigación.

| **Cabecera**   | **¿Qué indica?**                                     |
|----------------|------------------------------------------------------|
| Host           | A qué sitio web se dirige la petición.               |
| User-Agent     | Qué navegador o herramienta la envió.                |
| Referer        | Desde qué página anterior se llegó.                  |
| Cookie         | Datos de sesión que envía el cliente.                |
| Authorization  | Credenciales enviadas por el cliente.                |
| Content-Type   | Qué tipo de datos contiene el cuerpo.                |
| Set-Cookie     | El servidor asigna una cookie al cliente.            |

**Host**

Indica el dominio al que se dirige la petición.

En un servidor pueden vivir varios sitios.

El Host dice cuál de ellos debe responder.

**User-Agent**

Identifica el navegador y el sistema operativo.

Ejemplo normal:

Mozilla/5.0 (Windows NT 10.0; Win64; x64)

Ejemplo sospechoso:

curl/7.68.0

python-requests/2.25.1

Cuando un log muestra **curl** o **python-requests**, no es un navegador.

Es una herramienta.

Muchos ataques automatizados dejan esta firma.

**Referer**

Muestra de qué página llegó el visitante.

Ayuda a reconstruir el recorrido de un atacante.

**Cookie**

Contiene datos de sesión.

Si un atacante roba una cookie de sesión, puede suplantar al usuario.

Este ataque se llama **Session Hijacking**.

**Authorization**

Contiene credenciales o tokens.

En logs, nunca deberían mostrarse los valores completos.

**Content-Type**

Indica el formato de los datos.

Ejemplos:

application/x-www-form-urlencoded

application/json

**Set-Cookie**

El servidor entrega una cookie al cliente.

Sirve para mantener la sesión activa.

**¿Por qué son clave en investigaciones?**

Porque permiten responder preguntas:

- ¿Qué navegador o herramienta generó el tráfico? (User-Agent)

- ¿Qué dominio se visitó? (Host)

- ¿Desde dónde se llegó? (Referer)

- ¿Hubo una sesión activa? (Cookie)

- ¿Qué tipo de datos se enviaron? (Content-Type)

Con esas respuestas construyes la historia del incidente.

**6. ¿Qué es <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>?**

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> significa:

**HyperText Transfer Protocol Secure**

Es <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, pero con una capa de seguridad añadida.

Utiliza:

**<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443**

**¿Qué aporta <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>?**

**Cifrado**

La información viaja ilegible para quien la intercepta.

**Integridad**

Los datos no pueden modificarse en el camino sin que se detecte.

**Autenticación del servidor**

El cliente puede verificar que está hablando con el servidor correcto.

**Analogía**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> sería enviar una postal.

Cualquiera que la maneje puede leerla.

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> sería enviar una caja sellada con candado.

Solo quien tiene la llave puede abrirla.

**7. <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> en resumen**

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> se apoya en un protocolo llamado **<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>**.

<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> significa:

**Transport Layer Security**

Es el sucesor del antiguo <a href="../../GLOSARIO.md#ssl" target="_blank">SSL</a>.

**¿Qué hace <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>?**

- Cifra los datos.

- Garantiza que no se modifiquen.

- Verifica la identidad del servidor.

**El handshake <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> en resumen**

Cuando el navegador se conecta a un sitio <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>:

Cliente

↓

"Hola, quiero conectarme. Versiones que soporto."

↓

Servidor

↓

"Hola. Uso esta versión. Este es mi certificado."

↓

Cliente

↓

"Verifico el certificado con una Autoridad Certificadora."

↓

Cliente

↓

"Intercambiamos claves para generar una clave de sesión."

↓

Servidor

↓

"Listo. Desde ahora todo cifrado."

↓

Datos cifrados

Simplificado, eso es el **<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> Handshake**.

No necesitas memorizar cada mensaje.

Lo importante para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>:

- El handshake ocurre **antes** de intercambiar datos.

- Es el momento en que se presenta el **certificado**.

- Al final se usa una **clave de sesión** compartida.

**Certificados**

Un certificado digital es como un documento de identidad del servidor.

Contiene:

- El dominio.

- La organización dueña.

- La Autoridad Certificadora que lo emitió.

- Fechas de validez.

**Autoridades Certificadoras (CA)**

Son organizaciones de confianza que emiten certificados.

Ejemplos:

- Let's Encrypt.

- DigiCert.

- GlobalSign.

Si un navegador confía en la CA, confía en el certificado que emitió.

**Aviso en el navegador:**

Si un certificado no es válido, el navegador muestra un aviso.

- Certificado vencido.

- Certificado para otro dominio.

- Certificado emitido por una CA no confiable.

Eso puede indicar un problema real o un ataque.

**8. <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> vs <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**

| **Característica** | **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**           | **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**                          |
|--------------------|--------------------|------------------------------------|
| Puerto             | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80             | <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443                            |
| Cifrado            | No (texto plano)   | Sí (<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>)                           |
| Integridad         | No                 | Sí                                 |
| Autenticación      | No                 | Sí (certificado del servidor)      |
| Capa adicional     | Ninguna            | <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>/<a href="../../GLOSARIO.md#ssl" target="_blank">SSL</a>                            |
| Capa <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>           | Aplicación         | Aplicación                         |
| Riesgo en <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>      | Alto (datos visibles) | Menor (contenido oculto)        |
| Uso recomendado    | Solo datos públicos | Todo lo demás                      |
| Ejemplos           | Sitios antiguos, pruebas | Banca, login, correo, comercio |

**En una frase:**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> es rápido y abierto.

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> es igual de funcional, pero protegido.

Por eso la web moderna exige <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> en todas partes.

**9. <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> en la práctica para <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> oculta el contenido.

Pero **no** oculta todo.

**Lo que SÍ es visible (metadatos):**

- <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen y de destino.

- Puertos (<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443).

- SNI / Host.

- Tamaño de los paquetes.

- Duración de la conexión.

- Horarios y volúmenes.

**SNI (Server Name Indication)**

Es un campo en el handshake <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>.

Indica a qué dominio se conecta el cliente.

Esto permite a un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> saber **a qué sitio** se conecta una máquina, incluso
con el tráfico cifrado.

**Lo que NO es visible:**

- El contenido de la página.

- Los datos de los formularios.

- Las contraseñas.

- Las cookies.

- La URL completa.

**Consecuencia para el analista:**

Puedes saber que un equipo habló con un dominio malicioso.

Pero no puedes leer qué se envió dentro.

Por eso los logs del proxy, del firewall y de los servidores web siguen
siendo esenciales.

**10. ¿Cómo aprovechan <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> los atacantes?**

**Ataque 1 – Intercepción y Sniffing en <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> plano**

El tráfico <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> viaja en texto plano.

Un atacante en la misma red puede capturarlo.

Herramientas como <a href="../../GLOSARIO.md#wireshark" target="_blank">Wireshark</a> permiten leer:

- URL visitadas.

- Formularios.

- Contraseñas.

- Cookies.

Si un sitio no cifra el login, el atacante captura las credenciales.

Atacante

↓

Captura de tráfico

↓

Lectura de credenciales en texto plano

↓

Acceso a la cuenta de la víctima

**Ataque 2 – SQL Injection (SQLi)**

El atacante envía código SQL malicioso en un formulario o en la URL.

Ejemplo:

Usuario:

admin' OR '1'='1

Si la aplicación lo procesa sin validar, puede:

- Acceder a la base de datos.

- Leer datos de otros usuarios.

- Borrar información.

- Obtener la lista de administradores.

Señales en logs:

- POST o GET con caracteres sospechosos como:

' OR

UNION SELECT

'; --

- Muchos errores 500 después de esas peticiones.

- Respuestas 200 con datos que no corresponden.

**Ataque 3 – Cross-Site Scripting (XSS)**

El atacante inyecta código JavaScript malicioso en una página web.

Cuando otro usuario visita la página, el código se ejecuta.

Puede:

- Robar cookies.

- Robar sesiones.

- Redirigir al usuario a sitios falsos.

- Realizar acciones en nombre del usuario.

Señales en logs:

- Peticiones que contienen:

<script>

onerror=

javascript:

- Referers inusuales.

**Ataque 4 – Phishing con páginas falsas**

El atacante crea una copia falsa de una página real.

Ejemplos:

- Un portal de banco.

- Una página de login de correo.

- Un formulario de una empresa.

La víctima ingresa sus datos.

Los datos van directo al atacante.

Señales en logs:

- Dominios parecidos al real:

banco.com

banco-seguro.com

banco.verificacion-acc.com

- Certificados inválidos o de reciente creación.

- Muchos POST a un formulario de login falso.

**Ataque 5 – <a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a> y downgrade a <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**

<a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a> significa:

**Man In The Middle**

**Hombre en el medio.**

El atacante se interpone entre la víctima y el servidor.

Víctima

↓

Atacante

↓

Servidor real

El atacante ve y modifica todo el tráfico.

**Downgrade a <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**

Consiste en obligar a la víctima a usar <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> en lugar de <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

Si el sitio acepta <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, el atacante puede redirigir la conexión
al enlace sin cifrar.

Ejemplo:

Víctima pide <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>

↓

Atacante responde "usa <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>"

↓

La víctima navega en texto plano

↓

El atacante lee todo

**Ataque 6 – Exfiltración por <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**

El malware roba datos.

Los datos se envían hacia el servidor del atacante.

Puede hacerse por:

- POST hacia dominios externos.

- GET con datos en la URL.

- Peticiones a dominios recién registrados.

- Tráfico <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> a dominios que normalmente no se usan en la organización.

Señales en logs:

- Volúmenes altos de datos hacia un solo dominio.

- Peticiones con parámetros codificados.

- Tráfico <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> hacia dominios con mala reputación.

**11. ¿Cómo defenderse?**

- Implementar un **<a href="../../GLOSARIO.md#waf" target="_blank">WAF</a> (Web Application Firewall)**.

- Validar y sanitizar todas las entradas del usuario.

- Usar consultas parametrizadas contra la base de datos.

- Activar **HSTS** en los servidores web.

- Redirigir todo el tráfico <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> a <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- Usar versiones modernas de **<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>**.

- Mantener certificados válidos y renovarlos a tiempo.

- Deshabilitar <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> antiguo (<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> 1.0 y 1.1).

- Monitorear los logs de los servidores web.

- Registrar los accesos a rutas sensibles.

- Bloquear dominios con mala reputación.

- Capacitar a los usuarios para detectar phishing.

**HSTS**

HSTS significa:

**<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> Strict Transport Security**

Es una cabecera que le dice al navegador:

"Este sitio solo se usa con <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>."

Así el navegador no acepta bajar a <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

Bloquea en gran parte el ataque de downgrade.

**12. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Caso 1**

Log del proxy:

User-Agent: curl/7.68.0

Método: GET

Destino: api-interna.ejemplo.com

Interpretación:

No es un navegador.

Es una herramienta automatizada.

¿Quién la usa?

¿Debería un equipo interno consultar esa API con curl?

Posible acceso automatizado indebido.

**Caso 2**

Log del servidor web:

POST /login

401

POST /login

401

POST /login

401

POST /login

200

Interpretación:

Muchos intentos fallidos.

Luego un acceso exitoso.

Posible ataque de fuerza bruta o de relleno de credenciales.

Investigar:

- La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen.

- El usuario que entró.

- Si hubo cambios posteriores en la cuenta.

**Caso 3**

Log del firewall:

GET /api/usuarios

GET /api/pedidos

GET /api/facturas

Desde la misma <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

En pocos segundos

Interpretación:

Un barrido de rutas de API.

El atacante está probando endpoints para encontrar información.

Muchos generarán 404.

Algunos pueden responder 200 si la API no está protegida.

**Caso 4**

Log del proxy:

Tráfico <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> (sin cifrar)

Dominio: descargas-rapidas-files.xyz

Equipo: PC-CONTABILIDAD

Interpretación:

Un equipo navega en <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> hacia un dominio desconocido.

Sin cifrado, todos los datos viajan visibles.

Dominio reciente + tráfico <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> = posible malware o phishing.

Investigar el proceso que generó la conexión.

**Caso 5**

Log del proxy:

POST hacia dominio externo

Equipo: PC-SERVIDOR-ARCHIVOS

Volumen: 5 GB en 2 horas

Destino: almacenamiento-externo-xyz.com

Interpretación:

Un servidor interno envió gran volumen de datos hacia un dominio externo.

Patrón típico de **exfiltración de datos**.

Investigar:

- Qué aplicación generó el tráfico.

- Si el destino es legítimo.

- Si hay movimiento lateral previo.

**13. Lo que esperan de un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**

Cuando veas un log como:

Origen:

192.168.10.45

↓

Método:

POST

↓

Ruta:

/login

↓

Respuesta:

401

↓

Repetido 300 veces

Debes hacerte estas preguntas:

- ¿Qué método se está usando? POST, enviando datos.

- ¿Qué código devuelve? 401, autenticación fallida.

- ¿Qué cabecera llama la atención? User-Agent, Cookie.

- ¿A qué dominio se dirige? ¿Es legítimo?

- ¿El volumen es normal? ¿300 intentos son habituales?

Esa cadena de preguntas:

**¿Qué método?**

**¿Qué código?**

**¿Qué cabecera?**

**¿A qué dominio?**

**¿El volumen es normal?**

Es exactamente lo que se espera de ti en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1.

**14. Resumen**

**<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**

- Protocolo de transferencia de hipertexto.

- Capa 7 (Aplicación).

- <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80.

- Texto plano.

- Métodos: GET, POST, PUT, DELETE, HEAD, OPTIONS.

- Códigos: 200, 201, 301, 400, 401, 403, 404, 500, 502.

- Cabeceras: Host, User-Agent, Referer, Cookie, Authorization,
  Content-Type, Set-Cookie.

**<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**

- <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> + <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>.

- <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443.

- Cifra el contenido.

- Verifica la identidad del servidor con certificados.

- En <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>: solo ves metadatos (<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, puerto, SNI, tamaño).

**Riesgos principales**

- Intercepción en <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> plano.

- SQL Injection.

- XSS.

- Phishing.

- <a href="../../GLOSARIO.md#mitm" target="_blank">MITM</a> y downgrade.

- Exfiltración por <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.

**Defensas principales**

- <a href="../../GLOSARIO.md#waf" target="_blank">WAF</a>.

- Validación de entradas.

- HSTS.

- <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> moderno.

- Redirección a <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- Monitoreo de logs web.

**🧠 Conceptos clave para memorizar**

| **Concepto**   | **Debes recordar**                                           |
|----------------|--------------------------------------------------------------|
| <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>           | Protocolo web en texto plano. <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80.                        |
| <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>          | <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> cifrado con <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>. <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443.                               |
| GET            | Solicita información.                                        |
| POST           | Envía datos. Clave para logins y ataques.                    |
| 200            | Éxito.                                                       |
| 401            | Falta autenticación. ¿Quién eres?                            |
| 403            | Sin permiso. Acceso denegado.                                |
| 404            | Recurso no encontrado.                                       |
| 500            | Error interno del servidor.                                  |
| 502            | Error de un servidor intermedio.                             |
| User-Agent     | Identifica navegador o herramienta.                          |
| Host / SNI     | Indican a qué dominio se conecta el cliente.                 |
| <a href="../../GLOSARIO.md#waf" target="_blank">WAF</a>            | Firewall de aplicaciones web.                                |
| HSTS           | Fuerza el uso de <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.                                      |
| <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>            | Capa de seguridad que cifra la web.                          |
| Certificado    | Documento de identidad digital del servidor.                 |
| SQL Injection  | Inyección de código SQL malicioso.                           |
| XSS            | Inyección de JavaScript malicioso.                           |

**🎓 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Cuando analices tráfico web, no leas los números sin contexto.

Razona sobre lo que significan.

Un **403** es un rechazo.

El servidor reconoció al cliente, pero le negó el acceso.

Un **500** es un error del servidor.

Puede ser un fallo técnico... o una consulta maliciosa que rompió el
sistema.

Un **200** después de muchos **401** puede indicar algo grave:

Credenciales robadas en uso.

Ejemplo:

200

↓

401

↓

401

↓

401

↓

401

↓

200

Esa secuencia merece una investigación completa:

- ¿Qué cuenta se usó?

- ¿La <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> es conocida?

- ¿Hubo cambios de contraseña después?

- ¿Qué datos se consultaron?

Y recuerda siempre esto:

**<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> plano = datos visibles.**

Si un sitio de login usa <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, las credenciales viajan a la vista de
cualquiera.

Por eso la regla de oro es:

- Si hay datos personales: <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- Si hay autenticación: <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- Si hay dinero: <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

- Si no hay razón para usar <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>: <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

Un analista que entiende <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> sabe qué buscar en los logs.

Y eso es la diferencia entre detectar un ataque a tiempo... o descubrirlo
demasiado tarde.

---

**📘 Carrera de Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Semana 2 – Redes II**

**Evaluación – Módulo 12: <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Instrucciones:** Responde las siguientes preguntas sin consultar el
material de estudio. Piensa como si estuvieras realizando una prueba
para ingresar a un **<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**. Encontrarás preguntas conceptuales y
casos prácticos basados en logs y alertas reales. Al finalizar encontrarás
las respuestas con su justificación.

**Pregunta 1**

¿Qué significa la sigla **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**?

**A)** HyperText Transfer Protocol

**B)** High Transfer Text Protocol

**C)** Hyperlink Transfer Process

**D)** Host Text Transfer Protocol

**Pregunta 2**

¿En qué puerto escucha normalmente el protocolo **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>**?

**A)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443

**B)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80

**C)** <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a> 53

**D)** <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 22

**Pregunta 3**

¿Cuál es la principal diferencia entre **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>** y **<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>**?

**A)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> es más rápido que <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> porque usa <a href="../../GLOSARIO.md#udp" target="_blank">UDP</a>.

**B)** <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> cifra la comunicación mediante <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>, mientras que <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> viaja
en texto plano.

**C)** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> solo se usa en redes privadas.

**D)** <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> no utiliza puertos.

**Pregunta 4**

Un analista observa en los logs muchos intentos de acceso a un portal de
login.

¿Qué **método <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>** es el más probable en ese tipo de registros?

**A)** GET

**B)** DELETE

**C)** POST

**D)** OPTIONS

**Pregunta 5**

¿Qué indica un código de estado **403 Forbidden**?

**A)** La petición fue exitosa.

**B)** El cliente está autenticado, pero no tiene permiso para acceder al
recurso.

**C)** El servidor no existe.

**D)** Falta la autenticación en la petición.

**Pregunta 6**

¿Qué diferencia hay entre **401** y **403**?

**A)** Son exactamente lo mismo.

**B)** 401 indica que falta autenticación y 403 indica que el cliente no
tiene permiso.

**C)** 401 indica error del servidor y 403 indica éxito.

**D)** 401 se usa solo con <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.

**Pregunta 7**

Un log del proxy muestra:

User-Agent: curl/7.68.0

Host: portal-pagos.ejemplo.com

GET /api/clientes

¿Qué interpretación es la más razonable?

**A)** Un usuario navegando con su navegador habitual.

**B)** Una herramienta automatizada consultando una API.

**C)** Un problema con el servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**D)** Una actualización automática de Windows.

**Pregunta 8**

¿Qué aporta la cabecera **SNI** en una conexión <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> para un analista
<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?

**A)** Revela el contenido cifrado de la petición.

**B)** Permite saber a qué dominio se conecta el cliente, aunque el
contenido esté cifrado.

**C)** Oculta la dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen.

**D)** Indica la contraseña del usuario.

**Pregunta 9**

¿Qué tipo de ataque ocurre cuando un atacante inyecta código **SQL**
malicioso en un formulario o en una URL?

**A)** Cross-Site Scripting (XSS).

**B)** SQL Injection (SQLi).

**C)** <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> Amplification.

**D)** SYN Flood.

**Pregunta 10 (Caso práctico <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

El log del proxy muestra que un equipo interno genera tráfico **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> sin
cifrar** hacia un dominio recién registrado, con peticiones **POST** de
gran tamaño hacia Internet.

¿Cuál sería tu primera hipótesis?

**A)** El usuario está navegando normalmente por un sitio legítimo.

**B)** Posible exfiltración de datos o comunicación con un servidor
malicioso.

**C)** Un problema con la resolución <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**D)** Un fallo en el servidor <a href="../../GLOSARIO.md#dhcp" target="_blank">DHCP</a>.

**✅ Respuestas y justificación**

**Pregunta 1**

✅ **Respuesta correcta: A**

**Justificación**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> significa **HyperText Transfer Protocol** (Protocolo de
Transferencia de Hipertexto). Es el protocolo que permite transferir
páginas web entre el cliente y el servidor.

**Pregunta 2**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> escucha normalmente en el puerto **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 80**. El puerto **<a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a> 443**
corresponde a <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, el cual cifra la comunicación con <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>.

**Pregunta 3**

✅ **Respuesta correcta: B**

**Justificación**

<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> es <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> protegido por **<a href="../../GLOSARIO.md#tls" target="_blank">TLS</a>**. Esto cifra el contenido de la
comunicación, garantiza su integridad y autentica al servidor. <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, en
cambio, viaja en texto plano y puede leerse si se intercepta.

**Pregunta 4**

✅ **Respuesta correcta: C**

**Justificación**

Los intentos de login se registran como **POST**, porque ese método se
utiliza para enviar datos al servidor (usuario y contraseña). Una
secuencia de muchos POST a /login sugiere fuerza bruta o relleno de
credenciales.

**Pregunta 5**

✅ **Respuesta correcta: B**

**Justificación**

El **403 Forbidden** indica que el servidor reconoció al cliente pero le
negó el acceso al recurso. No hay permiso, aunque exista autenticación.

**Pregunta 6**

✅ **Respuesta correcta: B**

**Justificación**

- **401 Unauthorized:** falta autenticación. El servidor pregunta "¿quién
  eres?".

- **403 Forbidden:** el cliente está autenticado, pero no tiene permiso.
  El servidor dice "no puedes pasar".

Distinguirlos es fundamental para interpretar ataques y configuraciones
incorrectas.

**Pregunta 7**

✅ **Respuesta correcta: B**

**Justificación**

El **User-Agent** `curl/7.68.0` no corresponde a un navegador, sino a una
herramienta de línea de comandos. Una petición GET con ese User-Agent
hacia una API sugiere acceso automatizado y merece investigación.

**Pregunta 8**

✅ **Respuesta correcta: B**

**Justificación**

El **SNI (Server Name Indication)** es un campo del handshake <a href="../../GLOSARIO.md#tls" target="_blank">TLS</a> que
indica a qué dominio se conecta el cliente. Aunque el contenido esté
cifrado, el analista puede saber el destino de la conexión.

**Pregunta 9**

✅ **Respuesta correcta: B**

**Justificación**

La **SQL Injection (SQLi)** consiste en inyectar código SQL malicioso en
formularios o URLs para manipular la base de datos. El **XSS**, en
cambio, inyecta JavaScript malicioso.

**Pregunta 10**

✅ **Respuesta correcta: B**

**Justificación**

Tráfico **<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> sin cifrar** hacia un **dominio recién registrado**, con
**POST grandes hacia Internet**, es un patrón típico de:

- Exfiltración de datos.

- Comunicación con un servidor de Comando y Control (C2).

- Descarga o envío de datos por malware.

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> deberías investigar:

- La reputación y edad del dominio.

- El proceso que generó el tráfico.

- El volumen y la frecuencia de las peticiones.

- Si otros equipos muestran el mismo comportamiento.

**🏆 Resultado**

| **Respuestas Correctas** | **Nivel**                                                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **10/10**                | ⭐ **Excelente.** Interpretas <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>/<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> y puedes detectar ataques a aplicaciones web en los logs.                                                                     |
| **8–9**                  | 🟢 **Muy buen nivel.** Dominas métodos, códigos de estado y la diferencia entre <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> y <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>.                                                                          |
| **6–7**                  | 🟡 **Buen progreso.** Repasa los códigos de estado y las cabeceras más importantes.                                                                                    |
| **4–5**                  | 🟠 **Necesitas reforzar algunos conceptos.** Revisa la diferencia <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a> vs <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> y los métodos <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>.                                                                    |
| **0–3**                  | 🔴 **Es recomendable repasar el módulo completo.** <a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>/<a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a> son los protocolos que más verás en los logs de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.                                                   |
